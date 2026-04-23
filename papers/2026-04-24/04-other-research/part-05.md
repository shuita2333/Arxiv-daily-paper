# 📦 其他研究 | 2026年04月24日

> 本类共 **220** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-220**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-220**

---

### 201. [DAIRE: A lightweight AI model for real-time detection of Controller Area Network attacks in the Internet of Vehicles](https://arxiv.org/abs/2604.20771)

**<font color=#1a73e8>作者：</font>** Shahid Alam, Amina Jameel, Zahida Parveen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Vehicles (IoV) is advancing modern transportation by improving safety, efficiency, and intelligence. However, the reliance on the Controller Area Network (CAN) introduces critical security risks, as CAN-based communication is highly vulnerable to cyberattacks. Addressing this challenge, we propose DAIRE (Detecting Attacks in IoV in REal-time), a lightweight machine learning framework designed for real-time detection and classification of CAN attacks. DAIRE is built on a lightweight artificial neural network (ANN) where each layer contains Ni = i x c neurons, with Ni representing the number of neurons in the ith layer and c corresponding to the total number of attack classes. Other hyperparameters are determined empirically to ensure real-time operation. To support the detection and classification of various IoV attacks, such as Denial-of-Service, Fuzzy, and Spoofing, DAIRE employs the sparse categorical cross-entropy loss function and root mean square propagation for loss minimization. In contrast to more resource-intensive architectures, DAIRE leverages a lightweight ANN to reduce computational demands while still delivering strong performance. Experimental results on the CICIoV2024 and Car-Hacking datasets demonstrate DAIRE's effectiveness, achieving an average detection rate of 99.88%, a false positive rate of 0.02%, and an overall accuracy of 99.96%. Furthermore, DAIRE significantly outperforms state-of-the-art approaches in inference speed, with a classification time of just 0.03 ms per sample. These results highlight DAIRE's effectiveness in detecting IoV cyberattacks and its practical suitability for real-time deployment in vehicular systems, underscoring its vital role in strengthening automotive cybersecurity.

---


### 202. [Relative Entropy Estimation in Function Space: Theory and Applications to Trajectory Inference](https://arxiv.org/abs/2604.20775)

**<font color=#1a73e8>作者：</font>** Chao Wang, Luca Nepote, Giulio Franzese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory Inference (TI) seeks to recover latent dynamical processes from snapshot data, where only independent samples from time-indexed marginals are observed. In applications such as single-cell genomics, destructive measurements make path-space laws non-identifiable from finitely many marginals, leaving held-out marginal prediction as the dominant but limited evaluation protocol. We introduce a general framework for estimating the Kullback-Leibler divergence (KL) divergence between probability measures on function space, yielding a tractable, data-driven estimator that is scalable to realistic snapshot datasets. We validate the accuracy of our estimator on a benchmark suite, where the estimated functional KL closely matches the analytic KL. Applying this framework to synthetic and real scRNA-seq datasets, we show that current evaluation metrics often give inconsistent assessments, whereas path-space KL enables a coherent comparison of trajectory inference methods and exposes discrepancies in inferred dynamics, especially in regions with sparse or missing data. These results support functional KL as a principled criterion for evaluating trajectory inference under partial observability.

---


### 203. [Efficient Multi-Cohort Inference for Long-Term Effects and Lifetime Value in A/B Testing with User Learning](https://arxiv.org/abs/2604.20777)

