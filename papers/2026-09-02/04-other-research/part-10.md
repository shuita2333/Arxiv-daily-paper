# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-485**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-485**

---

### 451. [Singular Curvature in ReLU Training:Differentiation and the Gradient-Flow Limit Need Not Commute](https://arxiv.org/abs/2608.30960)

**<font color=#1a73e8>作者：</font>** Xiaoyang Li, Runni Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient descent (GD) is explicit Euler for gradient flow, but a state-accurate continuous-time surrogate need not remain accurate after differentiation. At every fixed nonresonant step size, ordinary automatic differentiation exactly differentiates the executed hard-ReLU GD program. We prove that, over a fixed finite horizon, the GD states converge and these exact discrete derivatives approach an event-free regional propagator, whereas the derivative of the limiting flow also contains speed-normalized activation-event transfers. A prepoint Stieltjes representation separates the absolutely continuous regional Hessian from atomic interface curvature; one nonzero gradient jump produces an exactly rank-one endpoint discrepancy, and global convexity prevents complete multi-event cancellation whenever an event is strict. Nevertheless, a standard family of globally 1-strongly convex residual-ReLU squared-loss risks realizes arbitrarily large reciprocal sensitivity ratios on open initialization sets, with a uniform transversality margin. The same discrete-versus-flow decomposition extends to parameters and reverse-mode adjoints; resolved smoothing in the scalar or autonomous-normal regime and consistent event localization recover the flow sensitivity. The results concern deterministic full-batch, finite-horizon dynamics with a stable finite itinerary of separated same-direction transverse events; they are consistency theorems, not prevalence claims for large-scale training.

---


### 452. [Vision Models Predict Urban Scene Appraisal with Limited Neural Alignment](https://arxiv.org/abs/2608.30964)

**<font color=#1a73e8>作者：</font>** Kaizhen Tan, Yuantao Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision embeddings are increasingly used as general-purpose representations for modelling how people appraise urban scenes, and are validated almost entirely by how well they predict human ratings. High predictive accuracy does not establish that these embeddings organise scenes as human perception does. We test the two properties separately against brain data. Using openly released EEG from 63 adults who viewed and rated 56 Berlin street scenes, we estimate the representational geometry of the scenes over time, the proportion of that geometry that is explainable at all, and its correspondence with seventeen feature spaces spanning language-supervised, self-supervised, category-supervised and dense-prediction training, two orders of magnitude of scale, and interpretable controls. Correspondence is low throughout: the best representation, DINOv2 ViT-B, reaches 29.6% of the lower bound of the noise ceiling, the panel spans 11.0% to 29.6%, and a Gabor energy descriptor is indistinguishable from the best model while outperforming every language-supervised model tested. Within a model, deeper layers still match later neural responses, so the hierarchical correspondence found for object recognition survives even at this low overall level. The same embeddings predict held-out appraisal ratings well, up to r = 0.87, and the two measures do not track each other across models; reweighting features towards the neural geometry lowers appraisal prediction for every model tested, against a control of matched dimensionality. Predicting how a street is appraised is therefore weak evidence that a model represents the street as the brain does. The benchmark uses only public data and requires no training, so evaluating a new representation needs only its embeddings for 55 images.

---


### 453. [DP-VOXLET: Provable Speaker Anonymization for Disentangled Speech Representations](https://arxiv.org/abs/2608.30969)

**<font color=#1a73e8>作者：</font>** Ivoline Ngong, Jack D'Iorio, Hailey Schoppe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Systems for speaker anonymization obfuscate the speaker of an utterance, while maintaining its original semantic contents and prosody. Recent solutions for speaker anonymization rely on learned representations that disentangle an utterance into semantic contents and speaker properties. To anonymize an utterance, these systems replace the speaker properties while leaving the semantic contents unchanged---an approach that can produce strong results on empirical measures of privacy.
In this work, we introduce speaker differential privacy, a formal definition of speaker anonymization based on the framework of differential privacy, and a mechanism for speaker anonymization that provably satisfies the definition. In contrast to prior heuristic-based anonymization systems, our approach enables a provable lower bound on re-identification success rate (e.g. equal error rate) for any possible adversary. We implement our approach in a framework that is compatible with existing disentangled representations. Compared to the prior work on differential privacy for speaker anonymization, our approach achieves significantly higher utility.

---


### 454. [Sparse Competition during Training For the Emergence of Specialized Modules](https://arxiv.org/abs/2608.30978)

**<font color=#1a73e8>作者：</font>** Baptiste Rossigneux, Karim Haroun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modularity in deep neural networks has been proposed as a means of improving both interpretability and training by promoting disentangled representations and reducing redundancy. In this work, we study the emergence of modular structure through competition dynamics between groups of neurons during training. We introduce a method that (i) maintains near-baseline accuracy, (ii) induces usage-based modularity by sparsely routing inputs to neuron groups, and (iii) encourages specialization of these modules, such that their activations are correlated with input classes. We evaluate the proposed approach on ImageNet-100 and CIFAR-100 and show that with it, specialized modules emerge without module-level supervision. These modules capture a meaningful high-level structure in the data, with individual modules responding to semantic categories (e.g., dogs or vehicles). We also study the emergence of a hierarchical partition of sub-tasks depending on the number of modules. Our results suggest that competitive dynamics can serve as a simple mechanism for inducing functional modularity in standard architectures.

---


### 455. [From Intent to Evidence: Policy-Steered Multi-Strategy Retrieval for Long-Video Agents](https://arxiv.org/abs/2608.31005)

