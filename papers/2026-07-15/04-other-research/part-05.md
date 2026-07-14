# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

---

### 201. [HyperBank: A Differentiable Bank of Classical Priors for Few-Shot Spheroid Microscopy Segmentation](https://arxiv.org/abs/2607.10684)

**<font color=#1a73e8>作者：</font>** M. Průšek, A. Novozámský, F. Šroubek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot spheroid segmentation must adapt to new cell lines, microscopes, and illumination conditions from only a small set of annotated images. While foundation few-shot segmenters can be accurate, their large opaque backbones make it difficult to understand which visual cues drive success or failure. We study this question with HyperBank, a differentiable bank of classical image-processing operators combining Frangi vesselness, a Sauvola threshold pyramid, structure-tensor responses, gradient magnitude, and Laplacian-of-Gaussian filters. HyperBank is fitted on the annotated support images and evaluated on disjoint held-out images across three independently acquired spheroid datasets. We treat it not as a general replacement for foundation models, but as a compact, interpretable few-shot microscopy pipeline and an analytic-prior probe of which classical cues carry the few-shot signal. The results show that, adapted on the same few annotated support images, a compact bank of analytic priors is competitive with, and on small-cluster, contrast-driven data can outperform, much larger foundation models, while those models remain stronger on externally sourced, texture-dominated spheroids. Leave-one-family-out ablations indicate that the useful few-shot signal is distributed across operator families and strengthened by support-set-tuned morphology.

---


### 202. [Incremental Online Scene Reconstruction by 3D Gaussian Triangulation](https://arxiv.org/abs/2607.10690)

**<font color=#1a73e8>作者：</font>** Yanjin Zhu, Shaofan Liu, Jianke Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incremental scene reconstruction is essential for real-world applications. Although 3D Gaussian Splatting shows strong potential, most existing approaches require offline conversion of the optimized Gaussians into an intermediate implicit field for explicit mesh extraction, which hinders seamless integration with downstream tasks. To address this limitation, we propose a novel online framework that incrementally reconstructs and updates high-fidelity explicit meshes by directly triangulating a dense geometric Gaussian representation, which supports both high-quality rendering and incremental surface reconstruction. Moreover, we present a direct meshing algorithm that efficiently extracts and updates the mesh from the Gaussian set. To ensure mesh accuracy, we enforce a plane-based pulling constraint that dynamically aligns 3D Gaussian primitives to the approximated local surface. Furthermore, our framework significantly reduces memory and computational overhead during long-sequence processing by dynamically freezing fully optimized historical regions. Experiments on public datasets demonstrate that our method outperforms conventional Gaussian-based methods on both rendering quality and reconstruction accuracy.

---


### 203. [Effective Synthetic Image Detection via Noise Residual Clustering](https://arxiv.org/abs/2607.10695)

**<font color=#1a73e8>作者：</font>** Caihui Yan, Gang Cao, Huawei Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative artificial intelligence (AI) has made synthetic images remarkably realistic, posing security threats such as misinformation and fraud. It is significant to detect the synthetic image in the manner of passive and blind image authentication. Most existing detectors rely on supervised training with large labeled datasets, leading to high costs and degraded performance on unknown generative models. To attenuate such deficiencies, we propose a training-free detection method. Specifically, noise residual fingerprints are first extracted by a simple yet effective pre-trained Noiseprint++ model. Then multi-scale features are further extracted from such residual by a frozen Vision Transformer (ViT), followed by adaptive weighted fusion. Only a few real image samples are used needed to initialize the clustering centers for unsupervised K-Means, distinguishing real and synthetic images without training. Extensive evaluations on four benchmark datasets show that our proposed scheme achieves an average accuracy of 82.2%, outperforming the state-of-the-art detectors on generalization ability. Superior performance is gained on the popular diffusion type of synthetic images, and the effectiveness of each module is validated by ablation studies. Source code will be publicly available at this https URL.

---


### 204. [On the modality gap and the contrastive loss in multi-modal representation learning](https://arxiv.org/abs/2607.10698)

**<font color=#1a73e8>作者：</font>** Fabian Mager, Hiba Nassar, Lars Kai Hansen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the modality gap in CLIP-style dual-encoder contrastive learning, where image and text embeddings remain misaligned despite being trained in a shared space. We argue that the gap is induced by a failure of the InfoNCE formulation with independent encoders. We conduct a uni-modal experiment with two independent encoders and identical initialization conditions and find that InfoNCE actively generates a gap at low temperatures. We provide a theoretical analysis of this phenomenon and show that the modality gap is indeed a mode-failure of InfoNCE, but only at low temperatures. We propose a simple modification called xNCE, which uses intermodal as well as intra-modality negative contrastive pairs. xNCE matches retrieval performance on MS-COCO while consistently reducing the gap even at low temperatures. Notably, xNCE improves zero-shot classification over the InfoNCE baseline across all benchmarks, whereas high-temperature InfoNCE and regularized InfoNCE both fail to do so, demonstrating that xNCE reduces the modality gap without sacrificing the discriminative geometry needed for transfer.

---


### 205. [Lottery and Sprint Arcade: Enabling Player-Driven Game Editing with Generative AI](https://arxiv.org/abs/2607.10711)

**<font color=#1a73e8>作者：</font>** Maya Grace Torii, Takahito Murakami, Yoichi Ochiai  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are shifting game generation from offline automation toward play-driven modification through natural language interaction. In this work, we present a play-driven game editing system that enables players to modify a retro Space Invaders - style arcade game through voice-based natural-language commands during play. Spoken instructions are interpreted by an LLM and translated into structured updates of internal configuration parameters, allowing iterative play - edit - feedback cycles in an invader-style game environment without exposing underlying system details. The game includes approximately 100 editable configuration fields controlling mechanics, visuals, interaction patterns, and audio behavior, enabling gameplay transformation through incremental parameter changes. To investigate how users experience play-driven AI-mediated editing (RQ1) and how emergent editing patterns relate to variations in player experience (RQ2), we conducted a user study combining subjective evaluations, workload measures, and log-based analysis of editing behavior. Participants were able to modify gameplay with generally positive experiences and moderate workload, and interaction outcomes did not strongly depend on prior programming experience. Editing-log analysis revealed distinct experiential tendencies: adjustments to immediately perceptible parameters were associated with higher usability, whereas edits affecting core gameplay structures were more closely associated with enjoyment. Post-session reflections further identified diverse editing strategies, including exploratory experimentation, goal-driven structural modification, and iterative parameter tuning. These findings demonstrate that voice-driven editing can support accessible, play-driven human - AI co-creation within a structured invader-style arcade game environment.

---


### 206. [Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud](https://arxiv.org/abs/2607.10712)

**<font color=#1a73e8>作者：</font>** Bálint Gyevnár, Atoosa Kasirzadeh, Nihar B. Shah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science. Historically, it required the resources of a company: deep pockets, ghostwritten articles, and corrupt academics. Today, Artificial Intelligence (AI) is increasingly automating scientific research, so we ask: Can a remote adversary weaponize the honest use of AI in science to compromise scientific integrity? We envision and empirically evaluate a new attack, indirect data poisoning, in which an adversary corrupts an open dataset and uploads the poisoned variant to a public repository. Autonomous research agents may independently retrieve and process this data, turning honest scientists into the unpaid and unwitting distributors of fraud at scale. Across five socially-salient topics, from hiring discrimination to the safety of autonomous vehicles, three widely used frontier AI systems (Claude Code with Claude Opus 4.7, Codex with GPT-5.5, Gemini CLI with Gemini 3.1 Pro), and 450 ethically contained experimental runs, we find that poisoning succeeds in 49.56% of runs, while the rate of poisoning detection is only 6.0%. The attack requires no topic-specific trigger-words, agent access, indirect prompt injection, or fabricated papers, only the open data ecosystem and misleading metadata. To mitigate the attacks, we propose and evaluate two measures: a scientist persona and a data provenance audit with five checks (referencing papers, social markers, statistical anomalies, related datasets, poisoning caution). We find that the persona still leaves 16.67% of runs with a poisoned conclusion, but provenance auditing reduces attack success rate to zero. Our results suggest that indirect data poisoning may enable scientific fraud at unprecedented scale, but these attacks can be mitigated with suitable auditing by agents during data retrieval.

---


### 207. [A Corpus of Persuasion Techniques in Slavic Languages](https://arxiv.org/abs/2607.10715)

