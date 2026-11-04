# 📦 其他研究 | 2026年11月05日

> 本类共 **280** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-280](./part-06.md)

---

### 51. [From Visual Matching to Textual Conditioning: Cross-Domain Few-Shot Segmentation via Reference Inversion](https://arxiv.org/abs/2611.04084)

**<font color=#1a73e8>作者：</font>** Jiahao Nie, Yun Xing, Wenbin An 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-Domain Few-Shot Segmentation (CD-FSS) aims to segment objects from unseen domains using only a few annotated references. Recent Segment Anything Model (SAM)-based methods have advanced CD-FSS, yet their reference-target visual matching is highly sensitive to target appearance variations. SAM3 introduces text-conditioned segmentation, enabling natural-language descriptions to guide segmentation across target images, but directly using the category name as the condition still yields unstable performance under severe domain shifts. We propose Reference Inversion for SAM3 (RI-SAM3) that leverages SAM3's large-scale vision-language pre-training to learn suitable textual tokens for each target category. RI-SAM3 comprises three core designs: (i) Bi-level Reference Inversion that learns complementary tokens before and after the frozen text encoder: the former remain anchored in SAM3's text space while the latter represent the category more flexibly; (ii) Layer-adaptive Textual Conditioning combines these tokens differently as object queries evolve across decoder layers; and (iii) Presence-aware Confidence Supervision that jointly supervises query confidence and target presence for reliable predictions. With SAM3 frozen, RI-SAM3 optimizes around 12K parameters only per category and it efficiently segments each target in a single forward pass with reusable textual conditioning without per-sample reference-target visual matching. Extensive experiments over multiple widely adopted benchmarks show that RI-SAM3 achieves superior performance consistently in CD-FSS tasks, together with strong robustness, efficiency, and generalization.

---


### 52. [CHROMA-MILL: Joint Low-Light Enhancement and White Balance under Colored Illumination](https://arxiv.org/abs/2611.04092)

**<font color=#1a73e8>作者：</font>** Pol Riubrogent-Comas, David Serrano-Lozano, Maria Pilligua 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capturing an image in a low-light environment produces a weak, noisy sensor signal. Low-light image enhancement (LLIE) aims to restore it. Auto white balance (AWB) is also required for every image, and the same noisy signal degrades its ability to infer the scene illuminant. LLIE is typically performed first, followed by AWB, but this strategy remains largely unexamined because existing low-light datasets span a narrow range of illuminants and lack illuminant ground truth for evaluating AWB. We address this with CHROMA-MILL, a RAW dataset of 50 scenes captured with a DSLR and smartphone under four calibrated illuminants at eleven intensity levels. Because light is additive, we blend these captures in the linear RAW domain to synthesize physically valid illuminant mixtures with exact chromaticity ground truth. Benchmarking on this data, we find joint correction is best, and introduce CTI-Retinexformer, which supervises an illumination map, a chromaticity prediction, and an illumination-invariant scene embedding, outperforming the best cascade by 0.7 dB PSNR$_L$ and 1.1 $\Delta E_{00}$.

---


### 53. [ScaleTraj: Scale-Decomposed Human Trajectory Generation](https://arxiv.org/abs/2611.04097)

**<font color=#1a73e8>作者：</font>** Yulin Zeng, Yiheng Zhao, Jun Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individual-level trajectories are essential for applications that rely on user-level mobility behavior. Existing mobility-generation approaches face a fundamental tension between individual-level and population-level statistical fidelity: top-down models reproduce aggregate mobility statistics but struggle to guarantee realistic individual trajectories, while bottom-up generators synthesize individual trajectories yet often fail to preserve key population-level mobility regularities after aggregation. In particular, many bottom-up generated populations fail to reproduce the displacement distribution, whose heavy tail is well summarized by a truncated power law. We formalize this phenomenon as the \textbf{Population-Level Displacement Gap}. To investigate its prevalence, we conduct a systematic evaluation of representative model-driven and data-driven trajectory generators. Our results provide evidence that the Population-Level Displacement Gap is prevalent across diverse generation paradigms. To diagnose this gap, we introduce the \textbf{Scale Fidelity Profile (SFP)}, a scale-decomposed metric that quantifies discrepancies in trip allocations across spatial scales. SFP indicates that population-level displacement mismatches co-occur with systematic errors in how trips are allocated across spatial scales. Motivated by this observation, we develop \textbf{ScaleTraj}, an autoregressive Transformer that decomposes location prediction into a Scale Selection Head that decides the movement scale and a Scale-Aware Cell Selection Head that predicts the destination conditioned on the selected scale. Experiments on two datasets show that ScaleTraj reduces the Population-Level Displacement Gap versus model-driven and data-driven baselines, while preserving fidelity. Our code is available at this https URL.

---


### 54. [Structured Clinical Memory as Context for Probabilistic Decision Models: A Synthetic Evaluation with Jev](https://arxiv.org/abs/2611.04101)

**<font color=#1a73e8>作者：</font>** Jash Sayani, Gaurang Karwande, Achinth Bharadwaj  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Longitudinal clinical context is often distributed across noisy, repetitive forms and narrative records. We study whether a compact structured memory can improve a probabilistic decision model's answers when the underlying patient vignette is already available. We created 30 fully synthetic cases spanning twelve clinical domains, paired each with synthetically generated structured memory, and evaluated 120 typed questions with Jev. The raw-vignette arm achieved 90.0% accuracy (95% normal-approximation confidence interval: 84.6%-95.4%); adding memory achieved 93.3% (88.9%-97.8%). Five questions changed from incorrect to correct and one changed in the opposite direction (exact McNemar $p=0.219$). Choice log loss decreased from 0.258 to 0.175 and binary Brier score from 0.054 to 0.022. Memory added 310 input tokens per call on average, while observed mean latency was unchanged at approximately 0.5 seconds. These results are directionally positive rather than clinically validating: the cases are synthetic, the labels are single-author judgments, and the memory is an oracle upper bound rather than extracted production output. The pilot supports evaluating structured clinical memory as a reusable state interface for decision models.

---


### 55. [Is This 3D Asset Usable? Beyond the Beauty Render for Asset Curation](https://arxiv.org/abs/2611.04102)

**<font color=#1a73e8>作者：</font>** Rushikesh Zawar, Vladimir Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large 3D repositories make it easy to collect assets, but difficult to determine whether they can be reused reliably across scene assembly, editing, rendering, game production, and training-data construction. An asset can look plausible in RGB while hiding disconnected geometry, problematic UV organization, or materials that fail to resolve correctly after import. We introduce Diagnostic Rendered Evidence (DRE): aligned beauty, wireframe, and UV-seam-plus-wireframe views scored by pass-specific frozen ViT classifiers and combined through late fusion. On 1,234 human labeled TexVerse assets, nested grouped evaluation achieves 86.36% balanced accuracy and 88.32% bad-asset recall. On a separate, balanced 764 external reference test, DRE achieved 88.9% balanced reference-label accuracy. Our method requires only an imported asset and renderer-derived evidence, without repository identity, creator, popularity, text, or source metadata at inference. Our results support cross-corpus portability and show that purpose built diagnostic views expose defects that just the beauty views can miss. Webpage: this https URL

---


### 56. [Structure, Dimensionality, and Distribution Shape - What Makes Pretraining Data Transferable, and Why the Input Pipeline Decides Which](https://arxiv.org/abs/2611.04106)

**<font color=#1a73e8>作者：</font>** Sangyoon Bae, Jiook Cha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What makes a pretraining corpus transferable? We describe a corpus by three properties: its structure, its dimensionality, and the distribution shape of each unit's values. We propose the Transfer-Invariance Principle: the same property can be irrelevant to transfer under one input transform and decisive under another, so the model's input transform, not the data modality, decides which properties can matter. To test it we build TransferForge, a generator that places a synthetic population at any prescribed structure, dimensionality, and distribution shape. KernelSynth, the synthetic prior of Chronos, cannot, because it draws independent series. When the model standardizes each input window (PatchTST on UCR), the distribution shape is inert and the structural setting governs. Synthetic pretraining then matches a real corpus of the same size and exceeds it once scaled. When the model encodes calcium fluorescence signals without normalization (POYO Plus), the shape becomes a governing constraint, and a shape-matched synthetic corpus replaces real pretraining with zero real neural activity. Flipping only the input normalization, with the model and data fixed, changes the effect of a shape manipulation by a factor of 5.3, so the pipeline, not the modality, sets the switch. The principle yields a recipe that chooses what to synthesize before any training. Pretraining data then becomes something to manufacture for the model, most valuably where real data is scarce, expensive, or private.

---


### 57. [Separating Common and Unique Directions for Data-Free Model Merging](https://arxiv.org/abs/2611.04108)

