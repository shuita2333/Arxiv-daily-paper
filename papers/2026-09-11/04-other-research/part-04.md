# 📦 其他研究 | 2026年09月11日

> 本类共 **176** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-176**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-176**

---

### 151. [Dimensionality Reduction for Hyperspectral Image Classification](https://arxiv.org/abs/2609.10334)

**<font color=#1a73e8>作者：</font>** Mohamed Cherifi, Ammar Mesloub, Mohammed Nabil El Korso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the issue of supervised classification in the context of hyperspectral satellite images. It deals with two fundamental aspects: dimensionality reduction of data and the selection of appropriate supervised classification techniques.
Firstly, we delve into dimensionality reduction, a critical step in simplifying the management of hyperspectral data. The reduction aims to decrease complexity in terms of memory and computing time. We examine two commonly used methods: Principal Component Analysis (PCA) and Linear Discriminant Analysis (LDA).
Subsequently, we explore the selection of the most suitable supervised classification algorithms for hyperspectral images. We compare the performance of three methods: K-Nearest Neighbors (KNN), Support Vector Machines (SVM), and Random Forest (RF) using real hyperspectral data. The results highlight that the combination of PCA and RF yields the highest overall accuracy and Kappa coefficient.

---


### 152. [Cyber-Financial Contagion: Modeling the Propagation of an AI Vendor Compromise Through the Banking System](https://arxiv.org/abs/2609.10350)

**<font color=#1a73e8>作者：</font>** Alex Leytes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The banking system now depends on a small set of shared artificial intelligence vendors for fraud screening, credit decisioning, anti-money-laundering triage, customer analytics, and internal decision support. This paper studies how a compromise inside one of those vendors can propagate along a chain of operational, informational, and financial linkages until it triggers losses that look, from the outside, like a classical banking crisis. We build a four-layer heterogeneous network that couples AI vendors, financial institutions, interbank exposures, and customer accounts, and we propose CFC-Prop, a stochastic epidemic-and-clearing model that runs on that network. On a synthetic dataset with 60 vendors, 220 banks, roughly 2,500 vendor-bank service edges, and 1,400 interbank exposures, CFC-Prop reproduces the heavy-tailed loss distributions and the sharp dependence on patch latency that are consistent with prior cyber-financial evidence. We also train an early-warning model, CFC-GNN, that uses vendor-side incident telemetry and graph structure to flag high-cascade-risk vendors before impact. Across four baselines the proposed model reaches AUROC 0.82 and AUPRC 0.60 while keeping calibration errors bounded. We release the full code, synthetic data, and reproducible scripts. The results argue that cyber concentration among AI vendors is a first-order financial-stability problem and give supervisors a concrete quantitative tool for reasoning about it.

---


### 153. [A Later Test Set Is Not a New Domain: Pretraining Familiarity Survives a Contamination-Free Hold-Out](https://arxiv.org/abs/2609.10357)

**<font color=#1a73e8>作者：</font>** Mahdi Naser Moghadasi, Faezeh Ghaderi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models are evaluated almost exclusively on public archives that predate them, so a strong score cannot be separated from having seen the test set during pretraining. The obvious remedy is a hold-out that postdates the models. We build one: thirteen forecasters -- four classical, three trained per dataset, six pretrained -- on seven groups drawn from five domains, every observation published after the last model was released, and every dataset rebuildable without an API key. Under this protocol pretrained models win 5 of 7 groups, lose one to a Theta baseline, and on daily exchange rates are indistinguishable from a seasonal naive forecast, along with every other method tested.
We then ask what separates the wins from the losses, and report a negative result: the two intrinsic properties one would reach for -- seasonal strength and spectral entropy, measured on the input window -- do not account for the pattern, and seasonal strength is if anything negatively associated with the advantage. What does track it is corpus familiarity. Our largest gain (28% lower MASE than the best classical method, on weekly Wikipedia pageviews) falls on Wikipedia pageviews, the domain TimesFM's authors describe as the bulk of its pretraining corpus, at the same granularities and differing only in time window. Within the pretrained family, where every model forecasts identical series so that series difficulty cancels, the TimesFM family outranks the Chronos family by -0.53 ranks on Wikipedia against -0.09 everywhere else (1,500 vs. 754 series, Mann-Whitney p < 1e-5). We conclude that a temporal hold-out removes memorisation of a window but not familiarity with a domain, that benchmarks therefore need domain hold-outs stated relative to disclosed corpora, and that the practitioner's question is less which model is better than whether their domain is one the model was raised on.

---


### 154. [SceneHI: High-Resolution 3D-Consistent Scene Texturing with Controllable Illumination](https://arxiv.org/abs/2609.10363)

