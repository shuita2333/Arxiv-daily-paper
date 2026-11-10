# 🧠 大模型相关研究 | 2026年11月11日

> 本类共 **438** 篇论文：已确认 **405** 篇，待复核 **33** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-438**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-438**

---

### 401. [Is Persona Generalization Predictable?](https://arxiv.org/abs/2611.12864)

**<font color=#1a73e8>作者：</font>** Olina Mukherjee, Arnav Goel, Aditi Raghunathan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona generalization occurs when fine-tuning a language model in one domain induces behavioral changes in others -- for example, the broadly unsafe behavior observed in emergent misalignment. We discover a surprising "on-the-line" phenomenon in persona generalization: in-domain and out-of-domain persona rates across various fine-tuning hyperparameters follow an approximately probit-linear relationship, and the specific probit-linear relationship is surprisingly shared even across model families and model sizes, including Qwen and Llama. Training choices that leave the set of trainable parameters unchanged, such as learning rate, weight decay, and training duration, largely move models along the same line, reducing transfer mainly by weakening in-domain learning. Changing which layers are fine-tuned, however, can change the slope. For unsafe behavior, fine-tuning only later layers yields shallower slopes, retaining strong in-domain learning while reducing out-of-domain misalignment. This "on-the-line" phenomenon unifies unexpected, isolated observations of persona generalization within a quantitative framework for predicting and controlling behavioral transfer.

---


### 402. [Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis](https://arxiv.org/abs/2611.12869)

**<font color=#1a73e8>作者：</font>** Julia Herbst, Simon Roschmann, Quentin Bouniot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Platonic Representation Hypothesis (PRH) suggests that neural networks are converging toward similar representation spaces. As language models become more capable, their representations are aligning with those of vision models. However, recent work has questioned whether this trend continues to hold for newer language models. Moreover, it has been shown that representation similarity metrics can be confounded by model depth and width, requiring appropriate baselines for interpretation. In this work, we first investigate where alignment emerges between unimodal models across model layers and representation dimensions. Next, we find that the PRH capability-alignment trend persists for newer models as long as the captions are sufficiently clean and informative. Finally, we contextualize cross-modal alignment, introducing unimodal and multimodal baselines on various datasets. Our results show that the cross-modal representational alignment of unimodal models can surpass that of explicitly aligned vision-language models, but remains substantially behind the alignment observed for models of the same modality. Code is available at this https URL.

---


### 403. [Beyond Modality Preference: Controlling Multimodal Arbitration under Modality Conflict in MLLMs](https://arxiv.org/abs/2611.12883)

**<font color=#1a73e8>作者：</font>** Zhaoying Pan, Shenyu Lu, Jun Hui Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) integrate information across modalities, but become unreliable when those modalities disagree. Under conflicting inputs, MLLMs may favor modalities that are not the most reliable for the task, thus motivating inference-time control of modality arbitration. We identify a small set of attention heads, termed arbitration heads, that causally influence whether predictions follow visual or textual evidence. Building on this, we introduce a lightweight, training-free intervention that biases these heads toward a designated trusted modality at inference time. The identified heads are stable across calibration set sizes and generalize across settings, and steering them enables effective bidirectional control of modality reliance across diverse benchmarks. Our findings identify an effective control mechanism to align MLLM predictions with task-specified modality priorities. The code is available at this https URL.

---


### 404. [World In-Context Learning for Agentic Robot Manipulation](https://arxiv.org/abs/2611.12885)

**<font color=#1a73e8>作者：</font>** Heng Fang, Zehui Guo, Yuehan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world transfers to another. Based on this insight, we propose World In-Context Learning (WICL), a paradigm in which a frozen model starts from a demonstration, rehearses the task in a world such as a simulator, and writes the feedback into its context rather than its weights. We build RoboScript, a modular infrastructure that implements WICL for agentic manipulation. From a single demonstration, RoboScript learns each task through rehearsal in simulation, freezes the learned knowledge as a Task Memory, and deploys the frozen memory on new scenes with data isolation that ensures every deployment input is available on a real robot. On all 50 tasks of RoboTwin 2.0, RoboScript reaches 83.4% mean success across clean and randomized settings with one demonstration per task and no gradient updates, exceeding the strongest trained action policy by over 20 points. The method generalizes across visual distributions, improves through reflection, scales with the foundation model, and transfers to a physical dual-arm robot through cross-embodiment memory adaptation. With a world in the loop, a robot can learn a manipulation task in its context as well as it learns one in its weights. All code is available at this https URL

---


### 405. [Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic Visual Reasoning](https://arxiv.org/abs/2611.12886)

**<font color=#1a73e8>作者：</font>** Haozhi Yuan, Handong Li, Yifan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) and multi-teacher on-policy distillation (MOPD) offer complementary routes to post-training. For visual agents, however, tool use presents two related challenges. Models may overlook useful tool-returned observations, while poorly grounded actions can limit the evidence available for subsequent distillation. We introduce Reframe, a post-training framework that treats the observation state, rather than only the output distribution, as an object of alignment. First, Ground-Drop-GRPO (GD-GRPO) trains spatial and temporal specialists with evidence-aware rewards and stochastic removal of the original visual input, encouraging them to acquire grounded evidence and use the returned observations. Second, Observation-Gated-MOPD (OG-MOPD) replaces deficient tool actions with canonical ones mid-rollout and resumes distillation from the repaired observation. The two stages complement each other, as learning to rely on tool-returned observations can help the policy benefit from observation repair. Neither stage requires a task-specific SFT cold start. Extensive experiments over 14 image and video benchmarks demonstrate that Reframe outperforms both Mix-RL and vanilla MOPD. Ablation results show that GD-GRPO increases observation dependence and tool gain compared with outcome-based GRPO.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 406. [Nanopath: Fast, Fair, Open Experimentation for Pathology Foundation Models](https://arxiv.org/abs/2611.10014)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Paul S. Scotti, Hassan Muhammad, Ryan Kim 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce nanopath, an open-source framework and benchmark for rapidly training and evaluating small-scale pathology foundation models. Using a single H100 GPU, a typical nanopath model trains in a little over an hour on up to one million TCGA pathology tile presentations and evaluates within 25 minutes on a broad suite of tile-level and slide-level tasks. Nanopath enables rapid exploration of research ideas at small scale, so promising training recipes can subsequently be tested with more data and compute. To enable fair comparisons between ideas, we constrain submissions to fixed data and compute budgets while keeping the downstream evaluation protocol fixed. Anyone may clone the codebase, automatically download the data, reproduce or modify existing models, and submit a run to Labless, our public experiment ledger where researchers and AI agents can search through prior attempts. Since its public release in June 2026, nanopath has received 1,269 experiments from 20 contributors. Here, we detail its design and assess how well its rapid evaluation tracks standardized THUNDER, HEST, and PathoBench (CPTAC) benchmarks across six nanopath and 14 reference foundation models. Nanopath's fast evaluation suite strongly tracked these standardized benchmarks, and a few 22M parameter nanopath models even outperformed giant 1.1B parameter models on a subset of downstream tasks. We subsequently discuss how we have since optimized nanopath's evaluation suite to be an even more faithful, quick proxy for external benchmarking. Nanopath provides an accessible testbed for students, researchers, and AI agents to explore pathology foundation modeling through fair, transparent, and directly comparable experiments.

