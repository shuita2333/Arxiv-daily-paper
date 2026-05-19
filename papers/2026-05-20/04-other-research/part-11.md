# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 501. [Ringmaster LMO: Asynchronous Linear Minimization Oracle Momentum Method](https://arxiv.org/abs/2605.18174)

**<font color=#1a73e8>作者：</font>** Abdurakhmon Sadiev, Artavazd Maranjyan, Ivan Ilin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently emerged as a strong alternative to AdamW for training neural networks, with encouraging large-scale pretraining results and growing evidence that matrix-structured updates can be faster in practice. Yet Muon, and more generally Linear Minimization Oracle (LMO) based methods, are typically used synchronously. This is problematic in heterogeneous distributed systems, where workers complete gradient computations at different speeds and synchronous training must repeatedly wait for slower workers. In this work, we introduce Ringmaster LMO, an asynchronous LMO-based momentum method for unconstrained stochastic nonconvex optimization. Our method builds on the delay-thresholding idea of Ringmaster ASGD. For SGD-type methods, Ringmaster ASGD achieves optimal time complexity by discarding overly stale gradients. Ringmaster LMO extends this mechanism to general LMO-based updates. We establish convergence guarantees under generalized $(L_0, L_1)$-smoothness and further develop a parameter-agnostic variant with decreasing stepsizes and adaptive delay thresholds. Finally, we translate our iteration guarantees into time complexity bounds under heterogeneous worker computation times. In the classical Euclidean smooth setting, these bounds recover the optimal time complexity of Ringmaster ASGD. Experiments on stochastic quadratic problems and NanoChat language-model pretraining show that the advantages of Ringmaster LMO grow with system heterogeneity and that the method outperforms strong synchronous and asynchronous baselines.

---


### 502. [Token-Space Mask Prediction for Efficient Vision Transformer Segmentation](https://arxiv.org/abs/2605.18177)

**<font color=#1a73e8>作者：</font>** Calvin Galagain, Martyna Poreba, François Goulette  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Query-based Vision Transformer segmentation models typically reconstruct dense spatial feature maps to predict masks, inheriting design patterns from convolutional architectures. We show that this explicit image-space reconstruction is not required. We introduce TokenMask, a token-space mask head that computes mask logits directly from query-token affinities and performs interpolation in logit space rather than feature space. This reformulation preserves the original linear scoring mechanism while simplifying the computational structure. Across diverse ViT backbones, datasets and segmentation tasks, TokenMask consistently improves efficiency over prior approaches by reducing computational and memory requirements while maintaining competitive accuracy, leading to tangible speedups on NVIDIA Jetson AGX Orin using TensorRT FP16 inference. Overall, TokenMask yields a simpler and more deployment-friendly design for embedded vision systems.

---


### 503. [Scalable Environments Drive Generalizable Agents](https://arxiv.org/abs/2605.18181)

**<font color=#1a73e8>作者：</font>** Jiayi Zhang, Fanqi Kong, Guibin Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.

---


### 504. [The Dynamics of Policy Gradient in Social Dilemmas with Partner Selection](https://arxiv.org/abs/2605.18185)

**<font color=#1a73e8>作者：</font>** Benedict Russell, Chin-wing Leung, Paolo Turrini  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In social dilemmas self-interested learning agents face the choice between the societal benefit of cooperation and the immediate reward of defection. Significant evidence exists on the benefits of assortment mechanisms such as partner selection for the emergence of cooperation, but this is largely available through agent-based simulations. In this paper, we provide an analytical solution to the problem, studying the policy-gradient dynamics in a multi-agent environment with partner selection. We show how partner selection changes the opponent distribution and hence the reward landscape, and prove this promotes cooperation under simple rules known from the literature. In particular, we find that population variance is a necessary condition for cooperation to emerge. Using a two-dimensional Wiener process, we extend the dynamics to capture the stochastic effects of partner selection and the resulting opponent distribution. We derive a sufficient condition for the population to be cooperation-promoting and prove the existence of a stationary distribution. Simulations confirm that the stochastic model accurately captures the policy-gradient dynamics and clarifies how the learning rate affects the emergence of cooperation.

---


### 505. [Dual-Rate Diffusion: Accelerating diffusion models with an interleaved heavy-light network](https://arxiv.org/abs/2605.18190)

**<font color=#1a73e8>作者：</font>** Grigory Bartosh, David Ruhe, Emiel Hoogeboom 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve state-of-the-art generative performance but suffer from high computational costs during inference due to the repeated evaluation of a heavy neural network. In this work, we propose Dual-Rate Diffusion, a method to accelerate sampling by interleaving the execution of a heavy high-capacity context encoder and a light efficient denoising model. The context encoder is evaluated sparsely to extract high-dimensional features, which are effectively reused by the light denoising model at every step to refine the sample efficiently. This approach significantly accelerates inference without compromising sample quality. On ImageNet benchmarks, Dual-Rate Diffusion matches the performance of standard baselines while reducing computational cost by a factor of $2$-$4$. Furthermore, we demonstrate that our method is compatible with distillation techniques, such as Moment Matching Distillation, enabling further efficiency gains in few-step generation.

---


### 506. [Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation](https://arxiv.org/abs/2605.18191)

**<font color=#1a73e8>作者：</font>** Guining Cao, Jiaxin Peng, Chu Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current reinforcement learning(RL) methods are broadly applicable and powerful in verifiable settings where scalar rewards can be provided. However, in open-ended generation tasks, verifying the correctness of responses remains challenging, and training reward models incurs substantial computational and annotation costs. Moreover, reinforcement learning (RLVR) often leads to diversity collapse and produces stereotypical or rigid outputs, outcomes that are particularly undesirable in open-domain scenarios. We propose Pairwise Preference Reward and Group-based Diversity Enhancement (PPR-GDE), a RL method that is more suitable for open-ended generation. PPR-GDE does not require scalar rewards and incorporates group-level diversity into the reward signal, it preserves the comparative structure of subjective evaluation through a pairwise preference reward, mitigates judge position bias via repeated comparisons with swapped response order, and introduces a group-based diversity reward that explicitly encourages semantic dispersion within a response group, all of these reward signals are integrated into a unified group-relative policy optimization objective. We instantiate PPR-GDE on role-playing task, experiments show that PPR-GDE achieves a better alignment quality as well as expressive diversity than strong RL baselines. Further analysis shows that pairwise preference is critical for preference alignment in subjective perspective, while the diversity metric plays an essential role in achieving superior expressive diversity and broader semantic coverage.

---


### 507. [Best Segmentation Buddies for Image-Shape Correspondence](https://arxiv.org/abs/2605.18193)

**<font color=#1a73e8>作者：</font>** Itai Lang, Dongwei Lyu, Dale Decatur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding correspondences is a fundamental and extensively researched problem in computer vision and graphics. In this work, we examine the underexplored task of estimating segmentation-to-segmentation correspondence between images in the wild and untextured 3D shapes. This task is highly challenging due to substantial differences in appearance, geometry, and viewpoint. Our approach bridges the cross-modality gap by linking pixels in the image segment to vertices in the corresponding semantic part of the 3D shape. To achieve this, we first distill deep visual features from a 2D vision model onto the 3D shape surface, allowing for the computation of feature similarity between image pixels and shape vertices. Then, we identify Best Segmentation Buddies, vertices whose most similar image pixel lies within the image segmentation region, enabling the reliable discovery of vertices in semantically corresponding shape parts. Finally, we leverage distilled 3D features from the 2D image segmentation model to segment the shape directly in 3D, bootstrapping the correspondence process. We demonstrate the generality and robustness of our approach across a wide range of image-shape pairs, showcasing accurate and semantically meaningful correspondences. Our project page is at this https URL.

