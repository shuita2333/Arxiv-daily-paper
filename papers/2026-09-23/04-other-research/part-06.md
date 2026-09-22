# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 251. [BindCLIP: One Balanced Coupling For Compositional Vision Language Scoring](https://arxiv.org/abs/2609.23717)

**<font color=#1a73e8>作者：</font>** Liuyang Song, Yi Zhang, Zhongyi Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global vision--language similarities compress an image and a caption into one vector, preserving semantics but not which word corresponds to which region or how those regions are arranged; a model can recognize every word and object yet prefer a compositionally incorrect caption. We argue that a frozen encoder retains this association structure, so the problem is to read it rather than to rebuild it beside the pretrained similarity. We introduce BindCLIP, a pairwise scorer built on one latent object: a balanced token--patch--depth optimal-transport coupling that places both candidate captions and several visual depths in a single plan. Semantic, entity, order, and spatial evidence are read as energies of this state, and exchanging the candidates permutes the plan, making the score exactly antisymmetric. A geometric refinement inside the coupling contracts moves that the candidates and the visual depths do not support. No task label, parser, relation inventory, or detector is used. One checkpoint and one inference path improve the official What'sUp, ARO, and SugarCrepe benchmarks over frozen global CLIP, with the strongest transfer on the relation splits. Controls rule out patch access and caption-length shortcuts, and an inference-time lesion localizes spatial arrangement to the coupling.

---


### 252. [VGGT-Prime: Compute-Adaptive Mixture-of-Heads for Efficient Visual Geometry Transformers](https://arxiv.org/abs/2609.23733)

**<font color=#1a73e8>作者：</font>** Abteen Arab, Guile Wu, Chengjie Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward visual geometry models such as the Visual Geometry Grounded Transformer (VGGT) have recently enabled direct 3D reconstruction from multi-view images. Despite their promising performance, these models scale quadratically with the number of input views due to their global attention mechanism, resulting in substantial latency for long sequence inputs. There have been some recent efforts to accelerate VGGT, but they primarily focus on reducing \emph{token redundancy} through token merging or key/value sparsification. Our work resolves this bottleneck from a different perspective by investigating \emph{architectural redundancy} in visual geometry transformers. We show that the multi-head attention modules in VGGT's global-attention layers contain substantial architectural redundancy, with only a subset of heads carrying critical geometric information. In light of this observation, we propose VGGT-Prime, a compute-adaptive mixture-of-heads model that resolves this redundancy to accelerate visual geometry transformers while maintaining competitive reconstruction quality. The key idea of VGGT-Prime is to estimate the appropriate computation level for each global-attention head using a lightweight router and then dynamically assign each head to different computation modes. Extensive experiments on multiple datasets demonstrate that VGGT-Prime can achieve an {$8\times$} inference speedup over VGGT while maintaining competitive performance on camera pose, depth, and point-cloud predictions. We further show that VGGT-Prime is complementary to existing acceleration methods, such as token merging, further improving inference speed by up to $14{\times}$ over VGGT. An overview of our work is available on our \href{this https URL}{project page}.

---


### 253. [ScholarStack: Layered Research Asset Orchestration and Cross-Task Reuse for Scientific Agents](https://arxiv.org/abs/2609.23735)

**<font color=#1a73e8>作者：</font>** ScholarSeed AI Team, Ao Zhang, Caoqinwei Gong 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents support a range of literature-based research tasks, such as retrieval, question answering, evidence-grounded generation, and claim assessment. Most existing systems, however, are organized around individual tasks: the same papers are repeatedly retrieved, segmented, and interpreted, and the understanding built in one task is difficult to reuse in the next. We present ScholarStack, a layered research asset framework that compiles a paper collection into reusable, versioned, and provenance-preserving assets at three complementary levels: source-grounded paper-level statements, domain-level organization, and evidence-grounded cross-paper syntheses. A common access interface returns task-specific views at the evidence granularity each task requires, preserving study conditions, source traceability, and verification status. We instantiate the framework on four task families spanning ten task settings, comparing agents that use the compiled assets with task-specific baselines under matched base models. Quality gains concentrate on tasks that require cross-paper evidence, such as multi-paper question answering and literature review generation, and query-time token cost falls on every task where it is measured, with assets compiled once and reused across tasks. These results suggest that layered research assets can serve as shared infrastructure for scientific agents, shifting literature-based assistance from isolated document processing toward cumulative, evidence-grounded workflows.

---


### 254. [OnlineWM: Causality-Aware Active Online Learning for Effective World Modeling](https://arxiv.org/abs/2609.23753)

**<font color=#1a73e8>作者：</font>** Yikun Miao, Fangqi Zhu, Quanxin Shou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative world models aim to predict future states conditioned on actions, where action controllability is fundamental for reliable dynamics modeling. While recent efforts leverage simulator-generated data to enhance this capability, existing training pipelines face two fundamental limitations. First, static offline data collection leads to a distribution misalignment between training sets and the model's evolving error patterns, failing to resolve critical long-tail scenarios where dynamics predictions remain unreliable. Second, the standard objective of minimizing observational discrepancy often encourages the model to exploit spurious correlations instead of capturing the underlying action-effect causality. To address these limitations, we propose OnlineWM, an online training framework that continuously improves world modeling through active simulator interaction and causality-aware optimization. OnlineWM introduces two key innovations: (1) Active Online Learning: Instead of using fixed datasets, OnlineWM adaptively queries the simulator for new interaction sequences that target the model's current predictive weaknesses, ensuring high-utility data acquisition. (2) Causality-Aware Fine-Tuning: We propose a counterfactual learning strategy that contrasts the outcomes of different actions from identical states, forcing the model to attribute state transitions to specific actions rather than ambient environmental evolution, thereby grounding its predictions in reliable causal mechanisms. By integrating active data acquisition with causal optimization, OnlineWM establishes a closed-loop refinement process that ensures the model is both robust to diverse scenarios and precise in its causal attribution. Extensive experiments demonstrate that OnlineWM significantly enhances action controllability and generalizes effectively to unseen domains.

---


### 255. [Training-Free Spectral Transductive Refinement for Cross-Domain Few-Shot Classification](https://arxiv.org/abs/2609.23758)

**<font color=#1a73e8>作者：</font>** Fahim Rahman, S.M. Tanjeeb Meheran Rohan, Md. Taimum Ibne Sayed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot recognition with frozen visual features is especially fragile under domain shift and one-shot supervision, where a single labelled image is an unreliable estimate of its class. We ask how far this fragility can be reduced purely at test time, without retraining the encoder or augmenting the source domain. We present Spectral Transductive Refinement (STR), a training-free transductive inference rule that exploits the geometry of the complete support-query episode. Given frozen embeddings, STR builds a joint k-nearest-neighbour graph, maps the episode into a normalized-Laplacian spectral coordinate system, initializes class representatives from the labelled support, and iteratively refines them using pseudo-labelled queries. We evaluate STR under two protocols. A controlled component study with frozen ResNet-18 features shows that spectral refinement consistently improves over single-prototype spectral initialization across five shifted domains, with the largest gains in the one-shot regime where support estimates are weakest. We then benchmark STR against recent Cross-Domain Few-Shot Learning (CD-FSL) methods using the standard miniImageNet-pretrained ResNet-10 backbone over eight established target domains. Operating entirely at inference time, STR attains the highest 1-shot average among compared methods and remains competitive at 5-shot, rivalling approaches relying on heavy source-domain meta-training augmentations. Because STR is transductive, we report its setting explicitly. Diagnostics attribute its gains to iterative refinement in spectral coordinates rather than added prototype capacity, which remains inactive in our configuration.

---


### 256. [GenVoid: Uncertainty-Aware Learning of Subsurface Material Defects with an Experimentally Validated Physics-Informed Generative Model](https://arxiv.org/abs/2609.23761)

