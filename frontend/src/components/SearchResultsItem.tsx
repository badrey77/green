"use client";
import { Heading, Image, List, ListItem, Stack } from "@chakra-ui/react";
import NutrItem from "./NutrItem";
import { FoodDataStruct } from "../utils/types";


const SearchResultsItem = (data : FoodDataStruct) => (
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
            mr={30}
            borderRadius={100}
            alignSelf={"center"}
          />
          <Stack spacing={2}>
            <Heading width={"200px"} as="h6">{ data.food.label}</Heading>
            <List>
                { Object.entries(data.food.nutrients).map(([k,v])=>(<NutrItem inkey={k} value={v} />)) }
            </List>
          </Stack>
        </Stack>
);

export default SearchResultsItem;