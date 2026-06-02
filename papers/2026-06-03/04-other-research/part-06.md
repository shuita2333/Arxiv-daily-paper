# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 251. [Optimal-Point Variance Reduction For Bayesian Optimization With Regret Guarantee](https://arxiv.org/abs/2606.00956)

**<font color=#1a73e8>作者：</font>** Shion Takeno  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies a one-step lookahead Bayesian optimization (BO) method and its theoretical guarantee. Although the empirical effectiveness of one-step lookahead BO methods, such as entropy search, has been studied extensively, they often rely on computationally intractable approximations, and their regret guarantees remain underdeveloped. Thus, this paper proposes a one-step lookahead BO method called optimal-point variance reduction (OVR), which requires only posterior sampling and Monte Carlo approximations. We obtain a uniform error bound over an input domain for the Monte Carlo estimation in OVR. Furthermore, we show that the regularized OVR, with the slight modification to promote exploration, achieves a vanishing Bayesian expected simple regret upper bound. Finally, we demonstrate the effectiveness of OVR through numerical experiments.

---


### 252. [Boundary-Protection W8A8 HiFloat8 Quantization for Large-Scale Text-to-Video Diffusion Transformers](https://arxiv.org/abs/2606.00957)

**<font color=#1a73e8>作者：</font>** Yiming Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a post-training quantization (PTQ) approach for Wan2.1-T2V-14B, a 14-billion-parameter text-to-video diffusion transformer, targeting the W8A8 HiFloat8 (HiF8) format on Ascend 910B NPUs. A central challenge in quantizing video DiT models is the heterogeneous activation distribution across transformer blocks: boundary blocks (the first and last few blocks) exhibit fundamentally different statistical properties from middle blocks, making uniform quantization ineffective. We conduct a systematic per-block activation analysis across all 40 WanAttentionBlocks and use the findings to motivate a boundary-protection strategy that retains the first two and last three blocks in BF16 while quantizing the remaining 35 blocks with W8A8 HiF8. The proposed PTQ method matches or marginally exceeds the BF16 baseline on all five VBench dimensions evaluated, indicating no measurable accuracy loss within the 5-prompt evaluation set. An ablation study over four protection configurations confirms that full boundary protection yields the highest average VBench score, validating the data-driven block selection. We additionally investigate quantization-aware training (QAT) as a complementary fine-tuning stage and analyze the conditions under which it fails to outperform plain PTQ on single-card hardware.

---


### 253. [SS-ZKR: Spatial-Semantic Zero-Knowledge Routing for Privacy-Preserving Multi-Agent Collaboration](https://arxiv.org/abs/2606.00962)

**<font color=#1a73e8>作者：</font>** Hassan Touheed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Foundational agent interoperability standards, notably the Agent-to-Agent (A2A) protocol and the Model Context Protocol (MCP), have advanced multi-agent system communication, and complementary identity frameworks leveraging W3C Decentralised Identifiers (DIDs) and Verifiable Credentials (VCs) provide cryptographic agent authentication. However, no existing protocol supports content-based semantic routing of agent payloads across organisational trust boundaries without requiring the routing intermediary to decrypt the payload, which is a hard constraint in compliance-sensitive environments governed by GDPR, HIPAA, and MiFID II. We propose SS-ZKR, a three-mechanism privacy-preserving routing protocol designed as a complementary layer atop A2A/MCP. Mechanism I introduces blind routing via differentially private semantic intent vectors cryptographically bound to zero-knowledge proofs of payload-schema consistency. Mechanism II offers vector-weighted adaptive payload sanitisation with formal (epsilon, delta)-differential privacy for numerical fields and heuristic semantic aggregation for textual fields. Mechanism III presents a spatial-to-cryptographic policy compiler that translates visually defined trust-zone topologies into deterministic zero-knowledge access circuits. We provide a formal threat model, analyse information leakage bounds of intent vectors, present pseudocode for all three mechanisms, and give analytical complexity comparisons against TEE-based and homomorphic encryption-based routing baselines. SS-ZKR lets enterprises in financial services, healthcare, and defence orchestrate heterogeneous AI agents across regulatory boundaries without exposing proprietary data to routing infrastructure.

---


### 254. [Flexible Control of 3D CT Generation via Text and Semantically-Defined Segmentation Prompts](https://arxiv.org/abs/2606.00967)

**<font color=#1a73e8>作者：</font>** Weicheng Dai, Chenyu Wang, Andy Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models for volumetric medical images have found many applications in medical imaging, ranging from data augmentation to serving as priors for inverse problems. For these applications, generating high-resolution 3D images with strong controllability is essential but remains highly challenging. Existing approaches typically control generation either through radiology reports used as text prompts or through full image segmentation. While text-based prompting is flexible, it provides limited spatial control over the location, shape, and boundary of abnormalities. In contrast, segmentation-based methods receive precise spatial guidance but are restrictive in requiring full-organ annotations. In this work, we propose a flexible multimodal framework for controllable volumetric image generation that supports input from radiology reports and segmentation prompts (both optional). Our approach allows users to provide segmentation of a specific anatomy or abnormality without requiring full-organ annotations. The semantic meaning of the segmentation mask is specified through an accompanying text description, resulting in a highly flexible and scalable conditioning mechanism. We develop a memory-efficient architecture based on a modified diffusion transformer that jointly processes image and segmentation tokens. The model further incorporates gated attention to effectively attend to long radiology reports. Experiments demonstrate that our method achieves state-of-the-art perceptual and semantic scores (e.g., 24% relative improvement in mean FID), generates high-resolution anatomically consistent CT volumes, and improves data efficiency when used for data augmentation. Radiologists' evaluation further confirms strong alignment between generated and real medical images.

---


### 255. [UME: A Unified Meta-Generalization Framework for Cross-Domain ETA](https://arxiv.org/abs/2606.00979)

**<font color=#1a73e8>作者：</font>** Duo Wang, Qiong Wu, Jianguo Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate Estimated Time of Arrival (ETA) prediction on checkout page is crucial in instant logistics for enhancing user satisfaction, optimizing dispatching, and controlling operational costs. In international on-demand delivery platforms, where ETA data originates from diverse countries or regions with different patterns, multi-domain modeling is of great importance and has been widely adopted. However, existing methods still face three critical challenges in real-world deployment. First, current multi-domain models struggle to generalize to completely unseen domains, failing to achieve zero-shot prediction during the initial cold-start phase. Second, cross-domain feature spaces are often assumed to be consistent, whereas new domains commonly suffer from structural missingness of offline (statistical) features due to the lack of historical data. Third, such feature missingness often compels industrial systems to model mature and cold-start domains separately, hindering knowledge transfer and increasing maintenance overhead. To address these challenges, we propose \textbf{UME}, a \textbf{U}nified \textbf{M}eta-generalization framework for \textbf{E}TA. Specifically, UME integrates a unified dual-branch architecture with a novel meta-learning mechanism that employs a hypernetwork-based meta learner. By leveraging domain-level knowledge and instance-level context, the meta learner empowers three meta modules to dynamically modulate feature gating, expert attention, and final prediction, capturing cross-domain correlations and facilitating intra-domain adaptation. A knowledge distillation strategy is further introduce to enhance performance. UME has now been deployed in Meituan-keeta delivery platform (the largest international food delivery platform in China). Extensive offline experiments and online A/B tests demonstrate that UME significantly outperforms existing baselines.

---


### 256. [Robust Asynchronous Planning via Auto-Formalization](https://arxiv.org/abs/2606.00981)

**<font color=#1a73e8>作者：</font>** Jiayi Zhang, Jianing Yin, Ben Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can plan by either generating action sequences directly as a Planner or translating tasks into domain specific language for an external solver as a Formalizer. While most real-world tasks are asynchronous with non-uniform durations, concurrency, and execution-time constraints, existing benchmarks hardly cover them. We unify these asynchronous planning challenges under a single formulation and introduce the first three benchmarks that address each at scale. We conclude that the choice of formal representation primarily determines whether planning scales: as dependency graphs grow from 5 to 100 actions, Planner collapses from 96% to 5% plan accuracy and PDDL2.1 Formalizer from 13% to 0%, while CP-SAT Formalizer averages 94% and still achieves 83% at 100 actions. Faithfulness diagnostics show that PDDL2.1's predicate-based planning representation becomes brittle compared to general constraint satisfaction programs, when LLMs must keep predicates, effects, and goals consistent. Execution-time updates of planning constraints further degrade performance sharply (Planner 23.9%, PDDL2.1 0.7%, CP-SAT 46.1%), but a state-aware repair strategy that updates only event-induced constraints recovers CP-SAT Formalizer to 84.5%.