**<font color=#1a73e8>作者：</font>** Dario Simionato, Andrea Tonon, Mingxue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In streaming platforms churn is extremely costly, yet A/B tests are typically evaluated using outcomes observed within a limited experimental horizon. Even when both short- and predicted long-term engagement metrics are considered, they may fail to capture how a treatment affects users' retention. Consequently, an intervention may appear beneficial in the short term and neutral in the long term while still generating lower total value than the control due to users churn.
To address this limitation, we introduce a method that estimates long-term treatment effects (LTE) and residual lifetime value change ($\Delta ERLV$) in short multi-cohort A/B tests under user learning. To estimate time-varying treatment effects efficiently, we introduce an inverse-variance weighted estimator that combines multiple cohorts estimates, reducing variance relative to standard approaches in the literature. The estimated treatment trajectory is then modeled as a parametric decay to recover both the asymptotic treatment effect and the cumulative value generated over time.
Our framework enables simultaneous evaluation of steady-state impact and residual user value within a single experiment. Empirical results show improved precision in estimating LTE and $\Delta ERLV$ and identify scenarios in which relying on either short-term or long-term metrics alone would lead to incorrect product decisions.

---


### 204. [SWE-chat: Coding Agent Interactions From Real Users in the Wild](https://arxiv.org/abs/2604.20779)

**<font color=#1a73e8>作者：</font>** Joachim Baumann, Vishakh Padmakumar, Xiang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice. We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild. The dataset currently contains 6,000 sessions, comprising more than 63,000 user prompts and 355,000 agent tool calls. SWE-chat is a living dataset; our collection pipeline automatically and continually discovers and processes sessions from public repositories. Leveraging SWE-chat, we provide an initial empirical characterization of real-world coding agent usage and failure modes. We find that coding patterns are bimodal: in 41% of sessions, agents author virtually all committed code ("vibe coding"), while in 23%, humans write all code themselves. Despite rapidly improving capabilities, coding agents remain inefficient in natural settings. Just 44% of all agent-produced code survives into user commits, and agent-written code introduces more security vulnerabilities than code authored by humans. Furthermore, users push back against agent outputs -- through corrections, failure reports, and interruptions -- in 44% of all turns. By capturing complete interaction traces with human vs. agent code authorship attribution, SWE-chat provides an empirical foundation for moving beyond curated benchmarks towards an evidence-based understanding of how AI agents perform in real developer workflows.

---


### 205. [Designing a Visualization Atlas: Lessons & Reflections from The UK Co-Benefits Atlas for Climate Mitigation](https://arxiv.org/abs/2604.20781)

**<font color=#1a73e8>作者：</font>** Jinrui Wang, Alexis Pister, Sian Phillips 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper reports on the process of designing the UK Co-Benefits Atlas, which communicates and publicizes data for climate mitigation. Visualization atlases -- an emerging type of platform to make data about complex topics comprehensive through interactive visualizations and explanatory content -- pose challenges beyond traditional visualization projects. Atlases must address diverse and often uncertain audiences and use cases, support both explanatory and guided exploration, and accommodate complex, evolving data. Over 10 months, our team of visualization and domain experts conducted 8 design workshops, iterative prototyping, 15 stakeholder onboarding sessions, and continuous reflection. These intertwined processes informed the development of the Atlas, comprising over 400 pages of visualizations and explanations. They also enabled a deeper understanding of how stakeholders may critically engage with the atlas in practice, in terms of interests, potential frictions when navigating huge amounts of data, and envisioned usage scenarios. Reflecting on our design process, we identify five driving forces in atlas design -- data, people, stories, context, and the atlas itself -- whose shifting dynamics influence different stages of visualization atlas design in different ways. Grounded in our case study, we discuss using these forces as a conceptual starting point for structuring and reflecting on future atlas design processes.

---


### 206. [Physics-Conditioned Synthesis of Internal Ice-Layer Thickness for Incomplete Layer Traces](https://arxiv.org/abs/2604.20783)

