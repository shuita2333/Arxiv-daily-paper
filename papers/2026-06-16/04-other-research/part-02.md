# 📦 其他研究 | 2026年06月16日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

---

### 51. [Sorries Are Not the Hard Part: An Expert-Review Case Study of a Semi-Autonomous Formalization](https://arxiv.org/abs/2606.13925)

**<font color=#1a73e8>作者：</font>** Vasily Ilin, Brian Nugent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can often close proof gaps in interactive theorem provers, but a verified theorem is not the same thing as a reusable library contribution. We study this distinction through a detailed case study: a semi-autonomous formalization of Grothendieck's vanishing theorem. The initial version compiles with no sorries, but an expert review found serious problems in definitions, theorem generality, file organization, and the API. We then ran a review-driven refactor and compression process and obtained a second expert review. The before-and-after comparison shows a sharp split: agents adapted well to local, mechanically checkable feedback, but remained weak at choosing definitions and designing APIs. We argue that autoformalization should be evaluated not only by closed sorries, but by whether the resulting formalization survives expert review.

---


### 52. [Self-Evolving Visual Questioner](https://arxiv.org/abs/2606.13929)

**<font color=#1a73e8>作者：</font>** Yijun Liang, Hengguang Zhou, Ming Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are typically trained as passive answerers, while their ability to actively ask diverse, non-trivial, visual-centric and grounded questions remains underexplored. Existing visual questioners' performance is bottlenecked by the availability of high-quality training data or the cost of curating them. We show that a VLM can continuously improve itself as a visual questioner without any external supervision. We propose a self-evolving framework that uses a VLM itself as both a proposer and a filter to produce harder, more informative, and visual-centric questions, while maintaining their exploration diversity to avoid training collapse. These questions are then used to train the VLM in both questioner and answerer modes. To evaluate the questioner, we introduce an agentic protocol that assesses questions along perception, reasoning, and diversity dimensions. Experiments across various backbone VLMs show that our method substantially enhances the quality and substantially expands the difficulty boundary of autonomous question generation. Under the same budget, our self-supervision is more effective than training on the static source data. Moreover, the self-evolving questioner remains a competitive or even better answerer.

---


### 53. [Adversarial Concept Search: Predicting Compositional Errors From Feature Geometry](https://arxiv.org/abs/2606.13934)

**<font color=#1a73e8>作者：</font>** Jennifer Meng Lu, Ruochen Zhang, Isabelle Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans cannot always intuit what scenarios are most challenging to LLMs. Hoping to capture challenging edge cases, developers either design problems to be difficult for humans or curate extensive benchmarks. What if we could instead anticipate which scenarios a model will fail on? In this paper, we use an LLM's representational geometry to predict which concept combinations it will fail on. We attribute this compositional failure to interference between salient features. In tasks that require systematic composition - toy programmatic settings, multihop reasoning, multilingual factual recall - we find that when a pair of concepts is encoded near-orthogonally, the model reliably composes them. When their linear encodings are close, producing interference, the model fails to compose them. Our method reliably anticipates failure modes across different compositional tasks, without evaluating specific inputs. These results lay the groundwork to use representational geometry to identify high-risk examples, construct targeted stress tests, and provide a scalable foundation for active learning in real-world deployment.

---


### 54. [MedLatentDx: Latent Multi-Agent Communication for Cross-Hospital Rare-Disease Diagnosis](https://arxiv.org/abs/2606.13945)

**<font color=#1a73e8>作者：</font>** Ziqing Wang, Lili Zhao, Kaize Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rare diseases affect over $300$ million patients across more than $7{,}000$ conditions, yet no single hospital encounters enough cases of any one condition for reliable diagnosis. Cross-hospital collaboration could help by allowing a diagnosing institution to use distributed, case-specific diagnostic evidence, but privacy regulations restrict the transmission of identifiable clinical text across institutional boundaries. This setting raises two challenges: existing medical agent systems often rely on textual evidence exchange, while raw latent states such as hidden states and KV caches may still reveal prompt-derived clinical content. We introduce MedLatentDx, a latent multi-agent communication framework in which hospital agents keep private clinical records and retrieved cases local, and send compact latent KV blocks to a host agent for rare-disease diagnosis. MedLatentDx supports two deployment settings: same-backbone hospital agents use latent KV distillation, while hospitals with different LLM backbones use cross-family latent alignment. On CrossRare-Bench, a self-built large-scale rare-disease benchmark with hospital-level partitions, MedLatentDx improves cross-hospital diagnostic performance while reducing reconstructable clinical content relative to raw-latent communication baselines.

---


### 55. [Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization](https://arxiv.org/abs/2606.13949)

**<font color=#1a73e8>作者：</font>** Hexuan Yu, Chaoyu Zhang, Heng Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern LLM-powered autonomous agents increasingly rely on rich user interface (UI) state observations to achieve reliable action grounding in complex digital environments. However, many deployments transmit the full UI state to remote inference servers even when most elements are irrelevant to the current task, which can leak sensitive but unnecessary context such as authentication codes, private notifications, and background application states. We propose MINIM, a trusted local broker that performs privacy-aware minimization on the client side before any observation leaves the device. Grounded in Contextual Integrity (CI), MINIM learns a dual-score representation for each UI element by predicting an inherent sensitivity score (s) and a task-conditioned necessity score (n). These scores drive a ternary disclosure policy that keeps essential elements, abstracts sensitive attributes when needed, and removes task-irrelevant content. We optimize a CI-aware objective that penalizes necessity errors more strongly on high-risk content, enabling aggressive pruning while preserving task-critical information. Experiments on real-world UI observations derived from WebArena show that MINIM substantially reduces task-irrelevant sensitive leakage while preserving task-critical semantic context and the interactive affordances required for reliable agent actions.

---


### 56. [Side-Channel Attacks Bypass Protection in 3D Printers](https://arxiv.org/abs/2606.13952)

**<font color=#1a73e8>作者：</font>** Eric Yocam, Varghese Vaidyan, Micah Flack 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Active Motor Noise Cancellation (AMNC) ships in commercial fused deposition modeling (FDM) 3D printers as a hardware countermeasure against acoustic side-channel attacks that target intellectual property (IP). We present the first empirical evaluation of a deployed AMNC countermeasure, using a public dataset of synchronized acoustic and vibration recordings from two AMNC-equipped Bambu Lab printers across 12 object classes. AMNC fully neutralizes the acoustic channel: classification accuracy is indistinguishable from the 8.33% random baseline. The vibration channel, which AMNC does not target, still leaks. With summary statistics the leak is coarse and amplitude-driven (vibration accuracy approximately 31% pooled, 36-47% within-printer), while the waveform shape carries essentially nothing (frequency-only features at chance). A full-sequence temporal model that ingests the ordered evolution of the print raises accuracy to approximately 61%, and an order-shuffling control (approximately 33%) shows that a substantial component is genuinely sequential and tied to print progression. The leak is device-specific: a classifier trained on one printer transfers near chance to the other. We conclude that AMNC is an acoustic-only defense: vibration remains a partial, geometry-correlated side channel it does not address, but one that does not, on this dataset, support full geometric reconstruction; reconstruction-grade attacks would require the magnetic or power channels AMNC also leaves untouched. We release all code.

---


### 57. [Smoothing Dark Areas in Molecular Latent Diffusion](https://arxiv.org/abs/2606.13955)

**<font color=#1a73e8>作者：</font>** Xi Wang, Jiahan Li, Yuxuan Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent diffusion is a promising framework for scalable 3D molecular generation, but it requires a latent space that remains smooth, valid, and navigable beyond posterior samples. Existing molecular VAEs, however, are typically learned through reconstruction-based objectives, which do not guarantee such a latent space. We show that this leads to dark areas: regions of latent space that are reachable during diffusion sampling but decode to disconnected or chemically invalid molecules. Unlike in image generation, molecular decoding requires strict structural and chemical precision, so even small latent perturbations can produce catastrophic failures. We therefore propose TopVAE, a topology-optimized VAE that reduces dark areas by making the decoder internalize structural and chemical constraints during training, eliminating the need for test-time chemical correction. TopVAE greatly improves off-posterior robustness, and when paired with a standard DiT, achieves $77\%$ lower FCD-3D on QM9, the highest V&C, $52\%$ lower FCD-3D on GEOM-Drugs, and $1.29{\times}$ more stable and connected molecules on zero-shot scaffold inpainting.

