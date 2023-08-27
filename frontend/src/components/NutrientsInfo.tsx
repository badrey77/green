import { Drawer, DrawerBody, DrawerCloseButton, DrawerContent, DrawerFooter, DrawerHeader, DrawerOverlay } from "@chakra-ui/react";
import NutrientsList from "./NutrientsList";
import { FoodDataStruct } from "../utils/types";

const NutrientsInfo = (
    {
        isOpen,
        onClose,
        btnRef,
        elements
    }) => {

    return <Drawer
      isOpen={isOpen}
      placement='right'
      onClose={onClose}
      finalFocusRef={btnRef}
    >
      <DrawerOverlay />
      <DrawerContent>
        <DrawerCloseButton />
        <DrawerHeader>Did you know ?</DrawerHeader>
  
        <DrawerBody>
          <NutrientsList foods={elements} />
        </DrawerBody>
  
        <DrawerFooter>
          {/* <Button variant='outline' mr={3} onClick={(e)=>{}}>
            Cancel
          </Button>
          <Button colorScheme='blue'>Save</Button> */}
        </DrawerFooter>
      </DrawerContent>
    </Drawer>;
  }

  export default NutrientsInfo;