**<font color=#1a73e8>作者：</font>** Shiting Wang, Yingjie Zou, Ke li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines multiple fine-tuned models without additional training, and arithmetic methods have emerged as a simple yet effective way to merge models without data. However, existing arithmetic methods treat task vectors in parameter space and apply a single element-wise rule to directions that can differ in mergeability. In a shared directional basis, we find a consistent two-regime structure: a low-dispersion common bulk shared across tasks and a high-dispersion task-dominated tail that carries disproportionate energy. These findings motivate Common--Unique Subspace Decomposition (CUSD), a data-free pre-merging method that separates task vectors into common and unique directional components, merges the common components with downstream arithmetic operator, and retains unique residuals separately. Experiments across $11$ base models, four model families, and four arithmetic-based merging operators show that CUSD improves 42 of 44 model--operator combinations and achieves up to 22.5% improvement over the corresponding baselines. Our code is publicly available at this https URL

---


### 58. [Decomposing Rank Reversals under Temporal Nonstationarity: Alignment, Aggressiveness, and Instability](https://arxiv.org/abs/2611.04116)

**<font color=#1a73e8>作者：</font>** Deying Song, Xueying Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under temporal nonstationarity, model performance rankings reverse across training horizons due to heterogeneous sensitivities to memory. While existing literature addresses adaptive lookbacks, effective model complexity, and empirical forecast evaluation in isolation, no unified framework explains the structural mechanics driving these rank reversals. We bridge this gap by deriving a model-agnostic decomposition of out-of-sample $R^2$ into target alignment, miscalibrated aggressiveness, and predictive instability. Within this framework, we mathematically characterize complexity phase boundaries, establish closed-form optimal-memory equations for ridge regression under local drift, and extend these guarantees to complex model architectures via surrogate bounds. We validate these theoretical dynamics by benchmarking 14 linear, tree-based, and neural architectures across large-scale financial panels. In doing so, our framework demonstrates that empirical model rank reversals are driven by predictable surges in miscalibrated aggressiveness, providing a rigorous mechanistic diagnosis of generalization under temporal shift.

---


### 59. [ScrambleMark: Zero-Query Watermark-Agnostic Black-Box Evasion of Modern Speech Watermarking](https://arxiv.org/abs/2611.04122)

**<font color=#1a73e8>作者：</font>** Binhao Ma, Weikang Ding, Hanqing Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Speech watermarking is becoming a key defense for digital copyright and content authentication. Existing attacks treat evasion as a removal problem: they erase the watermark, relying on detector access or on speech data that is hard to collect, such as paired clean-watermarked or clean target speaker speech. Commercial platforms are moving to close off these assumptions. TrustedAudio, for instance, restricts detection to authenticated users and denies meaningful detection feedback to unauthorized parties. Adversaries thus cannot tell whether a sample is watermarked or which watermark it carries, nor reliably remove it without degrading speech quality.
In this work, we show that evading a speech watermark does not require erasing it: detection relies on the structural consistency of the embedded pattern, and disrupting this consistency is enough to defeat it. Building on this observation, we identify harmonic structure as an effective attack surface, as perturbing it breaks watermark consistency while preserving perceptual quality. We therefore propose ScrambleMark, a zero-query, watermark-agnostic, black-box attack that evades detection through harmonic scrambling. ScrambleMark combines a deterministic engine for discovering transferable harmonic perturbations with a generative model that learns randomized scrambling patterns, avoiding reliance on fixed attack rules. Across three commercial platforms (Google SynthID, Resemble AI, and TrustedAudio), ScrambleMark is the only attack to both evade detection and keep speech natural, achieving nearly 97% evasion and a 4.2/5 human rating, far above the 1.1 to 1.7 of prior attacks. Beyond evasion, ScrambleMark withstands adaptive recovery designed to reverse it, evidence that structural evasion is hard to mitigate in practice.

---


### 60. [RGDM: Robust Graph Diffusion Model](https://arxiv.org/abs/2611.04146)

**<font color=#1a73e8>作者：</font>** Yancheng Wang, Ping Li, Dongfang Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models represent a powerful class of generative models known for their solid theoretical foundations and remarkable performance across diverse tasks and domains. Existing node level diffusion methods synthesize nodes and edges within a graph, but are not designed to learn a robust generator from adversarially corrupted graphs. In this study, we introduce the Robust Graph Diffusion Model (RGDM), designed to generate labeled synthetic graph structures consisting of nodes and edges that integrate seamlessly into a given graph. The RGDM consists of a Robust Graph Autoencoder (RGAE) and a Latent Diffusion Model (LDM). Leveraging an edge selection mechanism and an innovative low-rank regularization on the latent feature, the RGDM produces clean and high-quality synthetic graph structures, even when trained on graphs subject to adversarial attacks. Comprehensive experimental evaluations reveal that Graph Neural Networks (GNNs) trained on the augmented graph, which is formed by merging the original attacked graph with the synthetic graph structures, exhibit significantly improved robustness against various graph adversarial attacks in the context of semi-supervised node classification. The code of the RGDM is available at this https URL.

---


### 61. [Palimpsestic Accountability in the US Federal AI Inventories](https://arxiv.org/abs/2611.04153)

**<font color=#1a73e8>作者：</font>** Dipto Das, Syed Ishtiaque Ahmed, Aditya Vashistha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI inventory is a structured, often public record in which a government or organization lists and describes the AI systems it uses or plans to use. Studies of single AI inventory releases describe what systems do but say little about how they are governed over time. We linked entries across three releases of the US Federal AI Use Case Inventory (2023--2025), compared answers only where both releases required them, and analyzed governance accounts through a dual deductive-inductive approach, guided by the Algorithmic Decision-Making Adapted for the Public Sector (ADMAPS) framework. As the inventory grew from 710 to 3,611 entries from 2023 to 2025, fewer required answers were left blank, but accountability was rewritten through three mechanisms. Each release \emph{redrew} the scope of the questions; agency-assigned classifications \emph{gated} what was reported; and answers were also \emph{overwritten}, with gains and losses concentrated in single agencies and little account of human oversight and judgment. These findings show that each release redraws the boundary of accountability and leaves the public to \emph{re-stitch} the records, a condition we term \textbf{palimpsestic accountability}. We recommend versioned records, reasons for every reclassification, public files that distinguish kinds of missing answers, and oversight documented as conditions to improve public sector AI accountability.

---


### 62. [Improving PI-RADS Prediction and Prostate Cancer Detection from Multiparametric MRI with Anatomical Guidance](https://arxiv.org/abs/2611.04155)

**<font color=#1a73e8>作者：</font>** Seungbin Park, Thibault Heintz, Rachit Saluja 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of Prostate Imaging Reporting and Data System (PI-RADS) scores from multiparametric MRI (mpMRI) remains challenging, more so than clinically significant prostate cancer (csPCa) detection. Given the importance of lesion location in PI-RADS scoring, we evaluated whether incorporating prostate zonal masks improves PI-RADS prediction and csPCa detection across multiple architectures (3D ResNet-18, ResNet-50, and ViT) using a large-scale internal dataset. Anatomical guidance generally improved performance across architectures, with the best results achieved by ResNet-18 with 2-zone guidance for PI-RADS prediction (QWK = 0.511) and ResNet-50 with 5-zone guidance for csPCa detection (AUC = 0.809). Fine-tuned results on external datasets further demonstrated the benefits of anatomical guidance. Furthermore, models with anatomical guidance improved the utility of model-predicted PI-RADS scores for PI-RADS-based csPCa detection (positive defined as PI-RADS>=3). Combining model-predicted and expert-assigned PI-RADS scores significantly increased the AUC from 0.711 to 0.756 (p < 0.05), suggesting that AI-derived PI-RADS scores may provide complementary information to expert assessment for csPCa detection. Overall, our findings highlight the value of incorporating prostate zonal anatomy into deep learning-based prostate MRI assessment.

---


### 63. [On the Feature Evolution of Temporal Difference Learning](https://arxiv.org/abs/2611.04158)

**<font color=#1a73e8>作者：</font>** Shangzhe Li, Dechen Zhang, Difan Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal-difference (TD) learning trains neural representations using bootstrapped targets generated by evolving value estimates, yet how predictive features emerge and propagate under incomplete neural updates remains poorly understood. We investigate this problem using finite-width two-layer ReLU critics on a constructed family of smooth stochastic horizon-$H$ MDPs with unknown quadratic structure and $d$-dimensional observations. We first show that an informative TD update acquires the quadratic Bellman signal and yields a representation admitting a bounded predictive readout. The simultaneous hidden-weight and head update achieves a strict finite-sample prediction-risk improvement over matched head-only SGD, with a $2(d+1)$-fold larger population quadratic response. We then establish that an imperfect learned continuation can already provide informative supervision to an earlier zero-reward stage. By tracking coupled neural updates with one SGD step per target copy, without requiring intermediate Bellman regressions to be solved, we obtain a uniform prediction-error transient $\exp[-\Omega(K/(Hd))]$, up to action-independent shifts and explicit sampling and finite-width errors. On the constructed signed-action MDP family whose total reward is bounded by 1, we show that an exploration-then-commit algorithm can achieve $\widetilde{O}(d^3H^{1/3}T^{2/3})$ regret over $T$ episodes, using $K=\widetilde{O}(Hd)$ global updates. Our analysis connects bootstrapped feature acquisition, concurrent neural refinement, and finite-budget policy performance.