---


### 407. [REFORM-3D: A Representation-Centric Evaluation Framework for 3D Medical Vision Foundation Models](https://arxiv.org/abs/2611.10062)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Maregu Assefa, Muzammal Naseer, Divya Velayudhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluation of 3D medical foundation models is typically dominated by downstream task scores, which entangle representation quality with adaptation choices. This is especially critical in volumetric imaging, where spacing and anisotropy can substantially alter image statistics while the anatomy itself remains unchanged. We therefore introduce \textbf{REFORM-3D}, a \textbf{R}epresentation-centric \textbf{E}valuation \textbf{F}ramew\textbf{OR}k for benchmarking frozen 3D medical vision foundation \textbf{M}odels across three questions: Acquisition Robustness, asking whether features remain stable when spacing varies while anatomy is fixed; Cross-Modal Anatomical Alignment, asking whether labeled anatomical structures remain recoverable across modalities under balanced bidirectional retrieval; and Anatomical Transfer, asking whether organ identity remains recoverable from limited labeled support under case-disjoint evaluation. These are also pretraining questions, because what a 3D encoder learns depends on how volumes are geometrically presented during self-supervised pretraining. We further introduce Med3DINO encoder family, pretrained on $62.6$K unlabeled MR, CT, PET, CTA, and CBCT volumes under three explicit geometric assumptions: isotropic normalization, voxel-relative sampling, and spacing-aware resampling. Across Med3DINO and heterogeneous external encoders, REFORM-3D reveals module-specific strengths rather than a single model ordering. Within the controlled Med3DINO comparison, voxel-relative sampling yields lower embedding drift, whereas spacing-aware resampling favors anatomical transfer; semantic-transfer advantages depend on the dataset and feature type. Project link: \href{this https URL}{\highlightLR{REFORM-3D}}.

---


### 408. [Contrastive fine-tuning against stain and scanner bias improves robustness and downstream performance across pathology foundation models](https://arxiv.org/abs/2611.10093)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ryan Kim, Hassan Muhammad, Anish Dulal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathology foundation models achieve strong performance across diverse downstream tasks, yet their representations have been shown to encode scanner- and site-specific biases, creating generalization gaps and potentially limiting real-world utility. We introduce SPECTRA (Scanner and Pathology Embedding Contrastive Tuning for Robust Alignment), a model-agnostic contrastive learning post-training framework which explicitly encourages scanner- and stain-robust representations, to optimize performance and generalization on downstream applications. Using parameter-efficient LoRA adapters trained on matched multi-scanner and multi-stain whole-slide images sourced from the PLISM dataset, our method aligns spatially corresponding regions across acquisition conditions (scanner, stain), using other locations within each candidate condition as negatives. SPECTRA improved PathoROB robustness index, gene-expression prediction on HEST, slide-level classification AUC on CPTAC, and held-out PLISM retrieval for every model. Overall tile-level classification on THUNDER also improved, with exceptions for segmentation and calibration tasks. We open-source our training and evaluation codebases and release adapters and model weights for selected backbones.

---


### 409. [RAD-TFM: Robust and Domain-Adapted Tabular Foundation Models](https://arxiv.org/abs/2611.10230)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Matthew Peroni, Franck Le, Vadim Sheinin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of tabular foundation models (TFMs) has accelerated in recent years, outperforming traditional ML methods on many tabular benchmarks. A key finding is that TFMs can be pretrained entirely on synthetic datasets, opening opportunities to design data generators that encourage desirable model properties. Prior work has mainly focused on crafting high-quality priors over generators to improve overall pretraining performance. Our key insight is that parameterizing the generator distribution enables an adversarial, distributional robustness perspective: during training, we can adapt the generator to emphasize datasets that are particularly challenging for the model, which we formalize by introducing an optimality gap measure. Further, we develop a method to align the synthetic data generation with real-world datasets from a given domain, constraining the adversary to generate realistic data. Together, these algorithms comprise the Robust and Domain-Adapted Tabular Foundation Models (RAD-TFM) pipeline, a model-agnostic adversarial training framework. Applied to the TabPFN V2 classifier, RAD-TFM improves performance across 6 diverse tabular benchmarks, with up to a 10.8 percentage-point improvement in mean normalized AUC over the strongest baseline, using fewer than 100k additional synthetic training datasets, less than 0.1% of the original pretraining data. Applying the same pipeline to TabICL V2 also improves performance across three major benchmarks, demonstrating the generality of the framework. These results highlight a promising new direction for targeted adversarial continued training of TFMs using synthetic data alone.

---


### 410. [Can Time Series Foundation Models Serve as Surrogates for Power Systems Dynamic Simulation?](https://arxiv.org/abs/2611.10247)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sandy Miguel, Bruno Paes Leao, Cheng Feng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity dynamic simulation is essential for scientific and engineering applications, but its computational cost limits large-scale scenario screening. We investigate the use of pretrained time-series foundation models (TSFMs) as computationally efficient surrogates to address this limitation. In-context learning and post-training strategies, including retrieval-augmented reference sample selection and physics-informed regularization, are considered in the investigation. Results are benchmarked against a traditional AI model representative of the state-of-the-art in the domain. Experiments using an open-source TSFM and data from a simulated 9-bus power system indicate promising results. Retrieval augmentation improves in-context learning performance, and fine-tuning leads to superior results compared to the traditional AI model, especially when including physics-informed regularization. The fine-tuned TSFMs achieve lower errors and improved computational costs compared to the traditional AI model, and a 563$\times$ speedup compared to the original physics-based simulation.

---