---


### 508. [Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models](https://arxiv.org/abs/2605.18202)

**<font color=#1a73e8>作者：</font>** Samuele Bortolotti, Emanuele Marconato, Andrea Pugnana 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neuro-Symbolic Concept-based Models (NeSy-CBMs) are a family of architectures that integrate neural networks with symbolic reasoning for enhanced reliability in high-stakes applications. They work by first extracting high-level concepts from the input and then inferring a task label from these compatibly with given logical constraints. Yet, their label and concept predictions can be overconfident, making it difficult for stakeholders to gauge when the model's decisions can be trusted. We address this issue by integrating ideas from Conformal Prediction (CP), a framework providing rigorous, distribution-free coverage guarantees. We formalize three desiderata -- consistency, coverage, and conciseness -- that any conformal method for NeSy-CBMs should satisfy, and show that existing approaches fall short of at least one. We then introduce COCOCO, a post-hoc framework that conformalizes concepts and labels jointly and reconciles them via a single deduction-abduction revision step. COCOCO satisfies all three desiderata, retains distribution-free coverage, is robust to imperfect knowledge and supports user-specified size budgets. Our experiments on 8 data sets highlight how COCOCO compares favorably against competitors and natural baselines in terms of performance and set size.

---


### 509. [EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation](https://arxiv.org/abs/2605.18214)

**<font color=#1a73e8>作者：</font>** Rosario Leonardi, Francesco Ragusa, Daniele Materia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.

---


### 510. [A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders](https://arxiv.org/abs/2605.18224)

**<font color=#1a73e8>作者：</font>** Zegu Zhang, Jianhua Peng, Jian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed.
The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.

---


### 511. [Are Sparse Autoencoder Benchmarks Reliable?](https://arxiv.org/abs/2605.18229)

**<font color=#1a73e8>作者：</font>** David Chanin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.

---


### 512. [Attacking the First-Principle: A Black-Box, Query-Free Targeted Mimicry Attack on Binary Function Classifiers](https://arxiv.org/abs/2605.18231)

**<font color=#1a73e8>作者：</font>** Gabriel Sauger, Jean-Yves Marion, Sazzadur Rahaman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Binary function classifiers play a crucial role in maintaining the security and integrity of software systems by detecting malicious code and unauthorized modifications. However, machine learning-based classifiers are vulnerable to adversarial attacks that can evade detection. In this study, we present Kelpie, a novel framework for executing mimicry attacks, a stronger type of targeted evasion attacks, on binary function classifiers in a black-box, zero-query setting. Unlike previous approaches that rely on querying the target classifier to refine untargeted evasion attacks, Kelpie leverages code transformations that preserve the functionality of malicious payloads while causing them to be misclassified as we want. Through extensive experimentation, we demonstrate that Kelpie can successfully execute mimicry attacks against six state-of-the-art binary function classifiers representing different model architectures without requiring direct interaction with them. We further validate our approach with a practical demonstration, involving a keylogger and a wiper concealed within benign-looking functions embedded in an application. This work, to our best knowledge, is the first to demonstrate such a mimicry attack in a black-box, zero-query context, raising important questions about the reliability and security of existing machine learning-based binary function classifiers.

---


### 513. [SomaliWeb v1: A Quality-Filtered Somali Web Corpus with a Matched Tokenizer and a Public Language-Identification Benchmark](https://arxiv.org/abs/2605.18232)

**<font color=#1a73e8>作者：</font>** Khalid Yusuf Dahir  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Somali is a Cushitic language of the Horn of Africa with ~25 million speakers, yet no documented dedicated Somali pretraining corpus with a companion tokenizer and language-identification benchmark has been publicly released. Existing Somali text appears either inside multilingual distributions (HPLT v2, CC100, MADLAD-400, OSCAR, mC4) or in small, undocumented Somali-only uploads on Hugging Face. We introduce SomaliWeb v1, a quality-filtered Somali corpus of 819,322 documents (~303M tokens) built from three upstream sources (HPLT v2, CC100, Somali Wikipedia) through a six-stage reproducible pipeline. We release (i) the corpus, (ii) a matched BPE-16K tokenizer, and (iii) the first public side-by-side Somali benchmark of three production language identifiers. Our measurements reveal concrete quality defects in existing distributions: HPLT v2's "cleaned" Somali release retains 17.3% byte-exact duplicates, 56.1% of its documents contain fixable mojibake, and 10.7% of its byte-unique documents are near-duplicates at Jaccard tau=0.80. Our BPE-16K tokenizer emits 40.2% fewer tokens than GPT-4's cl100k_base on FLORES-200 Somali devtest as a tokenizer-level measurement; downstream language-model perplexity comparisons are deferred to a follow-up release.

---


### 514. [Enhancing Train-Free Infinite-Frame Generation for Consistent Long Videos](https://arxiv.org/abs/2605.18233)

**<font color=#1a73e8>作者：</font>** X. Feng, J. Zhu, M. Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Without incurring significant computational overhead, train-free long video generation aims to enable foundation video generation models to produce longer videos. Frame-level autoregressive frameworks, e.g., FIFO-diffusion, offer the advantage of generating infinitely long videos with constant memory consumption. However, the mismatch between training and inference, coupled with the challenge of maintaining long-term consistency, limits the effective utilization of foundation models. To mitigate these concerns, we propose \textbf{MIGA}, a novel infinite-frame long video generation method. Firstly, we propose an effective two-stage alignment mechanism that mitigates the training-inference gap by reducing the excessive noise span fed to the model. We then introduce an innovative dual consistency enhancement mechanism, where the self-reflection approach corrects early high-noise frames and the long-range frame guidance approach leverages later low-noise frames with broad coverage to steer generation, jointly improving temporal consistency. Extensive experiments on VBench and NarrLV demonstrate the state-of-the-art performance of MIGA. Our project page is available at this https URL.

---


### 515. [Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning](https://arxiv.org/abs/2605.18238)

**<font color=#1a73e8>作者：</font>** Yuyang Ji, Yixuan Shen, Anil Jain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital entities such as AI agents and humanoid robots increasingly operate alongside real humans, yet their identity infrastructure is based on credentials rather than embodied biometric identity. We introduce Biometric Identity Provisioning (BIP), a new problem and solution framework that addresses: given an enrollment gallery of real human identities, provision virtual identities that are non-colliding with every enrolled identity, maintain sufficient inter-class separability, and are realizable as high-fidelity face images. The key geometric insight is that real face identities occupy a low-dimensional subspace of the embedding hypersphere, leaving no residual subspace for virtual identities. Hence, virtual identities must instead be allocated as unclaimed gaps within the real face manifold itself. BIP is therefore a constrained packing problem: available gaps vastly exceed any foreseeable enrollment scale, and provisioned identities remain non-colliding even as new real identities are subsequently enrolled. Grounded in this geometry, our repulsion-based allocation is not bounded by any fixed provisioning count; we demonstrate 10M non-colliding virtual identity embeddings against a gallery of 360K real identities. Realizing these embeddings as face images requires a generator that operates outside the training distribution of real face images; we introduce GapGen, a gap-aware generator trained with a curriculum that progressively extends synthesis into non-colliding regions, validated at 1M photorealistic virtual face images. We further construct v-LFW, a virtual counterpart to LFW face dataset, with protocols for virtual face verification, cross-reality matching, real-vs-virtual detection, and unified recognition and detection.