**<font color=#1a73e8>作者：</font>** Jakub Piskorski, Dimitar Iliyanov Dimitrov, Marina Ernst 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persuasion techniques are powerful rhetorical devices used to sway public opinion in a wide range of media. We present a new corpus of persuasion techniques, focusing on Slavic languages. The corpus contains documents in Bulgarian, Polish, and Russian, annotated with persuasion techniques at the coarse-grained text-span level and fine-grained sentence level. The techniques are drawn from a taxonomy of 25 fine-grained persuasion techniques, grouped under six broad categories of rhetorical persuasion strategies. The corpus contains approximately 7500 text spans from 222 documents that cover topics hotly debated at the national and international levels. We describe the corpus creation process, provide detailed statistics, and examine correlations between topics and persuasion techniques. We use classic ML-based and generative AI-based models to provide baselines and benchmark results for the detection and classification of persuasion techniques at the text-span level and sentence level.

---


### 208. [Scaffold splits hide structural-frontier failures in ADMET models](https://arxiv.org/abs/2607.10729)

**<font color=#1a73e8>作者：</font>** Jiacheng Zheng, Chang Guo, Zixuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property models are commonly evaluated by holding out Bemis--Murcko scaffolds, yet a scaffold identifier is only one notion of chemical unfamiliarity. We introduce a label-free structural-frontier split that reserves the sparsest and most physicochemically remote scaffold groups, and evaluate it on six public experimental or curated ADMET tasks. Against a 70/10/20 scaffold control with identical acyclic grouping, the frontier inflates equally weighted primary error with a taskwise median of 87.0\% and a skew-sensitive mean of 130.3\% (descriptive task/seed bootstrap interval, 52.1--246.0\%). The mean falls to 75.9\% once BBB is removed; that endpoint is the one whose score ranking inverts at the frontier. A message-passing graph-network control still shows a large gap (mean 82.8\% over four tasks) and does not invert, so a low-capacity head does not explain the effect. We also test Multi-View Frontier Risk Extrapolation (\method), a count-adjusted tail-risk penalty over four molecular views, and treat it as a falsifiable probe. It changes normalized frontier error by only 0.16\% relative to empirical risk minimization for the perceptron head (interval, $-0.43$--0.84\%) and by $-1.9$\% for the graph network; three fixed robust-penalty controls are likewise inconclusive. Against the published Lo-Hi and DataSAIL splitters the frontier inflates error more on average, though no split is uniformly hardest. An audit of 31,561 marine natural products further shows that OOD status and agreement with legacy ADMET predictions depend on the molecular view, endpoint and teacher coverage. Split construction and label provenance are important evaluation constraints in their own right, and the tested training penalties do not resolve the frontier failures we observe.

---


### 209. [To Answer or to Abstain: Mitigating Search-Agent Hallucinations via Abstention-Aware Reinforcement Learning](https://arxiv.org/abs/2607.10738)

**<font color=#1a73e8>作者：</font>** Fengji Zhang, Tianyu Fan, Yuxiang Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in equipping Large Language Models (LLMs) with search tools and outcome-reward reinforcement learning (RL) have achieved new state-of-the-art results on open-domain QA tasks. However, we argue that current training paradigms harbor a critical vulnerability: they predominantly reward correct answers but fail to penalize fabricated ones when retrieval fails, thereby implicitly exacerbating hallucinations. To address this, we propose Abstention-Aware Reinforcement Learning (AWA-RL), which dynamically shapes the abstention reward utilizing the model's query-specific prior capabilities and continuous on-policy training observations. We also introduce a novel metric, RA-F1, to measure the capability-reliability trade-off. Compared to non-abstaining baselines, AWA-RL boosts absolute precision by up to 10.3% and overall RA-F1 by 2.9%, with only marginal sacrifice in raw accuracy. These results confirm that AWA-RL successfully yields highly capable and reliable search agents. The code, data, and model weights are publicly available at this https URL.

---


### 210. [Multi-Scale Convolution with Optimal Transport Attention Effect on Multivariate Time Series](https://arxiv.org/abs/2607.10740)

**<font color=#1a73e8>作者：</font>** HaoChong Fu, Jian Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The analysis of Multivariate Time Series (MTS) plays an important role in a lot of real-world practical applications, but it still remains some challenging problem about capturing multi-granularity structural patterns and suppressing noise appropriately. Multi-Scale Convolution with Optimal Transport Attention (MSC-OT) is proposed in this paper. MSC-OT is a useful architecture to optimize the attention mechanism. It combines multi-scale convolution with Sinkhorn optimal transport method based on inverted embedding. The inverted embedding approach embeds each variable as a token and allows the model to capture cross-variate relationships better. MSC-OT consists of two part: (1) Multi-Scale Convolution Enhancement, that applies multi-scale convolutions to attention score matrices based on inverted embedding, capturing local structural patterns in the variate-interaction space induced by compressed temporal representations; (2) Sinkhorn Optimal Transport Regularization, that formulates attention computation as an optimal transport problem and employs iterative matrix scaling to ensure balanced information flow across variates. Adaptive Fusion Strategy utilizes softmax-normalized learnable weights to dynamically combine base attention, convolution-enhanced, and OT-regularized scores. Experiments on widely-used datasets, including ETT, Electricity, Traffic, Solar-Energy, and Exchange-Rate, show that MSC-OT achieves well performance in both short-term and long-term forecasting tasks. Ablation experiments further validate the effectiveness of each proposed component and their synergistic contributions to improving prediction accuracy for multivariate time series forecasting.

---


### 211. [A Verifier-Centric Conceptual Model for Digital Credential Ecosystems](https://arxiv.org/abs/2607.10747)

**<font color=#1a73e8>作者：</font>** Shigeya Suzuki, Ryosuke Abe  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital credential ecosystems increasingly combine multiple standards. Because implementations have evolved independently across jurisdictions and application domains, systems described under the common label ``digital credential'' often remain mutually non-interoperable. Conventional element-by-element comparisons of identifiers, data models, credential formats, protocols, and signature algorithms do not explain why interoperability fails even when stacks share a data model, nor do they identify what a verifier must obtain, and what it must trust, before accepting a credential. We present a verifier-centric conceptual model built on two decompositions. The first separates credential processing into signature verification (L1), semantic interpretation (L2), and validation (L3), and models the supporting materials through two orthogonal planes: Constitution, which captures ecosystem-level arrangements and trust declarations, and Logistics, which captures how verification materials are stored and delivered; the Shinken framework makes trust assumptions explicit across all five functions. The second characterizes where each function may be placed along three dimensions (placement, timing, and disclosure). From the condition of being verifiable, the model derives seven consequences, distinguished as definitional corollaries, operational implications, and design trade-offs. Applying the model to four learner-credential stacks and to existing ecosystems including authentication federations, we show that it explains interoperability failures, verifier-side burden, offline verifiability, privacy implications, and terminological ambiguities that element-wise comparison leaves unresolved.

---


### 212. [Policy-Driven CT-Agent: Modeling Phase-Aware Diagnostic Control for Clinically Consistent CT Reasoning](https://arxiv.org/abs/2607.10748)

**<font color=#1a73e8>作者：</font>** Yanmeng Dong, Han Li, Yujia Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computed Tomography (CT) diagnosis often relies on dynamic selection of imaging phases, such as non-contrast, arterial, or venous phases, based on preliminary findings, clinical suspicion, and diagnostic guidelines. This phase-wise decision process is critical for reducing unnecessary radiation exposure while supporting timely staging and treatment planning. However, phase-selection protocols can vary across hospitals, regions, and guidelines, while most existing CT-based AI methods assume that all phases are available and focus on static tasks under a fixed imaging phase, failing to model whether additional phases are required. This limitation stems from heterogeneous multi-phase representations, the need for knowledge-guided phase control beyond visual cues, and the lack of supervision for phase-sufficiency decisions in existing datasets. To address these challenges, we propose Policy-Driven CT-Agent (PD-CTAgent) for clinically consistent CT phase selection and diagnostic reasoning. PD-CTAgent introduces a Clinical Structure Abstraction Module (CSAM) to harmonize heterogeneous CT phases into a unified, phase-aware evidence representation. Based on this representation, a Knowledge-Guided Diagnostic Control Model (KDCM) evaluates phase sufficiency and iteratively requests additional phases when necessary. The policy-driven agent design further allows PD-CTAgent to flexibly follow different institutional, regional, or guideline-specific diagnostic protocols. Together, PD-CTAgent bridges static CT analysis and real-world clinical workflows. Experiments on two public datasets, LIDC and MCT-LTDiag, and one private dataset demonstrate its effectiveness and clinical consistency. Code will be made public upon acceptance.

---


### 213. [Water Reflection Detection Using Symmetric Attention](https://arxiv.org/abs/2607.10749)

