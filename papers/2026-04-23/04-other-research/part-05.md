# 📦 其他研究 | 2026年04月23日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-244**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-244**

---

### 201. [TeamFusion: Supporting Open-ended Teamwork with Multi-Agent Systems](https://arxiv.org/abs/2604.19589)

**<font color=#1a73e8>作者：</font>** Jiale Liu, Victor S. Bursztyn, Lin Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In open-ended domains, teams must reconcile diverse viewpoints to produce strong deliverables. Answer aggregation approaches commonly used in closed domains are ill-suited to this setting, as they tend to suppress minority perspectives rather than resolve underlying disagreements. We present TeamFusion, a multi-agent system designed to support teamwork in open-ended domains by: 1. Instantiating a proxy agent for each team member conditioned on their expressed preferences; 2. Conducting a structured discussion to surface agreements and disagreements; and 3. Synthesizing more consensus-oriented deliverables that feed into new iterations of discussion and refinement. We evaluate TeamFusion on two teamwork tasks where team members can assess how well their individual views are represented in team decisions and how consensually strong the final deliverables are, finding that it outperforms direct aggregation baselines across metrics, tasks, and team configurations.

---


### 202. [Structure-Semantic Decoupled Modulation of Global Geospatial Embeddings for High-Resolution Remote Sensing Mapping](https://arxiv.org/abs/2604.19591)

**<font color=#1a73e8>作者：</font>** Jienan Lyu, Miao Yang, Jinchen Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained high-resolution remote sensing mapping typically relies on localized visual features, which restricts cross-domain generalizability and often leads to fragmented predictions of large-scale land covers. While global geospatial foundation models offer powerful, generalizable representations, directly fusing their high-dimensional implicit embeddings with high-resolution visual features frequently triggers feature interference and spatial structure degradation due to a severe semantic-spatial gap. To overcome these limitations, we propose a Structure-Semantic Decoupled Modulation (SSDM) framework, which decouples global geospatial representations into two complementary cross-modal injection pathways. First, the structural prior modulation branch introduces the macroscopic receptive field priors from global representations into the self-attention modules of the high-resolution encoder. By guiding local feature extraction with holistic structural constraints, it effectively suppresses prediction fragmentation caused by high-frequency detail noise and excessive intra-class variance. Second, the global semantic injection branch explicitly aligns holistic context with the deep high-resolution feature space and directly supplements global semantics via cross-modal integration, thereby significantly enhancing the semantic consistency and category-level discrimination of complex land covers. Extensive experiments demonstrate that our method achieves state-of-the-art performance compared to existing cross-modal fusion approaches. By unleashing the potential of global embeddings, SSDM consistently improves high-resolution mapping accuracy across diverse scenarios, providing a universal and effective paradigm for integrating geospatial foundation models into high-resolution vision tasks.

---


### 203. [An Efficient Black-Box Reduction from Online Learning to Multicalibration, and a New Route to $Φ$-Regret Minimization](https://arxiv.org/abs/2604.19592)

