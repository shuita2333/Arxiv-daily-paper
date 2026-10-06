# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 251. [Discrete Action Matching: Learning Stochastic Dynamics from Samples via State Graphs](https://arxiv.org/abs/2610.05071)

**<font color=#1a73e8>作者：</font>** Mikhail Persiianov, Alexander Korotin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning population dynamics from unpaired temporal marginals is an ill-posed inverse problem that requires structural assumptions on the underlying dynamics. We introduce $\textit{Discrete Action Matching}$ (DAM), a finite-state counterpart of Action Matching based on discrete Wasserstein geometry. For a prescribed marginal path and transport geometry, we derive an action-minimization objective for its canonical minimum-kinetic-energy current. Our key observation is that the density dependence of the discrete action reduces to neighboring density ratios. Along an empirical interpolation of the snapshots, DAM first estimates these ratios and then learns an action potential. The learned fields also define a graph-supported Markov sampler. Experiments on controlled synthetic dynamics and real mouse gastrulation data evaluate marginal reconstruction and interpolation. Additional experiments approximate numerical surface-transport paths from paired samples.

---


### 252. [ReDiffNet: Differential RGB-Infrared Learning for Low-Light UAV Oriented Vehicle Detection](https://arxiv.org/abs/2610.05074)

**<font color=#1a73e8>作者：</font>** Qifan Zhang, Ziran Zhou, Ruijie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-light UAV-based RGB-infrared oriented small-vehicle detection is important for nighttime traffic monitoring, emergency response, and urban inspection. Illumination variations, headlight glare, local shadows, and thermal-response degradation cause spatially varying modality reliability, while the small visual extent of vehicles further weakens boundaries, orientation cues, and thermal responses. Accordingly, selecting trustworthy observations based on local modality reliability while further exploiting complementary discriminative information in regions with ambiguous modality preference is key to constructing effective multimodal representations. Based on this insight, we propose ReDiffNet, a reliability-conditioned differential representation network in which modality reliability guides both evidence selection and complementary recovery. Specifically, degradation-aware reliability learning estimates relative spatial reliability, uncertainty-guided differential recovery exploits cross-modal differences to recover complementary cues in ambiguous regions, and reliability-conditioned reconstruction integrates retained and recovered evidence into a unified representation. ReDiffNet achieves 85.3% and 73.9% mAP50 on DroneVehicle and VEDAI, respectively, supporting its effectiveness.

---


### 253. [CGDD-Net: Context-Guided Dynamic Detail Modeling for Retinal Vessel Segmentation](https://arxiv.org/abs/2610.05078)

**<font color=#1a73e8>作者：</font>** Xincheng Li, Xiaoqi Sheng, Xinyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate retinal vessel segmentation requires features that capture vascular geometry while preserving information for fine-scale reconstruction. We propose CGDD-Net, a context-guided dynamic detail modeling network that connects adaptive feature extraction to a shared decoder pathway. Context-Guided Scale-Adaptive Deformable Encoding (CSDE) combines fixed-grid convolution with deformable local attention to capture vascular patterns at multiple spatial extents. Spatially Adaptive Multi-Kernel Gating (SAMG) selects receptive-field responses at each location. Dynamic Cross-Scale Detail Fusion (DCDF) aligns the gated intermediate features and compresses them into an eight-channel representation, which is reused at three decoder resolutions together with selected encoder skips. This design consolidates intermediate information before decoding instead of transferring each middle-stage feature through a separate direct skip. On DRIVE, CHASE\_DB1, STARE, and HRF, CGDD-Net achieves AUC values of 0.9824, 0.9938, 0.9895, and 0.9874, with F1 scores of 0.8323, 0.8102, 0.8510, and 0.8157, respectively. The complete model contains 1.96 million trainable parameters. In cumulative ablations, the full model improves F1 over the internal baseline by 2.48, 0.61, and 3.49 percentage points on DRIVE, CHASE\_DB1, and STARE. Twelve directed cross-dataset experiments further characterize transfer without target-domain adaptation. The results support shared intermediate detail delivery as an effective, parameter-compact architecture for retinal vessel segmentation. Code is available at \url{this https URL}.

---


### 254. [Towards cross-cultural study of folksong lyrics with machine translation](https://arxiv.org/abs/2610.05084)

**<font color=#1a73e8>作者：</font>** Anna Dvořáková, Anna Aljanaki, Danbinaerin Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Music is universally present in human societies. Ethnomusicologists have long been documenting the diverse expressions of human musicality, and comparative musicology has recently brought several studies of folksong to a more global scale. Such cross-cultural research has not been conducted on lyrics: the language barrier has so far prevented work with multi-lingual data. However, Natural Language Processing (NLP) technologies have reached a stage where this language barrier may no longer be prohibitive. Combining folksong lyrics corpora across five languages, we machine-translate them to a pivot language with a pre-trained neural topic model, and we examine the relationship between content and social function within each language, and across languages for wedding songs. As expected, human evaluation of translation results shows that non-Indo-European languages suffer from overall worse translation quality. Experiments with topic models then indicate that the content of lyrics is at best partially related to the social function of folksongs across all languages. These experiments are just first steps into cross-cultural folk musics lyrics analysis; however, they do indicate that a previously unobserved web of cross-cultural relationships beyond ethnomusicological typologies may be uncovered through the study of what people sing across the world's diverse folk musics.

---


### 255. [Direction-Conditioned Policies for Online Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.05087)

**<font color=#1a73e8>作者：</font>** S K Swaminathan, Damiya Gondha, Theyanesh Eswaramoorthy Rajahkrishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive Reinforcement Learning (CRL) learns representations that estimate goal reachability, yet its policy remains conditioned on raw goals and therefore does not directly exploit the geometry encoded by its critic. We introduce Direction-Conditioned Policies (DCP), a method built around a small modification to CRL: DCP selects previously visited states as waypoints during online training and conditions the policy on their direction and distance in representation space. At deployment, DCP applies the same interface directly to the final goal, requiring neither waypoint selection nor planning. Across nine navigation and manipulation tasks, DCP attains higher final success rates than CRL on seven tasks and spends more time near the goal on seven. Controlled maze experiments further show that DCP captures shortest-path geometry more accurately and that the supplied direction causally influences the actor's behavior. We identify waypoint coverage and ranking as limits to exploration, and show that learned candidate generation improves goal reaching in two controlled mazes.

---


### 256. [vMF Sentence LDA: A Spherical Topic Model over Sentence Embeddings](https://arxiv.org/abs/2610.05095)

**<font color=#1a73e8>作者：</font>** Ryotaro Kobayashi, Yuri Murayama, Kiyoshi Izumi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent Dirichlet Allocation (LDA) and models derived from it remain widely used topic models. LDA observes each document as a bag-of-words and models each topic by a categorical distribution over the vocabulary, so that it uses neither the internal structure of the document nor the similarity in meaning between words. Earlier work has responded to this limitation in two ways: many models have introduced embeddings, and some have assigned topics to sentences rather than to words. Their combination, a topic model that observes sentence embeddings, remains little explored. We propose vMF Sentence LDA (vSLDA), which keeps the admixture structure of LDA, observes each sentence as its L2-normalized embedding and models each topic by a von Mises-Fisher (vMF) distribution, which matches the cosine geometry of sentence embeddings. Its per-topic parameter count and per-iteration cost are linear in the embedding dimension, versus quadratic for the full-covariance Gaussian distribution in the existing model over sentence embeddings. We evaluate vSLDA where the limitation is expected to matter most, among topics that share much of their vocabulary: the topics that subdivide the one subject of a collection, and the narrow topics that result when a corpus is divided into a large number of topics. On two corpora, vSLDA attains the best mean rank against eight baselines when the fine categories within each coarse category are classified from the document-topic distributions. On the whole corpus, its advantage appears or widens as the number of topics grows. Weighting the word frequencies of each sentence by its topic posterior yields expected topic-word counts of the same form as those of LDA, so that the standard topic coherence and diversity measures apply to models that assign topics to sentences. On their product, topic quality, vSLDA leads in most within-category conditions of both corpora.

---


### 257. [Advectra: Asymmetric Latent Transport for Non-Stationary Physics](https://arxiv.org/abs/2610.05098)