**<font color=#1a73e8>作者：</font>** Athanasios Tragakis, Marco Aversa, Daniela Ivanova 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> SceneHI is a framework that lifts high-resolution, illumination-aware priors from 2D diffusion models to perform 3D texture synthesis. It is the first to demonstrate that high-resolution textures, previously limited to 2D synthesis, can be generated directly on 3D objects without model fine-tuning or optimization. Designed for complex, multi-object environments, SceneHI uniquely combines 3D-consistency, high-resolution fidelity, and physically plausible baked shadows within a single generative pipeline. To enforce strict geometric coherence, we introduce an exact analytical pixel-to-texel mapping that aligns diffusion trajectories across multiple viewpoints. We utilize High-Resolution Latent Textures (HRLTs) as a persistent canvas for gradually denoised textures, while camera views perform the denoising steps in latent pixel space. This ensures a shared base texture that can be subsequently refined to high resolution without compromising multi-view consistency. Finally, a light-aware generative pass embeds realistic geometry-consistent shadows directly into the atlases, bridging the gap to production workflows. SceneHI achieves high visual fidelity while reducing generation time by 80% compared to existing scene-level methods.

---


### 155. [OmniMed-FL: A Robust Multimodal Federated Learning Framework for Clinical Diagnosis](https://arxiv.org/abs/2609.10364)

**<font color=#1a73e8>作者：</font>** Ayush Debnath, Ruelia Saha, Sudip Misra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simultaneous assessment of medical imaging and patient records is often required in clinical diagnosis. However, standard machine learning algorithms cannot analyze these data types together. Meanwhile, compliance with HIPAA and GDPR can constrain centralized aggregation of sensitive patient data. This leaves a crucial void of secure fusion of visual and textual context across distant networks. Thus, we present OmniMed-FL, a controlled systems study of multimodal federated learning for five-class clinical condition classification (Normal, Pneumonia, COVID-19, Pleural Effusion, Cardiomegaly). Our proxy corpus pairs 3,000 public chest radiographs with 3,000 class-conditioned synthetic notes, matched by class, not by patient. The framework benchmarks eight fusion strategies, three initializations, four missing-text imputation rules, and matched federated baselines under non-IID Dirichlet partitioning across 3 to 20 hospital clients. As all notes are synthetic and pairing is not patient-level, these are descriptive proxy comparisons, not estimates of diagnostic performance or deployment readiness. Within those limits with clients ($K=5$) and severe skew ($\alpha=0.1$), local-only training achieves a macro-F1 score of 0.297, FedAvg achieves $0.662\pm0.074$, FedProx $0.737\pm0.085$, a matched FedMME-style one-shot ensemble $0.647\pm0.080$, and our SCAFFOLD-AdamW adaptation $0.070\pm0.015$, the 0.075 FedProx-FedAvg gap falling inside the wider of the two two-seed standard deviations. Over a $4\times3$ grid, label skew costs up to 0.27 F1 whereas a near-sevenfold client increase costs at most 0.10, while bidirectional volume grows linearly to 183.5 GiB at $K=20$. Multimodal fusion leads on both corpora, scoring 0.956 against 0.934 for text and 0.664 for images on the synthetic corpus and 0.906 against 0.880 and 0.737 on the radiograph corpus, for $2.3\times$ the model state of text alone.

---


### 156. [Beyond Weak Labels: Prompt-Guided Local Refinement for Weakly Supervised Water Segmentation in High-Resolution Multispectral Imagery](https://arxiv.org/abs/2609.10371)

**<font color=#1a73e8>作者：</font>** Muhammad Farhan Humayun, Mohammad Imangholiloo, Afifah Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution water mapping supports environmental monitoring and related applications, but accurate pixel-level labels are difficult and costly to produce. Official hydrographic vectors provide scalable weak supervision, but they contain artifacts like boundary noise, temporal mismatch, and omissions of small water structures. We propose a two-stage framework for weakly supervised water segmentation in high resolution multispectral imagery. Stage 1 learns initial masks from rasterized vector pseudo-labels, and Stage 2 converts these masks into structured component-wise prompts for localized refinement. On a manually corrected validation set, refinement improves SegFormer-B0 from 0.9509 to 0.9535 IoU and U-Net from 0.9408 to 0.9486 IoU, with corresponding F1 gains from 0.9749 to 0.9762 and 0.9695 to 0.9736. It leads to sharper shorelines, reduced boundary spillover, and better thin-structure delineation. The results indicate that prompt-guided refinement can improve pseudo-label-based water segmentation by targeting local errors that are poorly captured by global training supervision.

