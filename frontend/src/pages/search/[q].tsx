import { Box, Button, Code, Collapse, Container, Flex, IconButton, Link, Text, border, useDisclosure } from "@chakra-ui/react";
import { Main } from '../../components/Main'
import { useRouter } from "next/router";
import axios from 'axios';
import NutrientsList from "../../components/NutrientsList";
import { ArrowBackIcon, EditIcon, RepeatIcon } from "@chakra-ui/icons";
import MainBanner from "../../components/MainBanner";
import { get_ingredients_from } from "../../utils/common";
import Dishes from "../../components/Dishes";



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
    const { isOpen, onToggle } = useDisclosure()  
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
            <Button onClick={onToggle}>See Nutrients ({elements.length}){" >"}</Button>
            <Collapse in={isOpen} animateOpacity>
              <Box
                p='40px'
                color='white'
                mt='4'
                bg='teal.500'
                rounded='md'
                shadow='md'
              >
                <NutrientsList foods={ elements } />
              </Box>
            </Collapse>
          </Container> 
          <Container>
          <Box>
            <Dishes dishes={dishes} />
          </Box>
          </Container>
       </Main>
    )
}

export default Search;