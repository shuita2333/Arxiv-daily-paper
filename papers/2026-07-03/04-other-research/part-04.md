# 📦 其他研究 | 2026年07月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-236](./part-05.md)

---

### 151. [Soft Mixture-of-Recursions: Going Deeper with Recursive Vision Transformers](https://arxiv.org/abs/2607.00774)

**<font color=#1a73e8>作者：</font>** Sang In Lee, Jihun Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent recursive Transformer studies have primarily reused shared parameters across computation steps to construct compact, parameter-efficient models. In this work, we leverage recursion to build effectively deeper Transformers with stronger representational capacity. However, in Vision Transformers, simply increasing recursion depth does not reliably improve performance, as existing recursive approaches do not fully utilize the intermediate representations produced throughout recursive computation. We propose Soft Mixture-of-Recursions (SoftMoR) and its Vision Transformer instantiation, Soft Recursive Vision Transformer (SR-ViT). SoftMoR learns token-wise mixture weights to softly combine outputs from all recursion steps, allowing intermediate representations to be utilized in a learnable and flexible way. Across diverse vision tasks, SR-ViT consistently improves as recursion depth increases with minimal parameter overhead. On ImageNet-1K, increasing recursion depth from 1 to 4 improves SR-ViT-S top-1 accuracy from 79.83% to 82.48% with only 1.7M additional parameters, outperforming the substantially larger DeiT-B while using approximately 27% of its parameters. These results demonstrate that SoftMoR provides a parameter-efficient path to deeper and stronger Vision Transformers through recursion.

---


### 152. [SpiralFovea: Input-Adaptive Foveated Tokenization as a Third Lever of Resource-Adaptive Inference](https://arxiv.org/abs/2607.00780)

**<font color=#1a73e8>作者：</font>** Kyan Mahajan, Mohammad Saqlain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most adaptive-inference techniques for foundation models change what the model does - early exit, MoE routing, KV-cache compression, dynamic attention sparsity. The input that hits the backbone, however, remains a fixed-grid tokenisation indifferent to image content. We argue that this is a missed lever. We present SpiralFovea, a parameter-free, input-adaptive tokeniser in which token identity, location, scale, and count are all functions of local visual entropy and selection completes before any backbone parameter is queried. Around content-driven hotspot anchors, multi-scale spiral rings produce <= 78 patches that replace the standard 196-patch ViT grid at the input stage. Across four canonical fine-grained benchmarks, SpiralFovea yields +1.7-2.1 pp accuracy with a 60% reduction in input tokens, an 84% reduction in self-attention FLOPs at every transformer layer, and 18-29% throughput gains over the matched static tokenisation baseline. A controlled ablation on CUB-200-2011 Genus across four backbones reveals a clean diagnostic: the gain magnitude tracks inversely with the strength of the backbone's whole-image positional prior, isolating self-supervised foundation models as the regime where input-adaptive tokenisation is most valuable.

---


### 153. [LeVLJEPA: End-to-End Vision-Language Pretraining Without Negatives](https://arxiv.org/abs/2607.00784)

**<font color=#1a73e8>作者：</font>** Lukas Kuhn, Giuseppe Serra, Randall Balestriero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language pretraining remains dominated by contrastive objectives, whereas vision-only self-supervised learning has largely adopted non-contrastive methods. At the same time, the role of vision-language encoders has shifted: they are increasingly deployed not as zero-shot classifiers but as the frozen visual backbone of vision-language models and dense prediction systems, which consume the full grid of patch tokens rather than a single pooled embedding. We introduce LeVLJEPA, the first fully non-contrastive end-to-end vision-language pretraining method. LeVLJEPA learns through cross-modal prediction with stop-gradient targets and per-modality distributional regularization, without negatives, temperature, momentum encoder, or teacher-student schedule, and trains stably at large scale. We find that the resulting encoder provides markedly stronger dense semantic features for downstream use: as a frozen vision-language-model backbone, LeVLJEPA is the strongest of the evaluated encoders across GQA, VQAv2, and POPE under two distinct language models, and outperforms contrastive baselines on semantic segmentation, while remaining on par on global readouts such as linear probing. These results establish non-contrastive pretraining as an effective means of producing dense semantic vision features.

---


### 154. [Which Metric Reflects the Spelling Rate Accuracy in Event-Related Potential-Based Brain-Computer Interfaces?](https://arxiv.org/abs/2607.00794)

**<font color=#1a73e8>作者：</font>** Okba Bekhelifi, Naoual El Djouher Mebtouche  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For predictive models, the often-reported performance metrics are the loss and accuracy. In synchronous Brain- Computer Interface (BCI) systems, these metrics are informative for most BCI paradigms; however, for Event-Related Potential (ERP) applications the spelling rate, which measures the number of characters correctly selected is more important as it influences the estimation of information transfer rate (ITR) and any related metric measuring spelling performance. Moreover, ERP-based BCIs hold imbalanced data class distributions, which require reporting metrics that can handle the imbalance, such as the area under the receiver operating characteristic curve (ROC AUC). In this work, we study the correlation of the spelling rate with 13 metrics to identify which among them best reflect user spelling performance and how they are affected by trial repetition. The Results of two datasets (a private LARESI ERP dataset and the public OpenBMI ERP dataset) favor the Brier score, Matthews Correlation Coefficient (MCC), and the metrics that account for class imbalance in binary classification: ROC AUC, area under the Precision-Recall curve (PR AUC), Average Precision (AP), and partial AUC (pAUC). These findings encourage researchers and practitioners to report those metrics in ERP-based BCI experiments.

---


### 155. [Task-Relevant Representation Decoupling for Visual Reinforcement Learning Generalization](https://arxiv.org/abs/2607.00796)

**<font color=#1a73e8>作者：</font>** Jinwen Wang, Youfang Lin, Xiaobo Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual Reinforcement Learning (VRL) has achieved considerable success in solving control tasks. However, generalizing learned policies to new environments remains a major challenge, as agents often overfit to task-irrelevant features in the training environment. To solve this problem, we introduce the concept of decoupling observations into task-relevant and task-irrelevant representations. Building on this idea, we propose a self-supervised Task-Relevant Representation Decoupling (T2RD) algorithm for VRL. This algorithm consists of three components: task-relevant representation consistency, cross-reconstruction, and cross-dynamic prediction. The first two components achieve the decoupling of content and style features, but the resulting content representations are not necessarily task-relevant. To further refine task-relevant features from content representations, we design the third component that introduces dynamic prediction. T2RD achieves State-Of-The-Art (SOTA) generalization performance and sample efficiency in the DeepMind Control Suite and Robotic Manipulation tasks.

---


### 156. [Spotted: Location-informed Reidentification of Hyenas and Leopards in Camera Trap Surveys](https://arxiv.org/abs/2607.00804)

**<font color=#1a73e8>作者：</font>** Halil Sina Kelebek, Julia Hindel, Kobus Hoffman 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animal re-identification (ReID) in camera-trap surveys remains challenging due to low image quality, strong variation in illumination and viewpoint, and highly imbalanced numbers of observations per individual. As a result, current ReID performance is often insufficient for fully automated use, and practical workflows typically depend on expert review of algorithmically proposed candidate matches. Moreover, most existing approaches focus almost exclusively on visual cues and overlook auxiliary information routinely available in field studies, such as image timestamps and camera-trap locations. We introduce Spotted, a location-informed, human-in-the-loop animal ReID framework that integrates visual similarity with spatio-temporal feasibility priors derived from camera locations, thereby reducing the amount of required expert review. Our method (i) computes an image-model-agnostic feasibility score based on the minimum travel speed required for two detections to correspond to the same individual, (ii) uses these feasibility cues as pseudo-supervision to train a lightweight head on top of a frozen visual foundation model, and (iii) fuses adapted visual similarity with spatio-temporal feasibility to obtain a robust pairwise matching score. We additionally integrate an active pair sampling strategy to accelerate annotation by initially prioritizing uncertain predictions. We evaluate Spotted on three challenging camera-trap ReID datasets comprised of spotted hyenas and leopards, which we release as part of this work. Our model improves average top-5 identification accuracy by 9pp, 2pp and 9pp over the best baseline on our LeopardID102, SpottedHyenaID109 and SpottedHyenaID415 datasets, respectively. Further, we show that our human-in-the-loop strategy reduces the number of queried comparisons by up to 69pp while achieving equivalent positive matches.