---


### 516. [Privacy Preserving Reinforcement Learning with One-Sided Feedback](https://arxiv.org/abs/2605.18246)

**<font color=#1a73e8>作者：</font>** Lin William Cong, Guangyan Gan, Hanzhang Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study reinforcement learning (RL) in multi-dimensional continuous state and action spaces with one-sided feedback, where the agent receives partial observations of the state and obtains reward information for only a subset of the state-action space at each time step. This setting introduces substantial challenges in both learning efficiency and privacy preservation. To address these challenges, we propose POOL, a novel privacy-preserving RL algorithm. We conduct a comprehensive theoretical analysis of POOL, deriving a sample complexity bound that matches the known lower bounds for non-private RL. Here, E_rho denotes the privacy parameter, H is the time horizon, and alpha is the optimality-gap parameter. Our findings show that it is possible to enforce strong privacy guarantees while maintaining high learning efficiency, marking a significant step toward practical, privacy-aware RL in multi-dimensional environments with one-sided feedback.

---


### 517. [GaussianZoom: Progressive Zoom-in Generative 3D Gaussian Splatting with Geometric and Semantic Guidance](https://arxiv.org/abs/2605.18252)

**<font color=#1a73e8>作者：</font>** Jiale Shi, Jiarui Hu, Zesong Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce GaussianZoom, a generative zoom-in 3D reconstruction system with an iterative progressive framework that combines geometry-consistent scene modeling and multi-scale semantic reasoning to enable high-fidelity extreme zoom-in rendering from low-resolution inputs. To achieve this, we develop a novel multi-view consistent super-resolution module with depth-based feature warping and VLM-driven detail synthesis, ensuring accurate multi-view correspondence while enriching fine-scale appearance beyond the observed resolution. To support zooming across large magnification ranges, we further introduce a new expandable continuous Level-of-Detail hierarchy that dynamically modulates Gaussian visibility for smooth, alias-free cross-scale rendering. Experiments on Mip-NeRF360 and Tanks\&Temples demonstrate that GaussianZoom achieves superior perceptual quality, multi-view consistency, and robustness under extreme magnification, establishing a strong baseline for generative zoom-in 3D scene reconstruction.

---


### 518. [RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting](https://arxiv.org/abs/2605.18263)

**<font color=#1a73e8>作者：</font>** Ji Shi, Xianghua Ying, Bowei Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis with high visual quality. However, existing methods struggle with semi-transparent specular surfaces that exhibit both complex reflections and clear transmission, often producing blurry reflections or overly occluded transmission. To address this, we present RT-Splatting, a framework that disentangles each Gaussian's geometric occupancy from its optical opacity. This factorization yields a unified surface-volume scene representation with a single set of Gaussian primitives. Our hybrid renderer interprets this representation both as a surface to capture high-frequency reflections and as a volume to preserve clear transmission. To mitigate the ambiguity in jointly optimizing reflection and transmission, we introduce Specular-Aware Gradient Gating, which suppresses misleading gradients from highly specular regions into the transmission branch, effectively reducing distracting floaters. Experiments on challenging semi-transparent scenes show that RT-Splatting achieves state-of-the-art performance, delivering high-fidelity reflections and clear transmission with real-time rendering. Moreover, our factorization naturally enables flexible scene editing. The project page is available at this https URL.

---


### 519. [SRC-Flow: Compact Semantic Representations Enable Normalizing Flows for Image Generation](https://arxiv.org/abs/2605.18267)

**<font color=#1a73e8>作者：</font>** Longtao Jiang, Jiangmin Bao, Zhendong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Normalizing flows (NFs) provide exact likelihoods and deterministic invertible sampling, but have historically lagged behind diffusion models for large-scale image generation. We identify a key obstacle: NFs are required to learn a single invertible transport over the full ambient space, making them highly sensitive to high-dimensional representations. This leads to a semantic-capacity mismatch in modern visual representation spaces, where semantic information is compact but encoded in overcomplete features. We propose SRC-Flow, which introduces a Semantic Representation Compressor (SRC) to compact high-dimensional RAE features into a low-dimensional semantic space before flow modeling and preserve reconstruction through the frozen RAE decoder. This compact space reduces the modeling burden of NFs and enables effective likelihood-based generation in semantic representation space. We further adopt constant noise regularization tailored to the fixed unconditional bijection learned by flows. On ImageNet $256 \times 256$ and $512 \times 512$, SRC-Flow achieves state-of-the-art generation quality among normalizing flow methods, with gFID scores of 1.65 and 2.07 under classifier-free guidance, while retaining exact likelihood computation in the compact semantic representation space and deterministic invertible sampling at the flow level. Codes and models will be available at this https URL.

---


### 520. [Temporal Task Diversity: Inductive Biases Under Non-Stationarity in Synthetic Sequence Modelling](https://arxiv.org/abs/2605.18281)

**<font color=#1a73e8>作者：</font>** Afiq Abdillah Effiezal Aswadi, Oliver Britton, Ross Baker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning science often assumes that neural networks learn from a fixed data distribution. However, many practically important learning problems involve data distributions that change throughout training. How does such non-stationarity impact the inductive biases of deep learning towards models with different structural, generalisation, and safety properties? A fruitful testbed for studying inductive bias is in-context linear regression sequence modelling, where small transformers display strikingly different generalisation patterns depending on the diversity of the (fixed) training task distribution. In this paper, we explore the effect of diversifying the task distribution across training time, finding that such temporal diversity leads to an increased bias towards generalisation over memorisation.

---


### 521. [StableVLA: Towards Robust Vision-Language-Action Models without Extra Data](https://arxiv.org/abs/2605.18287)

**<font color=#1a73e8>作者：</font>** Yiyang Fu, Chubin Zhang, Shukai Gong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> It is infeasible to encompass all possible disturbances within the training dataset. This raises a critical question regarding the robustness of Vision-Language-Action (VLA) models when encountering unseen real-world visual disturbances, particularly under imperfect visual conditions. In this work, we conduct a systematic study based on recent state-of-the-art VLA models and reveal a significant performance drop when visual disturbances absent from the training data are introduced. To mitigate this issue, we propose a lightweight adapter module grounded in information theory, termed the Information Bottleneck Adapter (IB-Adapter), which selectively filters potential noise from visual inputs. Without requiring any extra data or augmentation strategies, IB-Adapter consistently improves over the baseline by an average of 30%, while adding fewer than 10M parameters, demonstrating notable efficiency and effectiveness. Furthermore, even with a 14x smaller backbone (0.5B parameters) and no pre-training on the Open X-Embodiment dataset, our model StableVLA achieves robustness competitive with 7B-scale state-of-the-art VLAs. With negligible parameter overhead (<10M), our approach maintains accuracy on long-horizon tasks and surpasses OpenPi under both synthetic and physical visual corruptions.

---


### 522. [Collision-Resistant Single-Pass Method for Unsupervised Fine-Grained Image Hashing](https://arxiv.org/abs/2605.18288)