---


### 257. [Profiling Privacy Preservation Against Gradient Inversion Attacks in Tabular Federated Learning](https://arxiv.org/abs/2606.00986)

**<font color=#1a73e8>作者：</font>** Ivo Osterberg Nilsson, Maximilian Birr Engvall, Viktor Valadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables multiple data holders to train machine learning models collaboratively without centralizing raw data, making it useful in privacy sensitive domains such as healthcare and institutional data sharing. FL keeps data local to clients while communicating only model updates, such as gradients or model deltas. Nevertheless, these updates can expose private client data through gradient inversion attacks (GIAs). We study this risk for tabular FL under an honest-but-curious server threat model across FL protocols, client batch sizes, training stages, attacker assumptions, model architectures, and binary classification, multiclass classification, and regression tasks. We use MIMIC-IV and complementary benchmark datasets. Our evaluation distinguishes numerical and categorical recovery, baseline recoverability, feature level recovery, and exact match rate (EMR). We evaluate FedSGD gradients and FedAvg model deltas with an exposure aligned protocol, comparing attacked models after matched client data exposure rather than matched communication rounds. We compare multilayer perceptron (MLP), ResNet, and FT-Transformer models, and isolate architecture effects through an MLP grid over width, depth, activation, normalization, and dropout. The results show that small client batches and updates representing few distinct records are most vulnerable. Larger local batches and stronger aggregation reduce reconstruction but do not eliminate leakage. FT-Transformer is consistently harder to invert than one-hot baselines, while reconstructability also varies substantially within the MLP family. These findings identify architecture as a practical privacy variable in tabular FL. We also show that aggregate reconstruction accuracy can overstate complete record recovery in sparse data, making EMR and baseline comparisons essential.

---


### 258. [Data Enrichment for Symbolic Regression Using Diffusion Models](https://arxiv.org/abs/2606.00988)

**<font color=#1a73e8>作者：</font>** Simon De Reuver, Tamas Kristof Toth, Teddy Lazebnik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) offers a route to scientific discovery by converting observations into interpretable governing equations. However, despite its promise, its reliability degrades sharply when spatiotemporal measurements are sparse, noisy, or physically incomplete, as commonly occurring in practice. Data enrichment (DE) has been shown to be able to mitigate this limitation, yet additional samples can mislead equation discovery unless they preserve the physical structure of the target system. Such implication of DE requires narrow domain expertise as well as technical fluidity, highly limiting its practical usefulness. In this study, we introduce a physics-guided latent diffusion framework for DE for down the line SR models. The proposed framework combines a variational autoencoder, a conditional latent diffusion model, and a physics-informed residual corrector to complete sparse observations with synthetic fields constrained by governing relations. We evaluate the approach on heat conduction, incompressible Navier-Stokes flow, and a moving single-mass Newtonian gravitational potential, using GPLearn, DEAP, and PySR as downstream SR backends. Our results reveal that physics-corrected enrichment consistently improves recovery in sparse regimes across physical dynamics and SR models. These results show that generative enrichment can strengthen equation discovery without additional domain expertise.

---


### 259. [Subliminal Learning Is Steering Vector Distillation](https://arxiv.org/abs/2606.00995)

**<font color=#1a73e8>作者：</font>** Camila Blank, Agam Bhatia, Senthooran Rajamanoharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Subliminal learning refers to a student language model acquiring a teacher's traits (e.g. a system-prompted preference for owls) when fine-tuned on the teacher's outputs, despite the outputs being semantically unrelated to those traits. It remains poorly understood how data without semantic meaning can transfer specific semantic traits. In this work, we show that subliminal learning is mediated by a single steering vector, i.e. a vector added to the model's activations. Across two open-source models, we find that the teacher's system prompt is well approximated by a steering vector, and that the student's behavior is driven by learning an aligned vector over fine-tuning. System prompts that are not well approximated by steering vectors are not subliminally learned. This is a special case of steering vector distillation, in which a student trained on the outputs of a steered teacher learns to imitate that steering. We demonstrate steering vector distillation on a range of semantic and random vectors. Adding a semantic vector to a model's activations can have both model-independent and model-specific (i.e. non-semantic) effects on its behavior, so generated data that is non-semantic can transmit a vector with semantic effects, enabling subliminal learning. This also explains why subliminal learning does not transfer between models. We find that adaptive optimizers are necessary for subliminal learning in language models: activation gradients on steered data carry a small but consistent component along the steering direction, and non-adaptive optimizers impede this by allowing outlier gradients to dominate.

---


### 260. [SWARD: Stochastic Window-Attention-Based Relational Distillation for Cross-Architectural Semantic Segmentation](https://arxiv.org/abs/2606.00999)

**<font color=#1a73e8>作者：</font>** Aditya Makineni, Qing Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale vision foundation models have driven substantial gains on dense prediction tasks such as semantic segmentation, but their size makes deployment impractical in resource-constrained settings, motivating knowledge distillation as a means of transferring their capabilities to lightweight student networks. However, modern foundation teachers are predominantly transformer-based that encode global context, whereas efficient students are typically convolutional networks with locally biased receptive fields. Existing distillation methods largely assume architectural homogeneity and rely on direct feature mimicry, which fails to bridge this representational gap and neglects the structured spatial dependencies and discriminative organization required for accurate semantic segmentation. In this paper, we propose SWARD, a knowledge distillation framework that addresses this gap through two complementary mechanisms. First, we introduce a Multi-Scale Windowed Attention Distillation (MWAD) module that aligns teacher-student attention-based relations within stochastically shifted window partitions whose offsets are randomly resampled at every training iteration. This removes window boundary bias, and, combined with the multi-scale design, captures both short- and long-range spatial dependencies. Second, we introduce Prototype Discriminative Regularization (PDR), a loss that helps shape the student's feature distribution by enforcing inter-class separation and intra-class compactness, further sharpening the discriminative structure beyond what feature mimicry alone can produce under the student's reduced capacity. Experiments across different vision applications (i.e., urban scene parsing and medical image segmentation) show that SWARD achieves state-of-the-art performance.

---


### 261. [Trust Functions: Near-Lossless Weak-to-Strong Generalization by Learning When to Trust the Weak Teacher](https://arxiv.org/abs/2606.01000)

**<font color=#1a73e8>作者：</font>** Arda Uzunoglu, Alvin Zhang, Daniel Khashabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weak-to-strong generalization studies how to improve a strong student using supervision from a weaker teacher when reliable labels are scarce. We view this primarily as a data selection problem, where the key challenge is to identify which weak labels are reliable enough to serve as a training signal. To address this, we introduce trust functions that assign each weak label a scalar trust score and use these scores to filter weak supervision. Across several domains, including world knowledge, quantitative reasoning, and strategy games, trust filtering yields students that match and sometimes surpass ground-truth supervision, achieving near-lossless weak-to-strong generalization. Moreover, trust functions enable an iterative weak-to-strong chain that compounds gains by training a student and reusing it as the next teacher, amplifying the gains. There are several mechanisms to which advantage of trust functions can be attributed.

---


### 262. [Automated Erythrocyte Detection and Tracking for Retinal Blood Flow Quantification in Erythrocyte-Mediated Angiography](https://arxiv.org/abs/2606.01006)