---


### 157. [Training-Free Debiasing of Diffusion Models via CLIP-Guided Denoising Optimization](https://arxiv.org/abs/2607.00817)

**<font color=#1a73e8>作者：</font>** Dain Kim, Jinseo Kim, Sungyong Baik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models achieve impressive visual quality, yet demographic bias remains a challenge, as neutral prompts consistently produce stereotypical representations across gender and race. Existing approaches remain limited by costly retraining or by inference-time interventions that often degrade image quality and semantic alignment. We propose Text Embedding Steering (TES), a training-free framework that mitigates demographic bias by directly optimizing conditional text embeddings during the diffusion process. We show that a two-stage strategy - early-stage global alignment followed by iterative denoising-time refinement with CLIP-based feedback - enables stable and controllable attribute steering without modifying model parameters. Extensive experiments on Stable Diffusion demonstrate that TES outperforms existing training-free baselines in fairness while maintaining competitive image quality. These results highlight that inference-time text embedding optimization is a practical and scalable solution for fairness-aware generation in diffusion models.

---


### 158. [Stitched Embeddings: A Unified Latent Space for 3D Garments and 2D Patterns](https://arxiv.org/abs/2607.00829)

**<font color=#1a73e8>作者：</font>** Andrea Sanchietti, Riccardo Marin, Bharat Lal Bhatnagar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While garments are essential for realistic digital humans, their topological variety makes them much harder to model than parametric bodies. Traditional tailoring relies on 2D sewing patterns, yet bridging these patterns to 3D geometry currently requires physical simulations. We present Stitched Embeddings, the first simulation-free framework to unify 3D garment reconstruction and sewing pattern inference within a single bidirectional latent space. By leveraging the geometric priors of a pretrained 3D foundation model, our approach overcomes the data scarcity typically associated with high-quality garment modeling. We propose to use the BoxMesh as a critical intermediate representation to align 2D panels into 3D configurations without the computational overhead of a simulator. This architecture achieves state-of-the-art accuracy in pattern reconstruction while significantly improving efficiency. Furthermore, our differentiable pipeline enables novel applications, including pattern recovery from meshes and 3D editing from 2D patterns. Finally, this work provides a scalable link between neural 3D vision and the physical garment manufacturing pipeline. Project Page: this https URL

---


### 159. [Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences](https://arxiv.org/abs/2607.00832)

**<font color=#1a73e8>作者：</font>** Zhenjia Li, Jinrang Jia, Yifeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A single panorama captures the full visual sphere from one camera center, yet confines users to looking around in place without enabling true scene exploration. Converting a single panorama into a persistent, renderable 3D representation for free-viewpoint navigation has attracted growing interest; existing methods either adopt iterative per-view completion that propagates inpainting results to update the underlying geometry, leading to progressive error accumulation and cumbersome multi-step pipelines, or leverage the temporal consistency priors of video generation models, yet the continuous-trajectory constraint intrinsic to such models limits their flexibility in covering scenes from multiple directions simultaneously. We present Pano2World, which takes a single indoor panorama as input and directly outputs a persistent, explorable 3D Gaussian scene. Given the source panorama, Pano2World first reconstructs a coarse 3D Gaussian proxy and renders it at adaptively sampled nearby poses to obtain geometrically aligned guidance panoramas; a panoramic diffusion model then jointly denoises all target views via View-Aware Attention Routing, where each target view simultaneously receives geometric constraints from its corresponding guidance panorama and global semantic guidance from the source panorama, naturally enforcing cross-view consistency. To avoid the information loss incurred by decoding the multi-view hidden features formed during joint denoising back to the pixel domain via VAE, we introduce Latent Feature Adapter, a geometry-aware bridge module that directly distills these hidden features into a scene latent, subsequently decoded into the final 3D Gaussian scene. Experiments demonstrate that Pano2World significantly outperforms existing methods on the multi-position panoramic novel-view synthesis benchmark.

---


### 160. [Spectroscopy Analysis with Machine Learning Regression for the Quantification of Carbon and Nitrogen Contents in Inceptisol and Oxisol Soil Types: Comparing Different Preprocessing and Validation methods as well as Feature Importance](https://arxiv.org/abs/2607.00834)

**<font color=#1a73e8>作者：</font>** Vinicius Herique Kieling, Guilherme Macedo Baggio, Felipe Augusto Bueno Rossi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Near-Infrared (NIR) spectroscopy has emerged as a promising alternative to traditional soil analysis methods, offering advantages such as speed, low cost, and non-destructive testing. This work proposes a machine learning (ML) approach to calibrate predictive models for carbon (C) and nitrogen (N) content in Oxisols and Inceptisols, utilizing NIR spectral data acquired with a portable MyNIR device. Various preprocessing methods were evaluated, with the most effective being the Savitzky-Golay (SG) filter and a robust outlier removal method based on the Nonlinear Iterative Partial Least Squares (NIPALS) algorithm coupled with a Huber loss function. Multiple validation strategies were compared, including 10-fold cross-validation, leave-one-out, and holdout via the Kennard-Stone method, followed by standardization. Stacking ensemble learning models were employed, using Partial Least Squares (PLS), Support Vector Regression (SVR), and Ridge as base models, with linear regression as the meta-model. The models were evaluated using R2, Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and Ratio of Performance Deviation (RPD) metrics. The performance gap between soil types suggests the influence of pedological characteristics. Furthermore, the models achieved an RPD > 2.0 with low overfitting, validating the potential of this approach for rapid C and N quantification. This study contributes to the optimization of sustainable agricultural practices, aligning with the demand for efficient and environmentally friendly analytical methods. The developed technique enables faster decision-making for producers and consultants based on organic matter content, fertility indicators, and nutrient availability.

---


### 161. [Rethinking Multi-Label Image Classification With Deep Learning: Taxonomy, Challenge, and Outlook](https://arxiv.org/abs/2607.00839)

**<font color=#1a73e8>作者：</font>** Xuelin Zhu, Xiu-Shen Wei, Jiawei Ge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-label image classification (MLIC), a fundamental task in computer vision, focuses on identifying multiple objects or concepts within an image, underpinning numerous read-world applications, such as autonomous driving, disease diagnosis, recommendation system, and mobile service robot. Over the past decade, deep learning paradigms based on convolutional neural networks, recurrent neural networks, and Transformers have significantly advanced this field, owing to their powerful capability in visual representation and relationship modeling. These advances have markedly improved the robustness, scalability, and generalization ability of MLIC models across diverse datasets and application domains. In this survey, we provide a comprehensive review of the deep learning-based literature on MLIC. Concretely, we first revisit the background, including problem definition, datasets, backbones and evaluation metrics. Next, we develop a plausible taxonomy for the deep learning-based MLIC approaches, organizing them into six groups: region-oriented methods, label-oriented methods, architecture-oriented methods, representation-oriented methods, learning-oriented methods, and data-oriented methods. Finally, we provide an insightful exposition of the underlying learning game in MLIC and its implications for other vision domains, and we empirically summarize the key challenges and research directions in MLIC while outlining promising avenues for future development. We believe this survey offers the research community a holistic and systematic perspective on MLIC, thereby facilitating subsequent exploration and innovation in this field and beyond.

---


### 162. [The Course of News Events: A Comparison of Bottom-Up and Top-Down Approaches for Collecting Text-Based Data about Disasters](https://arxiv.org/abs/2607.00849)

**<font color=#1a73e8>作者：</font>** Brielen Madureira, Andreas Niekler, Mariana Madruga de Brito  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> News articles are an important source of information on disaster impacts and adaptation. A key methodological challenge in socio-environmental studies is how to select a representative data sample. Two approaches are common: querying news databases top-down with the aid of an existing disaster inventory or using NLP methods to cluster news texts bottom-up based on temporal and spatial features. Using a dataset of German news about landslides worldwide, we compare these approaches and discuss variations in event coverage. Such research design decision can influence the resulting news sample, affecting its use in studies of inequality in media coverage, disaster monitoring and inventory enrichment.

---


### 163. [Mirror-Fusion Attention for Reflection-Aware Self-Supervised Representation Learning](https://arxiv.org/abs/2607.00850)

