import { Code, Container, Text } from "@chakra-ui/react";
import { Hero } from "../../components/Hero";
import { Main } from '../../components/Main'
import { useRouter } from "next/router";
import axios from 'axios';
import ResultsList from "../../components/ResultsList";
import { useState } from "react";



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

    const foods = results;
    const router = useRouter();
    return (
    <Container height="100vh">
        <Hero />
        <Main>
            <Text color="text">
                Your query <Code>{router.query.q}</Code>
            </Text>
        </Main>
        <ResultsList elements={ foods }/>
    </Container>
    )
    
}

export default Search;