---


### 157. [Shape-guided Gaussian Splatting for Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2609.10376)

**<font color=#1a73e8>作者：</font>** Pranav Poudel, Florence Dell'Aniello Picard, Nairouz Shehata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view X-ray 3D reconstruction is essential for reducing radiation exposure, but recovering a density field from a handful of X-ray projections is severely ill-posed. Recently, 3D Gaussian Splatting has achieved state-of-the-art performance in sparse-view reconstruction by representing the volume using explicit, optimized primitives, but it requires dozens of projected views. With fewer views, reconstruction quality degrades severely since the explicit primitives are optimized freely without any anatomical information. Anatomical structures, in contrast, share similar geometry and density across a population. Their variations are bounded within a limited range that statistical shape models can capture. This paper proposes a shape-guided Gaussian splatting framework for sparse-view X-ray 3D reconstructions. Our contribution lies in driving Gaussian positions toward anatomically valid configurations, alongside atlas-based density regularization. Our method ensures anatomically consistent reconstruction and improves PSNR by 2.83 dB over a state-of-the-art Gaussian splatting baseline with as few as 5 views. Code Available: this https URL

---


### 158. [MOONWALK: Mediating Operations with Intent-Evidence-Action Alignment Across Junior-Supervisor Review Workflows in Animation/VFX Pre-Production](https://arxiv.org/abs/2609.10385)

**<font color=#1a73e8>作者：</font>** Shih-Yu Lai, Wen-Fan Wang, Sai Ling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Animation and VFX pre-production review requires teams to translate loosely specified creative intent--briefs, evolving specifications, heterogeneous references, and verbal decisions--into revisions that junior artists can execute without repeated clarification. In practice, criteria drift across iterations, review judgments lose their evidential basis, and the reasoning behind a request rarely survives the senior-junior handoff. We contribute a design framework for intent-evidence-action alignment: intent is articulated into a shared project record, judgments are anchored to grounded evidence, and authorized decisions are converted into clear revision tasks tied directly to reference notes. We instantiate this framework in MOONWALK, a professional pre-production review system comprising a shared intent record, reference/specification anchoring, structured work-in-progress comparison, and supervisor-authorized action planning. In this workflow, AI handles administrative coordination--flagging missing context and organizing notes--while artists retain full creative direction. An in-studio study with professional practitioners compares MOONWALK with a chat-only (chatbot) interface using matched production materials, while participants' existing workflows provide a retrospective ecological baseline. Results indicate stronger intent alignment, decision traceability, and checklist executability, while also showing that aesthetic authority and final prioritization must remain with practitioners. The evaluation establishes the value of the integrated structured workflow over unstructured conversational AI chatbot. Code: this https URL

---


### 159. [Enhanced Deformable Convolution with Center-invariant Offset and Edge-aware Mask](https://arxiv.org/abs/2609.10387)

**<font color=#1a73e8>作者：</font>** Yixiao Li, Xiaoyuan Yang, Jin Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable convolution networks have recently become popular for many computer vision tasks, especially for semantic segmentation, because of their exceptional capabilities in dynamic spatial modeling. However, due to the dense deformable offsets and the lack of longer-range dependencies, they can not fully adopt proper and precise deformations for feature representations. To tackle the issues, in this paper, we propose Enhanced Deformable ConvNets (EDCN) for semantic segmentation. Specifically, a novel Enhanced Deformable Convolution (EDC) is exploited in the decoder, which integrates the Center-invariant Offset Module (COM) and Edge-aware Mask Module (EMM). The COM employs larger kernels and eliminates deformations at the kernel center, obtaining offsets that are more in line with the target from richer spatial information. Concurrently, the EMM obtains the significance of image content via Sobel edge detection, then selectively applies deformations based on the content significance, minimizing unnecessary deformations associated with relatively less important information, thereby avoiding impact from less informative regions. Experiments show that EDC outperforms state-of-the-art deformable convolution variants, including Deformable ConvNets V1-V4 and Entire Deformable ConvNets, across mainstream segmentation datasets with various decoder settings. Moreover, ablation studies confirm the effectiveness of each component. In addition, visualizations illustrate that EDC enhances spatial adaptation and target focus. We further analyze the extendibility of EDC to larger kernels on the image classification benchmark. Code will be publicly released.

---


### 160. [Rosetta at AlexandriaX-2026: LoRA-Adapted NileChat for Context-Aware Dialectal Arabic Dialogue Translation](https://arxiv.org/abs/2609.10395)