**<font color=#1a73e8>作者：</font>** Ruixin Li, Jin Liu, Yuling Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most self-supervised learning (SSL) methods encourage invariance across augmentations, but strict flip invariance can suppress informative left--right correspondences in approximately bilateral data such as medical images and human faces. We propose Mirror-Fusion-Augmented Self-Supervised Learning (MFASSL), a Vision Transformer framework that injects a soft reflection prior into standard SSL without redesigning the backbone. MFASSL constructs mirror-paired views aligned to an estimated symmetry axis and introduces a lightweight Mirror-Fusion Attention (MFA) module for adaptive token-level interaction between mirrored regions while preserving asymmetric cues. The base SSL objective is further coupled with reflection-consistency and mid-layer token-alignment losses. Across CheXpert, BraTS, CelebA-HQ, and WFLW, MFASSL improves downstream performance, calibration, and reflection robustness over MoCo-v3, DINO, and MAE baselines under matched ViT-B/16 settings. It also achieves stronger and more consistent gains than recent equivariant SSL approaches with only approximately 2.7\% additional parameters. These results show that lightweight geometry-aware priors can effectively complement invariance-based SSL.

---


### 164. [TrajLoc: Trajectory-Attention Localization for Multi-Object Motion Control](https://arxiv.org/abs/2607.00861)

**<font color=#1a73e8>作者：</font>** Omer Sela, Inbar Huberman-Spiegelglas, Michael Rotman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controlling the motion of multiple objects in image-to-video (I2V) generation requires preserving object identities while enforcing adherence to distinct target trajectories. This becomes particularly challenging as the number of objects increases and their paths intersect or occlude one another. Existing approaches entangle multiple trajectories within a shared, dense conditioning signal, making object-level correspondence difficult to preserve in crowded scenes. We depart from this paradigm and enforce a strict, per object spatial constraint that isolates instances independently. Our method, TrajLoc, achieves this directly within the attention layers by substituting the cross-attention weights of each object token with a Gaussian heatmap centered on its target location at every frame. The same per object token interface carries trajectory and depth through a learned embedding and preserves identity by encoding first frame appearance in place of an object token. Evaluations across six datasets, featuring up to 20 simultaneously controlled objects and out of distribution real world scenes, demonstrate that our method consistently improves both visual fidelity and trajectory adherence. Applied to two architecturally distinct backbones (CogVideoX 5B and WaN 2.1 14B), our approach achieves average gains of +4.3 dB PSNR and a 51% reduction in trajectory end point error compared to the strongest baselines. Project page: this https URL

---


### 165. [Constrained Bayesian Optimisation with Multiple Information Sources](https://arxiv.org/abs/2607.00865)

**<font color=#1a73e8>作者：</font>** Hauke Maathuis, Roeland De Breuker, Saullo Castro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian Optimisation (BO) under unknown constraints is particularly challenging when feasible regions are small. In such settings, existing methods that typically rely solely on evaluations of the true objective and constraints struggle to efficiently explore the design space. However, many real-world applications offer auxiliary data sources (e.g. surrogate models or simplified simulations) that can support early exploration. Despite this potential, their integration into constrained BO remains largely unexplored. We propose a general multi-source framework that extends constrained Max-value Entropy Search, capturing inter-source correlation while balancing evaluation cost and information gain. Experiments on both synthetic and physics-based benchmarks show that our method efficiently identifies feasible and optimal solutions, even when auxiliary data are only weakly correlated. The proposed approach consistently outperforms existing methods, particularly in early-stage exploration.

---


### 166. [EFlow: Learning Evidence Flow for Long-Video Reasoning with Adaptive Reflection](https://arxiv.org/abs/2607.00867)

**<font color=#1a73e8>作者：</font>** Wenhao Zhang, Kuanwei Lin, Xuyi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video reasoning is fundamentally constrained by how models acquire and utilize visual evidence. Existing tool-augmented video frameworks often interleave temporal grounding and answer reasoning within a single trajectory, causing early semantic hypotheses to bias evidence localization. We term this failure mode premature semantic commitment, where biased grounding retrieves incomplete evidence and incomplete evidence further reinforces incorrect reasoning. To address this issue, we propose EFlow, an evidence-first video reasoning framework built upon Qwen3-VL. EFlow explicitly separates temporal grounding and logical reasoning through CoT for Temporal Grounding and CoT for Reasoning, enabling the model to retrieve relevant evidence before answer inference. In addition, EFlow introduces a confidence-aware reflection mechanism that re-evaluates the full video when retrieved evidence is potentially insufficient. We further construct dedicated trajectory datasets and train EFlow through supervised fine-tuning, reinforcement learning, and reinforcement fine-tuning. Extensive experiments across five video understanding benchmarks demonstrate that EFlow consistently improves long-video reasoning performance.

---


### 167. [Dynamic Bidirectional Pattern Memory: A Production-Scale Empirical Characterisation of Inference-Time Gating in Clinical NLP](https://arxiv.org/abs/2607.00870)

**<font color=#1a73e8>作者：</font>** Ali H. Lazem, William Teahan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study inference-time pattern-memory gating in a production-scale clinical natural language processing (NLP) pipeline. The pipeline pairs a generator (Llama-3.3 70B) proposing extractions with a verifier (MMed-Llama-3.1 70B) accepting or rejecting them, over 167,034 PMC-Patients narratives, and adds a lightweight memory that learns at deployment which extractions to filter, so the verifier need not re-examine candidates already seen to fail. We report four findings. First, learning filtering rules directly from the verifier's rejections failed at full scale: the relation-extraction filter stayed empty despite 785,797 logged rejections, because they were spread too thinly across too many distinct forms to accumulate. Second, a simpler rule using a fixed clinical ontology produced the same filtering without the verifier, capturing 49,734 ontology-violating relations on a held-out 5,000-patient set. Third, of five versions of the question-answering filter, four failed for distinct, instructive reasons; the fifth succeeded by checking whether a patient's extracted entities support the question asked, and where it applies was 1.84 times likelier to flag an answer the verifier would reject than one it would accept. Fourth, one pattern held across all five: a filter is selective only when it tests the same evidence the verifier weighs, not when it imitates the verifier's output. Together these give a transferable result for any generator-verifier pipeline: the most natural memory design can fail silently at scale, and whether a pre-generation gate is selective is decided before any engineering effort, by whether its signal probes the question the verifier itself answers. Throughout, the system flags suspect extractions rather than deleting them, so every decision stays visible for clinical review. All code and test artefacts are released openly.

---


### 168. [Self-Evolving Agents with Anytime-Valid Certificates](https://arxiv.org/abs/2607.00871)

**<font color=#1a73e8>作者：</font>** Biswa Sengupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents violate the assumption behind most learning-theoretic guarantees: the data, evaluator, components, and hypothesis space are produced by the policy being updated. We present \textbf{SEA}, an architecture that confines self-modification to a small steering adapter and a versioned harness around a \emph{frozen} base model and admits each modification only through an anytime-valid gate that emits an auditable certificate against a fixed error budget. Five loop controllers compose published guarantees; because such gates can only \emph{select} among behaviors the frozen base already produces, five verifier-in-the-loop mechanisms -- best-of-$N$, micro-step search, self-authored reproduction oracles, search-layer control, and self-repair -- supply the dense, grader-free signal the gates require, computed from the issue text alone. On a $52$-instance SWE-bench Verified subset across four base models, base capability is the dominant, confound-free effect, and on two strong base models a deliberate no-op-composite control isolates the suite's contribution at $+4$ and $+5$ (\textsc{Glm}~5.2 $24\to28$; \textsc{Gpt} $29\to34$, the $65\%$ best), with event logs confirming that its mechanisms fire and prevent regressions. Results are single-run on expensive evaluations; confirming run-to-run variance and adapting the per-task algorithm mix are future work.

---


### 169. [How Ethos and Pathos Appeals Resonate in Reader Interpretations of Social Media Messages](https://arxiv.org/abs/2607.00873)

**<font color=#1a73e8>作者：</font>** Ewelina Gajewska, Katarzyna Budzynska, Jaroslaw Chudziak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rhetorical strategies and their influence on audiences are often studied through social media posts and comments. However, this focus overlooks the universal audience, which is the majority of readers who remain silent and do not explicitly express how a message affects them. This study investigates how two classical modes of persuasion, ethos and pathos, resonate in the silent audience's interpretations of meaning. Using a dataset of social media sentences paired with human-written interpretations, we label both sources for ethos and pathos and assess whether these rhetorical appeals are preserved. Our analyses show that interpretations diverge from the original sentences in 30% of cases, with rhetorically charged content eliciting greater variability than neutral content. We further find that ethos and pathos in original sentences can predict audience attitudes toward the author, underscoring the subtle ways rhetoric shapes perception beyond visible engagement.

