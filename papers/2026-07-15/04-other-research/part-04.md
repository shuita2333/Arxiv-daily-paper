# 📦 其他研究 | 2026年07月15日

> 本类共 **420** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

---

### 151. [CAFE: A Compound-AI Factorial Evaluation Framework](https://arxiv.org/abs/2607.10380)

**<font color=#1a73e8>作者：</font>** Fabian Lukassen, Christoph Weisser, Thomas Kneib 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce CAFE (Compound-AI Factorial Evaluation), an open-source platform that brings design of experiments to the evaluation of compound AI systems (CAIS). Such systems expose many interchangeable choices - e.g. which retriever, model, or prompt - and practitioners rarely know which of them most affects answer quality. With CAFE, a practitioner registers each swappable component of a pipeline as a factor to build a factorial design over the chosen factors, run the resulting configurations, and score the answers on a shared rubric using a configurable LLM judge together with human raters. From these ratings it attributes answer-quality variance to the components and their interactions with mixed-effects models and reports effect sizes, significance, the best configuration, cost and latency trade-offs, and judge-human reliability. Whereas existing tools mostly either search for a good configuration or score outputs in isolation, CAFE also explains which component drives quality and whether an observed difference is significant. We validate CAFE on a retrieval-augmented question-answering (QA) pipeline over the HotpotQA benchmark dataset, where it recovers planted factor effects and stays calibrated under a permutation null. CAFE is released as a Python package and as a Web application.

---


### 152. [A Stepwise Questioning Expert-Editor Multi-Agent Framework for Long-Document Summarization](https://arxiv.org/abs/2607.10390)

**<font color=#1a73e8>作者：</font>** Lingyun Shen, Xuejia Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) have shown promising potential in news summarization tasks, their performance on long-document summarization remains challenging as their length often exceeds the input limits. As the agent investment, which provide possibility to improve the inherent capabilities of LLMs. To enhance the effectiveness of long-document summarization based on LLMs, this paper proposes an expert-editor stepwise questioning multi-agent method, in which the expert and the editor guide another agent to refine the summary by posing questions on different aspects of the content and providing targeted clues for revision. We conducted experiments on two representative long-document scientific datasets and evaluated the results through widely recognized automatic metrics. The results demonstrated the effectiveness of our method.

---


### 153. [Vertical Fusion: Condensing Internal Representations for Robust ViT Classification](https://arxiv.org/abs/2607.10391)

**<font color=#1a73e8>作者：</font>** Francesco Di Salvo, Shyam Nandan Rai, Hamed Damirchi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite exposing rich intermediate representations, Vision Transformers (ViTs) are almost exclusively utilized as black-box feature extractors, where only the last layer is considered for downstream tasks. We challenge this convention by introducing the notion of recoverability: the capacity of intermediate representations to correct last-layer failures. By evaluating independent classification probes at every model depth across 16 datasets, we observe that intermediate probes correctly classify 18% to 76% of samples that the last-layer probe misclassifies. We show that these gains are not primarily driven by predictive diversity, but by a redundancy-correctness correspondence, where the internal hierarchy acts as a series of stable, redundant probes of a shared discriminative signal. While established horizontal ensemble strategies (i.e., across multiple models) can improve performance, they incur high computational cost and ignore this vertical signal within a single model. To bridge this gap, we propose VFusion, a principled vertical aggregation strategy employing a learnable mapping into a low-dimensional latent space that synthesizes features across the internal ViT hierarchy. VFusion substantially outperforms established aggregation baselines in both in-distribution and out-of-distribution settings, notably closing 45% of the accuracy gap between the best individual layer and a theoretical oracle performance. Our gains consistently generalize across model sizes and pre-training regimes, confirming that VFusion offers a robust and efficient alternative to horizontal ensemble methods. The code is available at this https URL.

---


### 154. [Self-supervised Automatic Matting](https://arxiv.org/abs/2607.10395)

**<font color=#1a73e8>作者：</font>** Xiaonan Hu, Zhiyuan Lu, Jingdong Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality alpha mattes are notoriously expensive to annotate, creating a fundamental data bottleneck for deep image matting. While prior work attempts to reduce annotation cost using coarser labels like trimaps or masks, they remain reliant on costly per-pixel supervision, limiting scalability and generalization. In this work, we push the boundary further and ask: can we train an automatic matting model using only RGB images, with no manual annotation at all? We answer this by presenting SSMatte, a self-supervised framework that for the first time achieves performance on par with fully-supervised automatic matting. Our key insight is to decompose the problem into semantic anchoring and detail matting. SSMatte first generates a semantic matting prompt from frozen self-supervised ViT features by propagating class-token seeds via a novel, training-efficient semantic anchoring loss based on a generalized Rayleigh quotient. This prompt then anchors a detail matting network, which is optimized via a fixed-point-based loss that enforces alpha-RGB consistency. Extensive experiments show SSMatte outperforms prior weakly-supervised methods, matches the performance of fully-supervised models on portrait benchmarks, and demonstrates favorable scaling and generalization behaviors with additional data. Our work pushes automatic matting to an fresh, fully annotation-free paradigm. Code will be available.

---


### 155. [SynthDocBench: Controlled Benchmark for Long-Context Visual Document Understanding](https://arxiv.org/abs/2607.10400)

**<font color=#1a73e8>作者：</font>** Abhigya Verma, Khyati Mahajan, Amit Kumar Saha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) have achieved strong performance on visual document understanding benchmarks such as DocVQA, ChartQA, and MMLongBench-Doc. However, real-world documents combine multiple factors such as length, layout complexity, modality, and question difficulty, which makes it difficult to attribute model failures to specific causes. We introduce SynthDocBench, a fully synthetic benchmark for long-context visual document understanding that systematically controls factors including document length, layout structure, modality composition, and question type. The benchmark is constructed using a combinatorial design, each factor is varied independently across generated documents, enabling controlled analysis of model behavior. Documents are generated end to end using an LLM pipeline across six layout archetypes, with a 40 percent random override to prevent models from exploiting spurious correlations. Additionally, SynthDocBench spans long-context documents with substantially greater length and structural diversity than existing benchmarks. Evaluating seven frontier VLMs, we uncover three failure modes that existing benchmarks cannot surface: sharp degradation with document length, a systematic positional sensitivity in which the middle third of a document is hardest for five of six models and five of six models show a negative Early-to-Late trend (steepest decline: 8.3 percentage points), and breakdown of chart comprehension in long-document settings. These results suggest that current models may be overfitting to benchmark artifacts rather than achieving robust long-context visual document understanding.

---


### 156. [Spatula: Exploring On-Demand In-Situ Interfaces and Interaction for Attribute Control](https://arxiv.org/abs/2607.10405)

**<font color=#1a73e8>作者：</font>** Boyu Li, Linjie Qiu, Lin-Ping Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Controlling attributes is a critical step toward achieving the final creative outcome, yet current approaches fall short in supporting users in the iterative refinement of generative content. We propose Spatula, a proof-of-concept system that generates on-demand, in-situ attribute control interfaces and interactions for creating motion graphics. Building on a technical probe that automatically analyzes animation context and generates corresponding attributes and UI, we frame attribute control as an explorable landscape and explore the attribute control space along four key dimensions: Discoverability, Resolution, Scope, and Expandability. Findings from a user study (N=12) show that our system provides intuitive and convenient interactions while supporting diverse needs for fine-grained parameter control. Furthermore, our applications demonstrate that the plug-and-play design generalizes to other domains, such as web design and 3D modeling.

---


### 157. [TVT-PAPD: Pathology-Aware Prototype Distillation for Self-Supervised Whole Slide Image Classification](https://arxiv.org/abs/2607.10406)

**<font color=#1a73e8>作者：</font>** Ramesh Naidu Laveti, Jaya Sreevalsan-Nair, T K Srikanth  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) has emerged as an effective paradigm for learning transferable representations from large-scale unlabeled whole slide images (WSIs). However, existing SSL methods primarily learn generic visual features and often fail to explicitly capture pathology-specific morphological patterns that are critical for disease characterization. To address this limitation, we propose Tiny Vision Transformer with Pathology-Aware Prototype Distillation (TVT-PAPD). This self-supervised pathology representation learning framework integrates a Tiny Vision Transformer (TVT) with a novel Pathology-Aware Prototype Distillation (PAPD) module. PAPD employs a learnable pathology prototype bank to discover and preserve representative tissue morphology patterns, encouraging semantically similar pathological regions to learn consistent and discriminative representations. The proposed framework enhances pathology-aware feature learning while maintaining computational efficiency with 90M parameters. Experiments on the Cancer Genome Atlas (TCGA) low-grade glioma (LGG)/glioblastoma (GBM) dataset and the Indian Pathology Brain (IPD-Brain) dataset demonstrate that TVT-PAPD achieves weighted F1-scores of 93.02% and 90.23%, respectively, for LGG-GBM classification, while exhibiting strong cross-cohort generalization across independent glioma datasets.