**<font color=#1a73e8>作者：</font>** Nada Esmaeil, Fathima Rena, Sibi Subhash 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the Rosetta system for Subtask 1 (Context-Aware English-to-Dialectal Arabic Dialogue Translation) of the AlexandriaX shared task, participating in both constrained and unconstrained tracks. The approach fine-tunes a LoRA adapter on NileChat-3B using structured system/user prompts that condition generation on dialect and dialogue context. For the unconstrained track, the adapter is additionally pretrained on MADAR and PADIC. Rosetta ranked 4th in the constrained track (spBLEU 26.10) and 5th in the unconstrained track (spBLEU 25.09). The experimental results demonstrate that external pretraining helps only two of thirteen dialects while slightly hurting overall performance, suggesting negative transfer.

---


### 161. [JarvisGUI: Towards Cross-Device GUI Agents with Dynamic Task Composition](https://arxiv.org/abs/2609.10451)

**<font color=#1a73e8>作者：</font>** Zixiang Chen, Yuheng Lu, Zihao Cheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world GUI usage frequently involves workflows that span multiple devices and platforms, requiring the transfer of intermediate results, maintenance of shared state, and coordination across heterogeneous environments. However, existing GUI benchmarks overwhelmingly evaluate agents on single-device, statically defined tasks, thus leaving such cross-device capabilities largely unexamined, resulting in an overly optimistic assessment of agents' readiness for real-world usage. We introduce JarvisGUI, a dynamic benchmark that evaluates GUI agents on cross-device workflows requiring coordinated interaction across heterogeneous platforms, including Android, Windows, and Ubuntu. Specifically, JarvisGUI formulates GUI tasks as input-output transformations under a lightweight type system, which allows us to automatically compose multi-step, cross-device workflows and dynamically evaluate agent performance within a unified framework. By evaluating agents in virtual environments spanning multiple operating systems, JarvisGUI reveals that state-of-the-art open-source GUI agents struggle with the state-transfer awareness, cross-platform contextual reasoning, and long-horizon dependency management required for real-world workflows, exposing a critical capability gap invisible to existing benchmarks.

---


### 162. [Advanced Brain Tissue Imaging with Data-Consistent Diffusion Priors in Laminographic X-Ray Nanoimaging](https://arxiv.org/abs/2609.10456)

**<font color=#1a73e8>作者：</font>** Wenxuan Fang, Abraham L. Levitan, Ana Diaz 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nanoscale imaging of mammalian brains is critical for connectomics. X-ray laminography enables high-throughput imaging of extended, plate-like biological specimens. However, the tilted acquisition geometry leads to incomplete Fourier-space coverage, giving rise to a missing-cone of information. Conventional reconstruction methods cannot recover unmeasured information within the cone, resulting in artifacts that distort fine brain structures. While resolving these requires modeling 3D structure, direct 3D deep learning approaches are limited by data scarcity and computational cost. Here we introduce LUCID (Laminography with Unified Consistent Diffusion), a framework that combines multi-view diffusion priors with projection-domain data consistency. LUCID integrates complementary 3D structural information while enforcing strict alignment with the laminography forward model. On simulated datasets, LUCID substantially improves spatial fidelity and restores missing Fourier components, outperforming baseline methods. Applied to experimental laminography data, LUCID generalizes robustly despite being trained exclusively on fully sampled tomographic volumes, and effectively recovers unmeasured Fourier information.

---


### 163. [Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](https://arxiv.org/abs/2609.10464)

**<font color=#1a73e8>作者：</font>** Andy Zeyi Liu, Haoran Sun, Lucas Baker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate physically realistic dynamics remains hitherto untested. In this work, we introduce SemiGroup-JEPA (SG-JEPA), which extends the LeWorldModel framework by supplying the parameter governing the physics to the temporal model via action-conditioning and jointly training an encoder and predictor through an autoregressive latent rollout. To evaluate the model's ability to generalize out of distribution, we design dynamical tasks under different gravitational fields that, despite obeying the same physical law, exhibit qualitatively different dynamics, ranging from floating motion in weak gravitational fields to rapid bouncing in strong ones. In contrast to DINO-WM, SG-JEPA reduces open-loop prediction error by up to 2 times on two-dimensional datasets, and increases control success rate up to 2.5 times for three-dimensional robotic datasets, for which we train independent diffusion policies. To explain this advantage, we develop a linear feature model that separates local law-conditioned error from its recursive amplification under rollout. Guided by this model, we find that back-propagating the multi-step rollout loss into the representation trains the encoder to keep the features that the predictor can carry forward, and that those are the features the dynamics depend on, so most of the gain comes from the encoder learning better features rather than from the predictor learning better dynamics. See project page at this https URL.

---


