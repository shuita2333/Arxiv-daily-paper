# 📦 其他研究 | 2026年06月11日

> 本类共 **269** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-269](./part-06.md)

---

### 101. [RealMath-Eval: Why SOTA Judges Struggle with Real Human Reasoning](https://arxiv.org/abs/2606.10254)

**<font color=#1a73e8>作者：</font>** Yiteng Mao, Kenan Xu, Yijia Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have achieved near-perfect performance in \emph{solving} high-school mathematics, their ability to \emph{evaluate} the diverse reasoning processes of real human students remains under-examined. To bridge this gap, we introduce \textbf{RealMath-Eval}, a rigorously annotated benchmark of 224 real-world exam responses from high schools. Our initial evaluation reveals that even state-of-the-art LLM judges struggle significantly on this task, exhibiting a high Mean Squared Error ($\sim$2.96) against expert human grading. To probe a plausible explanation, we contrast this performance with a control setting where the same judges evaluate synthetic LLM-generated solutions. We identify a stark ``Evaluation Gap'': judges are considerably more accurate and consistent on synthetic text (MSE $\sim$1.17) but struggle to generalize to authentic student reasoning. Through semantic embedding analysis, we find that synthetic errors suffer from a ``structural collapse'' into predictable, low-dimensional linear subspaces, whereas human errors form a more diverse error space. Furthermore, generative probability probes suggest that human reasoning involves significantly higher information-theoretic surprisal, indicating that student reasoning transitions are more out-of-distribution for current models. Finally, we find that surface-level style transfer fails to close this gap. Our findings suggest that current LLM evaluation pipelines relying heavily on synthetic data may not adequately capture the diversity of authentic student mathematical reasoning.

---


### 102. [FoA-SR: Faithful or Aesthetic? Profile-Aware Preference Optimization for Real-World Image Super-Resolution](https://arxiv.org/abs/2606.10275)

**<font color=#1a73e8>作者：</font>** Amjad Mahdi Alqarni, Peizhong Ju  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image super-resolution (SR) is often designed with a single restoration objective, despite the current capacity of generative models to produce multiple high-quality reconstructions for the same input. In this paper, we argue that the best restoration strategy is subject to the specific restoration profile: a Faithful restoration prioritizes reference consistency, structure preservation, and hallucination suppression, whereas an Aesthetic restoration prioritizes visually pleasing and natural-looking details. We propose FoA-SR, a novel preference optimization approach to real-world SR based on profiles. To achieve this goal, FoA-SR starts with our supervised FLUX.2-based SR adapter (Flux2SR) trained with LR latent conditioning, flow matching, and image-space reconstruction losses for paired LR-to-HR image super-resolution. Following the development of the shared supervised super-resolution adapter, FoA-SR generates a shared stochastic candidate pool for each input image and ranks the same candidates using profile-specific Faithful and Aesthetic rewards to mine winner-loser pairs. These pairs are used to fine-tune separate LoRA adapters while keeping the base model frozen. Experiments on RealSR and DIV2K show that FoA-SR can steer the same SR adapter towards distinct restoration objectives: a Faithful adapter improves reference-consistent metrics while an Aesthetic adapter boosts metrics that measure perceptual quality without reference. Our candidate-pool analysis shows that Faithful and Aesthetic rewards frequently select different winners, and a Hybrid-LoRA ablation shows that collapsing both profiles into one reward yields an implicit compromise rather than explicit profile control.

---


### 103. [Revisiting Positive Samples in Graph Contrastive Learning: From the Perspective of Message Passing](https://arxiv.org/abs/2606.10284)

**<font color=#1a73e8>作者：</font>** Lianze Shan, Ningchong Wang, Jitao Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Contrastive Learning (GCL), which trains graph encoders by maximizing similarity between positive samples and minimizing it between negative ones, has emerged as a mainstream graph pre-training paradigm. It is widely recognized that positive samples are essential in GCLs. Ideally, maximizing the similarity of positive samples enables graph encoders to capture intrinsic semantic and patterns of graph data. However, we discover an interesting phenomenon: GCLs can achieve competitive performance even without positive samples. This motivates us to revisit the fundamental mechanism of positive samples in GCLs. From the perspective of Dirichlet energy, we theoretically finds that message passing, a key mechanism in graph encoders, trivializes the maximization of positive samples, preventing GCLs from effectively learning from positive samples. To address this, we propose SPGCL to mitigate the trivialization caused by message passing and restore the learning efficacy of positive samples. Specifically, we find that high Dirichlet energy features help positive samples provide effective learning signals while low Dirichlet energy features contribute little to positive learning signal but is useful for positive sampling. Based on this, SPGCL propagates only high Dirichlet energy features and uses low energy features to construct a probability matrix for reliable positive sampling. Extensive experiments demonstrate the effectiveness of SPGCL.

---


### 104. [When Metrics Disagree: A Meta-Analysis of Knowledge-Graph-Completion Model Benchmarking](https://arxiv.org/abs/2606.10287)

**<font color=#1a73e8>作者：</font>** Haji Gul, Ajaz Ahmad Bhat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating Knowledge Graph Completion (KGC) models remains challenging because standard assessment relies on isolated rank-based metrics such as MRR, Hits$@$k, and Mean Rank, which often produce conflicting model orderings across datasets. A model that leads on MRR may trail on Hits@1, and strong performance on one dataset may not generalize to another. This fragmentation hinders comparison, enables selective reporting, and obscures real progress. We reframe KGC evaluation as a Multi-Criteria Decision-Making (MCDM) problem and present a meta-analysis of seven aggregators across five tests: consistency, cross-dataset stability, metric independence, robustness under noise, and generalizability. Each test is averaged over leave-one-model-out (LOMO) and leave-one-group-out (LOGO) removals so that reliability reflects aggregator behavior across diverse model subsets. Across tail $(h,r,?)$ and relation $(h,?,t)$ prediction, Pareto-optimal analysis identifies Z-score as the most balanced aggregator, which ranks DualE highest for tail prediction and FMS (Flow-Modulated Scoring) highest for relation prediction. A test-sensitivity analysis using the same removals shows that consistency and stability are largely removal-invariant, while generalizability and independence are the most sensitive. The framework resolves evaluation inconsistencies and offers evidence-based guidance for aggregator selection and model benchmarking in KGC.

---


### 105. [The Linux IOCTL Census: A Source-Derived Database of the Linux Kernel Control-Code Surface](https://arxiv.org/abs/2606.10290)

**<font color=#1a73e8>作者：</font>** Michael J. Bommarito II  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The ioctl system call is Linux's catch-all device-control interface. A userspace program opens a device node and hands the driver a numeric command code and an argument buffer, and the driver does whatever that code means, whether configuring hardware, reading back state, or moving data into and out of the kernel. Drivers define these commands themselves, by the thousand, and parse their arguments in kernel context, which makes ioctl handlers one of the broadest and least uniform local attack surfaces in the kernel. A handler that trusts an argument length it never validates can read or write kernel memory out of bounds, and the command space is catalogued in no central place. We present the Linux IOCTL Census, a source-derived and queryable inventory of that surface. An allmodconfig build compiles 878 modules across 169 subtrees, and over them a single deterministic libclang pass over the kernel source recovers 586 ioctl dispatch entry points, 1,289 decoded _IOC command codes, 3,583 controlled-input sinks, and 1,298 permission gates. A second pass encodes the kernel's own documented threat model as a queryable column, separating the capability-ungated ioctl surface, an upper bound on unprivileged reach rather than proven reach, from the part a hard capability gate puts out of scope. We backtest the census against 22 recent in-tree ioctl CVEs and release the structural tier as open data, on a schema shared with the companion Windows IOCTL Census so a single query spans both operating systems.

---


### 106. [What Spatial Memory Must Store: Occlusion as the Test for Language-Agent Memory](https://arxiv.org/abs/2606.10299)

**<font color=#1a73e8>作者：</font>** Doeon Kwon, Junho Bang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-agent "memory palace" systems anchor each memory to a world coordinate, on the intuition that geometry adds something text cannot. We make that intuition testable and report three results. First, the memory-palace default of folding spatial proximity into a linear blend beside recency and importance does not help and can hurt: in a pre-registered recall experiment the shipped blend fails its own frozen test (mean Delta-Hit@5 -0.0375, Wilcoxon p=0.306), sitting at a position-blind baseline, while a geometry-led weighting wins decisively (+0.3208, p<10^-15): geometry must lead recall when the query regime is spatial. Second, memory recall and visibility must be separated: recall is occlusion-blind by design (you correctly remember the next room behind a wall), while visibility is a perception predicate over stored geometry that the live system never computed. A one-line ray-versus-voxel digital differential analyzer (DDA), re-pointed from the gaze ray the agent already casts, supplies it: text and the live FoV cone both score 0.000 on 849 behind-wall targets while cone-plus-DDA reaches 0.982 (exact McNemar p<10^-6); coordinate recall separately resolves near-duplicate locations a cosine null cannot (1.000 vs 0.533, n=150). Third, the visibility predicate is confirmed live under a git-committed pre-registration (SPMEM-OCC-LIVE-v1: eight scripted worlds, automated oracle scoring, 96 behind-wall targets, false-visible 1.000->0.000, pooled exact McNemar p=2.5x10^-29), a run that surfaced and fixed a real relay anchor defect. We concede that occlusion-needs-geometry is near-tautological; the contribution is the measurement and isolation, separating what spatial memory must store from how it is read. These pilots power a frozen confirmatory study (SPMEM-ZERO-REAL-PREREG-v1); the full human-authored multi-world study with blind raters remains future work.

