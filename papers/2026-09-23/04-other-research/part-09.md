# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-463](./part-10.md)

---

### 401. [Structure-Aware Rendering: How Code Reveal Shapes Programmers' Visual Attention](https://arxiv.org/abs/2609.24616)

**<font color=#1a73e8>作者：</font>** Xiaotian Su, Jan Brasser, David Robert Reich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI coding interfaces present generated code either all at once or token-by-token. These rendering strategies reflect model generation rather than how programmers actually read code: selectively, non-linearly, and guided by the structure. We argue that code rendering is a first-class interaction primitive that shapes how programmers read and understand code. To explore this design space, we introduce structured rendering, a technique that reveals code in semantically meaningful chunks derived from its syntactic hierarchy, exposing high-level structure before low-level details. To isolate rendering effects on visual attention, we conducted an eye-tracking study with 53 participants comparing static, character-based, and structured rendering. Our findings show that rendering alters visual attention and reading behavior: dynamic rendering induces fewer but longer fixations and more sustained focus, while structured rendering further guides attention toward semantically meaningful units and supports high-level understanding. We release the anonymized dataset with an interactive demo (this https URL) to support future research.

---


### 402. [Ascent: An Agentic System over the Model Context Protocol for Real-World Clinical Data Analysis](https://arxiv.org/abs/2609.24620)

**<font color=#1a73e8>作者：</font>** Angelo Ziletti, Leonardo D'Ambrosi, Melanie Tuchardt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Answering epidemiological questions from real-world clinical data requires medical coding, schema-aware SQL, and validation of implicit choices about populations, denominators, and time. We present Ascent, an agentic system that exposes medical coding, question answering, and cohort analysis through a shared Model Context Protocol tool surface for standardized and native schemas. We introduce EpiTrap, a dataset testing whether systems avoid recognized pharmacoepidemiological errors, and compare a fixed pipeline with agents across models and orchestrators. With capable models, agents improve accuracy over the fixed pipeline by an average of 27 and 20 percentage points on native and standardized schemas, respectively. These gains require more tool calls and longer runtimes. Experience from real projects highlights the system's value for feasibility assessment, diagnostic iteration, and expert-guided analysis.

---


### 403. [Custom Named Entity Recognition and Topic Classification for Global Health Publications](https://arxiv.org/abs/2609.24625)

**<font color=#1a73e8>作者：</font>** Genis Skura, Antoine Geissbühler, Jean-Luc Falcone  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How should natural language processing models be selected and adapted for global health literature in environments where annotated data and computational resources are limited? This thesis investigates these challenges through experiments on semantic tag discovery, named entity recognition (NER), and multi-label topic classification. First, skip-gram word2vec models trained on progressively larger specialized corpora are compared with BioWordVec to assess how corpus size and domain context influence tag discovery. Vocabulary coverage and qualitative evaluation indicate that broader coverage does not necessarily yield more useful domain-specific associations. The analysis then turns to entity extraction, comparing convolutional spaCy models with a RoBERTa-based transformer on 1,000 annotated sentences. Under a lenient scoring protocol, the transformer achieves 0.80 micro-F1 versus 0.65-0.69 for convolutional models, but takes 82 seconds rather than 5-6 seconds. This trade-off motivates fine-tuning convolutional models and integrating a disease recognizer that achieves 81.33% test F1 on the NCBI Disease Corpus. Combined with PDF preprocessing, entity filtering, and MeSH enrichment, the resulting pipeline supports document-level indexing. To complement entity extraction with thematic annotation, MiniLM-based few-shot classification is compared with BART-MNLI zero-shot inference across 50 topics and 1,000 handcrafted test sentences. BART-MNLI achieves 95.2% single-label accuracy versus 59%; reported multi-label accuracies are 88% and 32% under partly manual assessment. However, its higher inference cost limits practical integration. The results show where domain specialization and lightweight adaptation offer practical value, and where transformer accuracy justifies higher inference costs, providing an empirical basis for building knowledge systems under resource constraints.

---


### 404. [Relationally Grounded Latent World Models for Autonomous Driving](https://arxiv.org/abs/2609.24626)

**<font color=#1a73e8>作者：</font>** Fabian Schmidt, Markus Enzweiler, Abhinav Valada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models learn predictive representations for autonomous driving, but the relational semantics these states preserve often remain implicit. We investigate whether traffic scene graphs can serve as privileged semantic supervision for latent world representations. Building on LAW, we construct actor-centric scene graphs from nuScenes 3D annotations, encode their serialized relational structure using a frozen text embedding model, and align the visual latent representations with this semantic target during training. We remove the supervision branch at inference, so it requires neither scene graphs nor 3D annotations and adds no test-time computation. On nuScenes, our method reduces average trajectory L2 error from 0.661 to 0.622 (5.9%) and collision rate from 0.456 to 0.217 (52.4%) relative to our retrained LAW baseline. It also outperforms an unstructured caption-style semantic target, supporting the benefit of explicit relational structure for latent world-model representation learning.

---


### 405. [FedMust: Semi-supervised Multi-task Student-Teacher Federated Learning for Multi-organ CT Segmentation](https://arxiv.org/abs/2609.24627)

**<font color=#1a73e8>作者：</font>** Ashkan Moradi, Bendik Skarre Abrahamsen, Mattijs Elschot  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-organ segmentation using deep learning requires large amounts of annotated patient data; however, institutions often lack sufficiently large and diverse annotated datasets. Privacy constraints further prevent institutions from sharing patient data to overcome this limitation. Moreover, due to the labor-intensive nature of annotation and the scarcity of diverse expertise, institutions typically have labels for only a small portion of their local data, leaving the larger unlabeled portion unused. In this work, we propose a flexible semi-supervised federated multi-task student-teacher framework that leverages federated learning (FL) to improve multi-organ segmentation using both labeled and unlabeled data across participating sites. At each communication round, the proposed framework initiates local training, where clients with labels for the same task form a federation to produce an aggregated teacher model. The resulting teachers generate task-specific features for all data at each client. Subsequently, all clients form a second federation to train a multi-task student model with a shared encoder and task-specific decoders that replicate the teacher-generated features across all segmentation tasks. The aggregated student model is then used to update the local teachers and initiate the next training round. Extensive experiments demonstrated the effectiveness of the proposed method compared with local and federated single-organ models, yielding an average performance gain of 13 percent across clients. The experiments also demonstrated the impact of multi-task learning and unlabeled data and the applicability of the framework in relaxing labeled-data requirements for client participation. The code is available at this https URL.

---


### 406. [High-resolution Nitrogen Dioxide Maps Reveal Exposure Limit Breaches across Europe](https://arxiv.org/abs/2609.24634)

**<font color=#1a73e8>作者：</font>** Linus Scheibenreif, Konrad Schindler  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nitrogen dioxide (NO2) is a common air pollutant, released into the atmosphere through the incomplete burning of fossil fuels, and associated with respiratory and cardiovascular diseases in humans. Ambient NO2 concentrations are regulated through air-quality limits assessed with a sparse network of fixed monitors. The revised EU Ambient Air Quality Directive (2024/2881) introduces a daily NO2 limit to be met from 2030. At present, neither the regulatory monitoring network nor existing coarse, annual-mean models can resolve NO2 concentrations at the spatio-temporal resolutions necessary to assess compliance. Here we map NO2 across Europe at hourly and 10m resolution with a machine-learning model that combines ground monitors with satellite, reanalysis, land-use, traffic and emission data and returns a calibrated predictive distribution at every location. Validated against held-out regulatory monitors and independent citizen-science campaigns, the maps resolve high-resolution spatiotemporal NO2 gradients for 110 metropolitan areas in Europe. We reconstruct the daily compliance statistic across those regions and find limit breaches in 91 EU air quality zones deemed compliant by the regulatory monitoring network, covering a population of approximately 135M. Beyond air quality zones and monitor locations, an estimated 9-9.4% (20M) of the population in mapped regions lives in areas where the daily NO2 limit is breached. The high-resolution maps offer a route to population-scale assessment of compliance with the 2030 limits.

---


### 407. [Corrective Forcing: Unified Post-Training for Diffusions and Flows in Generative Speech Enhancement](https://arxiv.org/abs/2609.24651)