### 164. [AgroVisNet: A lightweight Convolutional Network and the BD-PlantDX Expert-Validated Benchmark for Radish, Potato and Pointed Gourd Disease Classification](https://arxiv.org/abs/2609.10469)

**<font color=#1a73e8>作者：</font>** Md. Abdullah Mandal, Saad Ahmed, Md. Khalid Syfullah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated plant disease diagnosis is increasingly deployed on farmer-held devices in regions where agronomic expertise is scarce and network connectivity is unreliable. Three obstacles limit its practical value: public benchmarks are dominated by a small set of non-native crops, region-specific datasets are rarely validated by domain experts, and the architectures that reach competitive accuracy carry parameter budgets that are unsuited to low-cost hardware. We propose AgroVisNet, a compact convolutional network trained from scratch, together with BD-PlantDX, an expert-validated benchmark of 12,432 field images spanning 12 classes of radish, potato and pointed gourd in healthy and diseased states, collected across the Bogura and Nilphamari districts of Bangladesh. AgroVisNet couples grouped bottleneck residual blocks carrying sequential channel and spatial attention with multi-scale depthwise blocks and a dual-pooling classification head, reaching 290,572 trainable parameters. On BD-PlantDX the model attains 99.52% test accuracy and 99.52% weighted F1, exceeding all six ImageNet-pretrained lightweight backbones evaluated under an identical protocol while using 8.7 to 16.8 times fewer parameters and 1.3 to 8.5 times fewer multiply-accumulate operations. Exported for deployment, the model quantises to a 0.46 MB full-integer network at a 0.22 percentage-point accuracy cost and classifies an image in 8.40 ms on a single CPU. Across five random seeds accuracy remains at 99.57 +- 0.10%, a ten-variant ablation isolates the contribution of each component, and the same architecture transfers without redesign to two independently collected datasets at 98.71% and 99.05% accuracy. Grad-CAM evidence indicates that predictions rest on lesion-bearing leaf regions rather than on background cues.

---


### 165. [Nonmaximal sums of maximally monotone operators under Rockafellar's constraint qualification](https://arxiv.org/abs/2609.10487)

**<font color=#1a73e8>作者：</font>** Weifeng Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We construct counterexamples to Rockafellar's sum conjecture in which two maximally monotone operators satisfy the interior-domain condition but their sum is not maximally monotone. We give one counterexample on $c_0$ and another on $\ell^1$ with its usual norm. We establish a general construction theorem that computes the entire monotone polar of a class of graphs, gives a necessary and sufficient condition for their maximal monotonicity, and shows how a positive rank-one perturbation yields a nonmaximal sum under this condition. We verify the theorem's hypotheses and its maximality criterion on $c_0$, thereby obtaining a counterexample to the conjecture. Furthermore, we construct a bounded linear surjection from $\ell^1$ onto $c_0$ and use it to obtain the counterexample on $\ell^1$.

---


### 166. [Artificial Intelligence Literacy and Sustainable Development: An Ethical Governance and Development Goals Framework](https://arxiv.org/abs/2609.10489)

**<font color=#1a73e8>作者：</font>** Md. Masudul Islam, Mirza Niaz Morshed, Md. Shafiqul Islam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI literacy provides foundational competencies that support ethical, transparent, and sustainable technological development, although higher-order capabilities such as governance, critical evaluation, and strategic decision-making extend beyond basic literacy into advanced levels of AI competency. This study positions AI literacy as a governance capacity that complements and strengthens all 17 SDGs. It introduces a six-level taxonomy of artificial intelligence reasoning and ethics that extends traditional learning models by incorporating ethical judgement and strategic foresight. This taxonomy forms the foundation of an integrated framework linking education, governance, and sustainable development. A survey of 300 participants from diverse professional backgrounds within a national context which reveals strong technical awareness but limited ethical and governance readiness, highlighting critical gaps in public capacity to manage artificial intelligence responsibly. Findings show that ethical reasoning and reflective thinking are the strongest predictors of sustainable and trustworthy artificial intelligence use. The study proposed to embed literacy-based competencies into curricula, institutional policies, and governance mechanisms to accelerate equitable and responsible progress toward sustainable development goals

---


### 167. [Learning with Covariance Matrices: Principal Component Analysis Meets Learning with Graphs](https://arxiv.org/abs/2609.10490)