**<font color=#1a73e8>作者：</font>** Can Zhang, Baofeng Zhang, Xiaotian Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing long-video agents acquire evidence through one uniform behavior, ignoring whether the required evidence is concentrated, requires broad occurrence coverage, or must discriminate competing hypotheses---which can cause failure before substantive reasoning begins. Prescribing a fine-grained solution procedure for every question is not a satisfactory remedy, as it restricts autonomous exploration. We propose VESTA, a training-free long-video agent organized as a route-conditioned acquire--verify--consolidate loop. Before exploration, an intent router infers an evidence-acquisition policy---focused, recall, or contrastive retrieval over a shared visual--speech scene index---together with an evidence-accounting policy that configures the evidence view maintained during exploration. Policy-steered retrieval yields provisional references that multimodal evidence operations convert into observations, while the Reasoner remains free to verify them, re-query using intermediate findings, or inspect regions outside the retrieved set. A temporal evidence ledger consolidates observations into an adaptive, compressed view of temporal location, provenance, coverage, conflicts, verification outcomes, and hypothesis support, exposing missing and unresolved evidence to guide subsequent acquisition; finalization prioritizes verified observations. On Video-MME-v2, VESTA improves average accuracy by 2.7 points over VideoARM and gains across all six reported metrics. On LongVideoBench, EgoSchema, and LVBench under shared query-time models, it improves by 6.9 points on the LongVideoBench long subset and 1.5 on LVBench, and matches VideoARM on EgoSchema.

---


### 456. [Augmenting Interviewer Judgments of Patient Experience with Automatic Language Analysis](https://arxiv.org/abs/2608.31007)

**<font color=#1a73e8>作者：</font>** Aowen Shi, Michal Balazia, Danilo Postin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how psychiatric patients subjectively experienced a clinical conversation is important for feedback and alliance-related process monitoring. While interviewers form post-session judgments about patient experience, these judgments do not always match patients' self-reports. Automatic approaches for predicting perceived interaction quality from conversation have been proposed, but it remains unclear whether such approaches can complement human judgment rather than simply replicate it. To address this gap, we evaluate a clinician-support framework in which post-session interviewer ratings are combined with automatic language-based predictions to estimate patient-reported interaction quality in free clinical interviews. We assess this integration across multiple standard model types, including Ridge, SVR, MLP, GRU, and BiLSTM, all trained on sentence embeddings extracted from dyadic transcripts of 107 free conversations between psychiatric patients and interviewers. Our results show that combining interviewer judgments with model predictions through simple averaging yields the strongest overall performance. The interviewer-only baseline reached a Pearson correlation of 0.365. Among fully automatic models, Ridge achieved the strongest Pearson correlation (r = 0.286), while BiLSTM achieved r = 0.270. The strongest result was obtained by BiLSTM interviewer integration (r = 0.403). Our findings suggest that automatic language analysis and interviewer judgment capture complementary aspects of patient experience and that their combination provides a more accurate approximation of the patient's own report than either source alone.

---


### 457. [Language-Informed Flow Matching for Trend-Guided Structure-Based 3D Molecular Generation](https://arxiv.org/abs/2608.31009)

**<font color=#1a73e8>作者：</font>** Tianyu Gao, Zhikai Su, Jiashu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structure-based drug design (SBDD) requires ligands that satisfy both 3D target affinity and 1D chemical validity. Existing controllable generation methods often rely on task-specific fine-tuning or externally imposed sampling-time guidance, adding cost and potentially conflicting with evolving 3D geometric constraints. We propose LiFT, a language-informed cross-modal framework built on Flow Matching for trend-guided 3D molecular generation across both de novo design and scaffold hopping. LiFT uses a "Sense-Evolve-Assemble" agent to generate target-aware SMILES as intermediate chemical conditions, from which a pre-trained chemical foundation model extracts continuous semantic priors. These priors are integrated into geometric generation through a lightweight semantic projector with zero-initialized adaptive normalization for stable cross-modal conditioning. We further introduce a Self-Conditioned Decoupled Router (SCDR), which modulates the velocity field according to intermediate structural states during ODE integration. Experiments on Cross-Docked2020 show that LiFT achieves competitive distribution matching while improving medicinal chemistry metrics and maintaining competitive structural validity under task-steering settings without additional generator fine-tuning. Our results suggest that language-derived chemical priors provide effective trend-level guidance for 3D molecular generation. Code and released artifacts are available at this https URL.

---


### 458. [One note in three: a verified census of three deployed AI scribes, and the instrument that counted it](https://arxiv.org/abs/2608.31017)

**<font color=#1a73e8>作者：</font>** Sebastian Fox, Luke Markham, Ryan Lail 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambient AI scribes draft clinical notes under the reassurance that a clinician signs every note. We audited three commercial AI scribes on the same 142 consultations: 565 notes from recorded UK primary-care and US ambulatory encounters plus authored scenarios. Twelve discovery passes proposed 13,678 candidate errors; the 5,898 clearing an importance filter went to an adversarial panel of two models from different families, each told to refute what it could, and 618 survived. One note in three (31.3% [27.0, 35.6]) carries a verified failure, concentrated in allergy and medication information, invented patient identity, and history written up as examination on telephone consultations that can contain none. No product was given a patient record; setting aside the two classes a record would have prefilled, invented identity and dates, the rate is 24.8% [20.8, 29.0]. One failure mode did not fit our scheme, drawn from published scribe-error taxonomies: a treatment the clinician retracts, recorded as delivered care. Two clinicians adjudicated blind, disjoint samples: a physician author upheld 20 of 21 findings (95.2% [77.3, 99.2]) and an independent clinician, not an author, 12 of 12 ([75.8, 100]); both judged every sampled refusal genuine. A failure rate depends on the instrument as much as the scribes. With model, evidence and settings fixed, the review instruction alone moves the share of candidates verified from 9.3% to 79.0%, and the reviewing family moves it too: alone at that instruction the gentler flags 54.8% of notes against 27.8%. Between 28% and 97% of sampled notes carry a failure depending on the standard. Published audits disagree among themselves by a margin instrument differences alone can produce: omission is 54-86% of their errors against our 23.1%. We release all 618 findings with transcript-side evidence, every prompt and model version, and the re-runnable pipeline.

---


### 459. [MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents](https://arxiv.org/abs/2608.31022)

**<font color=#1a73e8>作者：</font>** Vernon Toh, Navonil Majumder, Zhengyuan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas. While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks. First, perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses. Second, agents often stop exploring before they see the full sequence. Third, models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence. These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.