**<font color=#1a73e8>作者：</font>** Shuxuan Yao, Chengjia Wang, Jianyuan Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reflections of water pose a significant challenge for computer vision systems, as standard deep learning models frequently confuse objects with their mirror images, producing spurious false positives and negatives in tasks such as object detection and semantic segmentation. As a result, detecting reflection axes in natural-water scenes is pivotal for reliable object detection and scene understanding. To mitigate this issue, we leverage the intrinsic imperfect reflective symmetry of water and introduce a Symmetry-Aware Water Reflection Detection Network, namely, SAWRD-Net, that couples dihedral group-equivariant convolutions with a matrix-decomposition decoder in an end-to-end framework. First, dihedral group convolutional layers extract geometry-consistent feature maps that explicitly encode both rotational and mirror symmetries. A Multi-scale Reflection Equivariant block then aggregates features across scales and employs a symmetric-attention mechanism to highlight reflection-relevant regions. The proposed matrix-decomposition decoder factorizes high-dimensional features into compact low-rank parameter and confidence spaces, after which the network directly regresses keypoints on the reflection axis. Then a robust principal component analysis fits the final axis. Evaluated on the largest available water reflection scene data set, SAWRD-Net achieves a true-positive rate of 0.890 against human annotations, outperforming all existing water reflection detectors.

---


### 214. [The VC dimension of partial concept classes via Radon's theorem](https://arxiv.org/abs/2607.10751)

**<font color=#1a73e8>作者：</font>** Grigory Ivanov, Attila Jung, Márton Naszódi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Following Alon, Hanneke, Holzman, and Moran (FOCS 2021), we define a partial concept class (PCC) as a family of partial functions \(f: V\to\{0,1,\ast\}\); equivalently, its concepts partition the ground set into black ($f^{-1}(1)$), grey ($f^{-1}(\ast)$), and white parts ($f^{-1}(0)$). Its VC dimension is defined by shattering sets on which the value $\ast$ is not taken. We study two geometric PCCs in real Banach spaces, both with a margin \(\delta>0\): expanded half-spaces, where the grey part is a strip of width at least \(\delta\) adjacent to a half-space, and expanded balls, where the grey part is an annulus of width \(\delta\) around a unit radius ball.
Our main results are dimension-free upper bounds on the VC dimension of the PCC of expanded balls in \(L_p\parenth{\mu}\), \(1\le p<\infty\), including the non-Euclidean and algorithmically particularly relevant case \(\ell^d_1\). These bounds depend on the margin and on the radii, but not on the ambient dimension or the underlying measure space. These are extensions of the work of Bourneuf, Charbit, and Thomassé (FOCS 2025) who studied the PCC of expanded balls in Euclidean space, that is, $\ell_2^d$. We also prove lower bounds on the VC dimension that match the upper bounds in terms of the margin parameter $\delta$. Finally, we derive a Dense Neighborhood Lemma in \(L_p\)-spaces, again extending the known Euclidean results.
Our method relies on the linearization of the distance through a map into a space of non-trivial Rademacher type, and then the use of a balanced signed-sum estimate, or a no-dimensional Radon theorem. The arguments rely on ideas from functional analysis that are clearly explained for the non-expert in that field.

---


### 215. [TriCons-Pose: Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation](https://arxiv.org/abs/2607.10754)

**<font color=#1a73e8>作者：</font>** Zuzhi Yang, Shuai Wang, Mounir Kaaniche 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level object pose estimation is a crucial yet challenging task in both academia and industry, and has achieved remarkable success by leveraging keypoint-based correspondence paradigms. However, most existing methods increasingly rely on stronger feature learning while overlooking whether the established correspondences are geometrically stable across diverse perturbations. This often results in fragile pose recovery under intra-class shape variations and occlusions. To tackle this challenge, we develop a novel Triangle-Invariant Geometric Consistency Learning for Category-Level Object Pose Estimation (TriCons-Pose) to anchor stable keypoints and aggregate pose-invariant cues, yielding reliable canonical mapping and accurate pose estimation. Specifically, a Structure-Consistent Keypoint Detector (SCKD) is designed to identify robust keypoints by enforcing cross-view structural consistency via normalized pairwise distance matching. Moreover, we propose a Pose-Invariant Geometric Aggregator (PIGA) to augment keypoint representations by injecting triangle-based pose-invariant descriptors into a local-to-global attention mechanism. The proposed framework is optimized using standard objective functions while incorporating an additional geometry consistency loss. Extensive experiments on REAL275, CAMERA25, and HouseCat6D datasets demonstrate the effectiveness of the proposed approach.

---


### 216. [Opti-Agent-Bench: Benchmarking End-to-End Optimization R&D Agents on Real-World Business Problems](https://arxiv.org/abs/2607.10768)

**<font color=#1a73e8>作者：</font>** Yongchang Fu, Xinjie Huang, Chengjun Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are increasingly deployed to solve optimization problems, yet existing benchmarks evaluate them on pre-structured mathematical formulations that bypass the most critical challenge: translating complex business requirements into correct models and solve efficiently. We introduce Opti-Agent-Bench, an end-to-end benchmark that evaluates Large Language Models (LLMs) across the complete optimization R&D pipeline, from understanding business-language descriptions through mathematical modeling, algorithm selection, and code implementation, to solution report generation. Our design rests on three pillars: (1) businesssemantic authenticity with anti-template traps that defeat pattern matching; (2) modular evaluation with cross-module consistency checking across Problem Understanding, Formal Modeling, Implementation, and Reporting; and (3) the ORAC bi-level validity framework that simultaneously ensures task quality and scoring integrity. Across several industrialscale tasks spanning integer programming, robust optimization, stochastic programming, and non-convex optimization, we expose critical failure modes of current models, including constraint omission, model-code inconsistency, and report-implementation divergence, that remain invisible under conventional single-metric evaluation.

---


### 217. [RED-Sphere: Hyperspherical Residual Edge Debiasing for Cross-Population Fundus Disease Domain Generalization](https://arxiv.org/abs/2607.10777)

**<font color=#1a73e8>作者：</font>** Yan Lin, Ziheng Wang, Shuang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image classifiers are often trained within one source population, yet clinical deployment requires robustness to patients whose appearance, acquisition style, and disease prevalence differ from the source cohort. Existing fairness and robustness methods often require group supervision or treat appearance variation as an undifferentiated nuisance, which is insufficient when population-correlated low-level cues and lesion evidence share edge and texture structure. We study a strict source-only cross-population setting, where external populations are unseen during optimization, validation, scheduling, hyperparameter and model selection. We propose RED-Sphere, a plug-and-play robustness framework for image classification under unseen population shifts. It estimates shortcut-sensitive nuisance responses with an edge and feature energy prior, attenuates dominant responses through residual soft gating, regularizes masked nuisance views with counterfactual-inspired consistency and separation losses, and predicts labels with normalized spherical prototypes. It favours angular semantic evidence over source-correlated activation magnitude while preserving lesion structure. Although demonstrated on 2D Scanning Laser Ophthalmoscopy (SLO) fundus classification for Age-Related Macular Degeneration (AMD) and Diabetic Retinopathy (DR), RED-Sphere is not tied to retinal anatomy: the same principle can be adapted with modality-specific nuisance priors wherever appearance shortcuts and semantic evidence are entangled. Under a strict White-only Harvard-FairVision protocol, RED-Sphere improves held-out macro-F1 across all 20 task and backbone comparisons, with average gains of 1.28 and 2.98 F1 points on AMD and DR. Gains in AUC and PR-AUC, visual diagnostics, ablations, and sensitivity analyses further support stronger external semantic alignment and more stable angular disease geometry.

---


### 218. [Toward Efficient Weakly Supervised Semantic Segmentation Using Only Low-Magnification Histopathological Images](https://arxiv.org/abs/2607.10783)

**<font color=#1a73e8>作者：</font>** Dung Minh Do, Nhat-Thanh Huynh, Duc Minh Huynh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide images (WSIs) provide rich tissue-level and cellular-level information, but storing and transmitting high-magnification pathology data is resource-intensive. Moreover, annotating WSIs at the pixel level is labor-intensive and time-consuming. Therefore, it is important to investigate whether low-magnification pathology images with limited annotations (i.e., image-level instead of pixel-level labels) can achieve performance comparable to high-magnification images. This paper presents a systematic benchmark study on weakly supervised histopathological image segmentation under different low-resolution storage settings. Starting from high-resolution image patches, we simulate lower-magnification inputs and reconstruct them to the original size using interpolation and deep learning-based reconstruction methods before applying the weakly-supervised segmentation pipeline. This framework enables a quantitative evaluation of how weakly supervised methods respond to different levels of resolution degradation. Experimental results show that reconstruction quality metrics alone are insufficient to predict downstream segmentation performance. In particular, the study identifies a critical degradation point where the localization of small-scale structures declines significantly. These findings provide practical guidance for designing efficient digital pathology storage systems while maintaining reliable automated analysis. Code is available at this https URL