### 411. [DAC-MACE: Context-Conditioned Expert Routing for Compact Scene Coordinate Regression in Camera Relocalization](https://arxiv.org/abs/2611.10263)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dingying Fan, Mingkai Liu, Haohua Que 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A camera becomes an absolute pose sensor when its images can be relocalized against a prebuilt map of the scene. On mobile robots and augmented-reality devices, that map must be small and quick to build. Scene coordinate regression (SCR) stores the scene in a compact network that predicts a 3D coordinate for every pixel, and mixture-of-experts (MoE) variants extend its capacity to larger outdoor scenes. In existing MoE-based SCR, however, the router assigns each pixel to an expert from the same local descriptor that the experts regress from, so repeated facades and windows at different locations receive similar routing inputs. We present DAC-MACE, which conditions soft expert routing on recalibrated and contextualized features. A residual context adapter (RCA) reweights the channels and locations of frozen encoder features, a global context encoder (GCE) mixes them with multi-scale self-attention, and an image-level pooled descriptor is added to the router input. A dual-threshold RANSAC--Levenberg--Marquardt estimator recovers the pose. On Cambridge Landmarks, DAC-MACE attains a mean per-scene median translation error of 13.0 cm over three seeds, the lowest among the RGB-only SCR methods compared (GLACE 13.6 cm, MACE 14.4 cm), and reduces the error on the largest scene from 24 to 19 cm relative to MACE. In a cumulative study, the MoE head, GCE, RCA, and the dual-threshold estimator lower the mean error from 17.0 cm to 14.4, 14.0, 13.6, and 13.0 cm. On 7-Scenes, adding GCE to a single ACE head raises Recall@(5 cm, 5$^\circ$) from 86.56% to 87.60%.

---


### 412. [PoseBench: Probing Pose Awareness in Visual Foundation Models](https://arxiv.org/abs/2611.10347)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Most Nilufa Yeasmin, Draix Wyatt, Ruyi Lian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose awareness characterizes the extent to which a learned feature space aligns with the underlying object-pose manifold, such that observations with similar poses exhibit greater feature similarity than those with increasingly different poses. While such structure is desirable for pose-sensitive 3D vision tasks, visual foundation models pre-trained on individual 2D images typically lack explicit 3D or pose supervision. This raises a fundamental question: Do 2D visual foundation models exhibit pose awareness after large-scale pretraining? To answer this question, we introduce PoseBench, a systematic benchmark to probe pose awareness in pretrained visual features. Our evaluation follows a progressive design: held-out rendered views probe intrinsic pose-aware structure under controlled conditions, while real-image queries evaluate how robustly this structure remains accessible under real-world variations. We further introduce pose-graph-based refinement as a complementary probe of compatibility between feature neighborhoods and the underlying pose manifold. Across 31 publicly available checkpoints from 10 pretraining families, PoseBench reveals that pose awareness is an implicit but non-uniform property of 2D visual foundation models, and consistent gains from pose-graph refinement suggest that feature spaces retain structure compatible with the underlying pose manifold. PoseBench therefore provides a systematic basis for understanding and selecting pretrained features for pose-sensitive 3D vision tasks.

---


### 413. [HexIt: Learning Hexahedral Block Decomposition with Expert Iteration on Combinatorial Maps](https://arxiv.org/abs/2611.10433)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arjun Narayanan, Per-Olof Persson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decomposing a polyhedral solid into a few well-shaped hexahedral blocks is a long-standing open problem in mesh generation. We cast it as a sequential decision problem on a 3-dimensional generalised map: an agent splits edges, faces and volumes with three insert operations until every cell is a hexahedron and the mesh passes a quality threshold, and a policy that convolves over the map's involutions chooses each insert. A successful decomposition takes over a hundred decisions, and a uniformly random policy never finds one. We clone a policy from constructed decompositions and improve it by expert iteration. On held-out chamfered solids that share no boundary topology with the cloning data, the final policy solves an expected $94.4\%$ in $20$ samples, and expert iteration raises the best-of-20 solve rate on large chamfered solids from $0.203$ to $0.355$. At matched compute, PPO, GRPO and VinePPO updates all make the cloned policy worse.

---


### 414. [Bayesian Low-Rank Posteriors for Scalable Membership Inference](https://arxiv.org/abs/2611.10455)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Khanh Nguyen, Antonio Emanuele Cinà, Andrey Barsky 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks (MIAs) aim to determine whether a sample was used during the training of a target model. Strong MIAs rely on reference (or shadow) models to estimate target-conditional score distributions, but training such ensembles is computationally expensive for modern large-scale Vision--Language Models (VLMs). In this work, we propose a scalable alternative that replaces explicit reference-model training with a Bayesian approximation over low-rank adaptation parameters. Specifically, we model uncertainty only within the LoRA subspace and construct a posterior from a single training run, from which we sample a diverse set of \emph{virtual reference models}. We instantiate this approach using Stochastic Weight Averaging Gaussian (SWAG), enabling efficient approximation of target-conditional score distributions at a fraction of the cost of conventional shadow-model ensembles. We evaluate the resulting attack on three downstream-adapted VLMs across two privacy-sensitive visual question answering tasks, namely Document VQA and Medical VQA. To isolate the effect of pretraining knowledge, we additionally introduce a controlled synthetic dataset. Our approach outperforms standard reference-based attacks while requiring only a single reference-model fine-tuning run, making membership inference more practical for large VLMs.

---


### 415. [BAPLe++: Cross-Model Transferability and Prompt-Level Defense of Backdoors in Medical Foundation Models](https://arxiv.org/abs/2611.10764)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ufaq Khan, Umair Nawaz, Satyajit Tourani 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical foundation models (Med-FMs) are increasingly adapted to clinical tasks through prompt learning, which tunes a small set of prompt tokens while the backbone remains frozen. Recent work has shown that this efficiency introduces a vulnerability: jointly optimizing learnable prompts and an imperceptible noise trigger during few-shot adaptation implants a backdoor that leaves clean performance intact but steers triggered inputs to an attacker-chosen class. Since prompts are compact and readily shared, this raises two questions: whether a backdoored prompt remains effective on a different Med-FM, and whether it can be repaired without retraining the backbone. We address both in BAPLe++. First, we present the first study of cross-model transferability of prompt-based backdoors, quantified by two proposed metrics, Clean Accuracy Difference (CAD) and Backdoor Accuracy Difference (BAD). Second, we propose DePLe (Defense via Prompt Learning), which uses the infected prompt as a fixed anchor and learns a new prompt on a small clean set that preserves the clean task while diverging from the compromised embedding region. Experiments on four Med-FMs and six chest X-ray and histopathology datasets show that backdoors transfer across models, but asymmetrically and in a dataset-dependent manner. Compared with four training-free input transformations, DePLe reduces backdoor accuracy more consistently while preserving, and in several settings improving, clean accuracy. Our code can be accessed on this https URL