---


### 158. [GNOCHI: Generative Neural mOdel for Close Human-Human Interactions](https://arxiv.org/abs/2607.10408)

**<font color=#1a73e8>作者：</font>** Gonzalo Gómez-Nogales, Marc Comino-Trinidad, Andrés Casado-Elvira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creating realistic 3D human-human interactions in virtual environments is challenging due to the high degrees of freedom in the human body and the need for physically accurate poses that do not collide with each other. Traditional methods for human-human interaction are based on motion tracking or 3D body reconstruction, but lack generative capabilities. Recent generative methods enable the synthesis of individual or interacting motions via text or image input, but generally fall short in modeling close interactions. This paper introduces a novel generative model for close 3D human-human interactions using a conditional variational autoencoder (cVAE), which generates poses for one human conditioned on the pose of another, allowing for controlled and diverse interaction synthesis. To train our model, we address two underlying long-standing challenges in the field of human-human interaction: data scarcity, for which we propose an automated supervised data augmentation strategy that generates synthetic yet realistic interaction poses; and collision awareness in generative approaches, for which we propose a self-supervised loss based on a collision resolution technique using volumetric proxies to ensure physically correct interactions. We extensively evaluate the capabilities of our model, and demonstrate a wide variety of plausible and physically correct interactions, not possible to generate with current state-of-the-art methods.

---


### 159. [Machine Learning-based Correlation of Charpy Impact Properties Between Sub-sized and Standard-sized Specimens for Nuclear Structural Materials](https://arxiv.org/abs/2607.10412)

**<font color=#1a73e8>作者：</font>** Yugandhar Kasala Sreenivasulu, Isshu Lee, John W. Merickel 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable correlations of Charpy impact test results between sub-sized and full-sized specimens are essential for structural integrity assessments, particularly in nuclear applications, where spatial constraints and limited material volume restrict specimen size. Although standards such as ASTM A370 and BS 7910 provide guidance on conversion methodologies, and numerous analytical correlation methods have been proposed in prior studies, these approaches generally have limited accuracy and their applicability is often constrained to specific materials, treatment conditions, and specimen geometries. In this study, a Machine Learning (ML)-based framework is proposed for correlating Charpy impact properties across specimen sizes. The proposed approach maps absorbed energy values across the full ductile-to-brittle transition region by applying a temperature shift combined with scaled residual projection, to align sub-sized test data with full-sized response. From the resulting temperature-energy profiles, the correlated values for upper shelf energy (USE) and ductile-to-brittle transition temperature (DBTT) are extracted by fitting data with a hyperbolic tangent model. The framework is validated using a dataset comprising 389 matched sub-sized and full-sized Charpy impact tests on SA533B steel. This ML-based approach demonstrates an improved correlation performance relative to conventional analytical methods, achieving R2 values of 0.942 for USE and 0.892 for DBTT. The trained ML models do not require access to full-sized Charpy data during inference, making this approach suitable for material surveillance programs, accelerated irradiation testing, and other applications involving small-size Charpy impact testing.

---


### 160. [SPORT: Structure-Aware Prototype Disentanglement for Incomplete Multi-View Clustering](https://arxiv.org/abs/2607.10413)

**<font color=#1a73e8>作者：</font>** Yaoyuan Guo, Zhibin Gu, Songhe Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototype-based Incomplete Multi-view Clustering has recently attracted increasing attention by exploiting prototypes as semantic anchors for missing-view imputation. However, existing approaches are still limited in three aspects. First, they typically focus on enforcing cross-view prototype consistency, while ignoring view-specific information embedded in prototypes, thus limiting multi-view expressiveness. Second, most methods rely on instance-level contrastive learning that only aligns paired samples across views, failing to preserve cluster-level relational structures. Third, missing-view imputation is usually performed using global prototypes alone, without considering local geometric neighborhood structures, leading to inaccurate recovery of missing representations. To address these limitations, we propose a novel framework termed Structure-aware PrOtotype disentanglement foR incomplete multi-view clusTering (SPORT), which explicitly disentangles shared and view-specific components of prototypes while preserving cluster-level relational structures. Specifically, we decouple prototypes into orthogonal shared and view-specific components, aligning only shared components to capture consensus semantics while de-correlating view-specific components to preserve complementary information. Meanwhile, a structure-aware contrastive learning mechanism is incorporated to explicitly model cluster-level relationships during cross-view representation learning. Furthermore, a hybrid imputation strategy integrates global prototype matching with local neighborhood matching, enabling joint exploitation of semantic prototypes and manifold structures for missing-view recovery. Extensive experiments on six benchmark datasets show that SPORT achieves superior performance over state-of-the-art methods under various missing rates.

---


### 161. [BOCCHI: A More Realistic and Challenging Benchmark for Local Motion Blur Detection with MSDCT-UNet](https://arxiv.org/abs/2607.10427)

**<font color=#1a73e8>作者：</font>** Kuan-Lin Chen, Yuan-Kang Lee, Cheng-Yuan Chiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Local motion blur detection requires pixel-level localization of blurred regions. Existing benchmarks let models rely on gradient shortcuts that fail to transfer. We introduce BOCCHI (Blurred Objects Captured across Cameras with Human-annotated Imagery), a real-captured benchmark whose sharp regions overlap the blur gradient distribution and defeat these shortcuts, and propose MSDCT-UNet (Multi-Scale Discrete Cosine Transform UNet), a frequency-aware encoder-decoder injecting multi-scale DCT priors through DCT Attention and FiLM. MSDCT-UNet ranks first in in-domain mIoU and boundary localization on BOCCHI, and BOCCHI-trained models outperform every other training source on cross-dataset transfer with only 633 training images.

---


### 162. [Context by Distinct Information: An Auditable Dirichlet-Process Working Memory for Long, Redundant Context Streams](https://arxiv.org/abs/2607.10441)

**<font color=#1a73e8>作者：</font>** Siddharth Pal, Viktoria Rojkova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Context engineering decides what information a model carries forward, and current designs meter it in tokens: compressing the past into a bounded recurrent state, keeping a key-value entry for every token, or imposing a fixed budget through a window or eviction rule. All three make the token the unit of memory even when the stream is redundant and the task depends on the distinct information it carries. Building on a companion mechanism paper that opens a cache slot only when an incoming key is novel, so memory scales with the number of distinct items rather than tokens, we develop that allocate-on-novelty cache as a working-memory component and organize context by how a task depends on the past: recall-carried information belongs in a content-addressed novelty cache, summary-carried information in a recurrent state, and locality-carried information in a recency window. The claim is empirical and bounded. On a matched character-level control, novelty-gated attention reaches full-attention performance while attending to about half the tokens, and coupling the cache with a state-space summary matches full-attention coupling at that reduced cost; the advantage grows as context lengthens, while a sliding window is preferable on short, locality-dominated spans. On next-code prediction over synthetic Medicare claims the coupled component leads full attention and every fixed-budget eviction policy at a thousand-event horizon, whereas cost forecasting over the same stream is summary-carried and the cache is neutral. The retained memory is an inspectable table of templates, codes, drugs, or places rather than an opaque state. The experiments are small-scale and use only public data; they establish the primitive that context can scale with distinct information rather than tokens, in a working memory that is content-addressable and auditable.

---


### 163. [Threat Vectors and the State of the Art in Defense Methods for Security in Neurotechnology](https://arxiv.org/abs/2607.10451)

**<font color=#1a73e8>作者：</font>** Bryce-Allen Bagley, Nathaniel Rose, Quintus Kilbourn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Brain-computer interfaces (BCIs) are a class of diverse hardware modalities, associated software, and connected devices which are widely used in a variety of fields, including neurosurgery, biomedical data analysis, and neuroimaging. Recent years have seen rapid advancements in BCI technology, and neurotechnology more broadly, with the first devices now passing clinical trials, early examples of consumer hardware entering the market, and many variants of consumer and medical hardware with increasingly extensive capabilities being developed rapidly. However, research and development in security for BCIs--known as neurosecurity--lags significantly behind the capabilities of BCIs themselves. In an effort to address as many vulnerabilities as feasible immediately, in this paper we review the current state of the art in neurosecurity, thoroughly survey the breadth and complexity of both firmly established and highly probable security threats to BCI systems, and provide recommendations of existing methods from cybersecurity, hardware security, and machine learning which can immediately be applied to address some of these gaps in neurosecurity.