---


### 58. [Can Machine Learning Forecast Rice Yields in Data-Constrained Settings? Satellite Climate Data, National Crop Statistics, and Lessons from Sierra Leone](https://arxiv.org/abs/2606.13959)

**<font color=#1a73e8>作者：</font>** Ibrahim Denis Fofanah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sierra Leone's agriculture operates with almost no data-driven decision support, and no published machine learning study has examined the country's crop yields. We ask whether rice yield can be forecast from data Sierra Leone currently has. Using 25 years of FAOSTAT production data (2000-2024) for nine major crops, we train XGBoost, Gradient Boosting, and Random Forest under a strict anti-leakage protocol with expanding-window walk-forward evaluation across seven held-out years, benchmarked against naive persistence. No model trained on crop statistics alone outperforms persistence. Augmenting with free satellite climate data (CHIRPS rainfall, NASA POWER temperature) reverses this result: a climate-only XGBoost reduces forecast error by one third (RMSE 284 vs 428 kg/ha), a gain that holds for a linear model and is robust to excluding the anomalous 2018 season. Early-season (May-June) rainfall is the dominant predictor, implying seasonal yield risk is observable months before harvest. No model anticipated the 2018 collapse, whose origins were institutional rather than climatic. We translate the findings into policy recommendations for Sierra Leone's Feed Salone Strategy, with a fully open-source pipeline.

---


### 59. [The Silent Cost of Artificial Intelligence Assistance: A Theory of Autonomy Surrender, the Recovery Mechanism, and the Restoration of Human Agency](https://arxiv.org/abs/2606.13962)

**<font color=#1a73e8>作者：</font>** Ancuta Margondai, Julie Rader, Emma Rader 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The integration of artificial intelligence into human decision-making environments has introduced a previously undertheorized cost: the gradual surrender of human autonomy in exchange for access to information and computational assistance. Building on the Human Identity and Autonomy Gap (HIAG) framework, this paper advances a theoretical model of autonomy surrender as a measurable, cumulative process driven by cognitive bandwidth depletion. The model proposes three interacting mechanisms: the silent cost of AI assistance, in which autonomy is transferred incrementally and without awareness; the surrender threshold, beyond which reclaiming autonomous function becomes cognitively and psychologically difficult; and the recovery mechanism, which establishes the design obligation and the ethical responsibility accompanying deliberate human re-assumption of control. The paper argues that human re-entry into the decision loop is not a passive option but an active cognitive event requiring intentional bandwidth restoration. The design of AI systems must incorporate structured re-entry pathways, here termed recovery mechanisms, that preserve human agency while appropriately distributing responsibility. The model further predicts a terminal state, here termed preference inversion, in which functional dependence on AI assistance is experienced not as a deficit but as a preference, transforming the restoration of autonomy from a design problem into a cultural and political one. Implications are drawn for AI system design, governance frameworks, and human factors research.

---


### 60. [CaricHarmony: Contrastive Diffusion Paths for Identity-Preserving Caricature Synthesis](https://arxiv.org/abs/2606.13964)

**<font color=#1a73e8>作者：</font>** Dongyu Wang, Dar-Yen Chen, Yi-Zhe Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sketch-based caricature synthesis suffers from a fundamental failure mode: when identity and shape conditions are combined in diffusion models, they create destructive interference that causes inevitable collapse toward either bland portraits or unrecognizable distortions. We identify the root cause as \emph{condition signal contamination} -- competing probability distributions in the denoising trajectory that make balanced generation impossible. We present CaricHarmony, the first training-free method that explicitly resolves this contamination through parallel uncontaminated diffusion paths. During inference, we maintain three paths: $\mathcal{P}^{\mathrm{i}}$ (pure identity), $\mathcal{P}^{\mathrm{s}}$ (pure shape), and $\mathcal{P}^{\mathrm{i+s}}$ (harmonized output). Novel energy functions operating on cross-attention features provide gradient guidance that steers $\mathcal{P}^{\mathrm{i+s}}$ toward optimal balance: $\mathcal{E}_{\mathrm{shape}}$ ensures sketch fidelity through layout and semantic alignment, while $\mathcal{E}_{\mathrm{id}}$ employs token-level correspondence matching robust to extreme distortions. Unlike DemoCaricature requiring 70 seconds per-identity fine-tuning or CaricatureBooth constrained to Bezier curves, CaricHarmony accepts any sketch format and generates in under 16 seconds. Experiments demonstrate state-of-the-art performance: 0.8615 shape CLIP score (vs. 0.8450) under comparable identity consistency score, with 7.81 overall user preference score (vs. 6.06). Our method fundamentally reconceptualizes the ID-shape conflict as conditioning signal contamination for diffusion models, enabling unprecedented creative control while preserving recognition.

---


### 61. [Software Dark Matter: Gazing at Uncharted Files to Navigate SBOM Integrations](https://arxiv.org/abs/2606.13966)

**<font color=#1a73e8>作者：</font>** Abhishek Reddypalle, Dennis Roellke, Santiago Torres-Arias  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern software supply chains have evolved into vast, heterogeneous networks where transparency - the granular understanding of all software components - is now a critical security requirement. While Software Bills of Materials (SBOMs) have emerged as the primary mechanism for this transparency, current industry practices rely on a metadata-centric paradigm that assumes an artifact is defined solely by its package manager declarations. We posit that this assumption is fundamentally flawed, creating a systemic visibility gap we define as Software Dark Matter (SDM). SDM represents the set of security-critical files present in an artifact's filesystem that are unaccounted for by its associated metadata. We implement a reference tool, DARKFILES, and use it to analyze four ecosystems of disjoint nature: DockerHub, Maven Central, plugin/extension marketplaces (Jenkins plugins and OpenVSX), and a real-world enterprise environment.
Our research makes the following contributions: we introduce a general-purpose metric for artifact fidelity calculating SDM as the ratio of untracked files per total file count. We introduce Packaging Lag, a phenomenon where official metadata remains out-of-date across multiple versions before catching up to an artifact's actual content. We demonstrate that SDM exposes vulnerable software invisible to SBOM-driven pipelines both by cross-referencing untracked packages against known CVE databases and through the direct discovery of three confirmed high-severity CVEs, showing that SDM is highly correlated with sensitive information including secrets and cryptographic keys.

---


### 62. [Choric Masking in Ambient Release Systems: A Finite Certificate Calculus for Trace Indistinguishability under Bounded Audiences](https://arxiv.org/abs/2606.13967)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper develops a finite certificate calculus for ambient release systems, staged probabilistic environments in which a protected coordinate is not observed directly but can remain statistically readable through visible roles, timing, repeated movement, bounded attention, linked rooms, and post-release state. The security notion, choric masking, requires the trace law induced by a protected locus to lie inside or near the convex hull of admissible cover traces under the tests available to a specified audience. For finite horizons, trace laws form polytopes, audiences induce measurement operators, and masking becomes intersection in the projected measurement space. Exposure is certified by separating hyperplanes, kernel obstructions, hypothesis-testing bounds, Fano-type localization lower bounds, and support separation in downstream rooms. The calculus distinguishes trace residue from carrier localization, full-trace exposure from attention-filtered exposure, first-room masking from delayed post-release exposure, and unresolved system pressure from carrier hazard. It proves measurement-polytope equivalence for exact and approximate masks, dual separation certificates, data-processing laws for attention lenses, aperture identities for gaze-thinned observation, lower bounds for mandatory unique gestures, composition rules for linked releases, and a repeated-room debt theorem showing how unresolved pressure can broaden selection and shift cost onto cover populations without localizing the source. The result is a finite, checkable language for auditing privacy, unlinkability, side-channel leakage, and accountability in public-facing release systems.

---


### 63. [Prompt2Effect: Training-Free Image-to-Video Model Specialization via LoRA Generation](https://arxiv.org/abs/2606.13971)