**<font color=#1a73e8>作者：</font>** Nodens Koren, Thomas Hofmann, Georgios Kissas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many latent neural operators represent input and output fields in a stationary latent chart. In particular, common latent routing mechanisms use fixed or shared assignment weights for feature projection and reconstruction, limiting their ability to model transport-dominated systems where coherent structures move relative to fixed coordinate frames. We propose Advectra, a transport-aware latent operator that introduces a regularized kinematic coordinate map to decouple source and target coordinate systems. This yields an approximately co-moving latent reference frame and enables asymmetric feature aggregation and reconstruction. Combined with a geometry-aware ordering mechanism for state-space models, Advectra captures advective dynamics while maintaining stable global interactions. Advectra achieves the best performance among evaluated geometry-constrained and form-free baselines on advection-dominated benchmarks, including passive scalar transport in Navier--Stokes flows and Rayleigh--Taylor instability, while demonstrating strong generalization on real-world engineering tasks. These results highlight the benefit of explicit moving-frame structure in neural operators for non-stationary physics.

---


### 258. [Small Agents with Semantic Search: Efficient Multilingual Code Localization](https://arxiv.org/abs/2610.05099)

**<font color=#1a73e8>作者：</font>** Maxence Lasbordes, Aarush Sinha, Raphael Sourty 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Locating relevant files from natural-language requests is a core subtask for agents operating over code repositories. We investigate whether this task can be delegated to compact, specialized models to enable on-device search while reducing the token usage, latency, and inference cost of larger agents. We show that semantic search improves file localization, with gains in accuracy, cross-language transfer, and inference efficiency. To study this setting, we introduce a training framework for file-localization agents built around ColGREP, a local semantic search tool based on late-interaction retrieval models. Our recipe combines weighted supervised fine-tuning on teacher trajectories, assigning turn-level credit based on retrieval outcomes, with reinforcement learning on localization quality. We train three model families with fewer than two billion parameters to formulate search queries, inspect retrieved content, and identify relevant files. On localization tasks derived from SWE-bench Lite and Multi-SWE-bench Flash, ColGREP-equipped agents substantially improve over their base models and outperform corresponding GREP-based agents. In addition to improving localization accuracy, ColGREP reduces mean end-to-end trajectory latency by 44.1\% on CPU while using 29.1\% fewer tokens, and enables better generalization to programming languages unseen during fine-tuning. These results suggest that compact, tool-specialized localization agents can provide an efficient interface between natural-language requests and large codebases.

---


### 259. [METRO: Metric-Enhanced Token Routing Operator](https://arxiv.org/abs/2610.05100)

**<font color=#1a73e8>作者：</font>** Nodens Koren, Thomas Hofmann, Georgios Kissas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art neural operators scale to complex meshes via slice-and-process architectures, yet many rely on linear compatibility scores for latent tokenization. Under common feature normalization, such scores are equivalent to isotropic Euclidean clustering, while without normalization they induce unbounded linear decision regions. In both cases, they lack slice-specific anisotropic locality, which can lead to redundant and entangled latent slices. To address this, we propose Metric-Enhanced Token Routing Operator (METRO), a geometry-aware routing mechanism that replaces linear projection with a learnable Mahalanobis metric. By enabling each latent slice to learn a local anisotropic tensor, METRO shapes receptive fields into exponentially localized, oriented ellipsoids that naturally align with flow features like boundary layers and wakes. As a drop-in replacement, METRO yields consistent improvements across both Transformer and Mamba backbones. Empirically, our method achieves substantial performance gains on irregular domains, outperforming baselines on both standard PDE benchmarks and complex industrial design tasks. Finally, METRO exhibits enhanced robustness in out-of-distribution regimes across varying Reynolds numbers and geometric configurations.

---


### 260. [Private Component-by-Component Learning](https://arxiv.org/abs/2610.05102)

**<font color=#1a73e8>作者：</font>** Dvir Karni, Eliad Tsfadia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study differentially private learning problems in the realizable setting, where a hypothesis is specified by $k$ components. A direct iteration of private component learners is obstructed by a simple difficulty: an approximate choice of the next component may destroy exact realizability of the labeled sample, even when the next component is locally accurate. We restore realizability using the LabelBoost procedure of Beimel, Nissim, and Stemmer [SODA '15, Algorithmica '21] and recycle data through two alternating reservoirs. The resulting learner, for a target privacy $\varepsilon$, pays only $\widetilde O(\sqrt{k}/\varepsilon)$ overhead relative to the active sample requirement of a single component learning step at target accuracy $\Theta(\alpha/k)$. For learning $d$-dimensional halfspaces over a finite coordinate grid of size $L$, exact realizability makes the direct component-depth objective quasi-concave. Instantiating the framework with the IPConcave algorithm of Nissim, Tsfadia, and Yan [SODA '26] and with the quasi-concave optimizer of Cohen, Lyu, Nelson, Sarl'os, and Stemmer [STOC '23] yields a realizable sample complexity of $\widetilde{O}\left(\frac{1}{\varepsilon \alpha}\cdot \min\{d^{2.5} \log^*L, \:\: d^{2.5} + d^{1.5} 2^{\log^*L}\}\right),$ which improves on the previously known bound of $\widetilde{O}\left(\frac{1}{\varepsilon \alpha}\cdot\min\{\frac{1}{\alpha}\cdot d^{5.5}\log^*L,\:\: d^{2.5}2^{\log^*L}\}\right).$ We also apply the framework to Boolean compositions: given proper private learners for classes $H_1,\ldots,H_k$, we obtain a proper private learner for $G(H_1,\ldots,H_k)$ for any fixed Boolean function $G:\{0,1\}^k\to\{0,1\}$. Compared with the closure theorem of Alon, Beimel, Moran, and Stemmer [COLT '20], this reduces the overhead on a common component sample bound from $\widetilde O(k/\varepsilon)$ to $\widetilde O(\sqrt{k}/\varepsilon)$.

---


### 261. [SharpDraft: Accelerating Long-Context Speculative Decoding with Cardinality-Aware Query Scaling](https://arxiv.org/abs/2610.05106)

**<font color=#1a73e8>作者：</font>** Jeonghoon Park, Seongwoon Jo, Jongwon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-form reasoning makes inference expensive, and speculative decoding mitigates this cost by verifying multiple draft tokens in parallel. Its speedup, however, can fade as context grows and draft acceptance declines. We focus on attention-mass dilution: as softmax normalizes over more visible Keys, the mass concentrated on the highest-scoring Keys can decrease. We introduce SharpDraft, a training-free method that counteracts this effect through cardinality-aware Query scaling, without the computational overhead of online adaptation. Under explicit assumptions, we derive an exact top-$k$ mass correction and deploy a closed-form fixed-slope approximation. Across AIME-26, GPQA-Diamond, and LongGenBench Diary, SharpDraft achieves $2.59$-$3.19\times$ geometric-mean end-to-end speedups over target-only autoregressive decoding when applied to DFlash, PARD, and EAGLE 3.1. With DFlash, it improves decoding speed and outperforms full-parameter and LoRA-based online adaptation in end-to-end speedup, while matching the unmodified drafter's reported peak allocated GPU memory.

---


### 262. [Best-of-$N$ Guidance for Test-time Diffusion Alignment](https://arxiv.org/abs/2610.05108)

**<font color=#1a73e8>作者：</font>** Richard Lee Kim, Yeongmin Kim, Gyuwon Sim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve strong generative performance but often struggle to align generated samples with human preferences measured by a reward model. A simple yet effective algorithm for test-time alignment is Best-of-$N$ (BoN) sampling, which draws $N$ i.i.d. samples from a pre-trained diffusion model and outputs the single highest-reward sample. Despite its empirical success, BoN makes limited use of reward information, as it is incorporated only at the final selection stage without influencing the reverse diffusion trajectory during sampling. Consequently, BoN sampling does not improve the average alignment of generated samples and is primarily suited to single-output settings. We propose Best-of-$N$ Guidance (BoNG), a novel method that integrates the principle of BoN sampling directly into the reverse diffusion process. BoNG performs online BoN selection over denoising particles and adjusts the reverse diffusion process to steer the particle population toward higher-reward regions during generation. Specifically, by introducing an asymmetric guidance interaction among denoising particles, BoNG uses the current BoN particle as a guidance signal to the rest of the particle population. This particle-level interaction reshapes the sampling process toward higher-reward regions, enabling BoNG to improve not only the final best sample beyond Vanilla BoN sampling, but also the average quality of generated samples. Over 36 empirical comparisons, BoNG achieves the best performance in 29 cases, ranking first in 80.56% of the comparisons against SMC and Vanilla BoN sampling. BoNG also supports multi-output capability, achieving 1.3$\times$ ImageReward score of the latest sample-based guidance method with a 1.6$\times$ speedup. We release the code at this https URL.