---


### 164. [Annotation-Free Furniture Codes: What They Encode, and How Far They Transfer](https://arxiv.org/abs/2607.10461)

**<font color=#1a73e8>作者：</font>** Benjamin Friedman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Layout-based 3D scene synthesizers place each object using two human-annotated channels: a categorical class label and a canonical-pose convention. We ask whether a single self-supervised token derived from object geometry can replace both, and study such tokens directly as a representation, decoupled from any synthesizer. A Finite Scalar Quantization (FSQ) point-cloud autoencoder is chamfer-trained on placed 3D-FUTURE furniture with no labels or pose annotations. Diagnostic probes recover fine-category (62.6 +/- 0.5%), super-category (85.6 +/- 1.3%), and yaw (52.7 +/- 0.5 deg) from the codes alone. Swapping the chamfer target from the rotated to the un-rotated point cloud collapses the yaw signal while raising class recovery, showing the codes' rotation content can be set by the training objective. Scaling across asset libraries needs codes that transfer; on an unseen dataset (ShapeNet), alignment is category-dependent: box-like furniture transfers, organically-shaped furniture does not, and a target-blind augmentation partly closes the gap.

---


### 165. [Not All Color Categories Are Equally Stable: A Multilingual Free Color Naming Experiment](https://arxiv.org/abs/2607.10465)

**<font color=#1a73e8>作者：</font>** Nuray Toganas, Adilet Yerkin, Elnara Kadyrgali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color naming is an important part of human color perception. Its task is to allow people to describe continuous colors using discrete color categories. However, the boundaries between color categories are often unclear, and some colors may be perceived differently depending on their saturation and brightness. While certain color categories remain recognizable across a wide range of shades, others may be associated with different color names when their appearance changes. This study investigates the consistency of color naming for red, yellow, and green color categories using a free color-naming experiment. A set of 18 color samples was selected from the COLIBRI dataset to represent different shades of these colors. Participants (n = 92) were asked to freely assign color names to each sample in Kazakh, Russian, or English without being limited to predefined categories. The results show that color categories differ in their consistency. Green shades were consistently identified as green despite variations in appearance, whereas yellow shades received a wider variety of names, including gold- and brown-related descriptions. Red shades showed moderate naming consistency. Our findings suggest that some color categories occupy broader perceptual regions than others and may therefore be more robust to visual variations. The study results can be used to develop perceptually meaningful color models and color naming systems.

---


### 166. [Pitfalls of Administrative Censoring in Survival Models with Time-Indexed Inputs](https://arxiv.org/abs/2607.10466)

**<font color=#1a73e8>作者：</font>** Yanqi Xu, Hui Dai, Carlos Fernandez-Granda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Survival models can model time-to-event outcomes using partially observed data. They are widely used in clinical prediction, including cancer risk, disease progression, treatment response, and mortality. Recent models often rely on rich inputs collected at a specific clinical encounter, such as medical images, laboratory tests, electronic health record snapshots, or sensor measurements. In large retrospective datasets, these inputs are usually collected over many calendar years. As a result, they may contain clues about when they were acquired through changes in devices, protocols, documentation, patient mix, or clinical practice. This creates a potential failure mode when outcomes are observed only up to a fixed study end date. More recent records necessarily have less potential follow-up than older records. A model that can infer the record date from the input may therefore learn to predict how much follow-up was available rather than the patient's true risk of experiencing the event. We call this failure mode administrative-cutoff leakage. In this paper, we characterize when this leakage can occur, distinguish it from classical informative censoring and genuine temporal changes in risk, and propose practical ways to detect it. In simulations, we show that administrative-cutoff leakage can inflate fixed-horizon AUC and can also affect Harrell's C-index under realistic follow-up patterns. We then demonstrate the same behavior in a real mammography cohort. These results motivate a simple design principle for survival prediction: for an n-year prediction task, the dataset should provide at least n years of potential follow-up after the latest input date. Otherwise, the models may be subject to bias induced by administrative-cutoff leakage.

---


### 167. [On the Real-World Generalisability of Optical Flow Models](https://arxiv.org/abs/2607.10470)

**<font color=#1a73e8>作者：</font>** Petter Reijalt, Sander Gielisse, Rickard Karlsson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of vision models to broadly benefit society is arguably a main research objective. In optical flow, however, the difficulty to obtain the ground truth has focused research mainly on synthetic data and domain-specific benchmarks. Here, we investigate the severity of this mismatch. We study how well modern optical flow estimation models generalise to real-world video and question if accuracy on synthetic benchmark proxies actually predicts accuracy on real-world optical flow. To address this, we build a real-world evaluation benchmark and evaluate the real-world generalisability of a broad set of recent optical flow models using standard checkpoints. Our benchmark contains 8,204 frame pairs across TAP-Flow, Slow Flow, and our own dataset FlowFactor. FlowFactor is a manually annotated real-world benchmark of 1,000 HD frame pairs organised into four confounding factors: large displacements, repetitive textures, occlusions, and lighting variation. Each setting mainly varies only one factor, enabling diagnostic, confounder-specific analysis. Using FlowFactor, we reveal that performance on varying lighting and large displacements correlates most strongly with real-world accuracy, and that improvements on large-motion regimes can trade off against robustness in small-motion, stationary scenes. Our experiments show that progress on Sintel, KITTI and Spring only weakly predicts accuracy on real-world data, highlighting the need for a broad real-world optical flow benchmark. Interestingly, scaling up the amount of training data does not necessarily resolve the gap, calling for new innovative research instead of simply scaling data and compute.

---


### 168. [When Reasoning Hurts Legal Drafting: The Verbalization Bottleneck in Patent Claim Generation](https://arxiv.org/abs/2607.10480)

**<font color=#1a73e8>作者：</font>** Lekang Jiang, Wenjun Sun, Stephan Goetz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patent claim drafting is a challenging legal drafting task that requires technical expertise, precise linguistic control, strict adherence to formal conventions, and the preservation of complex logical relationships among claim elements. While Chain-of-Thought (CoT) prompting has been widely used to improve the reasoning capabilities of large language models (LLMs), recent evidence suggests that its benefits may be limited, or even negative, in highly structured or pattern-sensitive tasks. Therefore, this paper investigates whether CoT prompting benefits patent claim generation. We propose a task-specific CoT method for patent claim generation and evaluate its effectiveness through both automatic metrics and human expert assessment. Our results show that reasoning-enhanced prompting can improve claim quality. Moreover, we demonstrate a counter-intuitive but important empirical finding: implicit CoT, where reasoning is kept internal rather than explicitly verbalized, consistently outperforms explicit CoT. Through systematic analysis, we show that explicit CoT can introduce an unnecessary information bottleneck for claim generation. Verbalized reasoning may compromise the quality of final outputs through three specific mechanisms: abstraction of critical details, disruption of internalized generation patterns, and cascading error propagation. Our findings provide new insights into legal tasks and CoT applications.

---


### 169. [Firewall3D: A Hardware Firewall for Defending 3D Printers Against Firmware Attacks](https://arxiv.org/abs/2607.10484)

**<font color=#1a73e8>作者：</font>** Seyed Ali Ghazi Asgar, Narasimha Reddy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the 3D printing market continues to grow rapidly, with an estimated value exceeding $30 billion, cybersecurity risks and attacks targeting additive manufacturing systems are also increasing. These attacks aim to sabotage printed components, steal intellectual property, or even physically damage the 3D printer itself. One major cybersecurity threat in this domain is firmware level attacks, which can be introduced through supply chain compromises, malicious firmware updates, or insider threats that deploy modified firmware to manipulate printer behavior. To defend against such threats, we propose a dedicated hardware based security solution,Firewall3D, that acts as a hardware firewall for 3D printers. Firewall3D continuously monitors physical layer signals, including stepper motor currents, end stop switches, nozzle and bed temperatures and cooling fans, to verify that the printer's physical behavior matches the intended G-code execution. Our experimental results demonstrate that Firewall3D can effectively detect a wide range of firmware attacks that could compromise print integrity, damage printer components, or leak intellectual property. Upon detecting abnormal behavior, the system can immediately trigger an alarm and halt the printing process, thereby preventing further damage and risks.