---


### 219. [LSTrans: Efficient Knowledge Transfer for Lightweight and Automated ECG Classification](https://arxiv.org/abs/2607.10784)

**<font color=#1a73e8>作者：</font>** Yi Zhao, Jiajun Gao, Chenyang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying deep learning models for automated electrocardiogram classification on resource-constrained wearable devices remains challenging due to high computational costs. To address this, we propose LSTrans, a lightweight hybrid model designed for efficient and sensitive ECG analysis. LSTrans introduces a specialized 1D convolutional backbone with an interleaved layer architecture to capture both macroscopic rhythmic trends and microscopic morphological variations. This backbone is cascaded with a Transformer encoder to model long-range temporal dependencies, incorporating Low-Rank Adaptation across critical layers to compress the model and reduce the trainable parameter space. We further employ homogeneous and heterogeneous knowledge distillation to transfer diagnostic expertise from high-capacity teacher models to the student. Experimental results on multiple benchmark datasets demonstrate that LSTrans achieves a competitive balance between diagnostic sensitivity and resource efficiency, substantially reducing peak memory footprints and training latency during downstream adaptation. The source code is available for review at this https URL.

---


### 220. [Detecting AI-Generated Video: A Vision-Language Dual-View Survey](https://arxiv.org/abs/2607.10787)

**<font color=#1a73e8>作者：</font>** Dylan Xinming Hou, Juntian Zhang, Xu Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The evolving realism of AI-generated Videos (AIGC-V) is rapidly rendering traditional artifact-centric detection insufficient, necessitating a paradigm shift from low-level inspection to high-level semantic verification. This paper presents a comprehensive survey of AIGC-V detection, reframing the task as Factual Fidelity Verification, which asks whether the events, entities, and physical processes depicted in a video are consistent with real-world facts. To systematize this rapidly evolving field, we propose a Vision-Language Dual-View taxonomy that organizes existing methods into a hierarchical, four-layer landscape, spanning intrinsic cue analysis, spatiotemporal consistency modeling, cross-modal consistency reasoning, and language-guided world-level reasoning. This dual-view framing highlights a fundamental transition from artifact matching in traditional deepfake detection to evidence-based semantic verification enabled by vision-language models and agentic reasoning pipelines. Based on a systematic review of 221 works, we synthesize AIGC-V generation paradigms, survey the landscape of detection methods, and review evaluation metrics and benchmarks in line with proposed views. Finally, we discuss current challenges and identify promising directions toward robust, explainable, and trustworthy detection.

---


### 221. [MAC-Splat: Multi-Attribute Consistency for High-Fidelity Sparse-View Reconstruction](https://arxiv.org/abs/2607.10792)

**<font color=#1a73e8>作者：</font>** Jinqian Yang, Yichen Wu, Wanhua Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing high-fidelity 3D scenes from sparse-views remains a central problem in generalizable neural rendering. Existing generalizable 3D Gaussian Splatting (3DGS) methods often exhibit geometric artifacts in sparse-view settings, since supervision based solely on 2D photometric losses cannot resolve depth and correspondence ambiguities. To address this issue, we propose MAC-Splat, a training framework built around direct 3D consistency supervision. MAC-Splat builds on the MASt3R geometric backbone and a frozen DINOv3 encoder to obtain semantically informed 2D correspondences, which serve as geometric anchors for 3D supervision. Using these anchors, we define the Multi-Attribute Consistency (MAC) loss. This objective jointly regularizes the 3D attributes of matched Gaussians, including their position, shape, and appearance, by enforcing agreement in a common world coordinate frame. The formulation is robust to outliers and respects the geometry of covariance matrices, which leads to stable training under sparse-view conditions. Experiments on ScanNet++ show that MAC-Splat outperforms strong baselines, with particularly large gains under different overlap regimes. In particular, it improves average PSNR over Splatt3R by more than 4.5 dB, reduces LPIPS, and maintains performance as the camera pose gap increases. These results indicate that a direct, multi-attribute 3D consistency objective, when combined with high-quality correspondences, is effective for addressing the ill-posed sparse-view reconstruction problem.

---


### 222. [Hierarchical Bayesian Quadrature](https://arxiv.org/abs/2607.10793)

**<font color=#1a73e8>作者：</font>** Tim Weiland, Toni Karvonen, Philipp Hennig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical integration is a cornerstone of various scientific computing applications, such as engineering simulations and model evidence computations in probabilistic machine learning. Bayesian Quadrature uses Gaussian process surrogates that explicitly encode structural assumptions about the integrand to obtain integral estimates with quantified uncertainty. These surrogates are predominantly based on stationary covariance functions, which results in model misspecification for integrands exhibiting nonstationary behavior. We tackle this issue through an adaptively growing, tree-based partition of the integration domain into local stationary models. Our method recombines the local integral estimates through a hierarchy of GP conditioning that reintroduces cross-subdomain correlations, while model selection criteria control the tree growth to avoid unnecessary partitioning. The resulting algorithm is simple, requires no MCMC, and adapts its evaluation budget to local integrand complexity. On benchmark integration problems and a model evidence computation for an epidemiological model, Hierarchical Bayesian Quadrature achieves substantial gains over standard Bayesian Quadrature on nonstationary integrands while matching its performance on stationary ones.

---


### 223. [STEC: Evidence Compression for Deep Search in Open-domain Multi-Hop QA](https://arxiv.org/abs/2607.10795)

**<font color=#1a73e8>作者：</font>** Xinkang Li, Rong Jiang, Xin Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In open-domain multi-hop question answering (QA), LLM-based search agents offer a promising approach to knowledge-intensive QA by combining retrieval with reasoning. Existing methods mainly improve open-domain multi-hop QA through reasoning paradigms, retrieval interaction, and search strategy optimization. However, using multiple search trajectories introduces a challenging final answer selection problem. Different trajectories may support different candidates, and the retrieved information can be heterogeneous, redundant, incomplete, or conflicting. Directly comparing raw trajectories exposes the verifier to noisy and unaligned content, while comparing answer strings ignores the evidence supporting each candidate, making reliable final selection difficult. To address this challenge, we propose STEC, an evidence compression framework for final answer selection in multi-hop QA. STEC selects the final answer from the existing candidate set through two mechanisms: (1) Answer-Level Evidence Compression, which groups trajectories by normalized answer identity and converts each answer group into a candidate-specific evidence representation; and (2) Evidence-Guided Answer Verification, which compares these representations and selects the final answer from the candidate set. The design shifts final selection from raw trajectory comparison to candidate-level evidence comparison. We evaluate STEC on four open-domain multi-hop QA benchmarks against representative baselines. Experimental results show that STEC performs best overall among the compared methods, and ablation results provide evidence that answer-level evidence compression contributes to final answer selection.

---


### 224. [h-Flow: Flexible Flow-based Image Editing via Doob's h-Transform](https://arxiv.org/abs/2607.10800)

**<font color=#1a73e8>作者：</font>** Zehui Guo, Zhen Wang, Junwei Shu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Editing images with pre-trained text-to-image flow models typically requires carefully balancing target alignment with the desired prompt and source consistency with the original image. Existing approaches either rely on inversion-based pipelines or heuristic source-to-target trajectory constructions, which often depend on architecture-specific designs or are sensitive to hyperparameters. In this paper, we propose h-Flow, a training-free and theoretically grounded flow-based editing framework. Inspired by Doob's $h$-Transform, we reformulate image editing as conditional generation under multiple terminal events corresponding to source consistency and target alignment. We first extend the classical $h$-Transform from SDE-based models to the deterministic RF framework by constructing an equivalent SDE with identical marginals. Within this formulation, we design dedicated $h$-functions for source consistency and target alignment, yielding closed-form reconstruction guidance and velocity-based semantic editing signals. We further introduce a velocity orthogonal decomposition to decouple reconstruction and editing directions, enabling a controllable trade-off between the two objectives. Extensive experiments demonstrate that h-Flow achieves effective, robust, and flexible editing across diverse scenarios. The code will be released soon.

---


### 225. [When does distribution shift break graph neural networks calibration?](https://arxiv.org/abs/2607.10804)