**<font color=#1a73e8>作者：</font>** Xiaomeng Yang, Yanyu Li, Gordon Guocheng Qian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalizing Image-to-Video (I2V) diffusion models with specific visual effects is increasingly demanded for high-end video generation. Current practice requires training a separate Low-Rank Adaptation (LoRA) module for each effect, incurring substantial data curation and iterative optimization costs that hinder interactive control. We present Prompt2Effect, a weight-driven hypernetwork that amortizes per-effect training by directly synthesizing effect-specific LoRA weights in a single forward pass. Unlike prior hypernetworks that regress adapter weights purely from semantics, Prompt2Effect is explicitly conditioned on the frozen base model weights, grounding weight prediction in the structural geometry of each layer. Furthermore, instead of predicting raw LoRA matrices, we introduce an SVD-canonicalized parameterization that resolves factorization ambiguity and stabilizes large-scale weight synthesis. Together, these design principles enable accurate and scalable LoRA prediction for high-dimensional I2V diffusion models. Extensive experiments demonstrate that Prompt2Effect achieves on-par or superior video quality and effect alignment compared to conventional LoRA fine-tuning, while reducing the computational cost from 56 GPU training hours to 3.3 seconds of hypernetwork inference. When used as initialization for subsequent fine-tuning, our predicted weights further improve final performance and accelerate optimization by approximately 10x.

---


### 64. [Creative Integration: A Decidable Criterion of Creativity](https://arxiv.org/abs/2606.13977)

**<font color=#1a73e8>作者：</font>** Yoshinori Nomura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> "Integrative" solutions are widely praised but rarely defined: we lack an operational way to tell a genuine integration -- one that makes the world cheaper to describe -- from a tidy re-description. Building on the lineage that
treats creativity and intelligence as compression, we give such a criterion for creative integration (CI): the resolution of a real conflict between A and B is CI if and only if, under a fixed description language, the description
length strictly shrinks (C = L_pre/L_post > 1), with the reduction located in the conflict itself. We make the judgment decidable through four binary, conjunctive gates, and we fix its extension through a taxonomy of
pseudo-integration that names and rejects the look-alikes. We back the criterion with a curated, multi-domain corpus and -- crucially -- validate it not by human inter-rater agreement but by four falsifiable tests it could fail: an
independent computational check, discrimination against hard negatives, out-of-sample prediction, and description-language robustness; all pass with margin. The contribution is not "creativity is compression" but its decidability,
discrimination, and corpus: on this account, what makes a move genuinely creative -- rather than merely novel -- is that it compresses a conflict, with novelty and value as downstream symptoms; whether all creativity is so
constituted we state as an explicit conjecture. We claim only the sign of C-1; we judge, not generate. The result is a citable primitive for a broader program.

---


### 65. [Fusing Stylometric and Embedding Systems to Estimate Authorship Likelihood Ratios in Japanese](https://arxiv.org/abs/2606.13991)

**<font color=#1a73e8>作者：</font>** Praju Ghatpande, Satoru Tsuge, Shunichi Ishihara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The likelihood ratio framework is widely recognized as the logically and legally sound basis for evidential analysis across forensic sciences, and its importance is increasingly acknowledged in analyses of authorship in textual evidence. To date, however, its application has been confined to English-language texts. Meanwhile, authorship attribution has traditionally relied on a diverse array of stylometric features, even as the rise of pre-trained large language models enables new contextual-embedding approaches. Combining these diverse approaches through fusion promises enhanced performance, yet it has not been applied to integrate stylometric-feature systems with embedding-based systems within the likelihood ratio paradigm. This study is the first to apply likelihood ratio-based forensic text comparison to Japanese digital texts, using ~1,000-character excerpts from blogs, to 1) evaluate system performance and likelihood ratio magnitudes and 2) assess the impact of fusing stylometric-feature systems with embedding-based systems. The results demonstrate that the fused system maintains excellent calibration while 1) increasing consistent-with-fact likelihood ratio magnitudes; 2) decreasing contrary-to-fact likelihood ratio magnitudes and 3) improving overall discriminability. The best-performing fusion achieved a log-likelihood-ratio cost of 0.32484, illustrating both the feasibility of likelihood ratio framework for Japanese and the benefits of fusion across heterogeneous systems.

---


### 66. [Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH](https://arxiv.org/abs/2606.13994)

**<font color=#1a73e8>作者：</font>** Vikhyath Kothamasu, Virginia Smith, Chhavi Yadav  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based Agents are becoming increasingly capable and widely deployed, creating growing incentives for adversarial misuse in the real-world. A key emerging threat is Decomposition Attacks \cite{glukhov2024breach, jones2024adversaries} in which a harmful task is broken into simpler, benign subtasks that evade safety mechanisms when executed separately but cumulatively fulfill the malicious intent. Although recent benchmarks assess agent safety in multi-turn and multi-tool-use settings, they do not explicitly capture this form of decompositional misuse and may not represent realistic adversarial execution flows. To this end, we introduce DeCompBench, a benchmark designed specifically to evaluate agentic safety under decomposition attacks. DeCompBench is created with a decomposition-by-design principle using a graphical framework and enables harmful task decomposition into individually benign and executable subtasks with realistic workflows. Our experiments using a custom decomposer show that state-of-the-art agents exhibit high refusal rates on monolithic harmful tasks, but significantly lower refusal rates on their decomposed variants, while often inadvertently fulfilling the adversarial objectives. These findings underscore the need for safety evaluations against decomposition attacks and corresponding defenses. Our dataset is publicly available and can be found at this https URL.

---


### 67. [Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents](https://arxiv.org/abs/2606.13995)

**<font color=#1a73e8>作者：</font>** Brendan King, Jeffrey Flanigan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI coding agents have rapidly transformed software engineering, powering widely used interactive coding assistants. Despite their interactive real-world use, existing benchmarks evaluate them as fully-autonomous systems. In this work, we introduce Dialogue SWE-Bench, an automatic benchmark dataset for evaluating the ability of coding agents to resolve real-world software engineering problems through dialogue with a user. We design a novel, persona-grounded user simulator to support our task evaluation, and augment our task evaluation with automatic evaluations of dialogue quality. We also propose a new schema-guided agent, aimed at improving the dialogue capabilities of off-the-shelf coding agents, which improves over strong baselines by 3-14%. Our results indicate that better coding models do not always correspond to better dialogue models, suggesting that dialogue capability is a distinct and currently understudied dimension of coding agent performance.

---


### 68. [Formalizing Numerical Analysis: An Agent Pipeline and Quality Audit Beyond Kernel Acceptance](https://arxiv.org/abs/2606.14000)

**<font color=#1a73e8>作者：</font>** Theodore Meek, Siyuan Ge, Di Qiu Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has demonstrated that coding agents can formalize entire advanced mathematics textbooks in Lean 4, yet existing efforts concentrate on branches of mathematics already well-represented in mathlib and measure success solely through kernel acceptance. We address both limitations by applying a coding agent to formalize Numerical Methods for Ordinary Differential Equations, a textbook in numerical analysis that is largely absent from mathlib, stressing the agent's capacity to develop new theory from scratch. We further introduce a systematic, reproducible three-dimensional framework for evaluating the quality of agent-produced formalizations beyond compilation: semantic correctness, Mathlib reuse, and cross-file reuse via LLM-as-judge methods. Applying this framework to our own formalization and to the released outputs of RepoProver and M2F, we uncover recurring unfaithful formalization patterns, including incomplete multi-part statements, added weakening hypotheses, and parameter restrictions, that kernel acceptance entirely obscures. Our results suggest that compilation-based metrics substantially overstate formalization quality, and we provide a reproducible audit methodology to support more rigorous evaluation of future autoformalization systems.

---


### 69. [HARBOR: Heading Analysis and Reconstruction from Behavioral Observation and Radar](https://arxiv.org/abs/2606.14006)

