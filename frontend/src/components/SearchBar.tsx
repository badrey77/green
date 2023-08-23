import React, { ReactElement, ReactNode, useState } from "react";
import { Link as ChakraLink } from "@chakra-ui/react";
import {
  Button,
  Input,
  InputGroup,
  InputLeftElement,
  InputRightAddon
} from "@chakra-ui/react";
import { Search2Icon } from "@chakra-ui/icons";
import { useRouter } from "next/router";

export const SearchBar = () => {

    const router = useRouter()

    const [ query, setQuery ] = useState('');

    return (
        <>
            <InputGroup borderRadius={5} size="sm">
            <InputLeftElement
                pointerEvents="none"
                children={<Search2Icon color="gray.600" />}
            />
            <Input onChange={(e)=>setQuery(e.target.value)} type="text" placeholder="Search..." border="1px solid #949494" />
            <InputRightAddon
                p={0}
                border="none"
            >
            <Button
                variant="solid"
                colorScheme="green"
                rounded="button"
                flexGrow={3}
                mx={2}
                size="sm" 
                borderLeftRadius={0} 
                borderRightRadius={3.3} 
                border="1px solid #949494"
                onClick={()=>router.push('/search/'+query)}
            >
                Search
            </Button>
            </InputRightAddon>
            </InputGroup>
        </>
        );
};