**<font color=#1a73e8>作者：</font>** Abderaouf Bahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are increasingly deployed in real-world applications where distribution shift is un-avoidable. However, how such shifts affect model calibration, defined as the agreement between predictive confidence and actual accuracy, remains poorly understood, and existing graph calibration methods typically rely on labeled validation data from the deployment distribution. In this work, I present the first closed-form theoretical characterization of GNN calibration under distribution shift. I show that calibration is governed by a single scalar quantity that explicitly depends on structural changes between the source and target graphs, as well as feature quality. This characterization precisely identifies when a model becomes over-confident, under-confident, or remains calibrated, and directly yields the optimal temperature scaling strategy. I further extend the analysis to graph convolutional networks with symmetric normalization, multi-class classification, and covariate shift, and derive a theoretical upper bound on the expected calibration error. My analysis also reveals that, under homogeneous distribution shift, a single global temperature is theoretically optimal, providing a principled explanation for why more complex node-wise recalibration methods offer no additional benefit. Building on these theoretical insights, I propose STAC, a source-free, label-free calibration method. Experiments on synthetic benchmarks demonstrate substantial calibration improvements, while evaluations on five real-world graph datasets show that reliable calibration without target labels remains challenging despite the strong predictive power of the theory.

---


### 226. [Abstractiveness Metrics for Evaluating Text Summarization: A Refined Formulation with Empirical Validation](https://arxiv.org/abs/2607.10806)

**<font color=#1a73e8>作者：</font>** Praveenkumar Katwe, Rakesh Chandra Balabantaray, Kali Prasad Vittala  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantifying abstractiveness in generated summaries is essential for evaluating summarization models beyond
surface-level metrics like ROUGE. We introduce Reference Abstraction (RA), Summary Abstraction (SA), and Abstraction
Ratio (AR) -- a set of principled heuristic metrics that measure how much a summary diverges from extractive copying
of the source text. The formulation uses the harmonic mean of document lengths modulated by a cubic non-overlap
factor, yielding dimensionally consistent, bounded output with non-linear sensitivity to the extractive-abstractive
boundary. Evaluation on 100 XSUM documents across four summarization models (BART-large-cnn, Pegasus-xsum, DistilBart,
MT5-small) demonstrates that the metrics successfully discriminate between extractive models (SA ~ 0.12-0.26) and
abstractive models (SA ~ 0.96-1.77), and that the Abstraction Ratio identifies summaries requiring manual evaluation
for potential hallucination. Code and results are available at this https URL.

---


### 227. [Lower Bound on the Cumulative Constrained Violation for the OGD+Projection algorithm for Constrained Online Convex Optimization (COCO)](https://arxiv.org/abs/2607.10808)

**<font color=#1a73e8>作者：</font>** Haricharan Balasundaram, Karthick Krishna Mahendran, Rahul Vaze  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of constrained online convex optimization is considered, where at each round, once a learner commits to an action $x_t \in \mathcal{X} \subset \mathbb{R}^d$, a convex loss function $f_t$ and a convex constraint function $g_t$ that drives the constraint $g_t(x)\le 0$ are revealed. The objective is to simultaneously minimize the static regret and cumulative constraint violation (CCV) compared to the benchmark that knows the loss functions and constraint functions $f_t$ and $g_t$ for all $t$ ahead of time, and chooses a static optimal action that is feasible with respect to all $g_t(x)\le 0$. Currently, the best known algorithm is OGD+Projection algorithm of [Vaze and Sinha, 2025] that has simultaneous regret of $O(\sqrt{T})$ and CCV of $O(T^{1/3})$ for $d=2$ [Balasundaram et al., 2026], and simultaneous regret of $O(\sqrt{T})$ and CCV of $O(\sqrt{T})$ for any $d$ [Sarkar and Sinha, 2026]. In this paper, we show that the CCV of the OGD+Projection algorithm is $\Omega (T^{\frac{d-1}{2d}})$. This is the first such lower bound result.

---


### 228. [Diachronic Sample Integration: Robust Tail-Risk Estimation with Generative Models](https://arxiv.org/abs/2607.10810)

**<font color=#1a73e8>作者：</font>** Shuning Zhao, Patrick Wong, Leran Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models are increasingly used as simulators for downstream decision-making under data scarcity, but in risk-sensitive applications their usefulness depends on rare adverse scenarios rather than typical samples. Standard generative objectives prioritize bulk distributional fidelity, leaving low-probability tails vulnerable to localized optimization noise and making tail-dependent functionals unstable under finite simulation budgets. We introduce Diachronic Sample Integration (DSI), a test-time inference framework that ensembles generated samples across checkpoints from a stochastic training trajectory. DSI targets a checkpoint-mixture distribution that averages checkpoint-specific tail fluctuations rather than relying on a single brittle endpoint. We formalize this mechanism through a finite-budget bias-variance theory. Empirically, across multivariate synthetic processes and high-frequency trading data, DSI substantially reduces tail-estimation error compared to single-checkpoint baselines under fixed simulation budgets, outperforming standard diffusion and state-of-the-art tail-aware baselines without modifying the generative objective.

---


### 229. [Graph Neural Networks for RFID-Based Spatial Geometry Inference in Spatial AI Systems](https://arxiv.org/abs/2607.10822)

**<font color=#1a73e8>作者：</font>** Curtis Shull, Merrick Green, Roy Rucker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indoor spatial understanding remains a fundamental challenge for intelligent systems operating in physical environments. Traditional RFID localization techniques typically estimate positions of tags using signal strength measurements but fail to capture higher-order spatial relationships between objects and infrastructure. Recent work on RFID and wireless indoor localization has increasingly emphasized robust learning under noisy propagation, while recent graph-based localization methods demonstrate the value of relational modeling over isolated samples. This paper introduces a graph-based learning framework that leverages Graph Neural Networks (GNNs) to infer spatial geometry from RFID observations. Rather than predicting isolated coordinates, the proposed system models relationships between RFID readings, antennas, and physical structures within an indoor floorplan. This framing is aligned with recent graph-based indoor positioning and graph construction literature, where topology is a first-class source of information for downstream inference. The approach integrates signal strength data, floorplan semantics, and spatial constraints into a graph representation where nodes correspond to RFID observations and edges encode proximity and contextual relationships. A GNN is then trained to predict geometric patterns such as linear trajectories, rectangular bounding regions, and movement paths of objects in space.

---


### 230. [Automated Stealthy Wear-Out Attack on Digital Twins With Deep Reinforcement Learning](https://arxiv.org/abs/2607.10830)

**<font color=#1a73e8>作者：</font>** Joshua Haworth, Aryan Pasikhani, George Pavlides 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital Twins (DTs) have emerged as pivotal enablers of Industry 4.0, offering transformative capabilities such as real-time monitoring, advanced simulation, and precise control of physical assets. By bridging the physical and virtual domains, DTs facilitate seamless integration of data-driven decision-making and operational optimisation. However, this seamless interaction significantly expands the attack surface of industrial systems, creating vulnerabilities that adversaries can exploit. This paper introduces a novel and stealthy wear-out attack leveraging Deep Reinforcement Learning (DRL) to target DT-enabled infrastructures. The adversary strategically and covertly manipulates control signals, inducing increased torque on a specific joint to accelerate wear and tear while evading detection by a state-of-the-art anomaly detection system. Extensive benchmarking of reinforcement learning algorithms - including Twin Delayed Deep Deterministic Policy Gradient (TD3), Soft Actor-Critic (SAC), Proximal Policy Optimisation (PPO), and Advantage Actor-Critic (A2C) - revealed that SAC consistently outperformed its counterparts in terms of sample efficiency, stability, and overall attack effectiveness. We evaluate the proposed adversary in an industrial setting using the UR10e robotic arm. Results demonstrate the adversary's ability to significantly elevate torque levels on the targeted joint, leading to accelerated degradation and increased maintenance costs, all while operating stealthily and avoiding detection. Our findings highlight the substantial risks posed by DRL-driven adversaries to DT-enabled environments and emphasise the critical need for robust defence mechanisms to protect critical industrial systems.

---


### 231. [Route, Communicate, and Reason: Gated Routing and Adaptive Depth for Efficient Multi-Agent Reasoning](https://arxiv.org/abs/2607.10836)