**<font color=#1a73e8>作者：</font>** Anh-Kiet Duong, Petra Gomez-Krämer, Jean-Michel Carozza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised fine-grained image hashing aims to learn compact binary codes that preserve subtle visual differences among highly similar instances without manual annotations. However, most existing methods neglect collision resistance, leading to identical hash codes for slightly semantically different samples. In this paper, we propose Collision-Resistant Single-Pass Self-Supervised Semantic Hashing (CS3H), a collision-resistant framework that directly optimizes Hamming-space similarity via a single-pass normalized Hamming distance loss to produce well-separated binary representations. We further introduce a collision-sensitive attention module to emphasize rare and discriminative local patterns, reducing hash collisions and improving fine-grained discrimination. Experiments on multiple benchmarks show that CS3H consistently outperforms state-of-the-art methods in retrieval accuracy while achieving superior collision resistance with minimal computational overhead.

---


### 523. [MEEDAV: A Synchronous Web Viewer for EEG, Eye-Tracking and Speech Data](https://arxiv.org/abs/2605.18296)

**<font color=#1a73e8>作者：</font>** Jan Pijálek, Karel Vlk, Ondřej Bojar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> MEEDAV is an open-source web-based application for the synchronised visualisation of electroencephalography (EEG), eye-tracking, and audio data collected in psycholinguistic research. While originally developed for the Eyetracked Multi-Modal Translation (EMMT) corpus, which uses four-channel EEG data from the Muse 2 headband, MEEDAV also supports higher-density EEG setups thanks to its channel-agnostic processing pipeline. The system performs time alignment across all modalities and provides optional ICA-based EEG denoising. It features interactive Plotly visualisations, including unified EEG-audio-gaze timelines, gaze-intensity plots, event markers, and spatial heatmaps of fixation/saccade patterns. Researchers can filter by participant and stimulus, inspect raw versus cleaned signals, and compute cross-modal correlations. All processing is handled in real time, with a modular backend that supports local file access or GitHub-based streaming. Although initially tailored to the structure of the EMMT dataset, MEEDAV demonstrates a generalisable approach to multimodal data exploration and offers a lightweight, browser-accessible solution for cognitive neuroscience and translation studies.

---


### 524. [SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning](https://arxiv.org/abs/2605.18299)

**<font color=#1a73e8>作者：</font>** Yufei Ma, Zihan Liang, Ben Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search-augmented reasoning agents interleave internal reasoning with calls to an external retriever, and their performance relies on the quality of each issued query. However, under outcome-reward reinforcement learning, every search decision in a rollout shares the same trajectory-level reward, leaving individual queries without step-specific credit. Recent process-supervision approaches address this gap by drawing step-level signals from outside the policy, relying either on a much larger teacher model, or on sub-question annotations produced by a stronger external system. In contrast, we propose SD-Search, which derives step-level supervision from the policy itself through on-policy hindsight self-distillation, requiring neither an external teacher nor additional annotations. In SD-Search, a single model plays two roles that differ only in conditioning: a student that sees only the context available at inference time, and a teacher that additionally conditions on a compact hindsight block summarizing the search queries and final outcomes of a group of rollouts sampled from the same question. Since the teacher knows how each rollout unfolded and which ones succeeded, its query distribution implicitly marks which decisions were worth making, and the student is trained to recover this behavior by minimizing the token-level Jensen--Shannon divergence to the teacher at search-query positions. This layers a dense, step-level signal on top of GRPO's coarse trajectory reward. Crucially, this signal is produced by the policy itself within the standard RL training loop, without external model inference, auxiliary annotation pipeline, or additional training stage.

---


### 525. [Dynamic Elliptical Graph Factor Models via Riemannian Optimization with Geodesic Temporal Regularization](https://arxiv.org/abs/2605.18316)

**<font color=#1a73e8>作者：</font>** Chuansen Peng, Xiaojing Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring time-varying graph structures from high-dimensional nodal observations is a fundamental problem arising in neuroscience, finance, climatology, and beyond. Two intrinsic challenges govern this problem: maintaining the \emph{temporal coherence} of the latent graph across successive observation windows, and respecting the \emph{intrinsic Riemannian geometry} of the symmetric positive definite manifold on which precision matrices naturally reside, a curved space whose geodesic structure departs fundamentally from that of the ambient Euclidean space. In this paper we propose dynamic estimation on the Grassmann manifold with a factor model (\textsc{Degfm}), a novel algorithm that jointly addresses both challenges. We model the time-varying precision matrix sequence as a low-rank-plus-diagonal structure governed by a latent elliptical graph factor model, which drastically reduces the effective parameter count and enables reliable estimation in the challenging small-sample regime. Temporal coherence is enforced through a Riemannian geodesic penalty defined on the Grassmann manifold, ensuring that the estimated graph trajectory is smooth with respect to the intrinsic geometry rather than the ambient Euclidean space. To solve the resulting non-convex optimization problem over Grassmann-manifold-valued sequences subject to the LRaD constraint, we derive an efficient Riemannian gradient descent algorithm that respects the manifold structure at every iterate and rigorously establish its convergence to a stationary point. Extensive experiments on both synthetic benchmarks and real-world datasets demonstrate that \textsc{Degfm} consistently outperforms state-of-the-art baselines across all evaluation metrics, confirming the practical effectiveness of the proposed framework.

---


### 526. [The Symmetries of Three-Layer ReLU Networks](https://arxiv.org/abs/2605.18319)

**<font color=#1a73e8>作者：</font>** Johanna Marie Gegenfurtner, Moritz Grillo, Guido Montúfar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a framework for analyzing parameter symmetries in deep ReLU networks and obtain a complete characterization of the generic parameter fibers for three-layer bottleneck architectures. Our approach provides explicit semi-algebraic descriptions of these fibers and yields a polynomial time algorithm for deciding functional equivalence of two parameters. The symmetries include discrete and continuous transformations arising from layer composition, and depend on whether deeper layers hide or preserve geometric structure from preceding layers. Finally, we show that some of these symmetries induce local conservation laws along gradient flow, while others do not.

---


### 527. [ISEP: Implicit Support Expansion for Offline Reinforcement Learning via Stochastic Policy Optimization](https://arxiv.org/abs/2605.18320)

**<font color=#1a73e8>作者：</font>** Yifei Chen, Shaoqin Zhu, Xiaoqiang Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning methods typically enforce strict constraints to ensure safety; yet this rigidity often prevents the discovery of optimal behaviors outside the immediate support of the behavior policy. To address this, we propose Implicit Support Expansion via stochastic Policy optimization (ISEP), which leverages a value function interpolated between in-distribution data and policy samples to implicitly expand the feasible action support. This mechanism "densifies" high-reward regions, creating a navigable path for policy improvement while theoretically guaranteeing bounded value error. However, optimizing against this expanded support creates a multimodal landscape where standard deterministic averaging leads to mode collapse and invalid actions. ISEP mitigates this via a stochastic action selection strategy, optimizing the policy by stochastically alternating between conservative cloning and optimistic expansion signals. We instantiate this framework as ISEP-FM using Conditional Flow Matching utilizing classifier-free guidance to effectively capture the interpolated value signal.

---


### 528. [Improved Baselines with Representation Autoencoders](https://arxiv.org/abs/2605.18324)