---


### 416. [Learning Biological Hierarchies in Single-Cell Foundation Models](https://arxiv.org/abs/2611.10838)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiangyu Guo, Ricardo Henao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cell types are organized by taxonomic relationships that define lineages in the so-called cell ontology. However, most existing foundation models typically ignore cell-type lineages encoded in this cell ontology. We introduce a biologically informed foundation model called scOntoFM, which embeds hierarchical cell ontology into representation learning. Using Lowest Common Ancestor (LCA) distances from the ontology graph, our framework pairs efficient offline triplet sampling with hierarchical cell-ontology learning. This approach jointly preserves local neighborhoods and shapes the global embedding geometry to reflect the ontology structure. Across diverse cell- and gene-level benchmarks, the model consistently improves performance, with especially strong gains in zero-shot settings. Our model also balances batch integration with biological structure preservation, providing complementary perspectives to existing embedding evaluation frameworks and supporting scalable biological discovery.

---


### 417. [REDiff-AD: No Training and No Target Masks for Industrial Anomaly Image Generation via Diversity-Driven In-Context MMDiT](https://arxiv.org/abs/2611.10875)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chih-Yu Tsai, Chih-Heng Chang, Jian-Jiun Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection is challenged by the scarcity and diversity of real defects, leaving insufficient anomalous data to effectively train downstream models. Existing anomaly generation methods often require product-specific fine-tuning, target mask annotation, or costly procedures to achieve realistic and diverse defects. We propose REDiff-AD, a framework that requires neither model training nor target masks and introduces Rectified Flow MMDiT into industrial anomaly generation for efficient sampling with fewer generation steps. Given a normal product image and a single masked reference anomaly, REDiff-AD employs in-context learning to transfer the defect appearance from the reference into the normal image. Internal attention signals generated during this process are further reused to localize the synthesized anomaly, while edge and color cues refine the localization into pixel-level pseudo-masks. Two lightweight modules further improve generation quality: adaptive reference conditioning enhances defect fidelity, while diversity guidance promotes varied defect patterns without additional training. Experiments demonstrate that REDiff-AD can well address the tradeoff between realism and diversity for anomaly pattern generation and achieve competitive downstream anomaly classification, detection, and localization performance. These results show that REDiff-AD is a simple, efficient, and effective solution for large-scale anomaly data augmentation and pixel-level data construction. Github code: this https URL

---


### 418. [Hydro-Dataset: A Multi-Modal Open-Source Pipeline for Nordic Hydrological Research and Foundation Model Benchmarking](https://arxiv.org/abs/2611.10992)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Getnet Demil, Md Moinul Islam, Mourad Oussalah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite world-class snow monitoring by the Swedish Meteorological and Hydrological Institute (SMHI) and Finnish Meteorological Institute (FMI), no station-anchored, multi-parameter snow benchmark dataset exists for the Nordic boreal domain. We present Hydro-Dataset v1.1, a reproducible open-source pipeline that harmonizes 582 SMHI meteorological observation stations across nine hydrological winters (2015/16-2023/24) into a CF-1.9 NetCDF product with 1.8~million annotated station-days. Six derived snow parameters, such as Snow Water Equivalent (SWE), snow phenology, melt rates, degree-day melt factor, rain-on-snow flags, and freeze-thaw cycles, supply benchmark-ready labels for hydrological foundation model training. ERA5-Land cross-validation (Pearson R=0.78, bias=-262mm) confirms observation-anchored SWE provides a more reliable benchmark than reanalysis for machine learning training.

---


### 419. [Prune to Probe: Causal Decision-Stability Probes for Efficient Reasoning](https://arxiv.org/abs/2611.11034)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yufei Qi, Chonghe Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models often continue generating after producing an answer, yet stopping prematurely may interrupt useful verification or revision. In this work, we investigate whether targeted interventions in a model's internal computation can provide a reliable signal for when to stop reasoning. We introduce Prune-to-Probe, an inference-time controller that uses causal activation interventions to probe the stability of a model's current answer. Specifically, we identify late-MLP coordinates that contribute to post-answer continuation while excluding those important for answer completion. Once an answer is stated, Prune-to-Probe temporarily suppresses the selected coordinates and measures the resulting stopping response relative to matched random interventions. Crucially, these interventions serve only as probes: the model either returns its existing answer or resumes generation from an untouched cache. On MATH, Prune-to-Probe reduces reasoning-token forwards by 2.60%, preserving all naturally correct trajectories while repairing six errors. On MMLU-Pro, it achieves 1.145% pooled savings with no observed harm. Further analysis shows that the intervention captures decision stability rather than correctness (AUROC 0.502). These results demonstrate the potential of causal activation probes for efficient inference-time control without permanent model modification.

---


### 420. [ZarrFM: A Canonical Tensor Storage Architecture for EEG Foundation-Model Pretraining](https://arxiv.org/abs/2611.11149)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Dheeraj Chintapalli, Sunkalp Chandra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical models for brain-computer interfaces (BCIs) increasingly require large, heterogeneous EEG corpora, yet existing datasets vary in sampling rates, channel layouts, window lengths, and storage formats, creating substantial preprocessing and I/O overhead. We propose ZarrFM, an execution-oriented representation that complements BIDS by storing a corpus as a single Zarr v3 hierarchy with indexed metadata, canonical channel spaces, explicit masks, hash-stable subject splits, verified event tables, and block-aligned sharding. On real PhysioNet recordings and synthetic corpora, we compare ZarrFM with EDF, FIF, NPY, HDF5, and Parquet. Across 200 recordings, its two-level index reduces metadata queries from 601 requests to 14. Preserving native signal codes reduces storage from 42.4 MB/hour in EDF to 22.7 MB/hour, while block-aligned sampling reaches 3,131 windows/s, up to 11 times faster than Parquet. Reads remain bit-identical across independent Zarr implementations, and concurrent failure-injected appends recover without data loss. These results show that ZarrFM can provide a compact, interoperable, and execution-efficient storage layer for large-scale EEG pretraining.

