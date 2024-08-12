# po Framework Documentation

## Welcome to po

**po** is your go-to framework for creating stunning parallax websites effortlessly. Inspired by the expressive and declarative style of Flutter's VelocityX, **po** abstracts away the complexities of web development into a high-level syntax that makes building interactive and visually captivating web experiences easy and enjoyable.

## Why Parallax?

Parallax effects enhance user engagement by creating a sense of depth, making background elements move at different speeds compared to foreground elements. Implementing parallax manually involves intricate coding. **po** simplifies this process, enabling you to focus on design and creativity.

## Getting Started

### Installation

Install the **po** CLI tool to get started:

```bash
npm install -g po-cli
```

## Project Structure
Here’s how your po project will be structured:


```bash
my-po-project/
│
├── src/
│   ├── index.po        # Main `po` DSL file
│   ├── components/     # Custom components
│   │   └── MyComponent.po
│   └── styles.po      # Global styles
│
├── dist/
│   ├── index.html      # Compiled HTML
│   ├── styles.css      # Compiled CSS
│   └── scripts.js      # Compiled JavaScript
│
├── po.config.js        # Configuration file
└── README.md           # Documentation
```

## Writing Your First po Code
Here's a simple example using po DSL to create a parallax section with a fluent, chainable syntax:

```
Page {
  Section {
    ParallaxImage src="background.jpg" speed=0.5
    Container {
      Text content="Welcome to `po`".white.xl4.bold.center.makeCentered()
      Button text="Learn More".roundedLg.red500.shadow2xl.make()
      .action("showMoreInfo")
    }
  }
}
```

## Predefined Widgets
po provides a set of predefined widgets to streamline your development:

**Page:** The primary container for your site.

**Section:** A section within the page.

**ParallaxImage:** Image with a parallax effect.

**Text:** For displaying text content.

**Button:** Interactive button element.

**Container:** Flexible container for grouping elements.

## Extensible Architecture
po allows you to extend its functionality:

### Creating a Custom Component:

```
Component MyComponent {
  Text content="Custom Component".customStyle()
}
```
### Using the Custom Component:
```
Page {
  MyComponent
}
```

## Importing Packages
You can easily import and use packages developed by others:

### Importing a Package:
```
import { CustomWidget } from 'custom-package'

Page {
  CustomWidget
}
```
## Creating and Using a Plugin:
Create a plugin to enhance your project:

### Plugin Example (my-plugin.po):
```
Plugin MyPlugin {
  ParallaxImage src="plugin-background.jpg" speed=0.7
}
```
## Using the Plugin:
```
import { MyPlugin } from './plugins/my-plugin.po'

Page {
  MyPlugin
}
```

## Compile and Run
Use a single command to compile and run your project:

```bash
po run
```
This command compiles your po code into HTML, CSS, and JavaScript, and starts a local server for previewing your site.

## Syntax and Style
**po** employs a chainable, fluent syntax for a clean and expressive design experience:

Example Syntax:

```
Page {
  Section {
    ParallaxImage src="hero.jpg" speed=0.3
    Text content="Experience Depth".white.xl4.bold.center.makeCentered()
    Button text="Discover More".roundedLg.blue500.shadow2xl.make()
    .action("explore")
  }
}
```
In this example, po provides an intuitive, chainable syntax for defining styles and behaviors, allowing for a fluid and readable code structure.

## Conclusion
po makes creating parallax websites straightforward with a declarative, chainable syntax that simplifies the development process. It enables you to focus on designing engaging web experiences with minimal effort.

**Happy coding with po!**