**<font color=#1a73e8>作者：</font>** Jaskirat Singh, Boyang Zheng, Zongze Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation Autoencoders (RAE) replace traditional VAE with pretrained vision encoders. In this paper, we systematically investigate several design choices and find three insights which simplify and improve RAE. First, we study a generalized formulation where the representation is defined as sum of the last k encoder layers rather than solely the final layer. This simple change greatly improves reconstruction without encoder finetuning or specialized data (e.g., text, faces). Second, we study the prevalent assumption that RAE (using pretrained representation as encoder) replaces representation alignment (REPA), which distills the same representation to intermediate layers instead. Through large-scale empirical analysis, we uncover a surprising finding: RAE and REPA exhibit complementary working mechanisms, allowing the same representation to be used as both encoder and target for intermediate diffusion layers. Finally, the original RAE struggles with classifier-free guidance (CFG) and requires training a second, weaker diffusion model for AutoGuidance (AG). We show that REPA itself can be viewed as x-prediction in RAE latent space. By simply re-parameterizing the output of the DiT model, it can provide guidance for "free". Overall, RAEv2 leads to more than 10x faster convergence over the original RAE, achieving a state-of-the-art gFID of 1.06 in just 80 epochs on ImageNet-256. On FDr^k, RAEv2 achieves a state-of-the-art 2.17 at just 80 epochs compared to the previous best 3.26 (800 epochs) without any post-training. This motivates EP_FID@k (epochs to reach unguided gFID <= k) as a measure of training efficiency. RAEv2 attains an EP_FID@2 of 35 epochs, versus 177 for the original RAE. We also validate our approach across diverse settings for text-to-image generation and navigation world models, showing consistent improvements. Code is available at this https URL.

---


### 529. [Causely: A Causal Intelligence Layer for Enterprise AI A Benchmark Study on SRE and Reliability Workflows](https://arxiv.org/abs/2605.18327)

**<font color=#1a73e8>作者：</font>** Dhairya Dalal, Endre Sara, Ben Yemini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents deployed into SRE workflows currently derive their understanding of environment state from raw observability telemetry at query time, paying a semantic-interpretation tax in tokens, latency, and inferential reliability. We propose Causely, a causal intelligence layer that maintains a structured representation of environment topology, attribute dependencies, and causal relationships that are anchroed to a ontological representation of the managed environment. Causely transforms raw telemetry into a live, queryable model providing the semantic and causal foundation AI agents require to diagnose, evaluate impact, and act safely in production. We evaluate this value proposition through a benchmark study conducted in a controlled setting with injected faults in a 24-microservice OpenTelemetry demo application. Our experiments compare four agent configurations (Claude Code, OpenAI Codex, HolmesGPT with Sonnet and Gemini backends). Experiments are run with and without access to Causely under two scenarios: an active incident and a healthy baseline. On the active-fault scenario, causal grounding reduces mean time-to-diagnosis by 63\%, mean token consumption by 60\%, and mean tool-call count by 78\%, compressing the investigation footprint by 4.8$\times$ and lowering direct API cost per run by 57\%; root-cause-diagnosis accuracy rises from 75\% to 100\%.

---


### 530. [CineMatte: Background Matting for Virtual Production and Beyond](https://arxiv.org/abs/2605.18328)

**<font color=#1a73e8>作者：</font>** Yuanjian He, Chen Zhang, Fasheng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LED Virtual Production (VP) uses large LED volumes to render backgrounds in real time, enabling in-camera visual effects but making post-shot changes labor-intensive. We address this with CineMatte, a robust background matting framework for VP and beyond. CineMatte employs a cross-attention-conditioned design. Instead of concatenating the background with the input, CineMatte employs a Siamese, frozen DINOv3 Vision Transformer with shared weights to encode the input frame and the captured background separately. A cross-attention module compares the two streams to predict the foreground, preserving pretrained semantics and improving robustness to background shifts. Previous ViT-based matting models use a parallel convolutional "detail branch" to recover fine details, which can cause boundary artifacts in real-world samples due to semantic misalignment with the backbone. We instead replace it with a pretrained, image-guided feature upsampler, which largely mitigates the problem. We also introduce CineMatte-4K, a 4K HDR image-video dataset captured on a professional LED VP stage. To the best of our knowledge, the image subset is the first dataset for VP matting and is non-synthetic, obtained via green-screen insertion; the video subset includes camera motion with tracked trajectories so that arbitrary backgrounds can be rendered later with correct parallax. Across CineMatte-4K and public benchmarks (VideoMatte240K, YouTubeMatte), CineMatte not only excels in VP but also generalizes robustly to real-world footage.

---


### 531. [Lost in the Folds: When Cross-Validation Is Not a Deep Ensemble for Uncertainty Estimation](https://arxiv.org/abs/2605.18329)

**<font color=#1a73e8>作者：</font>** Kirscher Tristan, Bujotzek Markus, Kirchhoff Yannick 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ensemble disagreement is widely used as a proxy for epistemic uncertainty in medical image segmentation. In practice, many studies form ensembles via K-fold cross-validation (CV), yet refer to them as ``deep ensembles'' (DE). Because CV members are trained on different data subsets, their disagreement mixes seed-driven variability with data-exposure effects, which can change how uncertainty should be interpreted. We audit recent segmentation uncertainty studies and find that terminology--implementation mismatches are common. We then compare a standard 5-fold CV ensemble to a 5-member DE (fixed training set, different random seeds) under otherwise identical configurations on three multi-rater segmentation datasets spanning three modalities. We evaluate uncertainty for calibration, failure detection, ambiguity modeling, and robustness under distribution shift. DE match segmentation accuracy while improving calibration and failure detection, whereas CV ensembles sometimes correlate more strongly with inter-rater variability on the studied datasets. Thus, ensemble construction should be chosen to match the research question: DE for reliability-oriented use (e.g., selective referral/failure detection) and CV ensembles as a proxy for ambiguity. We provide a lightweight nnU-Net modification enabling DE training within the default pipeline.

---


### 532. [3D Skew Gaussian Splatting with Any Camera Trajectory Visualization Engine](https://arxiv.org/abs/2605.18334)

**<font color=#1a73e8>作者：</font>** Beizhen Zhao, Yifan Zhou, Gaochao Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) has revolutionized real-time photorealistic view synthesis, its fundamental reliance on symmetric Gaussian distributions introduces visual artifacts that hinder accurate spatial data exploration. Specifically, symmetric kernels struggle to capture shape and color discontinuities , which cause blurriness and primitive redundancy that mislead human perception during visual analysis. To address these visualization barriers, we introduce 3D Skew Gaussian Splatting (3DSGS), a novel framework that significantly enhances the structural fidelity and compactness of explicit scene representations. Our key insight lies in extending the standard primitive to a general Skew Gaussian counterpart. This generalized primitive inherits the highly efficient rasterization properties of standard Gaussians while gaining intrinsic asymmetric modeling capabilities. We couple this with an enhanced opacity representation to better handle complex transparency, alongside a depth-aware densification strategy that intelligently manages primitive allocation. Furthermore, to make these advancements actionable for real-world visual analytics, we re-derive the CUDA rasterization pipeline to universally support both symmetric and skew Gaussians, integrating it into a decoupled, free-camera interactive visualization engine. Extensive experiments demonstrate that 3DSGS achieves superior rendering quality and structural compactness, particularly in regions with intricate details, while maintaining the real-time frame rates necessary for fluid interactive exploration. Supplementary derivations and visual results are available at \textbf{\textit{this https URL}}.

---


### 533. [Infini-News: Efficiently Queryable Access to 1.3 Billion Processed Common Crawl News Articles](https://arxiv.org/abs/2605.18337)