**<font color=#1a73e8>作者：</font>** Zesheng Liu, Maryam Rahnemoonfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Internal ice layers imaged by radar provide key evidence of snow accumulation and ice dynamics, but radar-derived layer boundary observations are often incomplete, with discontinuous traces and sometimes entirely missing layers, due to limited resolution, sensor noise, and signal loss. Existing graph-based models for ice stratigraphy generally assume sufficiently complete layer profiles and focus on predicting deeper-layer thickness from reliably traced shallow layers. In this work, we address the layer-completion problem itself by synthesizing complete ice-layer thickness annotations from incomplete radar-derived layer traces by conditioning on colocated physical features synchronized from physical climate models. The proposed network combines geometric learning to aggregate within-layer spatial context with a transformer-based temporal module that propagates information across layers to encourage coherent stratigraphy and consistent thickness evolution. To learn from incomplete supervision, we optimize a mask-aware robust regression objective that evaluates errors only at observed thickness values and normalizes by the number of valid entries, enabling stable training under varying sparsity without imputation and steering completions toward physically plausible values. The model preserves observed thickness where available and infers only missing regions, recovering fragmented segments and even fully absent layers while remaining consistent with measured traces. As an additional benefit, the synthesized thickness stacks provide effective pretraining supervision for a downstream deep-layer predictor, improving fine-tuned accuracy over training from scratch on the same fully traced data.

---


### 207. [GeoRect4D: Geometry-Compatible Generative Rectification for Dynamic Sparse-View 3D Reconstruction](https://arxiv.org/abs/2604.20784)

**<font color=#1a73e8>作者：</font>** Zhenlong Wu, Zihan Zheng, Xuanxuan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic 3D scenes from sparse multi-view videos is highly ill-posed, often leading to geometric collapse, trajectory drift, and floating artifacts. Recent attempts introduce generative priors to hallucinate missing content, yet naive integration frequently causes structural drift and temporal inconsistency due to the mismatch between stochastic 2D generation and deterministic 3D geometry. In this paper, we propose GeoRect4D, a novel unified framework for sparse-view dynamic reconstruction that couples explicit 3D consistency with generative refinement via a closed-loop optimization process. Specifically, GeoRect4D introduces a degradation-aware feedback mechanism that incorporates a robust anchor-based dynamic 3DGS substrate with a single-step diffusion rectifier to hallucinate high-fidelity details. This rectifier utilizes a structural locking mechanism and spatiotemporal coordinated attention, effectively preserving physical plausibility while restoring missing content. Furthermore, we present a progressive optimization strategy that employs stochastic geometric purification to eliminate floaters and generative distillation to infuse texture details into the explicit representation. Extensive experiments demonstrate that GeoRect4D achieves state-of-the-art performance in reconstruction fidelity, perceptual quality, and spatiotemporal consistency across multiple datasets.

---


### 208. [Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity](https://arxiv.org/abs/2604.20789)

**<font color=#1a73e8>作者：</font>** Pranava Madhyastha, Dagmar Adamcova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate the integration of human-like working memory constraints into the Transformer architecture and implement several cognitively inspired attention variants, including fixed-width windows based and temporal decay based attention mechanisms. Our modified GPT-2 models are trained from scratch on developmentally plausible datasets (10M and 100M words). Performance is evaluated on grammatical judgment tasks (BLiMP) and alignment with human reading time data. Our results indicate that these cognitively-inspired constraints, particularly fixed-width attention, can significantly improve grammatical accuracy especially when training data is scarce. These constrained models also tend to show a stronger alignment with human processing metrics. The findings suggest that such constraints may serve as a beneficial inductive bias, guiding models towards more robust linguistic representations, especially in data-limited settings.

---


### 209. [Fresh Masking Makes NTT Pipelines Composable: Machine-Checked Proofs for Arithmetic Masking in PQC Hardware](https://arxiv.org/abs/2604.20793)

