# 📦 其他研究 | 2026年07月04日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-266](./part-06.md)

---

### 201. [SAMoR: Motion Modelling for Articulated Objects of Any Skeleton and Topology](https://arxiv.org/abs/2607.02148)

**<font color=#1a73e8>作者：</font>** Yuhao Zhang, Gerard Pons-Moll, Tolga Birdal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling motion for articulated objects of arbitrary skeleton topology remains difficult: existing motion generators target a fixed human skeleton, and prior adaptations either fail to share a vocabulary across rigs or discard motion detail through global pooling. Our key observation is that while joint-level motion does not correspond cleanly across species, motion of functional joint groups does: a human arm, a wolf foreleg, and a bird wing share motion structure despite differing joint counts and connectivity, a correspondence that joint names (e.g., "forearm", "wing_L1") partially expose even when topology does not. We introduce SAMoR (Skeleton-Aware Motion Representation for Articulated Objects), a cross-topology motion representation that encodes each motion segment as a small fixed number ($K=8$) of part tokens shared across arbitrary skeletons. A graph-transformer encoder consumes per-joint motion features, kinematic graph structure, and joint-name embeddings, then compresses them into part-level tokens via cross-attention pooling and residual vector quantization, yielding a discrete motion codebook shared across rigs. To keep the part queries from collapsing into redundant global representations, we introduce a topology-agnostic attention supervision loss, with joint-name dropout to reduce over-reliance on text labels. We curate a heterogeneous corpus from HumanML3D, Truebones Zoo, and animated Objaverse-XL assets, and evaluate SAMoR on held-out characters with unseen skeletons. It supports accurate reconstruction and cross-topology transfer, and enables text-conditioned generation and part-wise editing via a MaskGIT token generator. SAMoR reaches $2.75 \times 10^{-2}$ normalized MPJPE on cross-topology reconstruction, $5.8\times$ below the strongest adapted variable-$J$ tokenizer baseline, while remaining competitive with fixed-skeleton specialists on HumanML3D.

---


### 202. [Patient-Specific Articulated Digital Twins from a Single Full-Body CT Scan](https://arxiv.org/abs/2607.02156)

**<font color=#1a73e8>作者：</font>** Han Zhang, Boyang Zhao, Mathias Unberath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patient-specific anatomical models provide individualized context for surgical planning, image-guided intervention, and algorithm development. However, most CT-derived models are static: they preserve the body configuration captured at scan time, but cannot represent how the same anatomy would appear after patient repositioning. This limitation is especially important for radiographic imaging, where appearance depends jointly on imaging geometry and patient pose. We present a proof-of-concept for constructing a patient-specific articulated digital twin from a single full-body CT scan. The method fits a parametric human body model (SMPL) to obtain a patient-aligned kinematic scaffold, binds segmented bones and organs to an anatomy-aware rig, and retargets body-pose changes while preserving skeletal geometry. On three full-body CT subjects, the fitted scaffold achieved 15.8 $\pm$ 4.0 mm chamfer distance and 95.9 $\pm$ 1.8% skeletal enclosure. Recomposition at the acquisition pose preserved major radiographic structure, with overall SSIM of 0.872 $\pm$ 0.016 and PSNR of 18.5 $\pm$ 1.4 dB across paired DRRs. Across unseen target poses, the resulting twins enabled articulation while maintaining high skeletal enclosure (94.4 $\pm$ 0.4%). As a feasibility demonstration, we render the articulated twin as pose-dependent DRRs. These results suggest the feasibility of extending static, view-controllable CT simulation toward pose-controllable anatomical twins for future synthetic imaging and positioning studies.

---


### 203. [Efficient PEFT Methods with Adaptive Checkpointing for Vision Models and VLMs on Resource Constrained Consumer-GPUs](https://arxiv.org/abs/2607.02158)

**<font color=#1a73e8>作者：</font>** Altay Toktassyn, Jurn-Gyu Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern pretrained vision models achieve strong accuracy but demand substantial GPU memory for fine-tuning, making edge deployment impractical. This paper compares five parameter-efficient fine-tuning (PEFT) methods (Full FT, LoRA, AdaLoRA, QLoRA, BitFit) on Transformers- (ViT-Small, TinyViT) and Mamba-based vision backbones (Vim-Small, MambaVision-T) under an on-device VRAM budget (e.g., 2 GB), together with three gradient-checkpointing strategies (none, static, and a proposed memory-budget-aware adaptive algorithm); and we evaluate three families of foundation-model baselines: zero-shot contrastive vision language models (OpenCLIP, SigLIP), self-supervised vision backbones with lightweight evaluation protocols (DINOv2), and autoregressive VLMs for prompt-based classification (PaliGemma, MobileVLM, SmolVLM). Experiments on CIFAR-100 and DTD report accuracy, training time, energy, and the NetScore family of multi-objective metrics, which we extend with two deployment-aware variants. QLoRA and BitFit cut energy 20-30% at a 1-2% accuracy cost; the adaptive algorithm reduces peak memory 43-79% with 9-30% energy overhead. DINOv2 surpasses fine-tuned models on CIFAR-100 (0.917 vs. 0.897) at a fraction of the energy, while small autoregressive VLMs remain uncompetitive.

---


### 204. [Visual Analytics of Neighborhood Attribute Profiles for Exploring Structural Equivalence](https://arxiv.org/abs/2607.02163)

**<font color=#1a73e8>作者：</font>** Kohei Arimoto, Masahiko Itoh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Exploring similar nodes in attributed networks represents a key challenge in data mining. While recent representation learning methods embed networks into low-dimensional vectors, they often implicitly assume a uniform and continuous feature space. This paper proposes a visual analytics approach using dimensionality reduction to help clarify the true topological structure of high-dimensional feature spaces formed by nodes' neighborhood attribute profiles. Analyzing inter-firm transaction networks indicates that structural roles can form complex, non-linear manifolds with density biases. Comparing this feature space with industry classifications suggested: (1) supply chain hierarchies transition continuously; (2) categories treated identically under general semantics can be clearly separated by actual transaction networks; and (3) a single industry label may fragment into multiple regions. These findings suggest potential limitations in assuming identical semantics imply similar structural roles and highlight the possible need for new similarity metrics aligned with manifold topology.

---


### 205. [Dynamic Neural Graph Encoding of Inference Processes in Deep Weight Space](https://arxiv.org/abs/2607.02166)

**<font color=#1a73e8>作者：</font>** Di Wu, Huan Liu, Zhixiang Chi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid advancements in using neural networks as implicit data representations have attracted significant interest in developing machine learning methods that analyze and process the weight spaces of other neural networks. However, efficiently handling these highdimensional weight spaces remains challenging. Existing methods often overlook the sequential nature of layer-by-layer processing in neural network inference. In this work, we propose a novel approach using dynamic graphs to represent neural network parameters, capturing the temporal dynamics of inference. Our Dynamic Neural Graph Encoder (DNG-Encoder) processes these graphs, preserving the sequential nature of neural processing. Additionally, we also leverage DNG-Encoder to develop INR2JLS (Implicit Neural Representation to Joint Latent Space) for facilitate downstream applications, such as classifying Implicit Neural Representations (INRs). Our approach demonstrates significant improvements across multiple tasks, surpassing the state-of-the-art INR classification accuracy by approximately 10% on the CIFAR-100-INR.

---


### 206. [Synthetic Contact with AI Reduces Cross-Partisan Animosity](https://arxiv.org/abs/2607.02181)

**<font color=#1a73e8>作者：</font>** Benjamin Lira, Noah Castelo, Stefano Puntoni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Americans' warmth toward members of the opposing political party has fallen sharply over the past three decades -- yet meaningful cross-partisan contact remains scarce, in part because people actively avoid it. Across five preregistered studies (total N = 3,960 U.S. partisans), we test whether brief conversations with AI chatbots representing the political outgroup can substitute for the contact people shun. Synthetic contact first lowers the barrier to entry: partisans would endure almost twice as long contemplating their own mortality to avoid a human outgroup partner as an AI one. These conversations then correct the misperceptions that fuel division. At baseline, Democrats placed Republicans more than a standard deviation past their actual position on environmental consumption attitudes -- enough to flip the average Republican from supportive to opposed -- and a single ten-minute conversation with an outgroup chatbot corrected those beliefs and warmed affect in a within-person study of both parties. A three-arm experiment ruled out pure engagement and sociality as drivers. Synthetic contact also moved behavior, in a sample of both parties and on a more affectively charged issue: participants who spoke with an outgroup bot about immigration were six percentage points more likely than controls to choose to have a real conversation with a partisan from the other side. A final study tested whether these gains last: the warmth effect replicated immediately in a new sample; most of it faded within a week, with a small residual concentrated among the most extreme partisans. Analyzing conversation content showed that information, more than friendliness, distinguishes outgroup bots from control chatbots. Together, these findings establish synthetic contact as a scalable, behaviorally consequential, and -- unlike face-to-face contact -- widely acceptable form of cross-partisan engagement.

