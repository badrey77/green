import { Box, Button, Code, Container, IconButton, Link, Text } from "@chakra-ui/react";
import { Main } from '../../components/Main'
import { useRouter } from "next/router";
import axios from 'axios';
import ResultsList from "../../components/ResultsList";
import { Banner } from "../../components/Banner";
import { ArrowBackIcon, RepeatIcon } from "@chakra-ui/icons";



export async function getServerSideProps(context) {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/main/search?q=${context.query.q}`);
      const results = response.data;

      return { props: { results } };
    } catch (error) {
      console.error('Error fetching search results:', error);
      return { props: { results: [] } };
    }
  }

const Search = ({ results }) => {

    const elements = JSON.parse(results);
    console.log(`Elements: ${elements}`);
    
    const router = useRouter();
    return (
    <Box height="100vh">
        <Banner />
        <Main 
        position={"relative"}
        margin={"0 auto"}
        padding={"10px"}
        >
            <Text
             color="text">
                Your query <Code>{router.query.q}</Code>
            </Text>
        </Main>
        <ResultsList foods={ elements } />
        <Link
          href="/"
          display={"grid"}
        >
          <Button>
            <ArrowBackIcon color="gray.600" />
          </Button>
        </Link>
    </Box>
    )
    
}

export default Search;