**<font color=#1a73e8>作者：</font>** Saurabh Sihag, Andrea Cavallo, Elvin Isufi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This feature article provides an overview of the theoretical foundations for coVariance neural networks (VNNs), i.e., graph neural networks (GNNs) operating on covariance matrices as graphs. Covariance matrices are ubiquitous across domains, and hence, the deployment of GNNs often leverages graphs of pairwise statistical dependencies. Existing theoretical contributions on GNNs consider abstract graph representations and cannot accommodate the data-driven nuances associated with covariance matrices. This tutorial brings into focus various novel theoretical insights via mathematical analyses of VNNs that have broad signal processing implications, including: (i) a conceptual equivalence between VNNs and principal component analysis (PCA)-based information processing; (ii) refined stability bounds on predictive outcomes in the presence of finite sample-induced covariance matrix perturbations; and (iii) refined characterization of transferability of VNNs across multiscale datasets. The theoretical insights discussed herein provide the underlying principles and justification towards adopting VNNs over workhorse PCA-based learning pipelines, in applications where covariance matrices are useful descriptors of data structure. We also convey how impact of these foundational advances permeates to \textit{principled} designs and applications of learning methods across broad domains where covariance matrices emerge. Notably, we elucidate the conceptual insights facilitated by VNNs to the specific task of characterizing brain age gap for neurodegenerative conditions using neuroimaging datasets, a timely problem in computational neuroscience. Broader impacts to other application domains are discussed as well.

---


### 168. [IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier](https://arxiv.org/abs/2609.10494)

**<font color=#1a73e8>作者：</font>** Blake Stenstrom, Charangan Vasantharajan, Brian Sathianathan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprises deploy systems, not checkpoints. Usable capability depends jointly on weights, serving route, precision, output contract, and harness, yet all 18 audited benchmarks score advertised model identifiers. We treat this as measurement error and give a protocol that makes it reportable. It has three parts. A gold-blind capability-binding preflight verifies that a route can execute the evaluation contract before any task reaches it; a reliability-inclusive first-pass scoring rule keeps failure in the score while keeping unsupported capability out; and adjudication is structurally score-blind. We call the protocol IB2 and release its algorithms, classification tables, request contract, and manifest schemas. Its reference instantiation, 128 locked tasks and 987 assertions over document, spreadsheet, chart, tool and database work, stays sealed: the procedure is the artifact, not the corpus. Across eleven systems, four results. Capability availability is measurable: two complete single-route runs on identical weights later failed distinct predicates of the finalized binding gate, while a third passed that gate before a fresh run. The advertised identifier exposed neither limit. Discrimination is not uniform: four of seven suites saturate under a six-system band, with the spread almost entirely from governed database work and multi-tab joins, so we report interval-backed resolution groups, not ranks; two of the nominal five-label output's four cuts fail multiplicity adjustment. Serving-arm choice moved one declared revision and precision from 77.38 to 82.54, paired interval [0.11,10.60], though the arms differ in access mode, harness generation, and the serving tool-call parser, and harness generation is a property of our evaluator, not any endpoint. Excluding failed responses from denominators changes the point ordering, so reliability inclusion changes a conclusion, not its wording.

---


### 169. [Cross-Model Agreement as a Deployment-Time Reliability Signal for Automatic Polyp Segmentation](https://arxiv.org/abs/2609.10495)

**<font color=#1a73e8>作者：</font>** Siddharth Gupta, Jitin Singla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-time colonoscopy, ground-truth annotations are unavailable at inference, so polyp segmentation models can fail silently. We propose Referee-Based Quality Estimation (RBQE), a reference-free framework measuring agreement between a primary segmentation model and an independently trained referee on the same image. RBQE is evaluated on a standardized 1,223-image external benchmark drawn from four public datasets, using four referee configurations chosen to separate two design axes: referee independence and architectural diversity. Using a common Agreement Dice descriptor, a same-architecture referee differing from the primary model only in random initialization already yields a useful reliability signal (ROC-AUC = 0.923), showing that independent training alone is sufficient. Cross-architecture referees improve further: SegFormer-B0 achieves the strongest performance (ROC-AUC = 0.960), significantly outperforming the same-architecture control and UNet++, and exceeding a representative Test-Time Augmentation baseline by 0.055 ROC-AUC under an identical protocol, whereas a prompt-coupled MedSAM referee underperforms despite maximal architectural diversity. Because empty-mask agreement is trivially separable, we also report a restricted evaluation excluding such cases: ROC-AUC falls to 0.876 (SegFormer-B0, 1,046 images) and 0.783 (same-architecture control, 975 images), yet RBQE's margin over both baselines widens on this identical subset. RBQE additionally increases the mean Dice of retained predictions as low-agreement cases are progressively rejected, supporting selective prediction, and requires only one additional deterministic referee forward pass at inference. Our study therefore supports cross-model agreement as a practical, interpretable reliability framework for automated polyp segmentation.

---


