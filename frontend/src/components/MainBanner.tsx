import { Box, Button, Link, Stack, Text } from "@chakra-ui/react";

const MainBanner = () => (
    <Stack
        position={"fixed"}
        top={0} 
        zIndex={"100"}   
    >
        <Box boxShadow={"base"} display={"flex"} background={"green.700"} w={"100vw"}>
        <Link
            href="/"
            _hover={{}}
        >
            <Stack bg={"green"} padding={".5em"} w={"7em"} >
                <Text fontWeight={"bold"} fontFamily={"Copperplate, Papyrus, fantasy"} textColor={"white"}>MAKE IT</Text>
                <Text fontWeight={"bold"} fontFamily={"Copperplate, Papyrus, fantasy"} textColor={"white"}>MYSELF</Text>
            </Stack>
        </Link>
        <Box 
        w={0} 
        h={0} 
        borderTop={"70px solid green"} 
        borderRight={"70px solid transparent"} 
        />
        <Box
            display={"flex"}
            w={"full"} 
            justifyContent={"flex-end"} 
            paddingRight={"4em"} 
            >
            <Stack alignItems={"center"} spacing={"3"} direction={"row"} padding={3}>
            <Button bg={"orange"} _hover={{ background: "orange.600", color: "white" }} textColor={"white"}>Home</Button>
            <Button bg={"green.700"} _hover={{ background: "orange.600", color: "white" }} textColor={"white"}>About</Button>
            <Button bg={"green.700"} _hover={{ background: "orange.600", color: "white" }} textColor={"white"}>Contact us</Button>
            </Stack>
        </Box>
        </Box>
    </Stack>
)

export default MainBanner;