---


### 170. [Grassmannian Splatting I: Moving rank-2 Spacetime Surfels for Dynamic Scene Rendering](https://arxiv.org/abs/2607.10489)

**<font color=#1a73e8>作者：</font>** Aaron Maurice Berman, Shantanu Dave  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Grassmannian splatting, a dynamic scene representation whose primitives are Gaussians supported on 3-planes in spacetime $\R^4$: generically, spatial 2-planes in uniform translation along their normals. Each primitive carries a unit normal $n \in \mathbb S^3/\{\pm 1\} \cong \mathrm{Gr}(3,4)$ and an unconstrained factor $L \in \mathbb R^{4 \times 3}$, with covariance \[
\Sigma_{4\mathrm{D}} = (P_n L)(P_n L)^T, \qquad P_n = I - n n^T. \] For generic $L$ and $n \neq \pm e_0$, conditioning on time returns a rank-2 surfel at every frame. The normal of the disk and its velocity along that normal are read off from $n$; the disk shape and the tangential drift of its center are set by $L$. Existing native 4D Gaussian splatting methods [\it{Yang et. al. 2023,Duan et. al. 2024}] slice full-rank spacetime covariances, so their per-frame primitive is a volumetric ellipsoid; since conditioning lowers rank by exactly one, a rank-2 surfel in the slice requires a rank-3 spacetime covariance, and the parameterization above realizes exactly these. The motion model is closed form, i.e. no deformation field is learned, and no custom CUDA is required: the conditioned disk feeds a standard 3DGS rasterizer through its precomputed-covariance interface. A soft clamp in the Schur denominator regularizes the static orientation and continuously bridges rank-3 static and rank-2 dynamic behavior, so static and moving primitives form a single continuous family. On the 17 HyperNeRF scenes of MonoDyGauBench, training is fastest among all compared methods (4.9 to 5.6 times faster than the strongest quality baselines), while ranking second in PSNR, MS-SSIM, and LPIPS. Code: this https URL

---


### 171. [NanoVSR: Towards Real-Time Video Super-Resolution on Edge Devices](https://arxiv.org/abs/2607.10495)

**<font color=#1a73e8>作者：</font>** Filip Pawlicki, Marcel Kańduła, Marcin Pucek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Video Super-Resolution (VSR) methods rely heavily on transformers and explicit optical flow, creating computational overhead and custom operations that hinder deployment on hardware accelerators like TensorRT. To address this, we introduce NanoVSR, a scalable, fully convolutional architecture designed for resource-constrained edge devices. Using structural reparameterization, NanoVSR collapses into standard convolutions during inference, ensuring seamless hardware compatibility and negligible runtime overhead. Furthermore, despite lacking explicit motion compensation, it maintains competitive restoration quality by implicitly learning spatio-temporal alignments through progressive training. Evaluated on the REDS4 benchmark, NanoVSR demonstrates an exceptional balance between accuracy and computational efficiency, significantly improving the trade-off for compact architectures. Our NanoVSR-644k baseline yields 28.64 dB PSNR while delivering 27.2 FPS on the NVIDIA Jetson Orin NX 16GB (25W), offering massive speed gains over heavier models. The scaled NanoVSR-1.7M variant reaches 29.15 dB with a throughput of 19.58 FPS, providing superior, edge-optimized upscaling. Code is available at this https URL.

---


### 172. [Learning from Noise: Effective-Rank Collapse and Out-of-Distribution Rejection in Restricted Boltzmann Machines](https://arxiv.org/abs/2607.10506)

**<font color=#1a73e8>作者：</font>** Oshada Rathnayake, Nikhil Shukla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Restricted Boltzmann machines (RBMs) represent data by shaping an energy landscape over visible and hidden configurations, but their discriminative use is fragile under out-of-distribution (OOD) inputs: samples outside the training distribution can be absorbed into one of the learned class basins rather than rejected. Here, we analyze this failure mode through the spectrum of the induced visible--visible interaction $J=WW^{T}$, where \(W\) is the visible--hidden weight matrix. Relative to a Marchenko--Pastur random-matrix reference, conventional training spreads spectral weight into many weak, bulk-compatible directions, increasing the effective rank of $J$. When auxiliary random binary images are assigned to a rejection label during training, the learned interaction undergoes effective-rank collapse: weak bulk-like modes are depleted, spectral weight concentrates into fewer dominant eigendirections, and the effective rank of $J$ approaches that of the empirical data covariance matrix. The resulting RBM rejects structured OOD image datasets while preserving MNIST classification accuracy, showing that random auxiliary exposure can reshape both the interaction spectrum and the free-energy landscape of an energy-based classifier.

---


### 173. [How Data Narratives Go Wrong: A Taxonomy of Issues Across the Data Communication Process](https://arxiv.org/abs/2607.10523)

**<font color=#1a73e8>作者：</font>** Yu Fu, Jiawei Zhou, Sichen Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data narratives increasingly shape public understanding, but their failures are rarely just isolated factual errors or deceptive charts. Instead, they emerge through a broader meaning-making process in which quantitative evidence is transformed into claims, representations, and arguments. While prior work has examined these failures across disparate fields (e.g., statistics, visualization, and fact-checking), the community lacks a holistic lens to explain how these issues arise, propagate, and compound. To address this gap, we introduce TIC, a Taxonomy of Issues in Data Communication, synthesized from prior literature and refined through the qualitative annotation of 700 real-world data narratives from fact-checking sites, research datasets, and controversial media. TIC organizes recurring breakdowns across six dimensions-data, analysis, visual encoding, text, reasoning, and interpretation-and situates them within a framework spanning analysis, narrative construction, and audience reception. Alongside the taxonomy and process framework, we contribute a qualitatively annotated case corpus with coding justifications and an interactive browsing interface. Collectively, these contributions provide a structured lens for diagnosing problematic data narratives and informing future sociotechnical support for trustworthy data communication.

---


### 174. [Agents Don't Just Agree, They Remember: Benchmarking Persistent Sycophancy in Stateful Personal Agents](https://arxiv.org/abs/2607.10526)

**<font color=#1a73e8>作者：</font>** Xutao Mao, Liangjie Zhao, Leyao Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Stateful personal agents increasingly maintain long-term user profiles, episodic memories, and reusable skills. This persistence turns conversational sycophancy into a state-writing failure: accepted user-centric claims can be committed as lasting preferences, background facts, or workflows and later reused after the original conversation is gone. We call this persistent sycophancy and introduce the Personal Agent Sycophancy Benchmark (PASB), a 1,600-task benchmark that traces whether a conversational claim is accepted, written into durable agent state, and reused in a later neutral query. Unlike prior benchmarks that provide pre-written memories, PASB evaluates real agents (Hermes-Agent and OpenClaw) that decide what to store. It isolates the write process by combining four scenario framings with four temporal delivery patterns and separating a five-turn persist stage from a cleared three-turn query stage, ensuring downstream effects arise only from durable state. Across twelve models, the commit boundary is the key inflection point: downstream failure increases from 45.0% in session-only episodes to 71.9% after commitment, a consistent increase of 27.0 percentage points. Committed claims exhibit three write-time patterns: status promotion, attribution removal, and scope broadening. These patterns become stronger under memory-like or procedural framing, repeated reinforcement, and even across domain boundaries. These results show that agent sycophancy is fundamentally a state-writing governance problem. Once user content is committed to durable memory, safety must govern what agents write, not only what they say. PASB identifies the write-time controls needed to gate risky commits while preserving the source, role, and scope of stored content beyond response-level mitigations.

---


### 175. [Motif: Discovering and Automating Personal Web Workflows](https://arxiv.org/abs/2607.10531)

**<font color=#1a73e8>作者：</font>** Shaokang Jiang, Daye Nam  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLMs and existing work on programming by demonstration have made it possible for end users to create automations by explicitly demonstrating their behavior to LLMs. However, these approaches rely on the assumption that users know what to automate and what is capable of being automated. Additionally, automation via LLM agents is often expensive compared with programs. We introduce Motif, a system that passively observes everyday browser activity to discover recurring interaction patterns that are programmable, makes recommendations to users whenever a pattern is discovered and generate a program to install after user confirmation. Users can review, and refine the program using natural language. We evaluated Motif in a multi-day study, comparing its ambient discoveries against automations users attempted to build via ``vibe coding.'' With eight participants, Motif discovered more automatable patterns than users recognized. Most of them matched participants' routines and were useful. Follow-up surveys showed most would continue using Motif-generated programs.