---


### 170. [Improving Sparse-View 3DGS Generalization via Flat Minima Optimization](https://arxiv.org/abs/2607.00885)

**<font color=#1a73e8>作者：</font>** Kangmin Seo, Sangeek Hyun, MinKyu Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in neural rendering have established 3D Gaussian Splatting (3DGS) as a highly efficient representation for novel view synthesis, enabling fast training and real-time rendering with strong fidelity. However, when supervision is limited to sparse input views, 3DGS tends to overfit to the observed images and generalize poorly to unseen viewpoints. We address this challenge from the perspective of flat minima (FM) optimization, which seeks solutions that remain stable under small parameter perturbations. Viewing Gaussian parameters as trainable weights, we adapt FM principles to the geometric and dynamic nature of 3DGS with a lightweight training framework. Our method regularizes optimization with controlled Gaussian perturbations that account for each Gaussian's anisotropy and the training progress, preserving fine details while improving robustness to sparse-view overfitting. To further stabilize this flat minima optimization process, we introduce periodic reinitialization, which temporarily returns non-positional parameters to their initial states for a short window. Together, these techniques integrate seamlessly into existing 3DGS pipelines without architectural changes. Experiments on LLFF and Mip-NeRF360 datasets demonstrate improved quantitative metrics and perceptual quality under sparse-view supervision, producing reconstructions that are sharper, more stable, and better generalized to novel viewpoints.

---


### 171. [Beyond Pixel Overlap: A Framework for Decomposing Segmentation Evaluation Metrics](https://arxiv.org/abs/2607.00886)

**<font color=#1a73e8>作者：</font>** Youwei Pang, Xiaoqi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluation metrics are central to binary target segmentation because they determine how progress is measured, compared, and interpreted. In this paper, target denotes the task-defined positive region to be segmented rather than a generic foreground object. It may be salient, camouflaged, transparent, glass-like, mirror-like, shadow-like, lesion-like, or defined by other application-specific semantics. We treat existing metrics as compositions of modular design choices rather than isolated formulas. The proposed framework decomposes each metric into five stages covering prediction representation, target extraction, target matching, score computation, and metric reporting. We use this framework to analyze representative metrics and show how newer metrics address specific limits in earlier protocols. The stage choices keep each metric's assumptions visible. We then discuss the design space opened by the framework and its implications for task-aware evaluation protocols. Reference code is available at this https URL.

---


### 172. [Geometry-Aware Cross-Height Channel Knowledge Map Prediction for UAV-Assisted Communications With Uncertainty-Guided 3D Sensing](https://arxiv.org/abs/2607.00887)

**<font color=#1a73e8>作者：</font>** Zhihan Zeng, Amir Hussain, Yue Xiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-altitude Unmanned Aerial Vehicles (UAVs) often need to infer channel knowledge across a range of heights from only sparse observations collected at a few altitude layers. To address this challenge, this paper studies height-conditioned cross-height channel knowledge map (CKM) prediction for UAV-assisted communications in geometry-rich urban environments. We develop a geometry-aware conditional prediction framework that combines urban scene priors, sparse multi-altitude observations, and target-height descriptors to reconstruct dense CKMs at unobserved target heights. An uncertainty head is further introduced to characterize prediction confidence and to support cost-aware online UAV sensing under motion and safety constraints. Experiments on a layered aerial CKM benchmark show that the proposed Feature Pyramid Network (FPN)-Transformer achieves the best overall performance under both unseen-scene zero-shot and legacy patch-random protocols, reducing the Root Mean Square Error (RMSE) to 5.347dB and 1.111dB, respectively, compared with 6.937dB and 1.221dB for the strongest baseline 3D-RadioDiff. Moreover, after applying our unseen-scene few-shot adaptation, the RMSE further decreases from 5.347dB in zero-shot prediction to 3.518dB with 10-shot two-height support, while the uncertainty-guided cost-aware sensing policy improves active reconstruction from 6.94dB at initialization to 4.79dB at sensing budget 40, outperforming uncertainty-only sensing at 5.08dB and random aerial sampling at 5.84dB.

---


### 173. [DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](https://arxiv.org/abs/2607.00889)

**<font color=#1a73e8>作者：</font>** Seok-Young Kim, Abdelrahman Elskhawy, Taewook Ha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present DeWorldSG, a novel framework that generates spatio-temporally robust 3D Semantic Scene Graphs from RGB-D sequences. Existing methods often struggle to construct reliable 3D scene graphs due to unstable 3D object representations and missing relations caused by frame-wise inference. DeWorldSG addresses these issues by estimating instance-level geometric 3D Gaussian distributions through depth-guided filtering and representing each object as a probabilistic 3D node rather than a single projected point. To mitigate relational sparsity from frame-wise inference, our framework further aggregates spatiotemporal evidence across object pairs and refines relations using contextual priors derived from a world model (V-JEPA 2). Experiments on the 3DSSG and ReplicaSSG datasets demonstrate state-of-the-art (SoTA) performance in both object and predicate prediction, while producing temporally consistent scene structures. In particular, our method improves triplet recall by 77.4% and predicate recall by 23.2% over prior SoTA approaches, making it suitable for robotic manipulation and AR applications. Our code and models are open-sourced.

---


### 174. [MG-RWKV: Multi-Grained Context-Aware RWKV for Temporal Forgery Localization](https://arxiv.org/abs/2607.00902)

**<font color=#1a73e8>作者：</font>** Jingchen Ni, Cangjin Yu, Dan Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driven by Artificial Intelligence-Generated Content (AIGC), the authenticity of audio-visual content is facing severe challenges. Temporal Forgery Localization (TFL) aims to precisely identify manipulated segments within untrimmed sequences. However, existing methods are limited by CNNs' local receptive fields or Transformers' quadratic complexity, while emerging linear models often struggle to balance global authentic context compression with local abrupt forgery perception. To address this, we propose MG-RWKV, a multi-granularity framework that leverages the data-dependent state evolution of RWKV to achieve efficient full-sequence processing with O(T) complexity. Our framework features three core innovations: (1) a Bidirectional RWKV architecture that captures bidirectional temporal contexts without quadratic overhead; (2) a Multi-Granularity Mixture of Experts (MG-MoE) that performs dynamic routing over explicit temporal receptive fields, adaptively selecting granularities based on forgery duration to significantly enhance decision interpretability; and (3) Cross-Granularity Consistency (CGC), which aligns adjacent feature pyramid levels through hierarchical scale-wise pairing and spatial boundary-aware weighting, effectively reducing false positives in authentic regions. Extensive experiments on Lav-DF, TVIL, and Psynd datasets demonstrate that MG-RWKV achieves state-of-the-art performance with low computational cost.

---


### 175. [Two AI Metrics Diverged: Will it Make All the Difference?](https://arxiv.org/abs/2607.00913)

**<font color=#1a73e8>作者：</font>** Alex Fogelson, Zachary A. Brown, Hans Gundlach 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As exponential compute scaling continues, will the capabilities of frontier AI models outstrip what is accessible to developers on a small fixed budget? Or will capabilities converge, with "meek models inheriting the earth"? Building on Gundlach et al. (2025b), we show that the answer depends on how we value and measure AI capabilities. We discuss conventional performance measures and show that, while validation loss shows a shrinking gap, on other metrics frontier models grow their lead forever. Classifying performance metrics by their functional forms in relation to training (and inference) compute, we provide tight mathematical conditions for determining which metrics favor meek models, and show that bounded performance metrics always do. But careful interpretation of performance metrics is essential: we show that many common bounded metrics have closely-related counterpart metrics that are unbounded (and vice versa). Determining the apt metric in a domain is a prerequisite for policy, since bounded and unbounded metrics may suggest opposing policy responses. If a particular capability -- like software engineering, synthetic biology, or rhetorical persuasiveness -- is unbounded when measured in the terms we care about, frontier-level capability will likely be concentrated in the hands of a few wealthy actors. Conversely, if that capability is instead bounded, frontier-level capabilities proliferate through meek models into the hands of the many.

---


### 176. [Condensing Large-Scale Datasets Directly with Minimal Information Loss](https://arxiv.org/abs/2607.00916)