---


### 207. [RadiomicNet: A Hybrid Radiomics-Guided Lightweight Architecture for Interpretable Medical Image Segmentation](https://arxiv.org/abs/2607.02185)

**<font color=#1a73e8>作者：</font>** Mohammad Amanour Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has achieved remarkable performance in medical image segmentation, yet it suffers from critical limitations: mathematical intractability, substantial parameter requirements, and lack of clinical interpretability. We propose RadiomicNet, a novel two-stream hybrid architecture that enhances standard deep learning by integrating handcrafted radiomics features directly into the segmentation learning process. The key contribution is the Radiomics Attention Gate (RAG), which leverages Gray-Level Co-occurrence Matrix (GLCM) and Local Binary Pattern (LBP) features to modulate skip-connection attention in a lightweight MobileNetV2-based encoder-decoder, providing ante-hoc interpretability without post-hoc approximations. A novel Radiomics Consistency Loss further enforces alignment between texture complexity and prediction uncertainty, reducing Expected Calibration Error (ECE) from 0.142 to 0.118. RadiomicNet achieves a Dice Similarity Coefficient (DSC) of 0.763 +/- 0.231 on the Breast Ultrasound Images (BUSI) dataset and 0.854 +/- 0.112 on Kvasir-SEG, outperforming U-KAN by 1.2% and 1.8%, respectively (p < 0.05, Wilcoxon signed-rank test), with only 3.27M parameters, 9.5x fewer than standard U-Net and 4.3x fewer than U-KAN. Gradient-based feature importance analysis reveals that GLCM dissimilarity (15.24%), GLCM energy (14.56%), and LBP entropy (11.49%) are the dominant radiomics cues, providing clinically meaningful explanations for segmentation decisions. The proposed approach demonstrates that compact, interpretable models grounded in domain knowledge can deliver state-of-the-art segmentation performance with substantially reduced computational overhead.

---


### 208. [Privacy-Preserving and Verifiable Approximate Distributed Coded Computing](https://arxiv.org/abs/2607.02187)

**<font color=#1a73e8>作者：</font>** Xavier Martínez-Luaña, Alba Gude-Santos, Manuel Fernández-Veiga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed machine learning enables collaborative model training without centralizing data, but it also exposes learning processes to privacy leakage and malicious manipulation. Existing defenses typically address these threats in isolation and are often tailored to specific learning paradigms or model architectures, limiting their applicability in realistic deployments. In particular, federated learning and decentralized learning exhibit distinct adversarial surfaces that are rarely addressed within a unified framework. In this paper, we present a model-agnostic framework for adversary-resistant distributed learning that jointly addresses privacy preservation and malicious behavior across both federated and decentralized settings. Our approach combines paradigm-specific defense mechanisms with GPBACC, a privacy-enhancing coded computing technique applicable to arbitrary machine learning models. For federated learning, we integrate robust aggregation strategies to mitigate the impact of malicious participants, while for decentralized learning we employ approximate decode-and-compare and group testing techniques to enable lightweight verification and adversary isolation without relying on a trusted aggregator. Crucially, we evaluate the proposed framework through an explicit, attack-driven analysis. We implement representative privacy attacks and malicious behaviors, and empirically demonstrate that the combination of GPBACC with robust aggregation and verification mechanisms significantly reduces privacy leakage and improves resilience against active adversaries. These results suggest that privacy-enhancing coded computing, when combined with appropriate adversary-resistance strategies, provides a practical and deployable foundation for secure distributed machine learning.

---


### 209. [An Optimisation Framework for the Well-Conditioned Training of Physics-Informed Neural Networks](https://arxiv.org/abs/2607.02194)

**<font color=#1a73e8>作者：</font>** Joseph Webb, Sadok Jerad, Coralia Cartis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have emerged as a promising route to solve partial differential equations, yet they have struggled to reach the precision of classical solvers. The obstacle is increasingly understood to be one of optimisation, owing to the severely ill-conditioned loss landscape. We present $\textbf{DSGNAR}$: Doubly-Sketched Gauss-Newton with Adaptive Ratio, a scalable second-order optimisation framework that confronts this ill-conditioning and, in doing so, obtains unprecedented accuracy and speed. $\textbf{DSGNAR}$ couples a doubly-sketched Gauss-Newton model with a novel strategy that carefully controls both regularisation and step length. Across a suite of problems spanning nonlinear, chaotic, multi-scale, high-dimensional, and Navier-Stokes, the framework greatly improves on the state of the art: able to attain relative $\ell_2$ errors as low as $3\times10^{-16}$ in double precision, improve contemporary results by five orders of magnitude on the canonical Burgers' equation, and as much as eight orders on a high-dimensional Poisson problem, while remaining markedly faster. We further show that, in single precision, solutions at the limit of round-off error can be obtained very quickly: Burgers' equation to $\ell_2^{\text{rel}} = 4.75 \times 10^{-7}$ in under ten seconds. The framework is also robust to the choice of architecture, arithmetic precision, and initial hyperparameters.
The code is available at this https URL

---


### 210. [Online Resource Allocation with Continuous Random Consumption: Regret under Degeneracy](https://arxiv.org/abs/2607.02196)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online resource allocation when both rewards and consumption sizes may be continuously distributed. Requests arrive sequentially and must be accepted or rejected irrevocably under fixed resource capacities. Each request belongs to one of finitely many observable types; conditional on an observable request type, both the reward and the scalar size are random, and the realized size scales a fixed type-specific resource-consumption vector. The model allows the deterministic fluid relaxation to be degenerate.
We show that additive regret is governed by the size-weighted mass of requests whose value-to-size ratios lie near the active acceptance cutoffs. We formalize this quantity through an active weighted-mass exponent p. When p > 1, this cutoff mass is thin, and the problem is genuinely hard: every online policy must incur regret of order at least $T^{1/2 - 1/(2p)}$, and this holds for every p > 1. A sample-path marginal policy matches this lower bound up to polylogarithmic factors; and when p = 1, so that the mass grows linearly near the cutoff, it attains $O((\log T)^2)$ regret. For example, if the size and the value-to-size ratio are independent and uniformly distributed, then p = 1; if instead the size and the reward are independent and uniformly distributed, then p = 2. Thus the policy achieves $o(\sqrt{T})$ regret throughout this regularity class without any fluid non-degeneracy assumption, allowing both primal degeneracy and dual non-uniqueness.

---


### 211. [What Types of Human-AI Teams Exist?](https://arxiv.org/abs/2607.02198)

**<font color=#1a73e8>作者：</font>** Nathan Hughes, Ibrahim Habli  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI teaming has received increasing attention in the literature. However, the range of studies conducted in multiple domains make it difficult to understand what types of teams are being studied, and in what ways are they similar/different from one another. In this study, we analyse 53 papers on human-AI teams and categorise them into five main clusters based on psychological taxonomies of teaming; AI Assistant, Ad-hoc Dependency, Ad-hoc Forced Dependency, Paired Equanimity, and Group Equanimity. Each cluster represents a unique combination of holistic team-level characteristics, indicating there are multiple disparate team types studied under the same definition. In turn, this raises the question of whether insights are truly transferable between papers. We conclude with guidance on how to identify the types of human-AI teams studied, a checklist for reporting a human-AI team in research work, and ways in which the field can be further synthesised.

---


### 212. [Self-explainable Operator Learning for Discovering Spatial Patterns in Functional Data](https://arxiv.org/abs/2607.02203)