---


### 107. [Where You Inject Diversity Matters: A Unified Framework for Diverse Generation](https://arxiv.org/abs/2606.10302)

**<font color=#1a73e8>作者：</font>** Cheng Zhang, Rui Xin, Chudi Zhong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-ended generation tasks often require a set of meaningfully different outputs, yet large language models often produce similar generations. Existing test-time diversity methods operate at different stages of generation with varying effectiveness, but it remains unclear what design choices lead to meaningful diversity in the output. We introduce a framework that characterizes test-time diverse generation methods by the diversity source introduced during generation and provide a transmission score for measuring how effectively variation in the source reaches the final output. Guided by this framework, we propose fully automated specification-level generation methods that first generate diverse intermediate specifications and then condition on them to produce final responses. Across five open-ended tasks and four backbone models, specification-level injection improves output diversity over test-time baselines while maintaining comparable quality. Our analysis shows that successful diversity injection depends on both the diversity of the sources and their transmission to the output, highlighting source design and source-to-output realization as two key levers for building more diverse generation systems.

---


### 108. [Dissect and Prune: Enhancing Robustness in AI-Generated Image Detection](https://arxiv.org/abs/2606.10309)

**<font color=#1a73e8>作者：</font>** Dahye Kim, Jaehyun Choi, Hyun Seok Seong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While existing AI-generated image detectors report high performance, we identify that this is largely driven by a critical prediction asymmetry: a bias toward the real class that severely limits sensitivity to generated content, especially under standard post-processing operations such as compression and resizing. We hypothesize that this stems from the model's reliance on spurious features, distracting signals that obscure true generative artifacts. To address this, we propose DEAR (Dissect and Prune), which leverages inpainted images to identify and prune these interfering components. Specifically, we find that features strongly aligned to either inpainted or non-inpainted regions are less robust to post-processing. By measuring the alignment between channel activations and inpaint masks, DEAR removes features at both extremes, retaining only those that capture genuine generative artifacts. Experimental results demonstrate that our approach significantly enhances robustness against unseen generators and post-processing, effectively mitigating the prediction asymmetry. Our code is available at this https URL.

---


### 109. [TabClaw: An Interactive and Self-Evolving Agent for Spreadsheet Manipulation and Table Reasoning](https://arxiv.org/abs/2606.10316)

**<font color=#1a73e8>作者：</font>** Mingyue Cheng, Shuo Yu, Daoyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spreadsheets and tables are widely used representations for structured data analysis, but effective analysis still requires substantial manual effort and domain expertise. Recent large language model (LLM) agents can automate parts of this process, but they often provide limited transparency into intermediate decisions, rely on implicit assumptions, struggle with multi-table comparison, and repeat similar workflows without adapting to a user's preferences. This paper presents TabClaw, an open-source interactive AI agent for spreadsheet manipulation and table reasoning. Users upload CSV or Excel files and issue natural-language requests; TabClaw clarifies ambiguous intent, exposes an editable execution plan, streams a ReAct-style tool-using analysis loop, dispatches specialist agents for parallel multi-table reasoning, and synthesizes findings with explicit consensus and uncertainty markers. Beyond one-off analysis, TabClaw records completed workflows, extracts persistent user memory, distills reusable skills from repeated tool-use patterns, supports package-style skill import, and upgrades skills from negative feedback. Experiments on spreadsheet manipulation and table reasoning benchmarks show that TabClaw improves executable task completion and reasoning performance while preserving an inspectable user workflow. This paper shows how TabClaw turns spreadsheets and tables into inspectable analytical workflows while gradually personalizing itself to recurring data-analysis tasks. Our code is available.

---


### 110. [Rank Collapse, Fixed Points, and the Renormalization Group Structure of MLP Residual Networks](https://arxiv.org/abs/2606.10324)

**<font color=#1a73e8>作者：</font>** Parviz Haggi-Mani, Irina Rish  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The analogy between deep neural network forward passes and renormalization group (RG) flows has been repeatedly noted in the literature, but existing treatments remain qualitative: depth is described as a coarse-graining scale, attention is likened to a partition function, and representations are said to flow toward fixed points. No existing work has defined a measurable RG order parameter, tested it under controlled variation of the input distribution, or made quantitative predictions that are empirically verified. We study the simplest architecture for which the analogy is tractable: a pure MLP residual stack trained on masked token prediction over synthetic Markov chain sequences with known spectral properties. We report three findings. (i) The effective rank of the residual stream decreases monotonically with depth after training, consistent with progressive integration of irrelevant degrees of freedom. (ii) This rank collapse is selective: it occurs for chains with short correlation length approximately 1 but is absent for chains with long correlation length approximately 7, measured at the position level to control for mean-pooling artifacts. The network preserves exactly the degrees of freedom relevant to the prediction task, the content of the RG relevance criterion. (iii) Inter-layer kernel drift is concentrated at one or two specific transitions, with the remainder of the network near a fixed point, consistent with a discrete fixed-point plateau. Together these findings constitute the first quantitative, position-level evidence that MLP residual networks implement a selective coarse-graining procedure governed by the spectral structure of the input distribution.

---


### 111. [Content-Induced Spatial-Spectral Aggregation Network for Change Detection in Remote Sensing Images](https://arxiv.org/abs/2606.10328)

**<font color=#1a73e8>作者：</font>** Yunlong Liu, Zekai Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The integration of spatial and spectral information is beneficial to the improvement of change detection performance. However, existing methods cannot efficiently suppress the influences of spatial and spectral differences in unchanged areas. To address these issues, in this paper we propose a content-guided spatial-spectral integration network (CSI-Net) for the fusion of global spatial details and spectral difference information. Specifically, the proposed CSI-Net is composed of a spatial reasoning (SR) module, a spectral difference (SD) module, and a content-guided integration (CGI) module. In the SR module, the spatial information is learned by cascaded graph convolution blocks for global modeling. The SD module is responsible for the extraction of spectral features, by calculating the means and variances of features to reduce the impact of spectral differences in unchanged regions. In addition, in order to integrate the spatial-spectral features efficiently, we design a CGI module to further take advantage of their complementary information. In this module, high-level content information is introduced as a guide for a proper interaction. Due to the efficient spatial-spectral fusion, the proposed CSI-Net can learn the changed features better while achieving a suppression of spectral differences. Experimental results on LEVIR-CD, WHU-CD, and CLCD datasets demonstrate that the proposed CSI-Net produces better performance compared to state-of-the-art methods, and is applicable to different scenarios

---


### 112. [Building Change Detection in Earthquake: A Multi-Scale Interaction Network and A Change Detection Dataset](https://arxiv.org/abs/2606.10329)

**<font color=#1a73e8>作者：</font>** Yunlong Liu, Zekai Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As one of the most destructive natural disasters, earthquakes have struck many countries around the world in recent years, causing serious economic losses. Change detection (CD) can be applied to post-earthquake damage assessment as it can infer destroyed change regions from multi-temporal remote sensing images. Furthermore, the CD with short imaging interval will better satisfy the needs of the emergency rescues after earthquakes. However, the capability of current methods built on deep neural networks is limited because the dataset with short imaging interval is absent. To meet post-disaster immediate relief, we create a CD dataset, Turkey earthquake CD dataset (TUE-CD), for the evaluation of building damage in the short term after an earthquake. Because of the short acquisition interval of the post-event images, the imaging angle is different for different temporal images, which leads to some side-looking problems. To deal with these challenges, we present a multi-scale feature interaction network (MSI-Net) for efficient interaction between bi-temporal features, as well as mitigating the effect of side-looking problems. Specifically, the proposed MSI-Net consists of joint cross-attention (JCA) modules, multi-scale offset calibration (MOC) modules, and feature integration (FeI) modules. The JCA module unifies channel cross-attention and spatial joint attention for sufficient feature interaction. The MOC module further estimates the offsets to align the bi-temporal image with the multi-scale features. Finally, calibrated features and multi-scale features are fused by FeI modules for the prediction of changed areas. Experiments on the WHU-CD, CLCD, and the constructed TUE-CD dataset indicate that the proposed MSI-Net provides better results than considered state-of-the-art CD methods.

---


### 113. [Privacy-Preserving Credit Risk Prediction with Alternative Data](https://arxiv.org/abs/2606.10333)