---


### 421. [Not Yet in the Profile: Uncertainty-Aware Dynamic User Profiling by Learning from Future Interactions](https://arxiv.org/abs/2611.11204)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jieyong Kim, Neil Shah, Dong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On the Web, user profiling builds compact user representations from interaction histories for efficient personalization, and dynamic user profiling updates them as users' behavior and preferences change. However, new user behavior can be ambiguous, and its interpretation differs across users. To address this, we introduce Uncertainty-aware Adaptive Profile Manager (UAPM), which separates the claims in a user profile from interpretations of new behavior that are not yet confirmed, through a Profile, a Buffer, and a Rulebook. UAPM records user-specific interpretation and update rules in the Rulebook, keeps ambiguous evidence in the Buffer outside the Profile as evidence for later decisions, and writes supported general and situational characteristics to the Profile. We train UAPM with Privileged On-Policy Distillation with Dual Specialization (POPD-DS), which learns from recorded future interactions during training without access to them at deployment. Its first stage, Dual Specialization, distills a stronger model into a current-only Student and a future-informed model that becomes the Teacher. In the second stage, privileged on-policy distillation (POPD), only the fixed Teacher receives future interactions and guides the Student's own management decisions alongside task rewards. Experiments on three Web personalization tasks show that UAPM outperforms multiple baselines under the same downstream input budget, improving on the best same-budget baseline by up to 5%.

---


### 422. [LoMASA: A Local Multi-Agent Sales Assistant with Confidence-Gated Delegation for B2B Quoting](https://arxiv.org/abs/2611.11234)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Liu, Xingbang Du  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontline sales staff spend much of their day re-coordinating quotes after customers change quantities, ask for discounts or new payment terms, or costs move. We present LoMASA (Local Multi-Agent Sales Assistant), a training-free multi-agent system that runs entirely on one desktop computer. A 35B mixture-of-experts model (System-1) makes each decision in a single forward pass and reads its confidence from the probabilities of the answer options. A 27B dense model (System-2) writes customer replies and escalation briefs and is consulted when System-1 is unsure. Code computes every price, margin and option, and hard pricing rules cannot be overridden. On a test split of 500 simulated episodes with 1512 decisions built from public supply-chain data, the salesperson has to decide only 19.5% of decisions: 38.0% are settled automatically, with a median latency of 2.67 seconds, and 42.5% are escalated to a manager by the hard rules. On the automatically settled decisions LoMASA is as accurate as a rule baseline (0.894 vs.\ 0.894) and makes fewer commitments whose margin later falls below the floor (2.61% vs 4.53%); the price is additional escalations to the manager. Option probabilities are well calibrated without any training, unlike confidence stated in words by the same model. We also report where the design does not help: the 27B model rarely changes a decision.

---


### 423. [CHANNELS4WORLD: An Environment-Scale Dataset for Wireless Foundation Models](https://arxiv.org/abs/2611.11428)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Joonkyu Jang, Hyung-Joo Moon, Kwang Soon Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wireless foundation models learn reusable representations across tasks, configurations, and deployment environments. Their pretraining requires environmental breadth, yet wireless datasets often sample few sites densely. We introduce Channels4World, a scene-centered dataset of 100,000 distinct outdoor RF scenes and a procedural method for generating them. Each scene links a generated environment and RF material assignments to 32 base-station (BS) positions, 16,384 UE positions, and aligned variable-length multipath and ordered interaction records at 3.5 and 7~GHz. The corpus comprises 52.43 billion physical BS-UE pairs, 104.86 billion frequency-specific evaluations, and a 29.14-TB packaged payload. Scene identity aligns geometry, placements, channels, and interactions across frequencies, allowing environmental breadth and within-scene observation density to vary independently. The public release offers predefined subsets at multiple scales and separate access to corpus components. A deterministic 90K/10K scene-level train-test split keeps both frequencies and all scene components together. We characterize morphology, RF materials, and transceiver placement across three generation profiles. Controlled propagation and path-retention analyses show that diffraction materially affects retained-link availability and multipath structure, while the retention policy reduces storage substantially with little loss in represented aggregate power. Under matched training exposure, models trained on broader scene collections perform better on held-out scenes, although an equal-episode control shows that scene count alone cannot explain the gain. By making environmental breadth explicit and controllable, Channels4World supports the development and evaluation of wireless foundation models for generalization across deployment environments.

---


### 424. [Data-informed Adaptation of Foundation Models for Causal Effect Estimation](https://arxiv.org/abs/2611.11504)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chunwei Ma, Russell D Wolfinger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Due to the fundamental problem of causal inference -- the impossibility of observing counterfactual outcomes -- there is always a gap between the training goal (outcome, propensity) and the inference target (CATE, ATE). Traditional causal effect estimation revolves around setting assumptions, selecting identification strategies, and choosing causal estimators, while more recently, Causal Foundation Models (CFMs), built on Prior-Data-Fitted Networks (PFNs), ease this process by pretraining on massive synthetic prior datasets. Despite their success, such amortization makes causal inference less transparent, obscuring which assumptions the model implicitly relies on for a given dataset. The high diversity of real-world data-generating processes (DGPs) and Structural Causal Models (SCMs) makes it hard to know, a priori, which causal inference strategy is compatible with a given dataset. In this work, we focus on this compatibility between an observational dataset and method-specific assumptions, and find that geometric characteristics of data embeddings -- specifically, the variogram -- provide a useful signal of whether a given causal estimation strategy is appropriate. We develop MoE-Learner, a mixture-of-causal-experts framework that embeds a dataset under multiple assumption-specific views and uses the variogram as a counterfactual-free router to assess each expert's validity. Rather than eliminating causal assumptions, this shifts their validation from a fixed, a priori choice to a criterion that can be checked directly from data geometry. MoE-Learner achieves the best average rank on benchmark datasets (IHDP, ACIC, Lalonde). Being orthogonal to (causal) foundation models, our method builds a bridge from data characteristics to causal estimation strategy rather than proposing another CFM.

---