**<font color=#1a73e8>作者：</font>** Mojgan Alishiri, Amirhossein Arzani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operator learning has emerged as a powerful tool for modeling complex physical systems in functional spaces. However, their neural network-based architectures make them opaque models, obscuring the reasoning behind their predictions. In this work, we introduce a self-explainable operator learning framework that overcomes this challenge by reformulating operator learning as a linear combination of generalized functional linear models expressed through integral equations. Exploiting the additive decomposability of these integral equations, we divide the input domain into subdomains and compute localized integrals to evaluate the contribution of each region to the final prediction. This decomposition enables direct interpretability where the model explains both inputs and outputs by linking specific input regions to corresponding output patterns, thereby revealing which spatial features drive predictions. We demonstrate the framework on function-to-scalar and function-to-function mappings in fluid flow problems involving blood flow and unsteady aerodynamics. The results show that the operator most often prioritizes regions with strong feature gradients, providing physically meaningful insight into the model's decision-making process. Comparisons with established post-hoc explainability methods demonstrate qualitative agreement while highlighting the key advantage of the proposed approach: explainability is embedded directly within the operator structure itself and does not require an external tool. Therefore, our framework provides a mathematically transparent and physically interpretable approach to uncover relationships within data, fostering trust in machine learning for scientific applications by enabling more informed data-driven analysis of physical systems.

---


### 213. [MedSaab-US: A Backpropagation-Free Multi-Scale Wavelet-Saab Framework for Thyroid Nodule Segmentation in Ultrasound Images](https://arxiv.org/abs/2607.02209)

**<font color=#1a73e8>作者：</font>** Mohammad Amanour Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning (DL) methods dominate thyroid nodule segmentation in ultrasound (US) images, achieving high Dice scores but at the cost of millions of parameters, GPU-dependent training via backpropagation, and limited mathematical tractability. These limitations impede deployment in resource-constrained environments. In this paper, we propose MedSaab-US, a backpropagation-free segmentation framework grounded in the Green Learning paradigm. MedSaab-US extracts multi-scale spatial-frequency features by combining multi-level Discrete Wavelet Transform (DWT) with multi-scale channel-wise Saab (Subspace Approximation with Adjusted Bias) transforms at patch sizes of 5 x 5, 11 x 11, and 21 x 21 pixels. Label-Assisted Greedy (LAG) feature selection retains the most discriminative features, which are fed to an XGBoost classifier for pixel-wise prediction. The Saab transform parameters are determined analytically from data statistics, while XGBoost employs iterative greedy tree construction without requiring backpropagation. Evaluated on the TN3K dataset (2,879 training and 614 test images), MedSaab-US achieves a mean Dice coefficient of 0.4784 +/- 0.2190, precision of 0.5768, and recall of 0.5604, with a model footprint under 500K parameters and CPU-only inference in approximately 0.3 seconds per image. We present this result as an exploratory non-DL baseline for thyroid ultrasound segmentation and analyze the specific challenges posed by isoechoic nodules. An ablation study further quantifies the contribution of each pipeline component, including separate evaluations of LAG feature selection and training-set size.

---


### 214. [Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks](https://arxiv.org/abs/2607.02210)

**<font color=#1a73e8>作者：</font>** Ravi Kant Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evolution toward fully autonomous telecommunications networks (Autonomous Network Levels 4-5) requires AI/ML agents to make real-time network decisions without human intervention. However, no standardized runtime mechanism exists to intercept and validate individual inference outputs before they trigger live network state changes, creating risks of erroneous autonomous decisions. This paper proposes the Guard Rail Validation (GRV) framework, a standardizable runtime architecture for intercepting and validating AI-driven decisions before execution. The framework evaluates decisions across multiple weighted dimensions -- including action scope, action type, service criticality, agent autonomy level, reversibility, and temporal behavioural patterns -- to determine a criticality level. Based on this level, graduated validation mechanisms are applied: execute-with-logging, bounds checking, independent agent validation, or multi-agent consensus. The framework additionally provides cross-agent conflict detection with criticality-weighted priority resolution and runtime conformance logging for regulatory compliance (e.g., EU AI Act Article 14). We present the architecture, algorithmic procedures, O-RAN deployment model, and evaluate threat coverage against known AI/ML attacks in telecommunications.

---


### 215. [Efficient Waste Sorting for Circular Economy: A Confidence-guided comparison between One-Vs-All and One-Vs-Rest Classification Strategies with Human-in-the-Loop for Automated Waste Sorting](https://arxiv.org/abs/2607.02230)

**<font color=#1a73e8>作者：</font>** Mohammed Fahad Ali, Dominique Briechle, Marit Briechle-Mathiszig 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The complexity of waste disposal regulations across European countries poses significant challenges for the residents and hinders the transition to a Circular Economy. In Germany, the proper sorting and disposal of household waste remains challenging across municipalities. Consequently, substantially reducing incorrectly disposed waste is vital for improving waste management and advancing the Circular Economy. AI-based waste sorting solutions can support residents through user-friendly tools, such as mobile applications, that guide proper waste disposal. To be effective in supporting the Circular Economy, however, these solutions must be configurable to reflect the specific waste sorting scheme of individual municipalities in Germany. In the scope of this work, an evaluation and analysis are performed of two prominent classification strategies: OvA and OvR. The research uses a dataset constructed in alignment with the waste categories and sorting scheme of the city of Goslar in Germany. Moreover, this work aims to extend beyond the overall performance by examining the behavior of OvA and OvR classification strategies in identifying samples likely to be misclassified. These classification strategies are compared by applying varying confidence thresholds to identify uncertain samples for subsequent human review. This evaluation aims to balance the number of misclassifications against the human effort required for data annotation.

---


### 216. [Purified OPSD: On-Policy Self-Distillation Without Losing How to Think](https://arxiv.org/abs/2607.02234)

**<font color=#1a73e8>作者：</font>** Zhanming Shen, Jintao Tong, Shaotian Yan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has emerged as a promising paradigm for improving LLM reasoning, where a privileged teacher with access to reference solutions provides token-level supervision on the student's own generated trajectories. However, we find that OPSD consistently fails on long chain-of-thought (long-CoT) reasoning models, yielding at best marginal gains while destabilizing the reflective reasoning capability these models depend on. Through a novel decomposition of the teacher's supervision signal, we identify the root cause: the teacher's supervision is dominated by a reference-induced component that drives rote memorization of reference-specific shortcuts, while the question-conditioned, inference-transferable component is ignored or actively opposed. Based on this diagnosis, we propose a two-step solution. First, we construct a reference-only teacher (the same model conditioned on the reference without the question) to isolate the non-transferable component of the supervision signal; the residual after subtracting this component captures the question-conditioned, inference-transferable correction. Second, we use pointwise mutual information (PMI) as the mechanism to transform this residual into a well-formed PMI target distribution that the student can directly distill from, filtering out the reference-induced shortcut. Experiments on four long-CoT models across two datasets demonstrate consistent improvements over both the base model and standard OPSD, while preserving the models' natural epistemic behavior throughout training.

---


### 217. [When Token Compression Breaks: Structural Pruning vs. Token Reduction for Robust ViT Segmentation under High Compression](https://arxiv.org/abs/2607.02237)

**<font color=#1a73e8>作者：</font>** Tien-Phat Nguyen, Ngai-Man Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are strong backbones for semantic segmentation, but their computational cost limits deployment. Recent token compression methods for efficient transformer-based segmentation reduce this cost by decreasing the number of tokens. However, existing evaluations primarily focus on low-to-moderate compression, leaving their behavior under aggressive compression and corrupted inputs unclear. Meanwhile, structural pruning provides an orthogonal route to efficiency by removing redundant components in the ViT architecture, but is rarely compared to token compression under a unified protocol. To bridge this gap, we benchmark representative token compression and structural pruning methods for ViT-based semantic segmentation under matched FLOPs on ADE20K and Cityscapes, together with their common-corruption variants ADE20K-C and Cityscapes-C. Our results reveal a consistent trend on both clean and corrupted inputs: token compression is highly effective at mild reductions but degrades sharply when compression becomes severe, consistent with substantial information loss from overly aggressive token reduction. In contrast, structural pruning exhibits a smoother degradation curve and is more stable at high compression. Motivated by these findings, we study a prune-then-merge pipeline that applies moderate token compression on top of a moderately pruned backbone. At comparable FLOPs, this combined strategy consistently achieves a better accuracy-robustness trade-off at high compression, offering a practical recipe for deployment-oriented ViT segmentation. Code is available at this https URL.

---


### 218. [Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support](https://arxiv.org/abs/2607.02245)