---


### 460. [SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting](https://arxiv.org/abs/2608.31023)

**<font color=#1a73e8>作者：</font>** Haozheng Yu, Xinyu Yang, Rundong Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study dynamic Gaussian Splatting from monocular videos. While recent advancements in dynamic Gaussian splatting offer a promising foundation for modeling dynamic scenes, they often overfit to the training views and fail under occlusion or complex scene motion due to the lack of reliable regularization signals in under-constrained regions. We propose Semantic Motion Graph (SMG), a novel approach models the Gaussian motion as the low-rank semantic motion. Our key insight is that the real-world scene motion is often structured by semantic coherence: regions that are spatially close and semantically related tend to exhibit consistent dynamics. To leverage this prior, we construct SMG to model structured motion of the scene. The Gaussian motion is driven by the motion of SMG nodes. We further observe that the uncertainty of Gaussian motion arises from both unreliable off-the-shelf priors and weakly constrained regions during optimization. SMG addresses this by using reliable graph nodes to guide the motion of nearby unreliable nodes. To evaluate dynamic Gaussian splatting under challenging real-world scenarios, we introduce a new multiview dataset collected under an ego-exo setup. Extensive experiments demonstrate that SMG achieves state-of-the-art performance on monocular dynamic Gaussian splatting across challenging real-world benchmarks. Project page: this https URL.

---


### 461. [Analytic Dynamics: Learning Physics-Grounded Representation for Fast Intrinsic Dynamics Inference from Monocular Videos](https://arxiv.org/abs/2608.31025)

**<font color=#1a73e8>作者：</font>** Jailing Lin, Jikuan Zhang, Jianhua Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inferring object dynamics from visual observations is essential for intelligent agents to reason about and interact with the physical world, yet remains challenging due to the fundamental gap between visual evidence and intrinsic dynamics. Existing methods either rely on costly per-scene optimization, limiting efficiency and scalability, or directly map visual evidence to intrinsic dynamics without intermediate physical abstractions, making them prone to appearance and geometry shortcuts. To bridge this gap, we propose Analytic Dynamics, a feed-forward dynamics inference framework that introduces an intermediate physics-grounded dynamics representation between visual observations and intrinsic dynamics. Specifically, we leverage privileged physical states, including position, displacement, and deformation gradient fields, which are available in simulation, to learn a structured dynamics representation that is difficult to discover from visual observations alone. By aligning visual representations with this space, we equip visual models with a physics-grounded inductive bias, guiding them to capture dynamics-relevant patterns for material model classification and parameter regression. To facilitate this research, we develop a dynamics data generation pipeline and benchmark containing paired physical state trajectories, rendered videos, and ground-truth material models and parameters. Extensive experiments demonstrate that Analytic Dynamics achieves efficient, accurate, and generalizable dynamics inference from monocular videos.

---


### 462. [Driving on Memory](https://arxiv.org/abs/2608.31029)

**<font color=#1a73e8>作者：</font>** Christian Löwens, Thorben Funke, Alexandru Paul Condurache  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving models plan future trajectories from raw sensor input. While earlier driving benchmarks often measured deviation from the human trajectory, current benchmarks such as NAVSIM and Bench2Drive evaluate models with richer simulation-based metrics intended to capture safe and compliant driving. A high benchmark score should reflect that a model can understand the scene in front of it and act accordingly. But how much of that score specifically comes from reacting to the dynamic part of that scene?
To probe this, we remove a model's camera input and replace it with memories from prior drives at the same location. The retrieved memories can provide persistent scene information, including road layout and location-conditioned regularities, but not the current traffic state. Surprisingly, memory is nearly sufficient on NAVSIM, reaching or even exceeding the performance of leading end-to-end methods without actually observing the evaluated scene. Our results suggest that a high NAVSIM score does not require a planner to react to the current traffic scene and should be treated with caution. This effect is benchmark-dependent: driving from memory causes substantially larger performance drops on Bench2Drive and RealEngine. We provide our code at this https URL .

---


### 463. [FaceSnap: Real-Time Personalized Lightstage Facial Performance Capture](https://arxiv.org/abs/2608.31033)

**<font color=#1a73e8>作者：</font>** Rukhshanda Hussain, Noé Artru, Emeline Got 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lightstage facial capture produces production-quality digital humans, but it is resource and labor-intensive. Multi-camera setups, hours of computation, and massive data storage create bottlenecks that hinder iterative workflows. This paper introduces FaceSnap, an end-to-end framework that streamlines capture via a two-stage approach. First, a one-time multi-view optimization from a range-of-motion sequence builds a personalized model encoding both geometry and expression-dependent appearance. This model then enables high-fidelity real-time facial performance capture from a single monocular lightstage camera, with no further multi-view capture required. FaceSnap jointly estimates geometry and dynamic 4K texture at 83 fps. The 4K texture is produced by a novel personalized residual upscaler that recovers subject-specific high-frequency detail, which generic upscalers fail to capture. FaceSnap achieves geometric accuracy competitive with full per-frame multi-view optimization while outperforming feed-forward methods trained on production-quality 3D data, all from a single camera view. Finally, we introduce Multi4D, a public benchmark for evaluating 4D facial reconstruction methods in lightstage environments, enabling topology-invariant geometric comparison across methods.

---


### 464. [Normalized Low-Rank Adaptation](https://arxiv.org/abs/2608.31036)

**<font color=#1a73e8>作者：</font>** Jiale Kang, Ziyin Yue, Zheng Zhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While low-rank adaptation (LoRA) is widely used for parameter-efficient model adaptation, how to regularize its training dynamics for stable and effective optimization remains underexplored. Because LoRA initializes the up-projection to zero, its early optimization dynamics are largely governed by the down-projection. Building on this observation, we introduce Normalized Low-Rank Adaptation (NoRA), a simple yet effective method that normalizes the down-projection matrices during training. We further show that the same normalization can be applied only at initialization, improving standard LoRA without requiring repeated normalization throughout training. Across pretraining, supervised finetuning, and reinforcement learning, NoRA consistently accelerates convergence, improves performance and training stability, and mitigates catastrophic forgetting. These benefits require neither additional trainable parameters nor inference-time computation, making NoRA a simple and broadly applicable enhancement to LoRA.