---


### 64. [ReconDreamer#: Self-Evolving Closed-Loop Synergy of Reconstruction and Generation for Dynamic Driving Scenes](https://arxiv.org/abs/2611.04173)

**<font color=#1a73e8>作者：</font>** Songling Liu, Guosheng Zhao, Xiaofeng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic driving scene reconstruction has made remarkable strides in recent years by leveraging generative priors, particularly in the quality of novel trajectory rendering. Nevertheless, a significant gap remains between the generated data and real-world sensor observations, severely hindering further improvements in reconstruction fidelity. In this paper, we present ReconDreamer#, a self-evolving framework that synergizes reconstruction and generation for dynamic driving scenes, which substantially bridges the gap between synthesized novel trajectory data and recorded real-world observations. Within this self-evolving closed-loop framework, the generative and reconstruction models mutually reinforce each other through iterative refinement, ultimately yielding a significant enhancement in the 3D representation capability of the reconstruction model. Additionally, we introduce a geometry-prior-based adaptive ground model to further enhance the rendering quality of the reconstruction model. To validate the effectiveness of the proposed method, we conduct comprehensive evaluations on Waymo, nuScenes, PandaSet, and EUVS benchmarks. Specifically on Waymo, at a 6-m lateral shift, ReconDreamer# improves NTA-IoU and NTL-IoU by 8.8% and 3.0%, respectively, and reduces FID by 15.1% relative to ReconDreamer++.

---


### 65. [Clocks all the way down: does sequence-processing AI need endogenous temporal structure?](https://arxiv.org/abs/2611.04181)

**<font color=#1a73e8>作者：</font>** Meysam Hashemi, Alireza Valizadeh, Viktor Jirsa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mainstream sequence-processing AI is temporally reactive: each update is driven by input and learned state transitions, rather than by an independently evolving internal temporal reference. Biological brains, by contrast, continuously generate rhythmic activity that structures perception, memory, and cognition, and this rhythmicity reaches all the way to behavior. We ask whether this difference is merely implementational or genuinely computational. Four lines of evidence suggest that endogenous temporal structure supports putative functions that input-driven architectures may not readily replicate: 1) phase-dependent routing of information, 2) delay-structured combinatorial representation, 3) cross-frequency multiplexing of items, and 4) oscillation-gated offline consolidation. A proof-of-concept delay-ablation test dissociates representational capacity from memory retrieval. In recurrent and spatial spiking networks with fixed synaptic weights and connectivity, shuffling delays preserves part of the capacity but substantially impairs the sequence retrieval. The relative contrast is more pronounced for spatial networks and longer propagations. Instantaneous transmission collapses capacity itself. We then outline a cross-frequency multiplexing scheme that combines item identity and serial order with alternative mechanisms for selective memory retrieval. Finally, we state one falsifiable hypothesis, conditions for matched-resource tests, and three research directions: the components already exist; the disciplined comparison does not.

---


### 66. [Agentic Path Maps: Exposing an Agent's Traversal Through the Garden of Forking Paths](https://arxiv.org/abs/2611.04183)

**<font color=#1a73e8>作者：</font>** Madeleine Grunde-McLaughlin, Hafsah Usman, Daniel Mitroshkov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When an AI agent executes an underspecified task, it embeds choices that may contradict unarticulated user context and preferences. However, interrupting the user for clarification on all such decisions is untenable. How might agents communicate impactful, but unexplored, paths to the user after execution? To investigate, we first distill a design space for communicating alternative paths, supporting the generation of new systems and structuring dimensions of future study. We then measure the impact of one vital design space dimension on user comprehension: the number of alternatives displayed. Through a user study (n=48) in the data analysis domain, we find that participants rarely consider alternative paths of their own volition, but AI overreliance reduces when alternative paths are visualized for them. By revealing paths the agent did not take, we demonstrate how users can better interpret results and incorporate personal context.

---


### 67. [Statistical Machine Learning for Medicinal Plant Leaves Classification](https://arxiv.org/abs/2611.04193)

**<font color=#1a73e8>作者：</font>** Jayani P. Gamage, Thiyanga S. Talagala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medicinal plants are usually identified using practitioners' experience, but reproducible, image based methods can complement this knowledge. We present MEDIPI (MEDIcinal Plant Identification), a statistical machine learning approach that classifies medicinal plant leaves from photographs. From each leaf image we extract 52 interpretable features covering shape, texture, color, and a new scagnostics category. We then classify leaves using a three level hierarchy: shape, then edge type, then species. We also release MedLEA, an open R package with 1,099 leaf images of 31 Sri Lankan medicinal plant species. On this dataset, a hierarchical Random Forest achieved the best overall accuracy (100%) in our comparison of hierarchical and non-hierarchical approaches and eight algorithms: Random Forest, XGBoost, Gradient Boosting, linear discriminant analysis, k-nearest neighbor, support vector machine, probabilistic neural network, and artificial neural network. Adding texture, color, and scagnostic features to shape features raised shape level accuracy from 90% to 97%. Linear discriminant analysis plots show how the trained model separates leaf shapes. Accuracy dropped sharply (23-50%) when training and test data came from different datasets, so generalization across datasets remains a challenge.

---


### 68. [SettleSplat: Monocular Gaussian Mapping under In-View Scene Changes](https://arxiv.org/abs/2611.04195)

**<font color=#1a73e8>作者：</font>** Anh Thuan Tran, Xiyun Song, Yubin Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online 3D Gaussian mapping enables fast and high-fidelity novel view synthesis, with broad applications in augmented reality, robotics, and autonomous systems. However, many current methods assume static scenes or filter out dynamics as outliers. In this paper, we study in-view scene changes where objects are manipulated in front of the camera within a single online sequence, unlike prior works that detect changes outside the camera view or between separate captures. This setting entangles transient and persistent dynamics, as objects can be distractors while moving and persistent once they settle. While recent studies start to address distractors by removing them for clean static background, in-view scene changes remain underexplored. To resolve this, we present SettleSplat, a monocular mapping system that maintains up-to-date 3D Gaussian maps under such changes. Specifically, we lift coarse per-pixel uncertainty into Gaussian dynamicity field, then prune transient ones. For persistent changes, we derive geometric contradictions weighted by parameter-free rendered depth uncertainty to separate true changes from under-optimized regions. On Bonn and Co-Fusion, SettleSplat achieves consistent 3D Gaussian maps, outperforming current baselines on both full images and change regions while maintaining comparable speed.

---


### 69. [An Information Budget for Label-Noise Memorization, and What Statistical Complexity Tracks: A Study with Multilayer Perceptrons](https://arxiv.org/abs/2611.04199)

**<font color=#1a73e8>作者：</font>** Nancy Baygorrea C., Otávio da Fonseca Martins Gomes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How much label noise has a network memorized, and when? We study a multilayer perceptron and what statistical complexity adds to a description of its predictions. Standard identities decompose predictive information into signal, memorization, and heterogeneity. The memorization term vanishes in the population under the stated noise-independence condition. A Fano-type bound relates it to training accuracies, but the memorized fraction M provides no upper bound. Across 89 MNIST runs with ten pre-specified hypotheses (five supported, four unsupported, one not testable), normalized memorization information rose with M on training samples, remained near zero on held-out samples with fresh noisy labels, and was close to its Fano bound. Unlike raw M, it has a zero population null under the independence condition and chance correction largely removed this difference. When every label was replaced by an incorrect class, test accuracy fell to 0.5%, yet predictions retained information about the true class. Mean statistical complexity peaked before memorization at corruption rates up to 40%. At higher rates, its peak fell within the memorization phase, near the epoch when mean training confidence reached 0.6 and the two could not be separated. As a stopping rule, it matched established rules only at low noise and detected corrupted samples less well than simple label-free scores. An exploratory extension of 280 runs covering Fashion-MNIST, pair-flip noise, and four training variants yielded similar results under uniform noise, but not pair-flip noise, where complexity peaked within two epochs. Conclusions are limited to this architecture, two small datasets, and synthetic noise.

---


### 70. [Impact of Input Resolution in Mammographic Mass Detection: A Controlled Multi-Architecture Study](https://arxiv.org/abs/2611.04200)