**<font color=#1a73e8>作者：</font>** Qing Yao, Lijian Gao, Qirong Mao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow models, as promising generative paradigms for speech enhancement, face a training--inference mismatch: training uses analytical path states, whereas inference recursively evaluates models on self-generated rollout states along discretized sampling trajectories. This mismatch causes prediction and discretization errors to accumulate. To address it, we introduce Corrective Forcing (CoF), a post-training paradigm that forces diffusion and flow models to learn from self-generated rollouts and correct their predictions. CoF corrects clean-speech predictions on rollout states toward the ground truth under dynamic sampling schedules, exposing the model to varying inference conditions. It further regularizes local evolution using locally corrected counterfactual transitions as references for factual transitions. By expressing model outputs through a shared clean-speech prediction parameterization, CoF applies the same post-training objective across diffusion and flow formulations. Experiments with SB-VE and OT-CFM demonstrate improvements in perceptual quality and reconstruction fidelity, together with robust performance across different numbers of sampling steps.

---


### 408. [5G-Shark: A Network Security Auditor for 5G Subscriber Privacy and Unauthenticated Signalling Resilience](https://arxiv.org/abs/2609.24656)

**<font color=#1a73e8>作者：</font>** Oscar Lasierra, Gines Garcia-Aviles, Antonio Skarmeta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The fifth generation of mobile networks was standardised with an explicit mandate to close long-standing privacy and security gaps, mandating the concealment of the subscriber's permanent identity, resistance to generational downgrade, and protection against location tracking. Assessing whether these guarantees hold in operational networks, however, requires separating two sources of residual exposure that prior studies do not distinguish and do not evaluate in the wild: protocol-design limitations, which remain exploitable even against a fully specification-compliant deployment, and implementation gaps, which arise from incomplete or non-compliant implementations. We present 5G-Shark, a security assessment tool and methodology that turns a legitimate mobility procedure against the subscriber. Rather than relying on active jamming or malformed-packet injection, 5G-Shark manipulates the standardised cell-reselection criterion to pull a target User Equipment onto a self-created rogue cell, establishing an attack vantage with minimal service disruption. Then, the proposed methodology effectively performs the required interactions to expose the security risks of the system under test, classifying them into the aforementioned categories. Built solely from open-source stacks and Software Defined Radio hardware and evaluated against commercial 5G Standalone deployments, 5G-Shark requests subscriber identifiers, forces Radio Access Technology downgrade via crafted Registration Reject codes, and induces denial-of-service states. For each vector, we attribute the root cause to protocol design or deployment non-compliance. We further provide empirical evidence that in several commercial deployments, temporary identifiers are re-allocated in near-sequential steps that keep successive values linkable, a weakness that enables persistent user tracking despite correct subscriber ID concealment.

---


### 409. [Beyond Endpoint Performance: Process-Level Evaluation of Self-Evolving Agents](https://arxiv.org/abs/2609.24663)

**<font color=#1a73e8>作者：</font>** Hongqiang Lin, Chao Liu, Xiaofan Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents convert interaction feedback into persistent artifacts, such as memories or skills, which in turn guide subsequent decisions. As these artifacts are iteratively updated throughout an experience stream, the capabilities they support may evolve. Consequently, endpoint performance alone offers an incomplete view of self-evolution. Process-level evaluation is therefore essential to identify when a target capability emerges and whether later updates strengthen, preserve, or weaken it. Motivated by this, we propose \textsc{EvoPathBench}, a benchmark that tracks individual capabilities during artifact-level self-evolution. EvoPathBench fixes the base model, tools, freezes evolving artifacts at successive checkpoints, and evaluates the target capability on held-out episodes. This benchmark evaluates agent self-evolution using public trading data and calibrated trajectories. It tests three capabilities: generalization to unseen tasks, retention after unrelated learning, and rule adaptation to new evidence. Experimental results show that gains on similar unseen tasks often weaken under distribution shift, retention losses are concentrated in a minority of evolution paths, and no method achieves reliable rule adaptation. Moreover, while self-evolution enables agents to generate candidate artifacts with substantial held-out gains, the selected updates consistently fall short of realizing this potential. Together, these findings establish capability-level process evaluation as a foundation for analyzing self-evolution, identifying candidate evaluation and selection as key targets for improvement.

---


### 410. [Ev-YOLO: Uncertainty-Aware Object Detection via a Unified Evidential Formulation](https://arxiv.org/abs/2609.24668)

**<font color=#1a73e8>作者：</font>** Simon Barbarit-Gaboriau, Hind Laghmara, Rémi Boutteau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is essential for deploying object detectors in autonomous systems operating in uncertain environments. Evidential Deep Learning (EDL) provides a principled framework for uncertainty-aware classification by representing network outputs as evidence and interpreting predictions through subjective logic. However, existing evidential object detectors typically combine evidential classification with regression uncertainty models that do not share the same theoretical foundation. In this work, we propose an evidential version of YOLOv8 in which both classification and bounding-box regression are formulated within a common evidential framework. Our approach exploits YOLOv8's distribution-based bounding-box representation, allowing the evidential formulation to be applied not only to classification but also to localisation. As a result, both tasks produce belief, uncertainty, and probability estimates that can be interpreted within the Dempster--Shafer framework. Experiments on KITTI, MUSES, and nuScenes show that the resulting detector remains broadly competitive with standard YOLOv8 in terms of detection accuracy while providing a localisation uncertainty that effectively discriminates between correct and erroneous detections. Moreover, this uncertainty becomes increasingly discriminative under domain shift.

---


### 411. [Trust in Edge-Enabled IoT Security: Features, Challenges and Research Directions](https://arxiv.org/abs/2609.24669)

**<font color=#1a73e8>作者：</font>** Esin Ece Aydın, Şerif Bahtiyar, Gürkan Gür  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Providing autonomous intelligence, pervasive connectivity and usability to human life and industry has led to the emergence of the Internet of Things (IoT). To support time-sensitive and resource-constrained applications, IoT systems nowadays increasingly rely on edge computing. This brings computation and decision-making closer to end devices. In edge-enabled IoT architecture, latency and communication overhead are reduced, but interactions among a larger and more diverse set of devices, edge nodes, services, and data sources are introduced as well. In such environments, security and privacy mechanisms provide the foundation for protection, while trust management can assess the reliability of interacting entities and adapting secure decisions. In this paper, we systematically review the current state of trust management in edge-enabled IoT. To this end, we propose a comprehensive taxonomy that maps physical, network, and application architectural IoT layers against the consumer, commercial, industrial, and infrastructure IoT domains. We further investigate state-of-art research based on their trust design, how trust integrated into secure IoT operations, the attacks that effect trust management process. Based on these findings, we identify key gaps in current research and outline future directions for context-aware and adaptive trust management in edge-enabled IoT.

---


### 412. [Muon Can Outperform Dedicated Continual Learning Methods](https://arxiv.org/abs/2609.24678)

**<font color=#1a73e8>作者：</font>** Sebastian George Sincari, Bogdan Alexandru Gheorghe, Antonio Barbalau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning with Low-Rank Adapters (LoRA) typically mitigates forgetting by penalizing the overlap between a new update and the accumulated past weights, which discourages certain update directions without controlling how an update distributes its energy over the ones that remain. We ask whether that restriction has to be task-aware, or whether a generic one supplied by the optimizer is enough. We train a plain incremental LoRA (IncLoRA) with Muon, which orthogonalizes each update, and compare it against O-LoRA and ELLA over five seeds and three task orders on the Standard CL Benchmark and three seeds on TRACE. IncLoRA+Muon reaches the accuracy band of the dedicated methods on Standard CL and improves on every AdamW configuration on TRACE. One update-constraining mechanism is enough, whether it comes from the loss or from the optimizer; on Standard CL a second one does not help, and for the most restrictive method it costs 8.4 points of accuracy and the plasticity to fit each task. What separates the two optimizers is not the size of the update, which under Muon is 0.91 to 2.06 times that under AdamW, but how it is distributed. AdamW confines it to between 1.4 and 1.8 effective singular directions, Muon spreads it over 7.0, and the two do not overlap in any tracked run. Part of the advantage usually attributed to dedicated CL methods may therefore be explained by the geometry of the optimizer's updates.

---


### 413. [Guaranteed Low-Rank Tensor Recovery from Modewise Measurements via Normalized Block-Weighted Riemannian Gradient Descent](https://arxiv.org/abs/2609.24679)

