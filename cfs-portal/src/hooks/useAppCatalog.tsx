import { useState, useEffect } from "react";
import { getAppPkg, newAppPkg, deleteAppPkg, instantiateAppPkg, updateAppPkg, getVims } from "../api/api";
import toast from "../utils/toast";
import { AppData, VimData, ActionType } from "../types/Component";

export const useAppCatalog = () => {
    const [appData, setAppData] = useState<AppData[]>([]);
    const [loading, setLoading] = useState(true);
    const [isConfirmationDialogOpen, setIsConfirmationDialogOpen] = useState(false);
    const [deleteItemId, setDeleteItemId] = useState<string | null>(null);
    const [vimData, setVimData] = useState<VimData[]>([]);
    const [isFormDialogOpen, setIsFormDialogOpen] = useState(false);
    const [formData, setFormData] = useState<FormData>(new FormData());
    const [rowId, setRowId] = useState<string>('');
    const [isUploadDialogOpen, setIsUploadDialogOpen] = useState(false);
    const [action, setAction] = useState<ActionType>(ActionType.CREATE);

    useEffect(() => {
        getAppData();
        getVimsData();
    }, []);

    const getAppData = async () => {
        try {
            const { data } = await getAppPkg();
            setAppData(data);
        } catch (error) {
            setAppData([]);
            toast.error('Error fetching app data');
        } finally {
            setLoading(false);
        }
    };

    const getVimsData = async () => {
        try {
            const { data } = await getVims();
            setVimData(data);
        } catch (error) {
            setVimData([]);
            toast.error('Error fetching VIM data');
        }
    };

    const handleFileUpload = async (file: File, action: ActionType) => {
        const formData = new FormData();
        formData.append('appd', file);
        switch (action) {
            case ActionType.CREATE:
                await handleNewAppPkg(formData);
                break;
            case ActionType.UPDATE:
                await handleUpdateAppPkg(formData);
                break;
            default:
                break;
        }
        setIsUploadDialogOpen(false);
    };

    const handleNewAppPkg = async (formData: FormData) => {
        console.log('handleNewAppPkg');
        try {
            await newAppPkg(formData);
            toast.success('New app created successfully');
            getAppData();
        } catch (error) {
            toast.error('Error creating new app');
        }
    };

    const handleUpdateAppPkg = async (formData: FormData) => {
        try {
            await updateAppPkg(rowId, formData);
            toast.success('App updated successfully');
            getAppData();
        } catch (error) {
            toast.error('Error updating app');
        }
    };

    const openConfirmationDialog = (id: string) => {
        setIsConfirmationDialogOpen(true);
        setDeleteItemId(id);
    };

    const closeConfirmationDialog = () => {
        setIsConfirmationDialogOpen(false);
    };

    const handleDelete = async () => {
        if (deleteItemId) {
            try {
                await deleteAppPkg(deleteItemId);
                toast.success('App deleted successfully');
                getAppData();
            } catch (error) {
                toast.error('Error deleting app');
            } finally {
                setIsConfirmationDialogOpen(false);
                setDeleteItemId(null);
            }
        }
    };

    const openFormDialog = () => {
        setIsFormDialogOpen(true);
    }

    const closeFormDialog = () => {
        setIsFormDialogOpen(false);
    }

    const handleInstantiate = async (id: string, formData: FormData) => {
        try {
            await instantiateAppPkg(id, formData);
            toast.success('App instantiated successfully');
            getAppData();
        } catch (error) {
            toast.error('Error instantiating app');
        }
    }

    return {
        appData,
        vimData,
        formData,
        rowId,
        loading,
        isConfirmationDialogOpen,
        isFormDialogOpen,
        isUploadDialogOpen,
        action,
        setAction,
        setIsUploadDialogOpen,
        setRowId,
        setFormData,
        handleFileUpload,
        openConfirmationDialog,
        closeConfirmationDialog,
        handleDelete,
        openFormDialog,
        closeFormDialog,
        handleInstantiate
    };
};
