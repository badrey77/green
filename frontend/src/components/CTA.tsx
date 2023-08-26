import { Link as ChakraLink, Button, Box } from '@chakra-ui/react'

import { Container } from './Container'

export const CTA = () => (
  <Box
    position="fixed"
    bottom={0}
    width="full"
    py={3}
    bgColor={"white"} 
  >
    <Container bgColor={"white"} width={"full"} flexDirection={"row"} alignItems={"stretch"} justifyContent={"space-around"} flexFlow={"wrap"} >
    <Button
      as={ChakraLink}
      isExternal
      href="https://chakra-ui.com"
      variant="outline"
      colorScheme="green"
      rounded="button"
      flexGrow={1}
      width="48vw"
      mx={2}
    >
      Where is my order ?
    </Button>
    <Button
      as={ChakraLink}
      isExternal
      href="https://github.com/vercel/next.js/blob/canary/examples/with-chakra-ui"
      variant="solid"
      colorScheme="green"
      rounded="button"
      flexGrow={1}
      width="48vw"
      mx={2}
    >
      Quick Meal !!!
    </Button>
    </Container>
  </Box>
)