**<font color=#1a73e8>作者：</font>** Xinyi Shang, Peng Sun, Bei Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in scaling dataset distillation rely heavily on decoupled information extraction pipelines, comprising SQUEEZE, RECOVER, and RELABEL stages. Despite their scalability to large-scale datasets, these methods suffer from prohibitive computational overhead and poor cross-architecture generalization. In this paper, we reveal the root cause of these bottlenecks: the implicit dual-compression process, from data to model and back to images, inherently induces severe information loss. Crucially, we empirically and theoretically demonstrate that this loss creates a distribution shift that fundamentally compromises the widely adopted RELABEL strategy, transforming the pre-trained model into an unreliable labeler that yields sub-optimal labels. To overcome these critical flaws, we propose CIM, a novel, metric-driven framework that abandons the flawed dual-compression paradigm. Instead, CIM explicitly quantifies and minimizes the information gap between the original and synthetic datasets. By directly aligning the data distributions, our approach ensures high-fidelity information condensation and inherently satisfies the prerequisites for effective relabeling. Extensive experiments demonstrate that CIM establishes a new state-of-the-art. Notably, it distills ImageNet-1K at an IPC=10 in merely 80 minutes on a single RTX-4090 GPU, achieving an unprecedented 48.7% Top-1 accuracy on ResNet-18 and significantly outperforming previous SOTA approaches, such as NRR-DD and DELT, by 2.6% and 2.9%, respectively. Our code is available at this https URL.

---


### 177. [From Personas to Plot: Character-Grounded Multi-Agent Story Generation for Long-Form Narratives](https://arxiv.org/abs/2607.00918)

**<font color=#1a73e8>作者：</font>** Aayush Aluru, Chloe Ho, Muhammad Hammouri 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) have demonstrated impressive creative fiction generation, they struggle to maintain narrative consistency and coherent plot lines in long-form stories. In this work, we introduce a unified framework for long-form narrative generation and verification. MAGNET, a multi-agent goal-driven narrative engine for storytelling, generates stories with persona-grounded character agents that propose actions based on a shared world state and evolving story goals, while ATLAS is a graph-based pipeline that compares scene-level world representations across a generated story to detect hallucinations. By evaluating MAGNET using an LLM editor, pairwise rubric scoring, and ATLAS, we show that our framework produces coherent narratives compared to single-model prompting and IBSEN. At 100 pages, MAGNET reduced annotations and hallucinations by 41 and 50%, respectively, compared to the single model baseline and by 34 and 45%, respectively, compared to IBSEN, with pairwise rubric evaluation showing similar results. These results suggest that long-form narratives can emerge from explicit world-state tracking and goal-driven multi-agent generation, providing a foundation for controllable and structurally coherent long-form narrative generation.

---


### 178. [GMO-E$^2$DIT: Grounded Multi-Operation Editing for E-Commerce Images](https://arxiv.org/abs/2607.00920)

**<font color=#1a73e8>作者：</font>** Zipeng Guo, Xiaoan Liu, Lichen Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world e-commerce image editing often requires multiple, localized, and auditable operations rather than global restyling. This compositional nature poses a dual challenge: models must precisely apply all requested edits to the correct regions while preserving unmodified content, even under ambiguous instructions. Existing one-shot editors conflate intent resolution, spatial grounding, and synthesis into a single step, frequently resulting in partial execution failures, which is unacceptable for commercial scenarios. To address this, we introduce GMO-E$^2$DIT, an agentic editing framework that couples a Vision-Language Model (VLM) with a mask-conditioned image editor to tackle structured multi-turn task completion. Given an underspecified instruction, the VLM agent constructs a region-grounded edit agenda, effectively decoupling cognitive reasoning from generative rendering. The framework then executes sub-programs via operation-aware masks and references, utilizing a reflection-driven loop to inspect intermediate results and determine the subsequent state. This iterative mechanism reliably preserves safe partial progress, retries unfinished operations, and recovers from errors. Furthermore, we develop a unified data pipeline providing aligned supervision for planning, execution, and reflection, alongside EComEditBench, a comprehensive benchmark for instruction-driven evaluation. Extensive experiments demonstrate that GMO-E$^2$DIT achieves competitive performance compared to strong closed-source models, yielding superior instruction accuracy and edit fidelity over existing baselines.

---


### 179. [Human-Machine Collaboration on Generative Meta-Learning: Model and Algorithm](https://arxiv.org/abs/2607.00926)

**<font color=#1a73e8>作者：</font>** Midhun Parakkal Unni, Samuel Kaski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalizing machine learning models to environments that differ from their training distribution remains a critical hurdle, particularly when data from the target domain is entirely or partially unavailable. We propose Generative Meta-Learning with Human Feedback (GMHF), a novel framework that bridges this domain gap by leveraging expert intuition to guide data synthesis. Grounded in a theoretical analysis of generalization error, we derive bounds demonstrating that aligning the distribution of generated data with human beliefs regarding the target physics significantly mitigates risk. GMHF operationalizes this insight by employing a Conditional Neural ODE (cNODE) as a generative digital twin, coupled with a Reinforcement Learning (RL) agent. The agent iteratively refines the latent physical parameters of the generated trajectories based on feedback, effectively steering the meta-learner toward the unobserved target distribution. Empirical validation on a nonlinear Duffing oscillator shows that GMHF substantially reduces deployment loss as expert reliability increases, and that the divergence between generated and target data falls under reliable feedback, directly corroborating the divergence-minimisation mechanism predicted by our theory. Further experiments on a non-dynamical probabilistic model confirm that the framework extends beyond ODE-governed systems, establishing human-AI collaboration as a rigorous catalyst for robust generalisation under distribution shift.

---


### 180. [Explainable AI for Cancer Drug Response Prediction: Beyond Univariate Feature Attributions](https://arxiv.org/abs/2607.00931)

**<font color=#1a73e8>作者：</font>** Martino Ciaperoni, Margherita Lalli, Simone Piaggesi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting cancer drug response from transcriptomic profiles is a cornerstone of precision oncology, yet the scientific value of machine learning models hinges not solely on predictive accuracy, but also on their capacity to generate reliable biological insights. Current explainability approaches in this setting are computationally costly, lack robustness, and reduce complex drug response to univariate gene importance scores, overlooking the coordinated gene activity that drives sensitivity and resistance. In this work, we present ILLUME+, a scalable post-hoc explainability framework that moves beyond single-gene assessments to capture multiple, complementary forms of explanation. Integrated into our end-to-end pipeline, ILLUME+ produces more stable gene importance scores than existing baselines, recovers established drug-gene associations and mechanisms of action, and enables AI-assisted hypothesis generation to uncover novel interaction-driven molecular signals in cancer biology.

---


### 181. [Diffeomorphic Optimization](https://arxiv.org/abs/2607.00947)

**<font color=#1a73e8>作者：</font>** Ludwig Winkler, Andrew Leaver-Fay, Joseph Kleinhenz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models learn data distributions that reside on a low-dimensional manifold within a higher-dimensional ambient space. Optimizing differentiable objectives on this manifold is challenging: the ambient loss landscape is high-dimensional, rugged, and non-convex. Direct gradient descent, blind to the manifold's geometry, quickly drifts off it. Diffeomorphic optimization starts from the observation that diffusion and flow models provide a map from the data manifold to a much simpler base space in which we perform gradient descent. Using differential geometry, we show this is equivalent to Riemannian gradient descent on the data manifold up to $\mathcal{O}(\lambda^2)$ corrections, keeping trajectories on-manifold by construction and yielding a smoother optimization surface. For protein design, we extend diffeomorphic optimization to the matrix Lie groups $\mathrm{SO}(3)$ and $\mathrm{SE}(3)$, deriving an autograd-compatible $\mathrm{SO}(3)$ gradient and a generalized adjoint-state method for backpropagation through Lie-group ODE solvers. Diffeomorphic optimization improves over tuned guidance on secondary-structure targeting with FrameFlow ($91.3\%$ vs. $63.3\%$ of residues in the Ramachandran target), outperforms OC-Flow on peptide binding affinity at $2\times$ the speed, and reduces Rosetta energies by thousands of units across the PDB test set for structures with hundreds of residues.

---


### 182. [Dataset Biases and Shortcut Learning in Motion-Based AI-Generated Video Detection](https://arxiv.org/abs/2607.00948)

