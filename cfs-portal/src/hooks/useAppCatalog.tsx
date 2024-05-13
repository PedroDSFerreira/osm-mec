import { useState, useEffect } from "react";
import { getAppPkg, newAppPkg, deleteAppPkg, instantiateAppPkg } from "../api/appPkg";
import { getVims } from "../api/vim";
import toast from "../utils/toast";
import { AppData, VimData } from "../types/Component";

export const useAppCatalog = () => {
    const [appData, setAppData] = useState<AppData[]>([]);
    const [loading, setLoading] = useState(true);
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const [deleteItemId, setDeleteItemId] = useState<string | null>(null);
    const [vimData, setVimData] = useState<VimData[]>([]);
    const [isFormDialogOpen, setIsFormDialogOpen] = useState(false);
    const [formData, setFormData] = useState<FormData>(new FormData());
    const [rowId, setRowId] = useState<string>('');

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

    const handleFileUpload = async (file: File) => {
        const formData = new FormData();
        formData.append('appd', file);
        try {
            await newAppPkg(formData);
            toast.success('New app created successfully');
            getAppData();
        } catch (error) {
            toast.error('Error creating new app');
        }
    };

    const openDialog = (id: string) => {
        setIsDialogOpen(true);
        setDeleteItemId(id);
    };

    const closeDialog = () => {
        setIsDialogOpen(false);
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
                setIsDialogOpen(false);
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
        isDialogOpen,
        isFormDialogOpen,
        setRowId,
        setFormData,
        handleFileUpload,
        openDialog,
        closeDialog,
        handleDelete,
        openFormDialog,
        closeFormDialog,
        handleInstantiate
    };
};