**<font color=#1a73e8>作者：</font>** Yushi Zhou, Feng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the recovery of low-multilinear-rank tensors from linear measurements and propose an adaptive block-weighted modewise Riemannian gradient descent method. The method combines memory-efficient modewise measurements with a normalized adaptive weighting strategy for the core and factor components of the Riemannian gradient. The weighting improves convergence without increasing the multilinear-rank bound of the search direction or the size of the reduced core used for retraction. Under the tensor restricted isometry property and a suitable initialization, we establish local linear convergence and derive sampling guarantees for sub-Gaussian and subsampled orthogonal with random sign (SORS) measurements. Numerical experiments on synthetic low-Tucker-rank tensors show that the proposed method reduces iteration counts and computational time while maintaining reliable recovery performance, especially near the recovery threshold and for structured SORS measurements.

---


### 414. [Domain Specific Post Quantum Signatures for Blockchains](https://arxiv.org/abs/2609.24689)

**<font color=#1a73e8>作者：</font>** Maja Lie, Ben Marsh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchains need more than post quantum single signer signatures. They need consensus profiled authentication objects with canonical bytes, priced invalid input rejection, stable transaction identifiers, hybrid downgrade resistance, public aggregation, merge semantics, accountable signer evidence, forward secure committee rotation, and light client consequences. We argue for domain specific post quantum signatures for blockchain roles, analogously to how hash function engineering produced domain specific primitives for hash table DoS and arithmetized proof systems. We formalize transaction authorization and quorum certificate requirements, instantiate them on Bitcoin, Ethereum, and a Sei Giga style high throughput BFT stress profile, and evaluate ML-DSA, SLH-DSA, Falcon/FN-DSA, HAWK, MAYO, SNOVA, UOV/QR-UOV, FAEST, SQIsign, LaBRADOR Falcon, Squirrel, Chipmunk, and DKKW/LeanSig. The conclusion is blunt. NIST single signer signatures are necessary components, although none of the current schemes is a drop in replacement for the signature layer of modern public blockchains. The missing object is a consensus ready post quantum signature profile, not another generic size table.

---


### 415. [What Makes a Good Medical Image Tokenizer? Rethinking Reconstruction and Generation in Medical Image Tokenization](https://arxiv.org/abs/2609.24691)

**<font color=#1a73e8>作者：</font>** Niklas Bubeck, Yundi Zhang, Vasiliki Sideri-Lampretsa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models now dominate medical image generation, and every such pipeline rests on a \emph{tokenizer} that compresses images into the latent codes for image generation to operate on. Thereby, the tokenizer choice bounds every downstream task from reconstruction fidelity and generation quality to the representations available for downstream analysis. Yet, medical imaging pipelines routinely utilize tokenizers from natural imaging on the hypothesis that their behavior carries over. However, this is an assumption never tested in the medical imaging regime, where datasets are orders of magnitude smaller and images exhibit far lower inter-sample variance. We present a systematic evaluation of medical image tokenizers evaluating thirty configurations across ten model families on twelve datasets at three compression factors, spanning reconstruction, generation, latent geometry, downstream classification, and memorization. We find that (1) performance on image reconstruction and generation strongly correlate, unlike prior reports on natural images; (2) modern tokenizers use nearly all of their codebook entries, but still leave most of the latent space unused; (3) training-set memorization is mild and is further suppressed by stronger latent space compression; and (4) discrete quantization can largely preserve downstream classification, with lookup-free schemes being the main exception.

---


### 416. ["MeBo Leaves a Piece of You Behind": Designing a Relational Voice-Based Memory Companion for Older Adults](https://arxiv.org/abs/2609.24706)

**<font color=#1a73e8>作者：</font>** Hasibur Rahman, Mahsa Nasri, Manasi Vaidya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autobiographical remembering supports identity, well-being, and social connection in later life, yet voice-based memory technologies largely rely on isolated prompts. We designed and built MeBo, a fully functional relational voice-based memory companion, through participatory design with 11 older adults. Their accounts shaped four Design Strategies that guided MeBo's interaction design and multi-agent implementation. In a mixed-methods evaluation with 20 older adults, participants found MeBo exceptionally usable (SUS = 87.75), enjoyable, sociable, emotionally responsive, and trustworthy. Participants reported higher positive affect and momentary social connection and lower negative affect after the session than before. Participants described how MeBo followed their stories, returned to earlier memories, adapted to their preferences, and made its growing memory visible and controllable. MeBo's relational framing surfaces tensions around what it should remember, who may access memories produced through interaction, and what becomes of them when the user or MeBo is no longer present.

---


### 417. [A Federated Artificial Intelligence Framework for Optimizing Pancreatic Cancer Treatment - Strategy Update](https://arxiv.org/abs/2609.24718)

**<font color=#1a73e8>作者：</font>** Anne-Christin Hauschild, Amirreza Aleyasin, Nils H. Beyer 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While a centralized approach involving patient consent to collect and analyze data centrally would theoretically offer the best data quality and predictive performance, it is not always feasible in practice. Federated Learning (FL) architectures have shown to be a very promising approach to use and access distributed disease related resources within the GDPR boundaries. In a previous case report, we described the preconditions at the participating sites and necessary administrative and process related steps to prepare data, people and infrastructure for improving subtype identification and assessing treatment options in pancreatic cancer. We update this report sharing our experience in tackling the challenges and show preliminary results of the actual federated learning AI pipelines. At the participating sites, we have to identify and annotate the data being accessible after extraction and transformation in a local FL hub - in our case a centrally developed and distributively deployed Docker container. This container comprises the FL scripts generating local models. We apply a newly developed FL algorithm considering all local features, including partial overlapping features specific to the local sites. Theoretically, an annotation in a cancer setting should succeed using the German oncology core data set (oBDS), which is already utilized for mandatory reporting to cancer registries, and can be sustained in the FL setting. The FL algorithms deal robustly with partially overlapping features as we showed with public data sets. Major roadblocks including straightening operational concepts for the infrastructures, ethics approval for such novel architectures and support for every site have been addressed. However, scaling up this approach in the future faces hurdles; while including broader multi-modal data sets should be feasible, large-scale deployment to more sites remains challenging.

---


### 418. [ReSTI: A Source-Grounded Audit and Repair of STI-Bench](https://arxiv.org/abs/2609.24727)

**<font color=#1a73e8>作者：</font>** Pengzhan Sun, Ramanathan Rajaraman, Shiu-Hong Kao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial--temporal benchmarks are valid only when their questions, source annotations, and answer options identify the same physical quantity. We audit STI-Bench against the official ScanNet, Waymo, and Omni6DPose sources and find systematic coordinate-system and timestamp errors, under-specified targets and times, and disagreements between keyed options and answer details. We introduce ReSTI, a source-backed revision that reconstructs every recoverable answer under an explicit target, time, coordinate system, physical quantity, and unit. Source reconstruction reveals task-level geometric failures: ScanNet Grounding omits the required alignment between annotation and raw camera coordinate systems, while Orientation measures camera rotation on the wrong plane. ReSTI replaces these labels with explicit, source-consistent geometric definitions and corrects other source-verifiable defects, including Waymo poses evaluated at the wrong timestamp. Across 2,064 legacy questions, ReSTI retains 1,782 questions and records 282 evidence-backed exclusions. ReSTI therefore provides a conservative and source-traceable basis for evaluating precise video spatial--temporal reasoning. Project page: this https URL.

---


### 419. [GraphSVR: q-Space--Aware Graph-Based Slice-to-Volume Registration for Diffusion MRI](https://arxiv.org/abs/2609.24732)

**<font color=#1a73e8>作者：</font>** Noga Kertes, Daphna Link Sourani, Alex M. Bronstein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-weighted imaging (DWI) remains highly vulnerable to subject motion, particularly in time-efficient protocols and in motion-prone populations. While slice-to-volume registration (SVR) can mitigate inter-slice and inter-stack misalignment, diffusion MRI introduces additional complexity due to diffusion-direction-dependent contrast and the requirement to align dozens of measurements within a common reference frame, effectively yielding a 4D registration problem. Existing approaches rely primarily on sequential modeling or pairwise similarity and often degrade under sparse gradient sampling or severe motion. We introduce GraphSVR, a q-space-aware graph-based framework for 4D SVR registration in DWI. GraphSVR represents slice groups as nodes in an acquisition-structured graph, with edges encoding temporal proximity, spatial slice geometry and diffusion encoding relationships. A graph neural network predicts globally consistent stack-wise rigid motion, optimized in a self-supervised, zero-shot manner using only an anatomical reference image, without requiring paired ground-truth motion. We evaluate GraphSVR using both fully synthetic diffusion simulations and realistic recombination-based simulations from real acquisitions with controllable motion severity and gradient sparsity. Performance is quantified using grid error (mm) and rotation error relative to known ground-truth transforms. Under severe motion, GraphSVR reduces grid error and rotation error by 73% compared to FSL eddy, the standard DWI motion-correction method, with the largest gains observed in sparse-direction regimes. These results demonstrate that explicitly modeling acquisition structure through graph-based reasoning improves robustness and global consistency in 4D DWI motion estimation. Code is available at this https URL.