**<font color=#1a73e8>作者：</font>** Kaan Buyukdemirci, Emine Ulku Saritas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep-learning-based mass detectors usually downsample mammograms, trading fine image detail for lower computational cost. However, published studies cannot reveal how much accuracy this trade-off sacrifices, since they also differ in architecture, preprocessing, and evaluation protocol. In this work, we isolated the effect of input resolution in a controlled study on the VinDr-Mammo dataset, training 18 detectors at six input resolutions ranging from 512 x 416 to 1600 x 1280 pixels, for 108 model-resolution combinations. Whole mammograms were resized without cropping or tiling. For each model, preprocessing, model initialization, augmentation, and evaluation procedures were kept fixed across resolutions. Detection accuracy was evaluated by mAP50 on the 219 mass-positive images of the official test split, and 57 combinations with test mAP50 of at least 0.60 were analyzed. From the lowest to the highest resolution, median mAP50 rose from 0.626 to 0.660 and the best mAP50 from 0.670 to 0.709. The best result, achieved by DINO with a ConvNeXt-S backbone, is the highest mAP50 reported to date on mass-positive VinDr-Mammo images. Gains were concentrated in small masses: for the smallest third of lesions, median mAP50 rose by 0.074 (from 0.367 to 0.441), compared with 0.007 and 0.032 for medium and large masses. Median training time increased from 0.45 to 1.40 h, and median inference time from 23.6 to 113.7 ms per image. Therefore, higher input resolution mainly benefits the small masses that are hardest to detect, at a computational cost that remains practical.

---


### 71. [Toward User-Centered Agentic Recommendation: When Does Platform Competition Benefit Users?](https://arxiv.org/abs/2611.04203)

**<font color=#1a73e8>作者：</font>** Kehan Zheng, Deyao Hong, Qian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional recommender systems operate within platform-specific catalogs, limiting access to potentially valuable resources across platforms. We propose user-centered agentic recommendation, a paradigm in which user agents compare recommendations from competing platform agents, and formalize their interaction as a repeated game. Platforms strategically modify descriptions without changing intrinsic item value, while each user agent assesses platform credibility using feedback from consumed items only. Our analysis shows that expanded resource access need not improve user welfare: strategic misrepresentation and limited verification can offset the benefits of platform competition. We quantify when platform credibility assessment allows users to benefit from broader access despite strategic exaggeration. Our analysis identifies resource and reporting conditions that guarantee higher average welfare than the original platform with an interaction budget linear in platform count. Experiments on synthetic and Amazon-grounded markets show that credibility assessment can improve finite-horizon utility, while its benefits depend on market size and mechanism parameters.

---


### 72. [LiSA: Linear Stochastic Attention for Long-Range Visual Modeling](https://arxiv.org/abs/2611.04216)

**<font color=#1a73e8>作者：</font>** Sahar Dastani, Fereshteh Shakeri, Samuel Barbeau 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-attention has become the standard for modern sequence modeling, enabling Transformers to model long-range dependencies across a wide range of modalities. Despite these advances, its quadratic cost with respect to sequence length remains a significant computational bottleneck. Recent work addresses this limitation by introducing linear variants of self-attention, namely with kernel approximations of the softmax operator. However, their first-order aggregation restricts expressivity and struggles to capture higher-order structure. We propose Linear Stochastic Attention (LiSA), a linear attention plug-in module that enables higher-order token interactions via a stochastic diffusion process based on truncated random walks. LiSA incorporates adaptive locality, favoring semantically similar neighbors to preserve fine-grained structures, while maintaining stable and efficient training. We conduct extensive experiments on classification, semantic segmentation, and object detection tasks and show improved results over state-of-the-art methods.

---


### 73. [Reliability-Role Collaborative Learning for Semi-Supervised Cardiac Image Segmentation](https://arxiv.org/abs/2611.04219)

**<font color=#1a73e8>作者：</font>** Zhongrui Xie, Wenfeng Zhang, Wei Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised cardiac image segmentation aims to exploit abundant unlabeled images together with limited annotations, but the reliability of pseudo-label supervision is highly uneven across spatial regions.
In a dual-network setting, interior regions are usually more stable, whereas boundary regions, low-confidence areas, and disagreements between networks can introduce noisy supervision.
However, existing methods typically impose uniform supervision on all unlabeled pixels, overlooking reliability differences and limiting discriminative learning in challenging areas.
To address this issue, we propose R2CL (Reliability-Role Collaborative Learning), a framework for semi-supervised cardiac image segmentation.
R2CL models confidence relationships between two networks to assign roles to unlabeled regions: mutually uncertain regions are used for entropy regularization, confidence-discrepant regions for directional knowledge transfer, and mutually confident regions as reliable supervision anchors.
Reliability-Role Mixed Cross Learning (RR-MCL) implements these roles through region-mixed training, directional cross-network supervision, and entropy regularization over mutually uncertain regions.
Reliability-Transition Prototype Contrastive Learning (RT-PCL) constructs query features from foreground-adjacent reliability-transition regions and learns network-specific class prototypes from mutually confident regions, improving feature discrimination around ambiguous boundaries.
High-confidence Context Refinement (HCR) exploits reliable interior pixels and trusted dense blocks within mutually confident regions to complement stable contextual supervision.
R2CL achieves stable improvements in region-overlap and boundary-related metrics across multiple datasets, with more evident advantages on the foreground-sparse MVAA-CT dataset.

---


### 74. [Mamba3R: Fixed-Capacity Selective State Memory for Long-Sequence 3D Reconstruction](https://arxiv.org/abs/2611.04221)

**<font color=#1a73e8>作者：</font>** Zhenxiang Xiong, Tianchen Deng, Nailin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction must maintain geometric quality over long inputs within a fixed GPU budget. A pretrained recurrent model provides bounded state, but freezing its backbone also fixes its learned state-observation interactions. We introduce Mamba3R, a jointly designed state-memory adapter that provides a trainable adaptation path without updating the backbone or task heads. A selective state-space mixer jointly transforms native state features and a fixed-capacity auxiliary memory, explicit read and write paths carry information across frames, and a decomposed feedback path regulates what the added memory feeds back. Only 1.28 million adapter parameters are trained. Under a shared periodic-reset protocol, it lowers trajectory error and improves accumulated surface and depth accuracy over recurrent baselines on public indoor and outdoor datasets and robot-recorded traversals, gaining up to 40 percent on one metric. Matched comparisons support both the choice of the mixing operator and the utility of carrying the auxiliary memory across frames. Allocated memory remains unchanged and throughput moves by at most 1.4 percent from one to two thousand frames. Replaying its recorded traversals offline, the platform's RTX 4060 averages 11.7 frames per second within 5.1 GiB with the same checkpoint, a mean throughput covering the 10 Hz sensor rate.

---


### 75. [DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?](https://arxiv.org/abs/2611.04228)

**<font color=#1a73e8>作者：</font>** Yang Chen, Bin Wen, Danyang Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent multimodal agents have shown promising progress in embodied planning and web interaction. However, existing evaluations often rely on simplified tasks with limited combinatorial structure, leaving it unclear whether current agents can robustly integrate perception and reasoning for multi-goal planning under temporal, physical, and multimodal constraints. We introduce DualWorldBench, a unified benchmark for evaluating agent planning under controlled symbolic--temporal and grounded--topological complexity. Built around a shared pickup--delivery interface, DualWorldBench consists of three complementary components: TextWorld, which isolates symbolic planning under varying task compositions and release dynamics; SimWorld, which evaluates grounded path planning under controlled topological variation with text, image, or multimodal inputs; and DualWorld-VQA, a diagnostic suite spanning perception, scene understanding, and planning. Experiments reveal a common gap between local understanding and globally consistent planning. In TextWorld, agents struggle to derive optimal task sequences under interacting temporal constraints; in SimWorld, grounded observations are not reliably converted into feasible action sequences. DualWorld-VQA further confirms that perception and topology understanding do not necessarily translate into constrained planning. Together, these results identify the central challenge as composing symbolic or grounded evidence into globally feasible and efficient multi-goal plans. These findings establish DualWorldBench as a challenging testbed for agents with tighter perception--reasoning--planning integration. All datasets and code are publicly available at our project website this https URL.

---


### 76. [Exact Optimality Certification of QPLIB 2096 through Complete Set Partitioning](https://arxiv.org/abs/2611.04230)