**<font color=#1a73e8>作者：</font>** Seren Yenikent, Jack Vinijtrongjit, Katherine Ng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental health disorders affect nearly one billion people globally, yet 75% of individuals in low- and middle-income countries receive no treatment due to workforce shortages, cost barriers, and stigma. Current AI-powered wellness solutions predominantly rely on single-mode conversational interfaces that suffer high abandonment rates and fail to provide measurable, immediate relief calibrated to users' dynamic emotional states. This paper presents Copewell, a novel multi-agent swarm system designed to expand access to mental wellness support through human-centered AI principles. Our architecture introduces three technical innovations: (1) a multi-source assessment framework integrating self-reported, physiological, and contextual data to mitigate algorithmic bias; (2) valence-arousal emotion mapping using Russell's Circumplex Model of Affect to route users to specialized AI agents; and (3) dual-mode intervention delivery combining conversational support with evidence-based sensory wellness protocols. We examine the sociotechnical design considerations underlying Copewell's development, including a privacy-first architecture, embedded ethical oversight through a dedicated Ethics Supervisor agent, and participatory design informed by mental health practitioners. Early practitioner engagement and beta deployment inform design decisions and identify directions for future empirical evaluation. This work contributes to responsible AI discourse by demonstrating how technical architecture can operationalize equity and safety principles from inception.

---


### 219. [ArcAD: Anomaly-Rectified Calibration for Cold-Start Supervised Anomaly Detection](https://arxiv.org/abs/2607.02252)

**<font color=#1a73e8>作者：</font>** Ningning Han, Lei Fan, Jia Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The deployment of Industrial Anomaly Detection (IAD) in real-world manufacturing frequently encounters a challenging cold-start bottleneck, in which limited normal samples fail to represent the full normal distribution and only a few anomalies are available. Under such a regime, existing methods struggle to form compact normal boundaries and fail to effectively exploit supervised signals from rare defects. To address this challenge, we propose Anomaly-Rectified Cold-start AD (ArcAD), a plug-and-play calibration framework for reconstruction-based IAD baselines. ArcAD follows a push-pull learning paradigm to construct a compact and discriminative normal boundary under data scarcity. On the one hand, ArcAD projects limited normal samples onto a hypersphere and pulls them into multiple compact clusters to maximize coverage of the normal manifold. On the other hand, it synthesizes pseudo-anomalies on the hypersphere and leverages real anomalies to push the boundary inward and sharpen anomaly discrimination. Extensive experiments on MVTec-AD, VisA, Real-IAD, and MANTA demonstrate that ArcAD significantly outperforms state-of-the-art supervised and unsupervised methods in both single-class and multi-class settings under cold-start conditions. Code is available at: this https URL.

---


### 220. [CheckRLM: Effective Knowledge-Thought Coherence Checking in Retrieval-Augmented Reasoning](https://arxiv.org/abs/2607.02262)

**<font color=#1a73e8>作者：</font>** Dingling Xu, Ruobing Wang, Qingfei Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning Language Models (RLMs) have significantly improved performance on complex tasks by extending the reasoning chain. However, these chains are prone to containing factual errors, particularly in knowledge-intensive tasks. To address this issue, we propose CheckRLM, a framework that improves the reliability of the reasoning process through Retrieval-Augmented Generation (RAG) by timely checking and correcting factual errors. Specifically, CheckRLM extracts factual claims from the reasoning chain to identify and localize subtle knowledge inconsistencies during inference. Upon detection of errors, a refinement mechanism performs minimal-cost yet precise corrections by leveraging external knowledge, ensuring coherence between the reasoning chain and correct knowledge. Extensive experiments demonstrate that CheckRLM substantially outperforms existing baselines, exhibiting a strong capability to mitigate error accumulation in long-horizon reasoning with lower costs. The code and data are available at this https URL.

---


### 221. [AGVBench: A Reliability-Oriented Benchmark of Data Augmentation for Vein Recognition](https://arxiv.org/abs/2607.02271)

**<font color=#1a73e8>作者：</font>** Haiyang Li, Yuming Fu, Qun Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vein recognition is a secure biometric technology often constrained by limited annotated data and imaging variations. While data augmentation mitigates this, strategies designed for natural images may disrupt the fine-grained topology and textures essential for identity discrimination. We present AGVBench, which evaluates 30 representative augmentation strategies on five public palm- and finger-vein datasets with seven backbone architectures, covering classic CNNs, vision transformers, and vein-specific recognition models. Our results show that multi-image mixing methods (e.g., MixUp, PuzzleMix, StarMixup) generally provide the strongest recognition performance. However, they are often poorly calibrated and vulnerable to adversarial perturbations, revealing a clear inconsistency between clean accuracy and adversarial security. We also find that severe geometric transformations frequently degrade recognition, which is potentially due to feature misalignment or spatial cropping, and that augmentation effectiveness varies across palm and finger vein datasets. These findings prove that accuracy-centric evaluation is insufficient for biometric augmentation. AGVBench provides standardized protocols to support reproducible research and guide the design of reliable, secure, and robust vein recognition systems. Our codebase is available at this https URL.

---


### 222. [FlowCIR: Semantic Transport via Flow Matching for Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2607.02284)

**<font color=#1a73e8>作者：</font>** Zhenqi He, Ziqi Jiang, Yuanpei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image by editing a reference image with a natural-language instruction, without relying on domain-specific annotated triplets. Most existing ZS-CIR methods rely on textual inversion to translate the reference image into pseudo-text tokens and then compose them with the instruction via simple concatenation in the text space, which can be lossy and brittle for fine-grained semantics. In this work, we propose a new paradigm, namely FlowCIR, that casts ZS-CIR as conditional semantic transport between reference and target embeddings. Leveraging \emph{conditional flow matching}, our model learns a lightweight transport field that maps the instruction representation toward a target-aligned query embedding conditioned on the reference image. Since FlowCIR operates on pre-extracted VLM embeddings and trains only a small transport module without updating the image or text encoder, it offers a computationally efficient training protocol compared with prior textual-inversion-based approaches. The resulting framework is training-efficient, requiring roughly $10\times$ fewer training resources than prior textual-inversion-based approaches. We further identify negation and removal as a major failure mode of VLM-based composition. To address this, we propose an inference-only Multi-Negative Steering strategy that steers a negation-containing relative instruction away from its negated semantics, mitigating the limited negation handling of VLMs and improving robustness on negation-heavy queries. Extensive experiments on standard CIR benchmarks demonstrate that FlowCIR achieves strong and competitive performance compared with recent ZS-CIR methods.

---


### 223. [Generalization in offline RL: The structure is more important than the amount of pessimism](https://arxiv.org/abs/2607.02288)

**<font color=#1a73e8>作者：</font>** Max Weltevrede, Matthijs T.J. Spaan, Wendelin Böhmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While pessimism counteracts overestimation bias in offline reinforcement learning (RL), being overly conservative has been associated with hindering certain forms of generalization. However, in this paper we demonstrate that being overly pessimistic does not inherently prevent optimal generalization in contextual MDPs (CMDPs). Instead, we argue successful generalization depends not on the amount of pessimism, but whether the pessimistic structure respects the underlying symmetries of the optimal solution. We prove that a mildly pessimistic, non-symmetric value function can generalize worse than an overly pessimistic, symmetric one. In offline RL, the structure of the pessimism is determined by the structure of the dataset coverage. As such, enforcing a symmetric value function can be non-trivial, and might require techniques such as data augmentation (DA). Inspired by our theoretical results, we argue that DA can best be applied through a consistency loss during policy extraction, rather than the common practice of (regular) offline training on an augmented dataset. This is empirically validated using IQL and CQL on a rotationally symmetric reacher environment.

---


### 224. [DisciplineGen-1M: A Large-Scale Dataset for Multidisciplinary Visual Generation and Editing](https://arxiv.org/abs/2607.02290)

**<font color=#1a73e8>作者：</font>** Zhaokai Wang, Mingxin Liu, Zirun Zhu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image generation and editing models can produce visually appealing natural images, yet they remain unreliable when the target image is a knowledge-intensive diagram whose correctness depends on disciplinary concepts, symbolic structure, and precise spatial relations. We introduce DisciplineGen-1M, a million-scale multidisciplinary dataset that supports text-to-image generation and image editing. It contains 1.2M samples spanning mathematics, physics, chemistry, biology, geography, computer science, economics, history, music, and sports. To construct the dataset, we design a scalable framework that combines vector-graphics rendering, OCR-based editing, curated programmatic synthesis, and large-scale text-to-image filtering. These pipelines produce captions, editing instructions, structured annotations, and paired images with controllable semantic differences. Building on DisciplineGen-1M, we further introduce a discipline-informed reasoning-generation model for both text-to-image generation and image editing. Experiments on discipline-related benchmarks, GenExam and GRADE, show substantial improvements over open-source baselines, while evaluations on general reasoning-informed benchmarks, WISE and RISE, further indicate broader transfer. The results suggest that large-scale structured academic visual data is a key ingredient for moving image generation from aesthetic plausibility toward verifiable knowledge-grounded visual creation. We will publicly release our dataset, model, and source code of the data curation pipeline to ensure reproducibility and benefit future research.

