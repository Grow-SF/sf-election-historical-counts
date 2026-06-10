import { Suspense } from "react";
import Story from "@/components/Story";

export default function Page() {
  return (
    <Suspense>
      <Story />
    </Suspense>
  );
}