**<font color=#1a73e8>作者：</font>** Hongzhe Zhang, Jiarong Xu, Jing He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit risk prediction is a critical problem in the consumer credit industry. Traditionally, financial institutions construct credit risk prediction models using borrowers' demographic, financial, and credit history data, collectively referred to as traditional data. Recent studies have demonstrated that alternative data, such as borrowers' mobile phone communication data, enable lenders to acquire fuller and more accurate profiles of borrowers' creditworthiness, thereby improving credit risk prediction performance. Nevertheless, alternative data are held by external entities independent of financial institutions. Directly sharing alternative data with financial institutions infringe on consumer privacy, yet existing credit risk prediction studies largely overlook this issue. To address this gap, we define a new problem, namely privacy-preserving credit risk prediction with alternative data, which simultaneously considers three practical constraints: the privacy-preserving constraint that protects consumer privacy, the model-confidentiality constraint that learns and stores the model centrally at the financial institution, and the lossless constraint that maintains the performance of the learned model. To solve this problem, we develop PrivacyCredit, a novel privacy-preserving machine learning method. We then theoretically demonstrate the privacy-preserving, model-confidential, and lossless properties of PrivacyCredit. Through extensive experiments using a real-world credit dataset linked with alternative data, we demonstrate the predictive value of securely incorporating alternative data into credit risk prediction and show that PrivacyCredit achieves the same predictive performance as the model learned from the insecure plaintext combination of traditional and alternative data. We further evaluate its model-confidentiality property and computational efficiency.

---


### 114. [Beyond Explaining Predictions: Logic-Based Explanations for Confidence in Machine Learning Models](https://arxiv.org/abs/2606.10347)

**<font color=#1a73e8>作者：</font>** Vinícius Peixoto Chagas, Carlos Henrique Leitão Cavalcante, Thiago Alves Rocha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning is increasingly used in critical domains, where both predictions and their associated confidence levels influence important decisions. To enhance transparency in such scenarios, it is important to understand why a model is confident or uncertain about its predictions. Recent logic-based approaches provide abductive explanations, minimal subsets of features sufficient to preserve the predicted class, with correctness guarantees. However, these methods focus solely on classification behavior and may produce explanations that cover instances with low predictive confidence. In this work, we introduce the concept of Minimum Confidence Threshold (MCT), which quantifies the weakest confidence guarantee provided by an abductive explanation. Building upon this concept, we propose confidence-aware abductive explanations, which preserve not only the predicted class but also a user-specified confidence guarantee. We formulate MCT computation as an optimization problem and introduce an algorithm for generating minimal explanations that satisfy a desired confidence threshold. We evaluate the proposed framework on boosted trees for binary classification, although the approach is applicable to other machine learning models that provide confidence scores. Experimental results show that traditional abductive explanations often provide substantially weaker confidence guarantees than the confidence associated with the explained instance itself. In contrast, confidence-aware explanations consistently improve the minimum confidence guaranteed by an explanation while requiring only a modest increase in explanation length. These properties make the proposed approach particularly suitable for applications where both predictive correctness and confidence are essential for trustworthy decision making.

---


### 115. [Multi-Angular Reflectance Anisotropy Observed from UAV Multispectral Imagery](https://arxiv.org/abs/2606.10350)

**<font color=#1a73e8>作者：</font>** Zhenqiang Qin, Chenguang Dai, Min Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV multispectral imagery naturally contains multi-angular observations due to low flight altitude and wide field-of-view imaging, which may introduce geometry-driven radiometric variability. This study proposes a geometry-aware multi-angular observation extraction workflow to quantify observation-geometry effects from a BRDF perspective. Specifically, camera intrinsics and extrinsics are refined via structure-from-motion (SFM), and homogeneous regions annotated on an orthomosaic are reprojected onto multiple raw sub-images acquired from different viewpoints. This enables joint extraction of multi-band reflectance and observation geometry parameters for the same ground targets under varying viewing directions. The extracted observations are further analyzed using band-wise polar visualization in the (VZA, RAA) domain. Results on a grassland target show clear reflectance anisotropy across ten bands, with red-edge and nearinfrared bands exhibiting 119-137% variability between maximum and minimum reflectance, indicating non-negligible observation-geometry effects on radiometric consistency.

---


### 116. [KG-SoftMAP: Soft Knowledge-Graph Priors for Bayesian Network Structure Learning from Sparse Discrete Data](https://arxiv.org/abs/2606.10358)

**<font color=#1a73e8>作者：</font>** Guoliang Xu, James E. Corter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning Bayesian network (BN) structure from sparse discrete data is hard: when each instance records only a few variables, most variable pairs lack the joint observations needed for reliable scoring, and data-only methods recover little structure. Imperfect domain knowledge, expressible as a weighted directed knowledge graph (KG), is often available. We propose KG-SoftMAP, which encodes such a KG as a soft, confidence-weighted, data-overridable edge prior and maximizes a MAP objective combining the BDeu score with a logit-form prior; the KG may be expert-curated or LLM-extracted. On controlled synthetic benchmarks, the only setting with ground-truth DAGs, KG-SoftMAP recovers partial directed structure at $\rho=0.05$ (DF1 $0.14$ to $0.29$, versus near-zero baselines) and substantially more once $\rho\geq0.2$ (DF1 $0.46$ to $0.96$), when paired with an informative but imperfect KG; recovery degrades gracefully as KG quality drops. On real sparse educational data, which has no ground-truth DAG, we evaluate deployment-facing measures only: prediction, calibration, and KG-consistency. The learned BN is best read as a diagnostic model: on SAF it trails logistic regression by $0.03$ F1_FAIL while providing KG-consistent edges, calibrated joint probabilities, and inference from arbitrary observed concept subsets; when no meaningful KG exists, discriminative logistic regression is preferable.

---


### 117. [Benchmarking stereo reconstruction for 3D printable Martian terrain models](https://arxiv.org/abs/2606.10364)

**<font color=#1a73e8>作者：</font>** Josephine Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing printable 3D models from Mars rover imagery is challenging because Martian terrain is low-texture, irregular, and partially observed. We evaluate a pipeline that estimates stereo depth from NASA Curiosity images, completes geometry, and exports watertight OBJ meshes. On Middlebury, RAFT-Stereo outperforms semi-global block matching (SGBM), reducing disparity MAE from 3.22px to 0.73px and increasing valid prediction coverage from 76.3% to 100.0%. On Curiosity imagery, however, RAFT's denser disparities show weaker edge alignment and higher photometric reprojection error, suggesting that benchmark accuracy does not directly transfer to Martian terrain reconstruction. Geometry completion demonstrates a tradeoff between local fidelity and global connectivity. We find that alpha shapes preserve accurate but fragmented structure, Poisson reconstruction produces more coherent meshes but adds unsupported surfaces, and a deterministic diffusion-fill baseline is intermediate but sensitive to stereo quality. Overall, standard stereo and completion methods can produce printable approximations of Martian terrain, but reliable reconstruction requires stronger domain-specific validation.

---


### 118. [ClinReadNet: A clinical reading-inspired network for low-dose abdominal CT image quality assessment](https://arxiv.org/abs/2606.10372)

**<font color=#1a73e8>作者：</font>** Xianye Xiao, Yulong Zou, Yujie Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In abdominal CT imaging, developing a low-dose, no-reference image quality assessment (No-reference IQA) model that mimics doctors' reading habits for evaluating CT image quality has significant practical value. This paper proposes a novel deep learning-based framework, ClinReadNet, whose design aligns with the clinical reading logic of radiologists: first, it introduces the Sobel ordinal quality network (SOQN) module, which can simultaneously focus on edge details highly relevant to image quality and the quality distribution pattern of the entire image, accurately matching the clinical image-reading judgment habit of "considering both local details and overall context"; second, the framework integrates the (shifted) window multi-scale temperature multi-head self-attention ((S)W-MTMSA) module, which further replicates the radiologists' image-reading process of shifting from overall scanning to local focusing, and accurately locks in regions of interest through multi-sharpness attention; third, it designs the hierarchical ranked probability score (HRPS) loss function, which combines the dual logics of coarse classification and fine classification, while paying attention to the distance information between grading labels, effectively improving the performance of image quality assessment. Experiments conducted on the LDCTIQAG2023 dataset show that the proposed method achieves the current state-of-the-art (SOTA) performance: the values of Pearson's linear correlation coefficient (PLCC), Spearman's rank-order correlation coefficient (SROCC), and Kendall's rank-order correlation coefficient (KROCC) reach 0.9507, 0.9554, and 0.8629 respectively, with the sum of their absolute values (Score) being 2.7690, outperforming existing methods.

---


### 119. [PF-Trans: Physics-Embedded Frequency-Aware Transformer for Spectral Reconstruction](https://arxiv.org/abs/2606.10373)