**<font color=#1a73e8>作者：</font>** Joao P. A. Dantas, Paulo F. Silva Filho, Jelton A. Cunha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maritime situational awareness often relies on Automatic Identification System (AIS) transmissions to track vessel movements. However, in operational or conflict scenarios, these data may be unavailable due to signal loss, deliberate deactivation, or intentional spoofing. In such conditions, synthetic aperture radar (SAR) imagery becomes a critical sensing alternative for wide-area maritime monitoring, despite providing only static scene snapshots. This work introduces HARBOR (Heading Analysis and Reconstruction from Behavioral Observation and Radar), a complete pipeline for transforming a single SAR image into predictive motion information without requiring any auxiliary data source at inference time. The method begins with SAR image preprocessing to enhance and segment vessel candidates, followed by automatic detection, size-based classification, and heading estimation using skeleton geometry and local intensity patterns. AIS data are used exclusively during an offline calibration phase to derive vessel-type-dependent motion parameters, which are then applied to generate probabilistic heatmaps of candidate future vessel positions. A case study using real COSMO-SkyMed SAR imagery demonstrates the pipeline on a maritime scene in southern Brazil, showing its ability to extract motion tendencies and generate probabilistic projections of vessel positions in data-denied environments.

---


### 70. [Pseudonym Scheme Based on Hybrid Certificates for Security Credential Management System in Vehicular Communications](https://arxiv.org/abs/2606.14008)

**<font color=#1a73e8>作者：</font>** Abel C. H. Chen, F. J. Hwang, Yu-Chih Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent years, the Institute of Electrical and Electronics Engineers (IEEE) and the European Telecommunications Standards Institute (ETSI) have developed a series of security communication standards for vehicular communications. These standards include mechanisms such as the Security Credential Management System (SCMS) and Butterfly Key Expansion (BKE) to protect vehicle privacy. However, these standards are mainly based on the Elliptic-Curve Cryptography (ECC), which may be vulnerable to attacks from quantum computing in the future. In response to this potential risk, this study proposes a hybrid certificate that combines the ECC with Post-Quantum Cryptography (PQC). This approach enables infrastructure systems to be built on cryptographic foundations that are more resilient to quantum-based attacks. Furthermore, this study presents a generalized pseudonym scheme that is compatible with various cryptographic algorithms for generating pseudonym certificates. This design aims to eliminate the possibility of inferring any correlation between the public key in a pseudonym certificate and that in an enrollment certificate. This study also conducts a comprehensive performance evaluation of the RSA, ECC, and PQC algorithms, particularly those standardized by the National Institute of Standards and Technology (NIST). The comparison considers factors such as message length and computation time. Based on the findings, this study recommends suitable pseudonym schemes that adopt hybrid certificates for secure and efficient use in vehicular communications.

---


### 71. [RT-VLA: Real-Time Vision-Language-Action Models via Knowledge Distillation](https://arxiv.org/abs/2606.14010)

**<font color=#1a73e8>作者：</font>** Xiangyu Huang, Zhenlin Hua, Han Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown strong potential for end-to-end autonomous driving by jointly modeling visual perception, language reasoning, explainability and action prediction. However, their large vision-language backbones and reasoning modules introduce substantial inference latency and thereby prevent their deployment in the unforgiving reality of the road networks. We propose RT-VLA, a lightweight, distilled VLA model that transfers the driving and reasoning capabilities of the state-of-the-art SimLingo model into a compact student through multi-level supervised distillation. RT-VLA preserves language-based reasoning and supports post-hoc explanation through offline language analysis of safety-critical driving moments without adding latency to real-time control. Compared to the SimLingo teacher, RT-VLA maintains competitive closed-loop driving and language reasoning performance while reducing inference time by 44.8X in vision-only mode and 7.9X in vision+language mode. These results suggest that supervised distillation is a practical approach for building real-time, explainable VLA-style autonomous driving models.

---


### 72. [PostDeg: Placement Beats Parameterization in LayerNorm GNNs](https://arxiv.org/abs/2606.14022)

**<font color=#1a73e8>作者：</font>** Yash Tomar, Aryav Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LayerNorm-based GNNs routinely erase the topology signals (degree, centrality, $k$-core) that node-selection policies should depend on, but the literature has not located where in the residual block the erasure happens. We answer that question: a positive per-node scalar inserted before LayerNorm is divided out up to a stabilizer term, while the same scalar inserted after LayerNorm reaches the score head as representation magnitude. The surviving slot is the post-LayerNorm position. We instantiate it with PostDeg, a parameter-free post-LayerNorm inverse-degree scale, and pre-register four falsifiers (graphwise scalars, extra LayerNorm, expressive same-slot capacity, backbone-agnostic source) that would reject the rule. PostDeg gains $+3.5\%/+2.5\%/+5.6\%$ over the LN backbone on influence maximization, network dismantling, and maximum independent set, with $10/10$ paired-seed wins per task; none of the four falsifiers fires. The takeaway is that placement, not parameterization, carries the gain -- a small invariance check that generalizes to any positive topology scalar in any normalized residual stack.

---


### 73. [ViT-Up: Faithful Feature Upsampling for Vision Transformers](https://arxiv.org/abs/2606.14024)

**<font color=#1a73e8>作者：</font>** Krispin Wandel, Jingchuan Wang, Hesheng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have become a dominant architecture for visual representation learning, providing exceptionally strong and broadly reusable backbone features. However, ViTs are commonly operated on relatively small patch-token grids due to the quadratic cost of global self-attention, which creates a persistent bottleneck for dense prediction tasks such as semantic segmentation and depth estimation. This has motivated the development of task-agnostic feature upsamplers. While recent state-of-the-art methods produce visually sharp dense representations, their reliance on shallow image encoders for guided upsampling can introduce feature leakage, fragmentation, and blur. We introduce ViT-Up, an implicit feature upsampling framework that replaces external image guidance with layer-wise query construction from intermediate ViT hidden states. This enables feature prediction at arbitrary continuous image coordinates while preserving alignment with the backbone feature space. Experiments demonstrate that ViT-Up consistently outperforms state-of-the-art image-guided upsamplers across dense prediction and semantic correspondence. On DINOv3-S+, ViT-Up improves over prior methods by up to +2.07 mIoU on Cityscapes and +4.17 PCK@0.10 on SPair-71k. With the larger DINOv3-B backbone, these gains increase to +3.36 mIoU and +8.09 PCK@0.10, demonstrating that ViT-Up scales favorably with backbone capacity.

---


### 74. [Utility-Constrained Policy Optimization](https://arxiv.org/abs/2606.14029)

**<font color=#1a73e8>作者：</font>** Mehrdad Moghimi, Bernardo Avila Pires  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained MDPs (CMDPs) are a widely adopted framework for incorporating safety into RL agents; however, the framework does not support risk-sensitive constraints. This can be problematic: For example, CMDPs allow for optimal solutions that, in order to satisfy the risk-neutral constraints, mix infrequent catastrophic behaviors and frequent, overly conservative ones. Moreover, prior empirical results suggest that enforcing stricter, risk-sensitive constraints can improve performance even under risk-neutral evaluation. The natural framework to incorporate risk-sensitive constraints is utility-constrained MDPs (UCMDPs), but no practical solutions for this problem existed. In this work, we introduce a simple yet powerful methodology for UCMDPs and constrained RL. Besides allowing for risk-sensitive constraints, our framework does not require us to fix constraint limits in advance of training the agent, provided that a sensible range is known. This increases policy flexibility and, in practice, allows for adjustments to these limits at no extra training cost. Besides benefiting from the generality of the framework, our agent shows strong performance in practice, consistently matching or outperforming existing baselines in several Safety Gymnasium benchmark tasks.

---


### 75. [Applicability Condition Extraction for Therapeutic Drug-Disease Relations](https://arxiv.org/abs/2606.14031)

**<font color=#1a73e8>作者：</font>** Guanting Luo, Noriki Nishida, Yuji Matsumoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying conditions that a certain drug takes therapeutic effect on a target disease is crucial for clinical decision-making support. However, most existing biomedical information extraction methods have focused on identifying only relations between drugs and diseases, while largely overlooking the context-specific conditions where such relations can apply. To address this problem, we introduce the task of applicability condition extraction for therapeutic drug--disease relations from biomedical research literature. We create the first dataset that has manually annotated triples of drugs, diseases, and applicability conditions on biomedical paper abstracts with 1,119 drug-disease pairs. Using this dataset, we systematically evaluate the performance of a range of existing methods. In addition, we propose a new method that enhances LoRA to consider relations between drugs and diseases. Our method consistently outperforms strong baselines across different evaluation settings. The source code and dataset of this paper can be obtained from: this https URL

---