**<font color=#1a73e8>作者：</font>** Chiao-Yi Wang, Havish S Gadde, Yi-Ting Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capillary-level retinal blood flow (RBF) has strong potential as a biomarker for various ocular diseases. However, modalities for measuring capillary-level RBF remain limited. Erythrocyte-mediated angiography (EMA), an emerging imaging technique, enables capillary-level RBF measurement by visualizing individual erythrocytes, yet automated erythrocyte detection and tracking, which are essential for quantifying blood flow, remain largely unexplored. To address this gap, we propose EMTrack, a novel framework featuring a flow-context module for erythrocyte detection that distinguishes moving from paused cells and a topology-aware tracking strategy that enables tracking under large inter-frame displacements and substantial motion variations. In addition, we establish RBF-EMA, a new EMA dataset with comprehensive erythrocyte detection and tracking annotations. Experimental results demonstrate that our method outperforms baseline methods both quantitatively and qualitatively on detection and tracking tasks in the RBF-EMA dataset. Moreover, RBF quantification results highlight the strong potential of our framework for automated retinal blood flow measurement.

---


### 263. [Can AI Review Improve Paper Drafting? An Empirical Study on 20 Computer Architecture Submissions](https://arxiv.org/abs/2606.01013)

**<font color=#1a73e8>作者：</font>** Di Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research is advancing faster than ever with artificial intelligence (AI); and so are the corresponding research papers. The exploding volume of AI-generated papers have put a strain to peer review, leading to the usage of AI-generated review, potentially wide yet sneaky. However, relevant ethical concerns about confidentiality, quality, and fairness are raised and no consensus has been reached in the broad research community. We expect the debate to continue for a while, but in the meantime, we ask an alternative, practical question: \textit{can AI review improve paper drafting?}
We study 20 computer architecture papers, with varying levels of submission lineage, to expose how well AI review aligns with human review, quantified by a set of metrics we define. To conduct the case study, we build a web UI-integrated tool, \emph{AI-Paper-Review}, that generates structured AI review of a draft paper, available at this https URL. This tool selects several AI reviewers from a diverse pool of AI reviewers and clusters and ranks their comments based on commonality and importance of review comments. It also allows to align AI comments with human comments to facilitate metric-based validation. The case study shows that AI review can cover a significant fraction of human-raised issues, but also raises issues missing in human review.
This paper is not intended to encourage using AI for peer review at the current stage, but to study that (1) how AI review can improve paper drafting and (2) the potential and limitation of AI-based peer review. The release of the tool and the case study data is intended to instigate future research on this topic. Misuse for peer review would violate the ethics policies from major academic venues.

---


### 264. [Cross-Axis Feature Fusion with Joint-Wise Motion Difference Prediction for Text-Based 3D Human Motion Editing](https://arxiv.org/abs/2606.01014)

**<font color=#1a73e8>作者：</font>** Gyojin Han, Junmo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address text-based 3D human motion editing, where the goal is to preserve the style and structure of a source motion while applying edits described in natural language. The release of the MotionFix dataset has spurred active research into training-based diffusion models that directly generate an edited motion from a source motion and a text instruction. While previous works have focused primarily on learning when an edit should occur temporally, our goal is to create a model that understands not only this temporal aspect but also which specific joints are responsible for the change. Targeting this, we propose a novel architecture and a complementary auxiliary task to aid its training. Our architecture consists of two axis-anchored transformers, which extract distinct features along the joint and time dimensions respectively, and a cross-axis fusion block that integrates these representations. We further introduce an auxiliary task that trains the joint-anchored transformer to regress the Soft-DTW distance between source and target joint rotations. This objective teaches the module to understand which joints to modify and which to preserve. Through comprehensive experiments on the MotionFix dataset, we demonstrate that our method significantly improves semantic alignment with both the text instruction and the source motion, as well as the overall fidelity of the generated motion, achieving state-of-the-art results.

---


### 265. [Tackling the Root of Misinformation by Teaching Laypeople about Logical Fallacies via Socratic Questioning and Critical Argumentation](https://arxiv.org/abs/2606.01020)

**<font color=#1a73e8>作者：</font>** Minjing Shi, Junling Wang, Jingwei Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying logical fallacies in everyday discourse is challenging for many people. This challenge is amplified in the era of Large Language Models (LLMs), where malicious agents can deploy fallacious arguments to disseminate misinformation at scale. In this work, we explore the potential of LLMs as part of the solution. We introduce LFTutor, an intelligent tutoring system which uses LLMs to tutor laypeople and help them learn about logical fallacies. LFTutor integrates intent-driven Socratic questioning and critical argumentation principles to actively engage learners to reflect on their reasoning. Through both automatic and human evaluations, we demonstrate that LFTutor significantly outperforms baseline LLMs lacking these pedagogical strategies. This work highlights the promise of combining LLMs with pedagogical scaffolding to foster critical thinking and argument literacy in the age of AI.

---


### 266. [Learning Neural Deformation Representation for 4D Dynamic Shape Generation](https://arxiv.org/abs/2606.01021)

**<font color=#1a73e8>作者：</font>** Gyojin Han, Jiwan Hur, Jaehyun Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent developments in 3D shape representation opened new possibilities for generating detailed 3D shapes. Despite these advances, there are few studies dealing with the generation of 4D dynamic shapes that have the form of 3D objects deforming over time. To bridge this gap, we focus on generating 4D dynamic shapes with an emphasis on both generation quality and efficiency in this paper. HyperDiffusion, a previous work on 4D generation, proposed a method of directly generating the weight parameters of 4D occupancy fields but suffered from low temporal consistency and slow rendering speed due to motion representation that is not separated from the shape representation of 4D occupancy fields. Therefore, we propose a new neural deformation representation and combine it with conditional neural signed distance fields to design a 4D representation architecture in which the motion latent space is disentangled from the shape latent space. The proposed deformation representation, which works by predicting skinning weights and rigid transformations for multiple parts, also has advantages over the deformation modules of existing 4D representations in understanding the structure of shapes. In addition, we design a training process of a diffusion model that utilizes the shape and motion features that are extracted by our 4D representation as data points. The results of unconditional generation, conditional generation, and motion retargeting experiments demonstrate that our method not only shows better performance than previous works in 4D dynamic shape generation but also has various potential applications.

---


### 267. [Data Collection for Training Quality-Control AI in Carpet Manufacturing](https://arxiv.org/abs/2606.01023)

**<font color=#1a73e8>作者：</font>** Akbar Erkinov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual inspection remains the dominant quality-control practice in woven and tufted carpet production, yet it is slow, subjective, and inconsistent at the line speeds and widths of modern looms. We present a design proposal for an in-line machine-vision system whose primary purpose is twofold: to inspect the carpet web in real time and, equally importantly, to systematically collect and label images of defect patterns so that increasingly capable quality-control models can be trained over the life of the this http URL proposal is grounded in a concrete industrial setting: a Six Sigma (DMAIC) project at a woven-carpet production facility that anticipated a production bottleneck following the installation of additional weaving machines, with a substantial baseline defect rate and significant financial exposure associated with quality failures. We describe an imaging subsystem based on synchronized line-scan cameras with combined bright-field and grazing illumination, derive the resolution and throughput requirements needed to resolve fine structural defects across a multi-metre web, and define a carpet-specific defect this http URL then lay out a staged modelling strategy that begins with unsupervised anomaly detection trained on defect-free material, following the paradigm exemplified by the carpet category of the MVTec Anomaly Detection benchmark, and matures through a human-in-the-loop annotation flywheel into supervised detection and segmentation models. Finally, we connect detection performance to the DMAIC objectives, showing how reductions in escaped defects translate into improved process quality and process sigma levels. The contribution is an end-to-end, deployable blueprint that treats data collection as a first-class engineering objective rather than an afterthought.

---


### 268. [DSL-LLaDA: Scaling Continuous Denoising to 8B Masked Diffusion LMs](https://arxiv.org/abs/2606.01024)

**<font color=#1a73e8>作者：</font>** Longxuan Yu, Yunshu Wu, Yu Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete Masked diffusion language models generate text by iterative parallel decoding, but few-step decoding suffers from a tradeoff between length and quality: with a fixed step budget, standard methods can generate a short, high-quality output, or they can produce long but repetitive text. Continuous denoising can sidestep this tradeoff by evolving all positions jointly in embedding space, but building such a model from scratch at scale remains an open problem. We show that a pretrained masked DLM can instead be lightly adapted to support continuous embedding-space denoising. Starting from LLaDA-8B-Instruct, we continue-pretrain for only 1,000 steps with Discrete Stochastic Localization (DSL), replacing binary masking with continuous per-token Gaussian noise as a soft mask. The adapted model supports continuous inference that evolves all positions jointly in embedding space and defers hard token commitment to the final step. On zero-shot summarization at low step budgets (<=16 forward passes), DSL-LLaDA-SDE achieves the best ROUGE-1 on all four benchmarks and largely avoids the premature-termination / repetition tradeoff of iterative unmasking. The same adaptation also yields selective noisy-state robustness: the model corrects corrupted tokens while preserving clean ones. Control experiments using standard masked diffusion training with the same compute demonstrate neither behavior.