---


### 420. [MiTHras: Task-specific Hierarchical Semi-supervised Contrastive Masked Autoencoder for Mitotic Figure Analysis](https://arxiv.org/abs/2609.24736)

**<font color=#1a73e8>作者：</font>** Trinh T. L. Vuong, Simon Graham, Quoc Dang Vu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mitotic figure (MF) analysis supports tumor grading and prognostic assessment, but automated models remain sensitive to differences in tissue type and image acquisition. We present MiTHras, a task-specific pretraining framework that combines pseudo-label-guided image- and token-level contrastive learning with masked reconstruction. We construct TCGA-MF-Pseudo, a corpus of 1.8 million cell-centered images from 14 TCGA cohorts spanning 11 organ sites. Comprehensive evaluation on MF classification, detection, count-based survival prediction, and subtype classification demonstrates the efficacy of MiTHras. It achieves the highest mean F1 on all three MF classification benchmarks and both subtype benchmarks. MiTHras also outperforms general-purpose and pathology foundation encoders by a larger margin under frozen-encoder linear probing than under full fine-tuning. Although detection gains are modest due to a shared candidate-detection stage, ablations confirm that token-level supervision improves typical-versus-atypical classification and linear probing. These findings establish that MiTHras yields robust, transferable representations for automated mitotic activity assessment.

---


### 421. [Ananke: Contractive Torus Attractor Networks](https://arxiv.org/abs/2609.24737)

**<font color=#1a73e8>作者：</font>** Zhongping Ji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Ananke, a representation-learning framework that scaffolds latent representations onto a structured product-torus prior, and its flagship visual backbone realization, Contractive Torus Attractor Networks (CTAN). By factorizing high-dimensional latent spaces into an orthogonal direct sum of two-dimensional phase planes ($\bigoplus_{k=1}^K \R^2$), Ananke coordinates feature updates via a decoupled dual-phase continuous flow: skew-symmetric Hamiltonian transport moves features tangentially along energy level sets to preserve semantic phase invariants, while signed gradient dissipation contracts transverse perturbations normally toward target invariant manifolds. For circular potential families with frozen parameters, logarithmic radial feedback yields the Exact Log-Symplectic Flow (ELSF), an analytical closed-form mapping with exact exponential decay of log-radius error that evaluates in a single forward pass without numerical integration. We establish local input-to-state bounds for level-set deviations and log-radius errors, and characterize the normal hyperbolicity and persistence of the ideal product torus under bounded perturbations. We further formulate the architecture through Lie--Trotter operator splitting, unifying spatial depthwise diffusion with local manifold contraction, and analyze both exact trigonometric flows and hardware-friendly symplectic dual-shear variants. Across natural image benchmarks (CIFAR-100) and clinically challenging endoscopy datasets (Kvasir-v2), CTAN demonstrates exceptional parameter efficiency: an ultra-compact hierarchical model with merely 0.27M parameters achieves 90.52\% accuracy on Kvasir-v2, outperforming 25M+ baselines (ResNet-50, DenseNet-161) by nearly two orders of magnitude in capacity, while scaled variants attain 80.32\% top-1 accuracy on CIFAR-100.

---


### 422. [An Exact Junction-Tree Extended Formulation for Optimal Classification Trees](https://arxiv.org/abs/2609.24741)

**<font color=#1a73e8>作者：</font>** Jiancheng TU, WenqiFan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop an exact linear programming (LP) formulation for bounded-depth classification trees with binary features, using a junction-tree representation. The formulation is integral and supports recursive subtree optimization. Exact reductions make the model smaller while preserving the optimal value and recovery of an optimal tree. The reduced model supports two solution methods: column generation and message passing. Column generation solves integral restricted LPs and uses bounds over the full feasible domain to certify optimality. Message passing recursively combines optimal subtree costs. Both methods solve common subtree problems that, once the preceding tree decisions are fixed, can be evaluated independently and in parallel. Computational experiments show that the exact reductions substantially reduce the size of the junction-tree formulation. The resulting linear programming formulation certifies instances for which the tested mixed-integer formulation does not establish optimality within the same computational budget, while the column-generation and message-passing methods certify more instances and achieve an order-of-magnitude reduction in geometric-mean runtime relative to an existing state-of-the-art exact method for optimal classification trees.

---


### 423. [Enhancing Transformer Representations of Symbolic ODE Expressions](https://arxiv.org/abs/2609.24746)

**<font color=#1a73e8>作者：</font>** Xiyue Fan, Adam Prugel-Bennett, Stuart E. Middleton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing approaches to solving differential equations, such as symbolic regression, physics informed neural networks, and neural operators, typically focus on numerical approximations or blind symbolic search via fitting to numerical data. Less attention has been paid to learning structured representations of mathematical expressions that preserve commutative properties and could support mathematical reasoning in symbolic forms. Transformer models have shown strong capabilities in solving symbolic differential equations. However, standard positional embeddings in transformers are designed for sequence data. Symbolic differential equations are naturally represented by expression trees, so these positional embeddings may not efficiently capture their hierarchical structures. We investigate existing tree positional embeddings in symbolic ordinary differential equation (ODE) tasks. We systematically study their effectiveness under different settings. Our results show that tree positional embeddings aid learning in early epochs and continue to improve performance throughout, ultimately yielding consistent advantages across various data sizes and tasks. Based on learned structural representations, we apply contrastive learning to support the commutative property in mathematics. Ablation studies provide insight into how these methods interact in modelling symbolic mathematical structures.

---


### 424. [Inference of Unknown Dynamical Components Using Next Generation Reservoir Computing: From Chaotic Systems to Climate Data](https://arxiv.org/abs/2609.24754)

**<font color=#1a73e8>作者：</font>** Jule Budnick, Andrew Keane, Serhiy Yanchuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate next generation reservoir computing (NGRC) as a data-driven approach for inferring unseen components of dynamical systems. We compare NGRC with traditional reservoir computing (RC) using the Lorenz and Rössler system, where two unknown components are inferred from one given component. For both systems, NGRC achieves accurate results while requiring fewer training data and less computational time than RC. We identified an inverse proportional behavior between the number of time-delayed steps needed for NGRC and the temporal resolution, indicating that the physical time span covered by the delay interval is an important factor in determining the required number of delayed steps. Finally, we apply NGRC to the observational climate data of ENSO (El Niño--Southern Oscillation) and infer one observable from the remaining variables. Despite the noise and complexity of the real-world data, the NGRC shows promising results. Our findings demonstrate the potential of NGRC for efficient inference of unseen components in both controlled dynamical systems and real-world data.

---


### 425. [Epi-Logic: A Conceptual Framework for Epistemic Runtime Control, Schema Validity Checking, and Controlled Accommodation in Autonomous AI Agents](https://arxiv.org/abs/2609.24755)

**<font color=#1a73e8>作者：</font>** Boris Wetzk  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents are increasingly deployed in areas where wrong decisions are hard to reverse. This paper examines schema mismatch: the condition in which an agent operates within an interpretive frame that no longer applies to the current context. Outputs produced under such a mismatch can appear internally consistent, linguistically plausible, and largely factually correct; output-quality metrics alone therefore capture the underlying loss of validity only partially.
The paper introduces Epi-Logic, a conceptual framework for epistemic runtime control. It couples the detection of schema dissonance, a graduated reduction of autonomy, and the auditable switch to a validated schema. A schema is formalised as a tuple of variable space, expectation model, validity conditions, axioms, and metadata. The Epi-Score aggregates seven graded dimensions of epistemic dissonance; the temporal validity dimension D8, violations of the validity conditions G, and axiom violations are carried as separate categorical paths that are not offset against the aggregate.
The architecture rests on a checking asymmetry: formalised validity conditions can be checked at runtime, whereas the correctness of many actions is established only ex post. The paper separates two architectural properties, a conditional result from sequential changepoint detection, and an empirical remainder. Eight falsifiable propositions with named baselines describe the transition to empirical validation. All propositions are empirically testable hypotheses, not established results.