### 76. [Toward 360-Degree Indoor Panorama Editing via Tuning-Free Diffusion Model with Refocusing Cross-Attention](https://arxiv.org/abs/2606.14035)

**<font color=#1a73e8>作者：</font>** Dinh-Khoi Vo, Nhut-Thanh Le-Hinh, Viet-Tham Huynh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot text-guided diffusion has significantly advanced image editing; however, its practical usability remains constrained by three persistent challenges: prompt brittleness that requires meticulous prompt engineering, spillover edits that unintentionally affect non-target regions, and failures on small or cluttered objects caused by limited fine-grained supervision in training data. We propose FocusDiff (Target-Aware Refocusing for Tuning-Free Diffusion Editing), a tuning-free framework for precise and region-specific image manipulation based on refocusing cross-attention. Given a target region obtained through automated segmentation or manual selection, FocusDiff applies selective blurring to non-edit areas to guide attention toward the masked region while accurately transferring the object's identity, structure, and appearance to the edited output. Integrated context-preserving modules further ensure background fidelity and global coherence, enabling accurate edits from simple text prompts in a single pass. We also extend FocusDiff to 360-degree indoor panorama editing and demonstrate its effectiveness within virtual reality environments. Extensive experiments on our localized editing benchmark LIMB, comprising 30 multi-object images and 100 annotated examples including challenging small-object cases, show that FocusDiff outperforms existing zero-shot editors in text-image alignment and background preservation, achieving superior precision, photorealism, and usability. The project page is available at this https URL.

---


### 77. [Defending the Core: A Centrality-Based Protection Strategy for Supply Chain Security in npm Dependency Network](https://arxiv.org/abs/2606.14036)

**<font color=#1a73e8>作者：</font>** Zixin Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The modern software supply chain, taking Node Package Manager (npm) dependency network for example, relies heavily on shared open-source dependencies. While this promotes rapid development, it introduces systemic vulnerabilities as well. Concerning this potential risk, we analyze the npm dependency network by modeling 53,481 packages and 78,520 dependency edges, and classify the network as a scale-free topology. Thus, we demonstrate its inherent vulnerability to targeted attacks on high-degree hubs. To mitigate this, we propose and evaluate a dual-pronged defense strategy consisting of Centrality-Based Node-Hardening and Dependency Weight Warning system. Moreover, by simulating the network under various attack scenarios, we prove that applying strict security protocols to just the top 1% of nodes, combined with pruning 30% of structurally trivial edges, prevents catastrophic network collapse and neutralizes cascading malware infections. The source code can be found at this https URL.

---


### 78. [Decompose Sparsely Where You Should, Absorb Densely Where You Should No](https://arxiv.org/abs/2606.14040)

**<font color=#1a73e8>作者：</font>** Ruixuan Deng, Zehao Jin, Zekun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are typically trained to reconstruct the \textbf{entire} residual stream through a sparse dictionary, implicitly assuming that all activation content is amenable to sparse, monosemantic decomposition. We question this assumption and hypothesize that activations contain a low-rank, dense component that is computationally important to the model yet inherently unsuitable for sparse representation, which serves as a major source of the persistent dense latents widely observed in trained SAEs. To test this, we add a small rank-$r$ linear bottleneck in parallel with standard SAEs (BatchTopK and Matryoshka), allowing dense structure to be absorbed before sparse reconstruction. On Gemma-2-2B layer 12, a rank-24 bottleneck reduces dense latent count by up to 84\% while improving sparse probing and targeted probe perturbation on both architectures at matched sparsity. The absorbed component is (i) \textbf{structurally identifiable} as the top principal components and outlier dimensions; (ii) \textbf{causally necessary}, with removing it raising next-token cross-entropy by 7.5$\times$, far exceeding the 2.8$\times$ from removing the geometrically near-identical top-24 PCA directions; and (iii) \textbf{redundantly encoded by sparse dictionaries}, with ablating 787 maximally aligned sparse features raising cross-entropy by only 2.9$\times$ and ablating 2,048 topic-aligned features leaving MMLU topic classification virtually unchanged, whereas removing the scaffold drops it from 98.7\% to chance. Together, our findings identify a compact, semantically informative and causally important component of residual stream activations (which we term a \textbf{computational scaffold}) that standard sparse dictionaries represent inefficiently, suggesting that the scope of sparsity-based interpretability methods warrants careful re-examination.

---


### 79. [Rethinking One-Step Image Editing through ChordEdit: Reproduction, Simplification, and New Insights](https://arxiv.org/abs/2606.14042)

**<font color=#1a73e8>作者：</font>** Minghan Li, Jeremy Moebel, Mengyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step image editing is important for making text-guided editing fast, practical, and easy to deploy, but its underlying mechanism is still not fully understood. We revisit ChordEdit through reproduction, ablation, and simplification. Our analysis shows that a) the chord window $\delta$ largely acts as an effective timestep shift from $t$ to $t - \delta$; b) chord transport acts on high-noise images and mainly performs low-frequency semantic editing; and c) proximal alignment acts on low-noise images and complements it by adding high-frequency target details. In this view, ChordEdit naturally decomposes editing into a coarse low-frequency transport stage and a fine high-frequency alignment stage. These findings suggest a path toward prompt-conditioned dynamic timestep selection for adaptive image editing. All code and results can be found at \href{this https URL}{link}.

---


### 80. [WAM4D: Fast 4D World Action Model via Spatial Register Tokens](https://arxiv.org/abs/2606.14048)

**<font color=#1a73e8>作者：</font>** Ying Li, Xiaobao Wei, Jiajun Cao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.

---


### 81. [Visible Adoption, Untracked Contribution: GitHub Evidence of the Accountability Gap Across Three Cohorts of an HCI Prototyping Course](https://arxiv.org/abs/2606.14054)

**<font color=#1a73e8>作者：</font>** Maria Teresa Parreira, Pranav Prabhat Sinha, Hauke Sandhaus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents a longitudinal, observational case study of how student GenAI adoption shifted across three cohorts (Fall 2022, 2023, and 2025) of the same graduate-level HCI prototyping course, using computational analysis of 203 GitHub repositories with student activity and 23,065 student commits. Building on a prior qualitative study of the 2023 cohort, we distinguish two levels of AI accountability trace: disclosure (naming that an AI tool was used) and attribution (crediting a specific artifact or task to an AI tool). We find that tool disclosure grew from 0% to 66% of repositories across the three cohorts, while explicit contribution attribution remains a minority practice, and the gap between the two reveals where accountability is missing even among students who disclose. By 2025, AI is infrastructure embedded in course templates and student-built devices: students increasingly name the tools they used, but rarely specify what those tools contributed. We argue that disclosure-based frameworks are insufficient for the vibe-coding era. The failure is not that students conceal AI use; it is that a norm built for episodic, identifiable acts cannot capture continuous, ambient co-creation. We offer this case study as grounding for the workshop's conversation about what genuine co-thinking accountability looks like.

---


### 82. [Non-Parametric Machine Text Detection via Multi-View Gaussian Processes](https://arxiv.org/abs/2606.14060)

**<font color=#1a73e8>作者：</font>** Aleem Khan, Nicholas Andrews  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial conditions such as paraphrasing and targeted style transfer sharply degrade the accuracy of machine text detectors. A document, however, carries multiple complementary signals (e.g., stylistic features, likelihood and rank-order features, and structural features), and an attack that suppresses one may leave others intact. While a parametric classifier can learn to combine these features given sufficient supervision, classifiers are prone to making confidently incorrect predictions when the distribution shifts (e.g., novel attacks or unseen language models). To address this, we propose a multi-view, non-parametric detection framework that extracts complementary feature views from the same document and aggregates per-view evidence through a Gaussian process ensemble. By aggregating evidence across views, an adversary must simultaneously defeat multiple independent axes of detection, substantially raising the cost of evasion. The Gaussian process formulation additionally provides calibrated probabilities and principled abstention on out-of-distribution inputs, supporting reliable deployment in high-stakes settings. We evaluate on three benchmarks spanning diverse generators and attacks: the DetectRL and RAID benchmarks, and the PAN2025 shared task and demonstrate that our multi-view detector maintains strong performance under the considered attacks, outperforming existing approaches against held out attacks.

---