**<font color=#1a73e8>作者：</font>** Ruggero Marino Lazzaroni, Jana Lasser, Kirill Solovev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale news corpora support a wide range of research in Computational Social Science and NLP, yet access remains constrained: commercial archives impose prohibitive costs and licensing restrictions, while open alternatives like Common Crawl's CC-News require terabyte-scale storage and computationally intensive processing. We present Infini-News, a retrieval toolkit and index for the entire CC-News archive from August 2016 to the latest available snapshot. Our contributions are threefold. First, we extract, clean the text, and parse the structured metadata of over 1.35B articles. Second, we enrich the corpus with language detection using three frontier language classifiers (GlotLID, lingua, and CommonLingua), and with multi-source geographic attribution that resolves a country of origin for 83.4% of articles across 222 countries. Third, we construct Infini-gram indexes: suffix-array structures that let researchers search the full archive for arbitrary text patterns in sub-second time. Together, these resources lower the barrier to longitudinal, cross-national media research.

---


### 534. [Focused Forcing: Content-Aware Per-Frame KV Selection for Efficient Autoregressive Video Diffusion](https://arxiv.org/abs/2605.18346)

**<font color=#1a73e8>作者：</font>** Peiliang Cai, Evelyn Zhang, Jiacheng Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in autoregressive video diffusion have enabled sequential and streaming video generation. However, long-horizon generation requires increasingly large KV caches, making efficient compression without sacrificing quality challenging. Existing methods mostly select historical frames based on attention scores, but their context decisions remain coarse. When multiple frames are generated in the same chunk, these methods often apply a shared history selection to the whole chunk, score historical frames solely by attention, and assign head-wise budgets either uniformly or by attention-pattern heuristics rather than explicit head-importance estimation. We show that frames within the same generated chunk can depend on distinct historical frames, that the same historical frame can receive different attention scores as its relative temporal distance to the current frames changes, and that masking different heads induces unequal generation degradation. Motivated by these findings, we propose \textbf{Focused Forcing}, a training-free KV selection method that focuses cached history along both generated-frame and head dimensions. For each generated frame, Focused Forcing preserves the most relevant and distinctive historical frames by combining attention scores with diversity scores of historical frames, while assigning larger budgets to heads with higher estimated importance. Across multiple autoregressive generation paradigms, Focused Forcing achieves up to $\textbf{1.48}\times$ end-to-end acceleration without training, while \textbf{improving visual quality and text alignment}. \textit{Our code will be released on GitHub.}

---


### 535. [Optimising CSRNet with parameter-free attention mechanisms for crowd counting in public transport](https://arxiv.org/abs/2605.18349)

**<font color=#1a73e8>作者：</font>** Aida Rostamza, Enrico Del Re, Joshua Cherian Varughese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Occupancy estimation and crowd counting are critical tasks in designing smart and efficient public transport vehicles. Given that public transport loading can vary from sparse to crowded, classical models for occupancy estimation must be adapted to suit this purpose. Attention mechanisms have shown remarkable capability in enhancing the representational power of deep neural networks for crowd counting in congested scenes with occlusion, complex backgrounds, and perspective distortion. However, conventional approaches, often implemented as parameterized sub-networks within convolutional layers, inevitably increase model size and computational cost, limiting deployment on resource-constrained edge devices. This paper investigates the effectiveness of state-of-the-art parameter-free attention mechanisms for crowd counting and density map estimation in highly congested scenes. We evaluate channel-wise (PFCA), spatial-wise (SA), and 3-D (SimAM) modules and compare their performance with parameterized attention modules constrained to introduce no more than 1% additional parameters. Furthermore, we present a novel combination of attention mechanisms that combines the strengths of PFCA and SA (PFCASA) customized for analyzing video streams onboard public transport systems. Using CSRNet as the backbone, experiments on the ShanghaiTech dataset demonstrate that parameter-free attention mechanisms achieve comparable or superior accuracy without introducing additional model parameters. A detailed performance analysis further reveals that PFCASA outperforms other attention modules in scenes with fewer than 40 individuals, while PFCA shows greater effectiveness as crowd density increases, underscoring their potential applicability for integration into smart public transport modalities.

---


### 536. [Decoupled Conformal Optimisation: Efficient Prediction Sets via Independent Tuning and Calibration](https://arxiv.org/abs/2605.18354)

**<font color=#1a73e8>作者：</font>** Fanyi Wu, Lihua Niu, Samuel Kaski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian conformal optimisation methods often use the same held-out data both to search for efficient prediction sets and to certify coverage or risk. This coupling is natural for high-probability risk-control guarantees, but it is not necessary when the target is standard finite-sample marginal conformal coverage. We propose Decoupled Conformal Optimisation (DCO), a train-tune-calibrate design principle that uses an independent tuning split for efficiency-oriented structural selection and a fresh calibration split for the final conformal quantile. Conditional on the tuned structure, standard split-conformal exchangeability yields finite-sample marginal coverage for any candidate class, without a confidence parameter or multiple-testing correction. DCO therefore targets a different finite-sample guarantee from PAC-style methods: marginal conformal coverage rather than high-probability risk control. Under consistency assumptions on the coupled risk bound, the two approaches nevertheless converge to the same population threshold. Across classification and regression benchmarks, including ImageNet-A, CIFAR-100, Diabetes, California Housing, and Concrete, DCO tracks the nominal coverage level closely while often reducing average prediction-set size or interval width relative to PAC-style calibration. On ImageNet-A, for example, the average set size decreases from $26.52$ to $25.26$ and the 95th-percentile set size from $58.95$ to $53.73$; on Diabetes, the average interval width decreases from $2.098$ to $1.914$.

---


### 537. [Proximal basin hopping: global optimization with guarantees](https://arxiv.org/abs/2605.18364)

**<font color=#1a73e8>作者：</font>** Guillaume Lauga, Cesare Molinari, Samuel Vaiter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global optimization is a challenging problem, with plenty of algorithms displaying empirical success, but scarce theoretical backing. In this work, we propose a new theoretical framework called Proximal Basin Hopping (PBH), carefully tailored to combine proximal optimization and local minimization. We use it to construct a practical algorithm that converges to the global minimizer with high probability, when using a finite amount of samples. Proximal Basin Hopping outperforms well known algorithms with theoretical backing on standard synthetic hard functions, and real problems such as fitting scaling laws for deep learning. Furthermore, the higher the dimension, the better the performance gap.

---


### 538. [GeoFlow: Enforcing Implicit Geometric Consistency in Video Generation](https://arxiv.org/abs/2605.18365)

**<font color=#1a73e8>作者：</font>** Jan Ackermann, Shengqu Cai, Boyang Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating geometrically consistent videos remains an open challenge: text-to-video diffusion models trained on web-scale data treat geometry only implicitly, leading to object deformation, texture drift, and non-rigid backgrounds under camera motion. Existing solutions either improve consistency as a byproduct, apply only to static scenes or realign the latent space of the model completely. We introduce a geometry-consistency reward that directly measures whether motion in a generated video is compatible with a coherent scene. Our key insight is that in physically consistent videos, background motion should be explainable by rigid camera-induced flow, while independently moving objects should preserve appearance identity along motion trajectories. We operationalize this using optical flow, depth--pose predictions, and feature-based correspondence to separate rigid and dynamic regions and evaluate their respective consistency. Integrating this reward with reinforcement fine-tuning transforms geometric consistency from an emergent property into an explicit optimization objective for video generators. The approach is model agnostic and applies to diverse dynamic scenes containing both camera and object motion. Experiments show substantial reductions in temporal geometric artifacts over strong baselines while preserving perceptual quality. Code and model weights are published.

---