**<font color=#1a73e8>作者：</font>** Trishit Mondal, Prajwal Bharadwaj, Nikhil Karanjgaokar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Internal voids are ubiquitous defects in manufactured structures, yet their characterization remains challenging because their geometry is hidden and can only be inferred indirectly from accessible measurements. Here we introduce \textit{GenVoid}, a physics-informed generative model-based framework for identifying internal voids in complex two- and three-dimensional solids from surface displacement measurements alone. By incorporating the governing mechanics into a generative inference framework, \textit{GenVoid} enables void identification across linear elastic, hyperelastic and plastic material behaviours and accommodates complex two- and three-dimensional structural geometries. Importantly, the framework explicitly accounts for uncertainty and noise in displacement measurements, producing probabilistic reconstructions of internal void geometry rather than a single deterministic estimate. We demonstrate the approach using high-fidelity synthetic datasets and experimentally measured displacement fields obtained from in-situ mechanical experiments, establishing its ability to infer hidden voids from realistic displacement measurements. To quantify the fundamental limits of such inference, we further introduce an observability measure that characterizes the sensitivity of boundary measurements to localized stiffness perturbations within the interior under an ensemble of applied loads. This framework provides a direct connection between defect location, sensor configuration and reconstruction fidelity, enabling systematic assessment of how the number and spatial distribution of boundary measurements govern void-identification accuracy. To this end, these results establish a physics-informed and uncertainty-aware approach for non-invasive characterization of hidden defects and provide a quantitative basis for designing measurement strategies for inverse problems in solid mechanics.

---


### 257. [On Probabilistic Inference Through Parametric Tensor Decomposition in Base Tensor Networks](https://arxiv.org/abs/2609.23774)

**<font color=#1a73e8>作者：</font>** Sagad Hamid, Tanya Braun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic inference is generally only tractable in low-treewidth graphical models, limiting its effective applicability in high-treewidth settings. Many existing methods improve efficiency by exploiting specific parametric structure, such as symmetries. However, they typically require such structure to be explicitly present, limiting their applicability to a broader range of graphical models. To address this limitation, we propose a framework where tractable inference is controlled by latent parametric structure exploitation, rather than requiring it to be explicitly present a priori. Our approach first reparameterises a graphical model as a specific tensor network representation, which we call a base tensor network. This representation yields two key properties that allow inference tractability to be controlled by parametric structure: 1) First, the complexity of inference is mainly determined by the parametric structure of a single tensor, called the base tensor. We characterise several tractable classes of base tensors for which the entire base tensor network can be contracted efficiently. 2) Second, decomposing the base tensor yields again a collection of base tensor networks. This allows inference to be naturally reduced to decomposing the base tensor into tractable components with sufficient parametric structure. We call this procedure parametric tensor decomposition. By exploiting parametric structure within the base tensor, our framework enables a novel view on inference beyond settings where such structure is explicitly present.

---


### 258. [Statistical Convergence of Transformer Encoder-Accelerated Robust Reinforcement Learning](https://arxiv.org/abs/2609.23775)

**<font color=#1a73e8>作者：</font>** Suman Banerjee, Hiroyasu Tsukamoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Obtaining the optimal action-value function in Markov decision processes is computationally intensive in large state--action spaces. In this study, we present statistically rigorous convergence results for a robust reinforcement learning algorithm warm-started by a transformer-based action-value function prediction, where natural language prompts encode task specifications. Our framework adopts the R-contamination model to characterize uncertainty in the state transition kernel, and employs conformal prediction to certify convergence via trajectory-level nonconformity scores constructed from the contracting Bellman residual. The resulting conformal quantile bounds the gap between the running and optimal action-value functions simultaneously over all iterations, thereby yielding a pre-certified stopping rule that requires little knowledge of the true transition kernel. Numerical case studies on perturbed maze environments of varying size and contamination level confirm that the transformer-based warm start measurably reduces the initial error and accelerates convergence, while the proposed conformal bounds track the true error trajectory more tightly than existing guarantees.

---


### 259. [Falling Trees: A Model Class for Interpretable Risk Prioritization](https://arxiv.org/abs/2609.23780)

**<font color=#1a73e8>作者：</font>** Varun Babbar, Zachery Boner, Margo Seltzer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world decisions require prioritizing high-risk cases, such as clinicians prioritizing high-risk patients before lower-risk ones. Falling rule lists (FRLs), which are ordered if--then rules with monotonically decreasing risks, provide an interpretable framework for such tasks; however, their single-path structure yields a highly restricted model class. We introduce falling trees, a new family of interpretable models that enforces the same monotonic risk constraint while permitting tree-structured branching. We present GRAVITree, a novel dynamic-programming-with-bounds algorithm for learning the Rashomon set of falling trees under depth and branching constraints. Our formulation can interpolate between rule lists and full decision trees, enabling user-desired model expressivity. In a new clinical dataset and in many public classification benchmarks, falling trees match or outperform FRLs and other interpretable baselines, often producing more sparse decisions for high-risk instances. Our results show that falling trees strike a practical balance between interpretability, expressiveness, and risk prioritization for high-stakes settings.

---


### 260. [Belted Engression: Sufficient Dimension Reduction for Generative Distributional Regression](https://arxiv.org/abs/2609.23789)

**<font color=#1a73e8>作者：</font>** Wenxi Tan, Bing Li, Lingzhou Xue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern conditional generative models face significant challenges when learning complex covariate dependencies. While sufficient dimension reduction (SDR) provides a principled approach to compress these dependencies, traditional SDR frameworks were not formulated for conditional generation. To bridge this gap, we propose Belted Engression, a unified and architecturally parameter-efficient framework for generative distributional regression. Our approach establishes an end-to-end compress-then-generate paradigm driven by sufficient representation learning, embedding a structural bottleneck into the generative architecture. Theoretically, we prove that the standard SDR condition is equivalent to a law-preserving generative factorization, which is achieved at the global optimum of the population Belted Engression objective. Furthermore, by uncovering a localized Bernstein-type control for the energy-score loss, we establish finite-sample convergence rates that are sharper than those of existing results. We also prove that this belted architecture is strictly smaller, operating with an asymptotically vanishing parameter count relative to the unstructured baseline. Extensive simulations and real-world applications demonstrate that Belted Engression achieves superior distributional prediction and SDR recovery with fewer trainable parameters.

---


### 261. [Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene](https://arxiv.org/abs/2609.23796)

**<font color=#1a73e8>作者：</font>** Yang-Tian Sun, Tianjia Liu, Zehuan Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image 3D object generation can now produce high-fidelity assets, yet accurately placing them into a coherent scene layout remains an open challenge. A central difficulty lies in how object layout is represented. Holistic methods absorb placement into a scene-level generation process, sacrificing object-level detail. Compositional methods preserve object fidelity by decoupling geometry from layout, but typically parameterize layout as sparse, unbounded pose variables that are difficult to learn and generalize poorly under scarce scene-level this http URL present Mira-Scene, a compositional 3D scene reconstruction framework that replaces sparse pose regression with dense, bounded correspondence recovery. At its core is the Canonical Coordinate Map (CCM), a pixel-aligned field that maps each visible object pixel to a surface coordinate in the object's bounded canonical space. When paired with a scene-space Point Cloud Map (PCM) from monocular geometry estimation, CCM induces dense canonical-to-scene correspondences from which object transformations are recovered through robust geometric alignment. Because CCM operates in bounded canonical space, it provides a stable prediction target that can be trained from scalable object-level 3D data without requiring scene-level layout annotations. Mira-Scene further introduces a multimodal diffusion transformer that jointly generates object geometry and CCMs, using modality-specific expert streams with shared attention and positional encoding to promote geometry-layout consistency. Experiments on indoor, outdoor, synthetic, and in-the-wild scenes show that Mira-Scene substantially outperforms strong baselines in layout accuracy, achieving relative gains of 39.8% in 3D-IoU and 16.5% in 2D-IoU over SAM3D, using limited open-source training data.

---


### 262. [WorkWorlds: An Infrastructure for Evaluating AI Agents on Workplace Tasks](https://arxiv.org/abs/2609.23806)

**<font color=#1a73e8>作者：</font>** Yining Hua, Levi Lian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many knowledge-work benchmarks are constructed around individual tasks, with the context needed for each task selected together with or after the task has been specified. This design measures performance on workplace-like tasks in an environment assembled for the task. When task specification guides which context is selected, the evaluation can encode task information into the environment and pre-complete part of the information-localization work that workplace performance normally requires. We introduce WorkWorlds, an evaluation infrastructure that separates organizational state from task specification. A world first fixes a revision, date, and employee seat and materializes the organizational state that employee can access; tasks are introduced only afterward. We implement WorkWorlds in a primary synthetic pharmaceutical company with 8 measured tasks across 6 employee seats, and construct additional organizational worlds. Across 192 matched evaluations, moving from task-curated context to the full role-visible workplace reduced evidence access from 90.4% to 74.5% and criterion pass from 79.4% to 68.2%, while pass conditional on evidence access remained nearly unchanged; most of the measured difference occurred before the agent reached sufficient evidence.