---


### 225. [Optimizing Visual Generative Models via Distribution-wise Rewards](https://arxiv.org/abs/2607.02291)

**<font color=#1a73e8>作者：</font>** Ruihang Li, Mengde Xu, Shuyang Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional reinforcement learning strategies for visual generation typically employ sample-wise reward functions, yet this practice frequently results in reward hacking that degrades image diversity and introduces visual anomalies. To address these limitations, we present a novel framework that finetunes generative models using distribution-wise rewards, ensuring better alignment with real-world data distributions. Unlike rewards that evaluate samples individually, distribution-wise reward accounts for the data distribution of the samples, mitigating the mode collapse problem that occurs when all samples optimize towards the same direction independently. To overcome the prohibitive computational cost of estimating these rewards, we introduce a subset-replace strategy that efficiently provides reward signals by updating only a small subset of a generated reference set. Additionally, we apply RL to optimize post-hoc model merging coefficients, potentially mitigating the train-inference inconsistency caused by introducing stochastic differential equation (SDE) in regular RL practices. Extensive experiments show our approach significantly improves FID-50K across various base models, from 8.30 to 5.77 for SiT and from 3.74 to 3.52 for EDM2. Qualitative evaluation also confirms that our method enhances perceptual quality while preserving sample diversity.

---


### 226. [One More Time: Revisiting Neural Quantum States from a Reinforcement Learning Perspective](https://arxiv.org/abs/2607.02292)

**<font color=#1a73e8>作者：</font>** Juan Agustín Duque, Sergio García Heredia, Vinicius Hernandes 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural quantum states (NQS) provide a flexible and scalable framework for approximating quantum many-body wavefunctions. Among NQS parameterizations, autoregressive models are especially attractive because they enable exact, independent sampling from the Born distribution, avoiding the autocorrelation and mixing issues of Markov chain methods. Yet their optimization remains comparatively underexplored: Adam is a scalable method but ignores function space geometry, while stochastic reconfiguration is principled but costly and numerically fragile in large models. To address this gap, we show that variational energy minimization can be viewed as an advantage policy-gradient problem over the Born distribution, motivating trust-region optimization for NQS training. We introduce Proximal Wavefunction Optimization (PWO), a principled trust-region algorithm that clips probability-ratio changes in the amplitude channel and phase increments in the phase channel. PWO avoids explicit matrix inversion, reuses samples across multiple updates, and combines the scalability of first-order optimization with theoretical guarantees. Across Ising and frustrated $J_1$-$J_2$ one- and two-dimensional spin systems, PWO improves stability and wall-clock convergence over Adam, minSR, and SPRING. Finally, we fine-tune a $1.5$B-parameter RWKV-7 model, demonstrating NQS optimization at a scale over three orders of magnitude beyond prior work.

---


### 227. [Dual-Selective Network for Domain-Incremental Change Detection](https://arxiv.org/abs/2607.02299)

**<font color=#1a73e8>作者：</font>** Yuzhi He, Junxi Huang, Haorui Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain-incremental change detection (DICD) continuously adapts models to new geographic domains while preserving prior knowledge. However, a structural mismatch exists: the label space remains fixed while domain characteristics vary drastically. Consequently, incremental models struggle to maintain stable spatial change representations across domains. Existing strategies, such as replay-based or regularization-based methods, often fail to scale to long domain sequences, leading to knowledge degradation or increased computational cost. We propose Dual-Selective Incremental Network (DSINet), a unified framework built on visual state space models. DSINet leverages Mamba's input-dependent selective mechanism through a selective spatial state unit (S3U). This unit preserves stable spatial change structures while filtering domain-specific variations during feature propagation. As a result, spatial representations remain stable across domains, preventing the accumulation of feature confusion over incremental steps. Additionally, we employ a concentration-balanced distillation (CBD) strategy to stabilize knowledge transfer across domains. It balances hardness and confidence concentration effects during incremental updates. This ensures reliable probability mass allocation and prevents over-smoothing or mode collapse during distillation. Together, these mechanisms maintain stable learning dynamics throughout incremental stages. Experimental results demonstrate that DSINet mitigates knowledge degradation across long domain sequences while maintaining the linear computational efficiency of state space models.

---


### 228. [InvSplat: Inverse Feed-Forward Scene Splatting](https://arxiv.org/abs/2607.02301)

**<font color=#1a73e8>作者：</font>** Polina Karpikova, Wenjing Bian, Haofei Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse rendering aims to recover both 3D geometry and physically meaningful material properties from images, enabling applications such as relighting and novel view synthesis. Optimization-based methods achieve high fidelity but require costly per-scene fitting, while image-space learning-based approaches often suffer from multi-view inconsistencies and lack an explicit 3D representation for stable novel view rendering. We present a feed-forward multi-view reconstruction framework for inverse rendering that directly predicts a structured 3D Gaussian representation with intrinsic material attributes. Each Gaussian primitive is parameterized by mean, normal, opacity, rotation, scale, albedo, metallic, and roughness, enabling a disentangled and physically grounded scene representation. Our model integrates priors from a material estimation network with a multi-view 3D reconstruction backbone, allowing joint prediction of geometry and reflectance parameters in a single forward pass. Experiments on synthetic and real-world datasets demonstrate improved multi-view consistency compared to 2D baselines, accurate material recovery, and stable novel view rendering. Our representation further supports physically-based relighting and more faithful modeling of view-dependent effects compared to existing RGB-based feed-forward reconstruction methods. Our project webpage is: $\href{this https URL}{\text{this https URL}}$.

---


### 229. [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](https://arxiv.org/abs/2607.02303)

**<font color=#1a73e8>作者：</font>** Wanyun Cui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Linear-attention and state-space language models compress the prefix into a fixed-size recurrent state, yielding O(1) memory at the cost of a lossy exact memory: when many key--value associations compete, earlier facts are overwritten and needle recall degrades. Inspired by Complementary Learning Systems, we give linear attention a hippocampal complement. HOLA (Hippocampal Linear Attention) keeps the usual delta-rule state as a compressive memory and adds a bounded exact KV cache, forming a semiparametric test-time memory: the state models linearly compressible structure, while the cache stores associations that should not be forced through that state. The cache writes without a learned eviction module, keeping tokens with large beta * ||e||, the prediction residual actually committed to the state; a decoupled RMSNorm-gamma cache read then turns these exact KV pairs into sharp retrieval rather than soft averaging. At 340M parameters trained on 15B SlimPajama tokens, HOLA lowers Wikitext perplexity from 27.32 to 22.92 (-16.1%), below a full-attention Transformer++ (26.88), and improves LAMBADA perplexity from 30.95 to 30.26. It also achieves the best linear in-context retrieval and remains much more robust than GDN or a matched HOLA+recency cache on RULER needle-in-a-haystack recall out to 32k tokens (16x its training length).

---


### 230. [On the Role of Directionality in Structural Generalization](https://arxiv.org/abs/2607.02307)

**<font color=#1a73e8>作者：</font>** Zichao Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Several SLOG test categories explicitly involve directional distinctions (modifier position shifts, argument extraction positions), yet AM-Parser, the previous SOTA, uses an AM algebra whose operations do not encode direction. We redesign the symbolic backend around CCG directed types (deterministic CKY + single linear decoder, 30K learnable parameters). Under the same BERT-base encoder, the system achieves 75.9$\pm$6.4% LF exact match, surpassing AM-Parser (70.8$\pm$4.3%). Per SLOG's own category groupings, gains are highly directional: the CCG system outperforms AM-Parser on all 5 position-shift categories (+29.9pp), while AM-Parser outperforms on all 6 recursive-depth categories. Replacing the encoder with DeBERTa-v3-large yields 90.7$\pm$4.9%, with the largest encoder gains in recursive-depth categories, complementary to directionality's gains. Directional representations shift the bottleneck from the symbolic layer (AM-Parser's 0% category ceiling) to the neural layer, which improves with encoder upgrades.

---


### 231. [NEvo: Neural-Guided Evolutionary Video Synthesis for Dynamic Visual Selectivity](https://arxiv.org/abs/2607.02317)