---


### 263. [InstMoE: Adaptive Multimodal Routing with Specialized Experts](https://arxiv.org/abs/2610.05111)

**<font color=#1a73e8>作者：</font>** Guimin Hu, Xiang He, Yingjian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal inputs are inherently heterogeneous, not only across modalities but also in the information pathways required for effective prediction. To address this limitation, we propose InstMoE, an adaptive expert routing framework for multimodal learning. InstMoE dynamically routes each input to specialized unimodal and cross-modal experts, allowing the model to adapt its information pathways to the characteristics of the input. However, routing can be misled when modality-specific variations obscure task-relevant semantics. Such irrelevant variations may distort routing decisions, causing inputs to be assigned to inappropriate experts. We therefore introduce a Contrastive Semantic Alignment module, which encourages semantically similar inputs to share task-relevant representations while suppressing irrelevant modality-specific variations. Experiments on multimodal sentiment analysis benchmarks demonstrate that InstMoE achieves state-of-the-art performance on CMU-MOSEI and CH-SIMS v2 while using substantially fewer parameters than competitive baselines. Further analysis shows that different inputs exhibit distinct expert preferences, demonstrating that InstMoE moves beyond fixed fusion toward adaptive multimodal computation.

---


### 264. [PCLM: Small-target localization with frozen CLIP via prototype contrast and local magnification](https://arxiv.org/abs/2610.05115)

**<font color=#1a73e8>作者：</font>** Zhipeng Ye, Feng Jiang, Qiufeng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small targets occupy few patches in a vision-language encoder, so spatial features often mix object appearance with surrounding content. We propose Prototype Contrast and Local Magnification (PCLM), a support-conditioned localization method that uses a frozen CLIP encoder. Five masked support images per class define foreground and background prototypes through equally weighted regional features. Their difference provides a shared scoring direction for query patches, explicitly comparing target evidence with the demonstrated background. Nine overlapping query windows are enlarged and encoded independently to sample small targets more densely. Reprojection and coverage averaging combine their scores into a continuous localization map. The class direction occupies 2 KiB regardless of support count and transfers unchanged across datasets with mapped categories. On 5,047 small-target queries from VOC, COCO, ADE20K and Oxford-IIIT Pets, PCLM achieves higher mean pixel AP than every evaluated text-conditioned localization baseline on each dataset under our evaluation protocol. Gains over the strongest scene-dataset baselines range from 5.63 to 13.23 percentage points. At comparable measured latency, local magnification improves scene small-target AP by 4.51 to 5.68 points over whole-canvas enlargement. Factorial experiments show that prototype contrast increases the benefit of local observation, including under matched image-coordinate filtering. Support-budget experiments show that additional examples refine category estimation without increasing representation size or query-time scoring cost.

---


### 265. [LexiHorizon: Stabilizing Reinforcement Learning for Long-Horizon Deep Search](https://arxiv.org/abs/2610.05119)

**<font color=#1a73e8>作者：</font>** Zhiqing Nong, Liang Wen, Chao-Hsuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep search agents tackle complex knowledge tasks through iterative retrieval, multi-hop reasoning, and evidence synthesis across multiple sources. Existing approaches typically assume relatively stable retrieval systems and operate over short-horizon tool interaction. However, when retrieval is sensitive to query formulation, even a semantically appropriate query may fail to surface critical evidence because of mismatched entity names, aliases, or keyword combinations. Recovering from such failures requires repeated query reformulation and longer interaction trajectories. This setting poses a distinct training challenge, as the policy must sustain long-horizon query exploration while managing an expanding volume of retrieved content. We propose LexiHorizon, a framework for training search agents over long horizons that expands the trajectory context budget, manages accumulated retrieval content using a window over recent tool observations while preserving the reasoning history, and introduces an outcome-gated search-effort reward that provides a bounded bonus for tool invocations to trajectories with nonzero answer reward. Experiments on XBench, WebWalkerQA, and BrowseComp-ZH show that the resulting 9B model consistently outperforms both its base model and MiroThinker-1.7-mini, with maximum absolute gains of 8.7 and 23.8 percentage points, respectively. These results suggest that combining an extended context budget with reasoning-preserving context management benefits long-horizon deep search agents.

---


### 266. [Component-Level Evaluation of Adaptive PINN Training for CFD-Oriented Crystal Growth Simulation](https://arxiv.org/abs/2610.05127)

**<font color=#1a73e8>作者：</font>** Niruta Chapagain, Rohit Raj, Bertwin Kurisinkal Shine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural network (PINN) training minimizes a weighted combination of partial differential equation (PDE), boundary-condition, and initial-condition losses. Because adaptive methods modify these weights during training, their weighted total losses are not always directly comparable. We compare fixed-weight PINN, gradient-normalized PINN (GNPINN), and a rule-based adaptive controller (AgenticPINN) under matched settings on a heat-equation benchmark and a simplified Czochralski-oriented thermal-fluid problem. In the crystal-growth MLP experiment, adaptive control reduced the PDE residual from the order of $10^{-5}$ to $10^{-6}$, while the boundary-condition loss increased from the order of $10^{-5}$ to $10^{-2}$. On the heat-equation benchmark, GNPINN achieved the lowest relative $L_2$ field error (0.054), whereas AgenticPINN obtained the smallest PDE residual but a relative $L_2$ error of 1.368. Gaussian-process surrogates were additionally evaluated using case-wise holdout tests on corrected Czochralski CFD parameter sweeps. The temperature-field error for the temperature sweep was approximately 6%, whereas the axial-velocity error for the crystal-rotation sweep was approximately 42%. These findings show that adaptive control can improve equation satisfaction while weakening other physical constraints. PINN training should therefore be evaluated using separate PDE, boundary-condition, and solution-error metrics rather than weighted total loss alone.

---


### 267. [How Does Geometry Enter Generated Motion?](https://arxiv.org/abs/2610.05135)

**<font color=#1a73e8>作者：</font>** Weihan Li, Junhao Wu, Yuhan Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Under a fixed physical law, the visible geometry of a scene determines how motion must change. We ask how video generators realize this relationship. We fix the law and the initial state and change only the geometry drawn in the first frame, within matched families of tracks and deflectors, and compare each generated trajectory with the simulator prediction for that geometry. Paired interventions change one thing at a time: a local bump, the height of a barrier, the words of the prompt, the length of the clip. Across nine image-to-video models, geometry is preserved and shapes the motion: the speed of the ball follows the drawn undulation of a track. A physical state would carry this response forward, and here the generated motion parts from the law. The mean slope barely accelerates the ball, successive contacts fail to compose through a consistent state, an edit ahead of the ball alters its motion before it arrives, and the ball climbs over barriers higher than its release point. Two global conditions organize the global trajectory: text strongly controls the destination, while clip length strongly controls timing in the open-weight models tested. The pattern persists with photographed first frames. Current video generation thus behaves as geometry-conditioned motion synthesis whose evolution of state differs systematically from that of a fixed physical law.

---


### 268. [AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents](https://arxiv.org/abs/2610.05140)

**<font color=#1a73e8>作者：</font>** Dongki Kim, Namkyeong Lee, Surag Nair 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agents rapidly evolve, existing benchmarks can become saturated, limiting their ability to distinguish capabilities and reveal remaining failure modes. Particularly in scientific domains, constructing and updating benchmarks requires substantial time, labor, and domain expertise, making it difficult to keep evaluation aligned with advances in agent capabilities. We address this challenge by investigating whether scientific-agent benchmarks can be automatically generated and iteratively adapted as agent capabilities evolve. We introduce AutoSciBench, a framework that represents each task as a high-level concept specifying the scientific domain, data modality, and required reasoning approach, together with a low-level recipe specifying how the question, environment, and ground-truth answer are constructed and verified. Agents attempt to solve each task, producing solver trajectories and corresponding judge feedback which AutoSciBench uses to revise the recipe or concept, closing observed shortcuts and shifting tasks toward raw-data re-examination, interpretation of intermediate results, and evidence integration. Experience distilled from completed refinement trajectories further guides new concept generation, allowing lessons from earlier task refinement to inform subsequent benchmark construction. Starting from existing benchmarks, we evaluate AutoSciBench across computational biology, materials science, and clinical imaging. Generated benchmarks reduce average solver accuracy by 22.4 and 25.5 percentage points relative to the human-curated benchmarks in computational biology and materials science, respectively, while generated tasks receive higher average quality ratings across all three domains, suggesting that scientific-agent evaluation can adapt as agent capabilities advance.

