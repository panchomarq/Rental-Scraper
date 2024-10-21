import { useState } from 'react';
import { Container, Burger } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';

const links = [
  { link: '/about', label: 'Features' },
  { link: '/pricing', label: 'Pricing' },
  { link: '/learn', label: 'Learn' },
  { link: '/community', label: 'Community' },
];

export function HeaderSimple() {
  const [opened, { toggle }] = useDisclosure(false);
  const [active, setActive] = useState(links[0].link);

  const items = links.map((link) => (
    <a
      key={link.label}
      href={link.link}
      className={`block px-3 py-2 rounded-md text-base font-medium ${
        active === link.link ? 'text-blue-500' : 'text-gray-600 hover:text-blue-500'
      }`}
      data-active={active === link.link || undefined}
      onClick={(event) => {
        event.preventDefault();
        setActive(link.link);
        toggle(); // Close menu on link click
      }}
    >
      {link.label}
    </a>
  ));

  return (
    <header className="bg-white shadow">
      <Container size="md" className="flex justify-between items-center py-4">
        <div className="hidden md:flex flex-1 justify-center space-x-4">{items}</div>
        <div className="md:hidden">
          <Burger
            opened={opened}
            onClick={toggle}
            className="text-gray-500 focus:outline-none"
            size="sm"
          />
        </div>
      </Container>
      {opened && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1">{items}</div>
        </div>
      )}
    </header>
  );
}