**<font color=#1a73e8>作者：</font>** Yuzhe Gui, Tianzhu Liu, Yanfeng Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Snapshot Broadband Filter Array (BFA) imaging provides high light throughput for spectral reconstruction but introduces severe spectral aliasing due to complex modulation. Current deep learning approaches, limited to spatial denoising, often fail to address the global frequency-specific degradations caused by the mask structure. To address this, we propose a Physics-embedded Frequency-aware Transformer (PF-Trans) for high-fidelity remote sensing spectral reconstruction. Our method explicitly integrates the physical sensing model through mask injection and a gray-scale consistency loss to ensure physical fidelity. Furthermore, we introduce a Dual-domain Block with a parallel Fast Fourier Transform (FFT) branch, enabling the network to perceive and suppress aliasing artifacts in the frequency domain. Extensive experiments on multiple datasets demonstrate that PF-Trans achieves state-of-the-art performance, achieving a Peak Signal-to-Noise Ratio (PSNR) of up to 48.50 dB on the GF-5 Shanghai dataset, significantly outperforming comparison methods.

---


### 120. [Belief-Space Control for Personalized Cancer Treatment via Active Inference](https://arxiv.org/abs/2606.10376)

**<font color=#1a73e8>作者：</font>** Deniz Sargun, H. Bugra Tulay, C. Emre Koksal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cancer treatment is at the core a sequential decision-making problem with partial observability, latent patient heterogeneity, and explicit constraints on the budget for medical measurements. Unlike standard Reinforcement Learning (RL) approaches that control state trajectories, cancer treatments permanently modify patients' transition dynamics, changing how states evolve over time. We model cancer treatment as a belief-space planning problem using active inference, deriving an expected free-energy objective that unifies goal-directed control and information acquisition under measurement budgets without. We implement this framework using real clinical cancer data from the AACR Project GENIE Biopharma Collaborative dataset. Results on clinical data demonstrate a simultaneous patient categorization and high treatment efficacy, under real measurement and treatment constraints.

---


### 121. [FSS-Net: Frequency-Spatial Synergy Network with Wavelet Attention for Carotid Artery Ultrasound Segmentation](https://arxiv.org/abs/2606.10378)

**<font color=#1a73e8>作者：</font>** Jiawei Liu, Zhijiang Wan, Junhua Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of carotid arteries in ultrasound imaging is critical for stroke risk assessment. However, speckle noise, low contrast, and blurred boundaries remain major challenges. In this paper, we propose a Frequency-Spatial Synergy Network (FSS-Net) to achieve noise-robust and high-precision carotid artery segmentation. The network integrates wavelet transform, multi-domain attention, and edge enhancement into a unified encoder-decoder architecture. Specifically, a Channel-Spatial-Wavelet Attention (CSWA) module is designed to suppress noise and purify semantic features in the frequency domain. A Wavelet-Enhanced Bottleneck (WEB) module is introduced to capture long-range global dependencies efficiently. Furthermore, a Laplacian-Guided Adaptive Edge Fusion (LAEF) module compensates high-frequency details and maintains boundary continuity. Extensive experiments on carotid ultrasound datasets show that FSS-Net achieves a Dice score (DSC) of 96.46% and strong robustness under low SNR conditions, outperforming several state-of-the-art methods. This method realizes accurate segmentation of carotid artery in ultrasonic imaging, effectively identifies carotid atherosclerotic plaque, and is verified by other task (such as segmentation of breast cancer), suggesting that it has good clinical application potential in identifying abnormal tissue masses in ultrasonic images.

---


### 122. [Expert-Level Crisis Detection in Mental Health Conversations](https://arxiv.org/abs/2606.10380)

**<font color=#1a73e8>作者：</font>** Grace Byun, Abigail Lott, Rebecca Lipschutz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world crisis intervention is inherently conversational, yet existing research largely focuses on static this http URL-world crisis intervention is inherently conversational, yet existing research largely focuses on static texts. When applied to multi-turn dialogues, current models exhibit significant performance degradation, struggling to track risk signals that emerge as context evolves. To address this gap, we introduce CRADLE-Dialogue, a clinician-annotated benchmark for turn-level crisis detection in conversational settings. The dataset features 600 dialogues with multi-label annotations across clinically grounded risks, including suicide ideation, self-harm, and child abuse, distinguishing past from ongoing risk. We further propose an Alert-Confirm evaluation protocol that distinguishes early warning signals (Alert) from turns where a specific crisis becomes explicitly identifiable (Confirm), reflecting the clinical need to intervene before risk becomes explicit. Experiments show that identifying when risk emerges is much harder than recognizing that it exists: models achieve only mid-40% to high-60% Micro F1. Additionally, we release a synthetic training corpus and a 32B-parameter model that substantially outperforms existing open-source models and achieves competitive or superior results against proprietary models across turn-level, dialogue-level, and confirm-only evaluation settings.

---


### 123. [Beyond Absolute Imitation: Anchored Residual Guidance for Privileged On-Policy Distillation](https://arxiv.org/abs/2606.10385)

**<font color=#1a73e8>作者：</font>** Wenhao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has demonstrated strong empirical gains in enhancing complex reasoning in LLMs by aligning a student model with a teacher's predictive distribution over the student's own trajectories. An emerging variant, Privileged OPD, further strengthens this paradigm by employing a self-teacher model augmented with privileged information, such as oracle traces, to mitigate teacher-student capacity gaps while providing dense, answer-directed supervision. However, current methods treat privileged information as a monolithic imitation target, failing to disentangle locally reachable reasoning steps from future-conditioned oracle signals. Consequently, the student is encouraged to match a hindsight-biased distribution that often falls outside its local predictive support. This reachability mismatch incentivizes the student model to skip valid intermediate reasoning in favor of locally unsupported shortcuts. To resolve this, we introduce Anchored Residual On-Policy Distillation (AR-OPD), a dual-view framework that disentangles privileged supervision. Rather than enforcing strict full-view imitation, AR-OPD establishes a locally compatible anchor using a partially privileged teacher, isolating and injecting oracle foresight as a controlled residual to provide destination-directed guidance. Across diverse reasoning tasks, AR-OPD outperforms full privileged OPD by 2.3 points and SFT by 7.9 points. Crucially, this anchored residual mechanism reduces hindsight leakage by 21.7% and mitigates late-stage drift, yielding up to a 7.2-point advantage on challenging long-horizon trajectories exceeding 768 tokens.

---


### 124. [Validation-Stage Combinatorial Fusion Analysis for Imbalanced Credit-Card Fraud Detection](https://arxiv.org/abs/2606.10393)

**<font color=#1a73e8>作者：</font>** Xiao Han, Chenyu Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit-card fraud detection is difficult because fraudulent transactions are rare, costly, and unevenly distributed. Strong gradient-boosted tree models already perform well on structured transaction data, so the value of another fusion method is not obvious. This paper examines whether Combinatorial Fusion Analysis (CFA), which searches over model subsets and rank-score fusion rules, can still add value on the IEEE-CIS Fraud Detection benchmark. Using a leakage-free 60/20/20 train/validation/test protocol, we evaluate 480 fusion configurations built from seven base classifiers. The best test-set result comes from diversity-weighted score fusion of Random Forest, XGBoost, and LightGBM (DEF WtScore), with AUC-ROC = 0.9405, AUPRC = 0.6699, and F1 = 0.6373. Bootstrap confidence intervals from 1,000 resamples show that the gains over the strongest single model exclude zero for all three metrics. CFA matches soft voting on AUC-ROC, improves AUPRC and F1, and outperforms stacking in this setting. A CTGAN augmentation experiment gives a negative result: synthetic fraud samples degrade both individual models and CFA. Overall, CFA is most useful here not as a way to combine every classifier, but as a validation-stage method for choosing a small, complementary subset and assigning diversity-aware weights.

---


### 125. [STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios](https://arxiv.org/abs/2606.10394)

**<font color=#1a73e8>作者：</font>** Sirui Liang, Bohan Yu, Peiyu Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to power personal agents for everyday applications, but evaluating these agents remains a challenge. Existing benchmarks still rely on sandboxed artifacts, static task design, and coarse scoring, which hinder scalability and limit progress toward reliable personal-agent evaluation. This paper introduces STAGE-Claw, an automated framework for building and evaluating realistic personal-agent scenarios in state-based personal-computing environments. Given a task hint, STAGE-Claw automatically creates and validates a realistic benchmark task with its environment, task prompts, ground truth, and related verification programs. Agents are then evaluated in realistic operating environments, where performance is measured by the correctness of the final system state rather than only the textual response. Using STAGE-Claw, this paper creates a benchmark with 40 challenging real scenario agent tasks, evaluates 11 frontier models, and analyzes their task scores, costs, tool-call reliability, and common failure patterns. Overall, STAGE-Claw offers a scalable, state-based way to evaluate agents in realistic user scenarios.

---


### 126. [Efficient RWKV-based Representation Learning for 3D Point Clouds](https://arxiv.org/abs/2606.10395)

