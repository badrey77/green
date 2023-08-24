export type FoodDataStruct = {
    food : {
        foodId: string,
        label: string,
        image: string,
        nutrients: {
            ENERC_KCAL: number,
            PROCNT: number, 
            FAT: number, 
            CHOCDF: number, 
            FIBTG: number
        }
    }
};