---


### 426. [Brain Metastases Segmentation for BraTS 2026 Task 1: A Multi-Architecture Comparison](https://arxiv.org/abs/2609.24769)

**<font color=#1a73e8>作者：</font>** Mahdi Islam, Musarrat Tabassum  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain metastases are the most common intracranial malignancy, occurring in roughly 30% of patients with primary solid tumors and carrying a median survival near 5.9 months. Automated segmentation is critical for treatment planning and volumetric monitoring, but metastases are frequently small, numerous, and heterogeneous in size within a single patient. We compare a plain nnU-Net baseline, a Residual Encoder Large (ResEncL) variant, region-based training, and a Primus transformer model for BraTS-METS 2026 Task 1, using patient-grouped cross-validation to prevent leakage from the longitudinal UCSD subset. Primus (label-based) is our strongest individual model by aggregate DSC/NSD, achieving 0.710/0.761 (ET), 0.742/0.785 (TC), 0.683/0.689 (WT), and 0.531/0.436 (RC). ResEncL trails Primus on aggregate DSC/NSD but achieves substantially higher lesion-wise F1 (e.g. ET: 0.452 vs. 0.052); a probability-averaging ensemble of the two only partially preserves ResEncL's F1 advantage (ET lesion-wise F1: 0.064). We further report three postprocessing and label-reconstruction pitfalls we believe generalize beyond this challenge. Code is available at this https URL.

---


### 427. [Virtual neural networks: hundreds of souls in a body](https://arxiv.org/abs/2609.24782)

**<font color=#1a73e8>作者：</font>** Petr Hurtik, Marek Vajgl, Zahra Alijani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A new concept, termed virtual neural networks, is introduced, where the count of trainable parameters is kept constant, and scalability is attained purely through computational resources. This concept is an abstract framework that can be realized using any standard convolutional neural network. It merges siamese neural networks with a deep ensemble technique by generating numerous virtual models that share weights derived from a small set of physical models. The ensemble comprises up to hundreds of trained models simultaneously. All virtual networks take the same input, and their interconnected structure induces an internal distortion that boosts the entire ensemble robustness. The accuracy of the ensemble improves as the number of virtual networks increases, without changing the capacity. Virtual neural networks outperform larger capacity models, typical deep ensembles, and contemporary approaches like SWA and Masksembles. Additionally, the highest-performing individual model from the ensemble surpasses other models trained individually, even those with a greater number of parameters. Code: this http URL

---


### 428. [Convex AI Compositionality and the Governance of AI System Populations](https://arxiv.org/abs/2609.24784)

**<font color=#1a73e8>作者：</font>** Andrea Ferrario  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI governance increasingly requires providers and public authorities to reason about multiple AI instantiations, alternative versions, and deployment configurations of multiple AI systems. Yet current regulation remains predominantly single-system-centric, acknowledging such multiplicity only sparsely without treating collections of related AI systems as governance objects. This creates an AI population governance problem: determining which instantiations can be meaningfully considered together and how their changing configurations can be represented and monitored. The first requirement has recently been addressed through trustworthiness-based accounts of AI identity. We address the second by introducing convex AI compositionality: a formal representation of the configurations generated by finite AI system populations that uses convex spaces. The core idea is that convex compositions of the operational states that a population of AI system instantiations may occupy over time are compatible with lifecycle reachability across the population and can preserve the formal identity relations between these systems. Well-known statistical and geometric constructions, such as weighted state distributions and convex hulls, become AI governance tools for distinguishing operational states, population weights, heterogeneity, and AI configuration change across different governance modes while remaining compatible, under stated conditions, with lifecycle reachability and AI identity. We illustrate our AI population governance framework through distributed healthcare deployments and controlled deployment of recruitment AI variants.

---


### 429. [Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788)

**<font color=#1a73e8>作者：</font>** Yujia Hu, Jiajun Li, Zihao He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose SVEET, a framework that requires merely training on a pretrained bidirectional video diffusion model but supports high-quality streaming video editing in an auto-regressive fashion. To tackle this problem, we first systematically revisit existing video-to-video diffusion approaches and identify two key principles for such streaming adaptation: backbone feature disentanglement and conditional frame independence. Building on these insights, we develop a novel paradigm for controllable video generation. At its core, an auxiliary model branch encodes source video inputs with temporally independent self-attention, and the intermediate features are injected into the corresponding backbone blocks for streaming-compatible control. Moreover, to bridge the discrepancy between the feature spaces of bidirectional and streaming models, we propose a decoupled training scheme that explicitly enforces the orthogonality between the optimization directions of video controllability and model causality. Such disentanglement ensures compatibility between the two objectives at inference and facilitates smooth zero-shot knowledge transfer across heterogeneous backbone architectures. Extensive experiments demonstrate that SVEET achieves superior editing quality while maintaining real-time performance, attaining 15 FPS on a single H100 GPU 17 without any auxiliary acceleration techniques. Codes are available at this https URL.

---


### 430. [Detecting Agitation Before Behavioral Escalation in Autistic Youth Through Multimodal Wearable Sensing](https://arxiv.org/abs/2609.24791)

**<font color=#1a73e8>作者：</font>** Nibraas Khan, Abigale Plunk, John Staubitz 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Challenging behaviors including aggression, self-injury, and property destruction are observed in 68% of autistic youth and pose risks to youth and caregivers. These episodes are preceded by agitation, a rising state of distress expressed through movement, vocalization, and autonomic arousal. Its signs are subtle and individualized, and its autonomic components are invisible without instrumentation. We collected upper-body movement from inertial measurement units, physiology from a wrist-worn device, and vocalizations from lapel microphones across 30 clinician-led sessions with 15 autistic youth, paired with expert behavioral annotations. We adapt four pretrained foundation models, one per modality, project each to a shared 128-dimensional space, and fuse them into a single group model. The model detected agitation with an area under the ROC curve of 0.724 at the clinician-annotated onset (within-participant permutation p=0.0005), declining to 0.608 at 30,s before onset. Thirteen of fifteen participants were above chance. A from-scratch configuration reached only 0.58, while frozen and fine-tuned features performed comparably (0.71 and 0.72). Audio contributed most of the signal, and a watch-only configuration stayed near chance. Individualized agitation is therefore detectable, including in unannotated windows preceding the annotated onset, using foundation-model transfer with one shared model rather than one per child.

---


### 431. [Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention](https://arxiv.org/abs/2609.24797)

**<font color=#1a73e8>作者：</font>** Julien Siems, Riccardo Grazzi, Korbinian Pöppel 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear RNNs based on the delta-rule enable efficient sequence modeling, but their linear updates with a low-rank correction constrain their expressivity. Prior work has shown that composing two delta-rule transitions in a single recurrent update can model a 2D rotation, but this increases the rank and the cost of the updates compared to a single transition. We show that Kimi Delta Attention (KDA) can realize 2D rotations by combining a single delta-rule transformation with a second reflection supplied by its channel-wise gate. This requires extending the parameter ranges of KDA by combining two existing range extensions: allowing gates in $[-1,1]$ and the delta-rule coefficient $\beta$ in $[0,2]$. We call the resulting model Complex KDA (CKDA). It preserves KDA's stability and efficiency, with transitions that remain diagonal-plus-rank-one and non-expansive, while reaching the state-tracking expressivity of DeltaProduct$_2$. We characterize the expressivity of CKDA and prove that every orthogonal diagonal-plus-rank-one matrix is exactly a CKDA transition matrix. A single CKDA layer can track every finite group isomorphic to a subgroup of $\mathrm{SO}(3)$, and many state-tracking results use one fewer layer for CKDA compared to other diagonal-plus-rank-one Linear RNNs. Empirically, combining both extensions yields the strongest length extrapolation among tested KDA range settings on $S_3$, $S_4$, and periodic audio continuation. In language modeling, CKDA outperforms Transformers and other linear RNNs, obtains similar results to a KDA baseline, and shows promising scaling behavior. Our code is open source at this https URL and our models are available at this https URL.