### 170. [Field Converter: Geometry-Initialized Temporal Residual Refinement for World-Grounded Player Pose Estimation from Soccer Broadcasts](https://arxiv.org/abs/2609.10498)

**<font color=#1a73e8>作者：</font>** Simon Khan, Laurent Gajny, Jennyfer Lecompte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D human pose from monocular sports broadcasts remains challenging when players must be localized in a shared metric world coordinate system rather than only reconstructed relative to their own body. We introduce Field Converter, a geometry-initialized temporal residual framework for world-grounded 3D player pose estimation from calibrated soccer broadcasts. Our method first uses camera and pitch geometry to initialize the player root through ray-ground intersection, then predicts a temporal residual correction from pose, image, camera, and geometric cues. On match-disjoint evaluation sequences, residual refinement reduces root error from 49cm with geometry alone to 14cm with a frame-wise MLP and 10cm with a TCN, while a Transformer achieves a comparable 11cm. The resulting world-space MPJPE reaches 13.2cm, and ablations show that residual prediction clearly outperforms direct global-root regression while temporal context matters more than the specific temporal backbone. Failure analysis further identifies airborne motion as the main limitation of the ground-based geometric initialization.

---


### 171. [Wicked Problem, Parsimonious Solution: Securing Electric Vehicle Charging Station Software](https://arxiv.org/abs/2609.10502)

**<font color=#1a73e8>作者：</font>** Emma Sheppard, Zachary Wadhams, Dalton Arford 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electric vehicle charging infrastructure presents a suite of novel cyber-physical threats. Among this infrastructure, charging stations are the most vulnerable elements. The software in the charging station supply equipment is particularly vulnerable. Currently, the software is an attack surface that is largely unprotected and poorly characterized. To represent the vulnerabilities in this attack surface, we advocate for applying modern software quality assurance to characterize vulnerabilities in electric vehicle charging station software. Specifically, we advocate for the application of hierarchical software quality assurance (HSQA) to specialized electric vehicle charging station software. HSQA provides a comprehensive view of the code quality and security -- from the level of individual vulnerabilities (e.g., CVEs) to high level characteristics (e.g., CIA Triad). HSQA incorporates quality and security considerations throughout the software development lifecycle. Thus, our position is that HSQA is an excellent approach for assessing electrical vehicle charging station software.

---


### 172. [Quantum Feature Engineering for Credit Default Prediction: When and Why IQP Circuits Help Linear Classifiers](https://arxiv.org/abs/2609.10505)

**<font color=#1a73e8>作者：</font>** Menachem Finkelstein, Diana Legziel Levy, Zohar Yakhini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Credit default prediction is a tabular classification problem in which modest gains in F1 translate directly into reduced financial exposure. We ask whether Instantaneous Quantum Polynomial-time (IQP) circuits can produce features that improve a classifier over both its raw classical baseline and Kernel PCA - the strongest unsupervised classical non-linear alternative - at an equal feature budget. The dataset provides 23 financial attributes per client; for an n-qubit circuit we select n of them, encode each as a rotation angle, and read 2n expectation values back out as new features. The motivation for using a quantum circuit is computational: an n-qubit IQP circuit runs in constant depth and encodes feature correlations in a 2^n-dimensional Hilbert space, whereas classical simulation of its exact output statistics scales exponentially in n. Using the UCI Default of Credit Card Clients dataset and five-fold cross-validation, we find that appending 16 IQP features (n = 8 qubits) to a Logistic Regression model raises F1 from 0.462 to 0.517 (+0.055, p < 0.0001). Kernel PCA, the next-best method, reaches only 0.493 at the same feature count; the gap survives Benjamini-Hochberg correction across 12 tests (p = 0.00007). No other classifier - Random Forest, SVM, XGBoost, or k-NN - benefits, which points to a linear-expressivity mechanism rather than a generic improvement. We also show that how the 8 input features are chosen matters: Random Forest importance-guided selection reaches F1 = 0.523, while encoding maximally uncorrelated features drops it to 0.496, demonstrating that the circuit amplifies informative structure rather than creating it from scratch.

---


### 173. [Precision in Rice Variety Classification using Stacking-Based Ensemble Learning](https://arxiv.org/abs/2609.10524)