---


### 263. [Iterative Atom Refinement: A Monotonicity Principle for Dictionary Learning](https://arxiv.org/abs/2609.23812)

**<font color=#1a73e8>作者：</font>** Alexander Christie, Miguel Moscoso, Alexei Novikov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dictionary learning seeks to recover an unknown dictionary $A$ from observations ${\bf y}_i = A{\bf x}_i$ with sparse coefficient vectors ${\bf x}_i$. We introduce the \emph{Iterative Atom Refinement} (IAR) algorithm, a simple procedure for recovering individual dictionary atoms. Starting from a random direction, IAR repeatedly selects the observations most strongly correlated with the current iterate and updates the direction by averaging the selected data. Our main contribution is a rigorous convergence theory of IAR. Using high-dimensional probabilistic estimates and a novel monotonicity principle for atom-selection probabilities, we show that a small initial advantage of one atom is amplified until that atom is isolated. Under our model assumptions, IAR identifies a generating atom after only three refinement steps. Numerical experiments support the theory and show that the resulting dynamics accurately capture the behavior observed in dictionary refinement.

---


### 264. [Confidence-Aware Teacher-Student Distillation for 3D Medical Segmentation](https://arxiv.org/abs/2609.23815)

**<font color=#1a73e8>作者：</font>** Georgios Triantafyllou, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation models typically rely on large amounts of densely annotated volumetric data, limiting their scalability across tasks and imaging modalities. This work addresses the challenge of predicting entire 3D anatomical structures from extreme annotation sparsity. An annotation-efficient student-teacher framework is proposed for automatic 3D medical segmentation that requires only a set of point prompts on a single 2D slice per volume, as input. A foundation model serves as an offline teacher, utilizing the provided point prompts from the selected slice to full-volume pseudo-annotations alongside their corresponding spatial confidence scores prior to student training. To mitigate the error propagation of noisy pseudo-annotations, a task-specific 3D student network is trained using a confidence-aware optimization strategy. By leveraging the teacher's pre-computed confidence scores, this strategy explicitly excludes statically uncertain regions of the pseudo-annotations from the loss calculation, while simultaneously emphasizing regions with higher confidence. Evaluated on 3D cardiac MRI datasets, our framework outperforms state-of-the-art semi-supervised methods, improving segmentation performance by up to 43.6%. Furthermore, it drastically reduces the manual annotation burden to just a few positive point prompts per volume, while improving surface boundary precision by up to 14.7% over the teacher and successfully recovering up to 34.1% of the performance gap toward the fully supervised upper bound.

---


### 265. [VISTA: Video-Injected Stylized Text-to-Animation](https://arxiv.org/abs/2609.23817)

**<font color=#1a73e8>作者：</font>** Monseej Purkayastha, Anindita Ghosh, Philipp Slusallek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present VISTA, a two-stage framework for generating stylized 3D human motion by fusing structural content from text prompts with expressive style from reference videos, without requiring jointly paired (text, video, stylized motion) triplets. A Dual-channel Autoencoder first maps motion sequences and video clips into a shared latent manifold. A masked autoregressive diffusion backbone then operates within this manifold, injecting video-derived style through a dedicated late-fusion Dual-AdaLN pathway while preserving text-conditioned content structure. A cross-batch unpaired training protocol with latent cycle consistency enables joint learning across separate semantically rich and stylistically diverse datasets. As a proof-of-concept for controllable animation synthesis, we validate VISTA on rendered motion-capture references: it achieves the highest style recognition accuracy among video-conditioned methods while preserving competitive content alignment, and its decomposed 3-way classifier-free guidance provides independent, user-controllable calibration of the content--style balance at inference time.

---


### 266. [Real-time Generalizable Heart Valve Mechanics for Clinical Disease Assessment via a Physics-Conditioned Neural Operator](https://arxiv.org/abs/2609.23826)

**<font color=#1a73e8>作者：</font>** Shawn Koohy, Wensi Wu, Matthew A Jolley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mitral regurgitation is the most common heart valve disorder worldwide, affecting over 2% of the global population, rising to at least 10% in adults over 75, and causing approximately 15% of valvular heart disease-related deaths. Yet only a minority of patients with severe disease undergo corrective surgery. Rapid assessment of valve mechanics could enable earlier, more precise intervention, but traditional finite element simulations remain too slow for clinical timelines and parameter sweeps. We introduce the Physics-Conditioned Neural Operator (PCNO), a transformer-based surrogate that predicts leaflet displacement, strain, and stress fields across mitral and tricuspid geometries, conditioned on systolic blood pressure and tissue properties. Trained on functional, regurgitated, and pathological valves, including tethering, P2 prolapse, and annular dilation, PCNO achieves up to a 15,260x speedup over fine mesh finite element simulations with comparable accuracy, identifies pathology class, and resolves diagnostic metrics within 3.5% error under out-of-distribution extrapolation.

---


### 267. [Pattern-level Differential Privacy for High-utility Complex Event Processing](https://arxiv.org/abs/2609.23827)

**<font color=#1a73e8>作者：</font>** He Gu, Thomas Plagemann, Vera Goebel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current privacy-preserving mechanisms (PPMs) in Complex Event Processing (CEP) systems are unnecessarily restrictive, reducing the utility of data received by data consumers. This article presents a novel approach to preserve privacy in CEP systems, improving the utility of detected event patterns by dynamically adapting the noise added to an unprotected data stream. We introduce a new guarantee named pattern-level differential privacy (DP), which enables us to apply and compare the strength of PPMs at the pattern level. We propose new pattern-level PPMs yielding pattern-level DP and analyze different trust settings of these PPMs and their requirements for context knowledge in the CEP system, e.g., the deployed queries. Our evaluation is based on three datasets (two real-world, one synthetic) and shows that the proposed PPMs increase data utility while preserving the same privacy level as the state-of-the-art PPMs. We use simulations to study the performance of our proposed PPMs in various practical scenarios. Furthermore, we demonstrate that computational complexity is not an obstacle to deployment.

---


### 268. [DFD-Lab: A Modular Audio-Visual Deepfake Detection Pipeline](https://arxiv.org/abs/2609.23830)

**<font color=#1a73e8>作者：</font>** Jan Rybarczyk, Mateusz Roszkowski, Jacek Komorowski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comparing audio-visual deepfake detectors requires coordinating dataset adaptation, temporal input representation, model interfaces and experimental conditions. We present DFD-Lab, a modular pipeline that separates these responsibilities while supporting shared training and evaluation workflows. We integrate three implementations: Xception-based maximum-logit fusion, ResNet with temporal LSTM fusion, and our AVFF reimplementation. Experiments cover external testing, degradation-based training augmentation and evaluation-time corruption. On a filtered subset of Deepfake-Eval-2024, models trained on FakeAVCeleb attain baseline AUROC values of 0.504, 0.538 and 0.458. JPEG50 training augmentation raises these to 0.691, 0.605 and 0.570, respectively, while all three accuracies decrease. These results illustrate why training interventions, evaluation corruptions and metric-dependent outcomes should remain distinct within a common pipeline. The contribution is the integration of audio-visual processing, interchangeable detectors and configurable experimental workflows, supported by empirical case studies. The findings highlight the challenge of cross-dataset detection and the complementary information provided by ranking and classification metrics.

---


### 269. [Comparative Performance and Parameter-Efficient Adaptation of DINOv2 for Active Trachoma Classification](https://arxiv.org/abs/2609.23832)