---


### 432. [MSI-Bench: Evaluating Multi-Speaker Voice Interaction for Collaborative AI Agents](https://arxiv.org/abs/2609.24812)

**<font color=#1a73e8>作者：</font>** Chenxu Xiong, Dongming Shen, Yuzhi Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice provides a natural and immediate interface for AI agents. Many settings in which voice agents could be useful, including meetings, households, and collaborative work, are inherently multi-speaker. Supporting these settings introduces challenges that are largely absent from one-on-one interaction. We introduce the Multi-Speaker Interaction Benchmark (MSI-Bench) for evaluating multi-speaker voice interaction. Each test case is a short multi-party multi-turn audio scene with participant context, expected tool calls, and atomic rubrics. The benchmark targets three capability families: multi-speaker memory, multi-speaker instruction following, and multi-speaker reasoning. It comprises 1,152 test cases, evenly split between Mandarin Chinese and English (576 each). The strongest configuration on each split passes all rubrics on only 66.8% of English and 54.5% of Mandarin cases, and the strongest open-weight configuration on 34.0% and 19.3%. Failure analysis separates perception from reasoning: open-weight models are bottlenecked by the multi-speaker audio front-end, while frontier systems still fail speaker-scoped decision making on clean transcripts---and models across the board often respond when no one has addressed them. These results identify speaker-grounded perception, speaker-scoped decision making, and conversational restraint as concrete targets for future voice agents.

---


### 433. [Mobile Imaging Solutions for Medical Diagnosis: Trends and Applications](https://arxiv.org/abs/2609.24814)

**<font color=#1a73e8>作者：</font>** Syed Muhammad Ibne Zulfiker, Tanzima Hashem, Fariha Tabassum Islam 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in processing power, camera technologies, and mobile image analysis have made smartphones and other mobile devices, such as laptops, increasingly suitable for medical diagnosis and healthcare applications. Researchers have developed low-cost solutions for the early detection and monitoring of various health conditions, including eye and ENT diseases, malnutrition, heart rate variability, skin and oral conditions, and injuries, using images captured by non-medical devices such as smartphones and webcams. This survey examines existing research on mobile image-based medical diagnosis, with an emphasis on its potential to enable low-cost and accessible healthcare. We comparatively analyze state-of-the-art solutions across different healthcare application categories, examining their advantages and limitations. Based on this analysis, we identify desirable characteristics of mobile image-based diagnostic tools and highlight areas where existing approaches have made progress as well as areas requiring further research. We also discuss application-specific and common challenges and outline directions for future research. Overall, this study provides a comprehensive overview of mobile image-based healthcare solutions and their potential to support low-cost disease diagnosis and monitoring, particularly for underserved populations in remote and resource-constrained settings.

---


### 434. [G-NAC: Graph Neural Automata Clustering via Emergent Domain Formation](https://arxiv.org/abs/2609.24823)

**<font color=#1a73e8>作者：</font>** Keith Miller, Tristan Crawford  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Graph Neural Automata Clustering (G-NAC), an unsupervised clustering method in which observations interact as cells on a fixed neighborhood graph. A shared recurrent graph-neural cellular rule evolves latent domain states through local interactions, which are converted into a rank-based spectral affinity for partitioning. Across 73 clustering tasks from 57 benchmark datasets, G-NAC achieved a mean adjusted Rand index (ARI) of 0.7951, comparable to Genie at 0.7941 and higher than the other evaluated baselines. Empirical training time and GPU memory scaled approximately linearly from 5,000 to 100,000 nodes. Learned transition rules also transferred from smaller source graphs to independent 100,000-node samples generated under matched conditions. These results demonstrate a recurrent graph-clustering formulation while identifying dependencies on graph quality, readout design, and source-target similarity.

---


### 435. [ZVeC: A Zero-Shot Framework for Instance-Level Vehicle Extraction and Generative Point Cloud Completion](https://arxiv.org/abs/2609.24825)

**<font color=#1a73e8>作者：</font>** Daisy Li, Kyle Gao, Quanyun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR point clouds acquired in underground environments exhibit severe geometric incompleteness due to occlusions and limited sensor viewpoints, making reliable point cloud completion challenging without large supervised datasets. We propose ZVeC, a zero-shot, instance-driven framework that reformulates scene-level completion as compositional object-level reconstruction. By decomposing a scene into semantic object instances, ZVeC reduces reconstruction ambiguity in cluttered environments while eliminating the need for scenario-specific training. Each segmented vehicle is completed independently using a depth- and 3D Gaussian-conditioned diffusion model that exploits generalized geometric priors before the reconstructed instances are recomposed into the original scene. To evaluate our approach, we construct a real-world dense LiDAR benchmark of underground parking environments. Experimental results demonstrate consistent improvements over representative scene-level baselines in both quantitative metrics and visual quality. The completed point cloud differs substantially from the measured input (average KL divergence ~ 2.1), yet reducing the input to only 1% of the original LiDAR measurements changes the completed reconstruction only marginally (KL divergence < 0.50). This demonstrates that ZVeC produces geometrically consistent completions even under extreme input sparsity.

---


### 436. [CRiDiT: Instantiating a run-time testbed for trust calibration in AI-infused systems](https://arxiv.org/abs/2609.24833)

**<font color=#1a73e8>作者：</font>** Yuntian Ding, Nicolas Herbaut, Camille Salinesi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The integration of AI into larger technical infrastructures has made the alignment of human trust with system trustworthiness, known as trust calibration, a critical engineering concern, since misplaced trust in either direction leads to operational and safety risks. While conceptual frameworks provide a strong foundation for understanding trust calibration, their translation into running systems remains a challenge, because there are few testbeds in which human trust inputs, machine trustworthiness evidence, gap detection and remediation operate together within a closed loop. This paper instantiates CRiDiT (Computational Risk-Sensitive biDirectional Trust) as a run-time testbed, operationalising machine-side trust with Dempster-Shafer Theory and PCR5 redistribution, human-side trust with Subjective Logic, and calibration with a threshold-based trust gap. Following the Design Science Research methodology, we exercise the artifact across three high-stakes scenarios (hiring, financial, legal), producing 144 logged interaction steps across fifteen sessions. The analysis shows that the artifact captures trust calibration dynamics as intended, and reveals three points at which the instantiated policy departs from its design requirements: the machine-side estimate begins from a global benchmark rather than task-relevant evidence; risk-sensitive thresholds do not produce risk-sensitive triggering; and the calibration policy assigns explanatory prompts to over-trust, where corrections narrowed the gap in all 6 observed cases. Since the first two arise from the same design decision, to make the difference of two estimated scalars the calibration criterion, they point toward a common requirement: that the criterion should operate on the evidence rather than on scalars derived from it. The third concerns what follows detection, and shows that the action vocabulary inherited from trust repair does not align with what the interaction logs show to be effective. The work contributes the artifact, a characterisation of its run-time behaviour, and the requirements this characterisation elicits.

---


### 437. [When Wider Views Fail: Stress-Testing Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2609.24839)

**<font color=#1a73e8>作者：</font>** Daisy Li, Kyle Gao, Quanyun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models enable efficient geometry estimation from sparse images, but their pretrained nature can make them vulnerable to distribution shifts beyond their training data. Identifying these failure modes is important for understanding when such models can be reliably deployed in unconstrained imaging settings. We investigate viewpoint variation as a controlled distribution shift by varying the angular span of sparse image inputs while keeping the input budget fixed. Across multiple feed-forward reconstruction models, we observe substantial degradation as viewpoint span increases, with wide spans producing both incomplete surface coverage and geometry unsupported by the observed imagery. These results reveal that viewpoint variation can induce failure modes beyond conventional reconstruction incompleteness, highlighting the need to evaluate pretrained feed-forward models under distribution shifts that challenge their learned geometric priors.

---


### 438. [Revisiting Multi-View Stereo: A Sequence-to-Sequence Formulation](https://arxiv.org/abs/2609.24850)

