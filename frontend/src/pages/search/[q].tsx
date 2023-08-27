import { Button, Code, Container, Link, Text, useDisclosure } from "@chakra-ui/react";
import { Main } from '../../components/Main'
import { useRouter } from "next/router";
import axios from 'axios';
import { EditIcon } from "@chakra-ui/icons";
import { get_ingredients_from } from "../../utils/common";
import Dishes from "../../components/Dishes";
import React from "react";
import NutrientsInfo from "../../components/NutrientsInfo";



export async function getServerSideProps(context) {
    try {
      
          const response = await axios.get(`http://127.0.0.1:8000/main/search?q=${context.query.q}`)
          const results = await new Promise((resolve,reject)=>{
            let ret;
            try {
              ret = response.data; 
              resolve(ret)
            }
            catch (error) {
              reject()
            } 
          });
          const list_of_ingredients = get_ingredients_from(results);
          const response2 = await axios.get(`http://127.0.0.1:8000/main/dishes?ingredients=${list_of_ingredients}`,
               {auth: { username: 'admin', password: 'tombraider' }})
          const proposals = response2.data;
          //   });
          // });
          //const results = response.data;
          return { props: { results, proposals } };
    } catch (error) {
      console.error('Error fetching search results:', error);
      return { props: { results: [], proposals: [] } };
    }
  }

const Search = ({ results, proposals }) => {

    const elements = JSON.parse(results);
    const dishes = JSON.parse(JSON.stringify(proposals.results));
    const { isOpen, onOpen, onClose } = useDisclosure()
    const btnRef = React.useRef() 
    const router = useRouter();

    return (
        <Main 
          position={"relative"}
          mt={"100px"}
          padding={"10px"}
        >
          <Container>
            <Text
              color="text" fontWeight={'bold'}>
                Your query <Code>{router.query.q}</Code>
                <Button
                onClick={(e)=>{}}
                border={"none"}
                background={"none"}
                _hover={{}}
                _active={{}}
                >
                  <EditIcon />
                  </Button>
            </Text>
          </Container>
          <Container>
            <Button ref={btnRef} onClick={onOpen}>See Nutrients ({elements.length}){" >"}</Button>
            <NutrientsInfo isOpen={isOpen} onClose={onClose} btnRef={btnRef} elements={elements} />
          </Container> 
          <Container maxW={"2xl"}>
            <Dishes dishes={dishes} />
          </Container>
          <Container  mb={20} >
            <Link href="#">Return to top</Link>
          </Container>
       </Main>
    )
}

export default Search;