**<font color=#1a73e8>作者：</font>** Kibrom Gebremedhin, Hadush Hailu, Bruk Gebregziabher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated grading of conjunctival photographs could reduce the cost and variability of trachoma prevalence surveys, but the relative value of modern pretrained visual representations, lightweight feature adaptation, and training-objective design has not been established under a common protocol. This study presents a controlled evaluation for binary classification of Trachomatous Inflammation-Follicular (TF) versus Normal using 1,546 images from the public UCSF/Lietman collection. Images are processed using the OPTED pipeline for zero-shot tarsal-conjunctiva segmentation, alignment, cropping, and standardization. We first compare six pretrained backbones using a common classification pipeline and then evaluate four lightweight adaptation mechanisms on DINOv2 ViT-B/14. Under stratified five-fold cross-validation, DINOv2 with Efficient Channel Attention (ECA) and focal-plus-center loss achieved 91.66 +/- 0.97% accuracy, 90.69 +/- 1.10% macro-F1, and 96.06 +/- 0.71% AUC. ECA introduces only five learnable parameters while matching the performance of substantially larger alternatives. Objective ablation further showed that ECA did not consistently improve plain DINOv2 across loss functions; the lowest-variance 91.66% accuracy was obtained with cross-entropy plus center loss. Overall, the fine-tuned DINOv2 representation provided most of the predictive performance, while ECA offered a highly parameter-efficient refinement whose effect depended on the training objective. The resulting workflow provides a reproducible benchmark for active trachoma image classification.

---


### 270. [Actionable Insights from Observational Data: The Case of Advanced Classes in K-12 Education](https://arxiv.org/abs/2609.23836)

**<font color=#1a73e8>作者：</font>** Nabit Bajwa, Seth B. Hunter, Sanmay Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamentally challenging question in K-12 education is about the effects of taking more advanced or challenging classes. It is particularly complex because students (and/or their parents) choose whether to enroll in these classes, making causal analysis challenging. In this paper, we begin to tackle this question by taking advantage of a novel dataset from a public school system in the US. This dataset records students' course enrollment decisions, prior academic histories, demographics, and subsequent outcomes around the time of a district-wide change that introduced optional open-enrollment advanced middle-school courses in subject areas. This is a rich observational dataset, but enrollment in advanced classes is driven by student characteristics and choices rather than random assignment. This creates a core identification challenge: the same factors that influence enrollment in advanced courses are also predictive of academic outcomes. As a result, simple comparisons between enrolled and non-enrolled students are confounded, and naive estimates may reflect underlying differences in student ability, motivation, or support rather than the impact of coursework itself. Our analysis shows that enrolling in advanced English courses has a net positive but modest effect on student achievement outcomes. However, these benefits are unevenly distributed: some students with relatively large predicted gains ("middle achievers" in prior years) are less likely to enroll than others. Some other groups (e.g. Black students and those with lower socio-economic status) also demonstrate significantly lower propensity to enroll. This gap between predicted benefit and observed enrollment illustrates how careful data analysis can extract actionable insights from large observational datasets, including identifying students who appear well-positioned to benefit but do not select into advanced options.

---


### 271. [From Regional to Global: Transfer Learning for Atmospheric Transport Emulators](https://arxiv.org/abs/2609.23838)

**<font color=#1a73e8>作者：</font>** Jeff Clark, Elena Fillola, Nawid Keshtmand 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Greenhouse gas emissions estimates can be derived using inverse methods by combining atmospheric concentration observations with chemical transport models. The latter traditionally use physics-driven simulators such as Lagrangian Particle Dispersion Models (LPDMs), which are expensive to run and do not scale well to modern satellites' high resolution data. Previously we developed a performant atmospheric transport emulator that approximates LPDM outputs ("footprints") over South America ~1,000X faster than the UK Met Office's LPDM. Expanding towards global emulation is not straightforward, as atmospheric transport is regionally heterogeneous. This paper evaluates spatial transferability capabilities of models across four world regions: South America, East Asia, South Asia, North Africa using both region-specific and multi-region models, and leave-one-region-out experiments. Regional differences are characterised in the context of input variable and output footprint distributions. This work builds intuition in cross-region generalisation and transfer learning, aiding regional performance towards efficient global emissions estimates.

---


### 272. [Adaptive Determinantal Client Scheduling in Federated Learning](https://arxiv.org/abs/2609.23843)

**<font color=#1a73e8>作者：</font>** Wen Xu, Ben Liang, Gary Boudreau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scheduling clients for model training is critical in federated learning due to both data and system heterogeneity. Most previous works focus on the quality of the scheduled clients to achieve faster convergence, shorter wall-clock convergence time, or better average model performance. They rarely consider the diversity of clients, which is important to counter heterogeneity and improve performance for the worst-off clients. In this work, we advocate the use of determinantal point processes (DPPs) to model and enhance the diversity in client scheduling. We first design the kernel matrices of DPPs using gradient information and quality scores, which inherently enables a flexible quality-diversity trade-off. Applying fast MAP inference over DPPs, we propose Adaptive Determinantal Client Scheduling (ADCS) in FL. We further quantify the gradient approximation error of ADCS and develop convergence analysis for general biased client selection in FL with non-convex loss functions. We conduct comparative numerical experiments showing that ADCS outperforms state-of-the-art client scheduling algorithms, including both quality-based and diversity-based ones.

---


### 273. [PROSE: A Theory of Optimal Stopping with Perishable Evidence for Peer Selection in Intermittently Connected Decentralised Learning](https://arxiv.org/abs/2609.23845)

**<font color=#1a73e8>作者：</font>** Christos Anagnostopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralised federated learning removes the aggregation server but makes collaboration dependent on transient peer availability. In mobile and intermittently connected systems, evaluating a promising peer consumes contact time and may cause the exchange opportunity itself to vanish, so that the evidence a learner gathers about a peer is perishable: it decays because links expire and because peer models drift while old measurements age. This paper develops a self-contained theory of optimal stopping for the resulting peer-selection problem. We formalise a receiver's within-contact decision as a finite-horizon Markov optimal-stopping problem with costly information acquisition and a future-arrival outside option, and prove that it admits an optimal policy characterised by a reservation value (Snell-envelope structure). Around this formulation we prove: (i) stage-uniform, drift-aware concentration and a maximin certification rule that is correct with high probability together with a finite-sample identification bound; (ii) a mobility-aware value of-information stopping rule and comparative statics showing that higher link hazard lowers the value of continued probing and enlarges the stopping region; (iii) a closed-form value of waiting under marked-Poisson contact arrivals, together with a search-theoretic reservation value whose comparative statics we characterise; and (iv) a myopic-optimality theorem establishing that, in sufficiently volatile (monotone) mobility regimes, the one-step confidence-safe rule is a sound surrogate for the optimal policy and never stops prematurely. We instantiate the theory as PROSE (Perishable-evidence Reservation-value Optimal Stopping for Exchange), a lightweight, fully local policy, and delineate the static contact and drift-free limits in which classical sequential decision problems are recovered. The development is entirely analytical.

---


### 274. ["I can do whatever I put my mind to!" How prioritizing belonging in the design of technology-based programs can support foster-involved youth with self-efficacy, self-expression, and personal exploration](https://arxiv.org/abs/2609.23861)

**<font color=#1a73e8>作者：</font>** Ila Krishna Kumar, Karishma Chadha  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this paper, we examine how intentionally designing for belonging impacts outcomes in a technology program serving a population of youth who have not had safe and supported experiences with technology - youth impacted by foster care. We reflect on the design of an internship program which engaged two foster-involved youth in creative self-expression and co-design with technology. We first outline how we designed the program to foster belonging, then analyze intern and facilitator reflections to understand how the program impacted the interns' experience. We highlight how the internship design affected youth's inclusion and overall engagement; self-expression; exploration; and self-efficacy. We conclude with a discussion of design recommendations for technologists and service providers aiming to engage youth in expressive and co-design technology experiences, particularly youth impacted by foster care.

---


### 275. [VISTA: An Attention-Based Multi-Agent Reinforcement Learning Architecture for Space Situational Awareness Sensor Tasking](https://arxiv.org/abs/2609.23875)