---


### 176. [Improving Sample Diversity in Autoregressive Text-to-Image Generation via Cluster Truncation](https://arxiv.org/abs/2607.10535)

**<font color=#1a73e8>作者：</font>** Trang Nguyen, Shuang Wu, Runyan Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion models achieve state-of-the-art image quality for text-to-image (T2I) generation, recent work has demonstrated that they suffer from sample diversity collapse. In this work, we investigate whether autoregressive (AR) image generation models can push the Pareto frontier between image quality and sample diversity. With recent advances in quality and efficiency, AR models have emerged as a viable alternative to diffusion-based image generation. Beyond enabling new use cases such as interleaved image-text generation, their sequential generation process makes them compatible with a wide range of token-based decoding strategies originally developed to improve diversity in text generation. Motivated by the potential of a better diversity-quality tradeoff in the AR paradigm, we present the first systematic study of sample diversity in AR image generation models. We show that two key properties of AR image generation, persistently high token-level entropy and substantial redundancy in visual token spaces, limit the effectiveness of existing token-level decoding methods for diversity enhancement. We therefore propose $p$-less cluster, a new decoding strategy that performs entropy-based truncation sampling at cluster level rather than at token level. We evaluate our approach and baseline decoding methods across four autoregressive T2I models and two datasets using a comprehensive suite of metrics spanning image quality, prompt alignment, and diversity. Our results show that $p$-less cluster unlocks the greatest diversity across most evaluated autoregressive T2I models and datasets while maintaining image quality and prompt alignment.

---


### 177. [Navigating the Open-Source Model Ecosystem: An Empirical Study of Creator Practices in Artistic Image Generation](https://arxiv.org/abs/2607.10538)

**<font color=#1a73e8>作者：</font>** Yiluo Wei, Yupeng He, Qiming Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The open-sourcing of powerful image generation models has created a vibrant ecosystem where creators curate and combine a vast array of community-contributed models. This practice stands in sharp contrast to using closed-source tools like Midjourney. Yet, little is known about these emerging creative workflows. To bridge this gap, this paper presents the first large-scale empirical study of creator model usage behavior within this open-source image generation ecosystem. We construct a novel dataset of 6 million images with their embedded generation metadata -- a detailed recipe of the creation process, including the models used and the prompts. By linking the usage of 22.4K base models and 154K LoRA models to the images, our findings underscore the ecosystem's unique strengths and its inherent obstacles. This provides valuable insights for making this ecosystem more sustainable and innovative. Moreover, we make our dataset publicly available, providing creators with practical references for producing better artworks and researchers to facilitate further studies.

---


### 178. [AI YOU Town: Make Friends and Money with Your Digital Twin](https://arxiv.org/abs/2607.10539)

**<font color=#1a73e8>作者：</font>** Yan Lin, Yuyang Dai, Jiahui Geng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing approaches to infer user traits and generate responses consistent with a persona rely on static prompting. They lack calibrated uncertainty, ignore sequential evidence, and drift during long interactions. We present \textbf{AI YOU}, a framework that continually updates a personality profile with 22 dimensions from conversation and embodies it in a personal digital twin. Practically, the system combines prompting, Bayesian updating, and conformal prediction for persona inference. A periodically refreshed memory anchor and cognitive memory with three layers preserve persona consistency over long interactions. Across the main results, AI YOU \emph{(i)} achieves conformal coverage ranging from 0.921 to 0.976, \emph{(ii)} improves uncertainty calibration and reasoning grounded in memory, and \emph{(iii)} enhances persona fidelity over static prompting in role playing over 100 turns while reducing trait drift, for most evaluated backbones under adversarial settings with multiple agents. The prototype \emph{AI YOU Town} initializes an imaginative twin world for future interaction. The online demo is available at \href{this https URL}{\mbox{\texttt{this http URL}}}.

---


### 179. [Physics-inspired Pseudo Anomaly Generation and Prototype Feature Guidance for 3D Anomaly Detection](https://arxiv.org/abs/2607.10544)

**<font color=#1a73e8>作者：</font>** Jian Ning, Qin Zou, Linchun Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D point cloud anomaly detection plays a vital role in industrial manufacturing, yet it faces significant challenges due to the scarcity and high acquisition cost of real anomalous samples. The inherently anomaly-free training data further hinders detection methods from effectively learning discriminative features between normal and abnormal instances. To address these issues, we propose PA3AD, a novel framework that introduces a physics-inspired pseudo-anomaly generation strategy to create physically plausible anomalous samples from normal data. Additionally, we incorporate prototype features via a weight-sharing mechanism to guide the model in capturing the distribution shifts between normal and anomalous samples. Specifically, PA3AD introduces two key innovations to tackle the scarcity of real anomalies. First, a physics-inspired module generates diverse pseudo-anomalous point clouds from normal data via multi-physics modeling. Second, momentum-updated prototypes and a difference-aware fusion block capture stable normal representations and their discrepancies with pseudo-anomalies. This design effectively learns distribution shifts, achieving superior detection performance. Extensive experiments on the Anomaly-ShapeNet and Real3D-AD datasets demonstrate that our method consistently outperforms existing state-of-the-art approaches. Our code will be made publicly available at this https URL.

---


### 180. [CRiT-QA: Evaluating Multi-hop Reasoning with Counterfactual Chains and Distractor Traps](https://arxiv.org/abs/2607.10562)

**<font color=#1a73e8>作者：</font>** JungMin Yun, JuneHyoung Kwon, YoungBin Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the multi-hop reasoning capabilities of large language models remains a significant challenge. Although current models achieve strong results on existing multi-hop question answering datasets, such performance often masks two critical vulnerabilities: (1) reliance on internal parametric knowledge rather than adherence to the provided context, and (2) exploitation of dataset shortcuts, such as single-document cues or type-matching, that diminish the need for genuine evidence aggregation across multiple documents. We introduce CRiT-QA (Counterfactual Reasoning with Traps), a dataset explicitly designed to address both limitations. To neutralize reliance on memorized knowledge and enforce strict context dependency, CRiT-QA transforms factual reasoning chains with counterfactual entities. Furthermore, it injects multi-anchor distractor chains, plausible but incorrect reasoning paths that diverge at different hops. These traps require models to follow the entire reasoning process rather than exploiting shallow heuristics. Our experiments show that LLMs exhibit substantial performance degradation on CRiT-QA compared to standard datasets, exposing their vulnerability to counterfactual conditions and distractor traps. CRiT-QA thus serves as a rigorous diagnostic tool for evaluating genuine multi-hop reasoning and provides a foundation for developing more reliable, evidence-grounded LLMs.

---


### 181. [Quantum Compressed Sensing CT Reconstruction Algorithm Based on Penalized Weighted Least Squares and Guided Total Variation](https://arxiv.org/abs/2607.10566)

**<font color=#1a73e8>作者：</font>** Yuwen Zhang, Yujie Liu, Ao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective. Existing quadratic unconstrained binary optimization (QUBO)-based sparse-view computed tomography (CT) reconstruction neglects photon-counting statistics and anatomical heterogeneity. We address both limitations within the QUBO this http URL. We propose a quantum compressed-sensing CT method combining penalized weighted least squares (PWLS) and guided total variation (GTV). PWLS weights projection residuals by photon-count reliability, whereas GTV uses gradients from a prior image reconstructed by the simultaneous algebraic reconstruction technique (SART) to preserve edges and suppress noise in homogeneous regions. After binary encoding, both terms form a unified QUBO model. Experiments used four 40 times 40 CT images under a 10-view fan-beam geometry with Poisson noise. Comparisons included conventional reconstruction methods, QUBO variants, gradient descent, simulated annealing, and a D-Wave hybrid quantum-classical this http URL results. PWLS-GTV achieved the best reconstruction quality across all cases. In the representative chest case, it reached a peak signal-to-noise ratio (PSNR) of 36.64 dB, compared with 22.48 dB for SART, the best conventional baseline. GTV consistently outperformed conventional total variation. Simulated annealing and the D-Wave hybrid solver produced similar reconstructions, whereas gradient descent was ineffective. Repeated hybrid-solver runs showed stable this http URL. The framework incorporates photon-statistical weighting and structure-guided regularization into QUBO-based CT reconstruction without changing its quadratic form, providing a proof of concept for quantum-assisted sparse-view CT reconstruction.