### 425. [MICE: Multi-animal Interaction Context Encoder - A Hierarchical Foundation Model for Mouse Behavior](https://arxiv.org/abs/2611.11644)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yen-Shuo Su, Weihan Li, Anqi Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantifying mouse behavior from pose is a foundational tool in neuroscience, ethology, drug discovery, and animal welfare. Self-supervised foundation models are a natural fit, but a foundation model for mouse behavior must handle social behavior - many behaviors that matter (aggression, courtship, mounting, allogrooming) are inherently multi-animal. Existing self-supervised pose models fall short: they encode each animal independently and discard interaction signal, hard-code the animal count, and pretrain one dataset at a time. We introduce MICE (Multi-animal Interaction Context Encoder), a hierarchical foundation model for mouse behavior that pretrains jointly on six mouse-pose corpora spanning one to four mice and 7 to 27 keypoints. MICE combines a hierarchical individual encoder capturing per-mouse kinematics at multiple temporal scales with a Perceiver-style social encoder whose learned latent codebook decouples parameter count from animal count, so a single checkpoint serves any group size without retraining. Across four evaluation protocols spanning six datasets, MICE matches or exceeds prior keypoint-based baselines, and layer-wise probing shows the social stage incrementally improves discriminability beyond the individual encoder. Code, weights, and data are available at this https URL.

---


### 426. [Means vs. Foundation Models for Emergency Call Forecasting](https://arxiv.org/abs/2611.11656)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Feriel Fass, Djemel Ziou, Marie-Flavie Auclair-Fortier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study investigates whether generalized means can achieve forecasting performance comparable to that of TimeGPT for daily emergency call volume prediction. Specifically, two families of generalized means, the Hölder means (HM) and the Lehmer means (LM), are evaluated against fine-tuned TimeGPT across forecasting horizons ranging from one to seven days. Forecasting performance is assessed on a real-world emergency call dataset using multiple error metrics, and Diebold-Mariano test. Experimental results show that HM and LM achieve nearly identical predictive performance across all forecasting horizons. For short-term forecasting, both generalized means outperform TimeGPT, with reductions of mean absolute error (MAE) approximately 1.24\% and 2.48\% at horizons of one and three days, respectively. Conversely, TimeGPT achieves a lower error at the seven-day horizon, with an descresing of MAE by 1.98\%. However, Diebold-Mariano tests reveal no statistically significant differences between the methods at the evaluated horizons. These findings suggest that generalized means can provide competitive forecasting performance compared with a energyvore foundation model.

---


### 427. [Autonomous Continual Learning and Knowledge Transfer via Cortex-Inspired Neural Assemblies](https://arxiv.org/abs/2611.11717)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kevin L. McKee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlike the brain, artificial neural networks (ANNs) suffer from "catastrophic forgetting": complete overwriting of solutions when re-training on new functions ("concept shift") or on a disjoint domain of the current function ("domain shift"). ANNs require each batch of data to be roughly representative of the complete distribution, a typically expensive and impractical requirement. In this paper, we introduce Functional Task Networks (FTNs), a method of continual learning and knowledge transfer modeled after several properties of the mammalian neocortex. FTN is formulated as a distributed, stochastic mixture of experts in which a sparse, binary routing mask is computed at inference time using a small support sample of input-output pairs. Per-batch reconfiguration of the router during training, together with mask-overlap-filtered replay, shapes a basis of overlapping, partially trained subnetworks. Unrelated tasks route through mostly separate assemblies, related tasks overlap on shared components. On block-sequentially trained continual learning and knowledge transfer tasks FTN retains solutions nearly as well as disjoint-mask isolation and attains the lowest pre-update head-start loss among matched-architecture comparators. The learned mask-overlap geometry tracks the known concept-sharing structure where available. We show experimentally that under correlated concept shift, support-set mask reconfiguration is necessary even for retention. Under domain shift, the distributed bank with replay is sufficient to handle retention without the configurer. Forward transfer, or head-start, and backward transfer, are also contributed by support-set mask configuration.

---


### 428. [Creative Priming: Decoupling Process from Product to Escape the Creative Paradox](https://arxiv.org/abs/2611.11740)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alon Albalak, Sebastian Gabriel, David B. D'Ambrosio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many of the most consequential advances promised by AI, from curing diseases and inventing new technologies to formulating new scientific theories, are fundamentally creative acts. Yet creativity is uniquely difficult to learn because it faces a creative paradox: learning to repeat past examples of creative success makes those specific examples more likely to recur, inhibiting the very creativity desired. This work argues that creativity is better modeled as an explicit process rather than as a property of individual artifacts, and proposes to learn the underlying generative principles behind the creative process. In particular, to escape the paradox, we introduce creative priming (CP), wherein a trained priming model generates a prompt-specific primer that assists a response model in being creative, explicitly decoupling the creative process from response generation. The priming model learns through GRPO, rewarding primers that lead to responses that are novel, high-quality, and diverse, thereby reinforcing the process that yields creative responses without reinforcing any specific response.

---


### 429. [CABrain: A Correlation-Aware Brain Foundation Model for EEG Decoding](https://arxiv.org/abs/2611.11782)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** SuGil Choi, Mooseop Kim, Chi Yoon Jeong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models have emerged as promising paradigms for decoding brain activity through large-scale self-supervised pretraining. Notably, most existing approaches employ masked patch reconstruction, in which randomly selected EEG patches are masked and recovered by the network. However, purely random masking may limit representation learning as informative patches from highly correlated channels often remain unmasked, causing the network to underutilize weakly correlated channels or serial dependencies. Furthermore, because these models are typically based on transformer architectures, their performance is influenced by the choice of positional encoding. Although positional encoding has been extensively explored in natural language processing and computer vision, few studies have adapted it to the unique characteristics of EEG signals. To address these limitations, this study introduces a conditional positional encoding method based on graph convolutional networks (GCNs) to explicitly model inter-channel correlations, along with an adaptive masking strategy that enhances representation learning by modulating the difficulty of masked patch reconstruction. To the best of our knowledge, this is the first study to integrate graph-based representations into conditional positional encoding and introduce adaptive masking within EEG foundation model pretraining. Experimental results on ten benchmark datasets demonstrate that the proposed GCN-based positional encoding and adaptive masking strategies, both individually and in combination, achieve state-of-the-art or competitive performance, highlighting their effectiveness in EEG foundation modeling.

---