**<font color=#1a73e8>作者：</font>** Miguel Leiva-Vélez, Adalberto Claudio Quiros, Nicolas Gaston Rozado 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth of resident space objects is increasing the complexity of space situational awareness sensor tasking, challenging classical optimization methods as they allocate finite, heterogeneous, and distributed sensing resources across ever-larger catalogues. Existing deep reinforcement learning approaches show promise in reduced settings, but fixed-dimensional state and action representations limit their ability to scale to large, dynamic catalogues and distributed sensing networks. We introduce VISTA (Variable-Entity Intelligent Sensor Tasking Architecture), a scalable deep reinforcement learning architecture for persistent uncertainty-driven catalogue maintenance across variable object populations and sensor configurations. VISTA combines physics- and mission-informed top-K retrieval with entity-centric attention, recurrent memory, and pointer-based action decoding, thereby keeping each agent's observation and action spaces independent of catalogue size. We evaluate VISTA across different scenarios, from fixed-size single-sensor benchmarks to large-scale space-based tasking and heterogeneous cooperative sensing. With 30 orbiting targets, VISTA recovers the catalogue 31.2% faster than the fixed-dimensional recurrent baseline. In the large-scale regime, VISTA reduces five-hour uncertainty by 97.5% relative to the strongest classical reference and by 99.3% relative to the recurrent learner. Zero-shot tests up to 20,000 objects reveal near-linear relations between sensing capacity, catalogue size, and recovery horizon. Learned policies also exhibit sensor modality adaptation and generalization to population and initial-uncertainty shifts. Together, these results demonstrate that VISTA provides a scalable framework for adaptive space situational awareness sensor tasking across large, distributed networks of heterogeneous ground- and space-based sensors.

---


### 276. [GLR-MM: Graph-Based Global-Local Reconstruction for Robust Multimodal Chest X-ray and EHR Representation Learning under Missing Modalities](https://arxiv.org/abs/2609.23876)

**<font color=#1a73e8>作者：</font>** Surbhi Sharma, Nikhil Manali, Devesh Maheshwari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical multimodal models must often predict before all chest X-ray (CXR) and electronic health record (EHR) inputs are available. Existing approaches align observed representations, model missingness, or reconstruct across modalities, but do not jointly exploit within-patient and clinically similar inter-patient evidence. We propose GLR-MM, a Graph-Based Global-Local Reconstruction framework for early ICU mortality prediction. It maps five CXR-EHR modalities to a shared space, reconstructs missing embeddings through complementary local cross-modal and global graph-attention branches, adaptively fuses their estimates, and optimizes class-balanced prediction, reconstruction, and contrastive objectives. On 9,620 MIMIC-derived ICU stays, we evaluate 10%, 30%, and 50% random modality missingness with shared deterministic masks. MUSE performs better under mild and moderate missingness, whereas GLR-MM achieves higher AUROC and AUPRC at 50% by 0.0088 and 0.0249, respectively. These results indicate that graph-guided reconstruction is most useful when inputs are severely incomplete.

---


### 277. [MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space](https://arxiv.org/abs/2609.23881)

**<font color=#1a73e8>作者：</font>** Markus Karmann, Shile Li, Christian Internò 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint Embedding Predictive Architectures (JEPAs) are a promising paradigm for learning task-agnostic latent world models without visual reconstruction. However, standard JEPA training exhibits a strong inductive bias towards slow features, causing feature suppression and the collapse of latent representation. While inverse dynamics provides temporal anti-collapse, it relies on action labels and offers little incentive to embed general, unlabeled dynamics. We introduce Difference Image and Single image embedding Regularization (DISReg), a novel regularizer that builds on an inverse-dynamics-style module that predicts temporal difference image embeddings without any pixel reconstruction loss, encouraging balanced static and dynamic feature learning. DISReg consists of a static term that shapes the distribution of the image embedding and encourages slow features, and a dynamic term, which, unlike direct regularization on the embedding, imposes no constraint on the image embedding's shape or distribution and instead only incentivizes that dynamic features be present. By integrating this regularizer into a standard JEPA, we establish our new architecture, MotionJEPA. Latent probing demonstrates that MotionJEPA produces more complete representations than other methods, and our trajectory analysis shows it maintains geometrically simple latent embeddings with low curvature. We further show that MotionJEPA improves downstream planning success under static-background distractors across four environments.

---


### 278. [Collaborative Streaming Anomaly Detection with Interactive Explanations and Ensemble Consensus](https://arxiv.org/abs/2609.23883)

**<font color=#1a73e8>作者：</font>** Diogo Risca, Afonso Lourenço, Ricardo Martins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a collaborative streaming anomaly detection system for high-speed data streams that explicitly integrates human analysts into the decision loop. The system combines heterogeneous detectors and aggregates their outputs through a normalization-based weighted consensus, complemented by artifact-aware rules to stabilize anomaly scoring under deployment. To improve interpretability, it derives surrogate models that approximate the ensemble consensus and expose human-readable sensor conditions associated with anomalous behavior. Analysts can actively intervene by reviewing anomaly episodes, adjusting consensus behavior, and refining surrogate rules used for anomaly prediction, producing a human-adjusted ensemble. We evaluate the approach on an industrial stream with 260\,000 events and 3 anomalous episodes, showing robust detection and actionable human-AI interaction.

---


### 279. [this-that-model-1.0: A typed decision model that decides in 30 ms, for a millionth of a cent](https://arxiv.org/abs/2609.23886)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Software delegates more of its branches to models every year: which queue a ticket enters, whether a command is safe to run, whether a claim clears without a person. What the program needs back is not prose. It is one of n declared options and a number it can threshold. Today that costs a round trip to a frontier model -- hundreds of milliseconds, a per-token bill, and a parser -- for a question that is usually a conjunction of three clauses. this-that-model-1.0 is a 2B-parameter typed decision model. Its answer is read directly from the hidden state at a designated position and restricted to the option set the caller declared, so no text is generated, nothing can be malformed, and every question in a request is answered in the same forward pass. It decides in 30.9 ms on one laptop GPU and generates zero output tokens doing it, where a frontier API call costs 8758 ms and the hosted systems that answer these questions well spend between 21 and 212 generated tokens per question thinking first, billed for every one. It sustains 32 decisions per second on one consumer GPU and never lets the state leave the machine. On a third party's recorded cohort of 68 decision questions, on their inputs and their wording, it scores 0.941 with a Brier score of 0.042, against 0.765 and 0.133 for the hosted service Jev on the same items. One pass of our 42-family internal suite takes 32 seconds and 0.000217 USD of electricity; the most accurate hosted model we measured needs 155.2 minutes and 10.636 USD. We also report where it loses. On multi-step arithmetic, which a single forward pass cannot carry intermediate results through, it scores 0.560 against their 0.98 to 1.00, and a targeted second training round improved the five task families it was written for and transferred to none of the other 13. The model is open-sourced in this https URL

---


### 280. [Circuit-Diff: Factual Edit-based Intervention Method for Localizing Knowledge in Attribution Graphs](https://arxiv.org/abs/2609.23892)

**<font color=#1a73e8>作者：</font>** Edward G. Friedman, Xiangchen Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability defines features as the fundamental units of a neural network and circuits as the weighted subgraphs that carry out its computation. Because individual neurons are polysemantic, Cross-Layer Transcoders (CLTs) were introduced as a way to approximate a model's circuits by generating an attribution graph. The nodes of that graph, however, are unlabeled features: reading a graph means pruning it and then working out by hand what each surviving node means. To make CLTs easier to use for circuit discovery, we introduce Circuit-Diff, which intervenes on the model itself with a low-rank factual edit and takes the features whose role in the attribution graph changes under that edit as related to the edited knowledge. On the edits we examine, the flagged nodes are not only detectors of the object token: read off the CLT's released feature dashboards, they include features for the history, geography and associations surrounding the old and new objects. We formalize the method, measure how reliable a frozen CLT remains after a factual edit, test the selected nodes causally by patching them on up to 24 CounterFact edits, give a case study, and release an open-source implementation built on the circuit-tracer package, together with two further tools (multi-prompt aggregation and rule-based supernode labeling).

---


### 281. [Benchmarking Post-Quantum Cryptography in Lightweight Virtualization Environments on Embedded Hardware](https://arxiv.org/abs/2609.23902)

**<font color=#1a73e8>作者：</font>** Nikolai Puch, Chi Hieu Ta, Moritz Beckel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-Quantum Cryptography (PQC) is being deployed while embedded systems increasingly adopt lightweight virtualization for workload isolation and security. Both trends change performance characteristics, yet their interaction is not well understood. To address this, we present a measurement study of PQC primitives on embedded-class ARM hardware under three execution environments with a shared software stack: native execution, a Docker container, and a Unikraft unikernel running under QEMU. We benchmark five signature and five key encapsulation mechanism families, and, for comparison, two classical algorithms each. We evaluate them using different parameter sets for a total of around 70 configurations, measuring execution time, memory, and energy per operation. To better gauge the impact on applications, we evaluated TLS 1.3 cipher combinations. We find that container overhead is negligible for primitive computation, whereas unikernel overhead depends on the algorithm. For most PQC families the overhead is negligible. A moderate overhead (1.28-1.53) arises in BIKE, HQC, and MAYO, and, above all, in Falcon signing (17.8-19.2). Per-operation energy closely tracks execution time in all environments. For TLS handshakes, container and unikernel clients need more time and energy per handshake, while all three environments converge once expensive post-quantum algorithms dominate the handshake. In these cases algorithm choice affects per-handshake energy by up to three orders of magnitude, far outweighing the environment. Overall, virtualization cost is inversely related to cryptographic cost: environment choice matters most for computationally cheap, standardized algorithms, while for expensive schemes, algorithm choice alone dominates performance.