**<font color=#1a73e8>作者：</font>** Jingyang Du, Zixiong Yi, Yang Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an exact computational proof that the frozen QPLIB_2096 instance has global minimum 7,025,720. The solution and certification approach was explored and refined through ZiYor, a self-evolving AI system. The authors provide the mathematical account and exact validation reported here. The original formulation has 300 binary variables, 6,900 triangle inequalities, and 25 nonconvex quadratic constraints. A coefficient-level reconstruction identifies its variables with the unordered pairs of 25 items. The triangle inequalities encode partitions, while each quadratic constraint becomes a bound on the total weight of edges incident to one partition block. This yields a set-partitioning formulation over all capacity-feasible blocks, with a separate edge-cost graph determining the objective. Exact enumeration examines 245,505 subsets of sizes one through six and finds 14,981 feasible blocks. Every six-element subset is infeasible; nonnegative capacity weights exclude all larger blocks. An integer price vector satisfies the dual inequality for every feasible block and has sum 2,229,456. Subtracting this sum from the total objective edge cost 9,255,176 gives a lower bound of 7,025,720, attained by the supplied six-block partition. Fresh solver-free checks validate the candidate against both frozen model formats and verify the certificate. The result is an instance-specific optimality proof with an exact primal and dual witness; no cross-instance performance conclusion is drawn.

---


### 77. [LINDA: Low Resource Foot Ulcer Segmentation using Local Similarity and Iterative Neural Dynamics](https://arxiv.org/abs/2611.04233)

**<font color=#1a73e8>作者：</font>** Trishaani Acharjee, Sudip Chakrabarty, Rajdeep Chatterjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foot ulcers are a leading cause of lower limb amputation, and the highest burden often falls on low and middle income regions where specialists and computing hardware are both scarce. Wound monitoring tools are most useful there when they are accurate yet small enough to run on ordinary devices, but accuracy usually comes from heavy networks. We present LINDA, a compact model that grounds segmentation in an explicit structural prior instead of raw intensity. A Local Self-Similarity (LSS) map, computed directly from the image and stable under local lighting changes, is fused into a ResNet-34 encoder, and a small Liquid Time-Constant module refines the boundary over four iterative steps. With every model trained under one protocol on the FUSeg 2021 dataset, LINDA obtains the best Dice (86.68\%), IoU (79.67\%), and boundary accuracy (HD95 6.37 pixels) in our comparison while using only 25.70M parameters, fewer than the U-Net and transformer baselines. As the LSS map is a fixed function of the input, it exposes the structural cues the model follows in a readable form. Together this makes LINDA an accurate, inspectable, and lightweight option for wound assessment in resource-constrained care.

---


### 78. [TCINet: Tissue-Conditioned Adaptive Cross-Branch Interaction Network for Nuclei Instance Segmentation](https://arxiv.org/abs/2611.04235)

**<font color=#1a73e8>作者：</font>** Zhenghang Qian, Yang Liu, Yanzhi Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Separating touching nuclei requires local boundary detail, while cell type classification requires broader morphological context. These requirements also vary with the surrounding tissue environment. We propose the Tissue-Conditioned Adaptive Cross-Branch Interaction Network (TCINet), a single-stage model with Task-Specific Feature Adapters (TSFA) and Tissue-Conditioned Task-Aware Cross-Branch Interaction (TC-TACBI). TSFA produces branch-specific features at skip connections, and TC-TACBI controls three asymmetric paths among nucleus-presence (NP), horizontal-vertical (HV), and nucleus-type (NT) branches using predicted tissue probabilities. On PanNuke under standard three-fold cross-validation, TCINet achieves multiclass and binary panoptic quality scores of 0.519 and 0.692, respectively. Zero-shot tests on MoNuSeg yield a detection F1 score of 0.876. On PanNuke fold 0, adding TC-TACBI increases mPQ from 0.505 to 0.525. Code is available at this https URL.

---


### 79. [LIRA: A More Interpretable Dynamic Loss-Informed Rank Allocation for Low-Rank Adaptation](https://arxiv.org/abs/2611.04239)

**<font color=#1a73e8>作者：</font>** Sihao Wang, Bozheng Li, Xuemiao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) has become a widely used parameter-efficient fine-tuning method for large pretrained models. However, standard LoRA typically assigns a fixed rank profile despite layer- and stage-dependent adaptation needs, while recent adaptive-rank variants often rely on heuristic or first-order signals that provide only an indirect link between rank reallocation and local loss behavior. This leaves the rationale behind each rank reallocation insufficiently interpretable. Motivated by this gap, we propose LIRA (Loss-Informed Rank Allocation), a dynamic-rank LoRA method designed to make online rank reallocation more interpretable. LIRA scores each layer by the estimated magnitude of the local loss perturbation associated with its recent LoRA-factor movements under a second-order approximation, making the basis for each rank change interpretable term by term. By periodically applying DELTA (Displacement-Evaluated Loss-Trajectory Allocation), a displacement-based algorithm for LoRA rank reallocation, LIRA produces discrete effective ranks under matched budgets while remaining compatible with standard (A,B) adapters. On RoBERTa-base GLUE under the La-LoRA/LoRA protocol, LIRA outperforms the uniform-LoRA and adaptive-rank baselines reported under this protocol; Trajectory EMA attains performance competitive with Fixed-point Fisher at lower estimation cost.

---


### 80. [VerfGraph: Efficient Zero-Knowledge Verifiable Graph Query Evaluation System](https://arxiv.org/abs/2611.04240)

**<font color=#1a73e8>作者：</font>** Tianyi Ma, Yuncong Zhang, Yuanzhuo Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph databases are often used to manage relationship-rich data, whose graph structure and attributes may be sensitive. In many applications, a database owner or a service provider evaluates queries over a private graph for a client. Because the graph cannot be fully disclosed and independently re-executing the query may be impractical, the client cannot directly verify the returned result. This creates a need for verifiable graph query evaluation that preserves data confidentiality. We present VerfGraph, a zero-knowledge system for verifiable graph query evaluation, which enables a client to verify that the query result was correctly computed over a committed graph data, without revealing private graph records or intermediate query values beyond the public inputs and what is implied by the query result. Building on the expansion-centric model introduced by the state-of-the-art zero-knowledge verifiable graph query evaluation system ZKGraph (ICDE'26), VerfGraph achieves more efficient and expressive zero-knowledge verifiable graph query evaluation by advancing design in two key ways. First, we propose novel operator-proof methods for core expansion and shortest-path operations that reduce costly sorting and comparison checks and eliminate edge canonicalization for bidirectional expansion. Furthermore, we introduce correctness proofs for count and weighted shortest-path operators, broadening the class of graph queries that can be verified. We evaluate VerfGraph using the LDBC Social Network Benchmark. Compared with ZKGraph on complex IC queries, VerfGraph achieves $33.9\times$-$59.7\times$ speedups in proof generation and reduces peak prover memory by factors of $4.5\times$-$6.6\times$, while maintaining millisecond-level verification and producing sub-MB proofs.

---


### 81. [Improving Diffusion-Based Augmentation for Data-Scarce Image Classification via Mask-Guided Reference Attention and Repulsive Noise Optimization](https://arxiv.org/abs/2611.04242)

**<font color=#1a73e8>作者：</font>** Hyun-Jic Oh, GaYeon Koh, Won-Ki Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based data augmentation has emerged as a powerful strategy for addressing data-scarce image classification. Recent pipelines typically adapt a pretrained text-to-image diffusion model to a limited number of class examples and subsequently sample synthetic images using diverse textual prompts. However, in extreme data-scarce regimes such as long-tailed single-sample settings, this approach suffers from a dual failure mode: the generated samples often lack discriminative foreground details crucial for classifier training, and the adapted class prior can bias the early denoising process, causing output images to exhibit similar patterns despite varying text prompts. To overcome these limitations, we propose a sampling-side framework of two complementary components that simultaneously enhance fine details and diversity. First, Mask-Guided Reference (MGR) Attention updates only foreground value tokens with reference features via zero-shot segmentation, limiting reference influence to the target object and mitigating excessive global feature injection. Second, Repulsive Noise Optimization (RNO) encourages initial noise trajectories to diverge from dominant generative modes of the adapted model, enabling target prompts to express broader contextual variation. Extensive evaluations show consistent improvements, with the largest gains in long-tailed single-sample settings of up to 2.50 and 2.94 points on CUB-LT IF100, and further robustness across few-shot and background-shift evaluations.

---


### 82. [P-SER: Physical Consistency-Constrained Scattering Expandable Representation for Class-Incremental HRRP Target Recognition](https://arxiv.org/abs/2611.04254)