**<font color=#1a73e8>作者：</font>** Md. Masudul Islam, Galib Muhammad Shahriar Himel, Md. Golam Moazzam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rice, a staple food for a significant portion of the global population, exhibits remarkable diversity in its varieties, presenting substantial challenges for accurate identification by consumers, traders, and farmers. This complexity often facilitates fraudulent practices, such as the unauthorized mixing of rice types, which undermines quality and trust in the supply chain. Despite its critical importance, existing research falls short of providing robust and efficient methods for precise rice variety classification based on external characteristics like color, size, and texture. To address this gap, our study introduces a comprehensive rice variety identification framework designed to enhance transparency and quality assurance. We developed a stacked ensemble model tailored for rice variety classification and curated a comprehensive dataset comprising 20 rice varieties, each distinguished by unique visual attributes. The proposed approach achieved an unprecedented classification accuracy of 100%. Furthermore, we integrated our model into a mobile application, enabling even novice users to effortlessly identify rice varieties using grain images from a smartphone camera. These findings underscore the transformative potential of advanced machine learning techniques in mitigating fraudulent practices and ensuring stringent rice quality control. Our work holds significant implications for agricultural stakeholders, paving the way for automated crop identification systems and advancing precision agriculture practices.

---


### 174. [A positive resolution of the gap-entropy conjecture](https://arxiv.org/abs/2609.10529)

**<font color=#1a73e8>作者：</font>** P. M. Aronow, Nathan Kallus, Patrick Lopatto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove the gap-entropy conjecture for fixed-confidence best-arm identification with independent unit-variance Gaussian arms, means in $[0,1]$, and a unique optimal arm. For each suboptimal arm $i$, let $\Delta_i=\mu_*-\mu_i$ be its gap from the optimal mean, and write $H=\sum_{i\ne *}\Delta_i^{-2}$. Let $p_r$ be the fraction of $H$ contributed by arms with $2^{-(r+1)}<\Delta_i\le2^{-r}$, and let $\mathrm{Ent}(I)=\sum_{r:p_r>0} p_r\log(1/p_r)$. Among all algorithms that identify the optimal arm with probability at least $1-\delta$ on every Gaussian instance, the optimal expected number of samples on a given instance, averaged over all permutations of the arm labels, is within absolute constant factors of $H(\log(1/\delta)+\mathrm{Ent}(I))$. Moreover, there is an algorithm, independent of the instance, whose expected number of samples is bounded by a constant multiple of this quantity plus $g^{-2}\log\log(e^e/g)$, where $g=\min_{i\ne *}\Delta_i$ is the gap to the closest competitor.

---


### 175. [Guiding Image-to-3D Generation with Test-Time Partial Observations](https://arxiv.org/abs/2609.10531)

**<font color=#1a73e8>作者：</font>** Jerred Chen, Simon Weber, Ronald Clark  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-3D models can generate visually compelling 3D assets from a single RGB image, but their geometry is often only loosely constrained by the available observations, limiting their use in applications that require geometric fidelity. In many real-world settings, however, partial geometric observations of the object may be available at test time. We introduce a training-free framework for incorporating such evidence into pretrained image-to-3D generative models without retraining or finetuning. To do this, we guide generation using a ray-consistent observation likelihood defined over the model's occupancy representation, combining surface occupancy and free-space evidence. Applied to SAM 3D and its multi-view extension, our approach substantially improves geometric fidelity across different levels of observability, as well as visual quality. Our results demonstrate that pretrained image-to-3D models can effectively integrate partial geometric observations through explicit test-time guidance, complementing their learned generative priors without modifying the underlying model.

---


### 176. [Programmable World Model](https://arxiv.org/abs/2609.10540)

**<font color=#1a73e8>作者：</font>** Zheng-Hui Huang, Guixu Lin, Jiacheng Lin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video world models generate increasingly realistic and interactive visual experiences, yet lack reliable mechanisms for maintaining persistent world state and enforcing programmable rules over extended interactions. We introduce Programmable World Model, a framework that decouples world-state evolution from visual observation generation. An agent translates natural-language instructions into executable programs that specify entity states and state-transition rules, enabling direct control over individual entities and their interactions. A lightweight engine executes these programs to update and maintain an explicit, persistent global world state, including off-screen entities and non-visual attributes. To connect world state with visual generation, we introduce state-augmented 3D oriented bounding boxes (OBBs) as an intermediate representation. This representation, together with the target camera trajectory, is deterministically compiled into pixel-aligned spatiotemporal conditioning signals for a pretrained video model serving as the generative renderer. This design allows users to create playable games with predefined mechanics, direct control over individual entities, and persistent world state throughout gameplay. We further introduce CombatStateBench, a benchmark for evaluating programmable world models. On CombatStateBench, our method achieves 94% Count Accuracy and 98% State Accuracy, substantially outperforming existing interactive video world models while supporting coherent long-horizon generation. These results demonstrate the effectiveness of separating explicit state evolution from generative rendering for building persistent, programmable worlds.

---


> [!TIP]
> 当前位于：**151-176**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-176**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