---


### 282. [Multivariate quantile regression via Kolmogorov-Arnold Networks](https://arxiv.org/abs/2609.23906)

**<font color=#1a73e8>作者：</font>** Andrew Polar, Michael Poluektov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces a novel algorithm for predicting conditional joint distributions of vector-valued targets in stochastic systems whose randomness is intrinsic rather than arising from observation errors or additive noise. Multivariate quantile regression also involves modeling conditional joint distributions but represents a less challenging task. It predicts the probability that vector-valued targets fall within predefined regions, identifies regions corresponding to predefined probability levels, or performs both tasks simultaneously. The proposed identification technique employs ensembles of Kolmogorov--Arnold networks (KANs) as flexible function approximators. Although the suggested technique is not theoretically restricted to KANs, KANs are particularly well suited to the proposed construction and are therefore used throughout this study. In addition to the training procedure, this work introduces a new discrepancy measure for joint distributions and a goodness-of-fit (GoF) test based on it. This GoF test was initially developed to validate and calibrate the proposed identification technique and is used here in an ad hoc manner. Although the test could be tabulated for broader use, such a tabulation is not pursued in this work. The test is also applicable more generally.

---


### 283. [A discrete generative model of neuronal spiking activity on microelectrode arrays](https://arxiv.org/abs/2609.23907)

**<font color=#1a73e8>作者：</font>** Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a discrete generative model that represents this activity using a shared vocabulary of spatiotemporal motifs. A residual vector-quantized autoencoder learns the motif vocabulary, while a factorized masked transformer predicts where activity occurs and which motif appears at each active location. We evaluate the model on 31 assays spanning human brain organoids and acute \emph{ex vivo} human hippocampal tissue. The learned motifs are broadly reused: assay identity explains only $9%$ of the entropy in motif use, and motif overlap across tissue types is comparable to overlap within them. When representation quality is evaluated independently of the generative prior, our approach achieves $5.2\times$ the voxel-level reconstruction average precision of a matched flat tokenizer. For masked completion and free generation, the full model achieves $1.4$--$2.6\times$ the site-level average precision of the matched generative baseline and outperforms it across all four families of generation metrics. These results establish a compact, reusable representation for array-wide spiking activity without learned assay-specific parameters, providing a scalable foundation for generative modeling across diverse neural preparations.

---


### 284. [Increasing Skill Level Recruits Deeper Attention Layers in a Frozen Chess Transformer](https://arxiv.org/abs/2609.23917)

**<font color=#1a73e8>作者：</font>** David Litman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chess involves complex reasoning in a deterministic environment, which makes it a useful setting for studying the mechanisms of computation inside transformers. The Maia-3 chess transformer takes Elo, a measure of competitive chess skill, as an input to the pre-trained network, so we can vary the skill the network is conditioned on with no change to its weights. Here we investigate how turning this skill dial affects self-attention. Ablating every attention head at every Elo from 700 to 2500, we find 1) increasing skill pushes the causal center of mass of the computation deeper, monotonically, for every chess piece and move type we measured; 2) the depth migration is much greater for specific tactics, especially knight forks, than for other move types; 3) the migration consists of deeper heads getting recruited for more specialized computations while one shared shallow head keeps a roughly constant contribution. These results may shed light on how conditioning inputs redistribute computation in larger transformers.

---


### 285. [The Neural Forcing for Three-Dimensional Incompressible Navier-Stokes finite time blowup](https://arxiv.org/abs/2609.23934)

**<font color=#1a73e8>作者：</font>** Beibei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a two-part neural framework for forced three-dimensional incompressible Navier--Stokes flow. Part~I develops the computational forcing system. A physics-informed neural model generates structured external-force trajectories, candidates are optimized through differentiable PDE rollouts or PPO-Clip, and selected forcings are frozen and checked by independent fixed-force replay. Part~II provides the mathematical certification layer. It separates neural candidate discovery from continuum analysis, derives integrated reciprocal-vorticity criteria that imply Riccati-type growth and finite-time loss of smooth continuation, develops a validated computational-to-continuum transfer strategy, and establishes a conditional positive-probability closure for a nondegenerate neural output law. The proof is complete at the continuum level.

---


### 286. [Measuring the Assistant's Harmlessness Preferences on the User Turn](https://arxiv.org/abs/2609.23935)

**<font color=#1a73e8>作者：</font>** Jord Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training turns a general next-token predictor into a chat model with a persistent assistant persona. If that persona is a character the model plays only on its own turns, its preferences should govern what the assistant says, not what the model predicts other speakers will say. We test this boundary and find that it does not hold: a safety-relevant preference of the assistant---for harmless over harmful tasks---shapes the model's predictions even on the user's turn, where the assistant is not the one speaking. We find that this preference is small or near-zero in pretrained base models, that it emerges through post-training, replicated across open-weight model families, grows with scale, and can be moved by narrow finetuning that never touches user turns. We claim that this is evidence that post-training does not merely install a shallow assistant persona, but instead generalises beyond just the local assistant turn, into the model's representation of the user.

---


### 287. [XYEval: Agents say yes to bad advice](https://arxiv.org/abs/2609.23939)

**<font color=#1a73e8>作者：</font>** Zhengxuan Wu, Yuxuan Li, Oyvind Tafjord 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective communication between users and AI agents is essential for human-AI collaboration. The XY problem is a well-known communication pitfall where a person asks about their attempted solution rather than their actual problem. We extend prior sycophancy evaluation to the XY problem in agentic settings, evaluating whether agents can resist plausible but misleading suggestions from users and communicate their reasoning. We introduce XYEval, a meta-evaluation framework that can transform an existing benchmark into an XY problem evaluation. We evaluate five models across six diverse benchmark suites. Agents suffer large XY drops under XY mutation across benchmarks, with relative drops reaching up to 46.7%. With $\tau^2$-bench, we further show that agent performance drops more when encountering a pedantic user who requires detailed explanations before approving a better solution. Our findings suggest that current agents lack the ability to effectively reason and communicate when facing misleading suggestions. A simple system instruction baseline that encourages awareness of XY problems only offers partial mitigation. Extensive trace analyses provide behavioral insights into how and why these XY drops occur across execution trajectories. Our results show that mitigating the XY problem remains challenging, requiring agents to both recognize user misdirection and clearly communicate the underlying problem.

---


### 288. [Echo State Network (ESN) for Signal Recovery in RF-Impaired IBFD MIMO Systems](https://arxiv.org/abs/2609.23945)

**<font color=#1a73e8>作者：</font>** Conrad Prisby, Siyao Li, Chengtao Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-band full-duplex (IBFD) multiple-input multiple-output (MIMO) systems enable simultaneous transmission and reception on the same frequency band, improving spectral efficiency for next-generation wireless networks. However, IBFD-MIMO systems are susceptible to self-interference (SI), which may overpower signals of interest (SOI). In this scenario, blind source separation (BSS) algorithms can be adopted to remove SI and perform joint sensing and communication (JSAC), but BSS algorithms mostly assume an idealized linear and quasi-stationary signal model, which does not hold under realistic radio frequency (RF) impairments, such as I/Q imbalance, carrier frequency offset (CFO), phase noise, and power amplifier nonlinearity. This paper proposes a two-stage echo state network (ESN)-based scheme that is superior to BSS under these realistic conditions. A frozen ESN is trained offline to characterize the static SI path, while an adaptive ESN, updated online via recursive least squares, tracks the time-varying SOI path using sparse pilot symbols. We evaluate the proposed scheme's SOI recovery performance and acquisition speed with different block sizes, comparing it against other recurrent neural networks (RNN), such as long short-term memory (LSTM) and gated recurrent unit (GRU). Simulation results show that the proposed approach outperforms BSS, LSTM, and GRU in both efficiency and SOI recovery, demonstrating the viability of ESNs for real-time, nonlinear self-interference cancellation in realistic IBFD MIMO systems.