**<font color=#1a73e8>作者：</font>** Yun Liu, Xuefeng Yan, Liangliang Nan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recent receptance weighted key value (RWKV) model combines RNN-style recurrence, offering a linear-complexity alternative to Transformers' quadratic self-attention for modeling global dependencies. However, when directly applied to point clouds, RWKV, originally developed for sequential text, struggles to capture local geometric structures and model spatial dependencies effectively. To address this, we propose the \textbf{P-RWKV} block, which bridges the gap between sequence modeling and irregular 3D geometry while preserving the efficiency advantages of RWKV. It consists of a Local Perception Expansion (LPE) component to expand contextual perception along the spatio-temporal sequence and a Spatial Context Enhancement (SCE) component to strengthen spatial awareness. To validate the effectiveness of P-RWKV for point cloud understanding, we construct PointER, a single-modality self-supervised representation learning framework whose encoder is composed of stacked P-RWKV blocks. Furthermore, we extend P-RWKV to a cross-modality setting and integrate the proposed core sub-modules into multiple architectures, demonstrating strong plug-and-play flexibility and architectural generality. Extensive experiments show that the P-RWKV block and its key sub-modules achieve competitive performance across various tasks with lower computational cost and inference latency. Code will be released upon acceptance.

---


### 127. [Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries](https://arxiv.org/abs/2606.10402)

**<font color=#1a73e8>作者：</font>** Federico Bianchi, Yongchan Kwon, Aneesh Pappu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is often a collective process: researchers share partial results, inspect failed attempts, and build on each other's ideas over long time horizons. Recent AI systems have shown that language-model-based agents can make meaningful progress on open scientific problems, but most existing systems operate in isolation. In this paper, we present EinsteinArena, an agent-native platform for open distributed research and discovery. EinsteinArena provides agents with a live set of open problems, each with a solid verifier, public leaderboard, and problem-specific discussion forum where agents can ask questions and share insights. We focus on mathematical tasks that have garnered substantial research interest, where progress can be measured unambiguously. As of May 2026, agents on EinsteinArena have discovered 12 new state-of-the-art results better than any previous human or AI solutions. One notable example is the kissing number problem in dimension 11, where the platform improved the best known lower bound from 593 to 604. This advance did not come from a single agent or isolated run. Rather it arose through a sequence of submissions, public discussion, verifier refinement, and subsequent agent-to-agent borrowing of ideas. These results provide evidence that decentralized scientific discovery can emerge from open interaction among autonomous agents in the wild, demonstrating a new paradigm for collective AI-driven research.

---


### 128. [FOGO: Forgetting-aware Orthogonalization Optimizer](https://arxiv.org/abs/2606.10406)

**<font color=#1a73e8>作者：</font>** Toan Nguyen, Yang Liu, Trung Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We argue that forgetting is not confined to continual learning but is a general optimization phenomenon: during standard training, dominant mini-batch gradients suppress rare but useful update directions, causing short-term forgetting at every step. When such knowledge is never revisited, these losses compound into long-term forgetting-the classical failure mode of continual learning. We introduce FOGO, a scalable optimizer that continuously detects and resolves gradient interference across both regimes. FOGO spectrally orthogonalizes momentum updates to prevent dominant directions from monopolizing optimization, then stores representative past directions in a compact codebook memory built on random projection, where pairwise distances are provably preserved in low-dimensional space. At each step, conflicts between the current update and stored directions are resolved via lightweight orthogonal correction and lifted back through a proximal step, with minimal overhead and no data storage. Across class-imbalanced classification, continual visual learning under domain and class shifts, continual fine-tuning of LLaVA-7B, and GPT-2 pretraining, FOGO consistently improves convergence and knowledge retention, outperforming Adam and Muon.

---


### 129. [A Comprehensive Inference-Time Augmentation Framework in Physiological Signals: Application to PPG-Based AF Detection](https://arxiv.org/abs/2606.10410)

**<font color=#1a73e8>作者：</font>** Davood Fattahi, Runze Yan, Saurabh Kataria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Accurate classification of physiological signals in real-world deployments is challenged by sensor noise, motion artifacts, and distribution shifts between training and deployment data. Inference-time augmentation (ITA), which applies augmentations during inference rather than retraining, offers a simple, model-agnostic mechanism to improve robustness. However, ITA application to physiological signals has remained narrow in scope, relying on limited augmentation methods with fixed, unoptimized parameters. This work proposes a unified ITA framework to address that gap.
Approach: The framework incorporates 13 augmentation methods spanning time-domain, amplitude-domain, frequency-domain, and artifact-injection transformations, with hyperparameters optimized via Bayesian optimization. We evaluate on atrial fibrillation (AF) detection from 30-second PPG signals using GPT-PPG and ResNet across five datasets comprising more than 400 patients and ${\sim}$9,800 hours of recording.
Main results: Standard ITA consistently improved AUROC (up to 8.5% for GPT-PPG and 0.7% for ResNet) and AUPRC (up to 10.6% for GPT-PPG and 0.8% for ResNet). Selective ITA further reduced average FPR by up to 4.4% (GPT-PPG) and 1.3% (ResNet) on non-AF datasets.
Significance: These findings establish ITA as a practical, model-agnostic approach for improving PPG-based AF classification reliability in deployment settings where retraining is not feasible, with broader applicability to physiological signal analysis.

---


### 130. [A Unified Multi-Modal Framework for Intelligent Financial Systems: Integrating Reinforcement Learning, High-Frequency Trading, and Game-Theoretic Approaches with Cross-Modal Sentiment Analysis](https://arxiv.org/abs/2606.10412)

**<font color=#1a73e8>作者：</font>** Fanrong Liu, Zhang Yuwei, Mingni Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of financial technology demands sophisticated artificial intelligence systems capable of handling diverse challenges across multiple domains simultaneously. This paper presents a groundbreaking unified framework that seamlessly integrates Proximal Policy Optimization for robo-advisory systems, advanced time-series prediction models for high-frequency trading, in-context learning mechanisms for dynamic investment advisory, game-theoretic approaches for competitive banking scenarios, and unified embeddings for cross-modal financial sentiment analysis. Our comprehensive framework addresses the critical gap in existing literature where these technologies have been developed in isolation, failing to leverage their synergistic potential. Through extensive experimentation across multiple financial datasets and real-world scenarios, we demonstrate that our integrated approach achieves superior performance compared to specialized single-domain systems. Specifically, our framework shows a 23.7% improvement in portfolio optimization metrics, reduces prediction error in high-frequency trading by 31.2%, enhances investment recommendation accuracy by 18.9%, optimizes competitive banking strategies with a 27.4% increase in Nash equilibrium convergence speed, and improves sentiment analysis accuracy by 15.6% through cross-modal fusion. The theoretical foundation of our work establishes convergence guarantees for the integrated optimization problem, while our empirical results validate the practical applicability across diverse financial institutions. This research not only advances the state-of-the-art in financial AI but also provides a blueprint for developing comprehensive intelligent systems that can adapt to the complex, interconnected nature of modern financial markets.

---


### 131. [Mitigating Bias in Low-SNR Financial Reinforcement Learning via Quantum Representations](https://arxiv.org/abs/2606.10448)

**<font color=#1a73e8>作者：</font>** Zeyu Liu, Xuanzhi Feng, Sing Kwong Lai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The financial market is a typical low signal-to-noise ratio (SNR) setting, which often destabilizes off-policy maximum-entropy methods like Soft Actor-Critic (SAC). Specifically, noisy state representations may produce unreliable Q-value estimates, and bootstrapping amplifies these errors, forming a failure mode we call the "Financial Entropy Trap". In this paper, we propose FPQC-SAC, an efficient and plug-and-play SAC variant that places a compact and bounded Parameterized Quantum Circuit (PQC) before the actor and critic networks to constrain feature propagation at the representation level, rather than filtering raw inputs or regularizing Q-values after bootstrapping. Notably, FPQC-SAC reduces the impact of extreme market fluctuations on Bellman target estimation, while trainable quantum entanglement preserves flexible cross-asset interactions. Empirical evaluations on real-world portfolio management tasks demonstrate that FPQC-SAC substantially enhances out-of-sample stability and cumulative returns by achieving a 66.89% relative gain in cumulative return over standard unconstrained SAC and outperforms the best continuous-control deep reinforcement learning baseline by approximately 27%. Open-source code is available at this https URL.

---


### 132. [Few-step Generative Models as Lossy Compression](https://arxiv.org/abs/2606.10450)