### 83. [ShearFuse-UNet: Hadamard, DCT, and Shearlet Transform Fusion for Next-Day Wildfire Spread Prediction](https://arxiv.org/abs/2606.14071)

**<font color=#1a73e8>作者：</font>** Ene Meco, Yingyi Luo, Emadeldeen Hamdan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose ShearFuse-UNet, a lightweight and computationally efficient deep learning model for next-day wildfire spread prediction from multi-modal satellite data. The model integrates three complementary transform-domain branches inside each encoder block of a U-Net backbone: a 2D Fast Walsh-Hadamard Transform (WHT) branch, a 2D Discrete Cosine Transform (DCT) branch, and a cone-adapted digital Shearlet residual branch. The WHT and DCT branches establish orthogonal latent spaces with learnable spectral scaling and fixed soft-thresholding, while the Shearlet branch provides anisotropic, multi-directional feature decomposition that explicitly encodes the elongated edge structures characteristic of fire fronts. A learned SpectralFusion gate adaptively combines the WHT and DCT responses, and the Shearlet reconstruction is added as a residual. This three-branch design bears a loose structural analogy to transformer self-attention: the WHT and DCT branches provide complementary spectral representations that are adaptively fused, while the Shearlet branch contributes directional content through a residual pathway. Unlike self-attention, the proposed design relies on fixed mathematical transforms rather than learned projection operators, reducing parameter count and computational cost. Evaluated on the WildfireSpreadTS dataset, ShearFuse-UNet achieves an F1 score of 0.596 with only 267k parameters, outperforming a ResNet18-based U-Net (14M parameters, F1 = 0.589) and demonstrating a highly favorable accuracy-efficiency trade-off. Results on the Google Next-Day Wildfire Spread dataset further validate these findings across a different benchmark.

---


### 84. [Diffusion-Refined Segmentation and Vision-Language Interpretation for Pediatric Brain Tumor MRI](https://arxiv.org/abs/2606.14072)

**<font color=#1a73e8>作者：</font>** Wentao Ke, Jianche Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate pediatric brain tumor segmentation remains challenging due to limited annotated data, heterogeneous imaging phenotypes, diffuse tumor boundaries, and class imbalance across tumor subregions. Here, we present a two-stage deep learning framework for improving multi-modal pediatric brain MRI segmentation and clinical interpretation. First, we evaluate 3D Res U-Net and Swin-UNETR baselines on BraTS-PEDs MRI scans, using four co-registered modalities to predict tumor core, whole tumor, and enhancing tumor regions. Second, we introduce diffusion-based refinement models conditioned on coarse Swin-UNETR predictions, including a 3D DDPM refiner and MedSegDiff. Conditioning substantially improves diffusion stability and performance, particularly for enhancing tumor boundary segmentation. Conditioned MedSegDiff achieves the strongest boundary agreement with the lowest HD95. Finally, predicted tumor volumes and representative segmentation overlays are integrated with a multimodal language model to generate structured radiology-style reports. Together, our results suggest that coarse-to-refined diffusion segmentation can improve pediatric tumor boundary delineation and support end-to-end interpretable AI-assisted neuro-oncology workflows.

---


### 85. [Rethinking Backdoor Adversarial Unlearning through the Lens of Catastrophic Forgetting in Continual Learning](https://arxiv.org/abs/2606.14078)

**<font color=#1a73e8>作者：</font>** Zhenqian Zhu, Yamin Hu, Yujiang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing studies reveal that current backdoor defenses exhibit limited robustness and often fail against specific types of attacks. More concerningly, prevailing safety tuning strategies tend to provide only superficial safety protection, as they fall short of completely eliminating the backdoor effects. In this work, we present a novel formulation of backdoor learning and unlearning as a sequential, three-stage process from a continual learning perspective. Within this framework, we formally define complete backdoor unlearning and further derive the necessary conditions for achieving it based on the mechanism of catastrophic forgetting. Guided by these insights, we propose Blind Inversion-Backdoor Adversarial Unlearning (BI-BAU), which formulates the generation of adversarial examples satisfying the unlearning conditions as a blind inversion problem. We solve this by integrating the bi-level optimization process of adversarial training into an Expectation-Maximization (EM) algorithm framework to optimize the maximum a posteriori (MAP) objective. Furthermore, BI-BAU is extended to untargeted adversarial scenarios with unknown target classes, as well as to multi-modal contrastive learning tasks, enhancing its applicability to real-world deployment scenarios where pre-trained models may be compromised. Extensive experiments demonstrate that our method exhibits general applicability across a wide spectrum of backdoor attacks and can effectively and thoroughly eliminate the backdoor effects from a backdoor model.

---


### 86. [Deep Spectral Learning of Embedded Latent Transfer Operators for Stochastic Dynamical Systems](https://arxiv.org/abs/2606.14079)

**<font color=#1a73e8>作者：</font>** Ryogo Tanaka, Yoshinobu Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a spectral learning method for stochastic nonlinear dynamical systems represented with embedded latent transfer operators in deep feature spaces. We instantiate the method as Deep Spectral Encoder (DSE), an operator-based latent state-space model in which a time-invariant neural encoder implements learnable nonlinear feature maps from observations, and these features define Markovian latent states whose temporal evolution and observation mapping are described by the transfer and observation operators, respectively. Functional canonical correlation analysis in a learnable Galerkin-projected feature space provides state coordinates from past and future observations, and the two linear operators are estimated on the state coordinates as ridge-regularized closed-form solutions that coincide with Galerkin projections of the associated covariance operators. On this representation, we generalize sequential Bayesian filtering and Koopman spectral mode decomposition in feature space. Experiments on several scenarios show stable and superior performance with sequential Bayesian filtering and dynamic mode decomposition baselines even under noise and partial observability.

---


### 87. [Hierarchical Identity-Based Signature with Designated Aggregator from Lattices](https://arxiv.org/abs/2606.14090)

**<font color=#1a73e8>作者：</font>** Stuti Kumari, Kunal Dey, Vikas Srivastava 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In hierarchical organizations, authenticating data from multiple users can be complex and resource-intensive. Hierarchical Identity-Based Signature with Designated Aggregator (HIBS-DA) provides an efficient solution by allowing users at different levels to generate signatures that can be combined into a single, compact signature. We first introduce the HIBS-DA framework and present the {\em{first}} lattice-based construction of HIBS-DA. Our scheme allows users at different hierarchical levels to generate individual signatures that can be aggregated into a single, compact signature, reducing communication and verification costs. The proposed construction is secure, correct, and resistant to forgery, making it suitable for large-scale environments such as universities, corporations, and government agencies.

---


### 88. [FEMOT: Multi-Object Tracking using Frame and Event Cameras](https://arxiv.org/abs/2606.14094)

**<font color=#1a73e8>作者：</font>** Shiao Wang, Xiao Wang, Chao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional RGB cameras have been widely used in multi-object tracking due to their ability to capture rich appearance and semantic information. However, their performance is often degraded under complex real-world challenges, such as motion blur, low illumination, and overexposure. Bio-inspired event cameras offer high temporal resolution and high dynamic range, providing complementary cues under extreme scenarios. Nevertheless, RGB-event multi-object tracking remains underexplored due to the lack of large-scale and well-annotated datasets. To address this issue, we propose FEMOT, a large-scale RGB-event multi-object tracking dataset that covers diverse real-world scenarios and 14 challenging attributes. With both RGB and event data as well as high-quality annotations, FEMOT provides a reliable platform for systematically evaluating RGB-event multi-object tracking methods. Based on FEMOT, we retrain and evaluate over ten strong trackers, thereby establishing a comprehensive benchmark for future research. Furthermore, we propose FEMOTR, a multimodal tracking framework that decouples RGB and event features and fuses them in the frequency domain, thereby effectively exploiting their complementary characteristics for robust object localization and identity association. Extensive experiments on FEMOT and DSEC-MOT datasets demonstrate the effectiveness of the proposed method. The source code and benchmark dataset have been released on this https URL.

---


### 89. [Lyapunov-Based Sample Complexity Analysis for Weakly-Coupled MDPs](https://arxiv.org/abs/2606.14095)