---


### 289. [Divergent strategies and convergent outcomes in autonomous materials discovery](https://arxiv.org/abs/2609.23957)

**<font color=#1a73e8>作者：</font>** Jihan Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents are mostly evaluated on whether they complete tasks or recover known results; we instead study variation across repeated open-ended campaigns. Sixteen separately initialized sessions of one model-harness configuration received a frozen database of 12,499 metal-organic frameworks, a methane-storage objective, a pinned protocol and a one-week budget. Strategies diverged into four approaches spanning 100--5,000 screened structures, and eight built 2,253 hypothetical structures. Yet the agents recovered the same materials frontier near 200 cm^3/cm^3, and an independent calculation of the database's porous region found its nine best structures all among their reports. Enforced checks on half the agents raised fresh-run reproduction from one of eight to eight of eight but could not detectably improve conclusion validity, because fifteen of sixteen agents selected the same audit-excluded entry, an incomplete structure whose missing anions created artificial pore volume. Replicated agents thus reveal both robust conclusions and common-mode errors from shared inputs.

---


### 290. [When AI Tutors Speak: Evidence from a Randomized Field Experiment](https://arxiv.org/abs/2609.23958)

**<font color=#1a73e8>作者：</font>** Shihao Yang, Marshall Van Alstyne, Chrysanthos Dellarocas  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Students increasingly study alongside generative artificial intelligence (AI), yet unguided access to fluent answers invites cognitive offloading, and there is little evidence on which configurations of AI tutoring produce learning. Two design margins are usually bundled together: pedagogical structure (how the tutor teaches) and interaction modality (how students talk to it). We separate them. In a preregistered randomized field experiment in a graduate corporate-finance course of an online MBA, we randomized 86 students between a structured tutor grounded in the course materials and a holdout in which consumer AI remained freely available. Within the tutored arm, each student's channel alternated weekly between voice and text, so the modality effect is identified within student. Structure mattered: tutored students gained 6.63 points more than ability-matched peers (p=.007), and the gain was concentrated in written reasoning, where the share of answers reaching relational quality rose from 8% to 49% in the tutored arm against 8% to 27% in the holdout. Modality did not matter for learning. The instructor's own final, on file for all 86 randomized students, shows the same direction (2.6 points of 100, with no difference on a pre-treatment midterm). Voice nearly doubled conversational interaction and cost 2.8 times as much to deliver, yet it produced weekly mastery statistically equivalent to text, even as students came to prefer it. Pedagogical structure shapes what students practice, and modality shapes how they interact with the tutor. Making an AI more humanlike does not by itself make it more educational.

---


### 291. [Colon3R: Cross-Domain 3D Reconstruction from Monocular Colonoscopic Video](https://arxiv.org/abs/2609.23961)

**<font color=#1a73e8>作者：</font>** Zhihao Xing, Yingyu Wang, Liang Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular colonoscopic 3D reconstruction is important for surgical robotic colonoscopy, but remains challenging due to weak texture, specular reflections, limited view overlap, and non-rigid tissue motion. Conventional multi-view 3D reconstruction methods rely on stable correspondences and approximate rigidity, which are often violated in colonoscopy. Existing endoscopic methods often rely on domain-specific supervision, whereas there are not enough in-vivo labeled data available to adapt geometry foundation models to clinical colonoscopy. We present Colon3R, a cross-domain semi-supervised framework built on pretrained VGGT that transfers coupled camera, depth, and pointmap geometry from labeled phantom and simulated data to unlabeled in-vivo colonoscopy without requiring target-domain geometric annotations. Unlike source-only fine-tuning, which learns only from phantom and simulated data, Colon3R directly exploits unlabeled in-vivo video through teacher-derived cross-view supervision. Our proposed hierarchical quasi-rigid reliability selects reliable supervision at the sequence, directed-pair, and pixel levels, while source-preserving adaptation retains the learned coupled geometry during target-domain adaptation. Extensive experiments demonstrate that our method achieves superior overall performance over state-of-the-art approaches in depth, pointmap, and camera pose estimation. Qualitative comparisons on real in-vivo colonoscopy further show substantially more complete and geometrically consistent reconstructions than competing methods under clinical domain shift. The code will be public available after the paper is accepted.

---


### 292. [Rethinking Diffusion Segmentation: When Does It Rely on Its Noisy State, and Does Diffusion Matter?](https://arxiv.org/abs/2609.23967)

**<font color=#1a73e8>作者：</font>** Hengzhuo Yang, Yuming Zeng, Yuling Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are increasingly adapted from generation to conditional prediction, where a conditioning signal is combined with an evolving noisy representation of the target. In fully supervised segmentation, however, the conditioning image can already support direct target prediction, so endpoint performance alone establishes neither reliance on the added diffusion state nor a deterministic advantage over image-only prediction. For state reliance, we disrupt target-derived state content or correct image-state pairing during retraining of twelve published methods across three datasets, with ten matched seeds per setting. All 40 original-method comparisons whose evaluated-mask routes remained downstream of noised-quantity reconstruction exhibited state reliance, whereas all 30 comparisons with a segmentation-supervised bypass preserved reference performance. Rerouting five originally bypass-capable methods by forcing segmentation supervision through noise-to-mask reconstruction converted all 30 corresponding comparisons from preserved performance to state reliance. For deterministic utility, matched image-only counterparts achieved similar or better performance in 28 of 35 settings overall, including 16 of 20 whose native methods relied on both audited state properties. These results identify supervision path as a determinant of state reliance in the audited methods. Separately, matched image-only counterparts show that diffusion-specific computation often provides no deterministic endpoint advantage, including in methods that rely on the audited state properties. More generally, when conditioning already supports strong target prediction, diffusion-specific claims require additional evidence that the added state is used and that diffusion-specific computation improves the claimed capability beyond a matched condition-only counterpart.

---


### 293. [MGRD: Compact morphology-gated residual diffusion for variance-aware cross-domain neurite forecasting](https://arxiv.org/abs/2609.23990)

**<font color=#1a73e8>作者：</font>** Tsung Yeh Hsieh, Cosmin Anitescu, Chunghwan Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tracking neurite morphology over time helps characterize structural changes during neuronal development and deterioration, but long-term time-lapse imaging is resource-intensive and difficult to scale. Forecasting future morphology could reduce this burden. Existing neurite digital-twin models such as gated spatiotemporal attention (gSTA) produce a single deterministic forecast without representing variability among plausible futures. We introduce Morphology-Gated Residual Diffusion (MGRD), a compact stochastic surrogate that jointly forecasts twenty future neurite-morphology frames from ten observed frames while conditioning on morphology features derived from the latest observation. On controlled phase-field trajectories, MGRD reduces trajectory-wise mean MAE by 9.7% relative to a matched control while updating 4.46 times fewer parameters. On human iPSC-derived neuron microscopy, MGRD improves all four reported metrics over gSTA, including a 39.6% reduction in trajectory-wise mean MAE and a 45.3% increase in skeleton F1. Without mouse-domain retraining or fine-tuning, MGRD also improves MAE and skeleton F1 on mouse cortical-neurosphere microscopy across 10-40-min sampling intervals and forecast horizons beyond 13 hours. Repeated sampling provides a case-level variance score for ranking forecast difficulty. Retaining approximately 60% of the lowest-variance cases reduces mean MAE by 17.6% on iPSC microscopy and 16.8% on simulation data. MGRD uses 1.01% of gSTA's parameters, requires less than one tenth of its training-update time, and generates a 50-step DDIM trajectory 7.9% faster when morphology features are cached. These results establish MGRD as a compact stochastic surrogate for neurite-morphology forecasting and case prioritization across simulation and microscopy datasets.

---


### 294. [Simpler Methods Work Better for L1 Penalized Logistic Models and Large Datasets](https://arxiv.org/abs/2609.23995)