**<font color=#1a73e8>作者：</font>** Yingtian Tang, Sogand Salehi, Ming Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The human brain processes dynamic visual input through hierarchically organized, functionally specialized regions. While recent in silico brain encoding models can synthesize optimal stimuli to probe selectivity in different brain regions, prior work has been largely limited to static images, leaving dynamic visual processing underexplored. We introduce a novel neural-guided video synthesis framework that generates stimuli optimized for target brain regions across visual cortex. Our method performs evolutionary search over a structured prompt space, guided by a dynamic encoding model that predicts voxel-level responses to video inputs. By maximizing predicted activity for a target ROI, the framework efficiently discovers hyper-activating dynamic stimuli that consistently surpass handcrafted localizer videos. The synthesized videos recover known selectivities across ventral, dorsal, and lateral pathways, and further reveal systematic differences in sensitivity to temporal dynamics. A searchlight analysis provides new insight into the progression toward increasingly complex social-dynamic features along the lateral stream, further supported by probing with synthesized abstract, non-naturalistic stimuli. Taken together, our framework enables in silico exploration of dynamic visual selectivity, with new predictions for in vivo experiments

---


### 232. [Self-Gating Attention for Efficient Time Series Forecasting](https://arxiv.org/abs/2607.02344)

**<font color=#1a73e8>作者：</font>** Dezheng Wang, Tong Chen, Wei Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer architectures have shown strong potential in time series forecasting, where multi-head self-attention is widely used to capture temporal dependencies across historical timestamps. However, standard self-attention has quadratic time and memory complexity with respect to the look-back length. This cost may limit its use in resource-constrained or high-throughput forecasting systems, where fast and memory-efficient inference is important. Through qualitative and quantitative analyses, we observe that self-attention maps in time series forecasting often contain redundant patterns across different timestamps. This phenomenon can be related to the repeated temporal patterns and relatively stable temporal correlations in many real-world time series. Motivated by this observation, we propose Self-Gating Attention (SGA), a plug-and-play attention mechanism that represents the attention score with a shared learnable matrix and an input-dependent residual component. The shared matrix captures common attention patterns, while the residual component captures input-dependent variations. In this way, SGA avoids the query and key projections used in standard attention score computation, leading to linear time and score-matrix memory complexity with respect to the look-back length. We integrate SGA into several forecasting backbones and compare it with standard self-attention and lightweight attention variants on nine publicly available real-world datasets covering electricity, finance, weather, medical monitoring, human activity, and climate records. The results show that SGA improves inference efficiency on public benchmarks while maintaining competitive forecasting performance against state-of-the-art attention mechanisms. These benchmark results provide deployment-oriented evidence.

---


### 233. [Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware](https://arxiv.org/abs/2607.02357)

**<font color=#1a73e8>作者：</font>** Zimo Ji, Congying Xu, Zongjie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM coding agents increasingly rely on third-party agent skills from public marketplaces, which execute with the agent's privileges and create a software supply-chain attack surface: a malicious skill can steal credentials, exfiltrate source code, or install backdoors. Existing defenses use static skill scanners based on pattern matching or LLM-as-judge analysis, but it remains unclear whether they withstand adaptive evasions that preserve malicious behavior while changing payload appearance.
This paper first presents an adversarial study of existing skill scanners through SkillCloak, a payload-preserving evasion framework that keeps the attack semantics intact while transforming their visible form. SkillCloak uses two complementary strategies: Structural Obfuscation, which rewrites visible payload indicators into semantically equivalent forms, and Self-Extracting Skill (SFS) Packing, which hides malicious components from the install-time view and restores them during agent execution. Across eight scanners and 1,613 in-the-wild malicious skills, SFS Packing bypasses every scanner at over 90%, while Structural Obfuscation bypasses over 80% on most static scanners and reaches 96% on a hybrid scanner, showing that appearance-based auditing is insufficient.
Motivated by this finding, we propose SkillDetonate, a behavior-centric runtime auditor that executes skills in a sandbox and detects malicious effects through OS-boundary information-flow evidence rather than install-time appearance. SkillDetonate combines on-demand closure lift, which observes instructions materialized during execution, with marker-based taint analysis, which tracks sensitive-data flows across the agent context, files, processes, and network operations. The results show that SkillDetonate detects 97% of attacks at a 2% false-positive rate and sustains 87% detection on real-world malicious skills.

---


### 234. [GAP-GDRNet: Geometry-Aware Monocular Visual Pose Sensing on a Single-Target Synthetic Spacecraft Dataset](https://arxiv.org/abs/2607.02360)

**<font color=#1a73e8>作者：</font>** Yonglong Zhang, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular relative pose sensing is a central perception problem in non-cooperative rendezvous and on-orbit servicing. In spacecraft images, however, weak surface texture, thin appendages, illumination changes, and partial occlusion often leave only sparse and unstable geometric evidence. This article presents GAP-GDRNet, a geometry-aware attention-enhanced framework for monocular RGB-based 6D pose sensing. The method follows the geometry-guided direct regression paradigm of GDR-Net and modifies two points in the pipeline: an attention-based feature refinement (AFR) module is placed before dense geometric prediction, and a patch-level geometric self-attention (PGSA) module is inserted into Patch-PnP. AFR reinforces global spacecraft structure together with local weak-texture cues; PGSA then relates downsampled geometric patches before final pose regression. A Blender-based annotation process supplies target masks, visible-region masks, dense model-coordinate maps, camera intrinsics, and 6D pose labels for supervised training.

---


### 235. [Data Comics for Education: Evaluating Effectiveness, Benefits, and the Ethics of AI-Assisted Creation](https://arxiv.org/abs/2607.02361)

**<font color=#1a73e8>作者：</font>** Zirui Shan, Vanessa Echeverria, Yuheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In today's data-driven world, students often struggle with interpreting visualisations due to limited visualisation literacy. Data comics have emerged as a promising medium to enhance engagement and understanding, but their educational value has seen little empirical examination, partly due to the effort required to create them. Recent advances in Generative AI (GenAI) offer a scalable solution to this challenge. We conducted a within-subjects study with 60 university students, comparing conventional visualisations with data comics, created with assistance from GenAI tools, across information retrieval and comprehension tasks. Students consistently performed better with data comics, particularly in insight comprehension tasks, independent of prior visualisation literacy. Students also commented data comics as more engaging and easier to understand, though concerns were raised about GenAI-driven misinformation and ownership. Our findings highlight the potential of data comics as a potentially effective tool for data communication in education, while underscoring the need to address ethical concerns related to AI-assisted creation.

---


### 236. [World Wide Models: Literary Tools for Cultural AI](https://arxiv.org/abs/2607.02369)

**<font color=#1a73e8>作者：</font>** Nina Begus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs stage a new form of cultural encounter that is massive, automated, and monolingual. Literary disciplines have always negotiated cultural struggles with comparative reading of literature, narratological and poetic analysis, critical theory, world literature, and translation. These tools have now become indispensable for building culturally literate AI. The essay develops a layered framework toward more nuanced textual models and pluralistic interpretations of AI, emphasizing the natural intersections of literature and AI development, connecting current debates in critical theory with structural monolingualism, and suggesting a new application of world literature approaches to address global AI textuality through macrostructure, circulation, and untranslatability.

---


### 237. [Representation Distribution Matching for One-Step Visual Generation](https://arxiv.org/abs/2607.02375)

**<font color=#1a73e8>作者：</font>** Lan Feng, Wuyang Li, Eloi Zablocki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We elucidate the design space of Representation Distribution Matching (RDM), our name for the paradigm that trains a one-step image generator by matching generated and reference feature distributions under frozen pretrained encoders. We identify two design axes, how the distributions are compared and the representations they are compared in, and controlled studies along them yield three findings. First, the classical MMD, which could not train convincing generators a decade ago, becomes a strong and scalable objective once estimated right. Second, the generated batch is then the operative variable, with an optimum above 2048, far beyond customary batch sizes. Third, any single representation can be gamed, driven below the real score while images stay visibly fake, so we match against a balanced battery of encoders and evaluate with SW_r14, a Sliced-Wasserstein distance over 14 encoders that is independent of the training loss and resists gaming. Combining the preferred choices yields improved RDM (iRDM): it sets the one-step state of the art on ImageNet at SW_r14 1.30, corroborated by PickScore, a human-preference proxy our objective never optimizes, which prefers it over the prior best one-step generator on 71.2% of matched samples. The same recipe post-trains the four-step FLUX.2 [klein] into a one-step generator, surpassing the four-step version on GenEval, 0.826 to 0.794, and on PickScore, 22.76 to 22.58, in 90 H200 GPU-hours. Project page: this https URL.