**<font color=#1a73e8>作者：</font>** Fangyi Wang, Peng Zhao, Haipeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution range profiles (HRRPs) provide compact radar target representations but exhibit strong aspect sensitivity, complicating class-incremental recognition when historical data are unavailable. Changes in viewing aspect shift scattering-peak locations and amplitudes, while reflector groups may produce responses resembling ships. Existing dynamic expansion methods can also incur substantial parameter and memory overhead. To address these challenges, we propose P-SER, a Physical Consistency-Constrained Scattering Expandable Representation framework for exemplar-free class-incremental HRRP recognition. P-SER reconstructs dominant scattering points from complex-valued sum- and azimuth-difference-channel HRRPs and observation geometry. The reconstructed spatial structure, target extent, and energy distribution are used to derive class-level scattering prototypes and sample-level saliency priors, providing physically grounded constraints for feature learning and old-class knowledge retention. A primitive scatterer dictionary further characterizes local strong-scattering mechanisms and calibrates uncertain ship--reflector predictions at inference. Meanwhile, lightweight residual adapters are incrementally introduced into a shared HRRP backbone to learn new classes with limited model growth. Experiments on simulated and measured HRRP datasets show that P-SER delivers competitive recognition performance without retaining old-class exemplars, while maintaining physical consistency, interference robustness, knowledge retention, and model scalability.

---


### 83. [OmniST: Topology-Invariant Spatiotemporal Forecasting with Guaranteed-Coverage Uncertainty at Unseen Sensor Locations](https://arxiv.org/abs/2611.04256)

**<font color=#1a73e8>作者：</font>** Praveg Vashishtha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard spatiotemporal graph convolutional networks need a fixed-size adjacency matrix, coupling model weights to a specific sensor count N; they cannot produce any output at a sensor absent from training. We present OmniST, a topology-invariant forecaster whose computation has zero structural dependency on the number of nodes, and which, composed with inductive split-conformal calibration, gives distribution-free, coverage-guaranteed prediction intervals at arbitrary (including never-seen) sensor locations, preserving that guarantee as sensors are added or removed. Topology invariance follows from coordinate-based tokenization, k-nearest-neighbor attention from geographic coordinates at each forward pass, and per-node temporal processing via a bidirectional GRU. On real Delhi air-quality data (37 stations, 2019-2023), OmniST attains a 30-day PM2.5 MAE of 31.0 ug/m3 and degrades at most 1.1 percent when 40 percent of stations are removed. Its inductive forecasts at unseen stations beat nearest-neighbor interpolation (about 12 percent) and a learned kriging GNN (IGNNK, about 21 percent), and, unlike either, carry a finite-sample coverage guarantee. The guarantee holds at 90 percent or above under 30-50 percent node dropout across four real datasets over three domains (Delhi and Beijing air quality, NOAA GHCN weather, Caltrans PeMSD7-M traffic), and still holds at 325 real sensors (full PeMS-BAY). We also fix a temporal-drift failure: static conformal under-covers over time (about 0.50 late), but a rolling adaptive-conformal estimator restores target coverage (0.89 overall, 0.96 late) at the cost of wider intervals.

---


### 84. [ProGeo-RC: Prototype-guided Semantic Reliability and Geometric Error Calibration for Semi-supervised Cardiac Image Segmentation](https://arxiv.org/abs/2611.04257)

**<font color=#1a73e8>作者：</font>** Yunfei Zhu, Wenfeng Zhang, Pan Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised medical image segmentation aims to train reliable segmentation models using limited labeled data and abundant unlabeled data. However, existing methods typically rely on prediction confidence or model consistency to estimate pseudo-label reliability, but these criteria are insufficient to characterize both semantic reliability and geometric plausibility. To address this issue, we propose ProGeo-RC, a prototype-guided semantic reliability and geometric error calibration framework for semi-supervised medical image segmentation. ProGeo-RC consists of two key modules: Prototype-guided Semantic Reliability Estimation (PSRE) and Structured Semantic-Geometric Error Calibration (S-SGEC). PSRE uses probabilistic class prototypes to estimate the semantic reliability of unlabeled predictions and calibrate pixel-wise teacher pseudo labels, while S-SGEC introduces signed-distance-field-based geometric constraints to refine ambiguous boundaries and suppress spurious foreground responses outside target structures. Experiments on the ACDC and MVAA-CT datasets show that ProGeo-RC achieves better performance compared with representative semi-supervised segmentation methods. Under the 10\% labeled setting on ACDC, ProGeo-RC improves DSC and Jaccard by 0.37\% and 0.49\% over the corresponding second-best results, while reducing 95HD and ASD by 0.61 and 0.21, respectively. These results indicate that joint semantic reliability estimation and geometric error calibration can provide more reliable pseudo supervision for semi-supervised medical image segmentation.

---


### 85. [Neologism Inoculation Prompting](https://arxiv.org/abs/2611.04260)

**<font color=#1a73e8>作者：</font>** David Demitri Africa, Cameron Holmes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inoculation prompting is a method to reduce undesired behaviours such as reward hacking in frontier models. It works by training a model on harmful examples under a prompt that specifies the undesired behaviour, which reduces the model's tendency to exhibit it unless prompted. However, the inoculation prompt is written in plain English, so any user can re-elicit the behaviour easily. We introduce neologism inoculation prompting (NIP), which replaces the English prompt with a new token that is trained on the frozen model and removed at deployment. NIP outperforms other inoculation methods, and performs competitively with gradient routing despite being simpler. It also works on reward hacking, but fails on sycophancy and harassment. Using control tokens and analyses of activations, we identify the mechanism for this as NIP hiding the harmful behaviour behind an unreachable region of model inputs, rather than deleting it. More broadly, our work suggests that neologisms can be a powerful way to carve out and shape access to behaviours that are undesired or harmful.

---


### 86. [Deep Learning Compilers: Architecture, Optimization, and Empirical Characterization](https://arxiv.org/abs/2611.04273)

**<font color=#1a73e8>作者：</font>** Jinghao Wen, Ruixuan Wang, Xun Jiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep learning (DL) models become increasingly complex and hardware architectures grow more heterogeneous, DL compilers play a critical role in optimizing computational efficiency and enabling scalable deployment. This paper presents a systematic analysis of DL compilers, covering their architectural evolution, compilation workflows, optimization techniques, and emerging research directions. We organize DL compiler architectures into frontend, middle-end, and backend stages, emphasizing the role of the middle-end in connecting high-level model representations with hardware-specific optimizations. We further examine representative DL compilers and recent optimization techniques across different compilation stages. Beyond architectural and technical analysis, we conduct an empirical evaluation of compiler behaviors to investigate the effectiveness of graph optimization, compilation overhead, and dynamic-shape handling. Experiments using PyTorch/TorchInductor on an NVIDIA RTX A6000 demonstrate that compiler benefits depend strongly on workload characteristics, with speedups of up to 8.21\times for fusion-friendly computation graphs, while other workloads exhibit limited improvements. Our results further reveal that compilation overhead can require thousands of executions to amortize, and dynamic-shape compilation reduces cumulative shape-transition costs by approximately 70\% at the expense of modest steady-state performance degradation. By combining systematic architectural analysis with quantitative experimental evidence, this work provides insights into the design, optimization, and practical deployment of modern DL compilers.

---


### 87. [Bidirectional Centered Score Matching for Discrete Diffusion Distillation](https://arxiv.org/abs/2611.04279)

**<font color=#1a73e8>作者：</font>** Peng Tu, Baoyou Chen, Haoyuan Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models with parallel decoding are often distilled using token-wise KL objectives. Although token-wise KL exactly matches the corresponding product-form block distributions, its probability-space optimization geometry and teacher-only candidate truncation may provide insufficient supervision under aggressive few-step distillation. Concrete Score Matching (CSM) provides an alternative within-position objective by aligning relative logit geometry, but its complete pairwise form incurs $\mathcal{O}(|\mathcal{V}|^2)$ complexity. We propose Bidirectional Centered Score Matching (BCSM), an efficient within-position distillation objective that constructs an $\mathcal{O}(K)$ bidirectional active set, reduces pairwise comparisons to $\mathcal{O}(K^2)$, and factorizes them into an $\mathcal{O}(K)$ objective. We further introduce cross-timestep transition alignment. Experiments demonstrate strong quality--efficiency trade-offs, including up to $6\times$ NFE reduction with a 16.9\% relative HumanEval gain and a 15.1\% relative MMMU gain at single-step inference.

---


### 88. [OmniScribble: Mixed-Initiative Authoring of Animated Sketches through Inspectable and Repairable AI Decisions](https://arxiv.org/abs/2611.04284)

**<font color=#1a73e8>作者：</font>** Hien Trinh, Tan-Hiep To, Trung-Nghia Le  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-assisted creative tools reduce the effort of authoring content, but delegating creative decisions to AI can make it difficult for authors to understand, correct, or redirect work. We present OmniScribble, a system for animating multi-object sketches that treats object decomposition and motion planning as editable artifacts. Rather than generating animation end-to-end, OmniScribble presents AI proposals at verification checkpoints, where authors can accept, repair, or regenerate them. Both manual and AI-assisted authoring operate on the intermediate representation and rendering pipeline, allowing us to isolate AI delegation. In a within-subject study with eight participants, AI-assisted authoring yielded a median within-participant reduction in completion time of 71.4\%, while perceived control and motion-intent alignment remained high. Interaction traces and interviews show that participants adapted to AI errors by repairing local issues, regenerating mismatches, and accepting proposals. These findings suggest that inspectable, repairable delegation enables generative automation while maintaining control over the outcome.