**<font color=#1a73e8>作者：</font>** Joren Michels, Lode Jorissen, Nick Michiels  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The visual quality of AI-generated videos has improved drastically in recent years, making it increasingly difficult for humans to distinguish between real and synthetic media. In this work, we evaluate the robustness and applicability of four state-of-the-art motion-based AI-generated video detectors. We identify significant preprocessing and sampling biases in these methods and demonstrate that they account for a substantial portion of their reported performance. Furthermore, we find that these detectors are highly sensitive to motion patterns specific to their evaluation datasets, where AI-generated videos generally exhibit less inter-frame movement than real videos. We show that for all detectors, performance collapses to near-random levels when evaluated on a dataset that does not contain this motion bias. Additionally, through dataset rebalancing and the application of simple spatial augmentations, we observe severe performance degradation across all evaluated models. In contrast, we find that an existing frequency-based detector maintains strong performance across all evaluated datasets, suggesting that frequency-based approaches may offer a more generalizable path forward for AI-generated video detection. We hope that our work raises awareness towards these vulnerabilities and encourages the development of more representative, unbiased datasets and more robust evaluation protocols.

---


### 183. [Learning Cardiac Motion Priors for Implicit Neural Representations](https://arxiv.org/abs/2607.00955)

**<font color=#1a73e8>作者：</font>** Andrew Bell, George Webber, Andrew P King 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) are well suited to cardiac motion estimation, providing continuous, compact representations of motion fields. However, fitting an INR to each image sequence is time-consuming and sensitive to the optimisation trajectory. Learned priors can help guide optimisation towards plausible motion fields and enable faster adaptation, but learning priors for cardiac motion INRs remains under-explored. In this work, we compare four strategies for learning cardiac motion priors, including a population prior learned by joint optimisation, a consensus prior obtained by weight averaging, auto-decoders, and meta-learning. Using short-axis tagged cardiac magnetic resonance images from the UK Biobank, we evaluate their impact on tracking accuracy, motion behaviour, and adaptation trajectory.
All learned priors substantially improved early adaptation performance compared with random initialisation. While the simple consensus prior was effective, auto-decoders recovered large deformations faster during early adaptation. Meta-learning achieved strong early performance and maintained the best adaptation trajectory over 50 iterations.

---


### 184. [Aionoscope: Debugging Latent-State Accessibility in Time-Series Representations](https://arxiv.org/abs/2607.00956)

**<font color=#1a73e8>作者：</font>** Alexander Chemeris, Ming Jin, Randall Balestriero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series models are often evaluated by what they can forecast or classify, but those scores do not show whether their representations preserve the process state a user may want to inspect: event timing, phase, amplitude, frequency, or regime variables. We introduce Aionoscope, a generator-based diagnostic tool for debugging latent-state accessibility in frozen time-series representations. Aionoscope separates process generation from observation rendering, producing seeded synthetic streams with exact categorical and dense labels across mixture complexity and nuisance variation.
We instantiate Aionoscope as Primitive Process Mixtures and evaluate 37 model-plus-adapter systems with a common pooled linear-probe protocol. The main result is a mismatch between coarse and fine-grained accessibility. Most systems make component presence easy to recover, but expose dense process state much less reliably: the highest observed dense-probe row reaches 0.689 mean masked $R^2$, while a dense-feature oracle reaches 0.999. This is the failure mode Aionoscope is designed to surface: a representation can look informative at the level of "what kind of signal is present" while hiding the timing, phase, amplitude, frequency, or regime variables needed for debugging.

---


### 185. [LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning](https://arxiv.org/abs/2607.00958)

**<font color=#1a73e8>作者：</font>** Alexander Chemeris, Ming Jin, Randall Balestriero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series are central to modern data mining applications, from industrial telemetry and server metrics to finance and physiology, yet time-series self-supervised learning often depends on view and augmentation choices that encode domain-specific invariances. We study how an SSL recipe behaves when its method-specific configuration is reused unchanged after the pretraining signal family changes, framing this as a fixed-recipe stress test rather than a comparison against optimally tuned methods. We introduce Latent Euclidean Next-Embedding Prediction Architecture (LeNEPA), a no-augmentation next-latent-token objective with a causal backbone. LeNEPA replaces the stop-gradient/EMA stabilization used by vanilla NEPA with SIGReg-based isotropy regularization and computes the predictive loss in a lightweight projected space that is discarded for evaluation. We compare LeNEPA with an ECG-tuned JEPA recipe under a fixed-horizon frozen-probe protocol on PTB-XL and Diag, a synthetic diagnostic corpus generated with Aionoscope. Both methods are retrained independently on each dataset while keeping their method-specific recipes unchanged. In this protocol, the ECG-tuned JEPA recipe is strong in-domain on PTB-XL but weaker when reused unchanged on Diag, whereas LeNEPA preserves useful frozen-probe gains on both datasets. Learning curves suggest faster early representation acquisition: LeNEPA reaches 80% of its final AUROC/AUPRC gain after 2--5k updates, compared with 5--10k updates for the faster JEPA readout. As a separate external frozen-encoder check, a CauKer-pretrained LeNEPA variant reaches 77.65% mean UCR-128 Random-Forest accuracy in a single-seed, best-checkpoint run, within 1.16 points of Mantis and within 0.24 points of MOMENT (77.89%). Overall, the results support no-augmentation latent prediction as a useful candidate recipe for low-retuning time-series SSL.

---


### 186. [GaussianEmoTalker: Real-Time Emotional Talking Head Synthesis with Audio-Driven and Blendshape-Based 3D Gaussian Splatting](https://arxiv.org/abs/2607.00959)

**<font color=#1a73e8>作者：</font>** Haijie Yang, Zhenyu Zhang, Yixuan Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven talking head synthesis has achieved impressive progress in lip synchronization and visual quality, yet generating expressive emotional avatars with controllable intensity remains challenging, especially under real-time constraints. In this paper, we present GaussianEmoTalker, an audio-driven framework for real-time emotional talking head synthesis based on 3D Gaussian Splatting. Instead of directly predicting the final emotional avatar from speech, we formulate emotional animation as a neutral-to-emotional residual deformation problem. GaussianEmoTalker first constructs an identity-specific neutral talking space with GaussianBlendshapes, which provides high-fidelity Gaussian attributes and phoneme-synchronized neutral motion. It then predicts an emotion-conditioned residual deformation by combining mesh displacement cues, audio features, emotion categories, and intensity encodings. To fuse these heterogeneous signals, we introduce a spatial-audio-emotion attention module that estimates the offsets of Gaussian attributes for expressive and temporally stable rendering. Extensive experiments demonstrate that GaussianEmoTalker achieves competitive video quality, accurate lip synchronization, controllable emotional expression, and real-time rendering compared with recent emotional talking head methods. Our project page is available at this https URL

---


### 187. [Slope-Guided Mamba and Angular-Refined Transformer for Light Field Super-Resolution](https://arxiv.org/abs/2607.00965)

**<font color=#1a73e8>作者：</font>** Li Jin, Jian Huang, Junde Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Light Field Super-Resolution (LFSR) necessitates accurate modeling of spatial-angular correlations while preserving intrinsic 4D ray coherence. However, maintaining such high-dimensional consistency remains challenging, primarily due to two inherent limitations in prevailing modeling paradigms. First, spatial and angular dimensions are often modeled in a decoupled manner, restricting early cross-dimensional interaction and leading to geometric inconsistencies. Moreover, although continuous sequence modeling paradigms show promise in representing epipolar structures, their rigid scanning mechanisms fundamentally conflict with epipolar geometry, limiting geometry-aware feature aggregation. To address these challenges, we propose a hybrid light field super-resolution network, termed SMART, which integrates a Slope-Guided Mamba and an Angular-Refined Transformer to effectively overcome these limitations. Specifically, we introduce an angular-modulated spatial module to bridge the decoupling gap, incorporating angular priors to strengthen spatial-angular correlation modeling. To mitigate the scan-geometry mismatch, we propose a manifold-aligned trajectory module that enables geometry-consistent sequence modeling along epipolar structures. Experiments on five benchmarks demonstrate that SMART achieves state-of-the-art performance, surpassing previous methods by 0.42 dB (PSNR) with significantly reduced artifacts.

---


### 188. [Understanding How Humans Inject Knowledge into Machine Learning Workflows through Visual Analytics](https://arxiv.org/abs/2607.00969)