---


### 465. [Language-Statistical Analysis of Neural Audio Codec Tokens Across Architectures, Corpora, and Noise Conditions](https://arxiv.org/abs/2608.31037)

**<font color=#1a73e8>作者：</font>** Joonyong Park, Shinnosuke Takamichi, David M. Chan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural audio codecs (NACs) convert speech into discrete token sequences, and prior work has reported that these sequences follow language-like statistical laws. This paper analyzes the token statistics of 13 NACs spanning multi-codebook residual vector quantization (RVQ), single-codebook VQ, and non-VQ designs, evaluated on three corpora under clean, white-noise, and real-world DEMAND-noise conditions. Zipf and Heaps parameters, unigram entropy, codebook occupancy, and Jensen-Shannon divergence (JSD) are estimated from matched token samples with explicit fit-validity safeguards and family-conditional $n$-gram orders. Corpus identity explains little variance in any metric, whereas acoustic condition and quantizer meta-category dominate in a metric-dependent way, and unigram entropy is the metric most strongly associated with meta-category. Clean-to-noise JSD computed at a common unigram order is associated with mel-cepstral distortion most clearly under DEMAND noise. The collapse and explosion degradation signatures previously reported for RVQ codecs concentrate in RVQ cells under white and DEMAND noise, respectively; explosion also occurs in non-VQ codecs, and single-codebook VQ codecs shift in occupancy and distribution shape without either signature. These results provide architecture-conditioned conventions for applying language-statistical analysis to NAC tokens.

---


### 466. [Type-Balanced Contextual Learning for Incremental Named Entity Recognition](https://arxiv.org/abs/2608.31038)

**<font color=#1a73e8>作者：</font>** Duzhen Zhang, Yahan Yu, Xiuyi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Incremental Named Entity Recognition (INER) stands as a pivotal task in information extraction, emphasizing the successive identification of new entity types within unstructured text. Faced with the continuous influx of entity types, INER grapples with two significant challenges: the widespread issue of catastrophic forgetting and the unique shift issue of the non-entity type semantics. While pseudo-labeling-based INER methods have proven effective in addressing these challenges, a previously overlooked issue arises: the biased context problem. Our analysis shows that, in new sentences, the contextual associations of tokens representing old entity types exhibit a significantly stronger bias towards new entity types compared to their contexts in old sentences. This tendency intensifies the degradation of old knowledge while promoting the overfitting of new knowledge. To solve this biased context, we propose a Type-Balanced Contextual Learning (TBCL) method, featuring a sentence-duplet learning scheme and a contextual consistency loss. This approach offers a fresh perspective for INER through context analysis. Extensive experiments across ten INER settings on three highly recognized datasets showcase the efficacy of our TBCL method, highlighting its proficiency in resolving the biased context issue inherent in pseudo-labeling based INER approaches.

---


### 467. [Rotational Equivariance in Machine Learning: A Comprehensive Tutorial](https://arxiv.org/abs/2608.31045)

**<font color=#1a73e8>作者：</font>** Peter Lippmann, Fred A. Hamprecht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotational symmetry is one of the most important structural principles in machine learning on 3D data. In applications ranging from physics and materials science to 3D computer vision, predictions should not depend on an arbitrary choice of coordinate frame. Rotational equivariance captures this requirement mathematically by enforcing that a rotation of the input induces a corresponding transformation of the model output. This tutorial provides a comprehensive introduction to rotational equivariance, starting from the physical and geometric intuition behind coordinate independence and building up the necessary machinery from geometric deep learning, group theory, and representation theory. We introduce message passing on Euclidean graphs, group actions and representations, spherical harmonics, Wigner matrices, tensor products, and Clebsch-Gordan decomposition, and explain how these ingredients give rise to modern equivariant architectures. We then survey the principal strategies for incorporating rotational equivariance in deep learning, including group convolutions, internal tensorial representations, and canonicalization-based methods, and discuss their practical strengths and limitations. The tutorial aims to lower the barrier to the subject by connecting the underlying mathematics to practical model design, by unifying ideas that are often expressed in different formal languages, and by helping practitioners choose among competing approaches through a clear discussion of their trade-offs.

---


### 468. [Segmentation of Bovid Dentition Under Imperfect Annotations: A Comparative Study of Convolutional and Attention Models](https://arxiv.org/abs/2608.31052)

**<font color=#1a73e8>作者：</font>** Keith G. Mills, Evan B. Sanders, Gregory J. Matthews 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation decomposes an image into distinct mask regions corresponding to different object categories, such as people, cars, signs or buildings. Advances in machine learning (ML) have shifted this task away from traditional rule-based heuristics such as edge detection, towards deep neural networks (DNN) that learn to classify pixels directly. However, semantic segmentation DNNs crucially depend on expertly designed mask targets to learn from, and imperfect or misaligned masks can interfere with a model's ability to learn effectively.
This paper presents a comparative study of segmentation architectures, ranging from convolutional backbones to vision transformers, applied to the B.O.V.I.D. dataset, a corpus of high-resolution bovid dental photographs paired with hand-made segmentation masks not originally designed for ML-based training. We evaluate a range of preprocessing and alignment techniques to mitigate the resulting label imperfections. We find that while these preprocessing choices have limited effect on quantitative metrics such as Dice score and mIoU, their qualitative impact on predicted masks is substantial.

---


### 469. [Identity-Conditioned Latent Consistency Distillation for Face Synthesis](https://arxiv.org/abs/2608.31053)