---


### 269. [MedGym:A Unified Continuous-Time Benchmark for Dynamic Medical Treatment Reinforcement Learning](https://arxiv.org/abs/2606.01028)

**<font color=#1a73e8>作者：</font>** Yuepeng Wang, Ken Kawano, Yongqi Zhou 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical treatment recommendation poses several challenges to reinforcement learning (RL): patient physiology evolves in continuous time, measurements and interventions are performed at irregular intervals, and treatment effects vary substantially across individuals. Existing RL formulations and simulated environments, however, are based on discrete-time MDP or POMDP abstractions with fixed or pre-specified decision intervals. Thus, it remains difficult to evaluate whether RL methods can handle time-interval-dependent disease progression, personalized treatment response, and safety between consecutive measurement points. To address this gap, we introduce MedGym, a benchmark environment for dynamic treatment recommendation. MedGym models longitudinal patient evolution in a continuous-time framework and constructs a configurable medical RL benchmark from clinical data by using Physics-Informed Neural Networks. The resulting benchmark supports both offline and online RL, and enables direct comparison between discrete-time and continuous-time methods under irregular treatment timing and patient-specific dynamics. Besides, MedGym supports evaluation from clinically important perspectives, including personalization, trajectory-level safety, and the performance gap between model-based offline learning and online deployment. By providing a standardized and configurable benchmark for continuous-time dynamic treatment, MedGym aims to facilitate more realistic and informative evaluation of medical RL methods.

---


### 270. [TriLens: Per-Layer Logit-Lens Entropy for White-Box Hallucination Detection](https://arxiv.org/abs/2606.01033)

**<font color=#1a73e8>作者：</font>** Bohan Yang, Yijun Gong, Zhi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model hallucinates, the final answer is wrong, but the mistake is not necessarily invisible inside the model. Different internal pathways may remain uncertain, disagree in how quickly they sharpen, or commit to competing continuations before the output is produced. We introduce TriLens, a white-box detector that turns this intuition into a compact representation: at every layer, it reads the multi-head self-attention output, the feed-forward output, and the residual stream through the model's own logit lens, then records only the entropy of each readout. The resulting 3L-dimensional trajectory describes how certainty forms across depth and across modules, without storing high-dimensional hidden states or sampling multiple generations. This simple signal yields a strong detector across instruction-tuned LLMs and QA benchmarks, and our analyses show that the three module-wise entropy trajectories provide complementary evidence. TriLens suggests that hallucination detection can benefit from tracking how internal computation settles, not only what the final layer predicts.

---


### 271. [OPD+: Rethinking the Advantage Design for On-Policy Distillation](https://arxiv.org/abs/2606.01039)

**<font color=#1a73e8>作者：</font>** Hanyang Zhao, Haoxian Chen, Han Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is a widely used technique to transfer capabilities from capable teacher language models to the base student models, and can be formulated in a reinforcement learning style objective using student generated rollouts. Yet, despite the divergence reward being dependent on student model likelihood, existing works usually adopt a stop gradient design primarily for stability, which makes the resulting advantage estimation questionable. In this work, we provide a generic optimization framework based on f-divergence between the student and teacher, and mathematically revisit whether such design space is valid. We prove that general stop-gradient operation would lead to biased estimates of the reward objective and corresponding gradient for general divergence functions. We propose OPD+, the corrected version of OPD that demonstrates improved performance over the baseline KL approach and also supports the choice of various f-divergence. We validate our findings on mathematical reasoning and tool-use benchmarks.

---


### 272. [Ask4VG: Risk-Aware Question Selection for Reducing Prior-Driven Answers in Medical VQA](https://arxiv.org/abs/2606.01044)

**<font color=#1a73e8>作者：</font>** Xiaorong Zhu, Qiang Li, Zibo Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical visual question answering requires models to ground their responses in image evidence, because visually unsupported answers can mislead downstream interpretation. However, many medical VQA questions are generic, template-like, or highly similar in form, which can encourage models to learn question-answer shortcuts instead of image-dependent reasoning and thereby increase the risk of hallucinated responses. We propose Ask4VG, a label-free pilot framework for risk-aware question selection. Ask4VG estimates question-induced hallucination risk through counterfactual visual probing: the same question is asked under the original image, a perturbed image, a blank image, and a mismatched image, and the resulting answer relations are converted into weak supervision for a counterfactual risk estimator. The learned estimator then reranks candidate question rewrites to favor intent-preserving questions that are less invariant to missing or mismatched visual evidence before final answer generation. On VQA-RAD with Qwen2-VL-2B-Instruct, prompt-only rewriting increases counterfactual risk, whereas predicted-risk reranking reduces held-out risk from 0.658 to 0.623 and improves exact accuracy from 0.337 to 0.356. A 300-sample PMC-VQA external check shows the same direction of risk reduction with a small accuracy gain. These results suggest that question selection is a promising complement to response-level hallucination mitigation for reliable medical VQA.

---


### 273. [Child-directed speech facilitates production, not comprehension, in BabyLMs](https://arxiv.org/abs/2606.01045)

**<font color=#1a73e8>作者：</font>** Bastian Bunzeck, Sina Zarrieß  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent studies suggest that child-directed speech is not conducive to language learning in BabyLMs. However, current evaluations focus predominantly on comprehension and not production, which is central to usage-based theories of language acquisition which argue how CDS facilitates early language use through constructional ''frames'' (frequent lexical patterns with open slots). We introduce a novel generation-based evaluation inspired by such theories in form of a frame-completion task, and compare Llama models trained with CDS, the BabyLM corpus, and web-crawl data (FineWeb-edu) on comprehension benchmarks and our novel framework. Our results reveal a clear dissociation between models' comprehension and production capabilities: while FineWeb-trained models excel at minimal pairs, CDS-trained models produce grammatical completions substantially earlier in training and concentrate probability mass on appropriate slot-fillers. These findings show that comprehension benchmarks underestimate what CDS affords to BabyLMs.

---


### 274. [Decoupled Residual Denoising Diffusion Models for Unified and Data Efficient Image-to-Image Translation](https://arxiv.org/abs/2606.01048)

**<font color=#1a73e8>作者：</font>** Ziyue Lin, Jiahe Hou, Hongyu Xia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Decoupled Residual Denoising Diffusion models (DRDD) for unified and data-efficient image-to-image (I2I) translation. While diffusion models have advanced I2I translation in terms of quality and diversity, we uncover a previously under-explored property in diffusion models. Crucially, beyond its conventional role of manifold lifting (i.e., moving data off low-dimensional manifolds), injecting Gaussian noise facilitates domain harmonization by implicitly aligning feature distributions across domains, a property particularly advantageous for unified I2I translation. However, existing diffusion models prematurely erode this harmonization effect, as noise and residuals are simultaneously removed in a single coupled diffusion process. To address this, DRDD decouples the diffusion process into two sequential and independent diffusion stages: (1) a stochastic noise diffusion for domain harmonization and manifold lifting, and (2) a deterministic residual diffusion that learns the core semantic mapping entirely within the fixed-noise domain. This decoupling preserves harmonization and manifold lifting effects throughout the transformation, substantially simplifying the learning of unified mappings across diverse tasks and domains. Notably, the noise diffusion stage is trained exclusively on abundant, unpaired target-domain images, greatly improving data efficiency. Comprehensive theoretical and empirical analysis demonstrates that DRDD is broadly compatible with mainstream diffusion models and consistently delivers robust, unified I2I translation, even under limited paired data. Our code is available at this https URL.

---


### 275. [TextFake: Benchmarking AI-Generated Image Detection on Text-Rich Images](https://arxiv.org/abs/2606.01050)

