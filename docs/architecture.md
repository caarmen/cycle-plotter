# Architecture

## Top-level packages, with top-level package dependencies
```mermaid
flowchart TD
    entities
    infrastructure
    interfaceadapters
    usecases
    main

    main --> usecases
    main --> interfaceadapters
    interfaceadapters --> infrastructure
    interfaceadapters --> usecases
    usecases --> entities
```

## All packages, with top-level package dependencies
```mermaid
flowchart TD
    entities
    subgraph infrastructure
        files
    end
    subgraph interfaceadapters
        cli
        cycledataparser
    end
    subgraph usecases
        icycledataparser[cycledataparser]
        plotter
    end
    main

    main --> usecases
    main --> interfaceadapters
    interfaceadapters --> infrastructure
    interfaceadapters --> usecases
    usecases --> entities
```

## Packages and modules, with top-level package dependencies
```mermaid
flowchart TD
    subgraph entities
        CycleDuration
    end
    subgraph infrastructure
        subgraph files
            opener
        end
    end
    subgraph interfaceadapters
        subgraph cli
            argparser
        end
        subgraph cycledataparser
            applehealth
            withingshealthmate
            factory
        end
        config
    end
    subgraph usecases
        subgraph icycledataparser[cycledataparser]
            base
        end
        cycle_dates_to_durations
        extract_cycle_durations
        subgraph plotter
            config
            plot_cycle_durations
        end
    end
    main

    main --> usecases
    main --> interfaceadapters
    interfaceadapters --> infrastructure
    interfaceadapters --> usecases
    usecases --> entities
```

## Packages and modules, with module dependencies
```mermaid
flowchart TD
    subgraph entities
        CycleDuration
    end
    subgraph infrastructure
        subgraph files
            opener
        end
    end
    subgraph interfaceadapters
        subgraph cli
            argparser
        end
        subgraph cycledataparser
            applehealth
            withingshealthmate
            factory
        end
        config
    end
    subgraph usecases
        subgraph icycledataparser[cycledataparser]
            base
        end
        cycle_dates_to_durations
        extract_cycle_durations
        subgraph plotter
            pconfig[config]
            plot_cycle_durations
        end
    end
    main

    argparser --> config
    argparser --> pconfig

    applehealth --> opener
    applehealth --> base
    withingshealthmate --> opener
    withingshealthmate --> base

    factory --> config
    factory --> applehealth
    factory --> withingshealthmate
    factory --> base

    main --> argparser
    main --> factory
    main --> base
    main --> extract_cycle_durations
    main --> pconfig
    main --> plot_cycle_durations

    cycle_dates_to_durations --> CycleDuration
    extract_cycle_durations --> CycleDuration
    extract_cycle_durations --> cycle_dates_to_durations
    extract_cycle_durations --> base

    plot_cycle_durations --> CycleDuration
    plot_cycle_durations --> pconfig

```