**<font color=#1a73e8>作者：</font>** Tiago Kienen Chaves, Bernardo Biesseck, David Menotti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved strong results in high-fidelity image synthesis, but their iterative sampling process makes large-scale generation computationally expensive. This limitation is especially relevant when generating synthetic face datasets for face recognition, where a large number of subjects with many samples in different poses, expressions, ages, etc., are required. In this work, we show that identity-conditioned face synthesis can be performed at a substantially lower computational cost by a latent Consistency Model with few iterations, without compromising image quality. For training, we distill knowledge from the foundation Diffusion Model Arc2Face (teacher) by adapting its original text-to-image pipeline to an embedding-to-face setting, replacing textual prompts with ArcFace identity embeddings. Our distilled model (student) generates identity-conditioned face images with an average inference time of 0.4819 seconds per image, compared with 2.102 seconds for Arc2Face, resulting in a 4.36$\times$ speed-up. Quantitative results, based on FID scores, show that the distilled model remains competitive with Arc2Face across all evaluation protocols. On 100k generated images, it achieves near-parity on CelebA (13.921 vs. 12.928) and outperforms the teacher on WebFace42M (9.317 vs. 9.802). Further evaluations on Synth-500 and AgeDB show a moderate performance gap for the former but comparable results for the latter. These results indicate that Arc2Face can be accelerated through task-specific latent consistency distillation while preserving high image quality for large-scale synthetic face generation. Our proposal is publicly available at this https URL.

---


### 470. [The Exclusion Ratchet: False-Positive Suppression Accumulates and Persists in Detection Rule Repositories](https://arxiv.org/abs/2608.31062)

**<font color=#1a73e8>作者：</font>** Sudaroli Dhananjeyan, Kumaran U  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a rule produces too many false alarms an analyst adds an exclusion, and the rule thereafter declines to alert in that circumstance. Each such decision is locally reasonable; what becomes of them collectively is not known. Recent longitudinal work established that curation does not converge, but measured restoration time only for revisions that were later reverted -- a measure silent about narrowing that is never undone. We measure that. Across nine years and 8,234 revisions of the SigmaHQ corpus we detect suppression semantically -- growth in the set of predicates held under negation without compensating growth in coverage -- and validate it against blinded hand labelling (precision 0.828, recall 0.911). The test is deterministic: nothing is learned from the data, and the definitions are released as code. Exclusions were added 1,642 times and withdrawn 304, a ratio of 5.4 to 1 that rises to 13 to 1 at the level of the individual rule. Thirty-one per cent of the narrowing is invisible to structural comparison, which existing structural accounts therefore undercount. Estimated by Kaplan-Meier, 86.7 per cent of exclusions remain in force three years on, and persistence is independent of whether the rule is the only coverage for its ATT&CK technique (p = 0.49). Of path-valued exclusions, 64.1 per cent can be satisfied by an unprivileged process that chooses a filename. Narrowing accumulates, is rarely revisited, and is not triaged by consequence. We give a criterion for deciding which exclusions to examine first.

---


### 471. [Multimodal Shared Latent Representation of Narration, Microscope and iOCT Images for Phase Recognition in Vitreoretinal Surgery](https://arxiv.org/abs/2608.31065)

**<font color=#1a73e8>作者：</font>** Onur Izmitlioglu, Shervin Dehghani, Tarek Ghannoum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical phase recognition is key to context-aware computer-assisted feedback in vitreoretinal procedures, yet the scarcity of synchronized multimodal intraoperative data, particularly microscope views and intraoperative OCT, limits approaches that aim to replicate the multimodal integration surgeons perform naturally. Surgical narration, by contrast, is abundantly available online and offers rich semantic supervision. Prior work has mainly explored pairwise contrastive learning (e.g., intraoperative OCT-microscope or microscope-narration), leaving the joint modeling of all three modalities largely unexplored. We introduce a framework that uses microscope views as a shared anchor to bridge surgical narrations and intraoperative OCT (iOCT) without requiring a fully synchronized tri-modal dataset, leveraging real microscope-narration videos and a synthetic dataset of synchronized microscope video and tool-aligned iOCT pairs. Contrastive alignment transfers structural priors from the synthetic domain to real videos lacking iOCT, and a dual-head MS-TCN++ integrates the resulting embeddings for joint macro- and micro-phase prediction. Evaluated on real vitreoretinal surgeries, our framework improves macro-phase recognition over a zero-shot baseline (mean F1 0.38 to 0.53) and provides an exploratory route to estimating fine-grained instrument-tissue measurements that are not directly observable in real microscope video alone; these micro-phase estimates are validated quantitatively on synthetic data and shown only qualitatively on real surgery. To our knowledge, this is the first work to unify microscope view, iOCT B-scans, and surgical narrations in a shared latent space for surgical phase recognition.

---


### 472. [Universal Transformers for Circuit Computations: Perfect Length Generalization in Tiny Transformers](https://arxiv.org/abs/2608.31067)

**<font color=#1a73e8>作者：</font>** Takuya Ito, Ruchir Puri, Murray Campbell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning generalizable algorithmic computations remains a challenge for neural networks, as reflected in persistent failures on compositional and length generalization benchmarks. We present a provably correct, transformer parameterization (with only 280 learnable parameters for Boolean algebra tasks) capable of learning and evaluating problems of any depth or length. We assume inputs are fully parenthesized, well-formed expressions. Our approach conceptualizes algorithmic tasks as circuit models embedded in transformers, enabling depth-1 circuit reduction in a single forward pass. To achieve depth generalization, we introduce a positional encoding that tracks each gate's depth within the circuit, enabling the model to identify evaluable subexpressions at each iteration via masked hard attention, with $O(n)$ per-iteration complexity via linear attention. Combined with an autonomous halting criterion, the model terminates after $d$ iterations for problems of depth $d$, yielding $O(n \cdot d)$ total complexity. We show that training on shallow problem instances (depth 1 and depth 2) effectively recovers interpretable parameters that {\em snap} into place, resulting in exact length generalization. Though we establish that our construction provably evaluates Boolean expressions -- a universal symbolic computation -- of arbitrary length perfectly, in other experiments we also demonstrate that our transformer variant can learn and generalize perfectly (100% accuracy) on other common length generalization benchmarks, including modular arithmetic and ListOps.