---


### 182. [Learning from Local Walks on Dynamic Graphs with Bandit Feedback](https://arxiv.org/abs/2607.10571)

**<font color=#1a73e8>作者：</font>** Sourav Chakraborty, Amit Kiran Rege, Claire Monteleoni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic multi-armed bandits on dynamic graphs, where arms correspond to the vertices of a network with time-varying edges. In this setting, the learner is restricted to local movement, selecting only its current node or an immediate neighbor at each round. This constraint decouples best-arm identification from exploitation: even after the optimal arm is identified, the learner may remain unable to reach it through the evolving topology. We identify a process-agnostic structural condition, based on sliding-window mixing, that ensures the graph's intrinsic walk remains stable for both exploration and navigation. Under this regime, we analyze a family of local explore-then-commit algorithms and establish sublinear expected regret. Our framework includes a reward-aware strategy, for which we prove a worst-case safety theorem and a separate performance gain theorem.

---


### 183. [Why Domain Matters: Domain-Aware Benchmarking of Underwater Object Detection and Annotation Quality](https://arxiv.org/abs/2607.10575)

**<font color=#1a73e8>作者：</font>** Melanie Wille, Dimity Miller, Tobias Fischer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater object detection is strongly affected by domain shift, where performance can vary significantly across different locations, habitats, and deployment conditions. However, detector performance is typically evaluated using aggregate metrics that hide failures in specific environments, while existing domain generalization benchmarks often rely on synthetic variations that do not reflect real-world conditions. We introduce a framework that characterizes underwater images by appearance, scene composition, and acquisition geometry to assign domain labels. Using this framework, we perform the first systematic study of how domain factors influence both human annotation quality in underwater object detection datasets and deep learning-based detector performance, revealing substantial domain-dependent discrepancies. By incorporating physically meaningful domain labels, domain shift becomes something we can characterize, measure, benchmark, and act on. We highlight how this can be used to guide data collection and annotation, design more informative benchmarks, and assess detector robustness across diverse underwater environments.

---


### 184. [DiffUE: Enhancing Utility-Unlearnability Trade-off of Unlearnable Examples via Diffusion Autoencoders](https://arxiv.org/abs/2607.10580)

**<font color=#1a73e8>作者：</font>** Syed Irfan Ali Meerza, Oktay Ozturk, Amir Sadovnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI models are increasingly trained on personal images scraped from social media and public platforms, often without consent, leading to serious privacy violations, such as unauthorized facial recognition and targeted advertising. To counter this, researchers have developed unlearnable examples (UEs), images modified with imperceptible noise to prevent AI models from extracting meaningful information. However, existing UE methods primarily rely on pixel-space noise, which can be bypassed by relearning strategies such as adversarial training, image transformation, and compression. While some techniques improve robustness, they often come at the expense of significant degradation in image utility and perceptual quality. In this paper, we introduce DiffUE to overcome these limitations by injecting noise into the semantic space of images instead of the pixel space. Instead of corrupting pixel values, DiffUE modifies high-level semantic features of images, ensuring robust unlearnability while preserving visual quality and utility. By leveraging a diffusion-based autoencoder framework to manipulate semantic features, DiffUE generates purposeful, natural-looking modifications that effectively resist advanced relearning strategies. Extensive experiments on four datasets, CIFAR-10, CIFAR-100, CelebA-HQ, and ImageNet, as well as a subjective user study, demonstrate that DiffUE significantly enhances the trade-off between image quality and unlearnability, offering a more robust and effective solution for safeguarding personal data in an increasingly exploitative AI landscape.

---


### 185. [Benchmarking UAV-based Vehicle Re-Identification under Simulated Weather Conditions](https://arxiv.org/abs/2607.10583)

**<font color=#1a73e8>作者：</font>** Vu Minh Tran, Khang Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV-based vehicle re-identification (ReID) has emerged as a promising technique for traffic surveillance, urban monitoring, and public-safety applications thanks to the flexible viewpoints and wide-area coverage provided by unmanned aerial vehicles. However, despite recent progress on UAV-based vehicle ReID benchmarks, the robustness of existing methods under adverse weather remains insufficiently studied. This is important because weather degradation can significantly affect the fine-grained appearance cues required for reliable vehicle matching in aerial imagery, especially under small object scale, viewpoint variation, and complex backgrounds. In this paper, we present a controlled comparative study of three representative recent vehicle ReID methods, namely CLIP-ReID, MSINet, and AdaSP, on two UAV-based benchmarks, VRU and UAV-VeID. To ensure consistent robustness evaluation, we generate synthetic foggy and rainy variants of both datasets using an analytical weather-effect pipeline while preserving the original identities and data splits. All methods are then trained and evaluated under matched clean, foggy, and rainy conditions. Experimental results show that adverse weather consistently degrades retrieval performance across both datasets, with rain causing larger drops than fog in nearly all settings. Among the evaluated methods, AdaSP demonstrates the strongest robustness, achieving 93.0% and 88.5% mAP on VRU-Large, and 88.7% and 76.2% mAP on UAV-VeID-Test under foggy and rainy conditions, respectively. Overall, our findings show that simulated adverse weather substantially increases the difficulty of UAV-based vehicle ReID, reveals clear robustness differences among recent methods, and highlights the need for weather-aware model design and evaluation protocols in future aerial ReID research. The code is released at this https URL.

---


### 186. [Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification](https://arxiv.org/abs/2607.10588)

**<font color=#1a73e8>作者：</font>** Siyu Wang, Wei Tan, Lulu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tasks such as customs tariff classification, export control categorization, and standards-based equipment coding require assigning an input instance to a fine-grained class under an explicit regulatory hierarchy. Unlike standard text classification, the correct label in these tasks is not determined by semantic similarity alone, but by rule-defined boundaries, threshold conditions, exclusion clauses, definitions, and local exceptions. As a result, two highly similar inputs may require different labels, while a retrieved passage that appears relevant may still be inapplicable under the governing rules. Existing flat classifiers, hierarchical text classification methods, and retrieval-augmented LLM systems are not designed to jointly enforce hierarchical validity, rule consistency, and fine-grained boundary reasoning. In this paper, we formulate this setting as regulation-driven fine-grained hierarchical classification, where an external instance must be assigned to a fine-grained class through a valid path in a regulatory hierarchy and supported by auditable evidence. We construct four benchmark datasets from representative regulation-intensive scenarios and validate the annotations through an expert-in-the-loop process. We further propose a constraint-aware hierarchical search framework that converts regulatory documents into a searchable tree, retrieves only valid local candidate nodes, and uses structured regulatory fields with evidence snippets to guide each next-hop decision. Experiments show that our method achieves the best mean accuracy on all four datasets and provides interpretable decision paths, with the largest gains on cases involving fine-grained neighboring categories and rule-based boundary conditions.

---


### 187. [Non-binary bottom-up constituency parsing without arity actions](https://arxiv.org/abs/2607.10591)

**<font color=#1a73e8>作者：</font>** Jungyeul Park, Eunkyul Leah Jo, Zihao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Non-binary bottom-up constituency parsing is usually taken to require arity actions: reductions such as \(\textsc{Reduce-}X\#k\) specify both the mother label and the number of children to be composed. We show that this arity parameter is not a necessary transition primitive. Our parser introduces constituent labels separately and recovers reduction spans from delimiter-bounded stack configurations. In a well-formed reduction configuration, arity is uniquely determined by the active delimiter and the label marker, making it a derived property of parser state rather than an action label. This factorization removes label--arity-specific reduce actions while preserving direct construction of original non-binary trees. Experiments on PTB and CTB show that the delimiter-guided parser remains competitive with an arity-specific bottom-up baseline under the same implementation framework, with substantially smaller action inventories. Analyses further show that its predicted arity profile remains close to the gold treebanks and that high-arity constituents do not collapse when arity actions are removed.

---


### 188. [Sharp Concentration Bounds for Bundle-Valued Statistics on Manifolds](https://arxiv.org/abs/2607.10592)

