import React from "react";
import {
  ChakraProvider,
  Flex,
  Heading,
  List,
  Stack,
  Image
} from "@chakra-ui/react";

import  NutrItem from './NutrItem';

const SearchResults = () => (
<Flex flexDirection="column">
      <Heading>Search Results:</Heading>
      <List display="block">
        <Stack
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
            src="https://www.allrecipes.com/thmb/AtViolcfVtInHgq_mRtv4tPZASQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/ALR-187822-baked-chicken-wings-4x3-5c7b4624c8554f3da5aabb7d3a91a209.jpg"
            mr={30}
            borderRadius={100}
          />
          <Stack spacing={2}>
            <Heading as="h6">Chicken Wings</Heading>
            <List>
              <NutrItem txt={"Cal: 87"} />
              <NutrItem txt={"Prot: 165"} />
            </List>
          </Stack>
        </Stack>
        <Stack
          spacing={2}
          flexDirection="row"
          alignItems="center"
          boxShadow={100}
          border="2px solid black.200"
          borderRadius={5}
        >
          <Image
            height="100px"
            width="100px"
            src="https://nourishedkitchen.com/wp-content/uploads/2018/10/fermented-hot-sauce-recipe.jpg"
            borderRadius={100}
            mr={30}
          />
          <Stack spacing={2}>
            <Heading as="h6">Hot Sauce</Heading>
            <List>
              <NutrItem txt={"Cal: 154"} />
              <NutrItem txt={"Prot: 69"} />
            </List>
          </Stack>
        </Stack>
        <Stack
          spacing={2}
          flexDirection="row"
          alignItems="center"
          boxShadow={100}
          border="2px solid grey.200"
          borderRadius={5}
        >
          <Image
            height="100px"
            width="100px"
            borderRadius={100}
            src="https://media.gettyimages.com/id/154947469/fr/photo/rouge-gel%C3%A9e.jpg?s=612x612&w=gi&k=20&c=VaUaYbMDJUWIFDqhYW6Kt9Xyt-ywrlWagNwnkYD0hrk="
            mr={30}
          />
          <Stack spacing={2}>
            <Heading as="h6">Jelly</Heading>
            <List>
              <NutrItem txt="Cal: 100" />
              <NutrItem txt="Prot: 200" />
            </List>
          </Stack>
        </Stack>
      </List>
    </Flex>
);

export default SearchResults;