---


### 473. [LISynSeg: Data-Centric Label-to-Image Synthesis for Cross-Modality Whole-Heart Segmentation](https://arxiv.org/abs/2608.31073)

**<font color=#1a73e8>作者：</font>** Jiacheng Wang, Ivana Isgum, Ipek Oguz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-heart segmentation (WHS) in computed tomography (CT) and magnetic resonance imaging (MRI) is affected by acquisition shifts and heterogeneous cardiac annotations. Existing WHS systems combine architectural design, transfer learning, and generic spatial or intensity augmentation. We investigate whether changes to data augmentation and training supervision can improve cross-modality WHS while the segmentation architecture is held constant. We present LISynSeg, a data-centric approach that augments real-image nnU-Net training with label-to-image synthesis. Synthetic volumes are generated from cardiac label maps using contrast and acquisition perturbations calibrated to the training cohort, then mixed with real images to retain thoracic context absent from the labels (and thus the synthesized images). We model cardiac label variation through controlled changes in myocardial wall thickness and partial supervision of uncertain vessel endpoints. On the CARE Whole-Heart benchmark, synthetic-only training performs worse than the real-image nnU-Net baseline, whereas calibrated real-synthetic training improves cross-modality segmentation without changing the architecture; the improvement is larger for MRI than for CT. The results show that modifying the training data strategy can benefit model development for heterogeneous cardiac data. Code and trained weights will be released at this https URL.

---


### 474. [Real-Time Video Anomaly Detection Using YOLO Pose Estimation and CLIP-Based Semantic Scoring](https://arxiv.org/abs/2608.31074)

**<font color=#1a73e8>作者：</font>** Vanodhya G. Warnasooriya, Amir Hajian, Watchara Ruangsang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a lightweight two-stage framework for real-time video anomaly detection. The first stage employs YOLO v11n-pose to detect persons and extract seventeen skeletal keypoints in a single forward pass. The second stage encodes each cropped person region through CLIP ViT-B/32 and computes cosine similarity against predefined textual descriptions of anomalous behaviors. This architecture eliminates the need for optical flow, standalone pose estimators, and density-based scoring modules. Experiments on CUHK Avenue, ShanghaiTech Campus, and a custom indoor dataset collected at Chulalongkorn University demonstrate an end-to-end throughput of approximately 51 FPS on an NVIDIA Titan XP GPU, a 3.36x speedup over the multi-feature baseline, while maintaining frame-level AUROC values of 89.26%, 70.26%, and 84.13%, respectively.

---


### 475. [Robust retinal biometrics for patient identity verification and retrieval across age and imaging devices](https://arxiv.org/abs/2608.31094)

**<font color=#1a73e8>作者：</font>** Jose D. Vargas-Quiros, Dennis Bontempi, Jeroen Vermeulen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patient identity errors can compromise longitudinal medical records, research databases, and downstream clinical decisions. We present a retinal biometric system for verifying claimed identities and retrieving the correct identity from color fundus images. We trained a 512-dimensional metric-learning encoder combining a ConvNeXtV2 backbone with ArcFace and triplet losses on 227,004 images from 21,851 patient-eye identities in the Rotterdam Study, spanning multiple imaging devices and up to 32.6 years of follow-up. The system was evaluated on held-out Rotterdam Study data and externally on the UK Biobank and Age-Related Eye Disease Study (AREDS). Before evaluation, we used the model to screen for identity inconsistencies and manually adjudicated flagged images, identifying incorrect assignments in 0.588% of Rotterdam Study images, 0.259% of UK Biobank images, and 0.164% of AREDS images. In retrospective-only verification after removing near-duplicate images, the system achieved AUROCs of 0.9998, 0.9997, and 0.9998 in the Rotterdam Study, UK Biobank, and AREDS, respectively. For identity retrieval using only previously acquired images, Recall@1 was 99.7%, 97.2%, and 97.6%, respectively, from galleries averaging 4436-8510 identities; the correct identity appeared among the top five results in at least 98.6% of cases. Performance remained robust across imaging devices and long follow-up intervals, while lower image quality and inconsistent retinal fields accounted for most failures. These findings establish retinal anatomy as a durable biometric signal, useful for safeguarding the integrity of longitudinal imaging records.

---


### 476. [One Adapter, Many Tasks: Task-Conditioned Feature Transformations for Continual Learning](https://arxiv.org/abs/2608.31096)

**<font color=#1a73e8>作者：</font>** Yunxiang Fu, Meng Lou, Yizhou Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class-incremental learning (CIL) requires a model to incrementally learn tasks that contain new classes without accessing earlier training data while preserving the ability to recognize all seen classes. Recently, pretrained-model-based approaches have become prevalent by adapting a frozen backbone with additional lightweight trainable modules. Existing methods, however, exhibit limitations: task-specific adapters learn explicit per-task representations but are parameter- and computation-inefficient, while LoRA-based merging methods combine per-task LoRA parameters into a single model whose static aggregated weights cause representation interference during inference. To address these problems, we present \textbf{FACET}: task-conditioned \textbf{F}e\textbf{A}ture transformation with \textbf{C}ondition\textbf{E}d feature consis\textbf{T}ency, achieving excellent parameter efficiency while producing highly discriminative features during inference. When continually trained on a task sequence, FACET learns a single shared adapter that employs a dynamic task-conditioned feature transformation, shaping the overall feature distribution of the adapter into a mixture of overlap-reduced task-specific components. On the other hand, we propose an efficient replay-free task-conditioned feature consistency loss, aiming to mitigate catastrophic forgetting of the learned mixture distribution in the adapter's feature space. Even when maintaining only a single adapter, FACET demonstrates robust scalability. On both very long task sequences (e.g., 200 tasks) and standard short task sequences (e.g., 20 tasks), our method achieves superior performance while using significantly fewer trainable parameters and GFLOPs. The code will be made open source upon acceptance.

---


