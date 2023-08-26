import { Flex, Heading, Box } from '@chakra-ui/react'

export const Hero = ({ title }: { title: string }) => (
  <Flex
    justifyContent="center"
    alignItems="center"
    height="10vh"
    bgGradient="linear(to-l, heroGradientStart, heroGradientEnd)"
    bgClip="text"
    mt={"10vh"}
  >
    <Box>
      <Heading fontSize="2vw">{title}</Heading>
    </Box>
    
  </Flex>
)

Hero.defaultProps = {
  title: 'Make it Myself !',
}