---


### 89. [When Debate Amplifies Risk: Social-Bias Vulnerabilities in Multi-Agent Safety Deliberation](https://arxiv.org/abs/2611.04289)

**<font color=#1a73e8>作者：</font>** Qinghua Mao, Xi Lin, Yuxin Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented Web applications increasingly employ multi-agent debate (MAD) to aggregate conflicting, noisy, and heterogeneous information, yet deliberation is fundamentally a social process susceptible to interpersonal dynamics. When retrieved Web sources contain latent hazards alongside safe factual content, social biases such as conformity pressure and authority deference can override evidence-grounded safety boundaries. In this work, we investigate whether the social structure of deliberation can paradoxically amplify latent Web safety risks. We introduce SafeConflict-Bias, a controlled counterfactual diagnostic protocol spanning six core Web risk categories, which holds queries and retrieved evidence strictly invariant while isolating conversational majority sway, authority cues, and confidence asymmetry. Empirical evaluation across diverse proprietary and open-source backbones reveals that while isolated models reliably reject unsafe guidance, standard MAD catastrophically capitulates to social pressure---surging unsafe adoption from 0.0\% up to 100.0\% and systematically silencing safe minority evidence. To resolve this systemic fragility without retraining or debate regeneration, we propose RiskTrace-Debias, an inference-time auditing framework uniting evidence-first precommitment, social-metadata masking, and consistency-gated arbitration. RiskTrace-Debias suppresses worst-case unsafe adoption to $\le 2.0\%$ across all architectures without inducing over-refusal, while generating verifiable provenance traces to audit interpersonal manipulation in Web deliberation.

---


### 90. [The Native Menace: Host-to-Browser Cross-Boundary Attacks via Native Messaging](https://arxiv.org/abs/2611.04291)

**<font color=#1a73e8>作者：</font>** Jyotirmay Chauhan, Rownak Islam, Jason Polakis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern browsers are complex software platforms that users can customize through browser extensions to further expand their functionality. Extensions derive their functionality from privileged browser APIs that expose powerful capabilities. Prior work has extensively studied how malicious webpages or extensions can target those capabilities. However, prior research has overlooked the NativeMessaging API, which allows extensions to create a communication channel that bridges the gap between web content rendered in the browser and native apps running on the user's machine. This API enables workflows that cross the browser's boundary to perform critical operations (e.g., digital signing) or exchange sensitive data (e.g., credentials). In this paper, we conduct the first, to our knowledge, empirical security analysis of NativeMessaging, and present a novel attack that allows a non-privileged malicious native app to misuse browsers' native messaging capabilities to stealthily intercept sensitive communications or launch confused deputy attacks against other native apps. To demonstrate the significant risk introduced by native messaging, we present a series of concrete attacks against popular and critical apps (e.g., 1Password, the European Union's eID system, Google Drive), whose browser extensions have more than 532 million cumulative downloads. Our attacks have severe ramifications, including full password vault leakage, and arbitrary document signing in governmental workflows. Fundamentally, these attacks are possible due to native messaging being built on top of an untrusted communication channel without providing a root of trust or enforcing some form of client attestation. Accordingly, we propose a straightforward mitigation technique of message encryption with out-of-band secret sharing, to prevent our attacks.

---


### 91. [Reciprocity Can Erase Direction:tructural Boundaries and Controlled Utility of Magnetic Graph Networks](https://arxiv.org/abs/2611.04295)

**<font color=#1a73e8>作者：</font>** Dawei Han, Zicheng Wang, Yaoxing Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Magnetic graph networks encode direction through phase, but a learned graph can erase the intended directional mechanism before prediction. We characterize this failure for support-based magnetic Laplacians. Exact identities relate imaginary energy and distance from zero phase to amplitude-weighted reciprocity. Top-$k$ selection forces complete collapse when the observed-node count satisfies $m\leq k+1$, and dense support imposes a lower bound on reciprocal-arc fraction. We then construct paired propagation examples with identical node features and symmetric amplitudes but opposite labels, giving a provable chance-level limit for direction-erasing representations. In 72 fixed neural fits, support phase achieved test AUROC 1.0000 on a unilateral ring but 0.5000 on reciprocal ring and complete supports; continuous score phase and a real directed comparator achieved 1.0000 throughout. All models solved the direction-free control. These are oracle-direction mechanism tests, not evidence of learned clinical direction. In the preserved public DeepDRiD development study, continuous phase was active but its robustness difference from zero phase was only $+0.0036$ (descriptive 95\% interval $-0.0014$ to $+0.0095$) on validation patients used for checkpoint selection. The contribution is a structural and experimental framework for distinguishing erased direction from unestablished task utility. It provides a precise circumstance in which magnetic phase preserves useful information, without asserting universal or clinical superiority.

---


### 92. [SEAM: Situated Executable Associative Memory for a Co-located Community](https://arxiv.org/abs/2611.04296)

**<font color=#1a73e8>作者：</font>** Keru Wang, Michael Xu, Ken Perlin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In groups, knowledge is distributed among individuals, and how it is brought together depends on social ties. Taking inspiration from how a single mind recalls and reacts to memories and current stimulus, we build a shared memory that does this for a community, prototyped as a social app, SEAM. Members post arbitrary moments; SEAM works out how fragments relate, distills knowledge about the group, and replies in a situated and associative way. Some of these memories act as instructions that can alter how the system behaves, making it programmable by its members. We deployed SEAM to 46 people in a co-located community for two weeks of open-ended use, and ran a follow-up workshop with 14. Members shared their days, interrogated the memory, and instructed it to track routines and run games; replies introduced them to people and subjects they had never encountered. SEAM points towards communities where knowledge finds people.

---


### 93. [CLOCs-R: Radar-Assisted Camera-LiDAR Fusion for Long-Range Object Detection](https://arxiv.org/abs/2611.04300)

**<font color=#1a73e8>作者：</font>** Richard Beuck, John Nguyen, Sudip Dhakal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-range 3D object detection remains difficult for autonomous vehicles because LiDAR returns become sparse and camera evidence weakens with distance, while automotive radar keeps returning measurements far beyond both. We present CLOCs-R, an extension of the CLOCs candidate-level fusion framework that adds radar evidence to camera-LiDAR rescoring. Radar returns are accumulated over several sweeps, compensated for ego-motion, and associated with each pre-NMS 3D candidate through a range-dependent gate. Compact features summarizing support, Doppler speed and spread, range residual, and offset are then appended to every camera-LiDAR pair before a lightweight fusion network rescores the candidates. We first verify that our fusion implementation reproduces CLOCs on KITTI. We then evaluate on the daytime clear-weather subset of the aiMotive dataset, reporting distance-binned metrics out to 200 m with frozen SECOND and Cascade R-CNN detectors. Camera-LiDAR CLOCs improves on SECOND up to 50 m but degrades beyond it. A residual scoring variant, introduced post hoc, corrects SECOND's score instead of replacing it and recovers most of this loss. Radar consistently improves BEV AP at 30-50 m (0.857 to 0.870), but beyond 50 m its gain is small (+0.003 center-distance AP), within seed variation, and CLOCs-R with residual scoring is statistically tied with LiDAR-only SECOND. Our analysis attributes the limited long-range benefit to weak separation of true and false detections by radar features, scarce far-range training positives, poor camera evidence at distance, and missing LiDAR proposals that rescoring cannot recover. We report all as-designed and post hoc results side by side.

---


### 94. [Weather Adaptive Autonomous Driving](https://arxiv.org/abs/2611.04305)

**<font color=#1a73e8>作者：</font>** Nicholas Taylor, Alexander Picon, Sudip Dhakal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera object detectors lose recall in rain, fog, snow and sand, and the confidence threshold at which a detector is deployed decides how many objects it misses and how many false alarms it raises. We study how a frozen detector should make this decision in adverse weather. We first reproduce SeqCRC, a conformal object detector whose first step calibrates the confidence threshold by conformal risk control (CRC), and use that step, calibrated separately in each weather condition, as our baseline. With YOLOv8x it keeps the held-out miss fraction within a 20% budget in every DAWN weather bin, where a single global threshold fails in fog, but the false alarms it needs are an output rather than a choice: from 1.6 to 117 per image across DAWN and BDD100K conditions. We then propose a calibrated trade-off dial. One setting, $\lambda$, the number of false alarms accepted to avoid one missed object, selects the expected-cost-optimal decision rule: either one score threshold, or a per-detection rule that keeps a box when its calibrated probability of being a real object, estimated by gradient-boosted trees from the detector's own per-box outputs, is at least $1/(1+\lambda)$. F-score preferences map onto the same dial, and CRC applied to $\lambda$ itself is planned to restore a per-condition miss guarantee. The dial is fitted once on BDD100K train and graded only on BDD100K val and DAWN.