**<font color=#1a73e8>作者：</font>** Tianhao Wu, Matthew Zurek, Weina Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the sample complexity of learning in average-reward weakly-coupled Markov decision processes (WCMDPs) and Restless Bandits (RBs) under a generative model. Naive reduction to a tabular MDP leads to high complexity bounds as the state-action space is exponentially large in the number of arms $N$. By exploiting the weakly coupled structure, we show that near-optimal policies can be learned with sample and computational complexities that are polynomial in $N$. Specifically, we analyze the plug-in approach, which applies an efficient planning algorithm to an empirical model estimated from data. For fully heterogeneous WCMDPs, we establish the first finite-sample PAC guarantee with polynomial complexity and an $O(1/\sqrt{N})$ optimality gap. For homogeneous RBs, we further prove that a smaller optimality gap is achievable under mild structural assumptions. A primary technical contribution of our work is a novel Lyapunov-based analysis framework. Unlike classical approaches that rely on the difficult-to-control bias function, our framework uses an explicitly constructed Lyapunov function along with a drift transfer technique between the true and empirical models. A key step of independent interest in our framework is a fine-grained perturbation analysis for the underlying linear programming (LP) relaxation, which provides a general tool for analyzing LP-based policies and weakly-coupled systems.

---


### 90. [A New Multi-Domain Benchmark for Micro-Action Recognition and Detection](https://arxiv.org/abs/2606.14096)

**<font color=#1a73e8>作者：</font>** Yanbin Hao, Pengyu Liu, Xing Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-actions are short-duration, low-amplitude subtle body movements at the whole-body level that can reveal latent intentions, involuntary reactions, and fine-grained affective changes. Our previous MA-52 benchmark has provided an important foundation for micro-action recognition, but it remains limited in scale, scene diversity, task coverage, and evaluation protocols. To advance micro-action analysis toward more realistic and comprehensive settings, we introduce MMA-82, a large-scale multi-domain extension of MA-52. MMA-82 expands the label space from 52 to 82 fine-grained micro-action categories and covers four distinct domains, including laboratory interviews, street interviews, psychiatric patient interviews, and emotion-rich television videos, resulting in 77,856 annotated instances from 454 subjects. Built upon MMA-82, we establish two core tasks: Micro-Action Recognition and Multi-label Micro-Action Detection. For recognition, we further define in-domain and cross-domain protocols, including few-shot and zero-shot settings, to evaluate model robustness, transferability, and generalization. Extensive experiments show that current methods still struggle with realistic micro-action understanding, especially under domain shift, long-tailed category distributions, and complex temporal localization. Beyond benchmarking, we investigate the relationship between micro-actions and emotion, showing that micro-actions are strongly associated with emotional states and provide complementary cues to facial micro-expressions for improved emotion recognition. These results demonstrate that MMA-82 serves as a comprehensive and challenging benchmark for realistic micro-action analysis and a valuable resource for human-centered AI. MMA-82 is available at this https URL.

---


### 91. [Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents](https://arxiv.org/abs/2606.14106)

**<font color=#1a73e8>作者：</font>** Seoyoung Choi, Minseok Ko, Hyunseok Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents are increasingly used to automate complex computer tasks across applications, websites, and operating systems. To improve their reliability, recent work has introduced experiential memory, where agents retrieve prior trajectories to guide decision-making in similar states. More recent approaches further extend this idea to visual memory by storing and retrieving screenshots from past interactions, providing agents with richer contextual information than text-only memories. However, the effect of visual memory in GUI agents remains insufficiently understood: it is unclear which failures visual memory mitigates, or which failures it exacerbates. To systematically analyze the effect of visual memory, we introduce a taxonomy of four GUI agent failures (i.e., cognitive failure, visual state misunderstanding, hidden operation blindness, and grounding error) that map to distinct stages of the perception-reasoning-action pipeline. We find that prepending full-image memory has a divergent effect on the failure distribution: it reduces state-level failures but worsens action-level ones, and increases hidden operation blindness and grounding error. Motivated by this finding, we propose Action-Grounded Visual Memory (AGMem), an action-grounded memory framework for GUI agents. The core idea of AGMem is to store image crops that capture the local GUI region closely related to a successful action or a recovery, rather than storing full screenshots. Experiments on OSWorld show that AGMem improves task success rates by 33.3 % over full-image memory. These results demonstrate that AGMem is an effective representation for visual memory in GUI agents.

---


### 92. [Numbers Already Carry Their Own Embeddings](https://arxiv.org/abs/2606.14108)

**<font color=#1a73e8>作者：</font>** Suhyun Bae, Donghun Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Adelic operation-preserved embeddings (AOE), a training-free representation that captures both a number's real value and its modular (p-adic) signatures. This construction preserves additive and multiplicative structure by design, turning numerical input into embeddings that "speak in the language of mathematics." Unlike prior approaches that rely on task-specific retraining, AOE is plug-and-play and drops seamlessly into existing architectures. On algebraic combinatorics benchmarks, it delivers consistent gains including the first-ever perfect accuracy on the Weaving Pattern task-while suggesting a principled path forward for overcoming the long-standing "number problem" in AI.

---


### 93. [DTVEM-RE: A Hierarchical Random-Effects Extension of the Differential Time-Varying Effect Model for Person-Specific Multi-Lag Estimation in Intensive Longitudinal Data](https://arxiv.org/abs/2606.14116)

**<font color=#1a73e8>作者：</font>** Amartya Bhattacharya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Differential Time-Varying Effect Model (DTVEM) of Jacobson et al. (2019) is a popular tool for finding the best time lag in intensive longitudinal data, but it assumes everyone shares the same lag structure. The original authors named fixing this as future work, and it clashes with the premise of modern clinical research, which is that people differ. We present DTVEM-RE, an extension that lets each person have their own lag coefficients, with two versions of the confirmatory step: a discrete-time hierarchical Bayesian VAR in Stan, which pools across people and gives calibrated uncertainty, and a continuous-time per-person Ornstein-Uhlenbeck model in ctsem, which handles unevenly spaced beeps directly. We report four results. A simulation shows the Bayesian version recovers the between-person spread tau_a with bias below 0.01 and coverage of 90 to 93 percent. On the Fisher et al. (2017) EMA dataset (N=40), person-specific lag-1 effects vary by an order of magnitude across three mood items, the Bayesian and GAMM estimates agree closely (r=0.87 to 0.92), and DTVEM-RE gives the best one-step-ahead prediction among four discrete-time methods. A multi-lag version shows all nine tau_k values have credible intervals excluding zero, and the lag where people differ most changes across items, something lag-1-only methods like mlVAR cannot detect. Finally, the two versions agree almost exactly on person-specific lag-1 estimates (r >= 0.995), differing only as shrinkage predicts. DTVEM-RE is, to our knowledge, the first person-specific implementation of DTVEM-style lag detection, and it contains standard DTVEM as a special case.

---


### 94. [Recovering Stranded Discrimination in Knowledge Tracing: Per-Item Bias Correction via Empirical-Bayes Shrinkage](https://arxiv.org/abs/2606.14123)

**<font color=#1a73e8>作者：</font>** Xiaoran Yan, Cheng Tang, Atsushi Shimada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deployed knowledge-tracing models are typically frozen after training, yet systematic per-item logit bias arises, from limited per-item expressivity in backbone architectures and from post-deployment shifts in item properties, degrading prediction quality. Global post-hoc calibrators such as Platt scaling, temperature scaling, and isotonic regression improve probability estimates but leave discriminative ability, as measured by AUC, unchanged. This AUC invariance is a structural consequence of monotone score-only transforms; recovering the stranded discrimination requires conditioning on item identity. We propose SLC (State-space Logit Correction), which converts binary observations to Gaussian pseudo-observations via Laplace/IRLS, applies empirical-Bayes shrinkage through a Kalman smoother, and fits an offset-Platt link. The state-space formulation also yields a detectability bound that characterizes the Bernoulli information floor, explaining why temporal tracking provides no benefit at current data densities. Across four datasets, five backbones, and three seeds, SLC improves AUC on all four datasets and NLL on three, with the advantage concentrating on sparse items. Cross-domain controls suggest that the same phenomenon can arise beyond education when the deployed backbone leaves entity-level bias.

---