**<font color=#1a73e8>作者：</font>** Yiwen Xing, Philip Beaucamp, Joyraj Chakraborty 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual analytics (VA) plays an increasingly important role in supporting machine learning (ML) workflows. In the field of visualization, such approaches and techniques are referred to as VIS4ML. While ML models are mostly learned automatically, the corresponding ML workflows receive a variety of human inputs, such as data labelling, feature engineering, model architecture designing, hyper-parameter tuning, and so on. In this work, we surveyed over 200 VIS4ML papers to gain an understanding of how humans inject their knowledge into ML workflows through interactive visualization. We collected a corpus of VIS4ML papers from the IEEE VIS conferences in the past decade. We developed a coding scheme to facilitate the literature research from four perspectives: characteristics of ML, visualization, interaction, and actions. The analysis of the coded dataset allows us to observe different pathways that transfer human knowledge to ML workflows via interactive visualization. Building on the analysis, we explain the phenomena of VIS4ML using the conceptual model that views VA as model building and the information-theoretic cost-benefit analysis that reasons VA as for optimizing ML workflows. This work provides unequivocal evidence showing the merits of using VA in ML workflows. The full list of surveyed papers, along with all analysis results and figures, is available at this https URL.

---


### 189. [Svarna: An Open Corpus Workbench for Modern Greek](https://arxiv.org/abs/2607.00970)

**<font color=#1a73e8>作者：</font>** Stergios Chatzikyriakidis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces Svarna, a free, open-source, web-based corpus workbench for modern Greek. Svarna integrates five databases covering various registers, institutional, literary, dialectal, social media, and historical, to provide a total of more than 507 million words and around 29 million sentences. This platform addresses the chronic gaps in Greek language technology. Although various corpus resources exist, they are scattered across different platforms, and in many cases, institutional access is restricted or they are no longer available online. Svarna integrates these resources into a single interface that can be used without logging in, installation, or specialized training. This system provides a concordancer with KWIC marking capabilities, frequency analysis including register-by-register normalization, collocation extraction using mutual information, a dictionary of 93 Greek discourse markers providing distribution profiles, text-level analysis tools including n-grams, variants, and collocation networks, register comparison using log-ratio, regular expression search, and an optional LLM layer for pragmatic annotation and free research mode. This platform is built upon SQLite FTS5 full-text indexes provided via a FastAPI backend, deployed as Docker containers on Azure, and released under the MIT license. Source code, build scripts, and deployment configurations are publicly available on GitHub. Users can add their own corpora and deploy their own instances. This document describes the system design, corpus structure, and use cases demonstrating the various queries supported by the platform. Svarna serves as the first step in exploring available data and is expected to lay the foundation for more comprehensive research in the future.

---


### 190. [TRCGL-Net: A Long-Tailed Multi-Label Chest X-Ray Classification Framework with Generative Data Augmentation and Label Co-Occurrence Modeling](https://arxiv.org/abs/2607.00975)

**<font color=#1a73e8>作者：</font>** Tong Shao, Hongshun Ling, Li Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest X-ray multi-label classification is a core task in intelligent medical imaging diagnosis. However, real clinical data often exhibit extreme long-tailed distributions, leading to degraded performance on rare diseases in tail classes. This issue is not only driven by data scarcity but also by two intrinsic factors:1) attenuation of tail-class lesion representations under complex anatomical backgrounds, and 2) dominance of head classes in modeling label co-occurrence relationships. To address these challenges, we propose TRCGL-Net. First, a learnable text-guided conditional diffusion model is employed to generate high-quality tail-class chest X-ray image samples under disease semantic constraints, improving data diversity and realism of rare disease patterns while alleviating class imbalance and preserving pathology-consistent this http URL, a channel reweighting mechanism is introduced to perform feature recalibration by emphasizing disease-relevant feature channels, thereby improving feature discriminability under long-tailed distributions.A class-aware attention mechanism is further applied to generate class-specific attention maps, enabling the model to localize disease-relevant regions and focus on fine-grained lesion this http URL, a graph convolution network based on label co occurrence is introduced to establish an information propagation mechanism among categories. Experiments on the PadChest dataset show that the proposed method achieves a tail-class mAP of 0.4904, an overall mAP of 0.4408, and an mAUC of 0.8989, outperforming state-of-the-art methods. TRCGL-Net effectively improves recognition performance for rare diseases under long-tailed distributions and mitigates the impact of extreme class imbalance in chest X-ray multi-label classification.

---


### 191. [Privacy-Preserving Depth-Only Open-Vocabulary 3D Semantic Segmentation Via Uncertainty-Guided Test-Time Optimization](https://arxiv.org/abs/2607.00978)

**<font color=#1a73e8>作者：</font>** Xuying Huang, Sicong Pan, Maren Bennewitz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving perception is a critical requirement for deploying 3D scene understanding systems in real-world indoor environments, yet it remains underexplored in open-vocabulary 3D semantic segmentation. Existing methods typically rely on obtaining rich semantic cues from RGB images, which may expose privacy-sensitive visual information. Depth-only 3D geometry provides a privacy-preserving alternative, but the absence of appearance-based semantic cues makes open-vocabulary predictions highly uncertain and less reliable. Under this setting, we propose to convert uncertainty into a guidance signal to identify unreliable semantic responses and use semantic priors from foundation models to regularize their refinement. We present UTTO, an uncertainty-guided test-time optimization framework for depth-only open-vocabulary 3D semantic segmentation. Without additional training, experiments on ScanNet20, ScanNet40, and ScanNet200 demonstrate that UTTO consistently improves depth-only open-vocabulary 3D segmentation and outperforms representative baselines under privacy-preserving conditions.

---


### 192. [Visualizing Engineering Fundamentals: Design of Mixed Reality and Physical Toolkits for Effective Learning](https://arxiv.org/abs/2607.00979)

**<font color=#1a73e8>作者：</font>** Mohammad Abu Nasir Rakib, Sharmin Akter, Eshwara Prasad Sridhar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examined students' experiences with mixed-reality applications and physical toolkits in Engineering Mechanics to inform design guidelines for educational tools. In a user study with 24 participants, we compared classroom instruction alone, classroom instruction with a mixed-reality application, and classroom instruction with physical toolkits. Thematic analysis of participant feedback revealed that learners' workflows and engagement with fundamental mechanics problems varied across instructional modalities. Participants valued multimodal and interactive experiences that combined visualization with hands-on interaction, while reporting challenges with complex or unclear visualizations. These insights support the human-centered design of mixed-reality and physical tools for engineering education.

---


### 193. [QCA: Query- and Content-Aware Keyframe Selection for Long Video Understanding](https://arxiv.org/abs/2607.00983)

**<font color=#1a73e8>作者：</font>** Jun Peng, Baiyang Song, Jie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is often plagued by severe temporal redundancy, where processing dense frame sequences is both semantically inefficient and computationally expensive. This challenge is further amplified when only a small subset of frames is truly relevant to the given query. In this paper, we propose a Query- and Content-Aware (QCA) keyframe selection framework that can select a compact yet information-rich set of frames from long videos. QCA first partitions the video into temporal segments and estimates the information contribution of each segment by jointly modeling query relevance and content deviation, and dynamically allocates keyframe budget to each segment. Within each segment, QCA anchors on the most query-relevant frame and iteratively incorporates additional frames to maximize diversity while maintaining high semantic relevance to the query. Crucially, our method requires no additional training and can be seamlessly integrated into existing Video-LLMs. Extensive experiments across multiple long video understanding benchmarks demonstrate that our proposed approach achieves state-of-the-art performance and has strong generalization ability. For instance, QCA achieves 67.8\% on LongVideoBench using 128 frames, while GPT-4o achieves 66.7\% using 256 frames. Our codes are available in \href{this https URL}{GitHub}.

---


### 194. [Automatic Detection of Stress from Speech in the Trier Social Stress Test](https://arxiv.org/abs/2607.00986)

**<font color=#1a73e8>作者：</font>** Hanna Drimalla, Wieland R. Cremer, Christine Kraus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatically detecting stress in speech provides an unobtrusive way to gain insights relevant to behavioral research or clinical assessment. This study investigates the automatic differentiation between a stressful and non-stressful situation, and the prediction of physiological and affective stress responses. Speech data was collected from 50 participants who either completed the Trier Social Stress Test (TSST) or a non-stressful control condition. With a processing pipeline that included speaker diarization and machine learning models, we achieved stress detection performance significantly above a mean baseline. Moreover, relevant physiological and affective stress responses were partially predictable from acoustic-prosodic features. Feature-importance analyses identified the most informative predictors contributing to model performance. The findings demonstrate that speech can serve as a meaningful and unobtrusive indicator of multiple dimensions of the human stress response.

