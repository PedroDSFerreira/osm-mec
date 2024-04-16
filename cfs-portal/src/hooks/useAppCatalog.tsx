import { ChangeEvent, useState, useEffect } from "react";
import { getAppPkg, newAppPkg, deleteAppPkg } from "../api/appPkg";
import toast from "../utils/toast";
import { AppData } from "../types/Component";

export const useAppCatalog = () => {
    const [appData, setAppData] = useState<AppData[]>([]);
    const [loading, setLoading] = useState(true);
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const [deleteItemId, setDeleteItemId] = useState<string | null>(null);

    useEffect(() => {
        getAppData();
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

    const handleFileUpload = async (e: ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) {
            toast.error('No file selected');
            return;
        }
        const formData = new FormData();
        formData.append('file', file);
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

    return {
        appData,
        loading,
        isDialogOpen,
        handleFileUpload,
        openDialog,
        closeDialog,
        handleDelete,
    };
};