**<font color=#1a73e8>作者：</font>** Ray Iskander, Khaled Kirah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum cryptographic (PQC) accelerators for ML-KEM (FIPS 203) and ML-DSA (FIPS 204) rely on pipelined Number Theoretic Transform (NTT) stages over $\mathbb{Z}_q$. Our prior work established structural dependency analysis at scale [1] and quantified the security margin of partial NTT masking [2]. Whether per-stage arithmetic masking guarantees pipeline-level security had no prior machine-checked answer for the r-bearing case: composition frameworks (ISW, t-SNI, PINI, DOM) were formalized exclusively for Boolean masking over $\mathrm{GF}(2)$; no proof assistant artifact addresses the NTT butterfly over $\mathbb{Z}_q$. We present three machine-checked results in Lean 4 with Mathlib, all zero sorry. First, we close a stated limitation of prior work: value-independence implies constant marginal distribution under fresh randomness (via an algebraic MutualInfoZero proxy). Second, butterfly per-context uniformity: for any Cooley-Tukey butterfly with fresh output mask over $\mathbb{Z}/q\mathbb{Z}$ ($q > 0$), each output wire has exactly one mask value producing each output, a uniform marginal independent of secrets, universal over all moduli, twiddle factors, and inputs. Third, a k-stage NTT pipeline with fresh per-stage masking satisfies per-context uniformity at every stage under the ISW first-order probing model. We document a named warning: pointwise value-independence is false for butterfly outputs. The Adams Bridge accelerator (CHIPS Alliance Caliptra) fails the fresh masking hypothesis, masking active only in INTT round 0, architecturally explaining its structural insecurity. Artifact: nine theorems, 1,738 build jobs, zero sorry. Composition for nonlinear gadgets (Barrett) is addressed in forthcoming manuscripts proving Barrett's PF-PINI(2) satisfaction ('one-bit barrier') [3] and k-stage composition for PF-PINI gadgets under fresh-mask renewal [4].

---


### 210. [LEXIS: LatEnt ProXimal Interaction Signatures for 3D HOI from an Image](https://arxiv.org/abs/2604.20800)

**<font color=#1a73e8>作者：</font>** Dimitrije Antić, Alvaro Budria, George Paschalidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D Human-Object Interaction from an RGB image is essential for perceptive systems. Yet, this remains challenging as it requires capturing the subtle physical coupling between the body and objects. While current methods rely on sparse, binary contact cues, these fail to model the continuous proximity and dense spatial relationships that characterize natural interactions. We address this limitation via InterFields, a representation that encodes dense, continuous proximity across the entire body and object surfaces. However, inferring these fields from single images is inherently ill-posed. To tackle this, our intuition is that interaction patterns are characteristically structured by the action and object geometry. We capture this structure in LEXIS, a novel discrete manifold of interaction signatures learned via a VQ-VAE. We then develop LEXIS-Flow, a diffusion framework that leverages LEXIS signatures to estimate human and object meshes alongside their InterFields. Notably, these InterFields help in a guided refinement that ensures physically-plausible, proximity-aware reconstructions without requiring post-hoc optimization. Evaluation on Open3DHOI and BEHAVE shows that LEXIS-Flow significantly outperforms existing SotA baselines in reconstruction, contact, and proximity quality. Our approach not only improves generalization but also yields reconstructions perceived as more realistic, moving us closer to holistic 3D scene understanding. Code & models will be public at this https URL.

---


### 211. [Adapting TrOCR for Printed Tigrinya Text Recognition: Word-Aware Loss Weighting for Cross-Script Transfer Learning](https://arxiv.org/abs/2604.20813)

**<font color=#1a73e8>作者：</font>** Yonatan Haile Medhanie, Yuanhua Ni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based OCR models have shown strong performance on Latin and CJK scripts, but their application to African syllabic writing systems remains limited. We present the first adaptation of TrOCR for printed Tigrinya using the Ge'ez script. Starting from a pre-trained model, we extend the byte-level BPE tokenizer to cover 230 Ge'ez characters and introduce Word-Aware Loss Weighting to resolve systematic word-boundary failures that arise when applying Latin-centric BPE conventions to a new script. The unmodified model produces no usable output on Ge'ez text. After adaptation, the TrOCR-Printed variant achieves 0.22% Character Error Rate and 97.20% exact match accuracy on a held-out test set of 5,000 synthetic images from the GLOCR dataset. An ablation study confirms that Word-Aware Loss Weighting is the critical component, reducing CER by two orders of magnitude compared to vocabulary extension alone. The full pipeline trains in under three hours on a single 8 GB consumer GPU. All code, model weights, and evaluation scripts are publicly released.