---


### 238. [HULAT2 at MER-TRANS 2026: Governed Multi-Agent Simplification for Spanish Easy-to-Read Generation](https://arxiv.org/abs/2607.02381)

**<font color=#1a73e8>作者：</font>** Lourdes Moreno, Paloma Martínez, Marco Antonio Sanchez-Escudero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the participation of HULAT2-UC3M in the Spanish track of MER-TRANS 2026, a shared task on multilingual Easy-to-Read translation. Three fully automatic Spanish runs were submitted. RUN1 and RUN2 used a LangGraph-based multi-agent workflow combining Gemini 2.5 Flash and RigoChat-7B-v2, parallel generation strategies, internal quality signals, Event-Condition-Action routing, controlled editing and traceable decisions. RUN1 used the base workflow, while RUN2 activated an additional lexical-support layer based on a glossary and lexical resources. RUN3 was a RigoChat-based generate-evaluate-regenerate baseline with prompt engineering and LoRA-based adaptation. The official leaderboard reports BLEU-Orig, BLEU-Gold, SARI and BERTScore. During development, additional internal signals were also inspected, including semantic fidelity, readability, lexical simplicity, syntactic clarity and factual consistency. According to official SARI, RUN1 was the best HULAT2 run, with 44.0543 points, followed by RUN2 with 43.1049 and RUN3 with 38.5136. These results indicate that, in this task setting, signal-guided multi-agent routing outperformed the linear regeneration baseline. They also show that adding lexical support did not automatically improve reference-based scores. Further segment-level and document-level analysis are required to assess readability, factual consistency and user-oriented adequacy.

---


### 239. [Know Your Source: A Public Knowledge Store for Media Background Checks](https://arxiv.org/abs/2607.02383)

**<font color=#1a73e8>作者：</font>** Benjamin Nichols, Michael Schlichtkrull, Nedjma Ousidhoum  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based retrieval-augmented generation (RAG) is increasingly used for automated fact-checking (AFC) and related tasks. By grounding LLM outputs in retrieved evidence, RAG-based systems provide transparent justifications while allowing external information to be updated independently of the underlying model. However, existing approaches often assume retrieved evidence is reliable, although real-world information may be conflicting, outdated, and can originate from unreliable or biased sources. Recent work on *source-critical reasoning* addresses this challenge through media background checks (MBCs) (Schlichtkrull, 2024), which assess the credibility of evidence sources to support downstream fact verification. However, generating MBCs relies on costly proprietary search APIs, limiting reproducibility. To mitigate this issue, we introduce MEDIAREF, a publicly available knowledge store of web-sourced documents that enables reproducible, low-cost evaluation of MBC generation across 200 media sources. We describe a reproducible methodology for constructing and updating the collection, assess widely used LLMs on the MBC generation task, and demonstrate that MEDIAREF supports higher-quality MBC generation through both automatic and qualitative evaluation.

---


### 240. [Transformer Geometry Observatory TGO-II: Representational Similarity Observatory](https://arxiv.org/abs/2607.02386)

**<font color=#1a73e8>作者：</font>** Kaustubh Kapil, Kishor P. Upla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Vision Transformers have achieved remarkable success across computer vision and language applications, the geometric evolution of their internal representations throughout training remains insufficiently understood. Existing analyses primarily focus on attention mechanisms and downstream performance, leaving the evolution of representation geometry largely unexplored. In this work, we present Transformer Geometry Observatory-II (TGO-II), a representation geometry analysis framework designed to investigate how Transformer representations evolve during supervised training. TGO-II analyzes Vision Transformer (ViT-Small/16) representations using Centered Kernel Alignment (CKA), Singular Vector Canonical Correlation Analysis (SVCCA), Two-Nearest Neighbor Intrinsic Dimensionality (TwoNN-ID), and token covariance analysis. Our experiments reveal three key observations. First, both CKA and SVCCA progressively decrease throughout training, indicating increasing representational specialization across Transformer layers. Second, intrinsic dimensionality consistently increases before stabilizing, suggesting progressive expansion of the representation manifold into a larger set of locally accessible degrees of freedom. Third, token covariance and coupling analyses demonstrate that strong token interaction structure persists throughout training, challenging the hypothesis that increasing representational complexity arises primarily from progressive token independence. These findings suggest that representation complexity and layer specialization emerge simultaneously during training. Manifold expansion appears to occur without token decoupling. Together, these observations motivate a new hypothesis in which Vision Transformers increase representational complexity through progressively richer transformations while preserving strong token interaction structure during learning.

---


### 241. [Steerability via constraints: a substrate for scalable oversight of coding agents](https://arxiv.org/abs/2607.02389)

**<font color=#1a73e8>作者：</font>** Thomas Winninger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are capable; human oversight is the bottleneck. Unconstrained agents introduce security risks, erode codebase scalability, and make human review increasingly costly. We argue that the same methods used for decades to manage large human engineering teams: access control, network policies, strict coding conventions enforced by tooling; transfer directly to coding agents, and are cheaper (in token) than recent agentic scaffolding. We sketch a start-to-end system on this principle, and report a controlled experiment in scalable oversight: a small reviewer (Gemma 4 e4b) inspects a Python codebase containing 11 inserted backdoors. Recall rises from 54.5% (unconstrained, no tools) to 90.9% (constrained substrate plus a ~200-LoC `docs` CLI), with substrate and tools contributing independently. We choose Python deliberately: substrate-level oversight gains are largest where the language gives the fewest guarantees by default; the principles extend to languages like Rust.

---


### 242. [Show Me Examples: Inferring Visual Concepts from Image Sets](https://arxiv.org/abs/2607.02402)

**<font color=#1a73e8>作者：</font>** Nick Stracke, Kolja Bauer, Stefan Andreas Baumann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can follow complex textual instructions, yet they struggle to reason from purely visual context. In particular, current models fail to infer shared concepts from sets of example images and apply them to new inputs. We introduce Visual Concept Inference from Sets (VICIS), a task that evaluates this capability. Given a small context set of images sharing a concept and a query image, the model must generate new images that preserve the context-defined concept while remaining consistent with the query. We show that state-of-the-art VLMs perform poorly on this task, often ignoring the visual context or defaulting to biased generations. To address this gap, we propose a training framework and architecture that learn to infer visual concepts from image sets and extract concept-specific embeddings from queries. Experiments on synthetic data and large-scale ImageNet/WordNet data show that our model generates more accurate and diverse outputs and generalizes to unseen concepts and modalities such as sketches.

---


### 243. [Object-centric LeJEPA](https://arxiv.org/abs/2607.02404)

**<font color=#1a73e8>作者：</font>** Jakob Geusen, Ender Konukoglu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image encoders trained with LeJEPA can deliver strong features for downstream tasks, but, like other image-level self-supervised methods, typically require large training datasets. Aligning representations at the level of objects rather than whole scenes promises greater data efficiency, but doing this in a completely self-supervised way, effectively jointly partitioning a scene and representing its objects, is unstable: the two are locked in a cyclic dependency, partitioning requires meaningful representations, while meaningful representations require consistent partitioning. We sidestep this instability by taking object masks as given during training, using cheap, off-the-shelf SAM proposals. We extend LeJEPA - whose distributional anti-collapse objective ports naturally from whole images to variable-sized sets of objects - to align object-centric representations rather than whole images. An additional instance-separating loss, which treats other objects in the same scene as negatives, further boosts downstream performance. Across two model scales and 10-100% of COCO, object-level LeJEPA outperforms image-level LeJEPA on tracking (DAVIS), classification (ImageNet-1k), segmentation (ADE20k), and re-identification (NAVI).

---


### 244. [Text-Driven 3D Indoor Scene Synthesis in Non-Manhattan Environments](https://arxiv.org/abs/2607.02407)

**<font color=#1a73e8>作者：</font>** Xianhui Meng, Zirui Song, Yuchen Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities in 3D indoor synthesis for Manhattan environments. However, existing methods often fail to capture plausible object layout patterns in non-Manhattan settings, primarily because they struggle to model non-orthogonal spatial relationships, leading to high geometric violations and low physical fidelity. To address this challenge, we propose SPG-Layout, a novel text-driven framework designed to generate physically plausible indoor scenes within complex non-Manhattan environments. Specifically, we first utilize statistical priors of object distributions to guide the training process, enhancing environmental understanding and fidelity. Furthermore, mirroring human design workflows, we adopt a hierarchical layout strategy that prioritizes the placement of large objects, thereby substantially minimizing layout violations. By synergizing these components, SPG-Layout achieves a balanced optimization of semantic realism and physical plausibility. To evaluate performance in these complex settings, we constructed a new benchmark comprising 500 diverse non-Manhattan environments. Extensive experiments demonstrate that SPG-Layout consistently and significantly outperforms existing methods across both Manhattan and non-Manhattan environments. The code will be publicly released.