**<font color=#1a73e8>作者：</font>** Aoxiang Fan, Corentin Dumery, Nicolas Talabot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computing accurate geometry from multi-view images is a fundamental problem in computer vision. Recent feed-forward (FF) models jointly estimate 3D geometry and camera parameters, but they typically suffer from geometry distortion caused by reconstruction ambiguity, even when ground-truth camera parameters are supplied. In this paper, we study the multi-view stereo (MVS) problem with known camera parameters and propose a novel approach that bridges conventional MVS and FF methods. Rather than casting MVS as a sequence-to-one mapping that predicts depth only for a single reference view, we reformulate it as a sequence-to-sequence task, akin to FF models, that jointly predicts geometry for all input views. We introduce a global transformer-based architecture with two components that explicitly exploit camera-induced priors: ray-map embeddings that inject camera parameters into image patch tokens, making the transformer camera-aware, and a unified global cost volume that replaces conventional per-view cost volumes to jointly capture 3D structure across all views. Extensive experiments on multiple public benchmarks show our approach achieves state-of-the-art performance, surpassing both MVS and FF reconstruction baselines.

---


### 439. [When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting](https://arxiv.org/abs/2609.24862)

**<font color=#1a73e8>作者：</font>** Yifan Hu, Xilin Dai, Zhiyuan Qu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic time series forecasting concerns systems whose underlying mechanisms evolve, making the relative effectiveness of numerical models, reasoning strategies, and intervention rules inherently time-varying. Consequently, a time series agent must adapt the forecasts it produces and the orchestration policy that determines which components to trust and how to coordinate them. The deployment process naturally provides supervision for this adaptation as forecast horizons elapse and realized targets reveal the effectiveness of earlier decisions. Committing all numerical expert forecasts and candidate agent paths before target observation allows each realized outcome to evaluate the entire alternative set, providing delayed feedback without additional annotation. However, existing time series agents primarily incorporate prior experience through forecast refinement, reflection, or retrieval, without systematically converting realized outcomes into persistent updates to the joint orchestration policy governing later origins. To exploit this delayed feedback systematically, we introduce TimEvolve, a frozen-backbone time series agent that converts each realized outcome into persistent joint updates of expert trust, agent path selection, and intervention strength. A temporally ordered predict, reveal, and update protocol applies this feedback to subsequent forecasts. Experiments across eight Time-MMD domains show that TimEvolve achieves the best average MSE and MAE ranks among fifteen methods and the lowest errors on both metrics in seven domains. These results demonstrate the value of learning forecasting policies from the futures encountered during deployment.

---


### 440. [ATCion: Exploring the Design of Icon-based Visual Aids for Enhancing In-cockpit Air Traffic Control Communication](https://arxiv.org/abs/2609.24863)

**<font color=#1a73e8>作者：</font>** Yue Lyu, Xizi Wang, Hanlu Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective communication between pilots and air traffic control (ATC) is essential for aviation safety, but verbal exchanges over radios are prone to miscommunication, especially under high workload conditions. While cockpit-embedded visual aids offer the potential to enhance ATC communication, little is known about how to design and integrate such aids. We present an exploratory, user-centered investigation into the design and integration of icon-based visual aids, named ATCion, to support in-cockpit ATC communication, through four phases involving 22 pilots and 1 ATC controller. This study contributes a validated set of design principles and visual icon components for ATC messages. In a comparative study of ATCion, text-based visual aids, and no visual aids, we found that our design improved readback accuracy and reduced memory workload, without negatively impacting flight operations; most participants preferred ATCion over text-based aids, citing their clarity, low cognitive cost, and fast interpretability. Further, we point to implications and opportunities for integrating icon-based aids into future multimodal ATC communication systems to improve both safety and efficiency.

---


### 441. [DTKDP: A Dual Teacher Knowledge Distillation and Pruning Framework for Lightweight Oriented SAR Ship Detection](https://arxiv.org/abs/2609.24872)

**<font color=#1a73e8>作者：</font>** Yuming Li, Fan Zhang, Alin M. Achim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two-stage oriented detectors achieve high localization accuracy in synthetic aperture radar (SAR) ship detection, but their large backbones, feature pyramids, proposal modules, and heavy region of interest (RoI) heads hinder deployment. Existing lightweight SAR ship detectors typically use one-stage frameworks that lack proposal-level refinement for precise rotated localization. This paper presents a dual-teacher knowledge distillation and pruning (DTKDP) framework for lightweight oriented SAR ship detection. DTKDP introduces learnable gates into convolutional, normalization, and linear layers to prune convolutional channels and RoI-head neurons. Rotated proposal alignment (RPA) distills teacher and student predictions in a shared teacher-generated rotated proposal space, while a dual-teacher scheme combines classification and regression guidance from a homogeneous main teacher with complementary classification cues from a heterogeneous auxiliary teacher. Experiments on the SAR Ship Detection Dataset (SSDD) and Rotated Ship Detection Dataset in SAR Images (RSDD-SAR) show that DTKDP reduces the parameters of Oriented Region-based Convolutional Neural Network (Oriented R-CNN) and RoI Transformer equipped with ResNet-50 backbones by 87.5-91.8% and their floating-point operations (FLOPs) by 75.6-79.9%. In terms of average precision (AP) and mean average precision (mAP), the resulting Oriented R-CNN-slim and RoI Transformer-slim retain accuracy close to their full-scale counterparts. Relative changes across $\mathrm{AP}_{50}$, $\mathrm{AP}_{75}$, $\mathrm{mAP}_{50:75}$, and $\mathrm{mAP}_{50:95}$ range from a 2.38% decrease to a 0.65% improvement. Compared with RTMDet-tiny, they improve all four metrics on both datasets by 0.52-27.55% and consistently surpass representative distillation methods, demonstrating a favorable accuracy-efficiency trade-off.

---


### 442. [Partner-Specific Affective Precision in Social Active Inference](https://arxiv.org/abs/2609.24876)

**<font color=#1a73e8>作者：</font>** Harshil Shah, Andrew Pashea  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In multi-agent social settings, model reliability varies across relationships. Beyond inferring what others will do, an agent must calibrate how confidently those inferences should guide policy selection for each relationship. An agent may maintain a well-validated model of one partner, a fragile model of another, and a model under revision for a third; collapsing these into a single confidence estimate loses information relevant to policy selection. We therefore formalize affective precision as a relationship-specific metacognitive estimate of confidence in the current partner model. Each partner's behavioral evidence updates a local confidence estimate that modulates policy precision during selection, regulating how strongly current beliefs are expressed in policy rather than changing the content of those beliefs. Simulations in a multi-partner graded trust game show that partner-local affective precision influences behavior primarily through policy commitment rather than direct improvement of partner-state inference. Because the mechanism tracks partner-response predictability rather than realized payoff, greater confidence produces sharper policy commitment without necessarily producing higher rewards. Under abrupt shifts in social behavior, confidence accumulated from previously reliable predictions can remain behaviorally active after the relationship changes, showing that confidence revision can lag behind social change. Finally, varying precision gain and priors produce distinct trust-calibration dynamics, showing how confidence accumulation and revision depend on model parameters. Together, these results show how relationship-specific affective precision can distinguish social prediction from social policy commitment.

---


### 443. [Decomposing Error and Style in Automated Clinical Coding](https://arxiv.org/abs/2609.24877)

**<font color=#1a73e8>作者：</font>** Han-Chin Shing, Jack Moriarty, Ryan Ware 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In automated clinical coding, where the label space spans tens of thousands of diagnosis and procedure codes, models are currently evaluated against a single gold annotation, treating any deviation as error. But we find when two teams code the same 110 ACI-Bench encounters, they agree on only 73% of codes (Jaccard similarity) for the same note; even after an independent clinical audit removes erroneous codes, agreement rises only to 77%. Is that gap error or something systematic? We model the systematic component as coding style $\psi$, a coder- or site-specific policy over what to code and how much to document, and recast coding as $p(\mathrm{code}\mid\mathrm{note},\psi)$, estimating $\psi$ with a 10-dimension rubric. If style were noise, conditioning on it would do nothing. Instead, across five datasets a model conditioned with a data-matching style raises ICD F1 by up to 26 points and an extreme mismatched one lowers it by up to 21. Four prompt based coding methods spanning 39-49 F1 converge to 52-56 once style is supplied (All p<0.05). Much of what single-gold evaluation charges to model error is recoverable, unmodeled style.

---


### 444. [Generating Chest X-Ray Counterfactuals by Specialising Foundation Image Models](https://arxiv.org/abs/2609.24879)