---


### 195. [AVSR-Diff: Scale-Agnostic Diffusion Priors for Temporally Consistent Arbitrary-Scale Video Super-Resolution](https://arxiv.org/abs/2607.00987)

**<font color=#1a73e8>作者：</font>** Geunhyuk Youk, Jeonghyeok Do, Dayeon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have significantly advanced video super-resolution (VSR) but remain largely constrained to fixed upsampling scales. Conversely, while coordinate-based arbitrary-scale VSR methods offer scale flexibility, they inherently suffer from severe over-smoothing at large scaling factors. Integrating generative priors with continuous decoding is promising but currently hindered by severe temporal flickering caused by the stochasticity of diffusion sampling. To address this, we propose AVSR-Diff (Arbitrary-scale Video Super-Resolution with Diffusion), a novel decoupled framework that separates scale-agnostic latent denoising from continuous coordinate rendering, effectively avoiding computationally heavy resolution-specific sampling. Our approach introduces a Temporally-Gated Feature Recurrence (TGFR) module to extract strictly aligned, temporally consistent latent priors. Furthermore, we design a continuous video VAE decoder incorporating a Scale-Aware Fourier Refinement (SAFR) module to dynamically adapt frequency components to any target scale. Extensive experiments demonstrate that AVSR-Diff consistently preserves high-frequency details and strong temporal stability across various scales, surpassing state-of-the-art arbitrary-scale baselines. Remarkably, our framework outperforms recent fixed-scale generative models even on their native resolution.

---


### 196. [KnowledgeDebugger -- an Exploration Tool for Knowledge Localization and Editing in Transformers](https://arxiv.org/abs/2607.01000)

**<font color=#1a73e8>作者：</font>** Eric Benz, Lennart Stöpler, Nikolai Bolik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent research has increasingly focused on understanding how Transformers store and process knowledge, as well as how this knowledge can be edited. Research work in this area is often conducted in two phases: first, phenomena are explored on individual samples. Then, when results appear promising, more statistically robust experiments follow. To support the first phase, we propose KnowledgeDebugger, a GUI-based exploration tool for knowledge localization and editing in Transformers. Our tool - inspired by LM-Debugger - offers no-code access to the methods in EasyEdit, a widely used library of state-of-the-art Knowledge Editing approaches. We demonstrate the tool's effectiveness through case studies of recent findings in this field.

---


### 197. [Logit-Contribution Scoring Identifies Non-Literal Retrieval Heads](https://arxiv.org/abs/2607.01002)

**<font color=#1a73e8>作者：</font>** Aryo Pradipta Gema, Beatrice Alex, Pasquale Minervini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In long-context use, large language models frequently synthesize answers from the meaning of a relevant context span rather than literally copy-pasting them. Identifying which attention heads perform this synthesis matters for interpreting long-context model behavior. Yet existing detectors miss these heads by construction: they reward heads whose attended token matches the generated token, a literal-copy criterion that captures where a head reads but not what it writes through its output-value (OV) circuit, the very mechanism that carries non-literal retrieval. We introduce Logit-Contribution Scoring (LOCOS), a write-aware detector that scores each head by the projection of its OV-circuit output onto the answer-token unembedding direction, contrasting needle and off-needle source positions in a single forward pass. Across three model families (Qwen3, Gemma-3, OLMo-3.1), mean-ablating the top LOCOS heads on the NoLiMa non-literal retrieval benchmark collapses ROUGE-L at lower head counts than prior attention-based detections; on Qwen3-8B, ablating 50 heads drives ROUGE-L from 0.401 to 0.000 while the strongest baseline still retains 0.292. The selected heads are retrieval-specific: parametric recall and arithmetic reasoning stay at baseline under the same ablation. On Qwen3-8B, the same ablation also drops MuSiQue from 0.55 to 0.08 and BABI-Long from 0.62 to 0.20, while a random-heads control stays within 0.05 of baseline.

---


### 198. [Generative Model Proposal based Particle Filtering for Data Assimilation](https://arxiv.org/abs/2607.01012)

**<font color=#1a73e8>作者：</font>** Chandni Nagda, Mayank Shrivastavam Gudrun Thorkelsdottir, Gan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data assimilation models state dynamics conditioned on sequential observations, and has wide-ranging scientific applications. In the filtering setting, the goal is to model the posterior over the current state given all observations so far. Classical solutions typically make simplifying distributional or functional assumptions, e.g., linear-Gaussian systems, which can be inaccurate in many scenarios. In principle, particle filters (PFs) remove these assumptions, yet often collapse in high dimensions. Recent generative approaches learn conditional state transitions, but without principled Bayesian updates they do not recover the correct filtering posterior and can accumulate error over long horizons. In this work, we introduce Flow Proposal Particle Filters (FPPF), which learn a conditional generative model based proposal approximating the variance-minimizing optimal proposal for particle propagation. Conditioning on observations steers particles toward high-likelihood regions before weighting, reducing weight variance and delaying degeneracy. Since our proposal admits tractable likelihood evaluation, FPPF computes accurate importance weights and retains a Bayesian update step. We further extend FPPF to high-dimensional problems through localization strategies, adressing another standard PF failure mode. Extensive experiments on a variety of dynamical systems show that FPPF outperforms statistical baselines and other generative methods in non-linear, non-Gaussian, and high-dimensional regimes.

---


### 199. [SuperFlex: Deformable Superquadrics for Point Cloud Decomposition](https://arxiv.org/abs/2607.01015)

**<font color=#1a73e8>作者：</font>** Gabriel Tavernini, Elisabetta Fedele, Tiago Novello 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Superquadrics have proven to provide a compact, geometrically meaningful representation for 3D objects. However, existing methods suffer from limited reconstruction accuracy, are restricted to rigid primitives, and lack robustness to partial point clouds. In this work, we present SuperFlex, an enhanced framework that expands the expressive power and applicability of superquadric decompositions. First, we introduce a novel loss formulation which significantly improves reconstruction accuracy. Second, we include bending and tapering deformations, enabling high-fidelity representation of curved and asymmetric geometries. Finally, we leverage these high-quality decompositions as supervision to train a model that is robust to partial real-world point clouds. Experiments demonstrate substantial improvements in reconstruction accuracy over both optimization- and learning-based baselines while maintaining a highly compact primitive representation.

---


### 200. [Reading Order Inference for Complex Document Layouts](https://arxiv.org/abs/2607.01018)

**<font color=#1a73e8>作者：</font>** Iddo Hakim, Sharva Gogawale, Omer Ventura 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reading order inference remains a critical bottleneck in the digitization of complex historical manuscripts, where pages contain multiple spatially interleaved reading streams, the canonical example being the Glossa Ordinaria layout, in which a central text is surrounded by commentaries that wrap around it in non-rectangular, non-convex regions. We present a training-free, graph-based framework: each OCR text line becomes a node in a directed candidate-transition graph, edges are scored by a weighted additive ensemble of two lightweight language-model signals (causal language model conditional likelihood and BERT next-sentence prediction, NSP; a third sentence-embedding signal was evaluated but did not improve reading order), and the global reading order is recovered as a degree-constrained directed path cover. To avoid the cascading "edge-theft" failures of greedy edge selection, we propose a max-regret inference rule that prioritizes commitments with high opportunity cost. We evaluate on synthetic Glossa Ordinaria grid layouts, on 23 ALTO page geometries (10 historical source pages plus mirrored and flipped variants), and on a 140-page multi-column English subset of OmniDocBench, comparing our method against the canonical recursive XY-cut (PaddleOCR PP-StructureV3) and two LayoutReader variants (layout-only and text+layout) on identical inputs. On wrap-around Glossa layouts our method recovers 95% of ground-truth successor edges on average vs. XY-cut's 50%; on the OmniDocBench multi-column subset it reaches 88% macro edge accuracy versus XY-cut's 75% and LayoutReader's 25%. The LayoutReader baselines transfer poorly due to a word-level vs. line-level granularity mismatch. We additionally verify mirror-invariance under horizontal and vertical page reflections: Our method changes by less than 1 percentage point, classical XY-cut by 2 points, and LayoutReader-T by up to 8 points.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