**<font color=#1a73e8>作者：</font>** Edward Raff, James Holt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear models with an $L_1$-norm penalty remain state-of-the-art for high-dimensional ($d > 1,000,000$) tasks, offering a straightforward method for solving real-world industry problems. Despite their widespread use in industry and utility, many $L_1$ solvers are not effective for general use, are prohibitively slow, and are ineffective in parallelization. This makes them difficult to train in an MLOps pipeline on large industry-scale corpora. In this work, we test several proposed ``state-of-the-art'' solutions from the literature and find that older methods are currently far superior for general use. We also identify several recommendations for academics to perform research that avoids erroneously overconfident results, which can prevent the transition to production use. Equally surprising, we find that a new and simple baseline, using LBFGS on a sub-gradient, is highly effective with minor tweaks, despite being dismissed in the literature for theoretical non-convergence. In practice, we find it is an easier-to-support and easier-to-scale method for production use.

---


### 295. [ShapeLex: Decoupling Local Shape Symbolization and Global Scale Modeling for Text-Controlled Time Series Generation](https://arxiv.org/abs/2609.24003)

**<font color=#1a73e8>作者：</font>** Subo Wei, Jianqi Gao, Mingyan Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-controlled time series generation aims to synthesize sequences that follow natural-language descriptions while remaining faithful to real data distributions. Existing paradigms often couple semantic understanding and sequence modeling in a single continuous latent space, lacking explicit local semantic anchors and separation between global continuous attributes and local discrete shapes. As a result, key local structures may be smoothed, missed, or misplaced. We propose Shape Lexicon (ShapeLex), which decouples text-to-sequence generation into discrete symbolization of local shapes and continuous modeling of global attributes. ShapeLex first induces a reusable vocabulary of discrete shape units, such as rises, spikes, and sharp drops, from training data, forming an interpretable symbolic space. An autoregressive generator then selects shapes according to the textual description, adjusts attributes such as position and duration, and composes them in temporal order into a shape skeleton. Finally, a mixture-density scale head models and samples the overall level and volatility to restore realistic global scale. Experiments on twelve public datasets, real user-written text, and downstream forecasting tasks show that ShapeLex generates series that better match real data distributions than existing methods. In addition, paired supervision is automatically synthesized from the learned vocabulary, avoiding annotation costs that grow with dataset size and improving scalability.

---


### 296. [WebMRIQC: A Web-Based Implementation of MRIQC for Accessible MRI Image Quality Assessment in Resource-Constrained Settings](https://arxiv.org/abs/2609.24014)

**<font color=#1a73e8>作者：</font>** Philip Nkwam, Ifeoluwa Oladeji, Sekinat Zurakat-Aderibigbe 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable quality control (QC) of magnetic resonance imaging (MRI) is essential for reliable diagnostic neuroimaging, yet standard manual assessment is subjective and time-consuming. MRIQC has established standardized automated extraction of image-quality metrics (IQMs), but its reliance on local computational imaging skills and capacity including high-performance computing, limits its adoption in resource-constrained settings (RCS). We present WebMRIQC (this http URL), an open-source browser-based platform that wraps the validated MRIQC engine behind a zero-installation web interface. WebMRIQC automates the DICOM-to-BIDS conversion of de-identified MRI scans, executes the unmodified containerized MRIQC pipeline on a shared compute node governed by a fair-share job queue, and returns an interactive in-browser dashboard. The dashboard grounds every IQM in published quality thresholds, benchmarks each scan against the normative distribution of high-resource open datasets, and supports cross-site multicentre implementation of optimized scan protocols in this http URL describe the system architecture and a validation framework establishing measurement equivalence between WebMRIQC and native MRIQC across thirteen IQMs on the BraTS-Africa and BraTS 2021 datasets. Preliminary results indicate strong agreement for contrast-, signal and noise-based metrics, demonstrating that web-based implementation lowers the barrier to standardized MRI QC and provides a foundation for harmonized, regionally adapted quality benchmarks across RCS imaging sites. The code is publicly available here this https URL.

---


### 297. [InterHier: Learning Interconnected Hierarchical Semantics for Open-Vocabulary Object Detection](https://arxiv.org/abs/2609.24026)

**<font color=#1a73e8>作者：</font>** Yeong-Jin Kim, Ho-Joong Kim, Seong-Whan Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we investigate the limitations of fixed, hand-crafted connectors in hierarchical semantic representations for open-vocabulary object detection. Existing methods establish semantic relationships between base categories and unseen novel categories by placing a fixed connector between adjacent super-/sub-categories. However, such fixed connectors may not optimally capture the relationships within a semantic hierarchy. To address this limitation, we propose interconnected hierarchical semantic representations (InterHier), which utilize a prepended learnable context to globally guide the interpretation of prompts containing hierarchical relationships. InterHier operates in two main stages. First, it constructs a hierarchy-aware prompt by integrating super-/sub-categories and prepending a learnable context. Second, it optimizes this learnable context to align visual region embeddings and textual embeddings. InterHier consistently improves performance over methods that rely on fixed connectors and can be seamlessly integrated into existing open-vocabulary object detection models. Experiments on open-vocabulary object detection benchmarks demonstrate that InterHier achieves competitive performance against state-of-the-art methods.

---


### 298. [When Evidence Conflicts: Reliability-aware Meta-review Generation](https://arxiv.org/abs/2609.24028)

**<font color=#1a73e8>作者：</font>** Xinzhe Wang, Fei Tao, Jiang Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating coherent meta-reviews from multiple peer reviews is challenging when reviewer evidence conflicts and varies in reliability. Existing approaches typically formulate meta-review generation as a multi-document summarization task and aggregate reviewer feedback uniformly, making it difficult to determine which opinions should be prioritized under disagreement. In this paper, we study meta-review generation through reliability-aware evidence aggregation. Our framework first extracts aspect-level opinions from peer reviews and identifies conflicting evidence within each aspect. It then estimates opinion-level support and review-level quality to measure evidence reliability. Based on these signals, the framework assigns reliability-aware weights to reviewer feedback, enabling the generator to prioritize better-supported arguments while preserving diverse perspectives. Experiments demonstrate that our method consistently improves meta-review generation over strong baselines on both automatic and human evaluations, with clear gains in conflict recognition and resolution under high-conflict review scenarios. The code and implementation details are publicly available at this https URL.

---


### 299. [Video-STLayout Pre-training](https://arxiv.org/abs/2609.24031)

**<font color=#1a73e8>作者：</font>** Akash Abdu Jyothi, Greg Mori  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, pre-training has become fundamental to learning effective video representations, enabling strong transfer to downstream tasks. A popular framework in pre-training involves aligning features of a video encoder with that of another modality, for example, language or audio. We introduce Video-STLayout pre-training, a novel strategy for obtaining rich video representations informed by spatio-temporal layout of object bounding boxes. Object layouts can easily be obtained by applying an off-the-shelf object detector on the video frames. Our method uses a contrastive loss to align video features with the layout features from a trained layout encoder. We show the effectiveness of our approach in the task of activity recognition in complex scenes.

---


### 300. [Graph-to-Grid (G2G): Continuous-Coordinate Feature Painting for Soccer Pass Surfaces](https://arxiv.org/abs/2609.24040)

**<font color=#1a73e8>作者：</font>** Kaan Günay, Orhun Gun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense pass surfaces give, for every pitch cell, whether a pass played there would arrive, whether the carrier would choose it, and what the possession would then be worth. The networks that draw them read the state as a raster of per-cell counts, losing where inside a cell each player stands. LiDAR detectors, bird's-eye-view perception and graph weather models move entity features onto a grid, binning each entity to a cell or learning the transfer. We evaluate the interpolated form: each player's features are scattered bilinearly onto the grid at the player's measured coordinates, so the surface loss trains the per-player encoder end to end. Those systems adopt an interface; this paper measures one. On 53,628 passes from the 2022 World Cup, painting improves selection likelihood over the same core fed rasters alone by about a quarter of a nat: in every match of an eight-fold cross-validation, with every arm tuned over five seeds, and after retraining on seven Bundesliga and 2. Bundesliga matches from another provider. Thirteen pre-specified studies locate the gain: painting the nine raw player features with no encoder carries three quarters of it, and the learned encoder and message passing add a smaller, resolved increment. Painting also helps the original SoccerMap and a canonical U-Net, whereas offset channels, a finer raster, an attention painter and a raster-free decoder do not. Frozen across the provider boundary the likelihood advantage is lost; injected tracking error compresses it. These results concern observed-endpoint prediction, not calibrated evaluation of hypothetical passes.

---


> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