**<font color=#1a73e8>作者：</font>** Xiaodan Xing, Rajat R. Rasal, Julia A. Meister 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counterfactual image generation answers questions about how a subject would have looked under retrospective, hypothetical scenarios. Recent methods have improved perceptual quality, identity preservation and faithfulness to an underlying causal model, but their adoption in healthcare is limited by scarce annotated data, distribution shift between datasets, and mismatches between pretrained generative models and those required for counterfactual inference. We propose specialisation, a data and parameter-efficient framework for adapting pretrained, non-causal generative models into causal mechanisms under distribution shift. Based on this framework, we train a radiology counterfactual image generation model, called RadCF, using latent flow matching. We validate our approach on three chest X-ray datasets spanning different dataset shifts, data volumes, and counterfactual questions, associated with challenging, highly-localised interventions. Our results show that RadCF and specialisation improve counterfactual soundness over existing methods while being data and parameter efficient, and that the resulting counterfactuals can detect and mitigate shortcut learning in a downstream medical classifier. Code is available at this https URL.

---


### 445. [Learning Prognostic Variables for AI Convective Parameterizations via Symbolic Distillation](https://arxiv.org/abs/2609.24882)

**<font color=#1a73e8>作者：</font>** Jurij Schönfeld, Tom Beucler, Julien Savre 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid AI-physics climate modeling aims to improve coarse (~100km-resolution) Earth system models by learning to parameterize subgrid processes from high-fidelity data. However, this so far mostly involves local-in-time, diagnostic parameterizations, in which the subgrid state depends only on the current coarse state with no memory of previous states, which is unrealistic for processes such as convection that have intrinsic persistence. To address this, we enhance local-in-time parameterizations by learning prognostic variables that compactly carry important, additional past information where no explicit sub-grid information is available. First we compress past information into a low-dimensional latent space using an autoencoder, which then informs a neural network trained to parameterize targeted subgrid-scale processes. We then replace the autoencoder with symbolic equations that govern the time evolution of the latent variables, yielding additional prognostic memory variables that can be integrated alongside the resolved atmospheric state. We evaluate this approach on two systems: the Lorenz-96 model (online) and surface precipitation from high-resolution atmospheric simulations (offline). A forced multivariate linear ordinary differential equation recovers most of the added value achieved by the autoencoder-based approach in both experiments. Benchmarked against diagnostic parameterizations without memory, our memory-informed approach improves climate statistics and temporal structure, including a realistic diurnal cycle of tropical land precipitation.

---


### 446. [A Global Comparison of Schemas, Transparency, and Interoperability in Public-Sector AI Registers and Inventories](https://arxiv.org/abs/2609.24883)

**<font color=#1a73e8>作者：</font>** Dipto Das, Shion Guha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) registers and inventories aim to make governmental AI visible, but their institutional scope, schemas, and reporting practices construct different representations of public-sector AI. We compare 8,368 records from country-specific and transnational inventories covering 72 countries. Across 23 harmonized fields, registers shared a descriptive core but rarely requested information about appeals, risks, legal bases, or external evaluation. We found that broad schemas often contained substantial missingness, schema similarity showed no significant patterned convergence, and multiple sources covering the same jurisdictions overlapped only selectively. Based on these findings, we synthesize a layered visibility framework that shows how register records reflect disclosure arrangements and why interoperability requires shared concepts, clear definitions, and preserved provenance.

---


### 447. [ToneCL: Contrastive Learning for Few-Shot Syllable-Level Tone Classification](https://arxiv.org/abs/2609.24903)

**<font color=#1a73e8>作者：</font>** Qisheng Liao, Youngah Do  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tone languages constitute over 50-70% of the world's languages, but the vast majority are low-resource, lacking the large transcribed corpora needed for automatic tone classification. Existing datasets are typically collected at the sentence level, whereas field linguists require fine-grained syllable-level annotations. We propose ToneCL, a lightweight contrastive learning framework for few-shot syllable-level tone classification. We simulate low-resource conditions on Mandarin and Vietnamese, limiting labeled data to tens of examples per tone class. ToneCL is pretrained on unlabeled speech with augmentations that preserve tonal identity, then fine-tuned on few-shot examples. Experiments show our method consistently outperforms baselines, achieving 91.6% on six-speaker Mandarin at 10 shots. Cross-lingual transfer is also effective: pretraining on Vietnamese and fine-tuning on Mandarin reaches 91.0\% accuracy at 10 shots. Ablation confirms that frequency band rejection is the most critical augmentation.

---


### 448. [SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI Co-evolutionary Paradigm](https://arxiv.org/abs/2609.24911)

**<font color=#1a73e8>作者：</font>** Xinnong Zhang, Jiayu Lin, Jia Wang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social simulation offers the social sciences an experimental instrument that the real world cannot supply, and generative agents have transformed it by acting as silicon samples that unite agent-based modeling with real behavioral data. Existing platforms verify collective behavior, align simulated populations with real societies in cross-sections, and employ autonomous agents for the research process. However, two social science requirements remain without systematic support: intervention in the content of a simulation and the researcher's control over the process that produces it. We present SocioVerse2, which extends SocioVerse 1.0 into a human-AI co-evolutionary paradigm built from two loops and one infrastructure. The longitudinal simulation loop simulates the target population with evolving environments and forks counterfactual branches via interventions. The controllable research loop takes the study itself as an editable state and updates state versions via controllable editing. The social science agentic infrastructure carries both loops through composable skills with researcher checkpoints, a population service over five persona pools, and an environment service over 21 real-world signal sources with point-in-time guarantees. We validate SocioVerse2 across three case families and seven case studies, from reproducing canonical agent-based models to modeling policy processes on real records and nowcasting macro-economic indices beyond the response model's knowledge cutoff. With the human-AI co-evolutionary paradigm, these cases go beyond system demonstrations to become substantive studies that investigate frontier questions in their respective disciplines. Code, data services, and a workbench are released as open-source resources.

---


### 449. [PixelDiT2: Representation-Grounded Pixel Diffusion Transformers](https://arxiv.org/abs/2609.24919)

**<font color=#1a73e8>作者：</font>** Yongsheng Yu, Wei Xiong, Yichen Sheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in pixel-space diffusion models have narrowed the image quality gap with latent-space diffusion, but still converge more slowly and lag behind in final image quality. We argue that a key reason is the lack of an explicit representation prior: unlike latent diffusion, which usually denoises in a compact and structured latent space, pixel diffusion needs to learn denoising-friendly representations and pixel generation simultaneously from raw RGB space. To address this problem, we propose PixelDiT2, an end-to-end pixel-space diffusion model designed to decouple representation learning from pixel generation without introducing an autoencoder or latent reconstruction bottleneck. We propose representation grounding that uses a frozen pretrained vision foundation model to provide explicit per-patch representation guidance throughout denoising, allowing the pixel diffusion transformer to focus more on pixel generation. On ImageNet-256x256, PixelDiT2 achieves an FID of 1.46 after 600 epochs; at 512x512 resolution, PixelDiT2 achieves an FID of 1.48 after 680 epochs.

---


### 450. [Linguistic Features for Interpretable Textual Entailment](https://arxiv.org/abs/2609.24932)

**<font color=#1a73e8>作者：</font>** David Torres-Moreno, Jorge Hermosillo-Valadez, Asela Reig-Alamillo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the success of neural models in natural language processing, their black-box nature limits interpretability and conceals the linguistic phenomena underlying their predictions. We present SLITE, an explainable hybrid model for Recognizing Textual Entailment that integrates two complementary layers of semantic analysis: a structural-relational layer, based on semantic compatibility and incompatibility between compositional entities, and a distributional-informational layer, based on structured patterns of information change between embedding-based representations of the premise and the hypothesis. We propose 17 features that combine entity-level semantic relations, polarity-sensitive lexical matching, and alignment measures over semantic sub-representations of the similarity matrix, including measures based on entropy and transfer entropy. A logistic regression trained on these features achieves an accuracy of 83% on three-class SICK and 96% on SICK-CE, outperforming IsoLex by 4 percentage points and falling within 2 percentage points of RoBERTa with a fraction of its computational complexity. Ablation studies and SHAP analysis confirm that structural-relational features are the primary drivers of classification, while distributional-informational features provide essential complementary contributions, particularly for detecting neutrality and contradiction. Our results demonstrate that further exploration of hybrid approaches is a viable and scientifically productive alternative to massive neural architectures, and we hope they will strengthen the dialogue between linguistic theory and computational modeling of inference

---


> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