**<font color=#1a73e8>作者：</font>** Fuma Kimishima, Jinjia Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DiffC provides a principled way to reuse pre-trained diffusion models for lossy compression, but its encoding and decoding procedures remain slow because they require many discretized forward and reverse steps. We study whether few-step generative models -- Rectified Flow, Consistency Trajectory Models (CTM), and MeanFlow -- can be cast as codecs within the same reverse channel coding (RCC) framework. The main challenge is that RCC requires posterior and shared distribution parameters, whereas these models do not explicitly parameterize intermediate conditional distributions. For Rectified Flow and MeanFlow, we use the equivalence between velocity parameterization and diffusion-style denoising parameterization to derive the quantities required by RCC. For CTM, which is distilled from EDM, we adopt the EDM noise parameterization together with local Gaussian approximations of the sender and shared distributions at intermediate states. This yields a proof-of-concept probabilistic formulation that enables compression with pre-trained few-step generative models without retraining. On low-resolution benchmarks, the resulting codecs reduce encoding and decoding time and improve realism in the low-bit-rate regime.

---


### 133. [The Distributed Detectability Band Against Marginal-Preserving Attacks](https://arxiv.org/abs/2606.10456)

**<font color=#1a73e8>作者：</font>** Zhang Qinqin, Gao Yuze  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-control monitors score individual agent actions to detect misbehavior, but real harm can be distributed across many benign-looking steps, each individually below any per-step alarm. We construct a marginal-preserving, correlation-encoded distributed-sabotage attack using a Gaussian-copula AR(1) construction: the per-step monitor-score marginal is held exactly equal to benign, so mean, max, top-k tail, and threshold monitors (Monitor A) are defeated by construction, while harm is encoded in the temporal correlation structure. We sequence the paper around three reviewer-mandated gates. (1) Realizability gate: the stealthy attack achieves KS-distance to benign of 0.013 (effectively zero) at all tested harm levels up to 3.0, confirming that harm is fully decoupled from the per-step marginal and realizability is not harm-limited. (2) Monitor-A-vs-B reconciliation: we show formally that the attack, built against Monitor A's score marginal, remains marginal-preserving under a different-score Monitor B (the correlation/sequence family: CUSUM, SPRT, HMM-LR, runs test, autocorrelation, windowed logistic), and scope worst-case claims to score functions that admit a temporal signature. (3) Non-empty detectability band: Monitor A achieves AUC 0.52 (chance); Monitor B spans AUC 0.79-0.97 at the same 1% FPR target, and as harm is amortized over more steps Monitor A collapses to chance while Monitor B holds at AUC ~0.95. These results demonstrate a non-empty detectability band and characterize the sub-threshold sabotage frontier: distribution-shape monitors fail by construction; temporal-correlation monitors can detect but are not trivially optimal.

---


### 134. [Trace2Policy: From Expert Behavior Traces to Self-Evolving Decision Agents](https://arxiv.org/abs/2606.10457)

**<font color=#1a73e8>作者：</font>** Junli Zha, Jinbo Wang, Chao Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision rules that enterprise experts apply tacitly -- in auditing, compliance, and contract review -- can be systematically recovered and improved through iterative error analysis. We present \textbf{Trace2Policy}, whose core mechanism -- \textbf{EISR} (\textbf{E}rror-driven \textbf{I}terative \textbf{S}kill \textbf{R}efinement) -- maintains a human-readable rule document as its optimization target: each round executes the rules on a validation set, clusters errors by root cause into MISSING, WRONG, or CONFLICT types, applies targeted patches, and commits only those that pass a regression gate. \textbf{For this class of compliance-sensitive, skewed-base-rate decision tasks, we identify rule quality -- not model capability -- as the dominant performance lever}: across five LLMs, one-shot distillation plateaus near $\sim$70\% on the deployed pool, while eight EISR rounds lift the same rules to 79.6\% when compiled into deterministic Python -- zero LLM calls at inference. \textbf{Execution form compounds the gain: in production, the same EISR-refined content runs 9.8~pp higher as compiled Python than as an LLM prompt, a form-and-engineering bundle the 22-day deployment matured together.} Deployed for 22 days at a major logistics carrier (3,349 audit cases), the compiled pipeline outperforms the pure-LLM baseline it replaced (72.7\%); on these calibrated, skewed-base-rate workloads, re-enabling LLM fallback monotonically degrades accuracy. An LLM-driven variant, \textbf{Auto-EISR}, reproduces this refinement at \$5--\$10 per cycle versus $\sim$70 expert-hours, and transfers to four public benchmarks spanning legal reasoning (LegalBench) and process-mining decisions (BPIC 2012) without re-engineering.

---


### 135. [Detecting Speculative Language in Biomedical Texts using Recurrent Neural Tensor Networks](https://arxiv.org/abs/2606.10471)

**<font color=#1a73e8>作者：</font>** Dhruv Dixit  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this investigation, we delve into the automated detection of speculative language within biomedical articles by utilizing distributed sentence representations and advanced deep learning techniques. The implications of such identification extend to information retrieval, multi-document summarization, and the exploration of new knowledge. Our exploration encompasses two distinct approaches for acquiring distributed sentence representations: the Paragraph Vector model and the Recursive Neural Tensor Network. These methodologies are then rigorously compared against three foundational baseline algorithms: Support Vector Machines, Naive Bayes, and pattern matching. Our findings reveal that the Recursive Neural Tensor Network (RNTN) demonstrates a slight performance edge (F1 = 0.885) over the top-performing baseline, the linear bigram SVM (F1 = 0.881). Meanwhile, the Paragraph Vector model proves less effective (F1 = 0.368), even after extensive training using an expansive, unlabeled dataset. We engage in a comprehensive discourse on the factors influencing these performance disparities and provide insightful recommendations for future research directions.

---


### 136. [Decoupling Thought from Speech: Knowledge-Grounded Counterfactual Reasoning for Resilient Multi-Agent Argumentation](https://arxiv.org/abs/2606.10475)

**<font color=#1a73e8>作者：</font>** Jakub Masłowski, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate frameworks have been shown to improve large language model performance in convergent tasks, but they are currently optimized in a way that heavily favors final output accuracy rather than stability of the process. During long-horizon exchanges reactive systems under sustained perturbations often experience logic degradation, argument repetition, and role drift. To structurally prevent the identity loss and maintain the process fidelity, we introduce Knowledge-Grounded Counterfactual Reasoning (KG-CFR), a dual-stage architecture that enforces a strict separation of concerns between a private, retrieval-augmented planning buffer, and a public execution layer. We assess this system in Dynamic Resource Allocation under Uncertainty (DRAU), a dedicated 1v1v1 environment, introducing diversity as distinct from standard debate settings. Over 270 completely factorial crisis simulation trajectories with stochastic environmental shocks, KG-CFR prevents judge-detected critical post-shock degradation (defined as a quality shift, $\Delta \le -0.20$) in more than 95% of perturbed runs, increasing the overall argument quality from 0.694 to 0.822. Our primary contribution is the demonstration of architectural decoupling being an important factor of systemic resilience enhancement under sustained pressure without quality loss. Furthermore, we introduce custom vector metrics for discourse divergence and plan-execution alignment that provide strong, directionally consistent evidence of operational stability. Our ablation experiments suggest that the proper doctrinal grounding can be an equally important factor for argument quality, as the prospective planning. KG-CFR, according to our initial metric evaluations, reduces semantic looping, by preserving the agent's consistency with the original plan.

---


### 137. [HE-DAP: Homomorphic Encryption-based Dynamic Adaptive Parameter Optimization for Statistical Computation](https://arxiv.org/abs/2606.10477)

**<font color=#1a73e8>作者：</font>** Yun-Soo Park, Hyunmin Choi, Hyoungshick Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homomorphic encryption (HE) enables privacy-preserving analytics but remains hindered by high computational overhead. We find that the inverse square root-a key primitive in many statistical and machine learning workloads-exhibits inconsistent and often suboptimal performance across HE libraries and hardware. This stems from a core trade-off between two costly HE operations: evaluating high-degree Chebyshev polynomials to speed up Newton's method versus performing bootstrapping to manage ciphertext noise. Because their relative costs vary by up to 6x across environments, any fixed configuration proves inherently inefficient.
To address this challenge, we present HE-DAP, a cross-platform optimization framework that automatically navigates this trade-off. By profiling an environment's unique performance characteristics, HE-DAP finds the optimal balance between polynomial degree and iteration count to accelerate the encrypted inverse square root computation for a given accuracy target. Our evaluation on Lattigo, HEaaN-CPU, and HEaaN-GPU shows that HE-DAP's adaptive approach yields significant performance gains. It accelerates the core inverse square root computation by up to 2.35x over the fixed configuration in PP-STAT while maintaining high numerical accuracy (MRE <= 3.1 x 10^-8). We further demonstrate that optimizing this fundamental building block directly enhances the end-to-end performance of complex statistical analyses, confirming the practical benefits of our environment-aware approach. By automatically adapting to heterogeneous execution environments, HE-DAP demonstrates that principled parameter optimization can make privacy-preserving statistical analytics practical at scale.

---


### 138. [3D-CoS: A New 3D Reconstruction Paradigm Based on VLM Code Synthesis](https://arxiv.org/abs/2606.10478)

