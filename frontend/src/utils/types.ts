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

export type DishType = {
    id: number,
    label: string,
    description: string,
    img: string,
    price: number,
    ingredients: Array<string>
}