---


### 269. [SemCam: Semantic Camera Motion Control for Video Generation](https://arxiv.org/abs/2610.05141)

**<font color=#1a73e8>作者：</font>** Janna Bruner, Omer Talmi, Ianir Ideses 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controlling the camera relative to a moving subject in an existing video is challenging: behaviors such as maintaining a frontal view require the camera to adapt to the subject's changing position and orientation, making the desired trajectory difficult to specify in advance. Existing camera-controlled video-to-video methods typically rely on explicit trajectories or reference motions, which do not directly express these dynamic camera--subject relationships. We introduce semantic camera motion control, a novel video-to-video task in which a reference video and a target motion label specify the desired subject-relative camera behavior without an explicit target trajectory. Our method, SemCam, learns to realize this behavior while preserving source content. It combines shared-basis low-rank adaptation with motion-conditioned modulation, while a background-consistency loss encourages fidelity in regions visible in both reference and target videos. We construct 661 paired videos covering eight semantic camera behaviors and evaluate on a separate 109-scene benchmark using subject-relative motion metrics, appearance measures, and a user study. SemCam achieves a semantic-motion success rate of 68.6%, compared with 45.3% for Vista4D, the strongest evaluated baseline, while maintaining comparable subject identity preservation.

---


### 270. [Arithmetic Actor Heads and Training Stabilization for Out-of-Distribution Reinforcement Learning](https://arxiv.org/abs/2610.05143)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Liang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) policies can deteriorate under out-of-distribution (OOD) magnitude shifts. Starting from soft actor-critic (SAC) and its Bayesian Amnesic Piecewise-Robust (BAPR) predecessor, we study the causal-symbolic BAPR (CS-BAPR) family. The practical method combines six training-stabilization settings with alternative actor heads: a Neural Addition Unit (NAU) with a Neural Multiplication Unit (NMU)-inspired quadratic correction, a Kolmogorov-Arnold Network (KAN), or a multilayer perceptron (MLP) with rectified linear unit (ReLU) or hyperbolic-tangent activations.

---


### 271. [R1A-PC: Physics-Guided Electromagnetic Inversion of Three-Dimensional Human Point Clouds in Complex Static Environments](https://arxiv.org/abs/2610.05144)

**<font color=#1a73e8>作者：</font>** Xudong Yuan, Ruyun Xu, Jingtai Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recovering three-dimensional human geometry from electromagnetic measure?ments in a complex static environment is difficult because strong multipath responses from walls, floors, and other objects obscure the weak target per?turbation. We propose R1A-PC, a physics-guided method that reconstructs a 2048-point human cloud from paired complex fields measured with and without the target. Complex background subtraction emphasizes target-induced ampli?tude and phase changes, while the background field remains available as an environmental condition. A frequency-balanced discrete Born adjoint produces a three-dimensional spatial knowledge map. At each of two bounded deformation stages, the decoder combines complex measurement features, background fea?tures, and multiscale physical features queried at the current point coordinates; the second stage queries again after the first coordinate update. We analyze the residual of paired subtraction, the weighted normal-operator structure of the raw adjoint, and the feasible set of the predicted cloud. In a held-out background generated by full-wave simulation under a fixed acquisition geometry, R1A-PC obtains a squared Chamfer distance of 0.001434 m2 and an F-score of 0.963080 at 0.05 m. Compared with TopNet, the Chamfer distance decreases by 70.28%. Removing physical guidance or background subtraction increases the Chamfer distance by 242.06% or 241.18%, respectively. Experiments across background layouts and poses support the complementary roles of paired subtraction and position-dependent adjoint features.

---


### 272. [Construction and Evaluation of Machine Learning Models for Near-Real-Time Fire Detection from MTG FCI Imagery](https://arxiv.org/abs/2610.05154)

**<font color=#1a73e8>作者：</font>** Asaf Vanunu, Boaz Nadler, Arnon Karnieli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geostationary satellite observations are important for wildfire detection and monitoring. The current study evaluates machine learning models for MTG FCI near-real-time fire detection in 1- and 2-km spatial configurations and compares them with threshold-based algorithms. The models were trained and evaluated using VIIRS fire reference data across diverse ecological regions in Europe, Africa, and the Middle East. The key results are that 1-km models significantly outperform both their 2-km variants and operational threshold products. The constructed 1-km models achieved F1 scores higher by up to 0.36 compared to baseline products. Importantly, the 1-km models detected small fires with higher probability compared to competing models. Finally, the models robustly detected fires up to 260 min earlier than baseline products. To support opensource applications, our trained models are publicly available.

---


### 273. [Cross-Modal Contrastive Learning for the Retrieval of Immunotherapy-Associated Molecular Signatures from Histopathology](https://arxiv.org/abs/2610.05157)

**<font color=#1a73e8>作者：</font>** Sigrid Vila-Bagaria, Mar Teixidó, Miquel Piñol 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gastric Adenocarcinoma is a leading cause of cancer mortality. Although "Inflamed/Non-Inflamed" subtypes have been proposed to predict immunotherapy response, their identification relies on a costly 10-gene RNA signature. We propose a Cross-modal Contrastive Multiple Instance Learning (CCMIL) framework for cross-modal retrieval, imputing these molecular signatures directly from standard Hematoxylin & Eosin (H&E) slides. By leveraging a supervised contrastive objective, CCMIL aligns visual morphological patterns with molecular phenotypes into a shared latent space. This establishes an interpretable search-by-case retrieval engine, enabling pathologists to query a whole slide image to surface transcriptomically coherent neighbors and approximate RNA signatures without genomic sequencing at inference. Our results demonstrate that this retrieval-first approach captures the continuous phenotypic spectrum of tumor inflammation and yields clinically interpretable attention heatmaps. Furthermore, the learned representation also supports competitive downstream classification, providing a practical molecular pre-screening strategy.

---


### 274. [CreativeFlow: A One-to-Many Analogical Relation Transfer Method for 3D Asset Generation](https://arxiv.org/abs/2610.05167)

**<font color=#1a73e8>作者：</font>** Xuechen Li, Shuai Zhang, Nanxuan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inspired by cognitive science, we present CREATIVEFLOW, an analogical generation framework that explicitly models analogical divergent thinking to mitigate creative homogenization in text-to-3D pipelines. Our method derives a series of meaningful yet relationally similar source-target asset pairs, each featuring distinct geometric configurations. Expert evaluations demonstrate that our framework substantially enhances creative novelty and visual fascination. This workflow and its resulting assets establish a foundational dataset and benchmark for future relation-aware 3D model training.

---


### 275. [Verification Trap: Understanding Test-Time Selection Failures under False Premises in Code Generation](https://arxiv.org/abs/2610.05170)

**<font color=#1a73e8>作者：</font>** Feng He, Hejia Wang, Linghao Meng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time compute has become a central way to improve code generation: systems sample multiple candidate programs and use verifier-visible evidence to select the final output. This paradigm implicitly assumes that the verifier provides a corrective signal independent from the generator. We challenge this assumption under misleading task premises. When the generator and verifier share a false premise, they become coupled through a mistaken belief: the generator produces premise-consistent shortcuts, while the verifier supplies evidence that fails to expose them. Consequently, the selector may choose a hidden-test-wrong candidate even when a hidden-test-correct program exists in the pool. We call this failure mode Verification Trap. Across three code-generation benchmarks and five code models, false premises consistently degrade first-sample correctness, reduce selector-chosen correctness after 64-sample test-time selection, and amplify recoverable mis-selection. Mechanistically, verifier-written tests inherit the premise-level blind spot, reshaping verifier-visible candidate space away from hidden-test correctness. These traces make Verification Trap predictable before hidden execution: a lightweight gold-free predictor using verifier-visible features reaches 0.846 AUROC. Our results identify decoupled evidence as a key mitigation axis: coupled scaling provides limited recovery, whereas premise-agnostic robustness auditors recover substantial oracle headroom.