**<font color=#1a73e8>作者：</font>** Sudipto Ghosh, Tanmoy Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent ensembling multiplies active parameters and inference cost without answering three basic questions: which agents to consult, how deeply a query should traverse a hierarchy of agents, and when inter-agent communication is worth its cost. We present GRADE (Gated Routing and Adaptive Depth for Efficient Reasoning), a hierarchical multi-agent system in which four lightweight learned gates jointly govern agent selection, hierarchy depth, inter-agent communication, and branch pruning. Training uses CoGRPO (Collaborative Group-Relative Policy Optimization), a novel critic-free recipe that adapts GRPO to multi-agent hierarchies and assigns a shared advantage signal to every gate and agent that participated in a rollout. Agent models are drawn from a hot-swappable Expert Registry; per-agent calibration maps allow experts to be replaced at inference time without retraining. At $\sim$17B average active parameters, GRADE outperforms all baselines on GSM8K, MMLUPro, and GPQA, surpassing the strongest baseline by 4.8 points on MMLUPro at half the active compute. On AIME-2025, where model depth dominates, GRADE remains competitive to existing frameworks. Ablations isolate the hierarchy and masked cross-attention as the largest contributors to accuracy, and show that per-agent calibration is necessary for safe hot-swapping.

---


### 232. [OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields](https://arxiv.org/abs/2607.10840)

**<font color=#1a73e8>作者：</font>** Yanqin Jiang, Tengfei Wang, Zhengwei Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Previous feed-forward 4D reconstruction methods either predict per-frame static point clouds, ignoring foreground motion, or estimate point cloud trajectories while being limited to small camera motions. This restricts their ability to aggregate observations over time and reconstruct complete dynamic scenes under large viewpoint changes. To address this limitation, we propose OmniX, a feed-forward 4D reconstruction framework that predicts dense 3D point trajectories for every pixel from videos with large camera motion. OmniX decouples dynamic motion modeling from static geometry prediction and represents motion using a compact set of dynamic tokens. By leveraging the sparse and low-rank structure of 3D motion, these tokens generate trajectory fields for all pixels across all images while efficiently preserving global interactions. To facilitate training, we further build an automatic UE5-based 4D data engine and introduce a large-scale dataset containing 80K scenes and 1.28M multi-view videos with full geometric annotations. OmniX achieves state-of-the-art performance on dense 3D point trajectory prediction and 3D point tracking, while also demonstrating competitive results on video depth estimation and camera pose estimation.

---


### 233. [Align and Segment: Unsupervised Learning for Building Segmentation From Misaligned Labels](https://arxiv.org/abs/2607.10841)

**<font color=#1a73e8>作者：</font>** Venkanna Babu Guthula, Oswin Krause, Dimitri Gominski 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised learning for image segmentation typically requires spatially aligned image and label sets. When images and labels originate from different sources, the pairing may be misaligned, which can significantly deteriorate the performance of the learned models. This is especially common in remote sensing, when aerial or satellite images are co-registered with labels from another source (e.g., OpenStreetMap). In this work, we propose a novel approach for training on misaligned labels, where we simultaneously learn the label alignment. Our align and segment (AnS) approach builds on the spatial transformer module to transform the misaligned labels using an affine transformation to provide a better learning target for a canonical semantic segmentation network. We prevent shortcut learning of misaligned labels in these semantic segmentation networks through a self-supervised regularization loss and show that it is complementary to data augmentation, especially for systematically misaligned training data. A decisive characteristic of our AnS approach is that it learns without requiring any golden labels. We experimentally show on both synthetic and real-world data from different cities that our approach enables high-quality building segmentation and precise label-image alignment at the same time. Code and derived datasets are available at this https URL

---


### 234. [FaciliTrain: Practicing Facilitation Skills through AI-Simulated Group Dialogue](https://arxiv.org/abs/2607.10850)

**<font color=#1a73e8>作者：</font>** Hang Jiang, Yuanxin Zhu, Diyi Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Skilled facilitation supports inclusive small-group dialogue, but deliberate practice is hard to scale: it depends on expert coaches, live practice partners, and iterative feedback. We present FaciliTrain, a voice-based training system in which learners step into the facilitator role of an AI-simulated multi-participant conversation, apply five evidence-based techniques, and receive structured AI feedback to support reflection. We report findings from a mixed-methods study with 24 participants, conducted as a formative study (N = 12) and a controlled pilot (N = 12; 6 treatment, 6 control). Both conditions achieved comparable accuracy on a live evaluation task, though treatment participants' self-rated comfort declined significantly while control participants' comfort improved (p = .018). Reflexive thematic analysis identifies four themes: the taxonomy externalizes implicit facilitation intuitions; Making Connections is the most cognitively demanding technique; voice acts as a deliberate-response forcing function; and participants overwhelmingly preferred AI feedback over self-practice. We discuss design implications for voice-based, AI-supported interpersonal skill training at scale.

---


### 235. [Learning To Focus: Anatomy-Guided Attention Regularization for Medical Image Classification](https://arxiv.org/abs/2607.10851)

**<font color=#1a73e8>作者：</font>** Tonmoy Hossain, Atiqur Rahman, Farhana Hossain Swarnali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image classification models are ideally expected to identify diagnostically relevant regions while making predictions, yet standard classification losses rarely provide spatial supervision. Explicit supervision via anatomical shape information, such as segmentation masks of task-relevant anatomy, has been shown to guide the network toward regions relevant to the target prediction. However, obtaining such masks incurs substantial manual annotation effort and computational overhead. With the advent of segmentation foundation models that exhibit strong localization of anatomical structures across diverse imaging modalities, we leverage this capability to extract anatomical shape priors without the burden of training a dedicated segmentation model. In this paper, we propose a new framework, Locus, an anatomical attention regularization framework that leverages pretrained segmentation foundation models to guide a classifier's attention toward diagnostically meaningful anatomical structures across diverse imaging modalities. Instead of enforcing pixel-wise alignment with the foundation-model-derived mask, we introduce a regularization term that adaptively balances attention between anatomical (foreground) and background regions, penalizing the classifier when background attention dominates. We validate Locus on eight diverse medical imaging datasets spanning dermoscopy, X-ray, histopathology, and cardiac MRI, showing consistent gains in classification performance alongside improved anatomically grounded attention.

---


### 236. [Diversify Diffusion with Temperature Sampling and Variance-Corrective Time Shifting](https://arxiv.org/abs/2607.10853)

**<font color=#1a73e8>作者：</font>** Peizhuo Li, Emre Aksan, Alexandru-Eugen Ichim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models faithfully reproduce their training distribution, but also inherit its imbalances and leave rare or under-represented modes hard to reach. A natural inference-time remedy is to sample from the high-temperature target $p^{(\gamma)}_0(x) \propto p_0(x)^{\gamma}$ for $0 < \gamma < 1$, which flattens dominant modes and lifts rare ones. However, naive score scaling while correctly reweighting modes also inflates the per-mode variance, breaking the reverse diffusion process and degrading sample quality. We introduce variance-corrective time shifting, a training-free fix that queries the network at a shifted timestep and scales the resulting score by $\gamma$, canceling the variance inflation while preserving the mode reweighting. The correction turns simple temperature sampling into a practical diversity knob for pretrained diffusion and flow-matching backbones with no retraining, and we demonstrate consistent gains at minimal cost to sample quality and condition fidelity across DiT, Stable Diffusion and Motion Diffusion models. We further show that the timing of the temperature intervention enables coarse-to-fine control: high-noise stages drive compositional diversity across modes, while low-noise stages drive local appearance variation under a fixed composition.

---


### 237. [AU-Guided Synthetic Video Generation for Micro-Expression Recognition](https://arxiv.org/abs/2607.10860)

**<font color=#1a73e8>作者：</font>** Pei-Sze Tan, Sailaja Rajanala, Yee-Fan Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-expression recognition is limited by the small scale, narrow demographic coverage, and restricted emotion labels of existing datasets. We introduce EquiME, a synthetic micro-expression dataset built from AU-guided image-to-video generation. EquiME contains 75K videos generated from 15K source face images across five target emotions, together with automatically inferred demographic metadata and video-quality measurements. We evaluate EquiME using frame-pair similarity, spatial variation, and no-reference perceptual-quality metrics, together with cross-dataset MER experiments on SAMM and CASME II. Models trained on EquiME achieve competitive cross-dataset performance on SAMM and CASME II and show comparatively low variation across the four evaluated architectures. This paper focuses on the dataset design, the structured AU-conditioning pipeline used for video generation, and the empirical evidence needed to assess EquiME as a synthetic MER resource. Project page: this https URL

---


### 238. [Singular perturbations and hierarchical learning in two-layer neural networks](https://arxiv.org/abs/2607.10869)