**<font color=#1a73e8>作者：</font>** Gabriele Farina, Juan Carlos Perdomo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give a Gordon-Greenwald-Marks (GGM) style black-box reduction from online learning to online multicalibration. Concretely, we show that to achieve high-dimensional multicalibration with respect to a class of functions H, it suffices to combine any no-regret learner over H with an expected variational inequality (EVI) solver. We also prove a converse statement showing that efficient multicalibration implies efficient EVI solving, highlighting how EVIs in multicalibration mirror the role of fixed points in the GGM result for $\Phi$-regret.
This first set of results resolves the main open question in Garg, Jung, Reingold, and Roth (SODA '24), showing that oracle-efficient online multicalibration with $\sqrt{T}$-type guarantees is possible in full generality. Furthermore, our GGM-style reduction unifies the analyses of existing online multicalibration algorithms, enables new algorithms for challenging environments with delayed observations or censored outcomes, and yields the first efficient black-box reduction between online learning and multiclass omniprediction.
Our second main result is a fine-grained reduction from high-dimensional online multicalibration to (contextual) $\Phi$-regret minimization. Together with our first result, this establishes a new route from external regret to Phi-regret that bypasses sophisticated fixed-point or semi-separation machinery, dramatically simplifies a result of Daskalakis, Farina, Fishelson, Pipis, and Schneider (STOC '25) while improving rates, and yields new algorithms that are robust to richer deviation classes, such as those belonging to any reproducing kernel Hilbert space.

---


### 204. [RoLegalGEC: Legal Domain Grammatical Error Detection and Correction Dataset for Romanian](https://arxiv.org/abs/2604.19593)

**<font color=#1a73e8>作者：</font>** Mircea Timpuriu, Dumitru-Clementin Cercel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The importance of clear and correct text in legal documents cannot be understated, and, consequently, a grammatical error correction tool meant to assist a professional in the law must have the ability to understand the possible errors in the context of a legal environment, correcting them accordingly, and implicitly needs to be trained in the same environment, using realistic legal data. However, the manually annotated data required by such a process is in short supply for languages such as Romanian, much less for a niche domain. The most common approach is the synthetic generation of parallel data; however, it requires a structured understanding of the Romanian grammar. In this paper, we introduce, to our knowledge, the first Romanian-language parallel dataset for the detection and correction of grammatical errors in the legal domain, RoLegalGEC, which aggregates 350,000 examples of errors in legal passages, along with error annotations. Moreover, we evaluate several neural network models that transform the dataset into a valuable tool for both detecting and correcting grammatical errors, including knowledge-distillation Transformers, sequence tagging architectures for detection, and a variety of pre-trained text-to-text Transformer models for correction. We consider that the set of models, together with the novel RoLegalGEC dataset, will enrich the resource base for further research on Romanian.

---


### 205. [PC2Model: ISPRS benchmark on 3D point cloud to model registration](https://arxiv.org/abs/2604.19596)

**<font color=#1a73e8>作者：</font>** Mehdi Maboudi, Said Harb, Jackson Ferrao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud registration involves aligning one point cloud with another or with a three-dimensional (3D) model, enabling the integration of multimodal data into a unified representation. This is essential in applications such as construction monitoring, autonomous driving, robotics, and virtual or augmented reality (VR/AR).With the increasing accessibility of point cloud acquisition technologies, such as Light Detection and Ranging (LiDAR) and structured light scanning, along with recent advances in deep learning, the research focus has increasingly shifted towards downstream tasks, particularly point cloud-to-model (PC2Model) registration. While data-driven methods aim to automate this process, they struggle with sparsity, noise, clutter, and occlusions in real-world scans, which limit their performance. To address these challenges, this paper introduces the PC2Model benchmark, a publicly available dataset designed to support the training and evaluation of both classical and data-driven methods. Developed under the leadership of ICWG II/Ib, the PC2Model benchmark adopts a hybrid design that combines simulated point clouds with, in some cases, real-world scans and their corresponding 3D models. Simulated data provide precise ground truth and controlled conditions, while real-world data introduce sensor and environmental artefacts. This design supports robust training and evaluation across domains and enables the systematic analysis of model transferability from simulated to real-world scenarios. The dataset is publicly accessible at: this https URL.

---


### 206. [AblateCell: A Reproduce-then-Ablate Agent for Virtual Cell Repositories](https://arxiv.org/abs/2604.19606)

**<font color=#1a73e8>作者：</font>** Xue Xia, Chengkai Yao, Mingyu Tsoi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic ablations are essential to attribute performance gains in AI Virtual Cells, yet they are rarely performed because biological repositories are under-standardized and tightly coupled to domain-specific data and formats. While recent coding agents can translate ideas into implementations, they typically stop at producing code and lack a verifier that can reproduce strong baselines and rigorously test which components truly matter. We introduce AblateCell, a reproduce-then-ablate agent for virtual cell repositories that closes this verification gap. AblateCell first reproduces reported baselines end-to-end by auto-configuring environments, resolving dependency and data issues, and rerunning official evaluations while emitting verifiable artifacts. It then conducts closed-loop ablation by generating a graph of isolated repository mutations and adaptively selecting experiments under a reward that trades off performance impact and execution cost. Evaluated on three single-cell perturbation prediction repositories (CPA, GEARS, BioLORD), AblateCell achieves 88.9% (+29.9% to human expert) end-to-end workflow success and 93.3% (+53.3% to heuristic) accuracy in recovering ground-truth critical components. These results enable scalable, repository-grounded verification and attribution directly on biological codebases.

---


### 207. [Volume Transformer: Revisiting Vanilla Transformers for 3D Scene Understanding](https://arxiv.org/abs/2604.19609)

**<font color=#1a73e8>作者：</font>** Kadir Yilmaz, Adrian Kruse, Tristan Höfer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformers have become a common foundation across deep learning, yet 3D scene understanding still relies on specialized backbones with strong domain priors. This keeps the field isolated from the broader Transformer ecosystem, limiting the transfer of new advances as well as the benefits of increasingly optimized software and hardware stacks. To bridge this gap, we adapt the vanilla Transformer encoder to 3D scenes with minimal modifications. Given an input 3D scene, we partition it into volumetric patch tokens, process them with full global self-attention, and inject positional information via a 3D extension of rotary positional embeddings. We call the resulting model the Volume Transformer (Volt) and apply it to 3D semantic segmentation. Naively training Volt on standard 3D benchmarks leads to shortcut learning, highlighting the limited scale of current 3D supervision. To overcome this, we introduce a data-efficient training recipe based on strong 3D augmentations, regularization, and distillation from a convolutional teacher, making Volt competitive with state-of-the-art methods. We then scale supervision through joint training on multiple datasets and show that Volt benefits more from increased scale than domain-specific 3D backbones, achieving state-of-the-art results across indoor and outdoor datasets. Finally, when used as a drop-in backbone in a standard 3D instance segmentation pipeline, Volt again sets a new state of the art, highlighting its potential as a simple, scalable, general-purpose backbone for 3D scene understanding.

---


### 208. [The "Small World of Words" German Free-Association Norms](https://arxiv.org/abs/2604.19620)

**<font color=#1a73e8>作者：</font>** Samuel Aeschbach, Rui Mata, Kaidi Lõo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Free-association norms provide essential empirical data for investigating linguistic, semantic, and cultural phenomena in the cognitive sciences. Although large-scale norms exist for languages such as English, Dutch, Spanish, and Mandarin Chinese, no comparable resource has been available for German. To address this gap, we present free-association norms for 5,877 German cue words as part of the German version of the multilingual Small World of Words (SWOW) project. We describe the data collection procedures, participant characteristics, and our comprehensive preprocessing pipeline before introducing the resulting SWOW-DE data set. Using data from three established psycholinguistic paradigms, we show that SWOW-DE norms robustly predict performance in lexical decision tasks, relatedness judgments, and psycholinguistic word ratings. Furthermore, we demonstrate that SWOW-DE responses compare favorably with existing German resources and provide a preliminary cross-linguistic comparison revealing both shared and language-specific association patterns, highlighting promising directions for future research. Overall, SWOW-DE represents the largest collection of German free associations to date and offers a unique resource for linguistic, psychological, and cross-cultural research.

---


### 209. [SAGE: Training-Free Semantic Evidence Composition for Edge-Cloud Inference under Hard Uplink Budgets](https://arxiv.org/abs/2604.19623)

**<font color=#1a73e8>作者：</font>** Inhyeok Choi, Hyuncheol Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge-cloud hybrid inference offloads difficult inputs to a powerful remote model, but the uplink channel imposes hard per-request constraints on the number of bits that can be transmitted. We show that selecting transmitted content based solely on attention-based importance, the standard approach in collaborative inference, is inherently limited under hard budgets. Two findings support this claim. First, replacing high-importance units with low-importance but complementary ones improves server accuracy. This shows that what matters is not individual importance but how well the transmitted set covers diverse aspects of the input. Second, spatially uniform selection without any content information achieves competitive accuracy at moderate budgets. This confirms that spatial coverage alone carries independent value. Based on this analysis, we propose SAGE (Semantic Attention-Guided Evidence), a principled, training-free method that combines importance filtering with embedding-diversity sampling. SAGE achieves 93% of the server ceiling in offloaded accuracy while transmitting fewer than half of the available evidence units on ImageNet-1K, substantially outperforming importance-only composition.

---


### 210. [GRAFT: Geometric Refinement and Fitting Transformer for Human Scene Reconstruction](https://arxiv.org/abs/2604.19624)

**<font color=#1a73e8>作者：</font>** Pradyumna YM, Yuxuan Xue, Yue Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing physically plausible 3D human-scene interactions (HSI) from a single image currently presents a trade-off: optimization based methods offer accurate contact but are slow (~20s), while feed-forward approaches are fast yet lack explicit interaction reasoning, producing floating and interpenetration artifacts.
Our key insight is that geometry-based human--scene fitting can be amortized into fast feed-forward inference. We present GRAFT (Geometric Refinement And Fitting Transformer), a learned HSI prior that predicts Interaction Gradients: corrective parameter updates that iteratively refine human meshes by reasoning about their 3D relationship to the surrounding scene.
GRAFT encodes the interaction state into compact body-anchored tokens, each grounded in the scene geometry via Geometric Probes that capture spatial relationships with nearby surfaces.
A lightweight transformer recurrently updates human meshes and re-probes the scene, ensuring the final pose aligns with both learned priors and observed geometry.
GRAFT operates either as an end-to-end reconstructor using image features, or with geometry alone as a transferable plug-and-play HSI prior that improves feed-forward methods without retraining.
Experiments show GRAFT improves interaction quality by up to 113% over state-of-the-art feed-forward methods and matches optimization-based interaction quality at ${\sim}50{\times}$ lower runtime, while generalizing seamlessly to in-the-wild multi-person scenes and being preferred in 64.8% of three-way user study. Project page: this https URL .

---


### 211. [Adding Compilation Metadata To Binaries To Make Disassembly Decidable](https://arxiv.org/abs/2604.19628)

**<font color=#1a73e8>作者：</font>** Daniel Engel, Freek Verbeek, Pranav Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The binary executable format is the standard method for distributing and executing software. Yet, it is also as opaque a representation of software as can be. If the binary format were augmented with metadata that provides security-relevant information, such as which data is intended by the compiler to be executable instructions, or how memory regions are expected to be bounded, that would dramatically improve the safety and maintainability of software. In this paper, we propose a binary format that is a middle ground between a stripped black-box binary and open source. We provide a tool that generates metadata capturing the compiler's intent and inserts it into the binary. This metadata enables lifting to a correct and recompilable higher-level representation and makes analysis and instrumentation more reliable. Our evaluation shows that adding metadata does not affect runtime behavior or performance. Compared to DWARF, our metadata is roughly 17% of its size. We validate correctness by compiling a comprehensive set of real-world C and C++ binaries and demonstrating that they can be lifted, instrumented, and recompiled without altering their behavior.

---


### 212. [CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers](https://arxiv.org/abs/2604.19632)

**<font color=#1a73e8>作者：</font>** Weidong Chen, Dexiang Hong, Zhendong Mao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphic design images consist of multiple editable layers, such as text, background, and decorative elements, while most generative models produce rasterized outputs without explicit layer structures, limiting downstream editing. Existing graphic design parsing methods typically rely on multi-stage pipelines combining layout prediction, matting, and inpainting, which suffer from error accumulation and limited controllability. We propose a hybrid generative framework for raster-to-layer graphic design parsing that decomposes a design image into editable text, background, and sticker layers. Text regions are parsed using a vision-language model into a text rendering protocol, enabling faithful reconstruction and flexible re-editing, while background and sticker layers are generated using a multi-branch diffusion architecture with RGBA support. We further introduce ParserReward and integrate it with Group Relative Policy Optimization to align generation quality with human design preferences. Extensive experiments on two challenging datasets, \emph{i.e.,} the Parser-40K and Crello datasets, demonstrate superior performance over existing methods, \emph{eg.,} achieving an overall average improvement of 23.7\% across all metrics.

---


### 213. [CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation](https://arxiv.org/abs/2604.19636)

**<font color=#1a73e8>作者：</font>** Xiangyang Luo, Xiaozhe Xin, Tao Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing human--object interaction (HOI) videos has broad practical value in e-commerce, digital advertising, and virtual marketing. However, current diffusion models, despite their photorealistic rendering capability, still frequently fail on (i) the structural stability of sensitive regions such as hands and faces and (ii) physically plausible contact (e.g., avoiding hand--object interpenetration). We present CoInteract, an end-to-end framework for HOI video synthesis conditioned on a person reference image, a product reference image, text prompts, and speech audio. CoInteract introduces two complementary designs embedded into a Diffusion Transformer (DiT) backbone. First, we propose a Human-Aware Mixture-of-Experts (MoE) that routes tokens to lightweight, region-specialized experts via spatially supervised routing, improving fine-grained structural fidelity with minimal parameter overhead. Second, we propose Spatially-Structured Co-Generation, a dual-stream training paradigm that jointly models an RGB appearance stream and an auxiliary HOI structure stream to inject interaction geometry priors. During training, the HOI stream attends to RGB tokens and its supervision regularizes shared backbone weights; at inference, the HOI branch is removed for zero-overhead RGB generation. Experimental results demonstrate that CoInteract significantly outperforms existing methods in structural stability, logical consistency, and interaction realism.

---


### 214. [CoCo-SAM3: Harnessing Concept Conflict in Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2604.19648)

**<font color=#1a73e8>作者：</font>** Yanhui Chen, Baoyao Yang, Siqi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> SAM3 advances open-vocabulary semantic segmentation by introducing a prompt-driven mask generation paradigm. However, in multi-class open-vocabulary scenarios, masks generated independently from different category prompts lack a unified and inter-class comparable evidence scale, often resulting in overlapping coverage and unstable competition. Moreover, synonymous expressions of the same concept tend to activate inconsistent semantic and spatial evidence, leading to intra-class drift that exacerbates inter-class conflicts and compromises overall inference stability. To address these issues, we propose CoCo-SAM3 (Concept-Conflict SAM3), which explicitly decouples inference into intra-class enhancement and inter-class competition. Our method first aligns and aggregates evidence from synonymous prompts to strengthen concept consistency. It then performs inter-class competition on a unified comparable scale, enabling direct pixel-wise comparisons among all candidate classes. This mechanism stabilizes multi-class inference and effectively mitigates inter-class conflicts. Without requiring any additional training, CoCo-SAM3 achieves consistent improvements across eight open-vocabulary semantic segmentation benchmarks.

---


### 215. [A Dual Perspective on Synthetic Trajectory Generators: Utility Framework and Privacy Vulnerabilities](https://arxiv.org/abs/2604.19653)

**<font color=#1a73e8>作者：</font>** Aya Cherigui, Florent Guépin, Arnaud Legendre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human mobility data are used in numerous applications, ranging from public health to urban planning. Human mobility is inherently sensitive, as it can contain information such as religious beliefs and political affiliations. Historically, it has been proposed to modify the information using techniques such as aggregation, obfuscation, or noise addition, to adequately protect privacy and eliminate concerns. As these methods come at a great cost in utility, new methods leveraging development in generative models, were introduced. The extent to which such methods answer the privacy-utility trade-off remains an open problem. In this paper, we introduced a first step towards solving it, by the introduction and application of a new framework for utility evaluation. Furthermore, we provide evidence that privacy evaluation remains a great challenge to consider and that it should be tackled through adversarial evaluation in accordance with the current EU regulation. We propose a new membership inference attack against a subcategory of generative models, even though this subcategory was deemed private due to its resistance over the trajectory user-linking problem.

---


### 216. [An AI Agent Execution Environment to Safeguard User Data](https://arxiv.org/abs/2604.19657)

**<font color=#1a73e8>作者：</font>** Robert Stanley, Avi Verma, Lillian Tsai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents promise to serve as general-purpose personal assistants for their users, which requires them to have access to private user data (e.g., personal and financial information). This poses a serious risk to security and privacy. Adversaries may attack the AI model (e.g., via prompt injection) to exfiltrate user data. Furthermore, sharing private data with an AI agent requires users to trust a potentially unscrupulous or compromised AI model provider with their private data.
This paper presents GAAP (Guaranteed Accounting for Agent Privacy), an execution environment for AI agents that guarantees confidentiality for private user data. Through dynamic and directed user prompts, GAAP collects permission specifications from users describing how their private data may be shared, and GAAP enforces that the agent's disclosures of private user data, including disclosures to the AI model and its provider, comply with these specifications. Crucially, GAAP provides this guarantee deterministically, without trusting the agent with private user data, and without requiring any AI model or the user prompt to be free of attacks.
GAAP enforces the user's permission specification by tracking how the AI agent accesses and uses private user data. It augments Information Flow Control with novel persistent data stores and annotations that enable it to track the flow of private information both across execution steps within a single task, and also over multiple tasks separated in time. Our evaluation confirms that GAAP blocks all data disclosure attacks, including those that make other state-of-the-art systems disclose private user data to untrusted parties, without a significant impact on agent utility.

---


### 217. [Disentangling Damage from Operational Variability: A Label-Free Self-Supervised Representation Learning Framework for Output-Only Structural Damage Identification](https://arxiv.org/abs/2604.19658)

**<font color=#1a73e8>作者：</font>** Xudong Jian, Charikleia Stoura, Simon Scandella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Damage identification is a core task in structural health monitoring. In practice, however, its reliability is often compromised by confounding non-damage effects, such as variations in excitation and environmental conditions, which can induce changes comparable to or larger than those caused by structural damage. To address this challenge, this study proposes a self-supervised label-free disentangled representation learning framework for robust vibration-based structural damage identification. The proposed framework employs an autoencoder with two latent representations to learn directly from raw vibration acceleration signals. A self-supervised invariance regularization, implemented via Variance-Invariance-Covariance Regularization (VICReg), is imposed on one latent representation using baseline data where structural damage is assumed constant but operational and environmental conditions vary. In addition, a frequency-domain constraint is introduced to enforce agreement between the power spectral density reconstructed from the latent representation and that computed from the corresponding input time series. Together, these mechanisms promote disentanglement, enabling the learned representation to be sensitive to damage-related characteristics while remaining invariant to nuisance variability. The framework is trained in a fully end-to-end and label-free manner, requiring no prior information on damage, excitation, or environmental conditions, making it well-suited for real-world applications. Its effectiveness is validated on two distinct real-world vibration datasets, including a bridge and a gearbox. The results demonstrate robustness to operational variability, strong generalization capability, and good performance in both damage detection and quantification.

---


### 218. [Chat2Workflow: A Benchmark for Generating Executable Visual Workflows with Natural Language](https://arxiv.org/abs/2604.19667)

**<font color=#1a73e8>作者：</font>** Yi Zhong, Buqiang Xu, Yijun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> At present, executable visual workflows have emerged as a mainstream paradigm in real-world industrial deployments, offering strong reliability and controllability. However, in current practice, such workflows are almost entirely constructed through manual engineering: developers must carefully design workflows, write prompts for each step, and repeatedly revise the logic as requirements evolve-making development costly, time-consuming, and error-prone. To study whether large language models can automate this multi-round interaction process, we introduce Chat2Workflow, a benchmark for generating executable visual workflows directly from natural language, and propose a robust agentic framework to mitigate recurrent execution errors. Chat2Workflow is built from a large collection of real-world business workflows, with each instance designed so that the generated workflow can be transformed and directly deployed to practical workflow platforms such as Dify and Coze. Experimental results show that while state-of-the-art language models can often capture high-level intent, they struggle to generate correct, stable, and executable workflows, especially under complex or changing requirements. Although our agentic framework yields up to 5.34% resolve rate gains, the remaining real-world gap positions Chat2Workflow as a foundation for advancing industrial-grade automation. Code is available at this https URL.

---


### 219. [HardNet++: Nonlinear Constraint Enforcement in Neural Networks](https://arxiv.org/abs/2604.19669)

**<font color=#1a73e8>作者：</font>** Andrea Goertzen, Kaveh Alim, Navid Azizan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enforcing constraint satisfaction in neural network outputs is critical for safety, reliability, and physical fidelity in many control and decision-making applications. While soft-constrained methods penalize constraint violations during training, they do not guarantee constraint adherence during inference. Other approaches guarantee constraint satisfaction via specific parameterizations or a projection layer, but are tailored to specific forms (e.g., linear constraints), limiting their utility in other general problem settings. Many real-world problems of interest are nonlinear, motivating the development of methods that can enforce general nonlinear constraints. To this end, we introduce HardNet++, a constraint-enforcement method that simultaneously satisfies linear and nonlinear equality and inequality constraints. Our approach iteratively adjusts the network output via damped local linearizations. Each iteration is differentiable, admitting an end-to-end training framework, where the constraint satisfaction layer is active during training. We show that under certain regularity conditions, this procedure can enforce nonlinear constraint satisfaction to arbitrary tolerance. Finally, we demonstrate tight constraint adherence without loss of optimality in a learning-for-optimization context, where we apply this method to a model predictive control problem with nonlinear state constraints.

---


### 220. [Budgeted Online Influence Maximization](https://arxiv.org/abs/2604.19672)

**<font color=#1a73e8>作者：</font>** Pierre Perrault, Jennifer Healey, Zheng Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a new budgeted framework for online influence maximization, considering the total cost of an advertising campaign instead of the common cardinality constraint on a chosen influencer set. Our approach better models the real-world setting where the cost of influencers varies and advertisers want to find the best value for their overall social advertising budget. We propose an algorithm assuming an independent cascade diffusion model and edge level semi-bandit feedback, and provide both theoretical and experimental results. Our analysis is also valid for the cardinality constraint setting and improves the state of the art regret bound in this case.

---


### 221. [MedFlowSeg: Flow Matching for Medical Image Segmentation with Frequency-Aware Attention](https://arxiv.org/abs/2604.19675)

**<font color=#1a73e8>作者：</font>** Zhi Chen, Runze Hu, Le Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching has recently emerged as a principled framework for learning continuous-time transport maps, enabling efficient deterministic generation without relying on stochastic diffusion processes. While generative modeling has shown promise for medical image segmentation, particularly in capturing uncertainty and complex anatomical variability, existing approaches are predominantly built upon diffusion models, which incur substantial computational overhead due to iterative sampling and are often constrained by UNet-based parameterizations. In this work, we introduce MedFlowSeg, a conditional flow matching framework that formulates medical image segmentation as learning a time-dependent vector field that transports a simple prior distribution to the target segmentation distribution. This formulation enables one-step deterministic inference while preserving the expressiveness of generative modeling. We further develop a dual-conditioning mechanism to incorporate structured priors into the learned flow. Specifically, we propose a Dual-Branch Spatial Attention module that injects multi-scale structural information into the flow field, and a Frequency-Aware Attention module that models cross-domain interactions between spatial and spectral representations via discrepancy-aware fusion and time-dependent modulation. Together, these components provide an effective parameterization of conditional flows that capture both global anatomical structure and fine-grained boundary details. We provide extensive empirical validation across multiple medical imaging modalities, demonstrating that MedFlowSeg achieves state-of-the-art performance while significantly reducing computational cost compared to diffusion-based methods. Our results highlight the potential of flow matching as a theoretically grounded and computationally efficient alternative for generative medical image segmentation.

---


### 222. [Exploring Language-Agnosticity in Function Vectors: A Case Study in Machine Translation](https://arxiv.org/abs/2604.19678)

**<font color=#1a73e8>作者：</font>** Nurkhan Laiyk, Gerard I. Gállego, Javier Ferrando 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Function vectors (FVs) are vector representations of tasks extracted from model activations during in-context learning. While prior work has shown that multilingual model representations can be language-agnostic, it remains unclear whether the same holds for function vectors. We study whether FVs exhibit language-agnosticity, using machine translation as a case study. Across three decoder-only multilingual LLMs, we find that translation FVs extracted from a single English$\rightarrow$Target direction transfer to other target languages, consistently improving the rank of correct translation tokens across multiple unseen languages. Ablation results show that removing the FV degrades translation across languages with limited impact on unrelated tasks. We further show that base-model FVs transfer to instruction-tuned variants and partially generalize from word-level to sentence-level translation.

---


### 223. [MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679)

**<font color=#1a73e8>作者：</font>** Liyang Li, Wen Wang, Canyu Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Diffusion Transformers (DiTs) have enabled high-quality joint audio-video generation, producing videos with synchronized audio within a single model. However, existing controllable generation frameworks are typically restricted to video-only control. This restricts comprehensive controllability and often leads to suboptimal cross-modal alignment. To bridge this gap, we present MMControl, which enables users to perform Multi-Modal Control in joint audio-video generation. MMControl introduces a dual-stream conditional injection mechanism. It incorporates both visual and acoustic control signals, including reference images, reference audio, depth maps, and pose sequences, into a joint generation process. These conditions are injected through bypass branches into a joint audio-video Diffusion Transformer, enabling the model to simultaneously generate identity-consistent video and timbre-consistent audio under structural constraints. Furthermore, we introduce modality-specific guidance scaling, which allows users to independently and dynamically adjust the influence strength of each visual and acoustic condition at inference time. Extensive experiments demonstrate that MMControl achieves fine-grained, composable control over character identity, voice timbre, body pose, and scene layout in joint audio-video generation.

---


### 224. [IR-Flow: Bridging Discriminative and Generative Image Restoration via Rectified Flow](https://arxiv.org/abs/2604.19680)

**<font color=#1a73e8>作者：</font>** Zihao Fan, Xin Lu, Jie Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In image restoration, single-step discriminative mappings often lack fine details via expectation learning, whereas generative paradigms suffer from inefficient multi-step sampling and noise-residual coupling. To address this dilemma, we propose IR-Flow, a novel image restoration method based on Rectified Flow that serves as a unified framework bridging the gap between discriminative and generative paradigms. Specifically, we first construct multilevel data distribution flows, which expand the ability of models to learn from and adapt to various levels of degradation. Subsequently, cumulative velocity fields are proposed to learn transport trajectories across varying degradation levels, guiding intermediate states toward the clean target, while a multi-step consistency constraint is presented to enforce trajectory coherence and boost few-step restoration performance. We show that directly establishing a linear transport flow between degraded and clean image domains not only enables fast inference but also improves adaptability to out-of-distribution degradations. Extensive evaluations on deraining, denoising and raindrop removal tasks demonstrate that IR-Flow achieves competitive quantitative results with only a few sampling steps, offering an efficient and flexible framework that maintains an excellent distortion-perception balance. Our code is available at this https URL.

---


### 225. [PREF-XAI: Preference-Based Personalized Rule Explanations of Black-Box Machine Learning Models](https://arxiv.org/abs/2604.19684)

**<font color=#1a73e8>作者：</font>** Salvatore Greco, Jacek Karolczak, Roman Słowiński 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainable artificial intelligence (XAI) has predominantly focused on generating model-centric explanations that approximate the behavior of black-box models. However, such explanations often overlook a fundamental aspect of interpretability: different users require different explanations depending on their goals, preferences, and cognitive constraints. Although recent work has explored user-centric and personalized explanations, most existing approaches rely on heuristic adaptations or implicit user modeling, lacking a principled framework for representing and learning individual preferences. In this paper, we consider Preference-Based Explainable Artificial Intelligence (PREF-XAI), a novel perspective that reframes explanation as a preference-driven decision problem. Within PREF-XAI, explanations are not treated as fixed outputs, but as alternatives to be evaluated and selected according to user-specific criteria. In the PREF-XAI perspective, here we propose a methodology that combines rule-based explanations with formal preference learning. User preferences are elicited through a ranking of a small set of candidate explanations and modeled via an additive utility function inferred using robust ordinal regression. Experimental results on real-world datasets show that PREF-XAI can accurately reconstruct user preferences from limited feedback, identify highly relevant explanations, and discover novel explanatory rules not initially considered by the user. Beyond the proposed methodology, this work establishes a connection between XAI and preference learning, opening new directions for interactive and adaptive explanation systems.

---


### 226. [An Answer is just the Start: Related Insight Generation for Open-Ended Document-Grounded QA](https://arxiv.org/abs/2604.19685)

**<font color=#1a73e8>作者：</font>** Saransh Sharma, Pritika Ramu, Aparna Garimella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering open-ended questions remains challenging for AI systems because it requires synthesis, judgment, and exploration beyond factual retrieval, and users often refine answers through multiple iterations rather than accepting a single response. Existing QA benchmarks do not explicitly support this refinement process. To address this gap, we introduce a new task, document-grounded related insight generation, where the goal is to generate additional insights from a document collection that help improve, extend, or rethink an initial answer to an open-ended question, ultimately supporting richer user interaction and a better overall question answering experience. We curate and release SCOpE-QA (Scientific Collections for Open-Ended QA), a dataset of 3,000 open-ended questions across 20 research collections. We present InsightGen, a two-stage approach that first constructs a thematic representation of the document collection using clustering, and then selects related context based on neighborhood selection from the thematic graph to generate diverse and relevant insights using LLMs. Extensive evaluation on 3,000 questions using two generation models and two evaluation settings shows that InsightGen consistently produces useful, relevant, and actionable insights, establishing a strong baseline for this new task.

---


### 227. [Planning in entropy-regularized Markov decision processes and games](https://arxiv.org/abs/2604.19695)

**<font color=#1a73e8>作者：</font>** Jean-Bastien Grill, Omar Darwiche Domingues, Pierre Ménard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose SmoothCruiser, a new planning algorithm for estimating the value function in entropy-regularized Markov decision processes and two-player games, given a generative model of the environment. SmoothCruiser makes use of the smoothness of the Bellman operator promoted by the regularization to achieve problem-independent sample complexity of order O~(1/epsilon^4) for a desired accuracy epsilon, whereas for non-regularized settings there are no known algorithms with guaranteed polynomial sample complexity in the worst case.

---


### 228. [On two ways to use determinantal point processes for Monte Carlo integration](https://arxiv.org/abs/2604.19698)

**<font color=#1a73e8>作者：</font>** Guillaume Gautier, Rémi Bardenet, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The standard Monte Carlo estimator $\widehat{I}_N^{\mathrm{MC}}$ of $\int fd\omega$ relies on independent samples from $\omega$ and has variance of order $1/N$. Replacing the samples with a determinantal point process (DPP), a repulsive distribution, makes the estimator consistent, with variance rates that depend on how the DPP is adapted to $f$ and $\omega$. We examine two existing DPP-based estimators: one by Bardenet & Hardy (2020) with a rate of $\mathcal{O}(N^{-(1+1/d)})$ for smooth $f$, but relying on a fixed DPP. The other, by Ermakov & Zolotukhin (1960), is unbiased with rate of order $1/N$, like Monte Carlo, but its DPP is tailored to $f$. We revisit these estimators, generalize them to continuous settings, and provide sampling algorithms.

---


### 229. [Epistemic orientation in parliamentary discourse is associated with deliberative democracy](https://arxiv.org/abs/2604.19699)

**<font color=#1a73e8>作者：</font>** Segun Aroyehun, Stephan Lewandowsky, David Garcia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The pursuit of truth is central to democratic deliberation and governance, yet political discourse reflects varying epistemic orientations, ranging from evidence-based reasoning grounded in verifiable information to intuition-based reasoning rooted in beliefs and subjective interpretation. We introduce a scalable approach to measure epistemic orientation using the Evidence--Minus--Intuition (EMI) score, derived from large language model (LLM) ratings and embedding-based semantic similarity. Applying this approach to 15 million parliamentary speech segments spanning 1946 to 2025 across seven countries, we examine temporal patterns in discourse and its association with deliberative democracy and governance. We find that EMI is positively associated with deliberative democracy within countries over time, with consistent relationships in both contemporaneous and lagged analyses. EMI is also positively associated with the transparency and predictable implementation of laws as a dimension of governance. These findings suggest that the epistemic nature of political discourse is crucial for both the quality of democracy and governance.

---


### 230. [Face Anything: 4D Face Reconstruction from Any Image Sequence](https://arxiv.org/abs/2604.19702)

**<font color=#1a73e8>作者：</font>** Umut Kocasari, Simon Giebenhain, Richard Shaw 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate reconstruction and tracking of dynamic human faces from image sequences is challenging because non-rigid deformations, expression changes, and viewpoint variations occur simultaneously, creating significant ambiguity in geometry and correspondence estimation. We present a unified method for high-fidelity 4D facial reconstruction based on canonical facial point prediction, a representation that assigns each pixel a normalized facial coordinate in a shared canonical space. This formulation transforms dense tracking and dynamic reconstruction into a canonical reconstruction problem, enabling temporally consistent geometry and reliable correspondences within a single feed-forward model. By jointly predicting depth and canonical coordinates, our method enables accurate depth estimation, temporally stable reconstruction, dense 3D geometry, and robust facial point tracking within a single architecture. We implement this formulation using a transformer-based model that jointly predicts depth and canonical facial coordinates, trained using multi-view geometry data that non-rigidly warps into the canonical space. Extensive experiments on image and video benchmarks demonstrate state-of-the-art performance across reconstruction and tracking tasks, achieving approximately 3$\times$ lower correspondence error and faster inference than prior dynamic reconstruction methods, while improving depth accuracy by 16%. These results highlight canonical facial point prediction as an effective foundation for unified feed-forward 4D facial reconstruction.

---


### 231. [SpanVLA: Efficient Action Bridging and Learning from Negative-Recovery Samples for Vision-Language-Action Model](https://arxiv.org/abs/2604.19710)

**<font color=#1a73e8>作者：</font>** Zewei Zhou, Ruining Yang, Xuewei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models offer a promising autonomous driving paradigm for leveraging world knowledge and reasoning capabilities, especially in long-tail scenarios. However, existing VLA models often struggle with the high latency in action generation using an autoregressive generation framework and exhibit limited robustness. In this paper, we propose SpanVLA, a novel end-to-end autonomous driving framework, integrating an autoregressive reasoning and a flow-matching action expert. First, SpanVLA introduces an efficient bridge to leverage the vision and reasoning guidance of VLM to efficiently plan future trajectories using a flow-matching policy conditioned on historical trajectory initialization, which significantly reduces inference time. Second, to further improve the performance and robustness of the SpanVLA model, we propose a GRPO-based post-training method to enable the VLA model not only to learn from positive driving samples but also to learn how to avoid the typical negative behaviors and learn recovery behaviors. We further introduce mReasoning, a new real-world driving reasoning dataset, focusing on complex, reasoning-demanding scenarios and negative-recovery samples. Extensive experiments on the NAVSIM (v1 and v2) demonstrate the competitive performance of the SpanVLA model. Additionally, the qualitative results across diverse scenarios highlight the planning performance and robustness of our model.

---


### 232. ["We are currently clean on OPSEC": Why JD Can't Encrypt](https://arxiv.org/abs/2604.19711)

**<font color=#1a73e8>作者：</font>** Maurice Chiodo, Toni Erskine, Dennis Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We analyse the 2025 Signalgate leak of sensitive US military information by the Trump administration, addressing why confidentiality was violated (messages leaked to the press) in spite of encryption (Signal), to deepen the socio-technical considerations when designing and deploying encryption. First, we use applied pi-calculus to formally model the boutique secure facility setup requested by the US Defence Secretary, to prove that a leak would not be prevented. We then examine how using a secure channel might still not give overall information security, as, in this case, power imbalances between personnel and officials led to the application of cryptography that compromised their operational security. We look at how cryptographic tools may have instilled a false sense of security, and led officials to "overshare". We then apply this analysis to the Trump administration's general desire to burn through political, legal, and now technical process, and demonstrate geopolitical harms that may arise from such ineffective use of cryptography in a brief use case. We conclude that, even with advancements in usability of cryptographic tools, genuine message security is still out of reach of the "average user".

---


### 233. [Ultrametric OGP - parametric RDT \emph{symmetric} binary perceptron connection](https://arxiv.org/abs/2604.19712)

**<font color=#1a73e8>作者：</font>** Mihailo Stojnic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In [97,99,100], an fl-RDT framework is introduced to characterize \emph{statistical computational gaps} (SCGs). Studying \emph{symmetric binary perceptrons} (SBPs), [100] obtained an \emph{algorithmic} threshold estimate $\alpha_a\approx \alpha_c^{(7)}\approx 1.6093$ at the 7th lifting level (for $\kappa=1$ margin), closely approaching $1.58$ local entropy (LE) prediction [18].
In this paper, we further connect parametric RDT to overlap gap properties (OGPs), another key geometric feature of the solution space. Specifically, for any positive integer $s$, we consider $s$-level ultrametric OGPs ($ult_s$-OGPs) and rigorously upper-bound the associated constraint densities $\alpha_{ult_s}$. To achieve this, we develop an analytical union-bounding program consisting of combinatorial and probabilistic components. By casting the combinatorial part as a convex problem and the probabilistic part as a nested integration, we conduct numerical evaluations and obtain that the tightest bounds at the first two levels, $\bar{\alpha}_{ult_1} \approx 1.6578$ and $\bar{\alpha}_{ult_2} \approx 1.6219$, closely approach the 3rd and 4th lifting level parametric RDT estimates, $\alpha_c^{(3)} \approx 1.6576$ and $\alpha_c^{(4)} \approx 1.6218$. We also observe excellent agreement across other key parameters, including overlap values and the relative sizes of ultrametric clusters.
Based on these observations, we propose several conjectures linking $ult$-OGP and parametric RDT. Specifically, we conjecture that algorithmic threshold $\alpha_a=\lim_{s\rightarrow\infty} \alpha_{ult_s} = \lim_{s\rightarrow\infty} \bar{\alpha}{ult_s} = \lim_{r\rightarrow\infty} \alpha_{c}^{(r)}$, and $\alpha_{ult_s} \leq \alpha_{c}^{(s+2)}$ (with possible equality for some (maybe even all) $s$). Finally, we discuss the potential existence of a full isomorphism connecting all key parameters of $ult$-OGP and parametric RDT.

---


### 234. [A Network-Aware Evaluation of Distributed Energy Resource Control in Smart Distribution Systems](https://arxiv.org/abs/2604.19715)

**<font color=#1a73e8>作者：</font>** Houchao Gan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution networks with high penetration of Distributed Energy Resources (DERs) increasingly rely on communication networks to coordinate grid-interactive control. While many distributed control schemes have been proposed, they are often evaluated under idealized communication assumptions, making it difficult to assess their performance under realistic network conditions. This work presents an implementation-driven evaluation of a representative virtual power plant (VPP) dispatch algorithm using a co-simulation framework that couples a linearized distribution-system model with packet-level downlink emulation in ns-3. The study considers a modified IEEE~37-node feeder with high photovoltaic penetration and a primal--dual VPP dispatch that simultaneously targets feeder-head active power tracking and voltage regulation. Communication effects are introduced only on the downlink path carrying dual-variable updates, where per-DER packet delays and a hold-last-value strategy are modeled. Results show that, under ideal communication, the dispatch achieves close tracking of the feeder-head power reference while maintaining voltages within the prescribed limits at selected buses. When realistic downlink delay is introduced, the same controller exhibits large oscillations in feeder-head power and more frequent voltage limit violations. These findings highlight that distributed DER control performance can be strongly influenced by communication behavior and motivate evaluation frameworks that explicitly incorporate network dynamics into the assessment of grid-interactive control schemes.

---


### 235. [ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis](https://arxiv.org/abs/2604.19720)

**<font color=#1a73e8>作者：</font>** Zhengwentai Sun, Keru Zheng, Chenghong Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human video generation remains challenging due to the difficulty of jointly modeling human appearance, motion, and camera viewpoint under limited multi-view data. Existing methods often address these factors separately, resulting in limited controllability or reduced visual quality. We revisit this problem from an image-first perspective, where high-quality human appearance is learned via image generation and used as a prior for video synthesis, decoupling appearance modeling from temporal consistency. We propose a pose- and viewpoint-controllable pipeline that combines a pretrained image backbone with SMPL-X-based motion guidance, together with a training-free temporal refinement stage based on a pretrained video diffusion model. Our method produces high-quality, temporally consistent videos under diverse poses and viewpoints. We also release a canonical human dataset and an auxiliary model for compositional human image synthesis. Code and data are publicly available at this https URL.

---


### 236. [Adaptive MSD-Splitting: Enhancing C4.5 and Random Forests for Skewed Continuous Attributes](https://arxiv.org/abs/2604.19722)

**<font color=#1a73e8>作者：</font>** Jake Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The discretization of continuous numerical attributes remains a persistent computational bottleneck in the induction of decision trees, particularly as dataset dimensions scale. Building upon the recently proposed MSD-Splitting technique -- which bins continuous data using the empirical mean and standard deviation to dramatically improve the efficiency and accuracy of the C4.5 algorithm -- we introduce Adaptive MSD-Splitting (AMSD). While standard MSD-Splitting is highly effective for approximately symmetric distributions, its rigid adherence to fixed one-standard-deviation cutoffs can lead to catastrophic information loss in highly skewed data, a common artifact in real-world biomedical and financial datasets. AMSD addresses this by dynamically adjusting the standard deviation multiplier based on feature skewness, narrowing intervals in dense regions to preserve discriminative resolution. Furthermore, we integrate AMSD into ensemble methods, specifically presenting the Random Forest-AMSD (RF-AMSD) framework. Empirical evaluations on the Census Income, Heart Disease, Breast Cancer, and Forest Covertype datasets demonstrate that AMSD yields a 2-4% accuracy improvement over standard MSD-Splitting, while maintaining near-identical O(N) time complexity reductions compared to the O(N log N) exhaustive search. Our Random Forest extension achieves state-of-the-art accuracy at a fraction of standard computational costs, confirming the viability of adaptive statistical binning in large-scale ensemble learning architectures.

---


### 237. [Benign Overfitting in Adversarial Training for Vision Transformers](https://arxiv.org/abs/2604.19724)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Meng Ding, Shaopeng Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable success of Vision Transformers (ViTs) across a wide range of vision tasks, recent studies have revealed that they remain vulnerable to adversarial examples, much like Convolutional Neural Networks (CNNs). A common empirical defense strategy is adversarial training, yet the theoretical underpinnings of its robustness in ViTs remain largely unexplored. In this work, we present the first theoretical analysis of adversarial training under simplified ViT architectures. We show that, when trained under a signal-to-noise ratio that satisfies a certain condition and within a moderate perturbation budget, adversarial training enables ViTs to achieve nearly zero robust training loss and robust generalization error under certain regimes. Remarkably, this leads to strong generalization even in the presence of overfitting, a phenomenon known as \emph{benign overfitting}, previously only observed in CNNs (with adversarial training). Experiments on both synthetic and real-world datasets further validate our theoretical findings.

---


### 238. [FB-NLL: A Feature-Based Approach to Tackle Noisy Labels in Personalized Federated Learning](https://arxiv.org/abs/2604.19729)

**<font color=#1a73e8>作者：</font>** Abdulmoneam Ali, Ahmed Arafa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized Federated Learning (PFL) aims to learn multiple task-specific models rather than a single global model across heterogeneous data distributions. Existing PFL approaches typically rely on iterative optimization-such as model update trajectories-to cluster users that need to accomplish the same tasks together. However, these learning-dynamics-based methods are inherently vulnerable to low-quality data and noisy labels, as corrupted updates distort clustering decisions and degrade personalization performance. To tackle this, we propose FB-NLL, a feature-centric framework that decouples user clustering from iterative training dynamics. By exploiting the intrinsic heterogeneity of local feature spaces, FB-NLL characterizes each user through the spectral structure of the covariances of their feature representations and leverages subspace similarity to identify task-consistent user groupings. This geometry-aware clustering is label-agnostic and is performed in a one-shot manner prior to training, significantly reducing communication overhead and computational costs compared to iterative baselines.
Complementing this, we introduce a feature-consistency-based detection and correction strategy to address noisy labels within clusters. By leveraging directional alignment in the learned feature space and assigning labels based on class-specific feature subspaces, our method mitigates corrupted supervision without requiring estimation of stochastic noise transition matrices. In addition, FB-NLL is model-independent and integrates seamlessly with existing noise-robust training techniques. Extensive experiments across diverse datasets and noise regimes demonstrate that our framework consistently outperforms state-of-the-art baselines in terms of average accuracy and performance stability.

---


### 239. [FASTER: Value-Guided Sampling for Fast RL](https://arxiv.org/abs/2604.19730)

**<font color=#1a73e8>作者：</font>** Perry Dong, Alexander Swerdlow, Dorsa Sadigh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Some of the most performant reinforcement learning algorithms today can be prohibitively expensive as they use test-time scaling methods such as sampling multiple action candidates and selecting the best one. In this work, we propose FASTER, a method for getting the benefits of sampling-based test-time scaling of diffusion-based policies without the computational cost by tracing the performance gain of action samples back to earlier in the denoising process. Our key insight is that we can model the denoising of multiple action candidates and selecting the best one as a Markov Decision Process (MDP) where the goal is to progressively filter action candidates before denoising is complete. With this MDP, we can learn a policy and value function in the denoising space that predicts the downstream value of action candidates in the denoising process and filters them while maximizing returns. The result is a method that is lightweight and can be plugged into existing generative RL algorithms. Across challenging long-horizon manipulation tasks in online and batch-online RL, FASTER consistently improves the underlying policies and achieves the best overall performance among the compared methods. Applied to a pretrained VLA, FASTER achieves the same performance while substantially reducing training and inference compute requirements. Code is available at this https URL .

---


### 240. [Generative Drifting for Conditional Medical Image Generation](https://arxiv.org/abs/2604.19736)

**<font color=#1a73e8>作者：</font>** Zirong Li, Siyuan Mei, Weiwen Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conditional medical image generation plays an important role in many clinically relevant imaging tasks. However, existing methods still face a fundamental challenge in balancing inference efficiency, patient-specific fidelity, and distribution-level plausibility, particularly in high-dimensional 3D medical imaging. In this work, we propose GDM, a generative drifting framework that reformulates deterministic medical image prediction as a multi-objective learning problem to jointly promote distribution-level plausibility and patient-specific fidelity while retaining one-step inference. GDM extends drifting to 3D medical imaging through an attractive-repulsive drift that minimizes the discrepancy between the generator pushforward and the target distribution. To enable stable drifting-based learning in 3D volumetric data, GDM constructs a multi-level feature bank from a medical foundation encoder to support reliable affinity estimation and drifting field computation across complementary global, local, and spatial representations. In addition, a gradient coordination strategy in the shared output space improves optimization balance under competing distribution-level and fidelity-oriented objectives. We evaluate the proposed framework on two representative tasks, MRI-to-CT synthesis and sparse-view CT reconstruction. Experimental results show that GDM consistently outperforms a wide range of baselines, including GAN-based, flow-matching-based, and SDE-based generative models, as well as supervised regression methods, while improving the balance among anatomical fidelity, quantitative reliability, perceptual realism, and inference efficiency. These findings suggest that GDM provides a practical and effective framework for conditional 3D medical image generation.

---


### 241. [Safe Continual Reinforcement Learning in Non-stationary Environments](https://arxiv.org/abs/2604.19737)

**<font color=#1a73e8>作者：</font>** Austin Coursey, Abel Diaz-Gonzalez, Marcos Quinones-Grueiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) offers a compelling data-driven paradigm for synthesizing controllers for complex systems when accurate physical models are unavailable; however, most existing control-oriented RL methods assume stationarity and, therefore, struggle in real-world non-stationary deployments where system dynamics and operating conditions can change unexpectedly. Moreover, RL controllers acting in physical environments must satisfy safety constraints throughout their learning and execution phases, rendering transient violations during adaptation unacceptable. Although continual RL and safe RL have each addressed non-stationarity and safety, respectively, their intersection remains comparatively unexplored, motivating the study of safe continual RL algorithms that can adapt over the system's lifetime while preserving safety. In this work, we systematically investigate safe continual reinforcement learning by introducing three benchmark environments that capture safety-critical continual adaptation and by evaluating representative approaches from safe RL, continual RL, and their combinations. Our empirical results reveal a fundamental tension between maintaining safety constraints and preventing catastrophic forgetting under non-stationary dynamics, with existing methods generally failing to achieve both objectives simultaneously. To address this shortcoming, we examine regularization-based strategies that partially mitigate this trade-off and characterize their benefits and limitations. Finally, we outline key open challenges and research directions toward developing safe, resilient learning-based controllers capable of sustained autonomous operation in changing environments.

---


### 242. [Generalization at the Edge of Stability](https://arxiv.org/abs/2604.19740)

**<font color=#1a73e8>作者：</font>** Mario Tuci, Caner Korkmaz, Umut Şimşekli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training modern neural networks often relies on large learning rates, operating at the edge of stability, where the optimization dynamics exhibit oscillatory and chaotic behavior. Empirically, this regime often yields improved generalization performance, yet the underlying mechanism remains poorly understood. In this work, we represent stochastic optimizers as random dynamical systems, which often converge to a fractal attractor set (rather than a point) with a smaller intrinsic dimension. Building on this connection and inspired by Lyapunov dimension theory, we introduce a novel notion of dimension, coined the `sharpness dimension', and prove a generalization bound based on this dimension. Our results show that generalization in the chaotic regime depends on the complete Hessian spectrum and the structure of its partial determinants, highlighting a complexity that cannot be captured by the trace or spectral norm considered in prior work. Experiments across various MLPs and transformers validate our theory while also providing new insights into the recently observed phenomenon of grokking.

---


### 243. [AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://arxiv.org/abs/2604.19747)

**<font color=#1a73e8>作者：</font>** Yutian Chen, Shi Guo, Renbiao Jin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view 3D reconstruction is essential for modeling scenes from casual captures, but remain challenging for non-generative reconstruction. Existing diffusion-based approaches mitigates this issues by synthesizing novel views, but they often condition on only one or two capture frames, which restricts geometric consistency and limits scalability to large or diverse scenes. We propose AnyRecon, a scalable framework for reconstruction from arbitrary and unordered sparse inputs that preserves explicit geometric control while supporting flexible conditioning cardinality. To support long-range conditioning, our method constructs a persistent global scene memory via a prepended capture view cache, and removes temporal compression to maintain frame-level correspondence under large viewpoint changes. Beyond better generative model, we also find that the interplay between generation and reconstruction is crucial for large-scale 3D scenes. Thus, we introduce a geometry-aware conditioning strategy that couples generation and reconstruction through an explicit 3D geometric memory and geometry-driven capture-view retrieval. To ensure efficiency, we combine 4-step diffusion distillation with context-window sparse attention to reduce quadratic complexity. Extensive experiments demonstrate robust and scalable reconstruction across irregular inputs, large viewpoint gaps, and long trajectories.

---


### 244. [Tstars-Tryon 1.0: Robust and Realistic Virtual Try-On for Diverse Fashion Items](https://arxiv.org/abs/2604.19748)

**<font color=#1a73e8>作者：</font>** Mengting Chen, Zhengrui Chen, Yongchao Du 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in image generation and editing have opened new opportunities for virtual try-on. However, existing methods still struggle to meet complex real-world demands. We present Tstars-Tryon 1.0, a commercial-scale virtual try-on system that is robust, realistic, versatile, and highly efficient. First, our system maintains a high success rate across challenging cases like extreme poses, severe illumination variations, motion blur, and other in-the-wild conditions. Second, it delivers highly photorealistic results with fine-grained details, faithfully preserving garment texture, material properties, and structural characteristics, while largely avoiding common AI-generated artifacts. Third, beyond apparel try-on, our model supports flexible multi-image composition (up to 6 reference images) across 8 fashion categories, with coordinated control over person identity and background. Fourth, to overcome the latency bottlenecks of commercial deployment, our system is heavily optimized for inference speed, delivering near real-time generation for a seamless user experience. These capabilities are enabled by an integrated system design spanning end-to-end model architecture, a scalable data engine, robust infrastructure, and a multi-stage training paradigm. Extensive evaluation and large-scale product deployment demonstrate that Tstars-Tryon1.0 achieves leading overall performance. To support future research, we also release a comprehensive benchmark. The model has been deployed at an industrial scale on the Taobao App, serving millions of users with tens of millions of requests.

---


> [!TIP]
> 当前位于：**201-244**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-244**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