---


### 276. [Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction](https://arxiv.org/abs/2610.05178)

**<font color=#1a73e8>作者：</font>** Sri Jahnavi Adusumilli, Deepak Giri, Pallavi Vaswani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective adaptive instructional systems require robust measures of learner engagement that go beyond static user profiles. This study employs Multimodal Learning Analytics (MMLA) to investigate the relationship between self-reported instructional modality preferences and objective neurophysiological markers of engagement. Thirty-seven participants engaged with learning content delivered via varying modalities (visual, auditory, reading/writing, kinesthetic). We captured real-time neural activity using two EEG devices: the Emotiv EpocX (14 channels, 128 Hz) and OpenBCI (16 channels, 125 Hz). Preferences were assessed using the VARK questionnaire. Consistent with literature challenging the "meshing hypothesis," aligning instructional modality with stated preferences did not significantly predict performance gains. However, spectral analysis of EEG data revealed divergent engagement patterns: when content aligned with preferences, distinct neural activity patterns emerged in theta and alpha frequency bands-markers associated with attention and cognitive processing. These signals were used to train a binary logistic regression classifier, achieving a mean accuracy of 83.21% with OpenBCI and 56.27% with Emotiv EpocX. These findings suggest that while self-reported preferences may not dictate learning outcomes, they significantly influence neurophysiological engagement, offering a viable, non-invasive input for adaptive educational algorithms.

---


### 277. [Order Matters: Competition-Guided Query Ordering for RNN-Based Object Detection](https://arxiv.org/abs/2610.05191)

**<font color=#1a73e8>作者：</font>** Shengjian Wu, Li Sun, Yu Shangguan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DETR-style detectors use one-to-one bipartite matching during training to assign object queries to ground-truth objects, enabling end-to-end set prediction without non-maximum suppression (NMS). However, without an explicit de-duplication procedure, multiple queries can still produce highly similar hypotheses for the same object, making training unstable and predictions less decisive. Inspired by the sequential ordering of NMS, we propose DETRNN, a plug-and-play module that turns unordered object queries into a competition-aware sequence for recurrent refinement. DETRNN builds an explicit confidence-and-similarity based order from prior predictions, then refines queries with an RNN along this order to model competition inside the decoder. This ordered recurrent refinement reduces redundant predictions, stabilizes optimization, and improves final detection accuracy. Experiments on multiple DETR-style detectors show consistent gains with comparable efficiency.

---


### 278. [Measuring Learned Monotone Temporal Aggregation at Matched Admissibility](https://arxiv.org/abs/2610.05196)

**<font color=#1a73e8>作者：</font>** Yew Lee Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk regulation imposes directional constraints on scores; we adopt their strict per-input form -- the score monotone non-decreasing in every exposure input -- as a normative commitment. Deployed pipelines -- monotone hand-crafted aggregates feeding sign-constrained gradient boosting -- already satisfy it by composition, so constrained-versus-unconstrained comparisons price a guarantee the incumbent has for free. We instead hold admissibility fixed on both sides and measure what learning the aggregation is worth. Our instrument is a recurrent network whose state is classical risk statistics (an exponentially weighted moving average and a high-water mark with learned transforms), monotone by construction in every input and per MC-dropout sample. The central finding, by functional regression, is a subsumption boundary: a learned monotone channel reproduces the geometrically weighted separable family of hand-crafted statistics, one channel per member, to Spearman $\rho \ge 0.996$, approximates window statistics with measurable ceilings, and fails at consecutivity ($\rho = 0.924$) and time localization (0.628), both structural, and at the exposure floor (0.829), a learnability boundary. One explicit admissible basis repairs each failure (rank correlation 1.000). In or near the separable family, learned and engineered aggregation are substitutes, and the learned channel is never statistically behind at full sample size and specified capacity. Its advantages are incumbent-specific: a committed grid pays up to 0.019 AUC in decay regions it leaves uncovered (the learned channel stays within 0.004 of the strongest engineered consumer at every swept point); the highest-dimensional comparator degrades fastest with scarce data; and beyond the training support, grid-fed tree-ensemble scores go flat while a strictly increasing head keeps ranking. No single incumbent is dominated on all three axes.

---


### 279. [From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists](https://arxiv.org/abs/2610.05197)

**<font color=#1a73e8>作者：</font>** Xiaxun Xie, Qingqing Long, Meng Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data-driven mechanistic hypotheses are essential to scientific discovery because they explain how underlying processes produce observed phenomena. AI agents and AI scientists increasingly support scientific data analysis. However, their ability to turn empirical findings into mechanistic hypotheses remains insufficiently examined. To address this gap, we introduce MechHypoBench, the first benchmark for evaluating whether AI agents and AI scientists can generate such hypotheses from empirical data. It combines paper-derived mechanisms from 14 scientific fields with real-world datasets containing 17.98 million records. The construction retains the observational complexity of empirical data while providing a specified underlying mechanism. Agents analyze the observations and propose open-form hypotheses. We develop an evaluation framework that assesses open-form mechanistic hypotheses through their consequences under withheld conditions. Experiments with general agents and AI scientists reveal a substantial gap between generated hypotheses and the underlying mechanisms.

---


### 280. [Cross-Time Directional Selection in Diffusion Sampling](https://arxiv.org/abs/2610.05199)

**<font color=#1a73e8>作者：</font>** Dhia naouali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How strongly do the remaining diffusion-sampling steps amplify a perturbation at a late latent state? Standard measurements answer this question with newly sampled isotropic noise, even though perturbations encountered during sampling have already been transformed by earlier steps. We compare these two cases directly. For each trajectory, we transport a centered perturbation from an earlier step to a late state, then replay its direction at the same magnitude as a newly sampled isotropic perturbation; both then undergo the same remaining
updates. Across the samplers we study, median paired shaped-to-fresh angular-gain ratios range from $1.14$ to $2.35$. Shaped angular gain exceeds its matched fresh counterpart in every trajectory in the original main cohorts. The same pattern appears when endpoint change is measured by latent RMS. The effect also appears in perceptual feature representations: earlier-sampling directions cause larger feature
changes at the endpoint, even when the corresponding pixel-space change is comparable. Permuting shaped directions across trajectories weakens the effect, including within class, indicating that the advantage depends on alignment with the receiving trajectory as well as on shared directional structure.

---


### 281. [F$^2$ SLAM: Turning Feed-Forward Geometry into Persistent Factors for SLAM](https://arxiv.org/abs/2610.05207)

**<font color=#1a73e8>作者：</font>** Zhisong Xu, Fan Zhu, Jiawei Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D models provide strong multi-view geometric priors, while on- line simultaneous localization and mapping (SLAM) relies mainly on local mea- surements and can accumulate drift over long sequences. Existing attempts to combine the two typically treat feed-forward predictions as an external geomet- ric state that is aligned or fused with the online estimate after the fact, which keeps broader multi-view evidence outside the optimizer that refines the SLAM state. We present F2SLAM, which instead converts feed-forward geometry di- rectly into optimization-native target-weight measurements attached to a persis- tent dense factor graph. A high-frequency stream maintains local tracking con- straints and graph connectivity, while a low-frequency stream uses wider multi- view context to selectively refresh existing measurements after a state-consistency check. Both streams constrain the same poses, inverse depths, and optional cam- era intrinsics through a single dense bundle adjustment. Experiments on multiple benchmarks demonstrate consistently strong trajectory estimation and improved dense reconstruction in both calibrated and uncalibrated settings. Notably, the uncalibrated configuration reduces the average ATE RMSE from 0.030 m for the strongest feed-forward baseline to 0.002 m on the Replica dataset.

---


### 282. [Ranking Bandits for Carousel Interfaces with Observable Browsing Depth](https://arxiv.org/abs/2610.05220)