**<font color=#1a73e8>作者：</font>** Swagatam Das, Vaclav Snasel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many geometric statistics and manifold learning pipelines routinely produce observations -- such as tangent vectors or local frames -- whose natural home is a varying family of fibers attached to different points of a base manifold, rather than a single shared vector space. Forming empirical averages requires transporting these observations to a common reference fiber, thereby introducing curvature- and holonomy-driven effects that are absent from classical concentration theory. We develop a non-asymptotic concentration theory for such transported empirical means, deriving finite-sample, dimension-free Hoeffding- and Bernstein-type bounds via sharp Hilbert-space inequalities. When shortest paths to the reference point are non-unique, transport becomes path-dependent and introduces a deterministic holonomy bias; we isolate and quantify this bias through bundle curvature and loop geometry, with sharp closed-form formulas for the tangent bundle of a round sphere. The resulting bias-variance decomposition separates the stochastic fluctuation decaying at the classical $n^{-1/2}$ rate in sample size $n$, from a curvature-driven error floor that no amount of additional data can eliminate; minimax lower bounds confirm both terms are unavoidable. We further establish a robust median-of-means estimator achieving optimal rates under heavy tails and the central limit theorem in the reference fiber. Controlled experiments on the sphere validate all theoretical predictions.

---


### 189. [AutoNorm: Understanding Adaptive Normalization in Transformers through Differentiable Gating](https://arxiv.org/abs/2607.10593)

**<font color=#1a73e8>作者：</font>** Piyush Kaushik Bhattacharyya, Divyanshu Rai, Swastik Singh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Normalization is a critical component for stabilizing Transformer training, yet the choice between static strategies such as Layer Normalization (LN) and adaptive alternatives remains largely task-dependent. In this paper, we investigate a key optimization challenge in differentiable normalization gating. Our experiments show that, on relatively stationary vision tasks, the high gradient variance introduced by Gumbel-Softmax gating can hinder convergence of the routing mechanism, causing learned gates to underperform simple random selection. In contrast, on non-stationary language modeling and classification tasks, sustained gating diversity enables the model to learn more effective layer-wise normalization policies. Motivated by these observations, we propose AutoNorm-S (Stabilized), a training strategy that mitigates optimization instability through a gate-freezing schedule. AutoNorm-S achieves competitive or improved performance across multiple benchmarks, outperforming adaptive normalization baselines on NLP datasets, including PTB and SST-2, while remaining competitive on standard vision benchmarks. These results suggest that decoupling normalization selection from optimization noise provides a practical and principled approach for adaptive normalization in Transformer architectures.

---


### 190. [End-to-End Real-Time Drone-Based Person Detection Framework Using Deep Learning](https://arxiv.org/abs/2607.10605)

**<font color=#1a73e8>作者：</font>** Payel Sarmah, Ayush Ranjan, Piyush Kaushik Bhattacharyya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, Unmanned Aerial Vehicles (UAVs) or drones have gained rapid response in terms of security, search and rescue (SAR), border surveillance, etc. Existing monitoring frameworks often struggle to maintain detection consistency when targets undergo significant scale variations due to altitude changes, leading to critical information gaps. To address this issue, this work proposes an integrated real-time detection pipeline for detecting targets through the wireless live drone video feed. Build upon YOLOv8-nano architecture, extensive flight experiments were conducted to determine the detection performance across multiple flight altitudes. Trained on VisDrone2019 dataset, the results of YOLOv8-nano model achieves 57.4%, 41%, 44.8% and 20.3% in precision, recall, mAP and mAP50:95 respectively. While demonstrating on real environment, this analysis revealed that the algorithm achieves near-total detection reliability at altitudes between 16 and 25 meters with the detection frame rate consistently maintained above 41 FPS and reaching a peak of 50 FPS. However, the goal of this work is to enable real-time person detection from an aerial platform via wireless transmission. This approach effectively addresses the dual challenges of identifying targets at varying scales and ensuring near-to-accurate localization during aerial observation.

---


### 191. [The Compliance Trap: Diagnosing How AI Agents Consume Conflicting Memory](https://arxiv.org/abs/2607.10608)

**<font color=#1a73e8>作者：</font>** Yixiong Chen, Xinyi Bai, Alan Yuille  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory is becoming a core component of long-horizon AI agents, allowing agents to reuse past experience when operating web browsers, software tools, and other interactive environments. Existing work mostly treats memory as a supply problem, asking what experience to write, how to store it, and which entry to retrieve for the next task. Yet we still lack a clear account of how models consume retrieved memory across a multi-step action trajectory. This consumption process matters because it determines not only what memories should be retrieved, but also what models and control policies are needed to use them safely. To diagnose this process, we propose Entry--Propagation--Recovery (E-P-R), a trajectory-level framework that asks where memory first changes an action, whether that change carries forward, and whether the agent can recover after leaving a correct path. We instantiate E-P-R on WebArena and on MemTrapBench, a controlled benchmark we build to isolate these phases. We find that the main failure often begins at entry: agents adopt conflicting memory at the first exposed decision point even when it is task-wrong. Repeated exposure then amplifies this early error, while recovery after divergence is weak. Together, these effects create a compliance trap: across models, conflicting memory induces similar compliance rates, but once agents comply, their success rates collapse to a low floor. Stronger agents therefore suffer larger absolute damage because each compliance event erases more baseline capability. These results suggest that memory-augmented agents should be evaluated not only by retrieval quality or final success rate, but by how they consume memory throughout the trajectory.

---


### 192. [M+Adam: Low-Precision Training via Additive-Multiplicative Optimization](https://arxiv.org/abs/2607.10611)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Liang, Sebastian Loeschcke, Mads Toftrup 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training with quantized weights can reduce costs but often results in degraded accuracy, especially when optimization is carried out in low precision, without storing high-precision copies. We identify a key failure mode: under low precision, standard optimizers can get stuck and not make progress, especially at large weight magnitudes due to coarse mantissa resolution. To overcome this, multiplicative updates have been previously proposed, in place of additive updates in standard optimizers. While successful under extremely low precision, such as under the logarithmic number system, they suffer from failures near zero and across sign changes. The failure modes of additive and multiplicative updates are therefore complementary. To exploit this, we propose M+Adam, which combines both update types: additive steps handle sign changes and small magnitudes, while multiplicative steps ensure progress at large magnitudes when additive updates are zeroed out under rounding. We prove monotone descent for M+Adam under standard smoothness assumptions. Across LLaMA-style pretraining with 60M-1B models, 1x-8x Chinchilla budgets, and using only BF16, FP8, and FP4 master weights, M+Adam consistently improves low-precision training.

---


### 193. [modelDNA: Calibrated Lineage Verification and Merge Decomposition from Sampled Weight Fingerprints](https://arxiv.org/abs/2607.10617)

**<font color=#1a73e8>作者：</font>** Muhammad Awais Bin Adil, Saad Aamir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The lineage graph of open-weight language models is self-reported: Hugging Face's base_model metadata field is optional and unverified, and over 60% of Hub models document no parentage at all. Methods for detecting lineage from weights exist in the research literature, but each ships as paper code tied to one signal and one experiment; when a provenance dispute breaks, the analysis is redone by hand. This report describes modelDNA, a tool that fingerprints a model from roughly 100-300 MB of ranged HTTP reads (instead of a full 15 GB download for a 7B model), compares the fingerprint against a reference database of foundation models across four published signal families, and returns one of eight verdict classes with a calibrated probability, preferring honest abstention to confident error. On a benchmark of 15 real Hub models with org-documented parentage, judged against 8 candidate bases (13 positives, 107 hard negatives), the system achieves AUROC 1.0, zero false positives at its reporting threshold, and 13/13 correct top-1 parent attribution. The report's second contribution is merge decomposition. Every mainstream weight-merging method is (near-)linear per tensor, and fingerprint sample positions are deterministic functions of tensor identity, so a merged model's fingerprint is the same linear combination of its parents' fingerprints. Mixture weights can therefore be recovered from fingerprints alone by sum-to-one constrained least squares. Against merges with published mergekit configurations as ground truth, the method recovers a slerp merge's layer-interpolation curves at r = 0.999 and a dare_ties merge's mixture weights to within 0.011 of the published values, without downloading any weights beyond the fingerprints. All fingerprints, benchmarks, and the inferred lineage graph of 55 models are public and reproducible offline.

---


### 194. [Spectral Consistent Flow for One-step 3D Medical Image Translation](https://arxiv.org/abs/2607.10627)