### 477. [Cross-Regional Grapevine Cold Hardiness Prediction via Learned Multimodal Latent Representations](https://arxiv.org/abs/2608.31097)

**<font color=#1a73e8>作者：</font>** William Solow, Paola Pesantez-Cabrera, Markus Keller 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate daily predictions of cold hardiness in woody plants are critical in regions where freezing temperatures can damage dormant buds and reduce seasonal yield. Existing biophysical, hybrid, and deep learning models have shown high predictive accuracy when trained on local data but remain largely site-specific. The limited availability of cold hardiness data, coupled with the lack of principled methods for transferring cold hardiness predictions to new regions and cultivars, has limited the broader adoption and practical utility of these approaches, particularly in data-scarce regions. To address these limitations, we propose a cold hardiness prediction framework that learns a transferable latent representation by capturing region-specific variation through learned embeddings. To enable prediction in previously unseen regions, we infer embeddings from (1) text descriptions of the cultivar and growing region, and (2) limited historical observations, supporting both zero-shot and few-shot transfer. Experiments on datasets from six regions across North America demonstrate that our approach consistently outperforms state-of-the-art cold hardiness prediction methods, yielding more accurate predictions and substantially improving transfer to data-scarce regions.

---


### 478. [DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution](https://arxiv.org/abs/2608.31106)

**<font color=#1a73e8>作者：</font>** Jiashu Zhu, Yanhao Zheng, Ruitian Tian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generators often omit audio or synthesize it in a separate stage, limiting reciprocal modeling of visual dynamics and acoustic events. We present DreamX-Creator 1.0, a compact native joint audio-video generation system centered on a 7B generator. Conditioned on a first frame and a text prompt, the generator jointly denoises modality-specialized audio and video streams. The streams are processed independently in the first half of the network and coupled in the latter half through Gated Cross-Modal Attention, whose token- and head-wise output gates modulate each active cross-modal attention-head output. A unified Audio-Video Data System constructs and filters temporally coherent clips, produces structured multimodal annotations, and organizes clips into capability-oriented data pools. Progressive Joint Training comprises two audio-video pre-training stages followed by High-Quality Finetuning. Audio-Video Reinforcement Learning further post-trains the generator with Modality-Aware Multimodal Feedback that routes video-, audio-, and cross-modal feedback to the corresponding streams. For high-resolution output, our Autoregressive 1-Step 2K Refinement pipeline adapts a bidirectional multi-step teacher into an autoregressive multi-step refiner and distills it into a student requiring one denoising evaluation per temporal chunk. Overall, DreamX-Creator 1.0 achieves native, synchronized audio-video generation with performance competitive with state-of-the-art open-source systems. By releasing our compact 7B generator and 2K Refiner, we seek to democratize native audio-video generation and provide an accessible foundation for future research in unified audio-video generative modeling.

---


### 479. [VeriCam: A Verification Baseline for the Classification of Unknown Data](https://arxiv.org/abs/2608.31107)

**<font color=#1a73e8>作者：</font>** Lucas Wojcik, Gabriel E. Lima, Sergio M. Silva Jr. 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advent of foundation models have enabled a new era in zero-shot classification. Yet, key challenges persist. Despite their impressive generalization power that leverages the immense pre-training knowledge, both foundation models for image and text as well as vision-text hybrids lack the representational power needed for fine-grained, minutiae-based class separation that some real-world tasks require. To address the current gaps in the literature, we propose VeriCam, a pipeline designed to learn highly specialized features that enable classification of unknown classes in unseen data. VeriCam works by leveraging the representation power of image models trained for the verification task, where the model develops an intricate feature space that incorporates fine-grained details. By training a model to discriminate between pairs of images from the same and different classes, a relational graph is constructed, representing the class relationships between data points. We then present two approaches for graph clustering: a naive algorithm and a specific setup for the Leiden graph clustering algorithm. The pipeline is validated on the LPLCv2 dataset, which comprises real-world traffic surveillance images. We show that the dataset carries an inherent capture device bias that is posed as a generalization challenge for downstream License Plate recognition tasks such as OCR. As such, we dynamically identify capture devices with a label-agnostic approach, enabling the construction of a fair and unbiased benchmark. In the cross-device scenario, our pipeline reaches an F1-Score of 93.45 in the verification baseline and a V-Measure score of 80.13 in the clustering step. All code is publicly available at this https URL

---


### 480. [BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives](https://arxiv.org/abs/2608.31113)

**<font color=#1a73e8>作者：</font>** Pradyumn Goyal, Yizhak Ben-Shabat, Hsueh-Ti Derek Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce BLARM, a feed-forward method for video-driven 3D mesh animation. Given a monocular video and a static object mesh, BLARM predicts a temporally coherent animated mesh whose motion follows the video. Rather than relying on explicit rigs or directly regressing high-dimensional vertex motion, we represent animation using a compact set of learned, time-varying rigid motion components and time-invariant vertex-to-component skinning weights. This yields a low-dimensional deformation space without requiring skeletons, cages, skinning weights, or rig annotations. Our architecture conditions geometry-derived deformation latents on video features through factorized spatial-temporal attention, then decodes rigid transformations blended by predicted skinning weights. Trained with trajectory reconstruction, entropy regularization, and motion-aware contrastive learning, BLARM produces accurate and temporally stable animations while recovering compact, interpretable motion structure from monocular video.

---


### 481. [On the Complexity of the Compatibility Problem for Succinctly Encoded Conditional Distributions](https://arxiv.org/abs/2608.31120)