---


### 245. [The Future of NLP may not be at NLP Conferences: Scholarly Migration Patterns in Natural Language Processing](https://arxiv.org/abs/2607.02416)

**<font color=#1a73e8>作者：</font>** David Jurgens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Processing (NLP) has traditionally been published in its core disciplinary venues like ACL. However, advances in Large Language Models (LLMs) has led to a blurring of the disciplinary lines between NLP and general Machine Learning (ML), with authors regularly publishing in venues from both fields. Here, we ask whether the disciplinary center of gravity is shifting. Using NLP research published from 2010 to 2026 and studies of both established and new authors, we find that a migration is taking place. First, comparing the pre- and post-LLM eras, established authors lost 19.2pp of share at flagship *ACL main-conference tracks while gaining 14.8pp in the newer Findings tracks, and general ML venues rose 8.6pp, even when adjusting for parallel growth in the fields. Second, among newer authors who debut with at least three first-author NLP-topic papers, the share whose work appears mostly at *ACL venues fell from 84% (2019) to 74% (2024), while the share appearing mostly at general ML venues rose from 5% to 21%. Using causal inference techniques, we estimate that these general ML venues confer a significant citation premium, which influences venue selection. Together, these results point to a significant shift in where NLP research is published.

---


### 246. [Wavelet-Guided Semantic Signal Compensation for Inversion-Free Image Editing](https://arxiv.org/abs/2607.02421)

**<font color=#1a73e8>作者：</font>** Anqi Tang, Wenhao Sun, Zhaoqiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided image editing aims to modify visual content according to a target prompt while preserving the background. Recent inversion-free image editing frameworks such as FlowEdit have demonstrated strong editing capability without requiring inversion. Empirically, FlowEdit can achieve substantial semantic changes under appropriate hyperparameter settings. However, we observe that under certain global attribute shifts, the editing trajectory may not effectively move away from the source distribution in the early timesteps. Our analysis suggests that in the high-noise regime, the dominant manifold-seeking flow toward the data manifold can reduce the influence of the text-conditioned direction, leading to limited global modification while background structures remain only moderately preserved. Inspired by this observation, we propose an inversion-free, frequency-aware semantic compensation strategy that strengthens the effective signal in the early stage of generation, while maintaining structural consistency in the background. The proposed method improves global editing capacity without sacrificing background fidelity.

---


### 247. [Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs](https://arxiv.org/abs/2607.02425)

**<font color=#1a73e8>作者：</font>** Francesca Pistilli, Simone Alberto Peirone, Giuseppe Averta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding human behavior while interacting with the surrounding world is crucial for many applications of embodied AI. First-person videos are particularly informative for this problem, as they well capture how activities reshape the scene over time. However, existing approaches often rely on implicit visual or language-aligned representations, disregarding structured reasoning over the scene dynamic. We argue that explicit, compositional and editable representations of human-environment interactions can play a crucial role for rich grounded activity understanding. To this end, we introduce SG-Ego, a large scale annotation set extending Ego4D with spatio-temporal scene graphs, where relations triplets are consolidated over time into explicit time-evolving descriptions of the scene state. To reason over this representation, we propose GLEN, a graph-based model that operates over scene graph sequences to both align them with textual actions and model their temporal evolution. In addition, we formulate the activity-driven graph-edit forecasting (A-GEF) problem, a novel task that casts scene dynamics as a sequence of structured transformations conditioned on ongoing actions, enabling explicit reasoning about how scenes change over time. We validate our approach across multiple downstream tasks, spanning retrieval benchmarks as EgoMCQ and EgoCVR, as well as long-horizon reasoning benchmarks as EXPLORE-Bench and the newly introduced A-GEF. GLEN achieves strong results compared to raw video baselines and it excels in reasoning settings, typically addressed only with MLLMs, while enabling controllable and structured predictions of scene dynamics driven by human activities. We believe our results establish spatio-temporal scene graphs, together with models that reason over them, as strong compositional and interpretable representations for video understanding and potentially beyond.

---


### 248. [QFedAgent: Quantum-Enhanced Personalized Federated Learning for Multi-Agent Activity Recognition](https://arxiv.org/abs/2607.02426)

**<font color=#1a73e8>作者：</font>** Quoc Bao Phan, Tuy Tan Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data, making it suitable for privacy-sensitive robotic sensing applications. However, multi-agent systems generate heterogeneous and non-independent and identically distributed (non-IID) multimodal sensor streams that degrade conventional FL algorithms, while classical fusion modules introduce substantial parameter overhead and communication cost. This paper proposes QFedAgent, a hybrid quantum-classical personalized FL framework for multi-agent activity recognition. The approach integrates a variational quantum circuit fusion module that models accelerometer--gyroscope interactions through quantum state encoding and entanglement, requiring only 72 quantum rotation parameters versus 33K in classical multi-layer perceptron-based fusion, achieving approximately 10x total parameter reduction. Experiments on the OPPORTUNITY dataset under subject-based non-IID partitions demonstrate 97.7% mean test accuracy, confirming that parameter-efficient quantum fusion remains competitive with conventional federated baselines.

---


### 249. [Physical surfaces make touch interactions in virtual reality precise, efficient, and bimanual](https://arxiv.org/abs/2607.02430)

**<font color=#1a73e8>作者：</font>** Wen Ying, Seongkook Heo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual reality (VR) systems can enable convenient hand-based interactions across diverse work scenarios. However, mid-air gestures lack tactile feedback and a physical reference surface to support the hand. This absence of haptic grounding can cause significant challenges in achieving precise and efficient touch interactions. This paper investigates the effect of different types of hand-grounded haptic feedback on the touch performance of VR tasks that demand high precision, such as selecting, tracing, and sketching. We compared three levels of haptic feedback: 1) No Haptic Feedback, where only visual feedback was provided; 2) Tactile Feedback, where users received vibrotactile and pressure feedback upon touching a virtual surface; 3) Physical Surface, where users interacted with a portable and tangible surface.
Our study found that portable physical surfaces enabled the best selection precision, tracing efficiency, and sketch quality. Furthermore, participants showed increased bimanual hand utilization when engaging with a physical surface during tasks. These observed behaviors corresponded to participants' preference for interacting with physical surfaces, attributed to a better sense of confidence and control.

---


### 250. [MARVEL: Margin-Aware Robust von Mises-Fischer Expert Learning for Long-Tailed Out-of-Distribution Detection](https://arxiv.org/abs/2607.02435)

**<font color=#1a73e8>作者：</font>** A.S. Anudeep, Vaanathi Sundaresan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For clinical deployment, it is essential that automated diagnostic systems remain reliable when confronted with previously unseen cases, yet deep models routinely misclassify out-of-distribution (OOD) inputs with high confidence, underscoring the need for more robust OOD detection methods. Although substantial effort has been devoted to improving model robustness, most of the existing literature assumes balanced datasets, evaluates OOD detection on coarse or non-clinical OOD sources, or lacks comprehensive assessment across diverse OOD scenarios. To address the gaps, we propose a novel methodology trained on diverse and imbalanced medical datasets and evaluated across a clinically reflective OOD spectrum. Our framework comprises three key components: (1) a Nonlinear von Mises-Fisher (NvMF) classifier capable of learning non-linear decision boundaries, with theoretical proof of its asymptotic connection to cosine classifiers; (2) a multi-expert framework in which margin-aware NvMF classifiers specialise in different regions of label distribution to better handle imbalance; and (3) an outlier expert trained explicitly to distinguish inlier from outlier data, thereby strengthening OOD detection. Evaluation on RFMiD, ISIC2019, and NCTCRC datasets demonstrates consistent improvements over state-of-the-art methods, achieving mean FPR95 reductions of 8.45%, 13.02%, and 36.90% respectively. These gains are further supported by comprehensive ablations that validated the contributions of each component. This enables reliable identification of unfamiliar cases for deferral to clinicians, supporting safer AI-assisted diagnosis in real-world workflows. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