### 430. [Benchmarking CNNs, Vision Transformers, and Foundation Models for Explainable Brain Tumor MRI Classification: Calibration, Decision Analysis, and External Validation](https://arxiv.org/abs/2611.11793)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Akwasi Asare  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for brain tumor MRI classification are usually compared by accuracy alone, on public datasets whose independence is rarely checked. We benchmarked six architectures: two convolutional networks (EfficientNetV2-M and ConvNeXt-V2-Tiny), two vision transformers (Swin-V2-S and ViT-L/16), and two foundation models (DINOv2-L and MedSigLIP-448), for four-class classification of 7,216 public MRI images. We assessed accuracy, calibration, explainability, ensembles, and decision curves, with every fitted quantity estimated on validation data only. Pixel-verified duplicate screening showed that 36% of the test images had a near-duplicate in the training data. Test accuracy ranged from 94.5% to 95.6%, with no pairwise difference after Holm correction, and fell to 90.3% to 91.7% on the 773 test images free of duplicates and shared patients. Ensembles did not outperform the best single model. Attribution maps passed a model-randomization test but localized expert-annotated tumors poorly. On 1,675 external BDNeuro-MRI images that did not duplicate the training data, accuracy ranged from 77.6% (MedSigLIP-448) to 95.0% (ViT-L/16), and 12 of 15 pairwise differences were significant. Internal accuracy on this public collection therefore did not distinguish the architectures, whereas the duplicate-filtered external test did.

---


### 431. [Adaptive Entropy-Sparing for Efficient Reasoning](https://arxiv.org/abs/2611.11901)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Cong Jiang, Xiaofeng Zhang, Tom Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) produce explicit chains of thought to improve transparency, but they frequently overthink, generating long yet inefficient reasoning chains that inflate computational costs and risk introducing errors. While numerous reinforcement learning methods struggle to penalize verbosity to achieve conciseness, they typically apply the penalty uniformly across lengthy sequences, which leads to credit confounding, that is, the failure to distinguish essential reasoning steps from superfluous ones. In this paper, we study a measurable proxy for this confounding: high-entropy tokens that often coincide with surface transition points where reasoning re-enters verification. Based on this insight, we propose Adaptive Entropy-Sparing (AES), which selectively spares high-entropy tokens that occur before an efficient in-group reference, while penalizing overlength high-entropy suffix tokens associated with superfluous branching. Our AES thereby navigates the suppression-exploration trade-off, reducing overthinking while preserving average reasoning accuracy. We also present an entropy-length model that motivates why local uncertainty can serve as a proxy for future reasoning cost. Across eight reasoning benchmarks, AES reduces reasoning length by up to 52.9% while increasing mean accuracy by up to 3.8% over the base models, consistently outperforming existing efficiency-oriented methods. Our code is available at this https URL.

---


### 432. [An Evaluation of Tabular Foundation Models as Training-Free World Models](https://arxiv.org/abs/2611.11921)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xian Yeow Lee, Ryoichi Takase, Ahmed Farahat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are widely considered to be a potential key component of model-based reinforcement learning and robot planning, but typically require task-specific training on substantial interaction data. We investigate whether a pretrained tabular foundation model (TabFM) can serve as a training-free dynamics model for world modeling by framing next-state prediction as in-context regression over transition pairs, and where such a model helps and where it breaks. Across synthetic dynamical systems and robot locomotion benchmarks, TabFM is more accurate than LSTM and MLP models trained from scratch on the same limited transitions in almost all settings, and among regressors fitted to the same data it is the most accurate on locomotion, while a Gaussian process is more accurate on smooth low-dimensional systems. However, models trained on the full dataset remain substantially better on most systems. When rolled out autoregressively over multiple steps, TabFM's accuracy depends strongly on how much context it is given. With a short context, its rollouts quickly degrade to the level of a trivial baseline, whereas with a long context they improve substantially and, on one locomotion task, exceed a trained LSTM. Inference is also about three orders of magnitude slower than an LSTM. Overall, in their current state, we find that training-free priors are useful as predictors when data are scarce and enough context is available, but they are not yet a substitute for trained world models in planning.

---


### 433. [Watching Itself Watch: Self-Auditing Visual Reliance for Video Reasoning](https://arxiv.org/abs/2611.11949)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rohan Dugad, Mi Luo, Kristen Grauman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning hinges on a small number of visually decisive tokens embedded in otherwise largely language-driven chains of thought. Yet prevailing post-training methods such as GRPO overlook this structure, assigning coarse trajectory-level rewards while requiring multiple rollouts and often costly external judges. We introduce Visually-Aware On-Policy Self-Distillation (VIOS), a post-training framework that identifies where a model under-utilizes visual evidence and concentrates learning at those positions. Our key insight is that a model can audit its own visual reliance: the divergence between its next-token distributions with and without the video reveals how strongly each prediction depends on the visual input. Measuring this reliance for both a student and an answer-privileged teacher exposes a per-token reliance gap, identifying positions where the teacher exploits visual evidence that the student overlooks. VIOS translates this signal into dense, targeted supervision through three complementary components: an exponential moving average (EMA) teacher that co-evolves with the student, a contrastive objective that encourages predictions to depend on the video, and a reliance-gap gate that focuses learning on visually under-utilized tokens. Crucially, VIOS requires only a single on-policy rollout from a single model, without external rewards, judges, or larger teachers. Across 12 benchmarks spanning general, temporal, spatial, knowledge-intensive, and long-video understanding, VIOS consistently improves three model backbones and outperforms contemporary video-reasoning systems, while training in over 9x fewer steps, 60x fewer FLOPs, and 111x fewer generated tokens. Project page: this https URL

---


### 434. [AnyBreak: Towards Jailbreaking Any T2I Model for Any Concept](https://arxiv.org/abs/2611.11980)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qi Lu, Zehui Guo, Yucheng Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models have demonstrated remarkable capabilities in image generation and editing, yet this progress has also introduced significant security risks. Prior work has shown that adversarial prompt can induce the generation of Not-Safe-For-Work (NSFW) content, including pornographic, violent, and graphic imagery. However, such attacks are typically mitigated by prompt filters and often rely on white-box assumptions. In this paper, we propose AnyBreak, a novel jailbreak framework that constructs adversarial images via multi-scale progressive semantic alignment. During the generation process, these adversarial images steer the generation trajectory in latent space towards unsafe data manifolds, enabling cross-modal transfer of malicious concepts from the text modality to the image modality. AnyBreak operates using only clean textual prompts and adversarial images at inference time, and can jailbreak any T2I models towards any malicious concepts in a fully black-box setting. We further introduce AnyBreak-V, an enhanced variant that incorporates a compensation term to bypass post-hoc safety checkers. Extensive experiments demonstrate that AnyBreak achieves high attack success rates while preserving visual fidelity and semantic consistency with the input prompts under black-box and clean-text constraints. Our findings reveal that existing T2I defense leave critical cross-modal attack surfaces insufficiently addressed. The code is available at this https URL.