**<font color=#1a73e8>作者：</font>** Yuhao Wang, Puyi Wang, Linjie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most recent 3D reconstruction and editing systems operate on implicit and explicit representations such as NeRF, point clouds, or meshes. While these representations enable high-fidelity rendering, they are fundamentally low-level and hard to control programmatically. In contrast, we propose and systematically evaluate a new 3D reconstruction paradigm, 3D Code Synthesis (3D-CoS), where 3D assets are constructed as executable Blender code, a programmatic and interpretable medium. To assess how well current VLMs can use code to represent 3D objects, we evaluate representative open-source and closed-source VLMs in code-based reconstruction under a unified protocol. We further introduce a suite of structured code-synthesis workflows, including blueprint-based planning, Retrieval-Augmented Generation (RAG) over Blender API documentation, few-shot geometric demonstrations, and a component-level Agent workflow for part-wise code generation. To demonstrate the unique advantages of this representation, we further evaluate localized text-driven modifications and compare our code-based edits with a point-cloud-based 3D editing baseline. Our study shows that code as a 3D representation offers strong controllability and locality, yielding stronger edit fidelity and better preservation of unedited regions in our targeted editing evaluation. Our work also analyzes the potential of this paradigm, delineates the current capability frontier of VLMs for programmatic 3D modeling, and highlights code synthesis as a promising direction for editable 3D reconstruction.

---


### 139. [ComBench: A Benchmark for Rigorous Proof Reasoning and Constructive Realization in Olympiad-Level Combinatorics](https://arxiv.org/abs/2606.10479)

**<font color=#1a73e8>作者：</font>** Shunkai Zhang, Haoran Zhang, Yun Luo 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combinatorics is central to Olympiad-level mathematical problem solving, requiring deep discrete reasoning, creative constructions, and rigorous structural insight. Recent evidence suggests that even today's strongest frontier models remain uneven on Olympiad combinatorics, revealing a gap in creative mathematical reasoning. We introduce ComBench, an Olympiad-level combinatorics benchmark for evaluating and diagnosing the combinatorial reasoning capabilities of large language models. ComBench contains 100 human-annotated competition-level problems organized around two complementary settings: analysis-centric problems, which primarily require rigorous mathematical arguments, and construction-centric problems, which require explicit constructions in addition to correctness justifications. The evaluation protocol combines rubric-guided proof grading with deterministic construction verification, exposing cases where proof quality and construction validity diverge. Experiments on frontier open- and closed-source models show that ComBench is far from saturated: the strongest model reaches 65.4% overall Avg. and 75.3% overall Best@4. We further find that Rigorous Proof Reasoning and Constructive Realization are distinct capabilities: Kimi-K2.6 trails GPT-5.5 on analysis-centric proof grading but surpasses it on construction-centric Best@4, while Existence and Construction problems remain consistently hardest across representative frontier models.

---


### 140. [AgentCanary: A Security Evaluation Framework for Autonomous AI Agents in Real Executable Environments](https://arxiv.org/abs/2606.10484)

**<font color=#1a73e8>作者：</font>** Peiyang Li, Songping Wang, Yi Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents have driven the transition from conversation to task execution, shifting security failures from textual deception to system compromise. Although security evaluation is crucial for proactive risk prevention, prior work is constrained by fundamental bottlenecks, including fragmented risk coverage, static or low-fidelity execution environments, and single-dimensional and coarse-grained assessment metrics. To address these challenges, we propose AgentCanary, a comprehensive security evaluation framework for autonomous AI agents. AgentCanary provides a systematic solution along three contributions. First, comprehensive risk coverage: we introduce an orthogonal Entry $\times$ Impact risk taxonomy that decouples how adversarial influence enters the agent from what harm it ultimately causes, and instantiate it as a scenario-aligned task suite spanning realistic deployment workflows. Second, a high-fidelity real executable environment: rather than static Q&A or mocked tool responses, agents interact with real tools against dynamically provisioned task artifacts, with persistent state across multi-step interactions that naturally supports long-horizon attack evaluation. Third, trajectory-grounded multi-dimensional evaluation: evaluation consumes the full agent trajectory rather than the reply text or a single tool call, enabling decomposed scoring along three orthogonal dimensions, Outcome Safety, Security Awareness, and Task Utility. We evaluate a broad set of frontier models on AgentCanary against multiple established adversarial attack methods across three agent frameworks. The results reveal that current agents often fail to recognize the attacks they face, particularly under compromised skills, persistent state, and long-horizon execution attacks, and provide a systematic baseline for developing more reliable and secure agent systems.

---


### 141. [PathRelax: Parallel-Path Relaxed Speculative Jacobi Decoding for Accelerating Auto-Regressive Text-to-Image Generation](https://arxiv.org/abs/2606.10492)

**<font color=#1a73e8>作者：</font>** Haodong Lei, Hongsong Wang, Bingxuan Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing need for high-resolution image generation in autoregressive text-to-image models has resulted in extended token sequences, significantly increasing computational costs and inference times. However, existing state-of-the-art methods for accelerating autoregressive text-to-image models rely on chain-structured draft token sequences, leading to inefficient draft token search and limited acceptance lengths. To address this, we propose parallel-path cross-relaxed speculative Jacobi decoding (\textbf{PathSpec}), a novel framework that enhances efficiency through a multi-sequence draft tree structure. Our parallel-path speculative Jacobi decoding (\textbf{PathExplore}) expands the token search space, achieving a higher speedup ratio without sacrificing image quality. Additionally, we introduce cross-path relaxed verification (\textbf{PathRelax}) that exploits semantic similarities across sequences to further boost token acceptance rates. Evaluated on the Parti-Prompts, MSCOCO2017, and T2ICompBench datasets, our method achieves a speedup ratio of 4.14 $\times$, 3.95$\times$, and 4.18$\times$, respectively. Remarkably, PathExplore, without any relaxed sampling, outperforms relaxed sampling methods in the speedup ratio, such as GSD and LANTERN. Moreover, PathRelax's relaxation mechanism can be seamlessly integrated with other relaxation techniques, enabling further acceleration and providing an efficient solution for real-time text-to-image generation. Our code is available at this https URL.

---


### 142. [A Reliable Fault Diagnosis Method Based on Belief Rule Base Consider Robustness Analysis](https://arxiv.org/abs/2606.10500)

**<font color=#1a73e8>作者：</font>** Mingyuan Liu, Dan Yin, Zongzong Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In equipment operation, the implementation of fault diagnosis is essential to ensure the continuity and safety of production equipment, improve operational efficiency and reduce maintenance costs. Since sensor readings are widely used for fault diagnosis, their reliability directly affects the results of fault diagnosis. A new fault diagnosis method is proposed to address the two problems of robustness assessment and robustness optimization of fault diagnosis models. For this purpose, a reliable fault diagnosis method based on a belief rule base (BRB) considering robustness analysis is proposed. Firstly, the robustness analysis of the BRB model is carried out systematically. Secondly, three robustness constraint strategies are proposed to optimize the robustness of the BRB fault diagnosis model. Finally, the effectiveness of the proposed model is verified by taking the fault diagnosis of WD615 diesel engine and Case Western Reserve University bearings as an example, and the experiments show that the proposed model improves both accuracy and robustness.

---


### 143. [When VR Meets BCI: (Un)Observable Brainwave-aware Privacy Reconstruction in the Metaverse via Unrestricted Inbuilt Motion Sensors](https://arxiv.org/abs/2606.10502)

**<font color=#1a73e8>作者：</font>** Tao Ni, Zehua Sun, Qingchuan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Metaverse devices, such as virtual reality (VR), have seen substantial development and widespread applications in numerous areas. Although recent studies have revealed privacy leakages in VR, these vulnerabilities were limited in the scope of observable behaviors in virtual scenes (e.g., what a user is seeing). In this work, we uncover the feasibility of going beyond the scope of observable user behaviors to unobservable brain EEG-correlated representations (e.g., what a user is perceiving) by leveraging unrestricted motion sensors in VR headsets to reconstruct brain EEG signals, a seemingly neglected but promising vector. The insight is that the inbuilt motion sensors (e.g., accelerometers) in the VR headset can capture subtle vibrations induced by pupillary responses, which are highly correlated with users' visual stimuli and in-brain perceptions.
Therefore, we design and implement BraVeSpy to systematically investigate and demonstrate the feasibility of this severe privacy leakage originating from brain EEG-correlated representations reconstructed from variations of inbuilt motion sensors. Our extensive evaluation results from different VR devices show that BraVeSpy, for the first time in the Metaverse, can reveal unobservable privacy, where we successfully unveiled perceptive images in the brain with 52.0%-67.2% accuracy. In particular, we also find that BraVeSpy outperforms the current approaches that are limited to coarse-grained inference of observable behaviors and achieves over 85.0% accuracy in inferring user activity-related sensitive information, such as fingerprinting websites, apps, and streaming videos, and over 96.0% accuracy in user de-anonymization, gaze movement tracking, and virtual keystroke inference.