**<font color=#1a73e8>作者：</font>** Cédric Gerbelot, Jean-Christophe Mourrat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the population gradient flow of an infinitely wide two-layer neural network learning a misspecified single-index model in high dimension. The two layers are optimized jointly, with a perturbative parameter tuning the relative training speed between the first and second layer. This setting was considered by Berthier, Montanari and Zhou in \cite{berthier2024learning}, who conjectured a hierarchical learning scenario with explicit timescales as the second layer is trained faster than the first. In this paper, we prove that the constant and linear components of the hidden link function are indeed recovered within the predicted timescales, at sharp explicit thresholds. We then analyze the onset of learning of the quadratic component and show that the components learned at earlier stages continue to influence the dynamics in an essential way. Our proof is based on quantitative approximation results for singularly perturbed flows evolving near a manifold defined by integral constraints. At a phenomenological level, we also show that the empirical measure of the weights displays singular behaviour when reaching the quadratic component of the hidden link, with a small fraction of neurons growing significantly while the remaining ones rearrange to preserve the components already learned.

---


### 239. [X-GuideAR: An Augmented Reality Framework to Mitigate Radiation Exposure during Fluoroscopic Guidance](https://arxiv.org/abs/2607.10873)

**<font color=#1a73e8>作者：</font>** Mingxu Liu, Zixuan Liu, Ruchen Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving optimal screw placement for orthopedic surgeries requires frequent alignment checks and multiple anatomical views under X-ray -- a process known as "fluoro-hunting" that increases radiation exposure to patients and surgical teams. This work introduces X-GuideAR, an augmented reality (AR) framework for identifying optimal X-ray views, aimed at reducing radiation exposure while ensuring accurate screw placement. To exemplify the benefits of X-GuideAR, we focus on S2 alar-iliac (S2AI) screw placement. Our system provides radiation-free guidance for view acquisition and drilling by generating synthetic X-ray previews that accelerate fluoro-hunting. Once the required anatomical views are identified using these previews, a real X-ray is acquired, and the preview of the drilling trajectory is augmented onto it, facilitating precise screw placement with minimal additional radiation. A preliminary study involving eight S2AI trajectories performed by an expert spine surgeon demonstrated a 62.3% reduction in the number of X-rays. Post-procedure evaluations showed that trajectories done with X-GuideAR supported an average safe screw diameter of 12.95 mm compared to 5.9 mm under the conventional workflow, suggesting improved bony containment and potential biomechanical benefit. X-GuideAR shows great potential to reduce radiation exposure and streamline S2AI screw placement, offering a promising direction toward safer and more efficient surgeries.

---


### 240. [LOGOS: A Living Logic for AI Agent Teams That Evolve With Humans](https://arxiv.org/abs/2607.10878)

**<font color=#1a73e8>作者：</font>** Yuma Ichikawa, Yamato Arai, Kosaku Kimura 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are evolving from answer engines into persistent teams that use tools, delegate work, learn from experience, and modify the artifacts that shape their future behavior. The defining question for deployment is no longer merely what agents can do, but who controls what they are allowed to become. We introduce logos, a pluggable layer for self-evolution and governance that strengthens existing multiagent frameworks rather than replacing them. logos compiles heterogeneous multimodal inputs, including documents, images, audio, tables, databases, APIs, and human instructions into versioned agent packs containing agents, tools, knowledge, tests, permissions, and policies. During operation, it transforms agent activity into portable, auditable event traces and applies fail-closed verification across frameworks and backends. Every learned prompt, memory, skill, tool, role, or workflow remains an untrusted release candidate until held-out execution evidence, human-controlled policy, and explicit authorization permit its promotion. This architecture enables "verifiable human-agent loop engineering": agents can act, ask, learn, and propose improvements, while humans can steer objectives, permissions, approvals, and irreversible actions without interrupting continuous operation. logos provides a living logic for accountable automation. Agents may evolve at machine speed, but only evidence and human authority can close the loop.

---


### 241. [First-Order Modal Logic in HOL: Deep and Shallow Embeddings with Automated Faithfulness (Extended Preprint)](https://arxiv.org/abs/2607.10880)

**<font color=#1a73e8>作者：</font>** Christoph Benzmüller, Daniel Kirchner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We extend, in Isabelle/HOL, the deep-and-shallow embedding methodology of our prior work from propositional to first-order modal logic (FML) with constant-domain Kripke semantics. Three embeddings of FML into classical higher-order logic (HOL) are provided side by side: a deep embedding, a heavyweight maximal-shallow embedding, and a lightweight minimal-shallow embedding. The minimal-shallow embedding is presented as an Isabelle/HOL locale, parametrised by an accessibility relation, a world-indexed interpretation, a universe of worlds, and a variable assignment; the locale form admits a global faithfulness theorem, stating that quantifying over all minimal-shallow interpretations recovers exactly deep validity.
A central technical contribution is a mechanisation, for FML under constant-domain Kripke semantics, of the (countable) downward Löwenheim-Skolem theorem, which underpins the automation of our faithfulness proof between the deep and minimal-shallow embeddings. Deploying it inside an extension of the minimal-shallow locale resolves the surjectivity problem that arises against an uncountable domain of individuals -- where the locale's variable assignment, having countable domain V = nat, cannot be surjective onto the domain -- and thereby yields faithfulness over the full domain.
Since prior work treats only the propositional fragment, we develop here the substitution machinery (free/bound-variable predicates, the fresh-variable function, capture-avoiding substitution, alphabetic renaming, the substitutability predicate, the substitution lemma, and size-based induction principles) needed for the first-order quantifiers.

---


### 242. [Incremental Transformer for Surrogate-Based Inverse Design of Geopolymer Mixtures](https://arxiv.org/abs/2607.10896)

**<font color=#1a73e8>作者：</font>** Giansalvo Cirrincione, Filippo Grassia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small-data inverse design is challenging in engineering informatics when observations are heterogeneous, mixed-type, and constrained by physical relations among design variables. This work proposes a topology-aware surrogate framework guided by an Incremental Transformer (INCRT) for physics-constrained inverse design, applied to geopolymer mixture design. The method integrates intrinsic-dimensionality analysis, mixed-variable design-space representation, tabular surrogate prediction, INCRT-based manifold rationalisation, and constrained inverse optimisation. Using a public benchmark of fly-ash and slag-based geopolymer concrete mixtures with compressive-strength and carbon-emission targets, the high-dimensional design space proves strongly redundant, organising around fewer effective mixture regimes. Compressive strength requires nonlinear tabular surrogates, while carbon emission is largely determined by composition and well recovered by regularised linear models. INCRT thus acts not as a replacement for tabular predictors but as a rationalisation layer providing prototype regimes and a manifold-support score for inverse design. Three strategies are compared: unconstrained surrogate optimisation, physics-constrained optimisation, and topology-aware physics-constrained optimisation. Unconstrained optimisation can match target strength but may yield physically invalid or off-manifold candidates; physics-only constraints do not always ensure data support. The topology-aware strategy yields candidates balancing target compliance, carbon reduction, physical admissibility, and proximity to the learned feasible manifold. The framework aims not to replace experimental validation but to support screening of credible candidate mixtures from small, mixed, physically constrained engineering datasets.

---


### 243. [Design Choices in Splitting-Based Self-Supervised Sparse-View CT Reconstruction](https://arxiv.org/abs/2607.10898)

**<font color=#1a73e8>作者：</font>** Nadja Gruber, Lukas Neumann, Ander Biguri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised data splitting has emerged as a promising paradigm for sparse-view CT reconstruction, enabling training from incomplete measurements without fully sampled ground truth. However, the influence of key design choices, including partitioning strategy, preprocessing, and inference, remains insufficiently understood. In this work, we introduce a unified framework that decomposes splitting-based reconstruction into these three components, enabling controlled comparison of existing methods and two incremental extensions: multi-partition splitting and an alternative inference strategy. Experiments on simulated LoDoPaB-CT data under independent and correlated noise, together with validation on the real-world 2DeteCT dataset, show that the optimal partitioning strategy strongly depends on the measurement noise structure. Lattice-based splitting performs favorably under independent noise, whereas angular masking is more robust under correlated noise and real measured data. Multi-partition splitting consistently improves over pure projection-wise splitting in several settings. Complementary perceptual and structural metrics, including LPIPS and HaarPSI, reveal differences between masking strategies that are less apparent from PSNR and SSIM alone. These results provide practical guidelines for designing self-supervised sparse-view CT reconstruction methods and highlight the limitations of common independence assumptions in realistic imaging environments.

---


### 244. [What to Distinguish and How? Opportunities and Challenges of Augmenting Multiple, Cluttered Objects in Complex Scenes for People with Low Vision](https://arxiv.org/abs/2607.10902)