---


### 95. [What Is the Influence of Task Order in Continual Learning? An Empirical Study and Order-Aware Evaluation for Motion Forecasting](https://arxiv.org/abs/2611.04309)

**<font color=#1a73e8>作者：</font>** Zirui Li, Yunlong Lin, Haohan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aggregate scores for continual learning algorithms rest on a distribution over task orders that is rarely stated. We formulate algorithm comparison as an expectation over a declared order distribution, which separates training variation from order variation, and apply it to motion forecasting with four road-layout tasks from the INTERACTION dataset, all 24 task orders, four algorithms, and three training replicates (288 runs). Task order accounts for 65\% to 91\% of the variation in current-task error and backward transfer, and 90\% to 99\% of this order effect comes from the identity of the starting task: the smallest task cannot be learned from a cold start. Beyond the first stage, the order effect is comparable to training variability. In most orders, the leading algorithm in current-task error and backward transfer is within one replicate standard deviation of the runner-up. Backward transfer depends on the order mainly through its reference term, which weights the first task most heavily, so relative improvement and final error identify different leading algorithms for displacement error. A transition-direction descriptor computed from task statistics tracks the position of the smallest task, and weighting orders by it leaves the algorithm ranking unchanged. These results call for benchmarks that declare their order distribution and report order-resolved, starting-task-resolved, warm-start, and final errors alongside aggregate scores. The code and data are available \href{this https URL}{here}.

---


### 96. [Bilateral Protection for Private LoRA Inference with Intel TDX](https://arxiv.org/abs/2611.04311)

**<font color=#1a73e8>作者：</font>** Xiaodong Li, Mingyuan Ma, Dongbo Yan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud services using private low-rank adaptation (LoRA) must protect client inputs and outputs alongside owners' proprietary parameters and execute the approved adaptation. We design and implement a system for bilateral protection of private LoRA inference using Intel Trust Domain Extensions (TDX), connecting approved application identity to actual artifact consumption and adapter activation. The client and LoRA owner independently verify remote attestation, application identity, and binding to the actual Transport Layer Security (TLS) public key before releasing inputs and the weight-decryption key. A fixed read-only image and verified-byte consumption connect approved identities to inference objects, with all inference inside a trust domain. Experiments on real TDX hardware reject controlled application and boot-parameter modifications before secret release. Across 400 fixed dialogues, protected and native CPU inference in the same trust domain produce identical token sequences for all 400 pairs. Across 12 independent trust-domain boots, the steady-state service-to-native time ratio is 1.0094, with a 95% interval of [1.0064, 1.0126]. The system connects bilateral secret release, approved model use, and task-capability preservation, providing verifiable implementation and cost evidence for confidential inference with a public base and private adapter.

---


### 97. [Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI](https://arxiv.org/abs/2611.04315)

**<font color=#1a73e8>作者：</font>** Vishal Pramanik, Maisha Maliha, Susmit Jha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon multi-agent systems suffer from three tightly coupled failures: task drift, role drift, and state staleness. We test the hypothesis that these share a common representational cause: agent hidden states move away from the directions encoding the active task, assigned role, and current shared state. A pilot study over 14,832 annotated turns supports this: drifted turns collapse near-uniformly across all three anchor subspaces (pairwise r = 0.72-0.78). Existing methods address these failures separately, operating at the surface-text level or treating control directions independently. We introduce ATLAS (Algebraic Task-role Locking with Adaptive Spectral Memory), a training-free intervention acting on hidden states before a token is generated. ATLAS builds a positive-semidefinite anchor kernel over task, role, and state subspaces and steers hidden states toward their shared high-coherence eigendirections; a low-rank Gram decomposition keeps this tractable. Across long-horizon memory, state maintenance, tool use, least-privilege coordination, and embodied stress tests, ATLAS outperforms prompting, retrieval, memory, and activation-steering baselines. Against A-MEM it improves memory macro-average accuracy by up to 5.7 points and reduces write/read failures by up to 31.7%/24.8%; against MemoryArena-Agent it gains up to 4.8 points. It gains 10.7-12.1 points under perturbation, reaches 93.5% role consistency, and transfers to a 72B backbone (macro-average 61.0 vs. 56.2). Ablating the joint task-role-state span costs 7.2 points against 0.8 for a matched-rank random span, indicating these directions are functionally implicated, not incidental; supplying them by prompt or retrieval recovers 4.3 points less. ATLAS is therefore a representation-level controller for open-weight multi-agent systems, complementary to output-level protocols for black-box agents.

---


### 98. [SteelHuman: Predicting Operator Estimates of Steel-Scrap Composition from Sparse RGB Views](https://arxiv.org/abs/2611.04317)

**<font color=#1a73e8>作者：</font>** Jovan Kamchev, Zoran Ivanovski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Steel scrap composition estimation is an important part of yield planning and fair supplier compensation. Measuring the composition of a multi-ton pile is an inherently laborious process, so the assessment is often left to trained human operators. Recent works tackle composition-level tasks, but require structured acquisition and multi-stage preprocessing. We study a simpler approach to steel scrap load assessment by aggregating features from sparse, handheld views of the pile. On 600 out-of-fold piles, frozen DINOv2 tokens aggregated uniformly across views reach 13.4% total variation (TV) distance against operator estimates. Most remaining error lies in allocation among four thickness-defined heavy melting scrap (HMS) classes, yet image-dependent allocation reduces within-HMS TV from 25.1% under a training-set split prior to 11.2%. Due to the lack of public datasets and benchmarks for predicting composition, external evaluation relies on the public DOES dataset intended for classification. A classifier using the same frozen features reaches 93.97% accuracy, exceeding the published results we compare against. The composition model also aligns with related DOES categories without adaptation.

---


### 99. [CORA: Teacher-Guided Causal O-RAN Adaptation for Jamming Detection](https://arxiv.org/abs/2611.04330)

**<font color=#1a73e8>作者：</font>** Sneihil Gopal, Richard A. Rouil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In mission-critical networks, a missed jamming event is costlier than a false alarm, so detectors should favor recall, operate causally, and work without labeled attack data. Retrospective Key Performance Indicator (KPI) detectors meet the label-free requirement but rely on future context and cannot run in streaming operation. We present CORA, a teacher-guided reinforcement learning (RL) framework that transfers the hindsight of a retrospective detector to a causal one without labels during training or deployment. Offline, a retrospective KPI detector evaluated on unlabeled historical logs defines a recall-weighted reward for a masked controller that adapts the sensitivity, persistence, and grace of a causal KPI detector. At deployment, the teacher is removed and the frozen controller acts causally, with no ground-truth labels and no target-specific calibration. The design maps onto offline training in the Non-Real-Time RIC and causal control in the Near-Real-Time RIC of an Open Radio Access Network (O-RAN). Under leave-one-out transfer across ten 5G O-RAN testbed configurations, CORA reaches recall-oriented operating points on the deployable frontier that none of the evaluated baselines covers. A Proximal Policy Optimization (PPO) controller raises mean recall from 0.687 to 0.771 over a fixed default detector on all ten configurations, while a Deep Q-Network (DQN) achieves a comparable F2-score to the best teacher-selected static configuration, with 61% fewer false alarms. Removing the teacher lowers recall on every configuration.

---


### 100. [Mitigating Spatial Blindness in Multiple Instance Learning for Whole-Slide Image Analysis](https://arxiv.org/abs/2611.04337)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Jincheng Li, Xing Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide multiple instance learning can predict diagnostic and prognostic labels from tissue composition while making limited use of spatial organization. Providing coordinates or a graph does not establish that a trained predictor uses tissue neighborhoods. We examine this gap as spatial blindness and hypothesize that early composition learning can weaken supervision of a spatial pathway. We introduce ResTopoMIL, which freezes a learned composition predictor before training a graph residual with a coordinate-reassignment separation loss. Permutation and information analyses distinguish architectural symmetry, available spatial information and the proposed optimization mechanism. On a controlled spatial task, staged training achieved an AUC of 0.987, compared with 0.684 for the same jointly trained architecture. Performance remained high on a composition-only task. Across four WSI classification and five survival benchmarks, ResTopoMIL improved mean primary performance on eight tasks; four improvements remained significant after Holm-adjusted patient-cluster tests. Coordinate-free residual controls recovered some of the gains, while neighborhood destruction reduced performance close to the composition anchor. Neighborhood-preserving transformations and anatomy-stratified perturbations further characterized this dependence. These results support fixing a composition reference as a practical intervention for learning spatial corrections, while retaining additional appearance capacity as a contributing explanation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-280](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