---


### 212. [Stream-CQSA: Avoiding Out-of-Memory in Attention Computation via Flexible Workload Scheduling](https://arxiv.org/abs/2604.20819)

**<font color=#1a73e8>作者：</font>** Yiming Bian, Joshua M. Akey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The scalability of long-context large language models is fundamentally limited by the quadratic memory cost of exact self-attention, which often leads to out-of-memory (OOM) failures on modern hardware. Existing methods improve memory efficiency to near-linear complexity, while assuming that the full query, key, and value tensors fit in device memory. In this work, we remove this assumption by introducing CQS Divide, an operation derived from cyclic quorum sets (CQS) theory that decomposes attention into a set of independent subsequence computations whose recomposition yields exactly the same result as full-sequence attention. Exploiting this decomposition, we introduce Stream-CQSA, a memory-adaptive scheduling framework that partitions attention into subproblems that fit within arbitrary memory budgets. This recasts attention from a logically monolithic operation into a collection of schedulable tasks, enabling flexible execution across devices without inter-device communication. Experiments demonstrate predictable memory scaling and show that exact attention over billion-token sequences can be executed on a single GPU via streaming, without changing the underlying mathematical definition of attention or introducing approximation error.

---


### 213. [Global Offshore Wind Infrastructure: Deployment and Operational Dynamics from Dense Sentinel-1 Time Series](https://arxiv.org/abs/2604.20822)

**<font color=#1a73e8>作者：</font>** Thorsten Hoeser, Felix Bachofer, Claudia Kuenzer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The offshore wind energy sector is expanding rapidly, increasing the need for independent, high-temporal-resolution monitoring of infrastructure deployment and operation at global scale. While Earth Observation based offshore wind infrastructure mapping has matured for spatial localization, existing open datasets lack temporally dense and semantically fine-grained information on construction and operational dynamics. We introduce a global Sentinel-1 synthetic aperture radar (SAR) time series data corpus that resolves deployment and operational phases of offshore wind infrastructure from 2016Q1 to 2025Q1. Building on an updated object detection workflow, we compile 15,606 time series at detected infrastructure locations, with overall 14,840,637 events as analysis-ready 1D SAR backscatter profiles, one profile per Sentinel-1 acquisition and location. To enable direct use and benchmarking, we release (i) the analysis ready 1D SAR profiles, (ii) event-level baseline semantic labels generated by a rule-based classifier, and (iii) an expert-annotated benchmark dataset of 553 time series with 328,657 event labels. The baseline classifier achieves a macro F1 score of 0.84 in event-wise evaluation and an area under the collapsed edit similarity-quality threshold curve (AUC) of 0.785, indicating temporal coherence. We demonstrate that the resulting corpus supports global-scale analyses of deployment dynamics, the identification of differences in regional deployment patterns, vessel interactions, and operational events, and provides a reference for developing and comparing time series classification methods for offshore wind infrastructure monitoring.

---


### 214. [From Meme to Method: Rethinking Animal Adoption Platforms through the Cat Distribution System](https://arxiv.org/abs/2604.20823)