**<font color=#1a73e8>作者：</font>** Takuma Yasuda, Atsuyoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Carousel interfaces allow a recommender system to directly observe how far a user has browsed. This signal distinguishes displayed but unclicked items from items that were never displayed, whereas conventional ranking-bandit models, including cascade and position-based models, generally treat examination as latent. We formulate a ranking-bandit problem in which a learner presents a list of $L$ items, observes the user's maximum browsing depth, and receives click feedback only for positions up to that depth. The objective is to maximize the expected number of clicks under an unknown item-attractiveness vector and a browsing-depth distribution. We propose three algorithms based on UCB, Thompson Sampling, and DMED, all of which update item statistics only from observed exposures. We derive an instance-dependent logarithmic upper bound for our UCB-based algorithm and an asymptotic upper bound for our DMED-based algorithm that coincides with the lower bound as its parameter $\alpha\downarrow 0$, establishing asymptotic optimality in this limit. Simulations in synthetic shallow- and deep-browsing environments, together with experiments parameterized from RecGaze interaction logs, show that OD-TS attains final mean regret similar to PBM-TS, while the proposed methods achieve lower final mean regret than PBM-UCB.

---


### 283. [PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment](https://arxiv.org/abs/2610.05233)

**<font color=#1a73e8>作者：</font>** Gavriel Habib, Dvir Samuel, Or Shimshi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming head-avatar reenactment aims to animate a reference image according to a live driving video, requiring robust motion transfer, long-term identity stability, and low latency. Existing methods often rely on specialized identity or motion representations, which can discard useful visual information and inherit failure modes from external extractors. In addition, many recent diffusion-based reenactment methods use offline, clip-based generation, jointly processing and denoising an entire video clip before producing its output, making continuous low-latency streaming difficult. We introduce PixReenact, a pixel-conditioned streaming reenactment framework built on causal video diffusion. PixReenact conditions directly on VAE-encoded reference and driving frames, without specialized identity or motion representations. To separate reference identity from driver motion, we train with cross-identity pseudo supervision together with corrective objectives anchored to the original reference and driving inputs. Long self-rollouts reduce autoregressive drift, while state-aware dual-teacher distillation separately addresses cold-start and steady-state generation. Across three cross-identity benchmarks and a long-horizon streaming benchmark, PixReenact demonstrates robust cross-identity reenactment, particularly under challenging conditions such as extreme viewpoints, occlusions, and pronounced facial expressions, while maintaining the reference identity over long streams. A 4-NFE rolling student continuously emits four frames per update with a mean emission latency of 239 ms.

---


### 284. [Pythia: Toward Foundation World Models for Multimodal Time Series](https://arxiv.org/abs/2610.05240)

**<font color=#1a73e8>作者：</font>** Xilin Dai, Hongzhou Chen, Yifan Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models offer a unified approach to forecasting across heterogeneous domains. Textual context and auxiliary observations provide complementary information about temporal dynamics, yet reusable multimodal predictive representations remain underexplored. We introduce Pythia, a foundation world model that learns context-conditioned latent dynamics across datasets through a joint-embedding predictive architecture. A stop-gradient numerical reference guides contextual corrections to predicted future states. A separate probabilistic decoder then adapts to the frozen predictive representation and observed history, decoupling world-model pretraining from observation-space forecasting. On MUSE, Pythia-Tiny's normalized mean absolute scaled error (MASE) and weighted sum quantile loss (WSQL) are 0.6879 and 0.4269, reducing errors by 6.26% and 5.00% relative to the strongest model evaluated in the published MUSE leaderboard. Through a series of controlled experiments, we investigate how to design a time-series world model through shared pretraining and how joint-embedding predictive learning can incorporate multimodal information. The results support separating predictive representation learning from probabilistic readout and show complementary contributions from entity descriptions, events, and covariates.

---


### 285. [What a Policy Gate Can and Cannot Know: Measured Boundaries of Cross-Platform Command Adjudication](https://arxiv.org/abs/2610.05246)

**<font color=#1a73e8>作者：</font>** Qishuai Jing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Gateways that adjudicate an agent's actions before they execute are only as good as their understanding of the action. We study a policy gate that never parses shell syntax: it consumes a typed, realised action (verb, operands, resolved zones, program-object identity) and decides ALLOW, ASK or DENY. Working on a Linux twin of the Windows benchmark of our previous study [1], we ask how faithfully it adjudicates, what survives translation, and whether deciding stays affordable as the system is used. A frozen 61-case table scores 61/61 in two rounds with no false allow; a 50-operator mutation campaign kills 46 of 50 mutants (92.0%), with all four surviving mutants classified. An 82-row audit yields 43 re-expressions, 21 carrier differences, 16 study-specific inapplicable rows and two unresolved cases; of 25 rows labelled "no counterpart," four remain unmapped here. Consulted by the executor, 25 escapes become zero with no benign payload blocked. In an exploratory one-gateway snapshot, three unauthenticated endpoint labels produce case-level non-refusal majorities of 81.8-98.0%, but immediate-execution majorities of 4.0-52.5%. Adjudication reads no accumulating state; credential verification does, scanning its whole ledger. We report that cost and the fix we would make.

---


### 286. [Kolmogorov-Arnold Networks for Personal Context Recognition on ExtraSensory](https://arxiv.org/abs/2610.05250)

**<font color=#1a73e8>作者：</font>** Hoang-Thang Ta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov--Arnold Networks (KANs) have attracted increasing attention in recent years, with applications across a wide range of AI tasks. In this paper, we evaluate several KAN variants on the ExtraSensory dataset for personal context recognition and compare them with a multilayer perceptron (MLP) and TabM. We conduct the main experiments using five user folds and three random seeds per fold and report the average Macro-F1, Micro-F1, and training time. We also perform shallow ablation studies on grid size, the number of grids, and data normalization to examine their effects on KAN performance. The results show that all evaluated KAN variants significantly outperform MLP in terms of Macro-F1 and Micro-F1 and achieve performance comparable to TabM. However, KAN variants generally require more training time, while TabM provides a more favorable balance between predictive performance and training efficiency. These results suggest that KANs are promising for personal context recognition, while their computational efficiency remains an important challenge. Our source code is publicly available at: this https URL.

---


### 287. [MGPO: Manifold-Guided Diffusion Alignment for Task-Aware Dataset Distillation](https://arxiv.org/abs/2610.05252)

**<font color=#1a73e8>作者：</font>** Yunyi Chen, Chenru Wang, Xinyi Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based dataset distillation (DD) suffers from a fundamental objective mismatch: likelihood-driven diffusion models prioritize density approximation over the discriminative decision boundaries required for downstream tasks. Beyond semantic mismatch, relying solely on density also leads to geometric coverage loss, where generated samples collapse into a few high-density modes and fail to cover the manifold's structural diversity. We propose Manifold-Guided Policy Optimization (MGPO), which reformulates DD as a multi-objective reinforcement learning problem and achieves Dual-Space Alignment via a pixel-space discriminative reward and a latent-space geometric reward guided by a class-wise Minimum Spanning Tree (MST). The discriminative reward enforces class separability, while the MST-based geometric reward encourages generated latents to cover a sparse geometric skeleton of each class, jointly addressing both failure modes. We further provide an idealized analysis that motivates the MST-based reward, including a Hausdorff approximation bound and a subsampling bound independent of the dataset size. The reward-modular design extends to structured tasks such as object detection and segmentation by substituting the frozen task reward model. Extensive experiments show MGPO consistently outperforms existing methods, including a +8.0% mIoU gain on segmentation under low-budget settings.

---


### 288. [Hybrid-Basis Feature Forecasting for Diffusion Sampling Acceleration](https://arxiv.org/abs/2610.05254)

**<font color=#1a73e8>作者：</font>** Kai-Liang Cheng, Yuan-Yuan Cheng, Yu-fan Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Hybrid-Basis Feature Forecasting (HybridFF), a training-free, plug-and-play framework for accelerating diffusion sampling. To capture local smoothness, long-range trends, and complex non-monotonic variations when modeling feature evolution, HybridFF first estimates coefficients using moving least squares (MLS) for each of multiple complementary basis families and then combines the corresponding predictors using fusion weights. In addition to the choice of basis functions, the fusion weights also play a critical role. We introduce two strategies to balance quality and speedup. HybridFF (Fixed) prioritizes efficiency with model-specific fusion weights calibrated on a small set and held constant during inference. HybridFF (Adaptive) updates the fusion weights online using branch reliability scores computed from an exponential moving average of full-step prediction errors, improving prediction fidelity and generation quality under aggressive caching while retaining substantial acceleration. Experiments across DiT-XL/2, FLUX.1-dev, SD3.5-Large, and HunyuanVideo demonstrate a favorable speedup--quality trade-off over representative single-basis forecasters and caching baselines.

