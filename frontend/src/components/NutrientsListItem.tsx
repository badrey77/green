import { Heading, Image, List, ListItem, Stack } from "@chakra-ui/react";
import NutrItem from "./NutrItem";
import { FoodDataStruct } from "../utils/types";


const NutrientsListItem = (data : FoodDataStruct) => (
      <Stack display={"contents"}
          spacing={2}
          flexDirection="row"
          justifyContent="flex-start"
          alignItems="center"
          boxShadow={100}
          border="2px solid black.200"
          borderRadius={5}
        >
          <Image
            height="100px"
            width="100px"
            src={ data.food.image }
            borderRadius={100}
          />
          <Stack spacing={2}>
            <Heading as="h6">{ data.food.label}</Heading>
            <List>
                { Object.entries(data.food.nutrients).map(([k,v])=>(<NutrItem key={k} inkey={k} value={v} />)) }
            </List>
          </Stack>
        </Stack>
);

export default NutrientsListItem;