### 539. [Beyond Square Roots: Explicit Memory-Efficient Factorization for Multi-Epoch Private Learning](https://arxiv.org/abs/2605.18379)

**<font color=#1a73e8>作者：</font>** Nikita P. Kalinin, Aki Rehn, Joel Daniel Andersson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Correlated-noise mechanisms are among the most promising approaches for improving the utility of differentially private model training, but rigorous guarantees require explicit, analyzable factorizations, and practical deployment requires memory efficiency. Recent works have developed banded inverse factorizations, which address both requirements by exploiting a banded structure in the correlation matrix. The bandwidth controls the size of the noise buffer used to correlate noise across iterations, and thus governs the tradeoff between utility and memory cost. Existing factorizations highlight this tradeoff: DP-$\lambda$CGD achieves high memory efficiency by using only a one-step noise buffer, but this limits its utility gains, while the banded inverse square root (BISR) factorization exploits larger correlation windows and is asymptotically optimal for large bandwidths but performs poorly at low bandwidths. We propose $\gamma$-BIFR, a unified generalization of both factorizations. In the low-memory, low-bandwidth regime, $\gamma$-BIFR significantly improves RMSE, amplified RMSE, and private training performance, while yielding tighter theoretical guarantees for multi-participation error in multi-epoch training.

---


### 540. [Generating Physically Consistent Molecules with Energy-Based Models](https://arxiv.org/abs/2605.18381)

**<font color=#1a73e8>作者：</font>** Christoph Griesbacher, Lea Bogensperger, Andreas Habring 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecules in equilibrium follow a Boltzmann distribution, making the underlying energy landscape a physically grounded modeling objective. However, such landscapes are difficult to learn from data and, once learned, hard to sample from. Diffusion and flow-matching models sidestep these difficulties by learning a time-conditional score or transport field between noise and data, losing the energy inductive bias in exchange for a more tractable training objective. We introduce EBMol, an energy-based model (EBM) that restores this inductive bias by learning an atom-additive scalar potential without explicit simulation during training. Our method employs a flow-inspired Restoring Field Matching objective to approximate the energy landscape. We adopt the Mirror-Langevin algorithm for sampling, enabling unified updates of atomic positions and types, and incorporate parallel tempering for inference-time compute scaling. EBMol is the first EBM for 3D molecular generation to achieve state-of-the-art performance on QM9 and GEOM-Drugs. Moreover, we show that the learned energy landscape serves as a principled quality metric for ranking and filtering configurations, and demonstrate controllable generation without retraining through shape-steered sampling via potential composition and zero-shot linker design.

---


### 541. [Graph Hierarchical Recurrence for Long-Range Generalization](https://arxiv.org/abs/2605.18387)

**<font color=#1a73e8>作者：</font>** Stefano Carotti, Marco Pacini, Alessio Gravina 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) and Graph Transformers (GTs) are now a fundamental paradigm for graph learning, combining the representation-learning capabilities of deep models with the sample efficiency induced by their inductive biases. Despite their effectiveness, a large body of work has shown that these models still face fundamental limitations in tasks that require capturing correlations between distant regions of a graph. To address this issue, we introduce Graph Hierarchical Recurrence (GHR), a novel framework that operates jointly on the input graph and on a hierarchical abstraction obtained through pooling. We also show that the limitations of existing models are even more pronounced in out-of-range generalization, where test instances involve interactions over distances longer than those observed during training. By contrast, despite its simple design, GHR provides three key advantages: strong performance on long-range dependencies, improved out-of-range generalization, and high parameter efficiency. To corroborate these claims, we show that across a broad set of long-range benchmarks, GHR consistently outperforms existing graph models while using as little as 1% of the parameters of current state-of-the-art models. These results suggest a complementary direction to the current trend of scaling architectures to obtain graph foundation models, indicating that increased model capacity alone may not be sufficient for generalization.

---


### 542. [Spherical Harmonic Optimal Transport: Application to Climate Models Comparisons](https://arxiv.org/abs/2605.18389)

**<font color=#1a73e8>作者：</font>** Pierre Houédry, Iskander Legheraba, Léo Buecher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal transport provides a powerful framework for comparing measures while respecting the geometry of their support, but comes with an expensive computational cost, hindering its potential application to real world use cases. On manifolds, convolutional algorithms based on the heat kernel have been proposed to alleviate this cost, but their theoretical properties remain largely unexplored. We establish that the heat kernel cost converges to the optimal transport cost as time vanishes in the balanced and unbalanced cases. In the specific case of the 2-sphere $\mathbb{S}^2$, we ensure that the associated Sinkhorn divergences retains the desirable geometric and analytic properties of classical optimal transport discrepancies. Moreover, we leverage the harmonic structure of the sphere to derive a fast Sinkhorn algorithm, requiring only $\mathcal{O}(n)$ memory and $\mathcal{O}(n^{3/2})$ time per iteration, with fully dense GPU-friendly operations. We validate its computational efficiency on synthetic data, and discuss its potential use in the evaluation of global climate models, providing both spatial and seasonal insights into models performances.

---


### 543. [Historical Knowledge Graphs for Global Maritime Estimated Time of Arrival](https://arxiv.org/abs/2605.18408)

**<font color=#1a73e8>作者：</font>** Neofytos Dimitriou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate vessel estimated-time-of-arrival forecasts are critical for port operations and decarbonization, yet global-scale travel-time prediction remains difficult without costly contextual data. Herein, I present a methodology for constructing a historical maritime knowledge graph using only Automatic Identification System (AIS) data. First, segmented trajectories are extracted from noisy AIS data using a Gaussian-mixture-model-based preprocessing pipeline. The graph is then constructed by iteratively processing the trajectories and storing speed distributions stratified by vessel type, time of travel, and direction of travel; the resulting global graph comprises 5,433 geohash-3 nodes and 12,334 edges. The graph can be queried to retrieve travel-time predictions between any two location via a hierarchical, priority-based system that uses historical statistics with principled fallback. On a temporally held-out test set, median RMSE is 22.75 min (segment-level) and 30.90 min (trajectory-level), with 69.1% of trajectories within 20% of actual arrival time. On a second external test set, median RMSE is 27.36 min (segment-level) and 37.46 min (trajectory-level), with 62.1% of trajectories within 20%. These results corroborate the promise of our method, enabling global travel-time prediction and providing a strong foundation for just-in-time arrival planning and emissions reduction.

---


### 544. [EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective](https://arxiv.org/abs/2605.18421)

**<font color=#1a73e8>作者：</font>** Yuyao Wang, Zhongjian Zhang, Mo Chi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent benchmarks for Large Language Model (LLM) agents mainly evaluate reasoning, planning, and execution. However, memory is also essential for agents, as it enables them to store, update, and retrieve information over time. This ability remains under-evaluated, largely because existing benchmarks do not provide a systematic way to assess memory mechanisms. In this paper, we study agent memory from a self-evolving perspective and introduce EvoMemBench, a unified benchmark organized along two axes: memory scope (in-episode vs. cross-episode) and memory content (knowledge-oriented vs. execution-oriented). We compare 15 representative memory methods with strong long-context baselines under a standardized protocol. Results show that current memory systems are still far from a general solution: long-context baselines remain highly competitive, memory helps most when the current context is insufficient or tasks are difficult, and no single memory form works consistently across all settings. Retrieval-based methods remain strong for knowledge-intensive settings, whereas procedural and long-term memory methods are more effective for execution-oriented tasks when their stored experience matches the task structure. We hope EvoMemBench facilitates future research on more effective memory systems for LLM-based agents. Our code is available at this https URL.

