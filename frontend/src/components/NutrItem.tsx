import { ListItem } from "@chakra-ui/react";

const NutrItem = ({ inkey, value }) => (
    <ListItem>
      <span role="img" aria-label="dish">&#x2022;</span>{" "}<strong>{ inkey }:{" "}</strong>{ value }
    </ListItem>
  );

  export default NutrItem;