**<font color=#1a73e8>作者：</font>** Yuning Zhang, Changtao Miao, Mingyu Liao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent AI-generated image (AIGI) detectors perform well on natural-image benchmarks, but their behavior on text-rich forgeries, such as fabricated screenshots, documents, and news pages prevalent in misinformation, remains untested. We introduce TextFake, a 20,000-image benchmark for text-rich AIGI detection spanning 28 languages, 4 topic categories, and 2 scene modalities. Fake images are synthesized via a four-stage pipeline that annotates real images along three controlled dimensions and generates counterparts through distribution-aligned structured prompting, ruling out covariate shortcuts. Zero-shot evaluation of 14 specialized detectors and 3 frontier VLM APIs reveals a large systematic gap: no method exceeds 80% accuracy, with some dropping over 60% from natural-image benchmarks. Diagnostic evaluations identify three failure modes: the Text Density Curse, where dense glyphs overwhelm low-level detectors; Cloaking via Rendering Fidelity, where stronger text rendering suppresses enerative artifacts; and Threshold Collapse, where routine perturbations drive detectors toward chance-level performance.

---


### 276. [Interaction-Limited Safe Continuous-Time RL for Dynamical Medical Treatment](https://arxiv.org/abs/2606.01051)

**<font color=#1a73e8>作者：</font>** Xun Shen, Yuepeng Wang, Akifumi Wachi 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic medical treatment requires deciding treatment intensity and intervention timing, while patient states evolve continuously and adverse events may occur between clinical interactions. Most existing treatment learning methods assume fixed schedules or enforce safety only at discrete decision points. We propose Interaction-Limited Safe Continuous-Time Reinforcement Learning, a framework that jointly optimizes treatment administration and clinical interaction timing under trajectory-level safety constraints. Our key idea is to reformulate the continuous time treatment problem as an option-based semi-Markov decision process, where each option specifies a continuous-time treatment policy and its duration. We develop a safety-tightening mechanism showing that suitably constructed constraints at interaction times guarantee safety over the full continuous-time trajectory with high probability. We further establish finite-sample guarantees for policy learning from logged treatment trajectories and introduce a practical data-driven conservative surrogate. Experiments show that the proposed adaptive interaction-timing mechanism improves both safety and treatment effectiveness over equidistant interaction schemes across different safe policy optimization methods.

---


### 277. [AnyEdit++: Adaptive Long-Form Knowledge Editing via Bayesian Surprise](https://arxiv.org/abs/2606.01053)

**<font color=#1a73e8>作者：</font>** Bowen Tian, Caixue He, Jiemin Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Editing complex, long-form knowledge in Large Language Models remains a significant challenge due to the difficulty of maintaining generation coherence. Existing autoregressive methods like AnyEdit alleviate length constraints but rely on Fixed-window Chunking, which disregards logical structure and compromises consistency. To address this, we present AnyEdit++, a structure-aware framework incorporating Bayes-Chunk, an adaptive segmentation mechanism that dynamically identifies semantic boundaries based on Bayesian Surprise. We underpin this approach with a theoretical framework establishing two key principles: (1) Structural Independence: we prove that cross-segment interference is minimized when anchor keys are geometrically orthogonal (a condition naturally satisfied by our surprisal-based boundaries but violated by fixed windows), and (2) Causal Locality: we demonstrate that updates injected at these semantic peaks yield strictly superior control compared to arbitrary split points. Extensive experiments across mathematical reasoning, code generation, and narrative tasks demonstrate that AnyEdit++ achieves superior performance and robustness compared to state-of-the-art baselines, validating that structural awareness is critical for effective long-form knowledge editing.

---


### 278. [MindClaw: Closed-Loop Embodied Mental-State Reasoning for Precision Intervention](https://arxiv.org/abs/2606.01063)

**<font color=#1a73e8>作者：</font>** Ruoxuan Zhang, Qiaoqiao Wan, Zhengguang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM) enables an agent to reason about another actor's beliefs, goals, and intentions, which is essential for human-centered embodied assistance. Existing ToM benchmarks have advanced text and multimodal mental-state recognition, but they mostly evaluate offline question answering or final action prediction. They do not fully test whether an embodied agent can stay connected to a changing environment, update actor-specific beliefs, decide when reasoning is needed, and intervene only when help is useful. Building on MindPower, we extend robot-centric ToM reasoning to a real-time closed-loop setting and introduce MindClaw, a framework for embodied mental-state reasoning with precision intervention. MindClaw connects multi-source inputs, belief memory, an embodied cognitive trigger skill, mental reasoning, and action generation, allowing the agent to output helpful actions at the right time while remaining silent when intervention is unnecessary. Experiments show that direct VLM baselines struggle with task awareness and intervention calibration, while MindClaw achieves the best overall performance, demonstrating the importance of trigger-skill optimization for closed-loop embodied ToM assistance.

---


### 279. [Before the Model Learns the Bug:Fuzzing RLVR Verifiers](https://arxiv.org/abs/2606.01066)

**<font color=#1a73e8>作者：</font>** Jaideep Ray  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) replaces human preference labels with executable reward functions such as math answer checkers, JSON tool-call validators, and code unit-test harnesses. That makes the reward partly a software artifact: if the verifier is wrong, optimization can learn the bug. We study this failure mode with a lightweight verifier-fuzzing framework that generates adversarial completions, compares buggy and stricter reference verifiers, logs paired decisions, and reports false-positive, false-negative, disagreement, exploit, and uncertainty metrics.

---


### 280. [A Multiscale Network with Supervised Contrastive Learning for Real-Time Facial Emotion Recognition](https://arxiv.org/abs/2606.01069)

**<font color=#1a73e8>作者：</font>** Rejoy Chakraborty, Archisman Adhikary, Chayan Halder 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time emotion recognition from facial expressions is a challenging task, particularly in video-based scenarios where multiple emotional states may occur over time. The difficulty increases further due to the fact that each emotional state is associated with facial expressions that vary significantly across individuals. The change of facial expressions portraying emotional state is not discrete, but rather continuous, which is very challenging to represent through computational aids. A system with the ability to detect variations in facial expressions can have a significant impact on determining the emotional state of an individual. Such a system can be very beneficial for psychologists during counseling by providing additional insights into the emotional state of a subject. In this paper, a deep learning-based system is presented to detect emotional changes in real-time video of a person by modeling the change in facial expressions. The current study is conducted on a standard dataset for training of the deep learning system and the system has provided very satisfactory outcomes in this respect.

---


### 281. [When Is 0.1% Enough? Analyzing the Combined Effects of Dimensionality Reduction and Quantization on Text Embedding Compression](https://arxiv.org/abs/2606.01074)

**<font color=#1a73e8>作者：</font>** Riku Kisako, Hayato Tsukagoshi, Ryohei Sasano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent high-performing text embedding models often output high-dimensional real-valued vectors, resulting in substantial storage and computational costs. To address this issue, compression methods based on dimensionality reduction or quantization have been proposed; however, the effects of combining dimensionality reduction and quantization have not been sufficiently investigated. In this paper, we systematically examine the effectiveness of compressing text embeddings by combining dimensionality reduction and quantization, using four MTEB task families and four pretrained embedding models. The experimental results demonstrate that combining dimensionality reduction and quantization enables substantially stronger compression than using either method alone, that in some settings embeddings can be reduced to as little as 0.1% of their original size with almost no performance degradation, and that the optimal compression strategy depends on the task.

---


### 282. [Non-Vacuous Certification of Transport MCMC via Oscillation-Controlled Normalizing Flows](https://arxiv.org/abs/2606.01078)