### 95. [Conditioning Matters: Stabilizing Inversion and Attention in Diffusion Image Editing](https://arxiv.org/abs/2606.14125)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhan, Hongchen Li, Can Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inversion-based image editing offers flexible and training-free control but still struggles with inversion accuracy and the trade-off between editing fidelity and background preservation. While recent methods improve inversion formulations or attention interactions, the role of textual conditioning in shaping diffusion dynamics and editing behavior remains underexplored. We show both empirically and theoretically that the precision of textual conditioning influences inversion stability by modulating the geometry of the diffusion velocity field, while also affecting the consistency of cross-branch attention during editing. These effects directly impact background preservation and semantic fidelity. Building on this analysis, we propose SimEdit, a conditioning-aware framework with two complementary components: (a) conditioning refinement, which constructs conditioning signals with improved semantic precision and structural alignment to facilitate stable inversion and consistent attention manipulation, and (b) token-wise cross-branch attention control, which separates edit-relevant and structure-preserving components and modulates them asymmetrically during attention manipulation. Extensive experiments on PIE-Bench demonstrate that SimEdit consistently improves both inversion reconstruction quality and editing performance over previous attention-manipulation approaches. Our code is available at this https URL.

---


### 96. [BoRAD: Bootstrap your Own Representations for Multi-class Anomaly Detection](https://arxiv.org/abs/2606.14129)

**<font color=#1a73e8>作者：</font>** Duy Hoang Khuong, Tri Nguyen Minh, Ngu Huynh Cong Viet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstruction-based anomaly detection is attractive for industrial inspection, but scaling it from category-specific training to a one-for-all setting is challenging. A single model must reconstruct diverse normal appearances without copying abnormal details, which exposes two coupled failure modes: identical shortcut, where anomalies pass through the reconstruction path, and mis-reconstruction, where normal categories are confused with one another. We propose \textbf{BoRAD}, a label-free training framework that treats this as a representation-capacity allocation problem. BoRAD uses a shared learnable prototype bank to impose two complementary regularizers: spatial prototype alignment contracts local within-prototype variation to suppress anomaly copying, while prototype-relative global alignment preserves between-prototype structure and improves sensitivity to abnormal angular deviations. The prototype bank and prediction heads are used only during training; inference remains a standard teacher-student feature discrepancy pass, with no class labels, negative pairs, memory retrieval, or prototype lookup. BoRAD achieves competitive one-for-all anomaly detection performance, including 86.2\% mAD on MVTec AD, 80.7\% mAD on VisA and 73.1\% mAD on Real-IAD. Diagnostic analyses further show reduced anomaly leakage, improved normal-category separability, and stronger anomaly-normal score separation.

---


### 97. [Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.14130)

**<font color=#1a73e8>作者：</font>** Omar Adalat, Edwin Hamel-De le Court, Francesco Belardinelli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe coordination problems surface in multi-agent reinforcement learning when global safety cannot be enforced by any agent unilaterally: the admissibility of one agent's action may depend on the dynamics of other agents. Decentralised shields can enforce safety at runtime, but purely factorised permissions often exclude optimal team behaviour that is safe only through coordination. We study deterministic safety guarantees for agents trained and deployed under decentralised execution, recovering team-optimal safe behaviour without centralised runtime control. Agents have a shared global specification $\phi$ in the safety fragment of Linear Temporal Logic ($\mathsf{LTL}_{\mathsf{safe}}$ ), and select among tuples of local $\mathsf{LTL}_{\mathsf{safe}}$ obligations whose conjunction implies the global specification $\phi$. Each agent may rely on the other agents' local obligations as assumptions because the whole contract tuple is certified simultaneously and allows projection into local action masks. At learning time, a non-stationary multi-armed bandit chooses among a library of local $\mathsf{LTL}_{\mathsf{safe}}$ obligations to select the tuple that optimises team reward, all without forgoing end-to-end safety. We evaluate the approach across 6 environments and 15 algorithmic variants.

---


### 98. [Decoupled Latent Optimization of Diffusion Models for Full Waveform Inversion](https://arxiv.org/abs/2606.14139)

**<font color=#1a73e8>作者：</font>** Chen Min, Zheng Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full waveform inversion (FWI) recovers subsurface velocity from seismic recordings by solving a severely ill-posed, nonconvex PDE-constrained optimization. Classical regularizers stabilize the inversion but fail to reproduce realistic geological structures; recent diffusion-prior methods improve realism at the cost of a fragile trade-off between data fidelity and prior consistency. We propose Decoupled Latent Optimization (DLO), which relaxes the standard latent-optimization formulation into a quadratic-penalty objective over an auxiliary physical variable and a latent variable. The data-fidelity gradient acts in physical space, the diffusion sampler contributes only through a decoded prior sample, and the standard smoothed-velocity initialization of classical FWI is preserved. On the OpenFWI benchmark, DLO outperforms classical regularizers and existing diffusion-based methods under clean, noisy, and missing-trace acquisitions. The prior, trained on 70*70 OpenFWI models, transfers directly to the Marmousi and Overthrust benchmarks, where DLO recovers intricate fault structures and remains robust to initialization smoothing and measurement noise.

---


### 99. [Personal Care Utility: Health as Everyday Infrastructure](https://arxiv.org/abs/2606.14145)

**<font color=#1a73e8>作者：</font>** Mahyar Abbasian, Elahe Khatibi, Saba A. Farahani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Healthcare is essential, expert, and episodic by design - built around the roughly one hour per year a person spends with a clinician. The 8,759 hours outside clinical settings, where eating, sleeping, movement, medication, and stress actually shape long-term health, have no comparable infrastructure. The bottleneck for personalized health is not raw data or reasoning capability; it is the absence of that infrastructure layer. This paper introduces the Personal Care Utility (PCU): a layered, event-driven architecture proposed as the missing utility for everyday health, in the way that payments, networks, and power are utilities for their domains. PCU organizes continuous personal signals into semantically meaningful life events through a Personicle, estimates dynamic health state against personal baselines, reasons about cause and context, and routes guidance through an orchestrator that separates clinical decision logic, behavioral strategy selection, and natural-language expression. This separation lets large language models support reasoning and communication while keeping safety-critical clinical decisions grounded in validated evidence. We instantiate PCU for Type 2 Diabetes - turning CGM, meal, activity, medication, sleep, stress, and clinical data into glycemic events, individualized state estimates, causal explanations, and knowledge-grounded interventions. A day-in-the-life scenario shows the same infrastructure producing real-time nudges, weekly summaries, medication check-ins, silence, or deterministic safety alerts depending on context and risk. We close with how PCU generalizes to other chronic conditions and the governance questions any always-on personal health utility must address. The result is a blueprint that treats personalization not as a final messaging layer, but as an architectural property of everyday health guidance.

---


### 100. [Encoder Winners Do Not Reliably Transfer Across VLA Backbone Scale: A Frozen-Backbone Grafting Diagnostic](https://arxiv.org/abs/2606.14153)

**<font color=#1a73e8>作者：</font>** Qingping Zeng, Fei She  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) policies typically inherit their vision encoder from upstream VLM releases, but it is unclear whether an encoder choice validated on a small VLA transfers to a larger backbone. We introduce a frozen-backbone grafting diagnostic: the vision tower of a released VLA is replaced by a candidate encoder under a fixed protocol (adaptive average pooling, LayerNorm, and a single trainable linear projector), with the language model and action expert frozen. Across four encoders, two LIBERO suites, two backbones (SmolVLA-450M and $\pi_{0.5}$-3.3B), and two-to-three seeds per cell (40 main grafting runs plus native, LoRA, pooling, and zero-/shuffled-image controls, all scored by offline action MSE), the small-backbone winner does not reliably select the large-backbone top tier: SigLIP is best on SmolVLA across both suites, while on $\pi_{0.5}$ DINOv2-small leads the spatial suite and the object suite is a seed-sensitive near-tie band; three of the four backbone-suite comparisons (and 11 of 12 seed-level cells) support backbone-dependent rankings. The grafting wrapper is itself non-neutral with opposite sign across backbones (+45-56% MSE on the SmolVLA native tower, -50-52% on $\pi_{0.5}$), so all conclusions are conditional on the fixed grafting protocol. We position frozen grafting as a cheap target-backbone diagnostic to run before committing to an encoder at scale, not as a closed-loop deployment claim.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