**<font color=#1a73e8>作者：</font>** Guy Emerson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The motivation for this paper is the investigation of the trade-offs implicit in probabilistic models used in machine learning. Models are often used to make predictions in the form of conditional probabilities. However, a pair of conditional distributions p(x|y) and p(y|x) may not be compatible with any joint distribution p(x,y). Given two such conditionals, determining if there exists a compatible joint is known as the compatibility problem. For discrete random variables, when the conditionals are encoded as probability tables, the compatibility problem has a known solution, which is computationally tractable. In this paper, we formalise and study a succinct version of the problem, encoding conditional distributions as arithmetic circuits. This is applicable to practical applications of probabilistic modelling in high-dimensional settings, including neural network models. We show that, for succinct circuit representations of conditionals, the compatibility problem is intractable. In the case that all probabilities are non-zero, the problem is co-NP-complete. In the case that probabilities can be zero, we give examples to demonstrate that several notions of compatibility can be distinguished, and we prove that multiple versions of the problem are PSPACE-complete. Furthermore, we show that, assuming the polynomial hierarchy does not collapse, there exist compatible succinct conditionals whose joint cannot be expressed succinctly. Implications of these results for probabilistic modelling and machine learning are discussed.

---


### 482. [Sharp Approximation Rates for Neural Networks with Affine Latent Parameterizations](https://arxiv.org/abs/2608.31157)

**<font color=#1a73e8>作者：</font>** Shijun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many parameter-efficient methods generate the parameters of a large neural network from a low-dimensional latent representation. Given an architecture $\Phi$ with $P_\Phi$ parameter slots, we write $\boldsymbol{\theta}_f=\mathcal{G}(\boldsymbol{\xi}_f)$, where $\mathcal{G}\colon\mathbb{R}^M\to\mathbb{R}^{P_\Phi}$ is a parameter generator and $\boldsymbol{\xi}_f\in\mathbb{R}^M$ is a latent representation of the target function $f$. The architecture $\Phi$ and the generator $\mathcal{G}$ are shared across the entire target class, while each target $f$ is represented by its own latent vector $\boldsymbol{\xi}_f$, with $\Phi_{\mathcal{G}(\boldsymbol{\xi}_f)}$ approximating $f$. This framework encompasses hypernetworks, low-dimensional parameterizations, parameter-efficient adaptation, and model compression. Understanding the tradeoff between the latent dimension $M$ and the network budget $P$ is therefore fundamental to characterizing the expressive efficiency of these methods. We study this tradeoff for affine generators and fully connected ReLU architectures. More precisely, optimizing jointly over architectures $\Phi$ satisfying $P_\Phi\leq P$ and affine generators $\mathcal{G}:\mathbb{R}^M\to \mathbb{R}^{P_\Phi}$, we prove that the optimal worst-case uniform approximation error over the unit ball of $\alpha$-Hölder functions on $[0,1]^d$, where $0<\alpha\leq1$, has the sharp order $ \bigl(P\min\{M,P\}\bigr)^{-\alpha/d}. $ In particular, our result shows that even a fixed-dimensional latent space suffices to achieve vanishing approximation error as the network budget increases.

---


### 483. [BRF-GS: Hyperspectral Bidirectional Reflectance Factor Modeling and Image Generation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2608.31159)

**<font color=#1a73e8>作者：</font>** Yiling Yao, Wenjuan Zhang, Bowen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The bidirectional reflectance factor (BRF) characterizes the directional radiative properties of terrestrial surfaces. However, existing three-dimensional (3D) radiative transfer models require complex scene construction and computationally intensive radiative transfer solvers, limiting efficient generation of multi-angle hyperspectral reflectance imagery. 3D Gaussian Splatting (3DGS) offers an efficient framework for neural scene representation and novel view synthesis, but its low-order spherical harmonics representation is insufficient for complex directional reflectance, while the high dimensionality and inter-band quality differences of hyperspectral data introduce additional challenges. To address these challenges, we propose BRF-GS, a 3DGS-based framework for BRF modeling and hyperspectral reflectance image generation. BRF-GS introduces a hybrid BRDF-driven kernel to represent complex directional reflectance, selects geometry-reliable spectral bands for robust 3D scene initialization, and adopts a two-stage training strategy that decouples geometry optimization from spectral modeling. We further construct the AIR-BRF dataset, a multi-angle hyperspectral directional reflectance dataset comprising three scenes with diverse natural and artificial targets. Experiments demonstrate that BRF-GS achieves superior spatial and spectral fidelity and accurately reproduces characteristic view-dependent BRF responses. The proposed framework provides an efficient data-driven approach for BRF modeling and multi-angle hyperspectral reflectance image generation in remote sensing scenes.

---


### 484. [Constant Individual Regret in General Games](https://arxiv.org/abs/2608.31166)

**<font color=#1a73e8>作者：</font>** Mingyang Liu, Gabriele Farina, Asuman Ozdaglar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncoupled no-regret dynamics provide a decentralized route to equilibrium, but prior guarantees for individual regret retain a polylogarithmic dependence on the horizon. We remove this dependence for every finite $N$-player normal-form game under full-information feedback. We introduce \emph{ECHO-OFTRL}: optimistic follow-the-regularized-leader (OFTRL) equipped with an EMA cascade for high-order optimism (ECHO), where EMA denotes exponential moving average. The algorithm is deterministic and fully uncoupled. If $m_{\max}$ denotes the largest action-set size, then, simultaneously for every horizon $T\geq1$, it guarantees that each of the $N$ players in the game incurs regret upper bounded by $O(\textrm{poly}(N, \log m_{\max}))$. Our algorithm leverages a new form of optimism inspired by modern filter design.

---


### 485. [Context-Aware Interleaved Batching for WhisperX](https://arxiv.org/abs/2608.31170)

**<font color=#1a73e8>作者：</font>** Carlos Bain, Max Bain  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While WhisperX accelerates speech transcription via intra-audio batching, it isolates audio segments, losing the historical context needed for coherent punctuation and terminology transcription. Conversely, standard Whisper retains context sequentially but suffers from slow inference and hallucination loops. To achieve the best of both worlds, we propose Context-Aware Interleaved Batching. By using VAD-derived segment boundaries, our algorithm stabilizes Whisper's text conditioning, allowing us to safely maintain continuous historical context across batched audio segments. As demonstrated on long-form audio benchmarks, this approach reduces Word Error Rate (WER) and improves proper noun transcription, all while maintaining high-throughput inference speeds.

---


> [!TIP]
> 当前位于：**451-485**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-485**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