**<font color=#1a73e8>作者：</font>** Jun Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transport MCMC trains a normalizing flow to precondition Metropolis--Hastings proposals, achieving high empirical efficiency on challenging posteriors; yet no prior work produces a numerically non-vacuous, rigorous spectral-gap bound for such samplers. We establish the first such bounds. For independence MH on the banana family we certify (\gamma^\ast = 0.828) at (D = 2) (covering in the original space) and (\gamma^\ast \ge 7.6\times 10^{-4}) at (D = 5) (covering in an analytically unwarped Gaussian space with a grid-certified gradient bound under the stated numerical Lipschitz certification), both rigorous at 95% confidence. The framework rests on three pillars: (i) spectral normalization with reduced scale clips constrains the flow Lipschitz constant from (10^{47}) to (10^4); (ii) a coverage-based empirical oscillation bound replaces the vacuous analytical bound with a data-dependent certificate; and (iii) oscillation-regularised training cuts the empirical oscillation by 60--90% at no cost to density fit, extending practical certificates through (D = 20) ((\gamma^\ast \ge 1.7\times 10^{-4})). Tests on four further targets (Gaussian mixture, shear-building, Neal's funnel, Bayesian logistic regression) identify three precise barriers: boundary curvature, target stiffness, and tail-coverage mismatch. An affine-vs-spline comparison shows that simpler architectures yield tighter certificates at identical NLL, inverting the usual expressiveness hierarchy.

---


### 283. [Chameleon: Style-Content Disentangled Framework for Cross-Domain Object Compositing](https://arxiv.org/abs/2606.01079)

**<font color=#1a73e8>作者：</font>** Sukhun Ko, Soo Ye Kim, Jihyong Oh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image compositing aims to seamlessly insert a foreground object into a background image, and recent advances in diffusion models have significantly enhanced the quality, especially when the foreground and background images come from the same domain (e.g., natural images). However, cross-domain compositing, where the foreground and background come from different domains, is relatively underexplored and remains challenging because the model must preserve the foreground object's identity while stylizing it to match the background domain. Existing cross-domain compositing approaches largely rely on training-free blending and refinement strategies. This is partly due to the lack of large-scale paired datasets for cross-domain compositing, limiting the development of training-based solutions. As a result, they are limited to tone-level alignment and often produce style-inconsistent or overstylized results. To overcome such limitations, we construct ChameleonDataset, the first large-scale training dataset for cross-domain compositing, with a comprehensive evaluation benchmark, built through a scalable data construction pipeline. Building on this, we propose Chameleon, a novel two-stage training-based cross-domain compositing framework. In the first stage, we propose Joint Hard Contrastive Learning (JHCL) to train ChameleonEncoder, which effectively disentangles style and content representations. In the second stage, we introduce Spatio-Temporal Attention Gating (STAG) into a diffusion transformer for effective stylization, adaptively regulating how style tokens from the first-stage encoder are injected across spatial and temporal dimensions. Our method outperforms state-of-the-art in-domain and cross-domain compositing models, sequential pipelines and commercial models, achieving improvements in both compositional plausibility and stylistic fidelity.

---


### 284. [ThinkSwitch: Context Distillation with LoRA and Weight Interpolation for Specific-Purpose Reasoning Tasks](https://arxiv.org/abs/2606.01080)

**<font color=#1a73e8>作者：</font>** Dhruv Saini, Rohan Pandey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models often improve on difficult tasks by spending inference-time compute on a reasoning trace before producing the final answer. That extra computation can be useful, but it also raises latency, token cost, and deployment complexity. We introduce \textbf{ThinkSwitch}, a low-compute procedure for co-training paired instruct and thinking checkpoints. Starting from compatible Qwen3-4B instruct and thinking models, each iteration asks the thinking checkpoint to generate answers, removes the reasoning trace, distills the answer-only pairs into the instruct checkpoint with QLoRA, and reconstructs a thinking checkpoint with spherical weight interpolation. The only human-supplied inputs are task prompts; the labels are generated by the model itself. On a 30-question AIME 2026 evaluation, ThinkSwitch improves the instruct checkpoint from 10/30 to 20/30 and the thinking checkpoint from 14/30 to 22/30. On a 30-question PubMedQA subset, it improves the instruct checkpoint from 13/30 to 18/30 and the thinking checkpoint from 18/30 to 25/30. The complete experiment uses 15 training prompts per domain and costs \$2.86 on a single cloud RTX 3070. The results are small-scale, but they indicate that targeted distillation loops can move part of the benefit of explicit reasoning into weights while preserving a separate thinking mode.

---


### 285. [Decision-Focused On-Policy Learning for Contextual Linear Optimization with Partial Feedback](https://arxiv.org/abs/2606.01081)

**<font color=#1a73e8>作者：</font>** Wyame Benslimane, Tinghan Ye, Pascal Van Hentenryck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning (DFL) trains predictive models by optimizing downstream decision quality rather than standalone prediction accuracy. For contextual linear optimization, most existing DFL methods assume offline data and full observations of the objective cost vector. We develop an on-policy learning method for sequential contextual linear optimization under partial feedback, generalizing the standard bandit feedback setting. Our method learns a stochastic predict-then-optimize policy that samples a cost-vector prediction from a conditional distribution and solves the resulting downstream linear optimization problem. To update this distributional model, we introduce a two-component hybrid gradient estimator. The first component is a score function estimator, which provides an unbiased but potentially high-variance policy gradient estimate. The second is a decision-focused plug-in component that uses an auxiliary nuisance estimate of the latent cost vector to exploit the downstream optimization structure, becoming more informative as the estimate improves. We prove an $\mathcal{O}(T^{-1/2})$ bound on the average squared policy-gradient norm, matching the standard non-convex SGD rate. Experiments on top-$k$ selection, shortest path, combinatorial pricing, and a real-data energy-scheduling benchmark show that the hybrid gradient approach achieves lower cumulative regret than contextual-bandit-style baselines across all benchmarks, using both Gaussian and richer conditional generative models. Code is available at this https URL.

---


### 286. [MViewRouter: Internalizing Geometric Equivariance via Multi-view Alternating Attention for Combinatorial Routing](https://arxiv.org/abs/2606.01084)

**<font color=#1a73e8>作者：</font>** Shiyan Liu, Bohan Tan, Yaoxin Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combinatorial routing problems such as the Traveling Salesman Problem (TSP) and the Capacitated Vehicle Routing Problem (CVRP) are fundamental NP-hard problems with broad real-world applications. While recent deep reinforcement learning methods have shown promising performance, they typically handle geometric symmetries only through data augmentation, resulting in inconsistent decisions and limited generalization. To address this issue, we propose MViewRouter, a multi-view framework that internalizes geometric equivariance as a structural inductive bias to achieve invariant decision-making across routing problem variants. Our approach introduces a Multi-view Alternating Attention (MAA) mechanism that enables parallel processing over the $D_4$ symmetry group, alternating between intra-view relational modeling and inter-view feature alignment. Furthermore, we optimize the policy via Collective Policy Gradient Aggregation (CPGA), leveraging consensus gradients from multiple symmetric views to stabilize training and accelerate convergence. Experiments on TSP and CVRP benchmarks, as well as real-world TSPLIB instances, demonstrate that MViewRouter achieves competitive solution quality and strong zero-shot generalization.

---


### 287. [Strong Stochastic Flow Maps](https://arxiv.org/abs/2606.01086)

**<font color=#1a73e8>作者：</font>** Sam McCallum, Zander W. Blasingame, Timothy Herschell 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow and diffusion models generate high-quality samples in many modalities; however, many network evaluations are required during inference due to numerical integration of an underlying differential equation. Flow maps alleviate this problem by learning the solution map of the differential equation directly, enabling few-step sampling. Yet, current methods are restricted to approximating the solution map of ODEs. These methods can be used to learn the transition kernel of an SDE, thereby obtaining a solution map that recovers the marginal distributions of the process (weak convergence) rather than the solution path (strong convergence). We propose Strong Stochastic Flow Maps (SSFMs) as a novel framework for learning the strong solution map of additive-noise SDEs, directly generalizing deterministic flow maps to the stochastic setting. Further, a polynomial approximation to Brownian motion is introduced and shown to converge pathwise. These results enable a simulation-free training objective for the solution map of diffusion models. We demonstrate that SSFMs outperform previous stochastic flow map methods on image generation and enable few-step sampling of molecular systems.

---


### 288. [A Fiber Criterion for Representation Identifiability in Supervised Learning](https://arxiv.org/abs/2606.01092)

