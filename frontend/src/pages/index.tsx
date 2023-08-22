import {
  Link as ChakraLink,
  Text,
  Code,
  List,
  ListIcon,
  ListItem,
} from '@chakra-ui/react'
import { CheckCircleIcon, LinkIcon } from '@chakra-ui/icons'

import { Hero } from '../components/Hero'
import { Container } from '../components/Container'
import { Main } from '../components/Main'
import { DarkModeSwitch } from '../components/DarkModeSwitch'
import { CTA } from '../components/CTA'
import { Footer } from '../components/Footer'
import { SearchBar } from '../components/SearchBar'

const Index = () => (
  <Container height="100vh">
    <Hero />
    <Main>
      <Text color="text">
        You can now search for <Code>Food</Code> or <Code>Restaurants</Code> and customize{' '}
        <Code>your orders</Code>.
      </Text>

      <List spacing={3} my={0} color="text">
        <ListItem>
          <ListIcon as={CheckCircleIcon} color="green.500" />
          <ChakraLink
            isExternal
            href="https://chakra-ui.com"
            flexGrow={1}
            mr={2}
          >
            Trends <LinkIcon />
          </ChakraLink>
        </ListItem>
        <ListItem>
          <ListIcon as={CheckCircleIcon} color="green.500" />
          <ChakraLink isExternal href="https://nextjs.org" flexGrow={1} mr={2}>
            Lucky Me ! <LinkIcon />
          </ChakraLink>
        </ListItem>
      </List>
      <SearchBar />
    </Main>

    <DarkModeSwitch />
    <Footer>
      <Text>We Love ❤️ Food !</Text>
    </Footer>
    <CTA />
  </Container>
)

export default Index