**<font color=#1a73e8>作者：</font>** Carl Angelo Angcana, Jamlech Iram Gojo Cruz  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The internet folklore of the Cat Distribution System (CDS) humorously suggests that cats are "assigned" to people rather than intentionally sought. Beyond its playful origins, CDS reflects a culturally resonant way people perceive and engage in adoption, and this user context can guide the redesign and improvement of adoption systems. In the Philippines, where an estimated 13.11 million stray cats and dogs place the country sixth worldwide in overpopulation, this framing offers a novel way to rethink adoption platforms. We developed a prototype application inspired by CDS principles, focusing on features such as algorithmic matchmaking, community reporting, and proximity-based discovery. An initial evaluation with potential users (n=35) indicated that the system was positively received for its ease of use and its alignment with users' intuitive expectations, though participants highlighted areas for improvement in transparency of matchmaking and owner-adopter communication. The findings suggest that culturally embedded metaphors like CDS can shape mental models, making adoption processes feel more serendipitous and less transactional.

---


### 215. [Closing the Domain Gap in Biomedical Imaging by In-Context Control Samples](https://arxiv.org/abs/2604.20824)

**<font color=#1a73e8>作者：</font>** Ana Sanchez-Fernandez, Thomas Pinetz, Werner Zellinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The central problem in biomedical imaging are batch effects: systematic technical variations unrelated to the biological signal of interest. These batch effects critically undermine experimental reproducibility and are the primary cause of failure of deep learning systems on new experimental batches, preventing their practical use in the real world. Despite years of research, no method has succeeded in closing this performance gap for deep learning models. We propose Control-Stabilized Adaptive Risk Minimization via Batch Normalization (CS-ARM-BN), a meta-learning adaptation method that exploits negative control samples. Such unperturbed reference images are present in every experimental batch by design and serve as stable context for adaptation. We validate our novel method on Mechanism-of-Action (MoA) classification, a crucial task for drug discovery, on the large-scale JUMP-CP dataset. The accuracy of standard ResNets drops from 0.939 $\pm$ 0.005, on the training domain, to 0.862 $\pm$ 0.060 on data from new experimental batches. Foundation models, even after Typical Variation Normalization, fail to close this gap. We are the first to show that meta-learning approaches close the domain gap by achieving 0.935 $\pm$ 0.018. If the new experimental batches exhibit strong domain shifts, such as being generated in a different lab, meta-learning approaches can be stabilized with control samples, which are always available in biomedical experiments. Our work shows that batch effects in bioimaging data can be effectively neutralized through principled in-context adaptation, which also makes them practically usable and efficient.

---


### 216. [FedSIR: Spectral Client Identification and Relabeling for Federated Learning with Noisy Labels](https://arxiv.org/abs/2604.20825)

**<font color=#1a73e8>作者：</font>** Sina Gholami, Abdulmoneam Ali, Tania Haghighi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training without sharing raw data; however, the presence of noisy labels across distributed clients can severely degrade the learning performance. In this paper, we propose FedSIR, a multi-stage framework for robust FL under noisy labels. Different from existing approaches that mainly rely on designing noise-tolerant loss functions or exploiting loss dynamics during training, our method leverages the spectral structure of client feature representations to identify and mitigate label noise.
Our framework consists of three key components. First, we identify clean and noisy clients by analyzing the spectral consistency of class-wise feature subspaces with minimal communication overhead. Second, clean clients provide spectral references that enable noisy clients to relabel potentially corrupted samples using both dominant class directions and residual subspaces. Third, we employ a noise-aware training strategy that integrates logit-adjusted loss, knowledge distillation, and distance-aware aggregation to further stabilize federated optimization. Extensive experiments on standard FL benchmarks demonstrate that FedSIR consistently outperforms state-of-the-art methods for FL with noisy labels. The code is available at this https URL.

---


### 217. [An Analysis of Attack Vectors Against FIDO2 Authentication](https://arxiv.org/abs/2604.20826)