**<font color=#1a73e8>作者：</font>** Vasileios Sevetlidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised learning evaluates predictors through their input-output behavior. When a predictor is implemented as a composition $f=c\circ h$, supervised evidence constrains the composite map $f$ but need not determine the representation-head factorization $(h,c)$. This paper formalizes the resulting representation-level identifiability problem: for a class of admissible representation-head pairs, a representation property is identifiable from the induced predictor exactly when it is constant on the fibers of the projection $(h,c)\mapsto c\circ h$, equivalently when it descends to a well-defined property of the predictor. Predictor-preserving augmentation gives a canonical obstruction: auxiliary information can be appended to a representation while the head ignores it, leaving the predictor unchanged but altering properties such as minimality, compression, invariance, equivariance, nuisance information, or semantic accessibility. This construction separates representation identifiability from optimization and finite-sample estimation. Finite-sample diagnostics illustrate, rather than prove, the criterion: exact algebraic witnesses hold the predictor fixed while changing representation diagnostics, and matched-performance Waterbirds models show that different constraints can select different representations at similar supervised performance. The results clarify that representation-level claims require assumptions, objectives, measurements, or inductive biases beyond supervised predictive behavior alone.

---


### 289. [CAREAgent: Clinical Agent with Structured Reasoning and Tool-Integrated for Order Generation](https://arxiv.org/abs/2606.01094)

**<font color=#1a73e8>作者：</font>** Ruihui Hou, Ziyue Huai, Chennuo Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical order generation serves as a critical bridge between clinical decision-making and real-world practice, translating medical decisions into concrete and executable orders. Existing agents mainly focus on coarse-grained decisions and overlook the fine-grained, executable information required for clinical orders. To address this gap, we propose CAREAgent, an agent for clinical order generation. To support its training, we introduce a two-stage agentic reasoning data construction method. First, we design an agent framework that constructs verifiable reasoning trajectories aligned with realistic clinical tool usage. Second, we filter reasoning trajectories by format compliance, order validity, and clinical plausibility. Building on the constructed data, the model is first trained via supervised fine-tuning to acquire fundamental reasoning formats and medical knowledge, and is subsequently optimized through reinforcement learning with multi-dimensional reward functions to enhance complex clinical reasoning capabilities. Experiments on multiple benchmarks demonstrate the effectiveness of CAREAgent. On ClinicalBench (unseen during training), CAREAgent improves the F1 score by 5.05%, 2.09%, and 0.86% over the single-agent, multi-agent, and agentic reasoning methods, respectively.

---


### 290. [Dual-Route Top-K Retrieval with 1v1 VLM Reranking for the CoVR-R](https://arxiv.org/abs/2606.01097)

**<font color=#1a73e8>作者：</font>** Yuyang Sun, Yongliang Wu, Xingyu Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe \emph{Dual-Route Top-K Retrieval with 1v1 VLM Reranking} for the CoVR-R challenge. The method treats composed video retrieval as two coupled problems: finding a sufficiently complete top-k candidate set, and then safely deciding whether any candidate should replace a strong current top-1. We first improve the reasoning/text seed with a VLM slot selector over existing candidates, without introducing DFN visual retrieval. We then add a visual route from contact-sheet embeddings using DFN-H/DFN-L. The routes are merged into a top-10 candidate set, after which a VLM final reranker performs conservative 1v1 comparisons between the current top-1 and each challenger. On the hidden test split, the final system reaches 95.28 R@1, 97.47 R@5, 98.48 R@10, and 99.66 R@50. The main lesson is that CoVR-R benefits more from recall-selection decoupling than from broad text reranking or direct multi-candidate VLM classification.

---


### 291. [Adaptive Dense Evidence Refinement for Video Relational Reasoning for VRR-QA Challenge](https://arxiv.org/abs/2606.01104)

**<font color=#1a73e8>作者：</font>** Yuyang Sun, Yongliang Wu, Xingyu Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> VRR-QA evaluates whether video-language systems can infer spatial, temporal, viewpoint, depth, and visibility relations that are not always resolved by a single frame. We present an inference-only system built around adaptive test-time computation. The system first answers each question with a direct video-language model pass, then uses multiple lightweight views to find unstable questions. Only these difficult questions are routed to a high-budget dense evidence module that constructs timestamped frame observations, relation-specific probes, candidate verification, and conservative temporal aggregation. This design separates two problems that are often confused in video question answering: finding plausible alternative answers and deciding when a current answer should actually be changed. On the test split, the final system obtains 90.07 average accuracy and 87.81 macro average accuracy. The report focuses on the final test system and the implementation settings required to reproduce the adaptive dense verifier.

---


### 292. [LeAP: Learnable Adaptive Permutation for Feature Selection in Heterogeneous and Sparse Recommender Systems](https://arxiv.org/abs/2606.01111)

**<font color=#1a73e8>作者：</font>** Yihong Huang, Chen Chu, Fei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern industrial recommender systems rely on thousands of heterogeneous features -- ranging from low-dimensional scalars (e.g., statistical value) to high-dimensional embeddings (e.g., user-id embeddings, MLP representations) -- to achieve high-precision predictions. Given the immense computational costs associated with training, efficient feature selection is critical. However, existing methods encounter three primary bottlenecks: (1) they typically assume uniform feature dimensions or require costly mapping to a fixed size; (2) they struggle with extreme sparsity, where the majority of features (e.g., 99%+) remain at default values; and (3) traditional permutation-based approaches are computationally prohibitive in large-scale settings.
To address these challenges, we propose LeAP (Learnable Adaptive Permutation), a novel, model-agnostic plug-in module for feature selection. LeAP transforms the inefficient random permutation process into a learnable mechanism, significantly accelerating the evaluation of feature importance. In addition, we introduce an adaptive regularization strategy tailored for heterogeneous dimensions and extreme sparsity, enabling superior feature importance ranking results across asymmetric input spaces. Experiments on four public recommendation datasets demonstrate that LeAP achieves state-of-the-art performance. Furthermore, LeAP has been deployed in a large-scale industrial search ranking model with over a billion daily requests and a 2TB model parameter scale. In this real-world scenario involving 12,000+ total feature dimensions, LeAP successfully identified and removed over 3,600 redundant dimensions without performance degradation, which is 2 to 10 times the ability of compared baseline methods.

---


### 293. [R^3: Composed Video Retrieval via Reasoning-Guided Recalling and Re-ranking](https://arxiv.org/abs/2606.01113)

**<font color=#1a73e8>作者：</font>** Zixu Li, Yupeng Hu, Zhiheng Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The CoVR-R challenge evaluates composed video retrieval, where a system must retrieve a target video from a large gallery given a reference video and a textual edit instruction. This setting is not a standard video-text retrieval problem: the query is defined by both the visual evidence in the source video and the transformation implied by the edit. A strong embedding model can provide scalable candidate recall, but it may under-express target-side consequences such as state changes, action replacement, object preservation, or temporal consistency. A pairwise multimodal reranker can verify such details more directly, but exhaustive reranking over the full gallery is computationally infeasible. We present $\mathbb{R}^3$, a zero-shot composed video retrieval pipeline built around Reasoning-guided Recalling and Reranking. The core idea is to turn the source-edit query into a reasoning-grounded retrieval program rather than treating the edit text as a short caption. First, the model generates a reasoning trace that describes the expected target video after applying the edit. Then the trace is encoded together with the source video as a reasoning-augmented query, and its retrieval score is fused with the base composed query through an agreement-gated residual rule. At last, a re-ranker verifies the recalled candidates with direct source-candidate comparison. Experiments have demonstrated the effectiveness of our method in addressing this challenge. Codes are available on this https URL.

---


### 294. [HASTE: Hardware-Aware Dynamic Sparse Training for Large Output Spaces](https://arxiv.org/abs/2606.01117)