**<font color=#1a73e8>作者：</font>** Yuheng Wu, Ruijia Chen, Jaewook Lee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People with low vision (PLV) struggle to perceive complex scenes like busy kitchens and crowded streets, which contain many objects, visual clutter, and dynamic elements. Prior AR systems for low vision either enhance low-level visual features or augment task-relevant objects for single tasks in simple settings, leaving multi-object augmentation in complex scenes underexplored. Informed by a formative study characterizing important objects and their perceived importance for PLV, we built SceneGlance, a wearable AR system that recognizes important objects and visually distinguishes them by importance level. Through a controlled lab study with 12 PLV in a mock-up kitchen scene and a free-form think-aloud study with 13 PLV navigating an outdoor route, we found that AR distinction on object importance shifted PLV's attention toward objects of higher importance, and supported perception strategies such as building mental snapshots from the augmentation distribution and hierarchical scanning by importance. However, this attention shift came with a tradeoff, as augmenting many objects reduced overall scene recall. The studies also surfaced challenges posed by AR augmentations in complex scenes, such as adjacent augmentations blending or interfering with each other, yielding design implications for more practical AR vision enhancement systems in the complex real world.

---


### 245. [The Nuts and Bolts of Natural Language to SQL Translation: A Systematic Analysis of Model Pipeline Optimisation Approaches and their Interactions](https://arxiv.org/abs/2607.10911)

**<font color=#1a73e8>作者：</font>** Filip Klubicka, Vasudevan Nedumpozhimana, Sneha Rautmare 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the age of large language models, Natural Language to SQL (NL2SQL) translation remains an open problem with many useful applications. We explore interactions between several NL2SQL pipeline extensions to inspire development of more lightweight models. Specifically, we integrate the NatSQL intermediate representation, include a preprocessing step and a fine-tuning step based on synthetic data, and develop a novel reranker model to improve SQL selection in the final beam. We perform an ablation study supplemented by a Shapley analysis of these different components integrated with two backbone architectures, SmBoP and RASAT. We find that simply combining all of them does not lead to best results, but that their impact depends on their interactions with the baseline system, as well as each other.

---


### 246. [DP-Splat: Bayesian Nonparametric Complexity Control for Gaussian Splatting](https://arxiv.org/abs/2607.10912)

**<font color=#1a73e8>作者：</font>** Aqi Dong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting represents scenes as finite mixtures of anisotropic Gaussians whose number of components $K$ is set by heuristic density control or user caps. Variational Bayes Gaussian Splatting (VBGS) recast splat fitting as conjugate variational inference, but $K$ remains fixed. We replace the finite symmetric Dirichlet over mixture weights with a truncated stick-breaking Dirichlet-process prior -- and, as a theory-backed alternative, a sparse overfitted finite Dirichlet -- so that the number of occupied components adapts to the data while every update remains a closed-form coordinate-ascent step; a natural-gradient stochastic variant makes the per-step cost independent of the number of points. We give an exact monotonicity guarantee, a rigorous truncation-error bound correcting an anti-conservative large-$\alpha$ approximation in common use, and an honest account of what the fitted number of components estimates. Empirically: (i) the effective complexity $\hat{K}$ adapts to scene complexity and recovers the true $K$ within $\pm 1$ on well-separated synthetic data with regime-appropriate concentration; (ii) a deconfounded comparison shows the DP prior's contribution is complexity selection, not per-component efficiency -- converged DP fits exceed single-pass fixed-$K$ VBGS by +2.7 dB at matched budgets yet tie an equally converged fixed-$K$ baseline, and on 3D scenes DP-Splat matches or exceeds VBGS's held-out color prediction with 5.9-7.6x fewer components; (iii) the posterior-predictive color variance is well calibrated on model-matched synthetic data; and (iv) the ordering suggested by exact-posterior asymptotics reverses under mean-field coordinate ascent: the DP prior resists over-splitting while the sparse finite mixture saturates its truncation, a gap between variational practice and posterior asymptotics documented across three orders of magnitude in $N$.

---


### 247. [SoK: Federated Learning for Intrusion Detection in Vehicular Networks](https://arxiv.org/abs/2607.10914)

**<font color=#1a73e8>作者：</font>** Yahya Shahsavari, Reza Nourmohammadi, Sara Rouhani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern vehicular networks face an expanding attack surface across internal Electronic Control Units (ECUs) and external Vehicle-to-Everything (V2X) communication. Federated Learning (FL) has emerged as a decentralized paradigm to deploy Intrusion Detection Systems (IDS) without compromising data privacy. However, the vehicular FL-IDS literature suffers from fragmented methodologies and unrealistic experimental setups. This paper presents a Systematization of Knowledge (SoK) that unifies the taxonomy of vehicular attack surfaces, evaluates FL topologies, and maps adversarial threats such as poisoning and inference attacks. By auditing over 60 publications, we identify recurring pitfalls: artificial IID data splits, reliance on trivial benchmarks, weak adversarial evaluation, and omission of real-time CAN constraints. Finally, we define a forward-looking research agenda and outline minimum benchmarking requirements necessary to transition vehicular FL-IDS from optimistic simulations to secure, real-world deployment.

---


### 248. [Learning Linear Temporal Specifications from Demonstrations with Uncertainty](https://arxiv.org/abs/2607.10918)

**<font color=#1a73e8>作者：</font>** Parastou Fahim, Constantino Lagoa, Rômulo Meira-G'oes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning temporal logic specifications from system demonstrations is essential for tasks such as formal verification and controller synthesis, especially in safety-critical domains. Existing approaches typically assume demonstrations are correct or only affected by misclassification errors. In practice, however, system traces are often uncertain or incomplete due to sensor faults, measurement errors, or data loss. We present a framework for learning minimal Linear Temporal Logic (LTL) formulas from demonstrations with uncertainty. Our approach models uncertainty via Hamming distance to generate possible estimates around each observed trace, which are grouped with constraints requiring that at least one trace per group is consistent with the learned formula. Our problem is then reduced to an equivalent Pseudo-Boolean Optimization. We evaluate our method against state-of-the-art LTL learning approaches and show that it recovers specifications that more closely align with ground-truth formulas under uncertainty.

---


### 249. [Infrared Organization and Critical Cognitive Field Formation in Transformer Dynamics](https://arxiv.org/abs/2607.10923)

**<font color=#1a73e8>作者：</font>** Byung Gyu Chae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit remarkable emergent behaviors, yet the physical mechanism governing their collective dynamics remains poorly understood. Cognitive Field Theory predicts that learning reorganizes the time-scale density of states (TDOS) through the infrared accumulation of slow relaxation modes, thereby enhancing the memory self-energy, reducing the cognitive forgetting gap, and strengthening the collective susceptibility. Using publicly available Pythia language models, we extract relaxation spectra directly from Transformer layer Jacobians throughout training, network depth, and model scale, allowing the TDOS, memory self-energy, forgetting gap, memory kernel, and infrared critical exponent to be measured quantitatively. The measurements reveal progressive infrared accumulation of slow relaxation modes, producing an approximately flat infrared TDOS with \( \rho(\lambda)\sim\lambda^{-0.1} \) and scale-free memory kernels \( K(t)\sim t^{-1}. \) The memory self-energy exhibits a pronounced transient maximum during early optimization before relaxing toward a metastable near-critical regime, corresponding to the smallest cognitive forgetting gap and the largest collective susceptibility predicted by Cognitive Field Theory. These observations provide quantitative experimental evidence that Transformer dynamics are governed by infrared collective organization. The reproducibility of the same dynamical behavior across training, network depth, and model scales suggests that infrared slow-mode organization represents a universal collective principle of Transformer dynamics.

---


### 250. [The Spectral Structure of Latent Treatment Effects](https://arxiv.org/abs/2607.10926)

**<font color=#1a73e8>作者：</font>** Hamza Virk, Bijan Mazaheri, Yihren Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying heterogeneous treatment effects under unobserved confounding is central in observational causal inference. In proxy models with a discrete latent confounder, prior Synthetic Potential Outcomes (SPO) [Mazaheri-Squires-Uhler '25] recover the mixture of treatment effects through recursively constructed scalar moments. We show that this sequence is one projection of a more fundamental object. Under the same population factorization assumptions, there is an exact compressed observable operator: after projecting onto the shared proxy signal subspace, the difference of two treatment-arm quotient operators is similar to the diagonal matrix of latent treatment effects. Its eigenvalues are the latent effects; its lifted left eigenvectors, after anchor normalization, recover the target-proxy feature matrix and then the latent mixture proportions. Every scalar SPO moment is a bilinear functional of a power of this operator. The resulting estimator handles overcomplete proxy systems, replaces high-order scalar inversion with finite-dimensional spectral analysis, and admits high-probability first-order perturbation bounds for treatment effects, feature rows, and simplex-projected mixture weights.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