---


### 545. [Generative Adversarial Learning from Deterministic Processes](https://arxiv.org/abs/2605.18425)

**<font color=#1a73e8>作者：</font>** Joris C. Kühl, Hanno Gottschalk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical AI is being successfully applied to data which does not follow the traditional paradigm of independent and identically distributed (i.i.d.) samples. In fact, physical AI is often trained on data which is not random at all, and is instead derived from chaotic dynamical systems like turbulence.
We aim to explain the empirical success of these methods using the example of generative adversarial networks (GANs), whose statistical learning theory under the i.i.d. assumption is generally well understood. We prove that it is possible, using an infinite-dimensional model of generative adversarial learning (GAL), to learn the invariant distribution of a sufficiently chaotic dynamical system from a single deterministically evolving time series of its states or measurements thereof, and give explicit rates for the convergence to the solution in terms of the Jensen-Shannon divergence.

---


### 546. [A Dataset for the Recognition of Historical and Handwritten Music Scores in Western Notation](https://arxiv.org/abs/2605.18436)

**<font color=#1a73e8>作者：</font>** Pau Torras, Jiří Mayer, Carles Badal 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A large amount of musical heritage has been digitised by memory institutions: libraries, museums, and archives. Nevertheless, the field of Optical Music Recognition (OMR) has struggled with making this music machine-readable, despite advances in deep learning, mostly because no datasets for training systems in realistic conditions were available. The MusiCorpus dataset aims to remedy this situation by providing 1,309 pages of historical sheet music, primarily handwritten, with MusicXML transcriptions and symbol annotations. It is the largest dataset of handwritten music to date and the first dataset containing a realistic and representative sample of musical document collections from memory institutions, suitable for training and evaluating both end-to-end and object detection-based OMR systems and comparing their performance.

---


### 547. [Heterogeneous Tasks Offloading in Vehicular Edge Computing: A Federated Meta Deep Reinforcement Learning Approach](https://arxiv.org/abs/2605.18437)

**<font color=#1a73e8>作者：</font>** Yaorong Huang, Jingtao Luo, Xuechao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vehicular edge computing (VEC) enables latency-sensitive vehicular applications by offloading computation-intensive tasks to nearby edge servers. However, real-world vehicular workloads are typically modeled as heterogeneous directed acyclic graph (DAG) tasks with complex dependency structures, making joint offloading and resource allocation highly challenging. Moreover, distributed MEC deployment raises privacy concerns when collaboratively training learning-based policies.
In this paper, we propose a Federated Meta Deep Reinforcement Learning framework with GAT-Seq2Seq modeling (FedMAGS) for heterogeneous task offloading in VEC systems. The proposed approach leverages Graph Attention Networks to capture DAG dependencies, a Seq2Seq-based policy to generate structured offloading decisions, and federated meta-learning to enable fast adaptation across distributed MEC servers without sharing raw data.
Extensive simulations demonstrate that FedMAGS achieves faster convergence, lower execution delay, and better scalability compared with state-of-the-art baselines. In addition, the federated design preserves data privacy while reducing communication overhead, making the framework well suited for dynamic and large-scale VEC environments.

---


### 548. [What is Holding Back Latent Visual Reasoning?](https://arxiv.org/abs/2605.18445)

**<font color=#1a73e8>作者：</font>** André G. Viveiros, Nuno Gonçalves, André F. T. Martins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can approach complex visual problems by mentally simulating intermediate visual steps, rather than reasoning through language alone. Inspired by this, several works on Vision-Language Models have recently explored chain-of-thought reasoning with continuous latent tokens as intermediate visual imagination steps. In this work, we investigate how recent models leverage such latent tokens. Surprisingly, we find that model accuracy is unaffected when latent tokens are replaced by uninformative ``dummy'' tokens. This indicates that latent tokens play a minimal causal role in the model's final prediction. To better understand this phenomenon, we analyze both the training signal provided by oracle latent representations and the quality of the latent tokens generated at inference time. Our experiments reveal two crucial issues holding back latent visual reasoning: First, in most existing datasets, oracle latent tokens provide limited additional information beyond the original image and do not substantially simplify the task, leading models to ignore them during training and effectively bypassing them at inference time. When fine-tuned on a diagnostic dataset, in which latent tokens provide sufficient support for the final prediction, we show that models can causally rely on them. Second, the latent tokens produced at inference time deviate from their corresponding oracle representations, collapsing to a narrow region and preventing benefits even when the model relies on them. Overall, our findings suggest that future progress in latent visual reasoning depends on two key pillars: high-quality datasets with informative intermediate steps and more precise latent token prediction.

---


### 549. [NeRF-based Spacecraft Reconstruction from Close-Range Monocular Imagery Under Illumination Variability and Pose Uncertainty](https://arxiv.org/abs/2605.18447)

**<font color=#1a73e8>作者：</font>** Antoine Legrand, Renaud Detry, Christophe De Vleeschouwer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous rendezvous and proximity operations around uncooperative, unknown spacecraft are critical for active debris removal and on-orbit servicing missions. A key component of such operations is the offline reconstruction of a 3D model of the target from a set of 2D images. This task is challenging due to two main factors. First, in-orbit illumination conditions exhibit considerable variability, and change rapidly over time. Second, the inaccuracy of pose information in the images, results in 3D reconstruction uncertainty. To overcome these challenges, we propose to extend Neural Radiance Fields with per-image degrees of freedom: a learnable appearance embedding that captures the illumination conditions specific to each image, and an image-specific pose correction term that refines its noisy pose label to increase 3D consistency across images. These parameters add minimal complexity, as they are learned jointly with the NeRF, yet they substantially improve robustness to illumination variability and pose inaccuracies. We validate our approach on three image sets representative of in-orbit operations, demonstrating its effectiveness for offline reconstruction and highlighting its suitability for online reconstruction, an open problem in the field.

---


### 550. [Modelling Customer Trajectories with Reinforcement Learning for Practical Retail Insights](https://arxiv.org/abs/2605.18449)

**<font color=#1a73e8>作者：</font>** Ken Ming Lee, Paul Barde, Maxime C. Cohen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding customer movement within retail spaces is essential for optimizing store layouts. Real-world trajectory data can provide highly accurate insights, but collecting it is costly and often infeasible for many retailers. Heuristics such as Travelling Salesman Problem (TSP) and Probabilistic Nearest Neighbours (PNN) are commonly used as inexpensive approximations, but actual customer trajectories deviate by an average of 28% from shortest paths, highlighting a tradeoff between accuracy and practicality. We propose an agent-based modelling framework that casts customer trajectory prediction as a maximum entropy reinforcement learning (RL) problem, balancing reward maximization with stochasticity to better reflect customers with bounded rationality. Using real-world trajectory data from a convenience store, we show that RL-generated trajectories align more closely with customer behaviour than TSP and PNN, providing more accurate estimates of impulse purchase rates and shelf traffic densities. Furthermore, only RL-based predictions yield repositioning decisions for impulse products that align with those derived from actual trajectory data, resulting in comparable estimated profit gains. Our work demonstrates that RL provides a practical, behaviourally grounded alternative that bridges the gap between oversimplified heuristics and data-intensive approaches, making accurate layout optimization more accessible. To encourage further research, the source code is available on GitHub.

---


> [!TIP]
> 当前位于：**501-550**（第 11/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