**<font color=#1a73e8>作者：</font>** Alexander Berladskyy, Andreas Aßmuth  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing attacks remain one of the most prevalent threats to online security, with the Anti-Phishing Working Group reporting over 890,000 attacks in Q3 2025 alone. Traditional password-based authentication is particularly vulnerable to such attacks, prompting the development of more secure alternatives. This paper examines passkeys, also known as FIDO2, which claim to provide phishing-resistant authentication through asymmetric cryptography. In this approach, a private key is stored on a user's device, the authenticator, while the server stores the corresponding public key. During authentication, the server generates a challenge that the user signs with the private key; the server then verifies the signature and establishes a session. We present passkey workflows and review state-of-the-art attack vectors from related work alongside newly identified approaches. Two attacks are implemented and evaluated: the Infected Authenticator attack, which generates attacker-known keys on a corrupted authenticator, and the Authenticator Deception attack, which spoofs a target website by modifying the browser's certificate authority store, installing a valid certificate, and intercepting user traffic. An attacker relays a legitimate challenge from the real server to a user, who signs it, allowing the attacker to authenticate as the victim. Our results demonstrate that successful attacks on passkeys require substantial effort and resources. The claim that passkeys are phishing-resistant largely holds true, significantly raising the bar compared to traditional password-based authentication.

---


### 218. [AVISE: Framework for Evaluating the Security of AI Systems](https://arxiv.org/abs/2604.20833)

**<font color=#1a73e8>作者：</font>** Mikko Lempinen, Joni Kemppainen, Niklas Raesalmi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) systems are increasingly deployed across critical domains, their security vulnerabilities pose growing risks of high-profile exploits and consequential system failures. Yet systematic approaches to evaluating AI security remain underdeveloped. In this paper, we introduce AVISE (AI Vulnerability Identification and Security Evaluation), a modular open-source framework for identifying vulnerabilities in and evaluating the security of AI systems and models. As a demonstration of the framework, we extend the theory-of-mind-based multi-turn Red Queen attack into an Adversarial Language Model (ALM) augmented attack and develop an automated Security Evaluation Test (SET) for discovering jailbreak vulnerabilities in language models. The SET comprises 25 test cases and an Evaluation Language Model (ELM) that determines whether each test case was able to jailbreak the target model, achieving 92% accuracy, an F1-score of 0.91, and a Matthews correlation coefficient of 0.83. We evaluate nine recently released language models of diverse sizes with the SET and find that all are vulnerable to the augmented Red Queen attack to varying degrees. AVISE provides researchers and industry practitioners with an extensible foundation for developing and deploying automated SETs, offering a concrete step toward more rigorous and reproducible AI security evaluation.

---


### 219. [DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation](https://arxiv.org/abs/2604.20841)

**<font color=#1a73e8>作者：</font>** Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generative models enable the synthesis of realistic human-object interaction videos across a wide range of scenarios and object categories, including complex dexterous manipulations that are difficult to capture with motion capture systems. While the rich interaction knowledge embedded in these synthetic videos holds strong potential for motion planning in dexterous robotic manipulation, their limited physical fidelity and purely 2D nature make them difficult to use directly as imitation targets in physics-based character control. We present DeVI (Dexterous Video Imitation), a novel framework that leverages text-conditioned synthetic videos to enable physically plausible dexterous agent control for interacting with unseen target objects. To overcome the imprecision of generative 2D cues, we introduce a hybrid tracking reward that integrates 3D human tracking with robust 2D object tracking. Unlike methods relying on high-quality 3D kinematic demonstrations, DeVI requires only the generated video, enabling zero-shot generalization across diverse objects and interaction types. Extensive experiments demonstrate that DeVI outperforms existing approaches that imitate 3D human-object interaction demonstrations, particularly in modeling dexterous hand-object interactions. We further validate the effectiveness of DeVI in multi-object scenes and text-driven action diversity, showcasing the advantage of using video as an HOI-aware motion planner.

---


### 220. [SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation](https://arxiv.org/abs/2604.20842)

**<font color=#1a73e8>作者：</font>** Ruohan Liu, Shukang Yin, Tao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.

---


> [!TIP]
> 当前位于：**201-220**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-220**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