---


### 144. [Cross-Modal Knowledge Distillation without Paired Data: Theoretical Foundation and Algorithm](https://arxiv.org/abs/2606.10504)

**<font color=#1a73e8>作者：</font>** Trong Khiem Tran, Anh Duc Chu, Quang Hung Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-modal knowledge distillation (CMKD) studies how a (large) teacher model trained on one type of data (e.g., images) can guide a (smaller) student model building on another type of data (e.g., text/audio). Existing CMKD methods often require paired multi-modal data with aligned semantics, but obtaining such paired data are often costly and impractical. To mitigate this limitation, we develop a new CMKD framework for the more challenging setting where paired data are unavailable. In particular, we establish a cross-modal distributional relationship between teacher and student models, which reveals two fundamental quantities governing effective distillation: feature alignment and label alignment. These quantities characterize semantic discrepancy between modalities at the levels of representation and prediction distributions, respectively. Motivated by this insight, we propose a principled framework, with theoretical guarantees, that enables effective cross-modal knowledge distillation by aligning distributions rather than individual samples. Extensive experiments across a wide range of multimodal benchmarks show that our framework is highly effective in both unpaired and paired data settings, improving significantly over prior work.

---


### 145. [A Deployment-Oriented Framework for Explainable AI-Assisted eBPF/XDP Mitigation at the IoT Edge](https://arxiv.org/abs/2606.10508)

**<font color=#1a73e8>作者：</font>** Abdurrahman Tolay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) deployments combine heterogeneous, resource-constrained devices with weak security configurations, exposed services, limited logging, patching constraints, and long lifecycles. Signature- and threshold-based controls remain useful baselines, but they are insufficient as standalone mechanisms in dynamic IoT networks. Likewise, offline artificial intelligence (AI) benchmark performance alone does not establish operational deployability. This article presents a conceptual framework and research agenda for a Linux-based IoT edge gateway that combines resource-aware flow-level AI-assisted risk scoring, event-level explainability, and bounded mitigation through eBPF/XDP. The controller applies reversible, time-limited actions subject to critical-device safeguards, updates packet-level enforcement state, and records structured logs. The architecture separates complex reasoning and policy control in user space from concise packet-handling decisions in the kernel. It also defines a future hardware-aware evaluation pathway covering detection quality, resource cost, response timing, rollback behaviour, and legitimate-traffic preservation. The paper does not report new experimental meas

---


### 146. [LAFP: Preserving Latent Action Structure in Latent Policy Learning via Flow Matching](https://arxiv.org/abs/2606.10517)

**<font color=#1a73e8>作者：</font>** Jiexi Lyu, Xizhou Bu, Qingqiu Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning high-quality latent actions from large-scale unlabeled videos, coupled with limited real-world interaction data for training an action decoder, has emerged as a promising paradigm for scalable latent policy learning. However, existing approaches typically rely on behavior cloning, which tends to collapse inherently multimodal action distributions into unimodal ones, thereby degrading the pretrained latent action structure. While flow matching provides a potential alternative, directly applying it leads to a misalignment between latent actions and physical actions during action decoder training, due to the stochastic nature of the learned policy. To address these, we propose Latent Action Flow Policy (LAFP), which leverages flow matching for latent policy learning and introduces an inference-time interpolation mechanism to mitigate stochasticity-induced misalignment. Experimental results demonstrate that LAFP consistently outperforms prior methods on downstream imitation learning tasks, achieving up to 10-15% improvement in success rate while incurring less than 1x additional inference overhead.

---


### 147. [GUI-AC: Enhancing Continual Learning in GUI Agents](https://arxiv.org/abs/2606.10522)

**<font color=#1a73e8>作者：</font>** Can Lin, Tao Feng, Hangjie Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical User Interfaces (GUIs) serve as the dominant medium for human-computer interaction, yet building GUI agents that generalize across the vast diversity of real-world interface environments, with the same flexibility and robustness that humans naturally exhibit, remains unsolved. Notably, GUI data are inherently non-stationary: the continual emergence of previously unseen interface instances (e.g., novel domains and resolutions) induces persistent distribution shifts, significantly impeding the continual learning of existing GUI agents. Reinforcement fine-tuning (RFT) has attracted considerable attention as a promising approach. Nevertheless, RFT exhibits pronounced instability in its grounding capability, manifested as sharp reward discontinuities and high-variance oscillations. The imbalanced distribution of rollout outcomes introduces substantial noise into advantage estimation, leading to policy overconfidence. The fixed clipping bound suppresses the increase in policy probabilities needed to adapt to new distributions, leading to a collapse in exploration capacity. To address these challenges, we propose GUI-AC, a method that enhances the continual learning capability of GUI agents. GUI-AC introduces grounding certainty to support two core mechanisms: (i) Adaptive Advantage, which down-weights noisy advantage estimates to prevent policy overconfidence; and (ii) Dynamic Clipping, which relaxes the clipping bound to encourage exploration range. Extensive experiments show that these mechanisms jointly improve performance, enabling our method to surpass state-of-the-art baselines. Code is available anonymously at this https URL.

---


### 148. [Representation-Aware Advantage Estimation: Your Reward Model Provides More Than A Scalar Output](https://arxiv.org/abs/2606.10528)

**<font color=#1a73e8>作者：</font>** Guozheng Li, Xiyan Fu, Yiwen Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current reinforcement learning from human feedback (RLHF) methods primarily rely on scalar rewards from a trained reward model (RM). While effective, scalar rewards are often noisy and fail to capture fine-grained preference differences, whereas RM hidden states encode richer semantic and preference information. We introduce the representation-aware advantage estimation, which leverages RM hidden states and models them as auxiliary signals for better advantage estimation. Specifically, we propose the Graph-based Advantage Estimation (GraphAE), treat each sampled group as a graph, where nodes correspond to responses and edges capture their similarity in the RM hidden space. Then advantages are computed via graph propagation, enabling each sample to incorporate contextual information from its neighbors. GraphAE is lightweight and can be seamlessly integrated into existing group-based RL algorithms. We apply GraphAE to GRPO, GSPO and RLOO, and conduct extensive experiments on different models and benchmarks. Empirical results show consistent improvements across three benchmarks, with gains of up to + 6.3 on Arena-Hard-v0.1, + 8.27 on AlpacaEval 2.0, and + 0.22 on MT-Bench. These results demonstrate that leveraging RM representations leads to more sample efficient and robust RLHF.

---


### 149. [Machine Learning Methods for Studying Latent Neural Activity Dynamics](https://arxiv.org/abs/2606.10530)

**<font color=#1a73e8>作者：</font>** Shufeng Kong, Fumei Deng, Xinyi Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent developments in brain recording are driving a demand for machine learning tools capable of decoding the latent structure of large populations of neurons. In this paper, we provide a comprehensive survey that outlines the trajectory of Latent Variable Models (LVMs) from early state-space models to more recent deep generative models. We organize the literature into three closely related domains: (1) Single-Region Latent Dynamics, which includes models such as linear dynamical systems to more complex dynamics represented by Recurrent Neural Networks (RNNs) and Neural Ordinary Differential Equations (ODEs); (2) Multi-Region Communication, which employs probabilistic as well as subspace methods to study how information is transferred across different brain areas considering synaptic propagation delays and network connectivity; and (3) Behavior-Aligned Modeling, which seeks to disentangle neural activity related to task performance from other internal states via supervised or contrastive learning. This survey also includes large-scale neural foundation models, such as Transformers and diffusion models, that rely on large-scale pre-training for optimal performance across subjects. Finally, we conclude and discuss benchmarks, evaluation criteria, and open challenges, such as the ability to identify causal links or directionality of communication, to facilitate future research for bridging interpretable brain dynamics with reliable neural decoding.

---


### 150. [Audio-Visual Exchange-Aware Token Pruning for Efficient Audio-Visual Captioning](https://arxiv.org/abs/2606.10533)

**<font color=#1a73e8>作者：</font>** Zihan Meng, Dexiang Hong, Weidong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual captioning generates natural language descriptions from video and audio content. Multimodal LLMs have advanced this task, but both modalities contribute many tokens to the LLM input, where prefill self-attention scales quadratically. Existing token-pruning methods usually retain tokens by attention, saliency, or cross-entropy loss, yet the hard threshold selection makes it difficult to retain tokens that are truly valuable, especially for high-confusing tokens near the decision boundary. To this end, we propose a AVEX-Prune, an RL-based audio-visual dynamic token pruning method in this work. In our AVEX-Prune, an audio-visual token exchange strategy is proposed to select truly valuable tokens by replacing low-confidence retained tokens with high-confidence candidate tokens from the same or the other modality, and measuring the differences in caption generation from token swaps. AVEX-Prune preserves full-token quality at a 40% retention ratio on both VILA 1.5-8B (54.5 vs. 54.6) and VideoLLaMA 2 (57.0 vs. 56.8).

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-269](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