---


### 435. [Do Time-Series Foundation Models Forecast Index-Futures Returns? A Preregistered Evaluation of Models, Metrics, and Input Representations](https://arxiv.org/abs/2611.12141)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rishabh Upadhyay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask whether the apparent forecasting skill of frozen time-series foundation models (TSFMs) on intraday index-futures returns is incremental skill. In a pre-registered evaluation on E-mini Nasdaq-100 (NQ) and E-mini S&P 500 (ES) futures, a common panel of five zero-shot models (Chronos-Bolt, Chronos-2, TimesFM 2.5, Moirai 2.0 and TiRex), plus separate experiments with Kronos, is compared with a no-change forecast at 5-120 minutes, using native prices, log returns, volatility-standardised returns and a volume clock as inputs. On a blind set opened once, 0 of 160 model-representation-horizon-market cells beat no-change, and a Hansen SPA test gives p = 1.000 on both markets; a later retrospective hold-out, scored as a descriptive check, gives 0 of 120. Input representations change forecast magnitude but not accuracy, and a transformation-aware ridge regression does as well. Several standard measures nevertheless suggest skill. Price-level correlation exceeds 0.9996, but no-change scores higher. Within-day RankIC across forecast origins rewards a trivial revert-to-mean rule (+0.35 at 30 minutes); we derive the expected within-day covariance under a random walk in closed form, and a sign-randomised null reproduces about 95% of the observed value. One model beats HAR for 5-minute volatility, but not the EWMA its input already contains. On strongly planted synthetic signals the models recover part of the signal at 5 minutes, and recovery deteriorates at 30 minutes. Benchmark-level success of TSFMs should therefore not be assumed to carry over to low-signal domains such as intraday returns.

---


### 436. [A forensic evaluation framework for egocentric foundation models: an EFM3D case study for crime scene reconstruction](https://arxiv.org/abs/2611.12259)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Davidson Chisom Onwubiko, Shahana Bano, Carlos Francisco Moreno-García  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models increasingly combine geometry, semantics, and spatial context for three-dimensional scene understanding, but their suitability for forensic crime scene reconstruction remains unclear. This study presents a structured forensic evaluation framework for egocentric foundation models and demonstrates it using the Egocentric Foundation Model for 3D (EFM3D). Four simulated indoor crime scenes were recorded with Meta Project Aria Gen~1 at Robert Gordon University's East Lodge House forensic training facility. The framework evaluates room-scale reconstruction, semantic scene understanding, computational performance, and forensic suitability. Across the four scenes, EFM3D generated meshes averaging $12{,}668\pm2{,}430$ vertices and $24{,}838\pm4{,}903$ faces, with 39,529 recorded semantic predictions spanning 21--24 categories at a mean confidence of 0.40. Because reference meshes and expert-labelled 3D ground truth were unavailable, these statistics are treated as descriptive outputs rather than measures of geometric or detection accuracy. Final inference runs processed $1{,}388\pm203$ snippets per scene at $0.69\pm0.01$ samples/s and required $50.77\pm6.12$ minutes per recording. A seven-criterion capability profile indicated stronger support for room geometry, furniture localisation, scene context, and spatial relationships than for fine-scale forensic evidence. The results position EFM3D as a complementary tool for contextual documentation and scene review rather than a replacement for high-fidelity forensic capture. The framework provides a reproducible basis for evaluating future egocentric foundation models in specialised forensic settings.

---


### 437. [Out-of-the-Box Tabular Foundation Models for Bayesian Optimization in Materials Discovery](https://arxiv.org/abs/2611.12491)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Klemens Flöge, Simon Bing, Leo Grinsztajn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization is widely used in active learning loops for materials science. Gaussian processes serve as the de-facto surrogate model family, but require task-dependent kernel choices and can lack the modeling capacity for complex relationships. Tabular foundation models (TFMs) have recently emerged as the state-of-the-art for predictive tasks on structured data, without requiring bespoke kernels or hyperparameter tuning. We evaluate two TFMs, TabPFN and TabICL, as out-of-the-box surrogate models on two standard materials science benchmarks, comparing against a large field of baselines encompassing Gaussian processes, random forests, and CatBoost. Our findings indicate that TFMs are highly competitive surrogate models across the two benchmarks, without task-specific training for active learning or GP kernel selection. Our results motivate developing TFMs further as surrogates for active learning in materials discovery.

---


### 438. [Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability and Perturbation Audit of Jev-Style Decision Models](https://arxiv.org/abs/2611.12521)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Julien Delaunay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> "System 1" decision models (pioneered by TypeSafe AI's Jev) replace autoregressive text generation with a single forward pass returning typed probability distributions over declared schemas (Choice, Score, Noul). While deployed for low-latency routing and automated triage, their statistical calibration and post-hoc explainability remain uncharacterized. We introduce an open, deterministic audit benchmark evaluating System 1 decision models across calibration under label-preserving perturbations, cross-question interference, and post-hoc attribution faithfulness. Evaluating five open-weight models (0.8B to 27B) alongside generative System 2 baselines -- both single-token logprob scoring and structured JSON/CoT decoding -- across NLI (e-SNLI), adversarial syntactic shortcuts (HANS), synthetic clinical triage (N=900), prompt injection defense (Tensor Trust, N=250), and an 86-case logic-gate trigger suite yields five findings: (1) provider confidence is an exact closed-form dispersion transform (1 - H(p)/ln K on sub-10B models; normalized margin on Clef-27B) rather than empirical accuracy; (2) bundling multiple questions in one request induces directional cross-question interference (11.7% to 22.4% binary flips on Tev1-0.8B, vs. 0.1% to 0.2% on Tev1-4B); (3) System 1 models with >= 4B parameters are faster and better calibrated under syntactic shifts (ECE_w = 0.030 to 0.087) than logprob (0.144) and JSON (0.378) baselines; (4) for prompt-injection defense (N=250), >= 4B models achieve 0.988 to 0.998 AUROC with up to 95.2% recall and 0.0% false alarms at 48 to 60 ms; and (5) single-pass inference makes 512-coalition XAI interactive (1.3 to 3.2 s/input), while KernelSHAP with a logit link (S1-SHAP) mitigates softmax saturation on disjunctive OR gates (89.3% to 100.0% gate recovery vs. 57.1% to 82.1% in prob space; p_adj = 0.004).

---


> [!TIP]
> 当前位于：**401-438**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-438**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