**<font color=#1a73e8>作者：</font>** Haoqing Li, Jun Shi, Mingchao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Spectral Consistent Flow (SC-Flow), a 3D medical image translation framework with a single function evaluation (1-NFE) in the latent space. This approach reformulates medical image translation as a stochastic Brownian bridge process that directly constructs a mapping between source and target modalities by predicting the support regularized mean velocity field. To mitigate modality entanglement, over-smoothing, and artifacts induced by the implicit low-pass modulation of the latent average velocity, we introduce a Spectral Consistency Corrector that dynamically regularizes the evolution of the power spectral density via learnable frequency-domain gain modulation. This mechanism establishes an explicit bridge between spatial textures and spectral energy flow, enabling the model to recover fine-grained anatomical fidelity while maintaining global structural coherence. Extensive experiments on four datasets demonstrate that SC-Flow delivers significantly more accurate, consistent, and robust performance across various translation scenarios.

---


### 195. [Anamnesis: An Open-Source Platform for Large-Scale Backstory-Conditioned Survey Simulation](https://arxiv.org/abs/2607.10628)

**<font color=#1a73e8>作者：</font>** Song-Ze Yu, Joseph Suh, Serina Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Anamnesis, an interactive system for demographically controllable survey simulation using large language models. Open-source, and designed for non-technical users/researchers, Anamnesis enables the prototyping and stress-testing of survey instruments on virtual populations rather than real human subjects. The platform operationalizes the recently introduced Anthology and Alterity frameworks, which use structured narrative backstories to condition model responses, within a unified web interface. It supports open-ended generation, probabilistic demographic resampling, and multimodal (image and audio) surveys. We evaluate the system through two case studies: (1) replicating segments of Pew Research Center's American Trends Panel (ATP) on political typology and biomedical issues and (2) emulating human preference in the New Yorker Caption Contest. In both cases, Anamnesis produces opinion distributions that more closely match real-world survey data than standard persona-prompting baselines, offering a transparent, reproducible, and open-source alternative to proprietary simulation services.

---


### 196. [Auditing Construct Overlap in Explainable Machine Learning: Evidence from Burnout-Depression Prediction Across Student Cohorts](https://arxiv.org/abs/2607.10633)

**<font color=#1a73e8>作者：</font>** Alireza Dehghan, Negin Ashrafi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainable machine learning (XML) pipelines applied to composite mental health outcomes can produce apparently-robust, cross-population-stable risk hierarchies that are largely artefacts of how the outcome was constructed. We demonstrate this using an ElasticNet pipeline applied to 886 medical students at the University of Lausanne (primary cohort, 2022), validated across 2,580 longitudinal observations at three time points and 701 non-medical students from eight faculties; all three datasets share identical instruments. The pipeline produces a hierarchy in which trait anxiety and health satisfaction dominate wherever the outcome is measured, with Kendall $\tau = 1.0$ for the top-two positions across all five evaluation sets and consistent transfer performance ($R^2$: 0.41-0.49). Two residualization experiments, which isolate shared variance between correlated variables via regression, reveal the mechanism: when trait anxiety (STAI-T) is residualized against the co-included depression subscale (CES-D, $r = 0.72$), model $R^2$ drops from 0.41 to 0.16 and STAI-T falls from rank 1 to rank 6; when burnout subscales are residualized against CES-D, $R^2$ collapses to 0.016. Prediction intervals average 35.4 units on a 0-100 scale (2.4 outcome standard deviations), independently ruling out individual-level deployment. The residualization protocol is the paper's transferable contribution: any XAI study combining correlated predictor and outcome constructs should apply this check before interpreting apparent stability as a finding.

---


### 197. [Modernizing HEBO: a robust Bayesian optimization baseline for practical heteroskedastic and non-stationary problems](https://arxiv.org/abs/2607.10669)

**<font color=#1a73e8>作者：</font>** L. A. Zhukov, E. V. Shaburova, D. V. Antonets  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization is increasingly used to guide data-efficient experimentation in chemistry, materials science, and related laboratory settings, but its practical performance depends strongly on how well surrogate-model assumptions match the geometry and noise structure of the underlying objective. We introduce tidyHEBO, a robust Bayesian optimization model inspired by heteroskedastic evolutionary Bayesian optimization (HEBO) for single-objective, sequential optimization. tidyHEBO reconstructs the HEBO design philosophy in BoTorch and revises surrogate training, output-warping selection, acquisition function evaluation, and Pareto-front search. We benchmarked tidyHEBO on synthetic functions, Olympus emulators, fully experimental reaction-optimization datasets, needle-in-a-haystack (NIAH) materials problems, and Bayesmark hyperparameter optimization tasks. On these tasks tidyHEBO achieved competitive to superior performance and improvement in robustness across repeated optimization runs. We therefore propose tidyHEBO as a practical tool for sequential experimentations and a strong general-purpose benchmark for future Bayesian optimization research.

---


### 198. [From Self-Attention to Connection Laplacian: A Unified Operator View of Transformers](https://arxiv.org/abs/2607.10677)

**<font color=#1a73e8>作者：</font>** Binbin Lin, Wei Chen, Yalun Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention is a ubiquitous primitive in modern sequence models, yet its operator-level geometry is only partially understood. We view a token sequence as a vector field over the token-position graph and identify attention as a connection walk: messages are aggregated by a nonnegative walk matrix while being transported along each edge by a learned linear map. Within this framework, we prove that single-head attention (SHA) is exactly a connection propagation step with constant transport, and that multi-head attention (MHA) is exactly a single edge-dependent connection walk whose effective transport is an attention-gated mixture of headwise transports. We further clarify the conditions under which the corresponding generator reduces to a random-walk connection Laplacian, highlighting the roles of stochasticity, reversibility, and metric-compatible transports. Empirically, we find that trained Transformers across scales (from 124M to 8B) and structures (encoder/decoder) exhibit geometric structure consistent with our theory: effective attention graphs converge to stable geometric operators in deeper layers, learned transports self-organize into approximate scaled isometries, and both phenomena strengthen consistently with scale. Overall, the paper provides a precise connection-walk formalism that links self-attention to classical geometric operators, along with a set of operator-level tools for analyzing transformer models from a geometric perspective.

---


### 199. [Personalized Emotional Intelligence in Generative AI through Symbolic Affective Reasoning](https://arxiv.org/abs/2607.10678)

**<font color=#1a73e8>作者：</font>** Qing Lin, Mengmi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotional intelligence enables humans to recognize emotions, infer their causes, reason about interventions, and modify their environment to achieve desired affective states. Despite recent advances in artificial intelligence (AI), current models remain largely limited to generating realistic content or performing semantic reasoning, with little capacity for understanding, predicting, and personalizing human emotional responses. Here we introduce Emotion-augmented geneRatiOn System (EROS), a hybrid AI framework that integrates symbolic reasoning with deep learning to enable personalized emotion augmentation through visual content. Leveraging large-scale image-emotion datasets, EROS discovers generalizable affective rules, identifies emotion-relevant image regions, and predicts context-aware visual modifications that preserve scene semantics while steering emotional responses toward desired targets. To account for individual variability, EROS incorporates an expandable memory bank that supports inference-time personalization without model fine-tuning, yielding interpretable emotional profiles and rapid adaptation to new users. Across extensive human psychophysics experiments, EROS elicits target emotional responses more effectively than state-of-the-art large multimodal models while adapting to individual affective preferences. Beyond affective computing, EROS provides a foundation for AI systems that can understand, reason about, and augment human cognitive states, with potential applications in mental health, adaptive media, education, and human-computer interaction.

---


### 200. [LayerNorm as Implicit Gain Control in Looped Transformers](https://arxiv.org/abs/2607.10681)

**<font color=#1a73e8>作者：</font>** Matthias M. M. Buehlmaier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In pre-LayerNorm looped transformers, LayerNorm inside the recurrent block acts as an implicit gain controller: by coupling the block's local Lipschitz constant inversely to the activation scale, it renders the recurrence Jacobian non-normal -- asymptotically contractive at every verified fixed point even where its operator norm exceeds 1 -- so the true stability budget is the spectral margin, not an operator-norm bound. That margin depletes as the carry $\rho \to 1$, and a minority of initializations never converge to a fixed point at all, so the diagonal carry constraint $\rho(\bar{A}) < 1$ is necessary but not sufficient for convergence of the full recurrence. Training experiments across six tasks, including a controlled ablation, reveal that the linear carry is not the depth-memory mechanism: gradient descent routes memory through the block's more expressive nonlinear recurrence and leaves the stability-constrained carry at rest -- the carry's role is stabilization, not memory. We characterize the boundary of this claim: on tasks with axis-aligned per-channel structure, gradient descent does recruit the carry. All results are derived analytically and verified in a from-scratch, CPU-scale implementation; verification at larger scale is needed.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-420](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