**<font color=#1a73e8>作者：</font>** Nasib Ullah, Jinbin Zhang, Jean Lucien Randrianantenaina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme multi-label classification (XMC) involves learning models over large output spaces with millions of labels, making the output layer a memory-compute bottleneck. While sparsity-based methods reduce arithmetic complexity, they often fail to yield proportional speedups due to irregular memory access, poor hardware utilization, or reliance on auxiliary architectural components in long-tailed regimes. We introduce group-shared fixed fan-in sparsity, a semi-structured output-layer design in which semantically related labels share a sparse input pattern while retaining independent weights. This grouping introduces a task-aligned inductive bias -- encouraging related labels to share feature subsets -- while reducing index memory overhead, increasing feature reuse across labels, and enabling efficient GPU execution via custom CUDA kernels that leverage modern accelerator primitives. As an alternative to auxiliary objectives, we exploit the long-tailed structure of XMC by decomposing the output layer into a small dense head over frequent labels and a group-shared sparse tail over the remainder, providing an informative gradient pathway while preserving the memory benefits of sparsity. Through kernel-level microbenchmarking, we show that group-shared fixed fan-in translates arithmetic reductions into practical wall-clock gains, achieving up to $4.4\times$ speedup in the forward pass and up to $25\times$ speedup in backward passes over standard fixed fan-in sparsity, while operating within a few percent of a FLOPs-matched dense bottleneck. Across large-scale XMC benchmarks, our approach matches or improves precision@k over prior sparse baselines, while narrowing the performance gap to dense.

---


### 295. [Rank-Aware Quantile Activation for Motion-Robust Crop Segmentation in UAV Imagery](https://arxiv.org/abs/2606.01118)

**<font color=#1a73e8>作者：</font>** Abinav Kiran, Sravan Danda, Aditya Challa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion blur from high-speed UAV acquisition de-grades semantic segmentation on rare texture-dependent classes with high agronomic value. Standard CNNs rely on high-frequency magnitude features that blur destroys, causing statistical erasure of minority signals. We propose Dual Quantile Activation (QAct), a rank-aware block replacing magnitude gating with instance-level rank normalization. Evaluated onAgriculture-Vision 2021 across zero-shot and blur-supervised regimes at multiple severities, QAct is the dominant architectural factor: it delivers consistent mIoU gains over ReLU across both regimes and all severities, with strongest gains on rare structural and texture-dependent classes. Some dominant classes (water,planter skip) show mixed per-class performance under distillation. At moderate blur, zero-shot QAct outperforms distillation-trained ReLU; across all severities, Distill-QAct achieves best performance, confirming rank aware activation and blur-domain training are complementary robustness sources.

---


### 296. [A Per-Component Diagnostic Protocol for Neural HJB-PIDE Solvers under Control-Dependent Lévy Jumps](https://arxiv.org/abs/2606.01122)

**<font color=#1a73e8>作者：</font>** R. Drissi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a five-step diagnostic protocol for residual-trained neural HJB-PIDE solvers with control-dependent Lévy jumps, targeting a general failure mode of neural PDE methods: a learned solution can match headline scalar diagnostics while miscomputing an operator inside its training loss. The protocol pairs each neural solve with at least one from-scratch independent reference, decomposes the Hamiltonian into drift, diffusion, compensator, and nonlocal-integral components across a u-grid, and compares the value function and its low-order derivatives over a (t,x) grid before any argmax comparison. Applied to a standard CRRA-Merton-Variance-Gamma benchmark, it isolates a missing 1/2-mixture factor in the neural method's importance-proposal density that scaled the nonlocal integral by exactly half - a textbook signature of a constant proposal scale error, invisible to longer training, grid refinement, and truncation sweeps. With the bug corrected, four references - two finite-difference solvers with disjoint discretizations, the neural solver, and a semi-analytic scalar baseline obtained from CRRA homogeneity - agree on the optimal control to within ~2%. The constant-coefficient CRRA benchmark collapses by homogeneity to a scalar maximization, so the scalar baseline is the efficient method here; the contribution is the protocol, applicable in principle to non-homogeneous and higher-dimensional settings where neural HJB-PIDE solvers are genuinely needed. The episode is a concrete instance of a broader neural-PDE verification failure: pointwise agreement of a learned value or control can coexist with a systematically wrong nonlocal operator, so per-component and surface-level checks are needed before trusting the argmax policy.

---


### 297. [From Reward-Free Representations to Preferences: Rethinking Offline Preference-Based Reinforcement Learning](https://arxiv.org/abs/2606.01123)

**<font color=#1a73e8>作者：</font>** Jun-Jie Yang, Chia-Heng Hsu, Kui-Yuan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference-based reinforcement learning (PbRL) avoids explicit reward engineering by learning from pairwise human preference feedback. Existing offline PbRL methods typically follow a two-stage pipeline, first learning a reward or preference model from labeled preferences and then performing offline RL on unlabeled data. We revisit offline PbRL through the lens of reward-free representation learning (RFRL) from the zero-shot RL literature, and propose a new training framework that first learns latent successor-measure representations from reward-free offline data, followed by contrastive search and fine-tuning using preference data. Through extensive experiments and ablations, we show that our method achieves superior preference efficiency over offline PbRL baselines. This work is the first to connect RFRL with PbRL, highlighting its potential as a feedback-efficient solution. Our code is publicly available at this https URL.

---


### 298. [STARFISH: faST Accuracy Recovery in pruned networks From Internal State Healing](https://arxiv.org/abs/2606.01126)

**<font color=#1a73e8>作者：</font>** Shir Maon, Odelia Melamed, Adi Shamir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pruning is a process designed to reduce the number of weights in a large neural network. This can substantially speed up inference but might cause a considerable reduction in the model's accuracy, and thus it is usually followed by a healing process that regains some of the lost accuracy. In this paper, we propose a new healing method, STARFISH, that can recover (most of) the accuracy of any pruned network efficiently. The main idea of STARFISH is to optimize the pruned network to align with the original network's internal state representations using a tiny calibration set of unlabeled examples. For the common case of removing 50% of the weights, STARFISH healing improves the recovered accuracy by up to 22% over the state-of-the-art methods on ViT-based networks. Its advantage is even more pronounced under aggressive pruning. For example, after eliminating 75% of the weights in a DeiT-B network for ImageNet, STARFISH uses only 0.4% of the number of training images as a calibration set and recovers 82% of the original dense accuracy, whereas competing recovery techniques reach only 40% of the dense model accuracy.

---


### 299. [Local MixVR: Breaking the Communication-Sample Dependence in Distributed Learning](https://arxiv.org/abs/2606.01128)

**<font color=#1a73e8>作者：</font>** Tehila Dahan, Bassel Hamoud, Roie Reshef 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication overhead is a crucial bottleneck in scalable distributed learning. While existing methods aim to efficiently utilize data points, such as Local SGD, Minibatch SGD, and their accelerated variants, they still exhibit communication-round complexity that scales with the total number of samples $N$. In this paper, we introduce Local MixVR, a distributed framework that integrates local updates with variance-reduction techniques to mitigate local noise. We show that Local MixVR is the first distributed method to eliminate the dependence of communication complexity on $N$, achieving a complexity that scales only with the number of workers $M$. In common regimes where $M<O\left(N^{1/4}\right)$, Local MixVR outperforms the state-of-the-art Minibatch Accelerated SGD baseline, bridging a long-standing gap in distributed optimization and establishing a new paradigm for communication-efficient training.

---


### 300. [HakushoBench: A Japanese Chart and Table VQA Benchmark from Governmental White Papers](https://arxiv.org/abs/2606.01132)

**<font color=#1a73e8>作者：</font>** Issa Sugiura, Shuhei Kurita, Yusuke Oda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding chart and table images is essential for applying vision-language models (VLMs) to real-world document understanding. While English benchmarks have advanced rapidly, non-English counterparts remain scarce, leaving it unclear whether this progress generalizes across languages. A key obstacle is the difficulty of collecting realistic and diverse non-English chart and table images at scale. To address this, we leverage governmental white papers as a scalable source for benchmark construction beyond English, as they contain naturally occurring charts and tables across diverse formats and domains and are freely accessible in many countries. As a first instantiation, we introduce HakushoBench, a challenging Japanese chart and table VQA benchmark built from 33 governmental white papers. HakushoBench contains 2,053 images spanning over 10 image types, with manually annotated QA pairs, designed to assess deep and holistic understanding of charts and tables, rather than local visual cues alone. Experiments across a broad range of VLMs demonstrate that HakushoBench remains challenging for open-weight models: the best open-weight model achieves only 58.6% accuracy, and a 34.9-point gap between open-weight and proprietary models highlights substantial room for improvement in complex chart and table understanding. We release our dataset and code.

---


> [!TIP]
> 当前位于：**251-300**（第 6/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