---


### 289. [Learning from imperfect teachers for low-resource acoustic generalization](https://arxiv.org/abs/2610.05256)

**<font color=#1a73e8>作者：</font>** Shuanglin Li, Ruxiao Qian, Jian Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) improves low-resource acoustic learning by enriching one-hot supervision with the softened predictive distribution of a fixed teacher network. However, a teacher trained with limited or imbalanced annotations may produce a biased distribution whose components are not uniformly reliable. Although this distribution can still encode useful knowledge, direct full-distribution matching may also transfer teacher-induced biases, thereby distorting the student's decision boundary and degrading its generalization performance. To address this limitation, we propose Boundary-Anchored Mass-Partitioned Distillation (BA-MPD), a logit-based distillation objective composed of Boundary-Anchored Correction (BAC) and Mass-Partitioned Distillation (MPD). BAC addresses missing ground-truth labels in the set of the teacher's top predictions by swapping the true label for the lowest-ranked entry of the set, thus keeping the mass and uncertainty of the set unchanged. MPD then distills this corrected distribution through separate losses that enforce relational consistency within the set, balance the mass between high- and low-confidence groups, and weight lower-confidence dependencies. Ultimately, BAC and MPD together suppress harmful ranking errors and noisy low-confidence details, while retaining all useful teacher information. Experiments on two acoustic benchmarks under multiple label budgets show that BA-MPD consistently improves over supervised-learning baselines and vanilla KD while remaining competitive with strong logit-based KD baselines. Cross-budget results further show that BA-MPD remains effective when the teacher and student models use mismatched label budgets, demonstrating its ability to exploit imperfect teachers across supervision gaps. Implementation available at this https URL.

---


### 290. [Synergizing Drone Delivery Order Pooling and Road Network Monitoring through Monitoring-Task Orderization](https://arxiv.org/abs/2610.05270)

**<font color=#1a73e8>作者：</font>** Yulong Hu, Meng Xu, Sen Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper investigates the real-time dispatch of a shared drone fleet for on-demand food delivery and urban road network monitoring. We consider a courier-drone collaborative setting in which couriers transport orders to launchpads and drones complete the final delivery leg to kiosks. Drones may consolidate multiple origin-destination orders within one flight and make monitoring-aware route adjustments to collect real-time traffic information subject to delivery-time constraints. This yields a joint decision problem coupling dynamic order-to-drone matching, multi-order pooling, routing, and time-varying monitoring under fleet-level competition and uncertainty. We propose monitoring-task orderization, which periodically converts road-network nodes with high congestion and stale information into virtual monitoring orders. Pooling these virtual tasks with food-delivery orders creates a unified heterogeneous task set and transforms the coupled matching-and-routing problem into an order-level decision process. Building on this abstraction, we formulate a decentralized graph-interdependent Multi-Agent Markov Decision Process and develop Graph Multi-Agent Q-Learning (Graph-MAQL), which captures localized inter-agent dependencies through bipartite match coordination graphs. Agent-task value estimates are then used as edge weights in a dynamic heterogeneous bipartite matching program for globally feasible execution. Experiments using real-world data reveal strong operational synergy between delivery and monitoring. Monitoring-task orderization improves monitoring performance by 25.1% with less than a 1% reduction in delivery performance, while Graph-MAQL improves the aggregate objective by up to 20.8%, reduces deadline violations by over 40%, and transfers zero-shot to higher demand intensity without retraining.

---


### 291. [When Verifiable Counts Depend on Wording: Auditing Wording Robustness in Instruction Following](https://arxiv.org/abs/2610.05278)

**<font color=#1a73e8>作者：</font>** Qishi Zhan, Seoyeon Jang, Zihan Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verifiable instruction-following benchmarks often express each constraint through one fixed template. We test whether scores remain stable when the operational requirement is unchanged but its wording varies. We introduce WISE, a matched evaluation suite and reporting protocol instantiated on exact word count, keyword inclusion exactly once, and an inclusive 8--12 word range. Across 100 matched tasks, up to thirteen models from seven providers, and repeated generations scored over the complete visible output, wording alone produces substantial compliance shifts. In an avoidance-family panel, five avoidance and exclusion forms fall below the positive baseline, while constructional controls also shift compliance substantially: in the nine-model control panel, compliance is 54.9% for the original positive form, 48.2% for a longer positive form, 36.7% when the target appears later, and 33.8% for AVOID1. A strict JSON-structure probe shows wording sensitivity beyond counting, with a different direction of effect. Effect sizes, failure directions, weakest forms, and model rankings vary across realizations. Under the most disruptive exclusion form, the top-ranked model changes and 24.1% of strictly ordered model pairs reverse. Human validation further shows that unanimous agreement on an exact-count interpretation can coexist with substantially different model behavior. WISE supplements conventional scores with mean and worst-form compliance, wording gaps, failure profiles, and ranking stability.

---


### 292. [Fast Convergence through Distributed Augmentation for Class-Imbalanced Federated Learning](https://arxiv.org/abs/2610.05279)

**<font color=#1a73e8>作者：</font>** Arathi Nair M, J. Harshan, Anwitaman Datta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In federated learning, mitigating class imbalance is essential to improve minority-class performance. A common approach to address this problem is to augment minority-class samples to achieve local class balance. Existing approaches treat augmentation as a heuristic and do not establish how the amount of augmentation influences the convergence of federated learning, leading to excessive augmentation and increased training time. To address this limitation, we first establish the relationship between augmentation and the convergence behavior of federated learning. Leveraging this insight, we propose DAFL, a distributed augmentation framework that determines the minimum augmentation required for each client-class pair by jointly minimizing augmentation and training time while constraining global class imbalance, thereby improving minority-class F1-score. Experimental results demonstrate that DAFL consistently improves minority-class F1-score while substantially reducing training time, particularly under severe global class imbalance and high label proportion imbalance.

---


### 293. [When Agent Context Goes Stale: Incoherence in Volatile Agent Context](https://arxiv.org/abs/2610.05281)

**<font color=#1a73e8>作者：</font>** Yingying Liu, Junzhou Fang, Chenxiong Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern agents increasingly ground their reasoning in observations returned by tools, such as file contents read from a workspace. However, the data sources underlying these observations may later be modified by users, other agents, or external tools, while the model retains only the stale content in its context window. Existing agent runtimes provide little support for notifying the model that a previously observed fact has become stale, causing agents to reuse outdated observations and make incorrect claims about the current workspace state. We propose Concord, a context coherence framework that maintains the consistency between tool observation in agent context and the mutable sources from which they were derived. Concord links each observation to its source, detects source changes, and uses configurable handling policies to update, annotate, or suppress stale context before reuse. Concord is applicable across different agent runtimes and external resources, and can be easily extended to new runtime-resource settings. We implement Concord as a general framework, and instantiate a concrete use case to assess its effectiveness. We construct ConcordBench, where previously observed file contents become stale after subsequent edits. Across three evaluated frontier models, Concord produces answers consistent with the restored workspace state in all evaluated cases under these constructed conditions, matching the oracle on recover count for this benchmark, while using 46.4% fewer tokens than the strongest non-oracle baseline.

---


### 294. [Mobile-4DGS: Unified Static-Dynamic Real-time Mobile Gaussian Splatting](https://arxiv.org/abs/2610.05289)

**<font color=#1a73e8>作者：</font>** Xiaobiao Du, Beixi Hao, Zhen Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting (3DGS) have achieved remarkable performance in novel view synthesis, yet deploying both static and dynamic Gaussian representations on resource-constrained mobile devices remains challenging due to heavy storage, redundant primitives, and costly per-frame computation. We present Mobile-4DGS, a unified lightweight framework for high-fidelity real-time static and dynamic Gaussian rendering on mobile platforms. For compact appearance modeling, we introduce a Monte Carlo Specular Energy Aggregator that compresses high-order radiance residuals into the first-order Spherical Harmonics (SH), together with an Attribute-Conditioned SH Enhancement module whose predicted offsets are pre-baked before inference. We further propose a Multi-View Alpha-Based Densification and Pruning strategy to suppress redundant primitives while maintaining multi-view consistency. For dynamic scenes, we develop a compact explicit 4D representation by constructing second-order Gaussian motion, learnable temporal support, and a binary static-dynamic partition, enabling continuous-time modeling without runtime deformation networks. Based on this partition, a Depth-Order Certificate selectively reuses previously committed depth orders to reduce re-projection, sorting, merging, and index-buffer updates during playback. Extensive experiments on static and dynamic scenes demonstrate that Mobile-4DGS substantially reduces storage and rendering overhead while maintaining competitive visual quality, enabling real-time 3D and 4D Gaussian Splatting on mobile devices. \textcolor{magenta}{\href{this https URL}{Code has been released: this https URL}}.

---


### 295. [Smoothed Gradient Method for Nonconvex Federated Stochastic Bilevel Optimization](https://arxiv.org/abs/2610.05290)

**<font color=#1a73e8>作者：</font>** Xinwen Zhang, Peiran Yu, Zhaosong Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, federated stochastic bilevel optimization has attracted increasing attention due to its wide range of applications in machine learning. To reduce the computational overhead associated with second-order Hessian and Jacobian matrices, several first-order methods have been proposed. However, existing methods typically impose restrictive assumptions on the lower-level function, suffer from a strong dependence on the condition number in their convergence rates, and require different learning-rate scales for variables across the upper- and lower-level problems, limiting their practical applicability and complicating hyperparameter tuning. To address these challenges, we propose a stochastic doubly smoothed gradient method for nonconvex federated stochastic bilevel optimization problems, which decouples the learning rates of upper- and lower-level variables and does not require a strongly-convex lower-level loss function. We establish rigorous theoretical guarantees for the proposed algorithm, demonstrating an improved convergence rate of $O(\kappa^{15/2}/\epsilon^5)$ and a communication complexity of $O(\kappa^{4}/\epsilon^3)$, where $\kappa$ denotes the condition number and $\epsilon$ represents the solution accuracy. Notably, these bounds exhibit significantly better dependence on the condition number $\kappa$ than those of existing methods. Extensive experiments validate the effectiveness of our algorithm.

---


### 296. [BossouChimpanzee: Long-term Chimpanzee Video Dataset](https://arxiv.org/abs/2610.05293)

**<font color=#1a73e8>作者：</font>** Daniel Schofield, Susana Carvalho, Vladimir Iashin 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe the BossouChimpanzee video dataset, a unique long-term visual record of wild chimpanzees at an outdoor laboratory for field experiments in Bossou, Guinea, spanning three decades (1988-2018) and comprising over 1,200 hours of continuous video recordings collected through collaborative fieldwork and research. In this paper, we outline the history and scientific contributions of the experimental paradigm and video archive, provide key statistics and details on the structure of the main video dataset, and release an initial ~74h snapshot, BossouChimpanzee70h, covering 23 identified individuals focused on chimpanzee individual and action recognition, ahead of the full video resource. This dataset represents a valuable resource for cognitive and behavioural research in ethology and a rich benchmark for training and evaluating machine learning models on audiovisual data from the wild.

---


### 297. [FlexCast: Adaptive Weather Forecasting from Arbitrary Field Sets](https://arxiv.org/abs/2610.05296)

**<font color=#1a73e8>作者：</font>** Yuang Zhang, Chen Hui, Weisi Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most deep learning weather models assign a fixed set of variables and pressure levels to predefined channels, limiting transfer across atmospheric field configurations. This dependence on a fixed field set limits the transferability of trained models across atmospheric field configurations. We propose FlexCast, a field-adaptive weather forecasting model that uses a single set of parameters to produce identity-aligned forecasts for variable-cardinality subsets drawn from a 69-field ERA5 registry. Specifically, a metadata-conditioned adapter the first encodes variable identity, pressure level, and field type and combines them with spatial features. Then, shared rank-16 projec?tions are modulated by metadata-dependent gates to produce field?specific features, while masked set fusion aggregates the available fields into a fixed-width representation. Subsequently, a multiscale U-Transformer processes the fused atmospheric features, while an identity-aware query decoder produces forecasts for the requested fields. Finally, FlexCast learns a standardized six-hour increment and applies it recursively to generate forecasts at longer lead times. Experiments on the 2020 ERA5 test set demonstrate that FlexCast operates across varying field configurations. Compatible cross-field context is associated with lower forecast errors, whereas mismatched context increases them.

---


### 298. [Do Neural Networks Learn Structure-Preserving Maps? A Case Study in Latent-to-Hilbert Embeddings](https://arxiv.org/abs/2610.05297)

**<font color=#1a73e8>作者：</font>** Muhammad Adnan Shahzad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask whether a neural network can learn a structure-preserving map from a compressed latent space to a Hilbert-space representation. Using an 8-dimensional autoencoder bottleneck on MNIST and $n$-qubit product-state targets from PCA-based angle encoding, we report four findings. Although the target angles are generated by a nonlinear sigmoid transformation of the latent projections, the resulting mapping is well approximated by a linear function over the observed latent distribution: linear regression from $z$ to the true target angles achieves $R^{2} = 0.98$, while regression to the MLP's recovered angles achieves $R^{2} = 0.91$. The learned map's primary direction is strongly aligned with the target-induced direction, with cosine similarity $0.989$, while remaining nearly orthogonal to the input's principal direction, with cosine similarity $0.002$. The map is genuinely rank-4: removing any singular direction degrades inner-product preservation by $2.5$--$5.9\times$ despite a singular-value spectrum with two dominant and two small values. The learned subspace does not coincide with the PCA basis used to construct the target, and different random seeds recover the same primary direction but diverge in higher ranks. Finally, kernel ridge regression with an RBF kernel outperforms a tuned MLP (IP error $0.0144$ vs.\ $0.0197$), suggesting that for approximately linear structure-preserving mappings, classical kernel methods may be a simpler and more effective alternative.

---


### 299. [Revisiting Ground-Truth Synthesis from High-Speed Video: Exact Validity Conditions and an Audited Consumer Capture Corpus](https://arxiv.org/abs/2610.05298)

**<font color=#1a73e8>作者：</font>** Abdullah Al Shafi, Sumaiya Rahim Suma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion-deblurring datasets are commonly synthesised by averaging $N$ consecutive high-frame-rate frames and labelling the result with the central frame. We show that this label is unbiased for every capture timing only when the window is odd and the frames' sample durations are equal. An even window shifts every label by a fixed fraction of the blur length, even under perfect timing. Unequal durations are subtler: their mean misalignment is zero, so dataset statistics cannot reveal them, yet when the offset cannot be read from the blur they convolve the supervision rather than adding noise to it. Auditing 51 smartphone clips recorded at a nominal 240 fps, we find 19 captured near 176 fps, a behaviour recorded only in the container's timing tables. In a controlled test the parity choice costs a fitted linear deblurring filter far more than these timing irregularities do, and interpolation labels, unlike blur labels, can be repaired with the true frame times. We provide a tool that checks both conditions without decoding, and will release the clips and their timing tables.

---


### 300. [Kinematics-Centric Continuous Sign Language Retrieval with Gloss-Guided Boundary-Aware Alignment](https://arxiv.org/abs/2610.05306)

**<font color=#1a73e8>作者：</font>** Chang Liu, Ke Han, Davide Talon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language-text alignment remains a fundamental challenge for text-driven sign language understanding. Existing methods predominantly rely on appearance-heavy RGB representations, which entangle motion semantics with visual variations and lead to ambiguous motion-language grounding. In this paper, we reformulate sign language-text alignment in a structured kinematic space and propose a kinematics-centric framework that adopts 3D SMPL-X motion as the primary representation. By explicitly modeling the kinematic dynamics of signing in a unified motion space, our approach reduces reliance on appearance signals and yields more semantically consistent representations. To capture the compositional nature of sign language, we introduce a gloss-guided local alignment mechanism that leverages gloss temporal spans as weak supervision to decompose continuous motion into coherent segments and establish fine-grained motion-text correspondences, thereby reducing ambiguity in localizing word-level semantics in continuous signing. Furthermore, we develop a visual distillation strategy, where RGB signals serve as privileged supervision during training to provide complementary contextual cues, while being completely removed at inference time. Extensive experiments on standard benchmarks demonstrate that our method achieves state-of-the-art bidirectional retrieval performance on CSL-Daily and competitive results on PHOENIX-2014T. These results highlight the effectiveness of kinematic representations and explicit local grounding for sign language-text alignment.

---


> [!TIP]
> 当前位于：**251-300**（第 6/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
