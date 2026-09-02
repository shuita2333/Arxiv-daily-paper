# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

---

### 201. [Target-Aware State-Adaptive $p$-Dirichlet Graph Neural Regression for Non-Invasive Body-Composition Estimation](https://arxiv.org/abs/2608.29496)

**<font color=#1a73e8>作者：</font>** Nadejda Drenska, Matthew Lemoine, Gowri Priya Sunkara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of body-composition outcomes, including body fat percentage (BFP), bone mineral density (BMD), and appendicular lean mass (ALM), is important for evaluating metabolic, skeletal, and muscular health. Direct assessment using dual-energy X-ray absorptiometry (DXA), however, requires specialized equipment and involves ionizing radiation. We propose a target-aware, state-adaptive $p$-Dirichlet energy-flow graph neural regression ($p$SADE-GNR) framework for estimating these outcomes from non-invasive anthropometric measurements. A neural encoder maps participant representations to hidden states that are propagated over an outcome-specific participant-similarity graph by a state-adaptive forward-Euler discretization of the graph $p$-Dirichlet energy flow. Graph distances weight each original or latent coordinate by its normalized absolute training-fold correlation with the outcome. Using clinical data from the Pennington Biomedical Research Center and five-fold cross-validation, the correlation-weighted model using the original standardized measurements achieved the lowest root mean squared error in all nine primary outcome-cohort combinations and outperformed previously reported support vector regression or least-squares support vector regression reference values in eight of nine comparisons. Autoencoder, variational-autoencoder, and Gaussian-mixture variational-autoencoder representations generally did not improve primary-outcome prediction or reduce computational cost. In an exploratory age-prediction analysis including ALM, BMD, and BFP as predictors, the correlation-weighted GMVAE model achieved the lowest mean error in all three cohorts. These results support target-aware, state-adaptive $p$-Dirichlet graph neural regression for non-invasive body-composition estimation.

---


### 202. [Adversarial Online Classification with a Preview](https://arxiv.org/abs/2608.29503)

**<font color=#1a73e8>作者：</font>** Roi Livni, Sahil Singla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Worst-case online classification is governed by sequential complexity, such as Littlestone dimension, and can be impossible even for statistically simple classes, such as thresholds of VC dimension one. We study a preview model in which an oblivious adversary fixes an entire labeled sequence of length $T$, a uniformly random subset of size $pT$ is revealed before prediction begins, and the remaining $(1-p)T$ examples are then presented in their original adversarial order.
Against the best full-sequence hypothesis evaluated on the unrevealed examples, we characterize the dependence on the preview rate $p$: for binary classes of VC dimension $d$, the optimal excess loss is $\Theta(d/p+\sqrt{dT})$, up to the trivial cap at $T$; for multiclass classes we obtain the corresponding $\widetilde O(d_{\rm DS}/p+\sqrt{d_{\rm Nat}T})$ bound with no dependence on the number of labels. Thus a random preview can replace worst-case sequential complexity by classical statistical dimensions without randomizing the online order. To achieve the sharp binary bound, our ChainedPrediction algorithm uses an online analogue of chaining, implemented as a multiscale aggregation algorithm rather than only as an analytic argument.

---


### 203. [Denoising as Projection: Constrained Optimization with Gradient-Guided Diffusion](https://arxiv.org/abs/2608.29507)

**<font color=#1a73e8>作者：</font>** Runyu Zhang, Jiawei Zhang, Gioele Zardini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are increasingly used not only for sampling from learned data distributions, but also for generating samples that optimize task-specific objectives. A common approach is to guide the reverse diffusion process using gradients of an external objective. However, when the data distribution is supported on a structured feasible set, such as a manifold or a constraint set, gradient guidance can move samples away from the learned data geometry. In this paper, we study a simple projected-gradient-guided diffusion update based on the observation that the Stein denoising operator can act as an approximate projection onto the data geometry. The proposed update incorporates the objective gradient inside the denoising step, yielding an inference-time method that uses only a pretrained denoiser and gradient evaluations. We analyze this update as an inexact projected-gradient method for constrained optimization over learned feasible geometries. Our theory covers three settings: linear manifolds, compact convex feasible sets, and compact Riemannian submanifolds. In all these settings, we prove descent and finite-time convergence guarantees. Numerical experiments support the theoretical interpretation and illustrate how the proposed update balances objective descent with preservation of the learned geometry.

---


### 204. [ARMOR: Manifold-Oriented Training for Adversarially Robust Aerial Object Detection under Data Scarcity](https://arxiv.org/abs/2608.29510)

**<font color=#1a73e8>作者：</font>** Haoran Wang, Matthew Lau, Alec Helbling 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial object detection is increasingly deployed in real-world applications, but models remain vulnerable to physical, universal adversarial patches that cause them to miss objects. Furthermore, defenders face the practical constraint of training data scarcity: aerial imagery is costly to collect and label, so a deployment site typically yields hundreds of images rather than the tens of thousands that adversarial robustness benchmarks assume. To tackle model vulnerability and training data scarcity, we propose Adversarial Robustness with Manifold-Oriented Training (ARMOR), a novel defense that realizes the core insights of on-manifold adversarial training (OMAT) in low-data regimes. ARMOR builds on the insight of OMAT to model the data manifold - the compact structure capturing the data's relevant features - to learn and robustify these features during training. While OMAT relies on the data-intensive operations of training large generative models and adversarial training to achieve this, ARMOR adopts a data-efficient approach that reuses labels the detection task already supplies: ARMOR (i) masks image backgrounds to retain object-relevant features, and (ii) injects randomized patches on objects to improve feature robustness. Our low-data experiments with physically-realizable adversarial patches evaluate both query-free transfer attacks and defense-aware attacks. ARMOR maintains strong clean performance of over 0.90 model confidence, while improving adversarial robustness by up to 0.32 in model confidence over state-of-the-art defenses. Physical experiments with printed patches confirm that these gains survive deployment. Overall, ARMOR translates insights from manifold-based training to defend object detectors amidst training data scarcity.

---


### 205. [On the Plasticity Collapse in Continual Machine Unlearning](https://arxiv.org/abs/2608.29513)

**<font color=#1a73e8>作者：</font>** Yingdan Shi, Xiang Xu, Kaize Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning enables deep neural networks to selectively remove the influence of specific data in response to privacy and regulatory requirements. While prior work largely studies single-shot unlearning, real-world systems must accommodate continual unlearning, where multiple unlearning requests occur sequentially over time. In this work, we identify a fundamental limitation of this setting: plasticity collapse, a progressive breakdown in a model's ability to effectively forget. Through theoretical analysis of continual unlearning dynamics, we show that continual unlearning operations accumulate geometric constraints in parameter space, leading to saturated subspaces that restrict future updates. This structural effect induces two distinct failure modes: (1) Forward failure -- diminishing forgetting quality for subsequent tasks, and (2) Backward failure -- spontaneous re-memorization of previously forgotten information. Extensive experiments across multiple architectures, datasets, and methods in image classification confirm that plasticity collapse is not an artifact of specific implementations, but a pervasive phenomenon inherent to continual unlearning. Our findings reveal a critical barrier to the long-term reliability of machine unlearning systems and motivate the development of plasticity-preserving unlearning algorithms. Our code is available at this https URL

---


### 206. [FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation](https://arxiv.org/abs/2608.29519)

**<font color=#1a73e8>作者：</font>** Hao Feng, Zhi Zuo, MingJian Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Function-Room Generation, a new indoor 3D scene generation setting that creates rooms supporting explicit functional goals rather than merely visually plausible layouts. Existing agentic and executable methods improve controllability, but often depend on costly test-time generate--evaluate--revise loops, making functional room generation slow and computationally expensive. We address this challenge with three technical contributions. First, we design a recursive domain-specific language to effectively organize the hierarchical object compositions required by functional rooms, from room structure and major furniture to dense support-surface and nested small objects. It represents rooms as staged executable programs with explicit geometric and functional relations. Second, we propose a sequential feed-forward scene construction framework that distills recursive construction traces into a scene construction expert. At inference time, the expert writes executable DSL code stage by stage, and a deterministic executor directly instantiates each stage without teacher agents, online critics, or iterative repair. Third, we introduce ScenePRM, an execution-grounded process reward framework that improves the expert through reinforcement learning with functional, geometric, relational, and future-constructability feedback. We further establish a function-oriented benchmark and show state-of-the-art performance on both general indoor scene generation and function-room generation, achieving stronger functional completeness, relation correctness, geometric executability, and generation efficiency.

---


### 207. [Ontology-Guided Multi-Agent Extraction of Evaluation Objects from Academic Review Texts: Evidence from Chinese Library and Information Science](https://arxiv.org/abs/2608.29526)

**<font color=#1a73e8>作者：</font>** Haolin Chen, Hongyi Dong, Yu Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Academic reviews, scholarly commentaries, and book reviews serve as sources of evaluative statements about theories, methods, literature, institutions, and policies, providing valuable evidence for scholarly evaluation. Existing scientific entity extraction methods mainly target research articles and are less effective for evaluation objects, which are often abstract, context-dependent, and characterized by ambiguous type boundaries. This study proposes an ontology-guided multi-agent framework for evaluation object extraction. The framework combines candidate discovery, ontology-constrained classification, and domain review. Experimental results show that it achieves a Precision of 90.33%, Recall of 84.55%, Entity-level F1 of 87.34%, Strict Typed F1 of 79.78%, and Type Accuracy of 91.35%, substantially outperforming rule-based and zero-shot baselines. Ablation results indicate that the multi-agent workflow improves recall and stability, while ontology-based boundary constraints enhance fine-grained classification and reduce category confusion. The framework supports the structured utilization of evaluative scholarly texts and provides methodological support for evidence-based research evaluation and STI mining.

---


### 208. [Context or Digits? Balancing Memorability and Efficiency in Virtual Reality Authentication](https://arxiv.org/abs/2608.29531)

**<font color=#1a73e8>作者：</font>** Yuxuan Huang, Qiao Jin, Tongyu Nie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present Adaptive Direction-Based Authentication (ADBA), a knowledge-based authentication method for Virtual Reality that decouples users' needs temporally by enforcing password creation based on virtual environment context while supporting both context- and digit-based entries during authentication. This design prioritizes memorability for new passwords and offers both efficient and memorable options to support users' evolving needs. We conducted a remote longitudinal study with 66 participants comparing ADBA against 6-digit PINs over 2-3 weeks. The results demonstrated that ADBA achieved superior memorability and lower perceived task load. Interestingly, no participant chose to enter via digits in the study, yet they still perceived ADBA to be highly efficiency despite longer objective entry times. ADBA also provided security benefits through randomly-generated digit representations, though some degree of password homogeneity was observed in specific virtual environments. Our findings suggest that ADBA offers solid advantages to the traditional PINs, and successfully addresses the tradeoffs between efficiency, memorability, and security under the usage scenarios considered in the study.

---


### 209. [NepScript Genesis: Neural Architecture Search for Handwritten Devanagari Digit Synthesis](https://arxiv.org/abs/2608.29540)

**<font color=#1a73e8>作者：</font>** Mausam Gurung, Prabin Neupane, Sajjan Acharya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces NepScript Genesis, a Neural Architecture Search (NAS) framework for automated Generative Adversarial Network (GAN) discovery, applied to conditional Devanagari handwritten digit synthesis. We compare five NAS strategies against a carefully constructed Deep Convolutional GAN (DCGAN) baseline (FID=332.28). Architecture selection utilizes a two-stage pipeline guided by a novel domain-aware evaluation metric (Enhanced Score). Results demonstrate that Adaptive Exploration achieves the optimal quality-efficiency trade-off, attaining an FID of 79.12 -- a 76.19% improvement over the baseline -- and the highest mode coverage among the NAS strategies (Recall=0.531) in under one GPU-hour. Furthermore, we demonstrate that incorporating script-specific structural heuristics into the search phase prevents early-stage mode collapse. In a downstream low-resource evaluation, augmenting 250 real training samples per class with GAN-generated digits from the best NAS model improves CNN classification accuracy from 91.0% to 96.5% (+5.5 percentage points), demonstrating that NAS-optimized synthesis produces digits of sufficient quality to benefit practical recognition pipelines when real data is scarce.

---


### 210. [BEACON: Behavioral and Semantic Enrichment of AlphaEarth Embeddings through Tri-Modal Contrastive Learning](https://arxiv.org/abs/2608.29553)

**<font color=#1a73e8>作者：</font>** Hao Tian, Heng Cai, Yifan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models such as the AlphaEarth Foundation produce compact and globally consistent representations of the Earth's surface that transfer effectively to a wide range of downstream tasks. However, because these models are trained primarily on Earth-observation imagery, their embeddings mainly capture physical and spectral characteristics while encoding human activity and urban function only weakly. To address this limitation, we propose BEACON, a tri-modal contrastive learning framework that aligns three complementary views of urban space: physical representations from AE embeddings, semantic representations from point-of-interest (POI) text, and human behavioral representations from hourly POI visitation, while keeping the deployed representation image-only. Using the Houston Metropolitan Area as a case study area, we evaluated the performance of the BEACON framework on nine downstream tasks, including seven regression and two classification tasks against six baselines (raw coordinates, Space2Vec, SatCLIP, TESSERA, Clay and AlphaEarth), using frozen linear and MLP probes over five seeds. Under a linear probe, BEACON improves relative R^2 over AlphaEarth by up to 43% for obesity prevalence, 34% for poor mental health, and 22% for median household income, while remaining competitive in the prediction of physical and environmental variables. These findings highlight the value of augmenting geospatial foundation models with semantic and behavioral signals, extending their applicability from physical Earth observation to human-centered urban analytics.

---


### 211. [Asynchronous Cooperative Online Learning for Multi-Robot Control under Computational Delays](https://arxiv.org/abs/2608.29562)

**<font color=#1a73e8>作者：</font>** Xiaobing Dai, Zewen Yang, Wei Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring the safe operation of multi-agent systems (MASs) under uncertain environments is crucial for cooperative robotic, where external disturbances and inaccurate dynamic models can significantly compromise performance and reliability. To address this challenge, calibrated machine learning models, particularly Gaussian process (GP) regression, are extensively employed due to their interpretable performance quantification. As the interconnected communication of MASs facilitates cooperative learning, agents are able to enhance learning performance by exchanging local GP inferences with their neighbors and aggregating the received information via distributed GP strategies. However, variations in computational power and prediction tasks among agents inevitably lead to heterogeneous computational delays and differences in query points, which are often overlooked in existing aggregation methods. To overcome these limitations, this work proposes an asynchronous cooperative learning strategy that explicitly accounts for prediction accuracy, query point variations and delay effects. Additionally, a distributed control law based on an adjoint MAS is developed to ensure the desired control performance. Simulations on unmanned surface vehicles validate the effectiveness of the proposed approach, demonstrating substantial improvements in both learning and control performance compared to the state-of-the-art approaches.

---


### 212. [HoopMind: A Real-Time Neural Game-Tree System for Opponent-Aware Possession Planning](https://arxiv.org/abs/2608.29563)

**<font color=#1a73e8>作者：</font>** Yibo Gong, Cong Guo, Jiacheng Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> School coaches prepare for opponents with game film and intuition. The analytics tools of professional teams stay out of reach. We ask how far public data can close this gap. Professional basketball is our case study, chosen for its data rather than the league. We fuse five public sources into one per-shot dataset of 4.23M shots over 21 seasons. The sources are shot locations, two play-by-play feeds, official matchup tracking, and player biometrics. Alignment across them is 99.5% to 100%. We also report two data pitfalls that are easy to miss. We then model a half-court possession as a sequential game. Shot values come from ShotNet, an embedding multilayer perceptron (MLP). On a held-out season it beats a zone-rate baseline and a logistic baseline, and its probabilities are well calibrated. A depth-limited expectimax search then solves the offensive decision tree, with branch-and-bound pruning to keep it real time. All training runs offline, so the online system stays light. A scouting planner and a playable simulator both run in a single browser page.

---


### 213. [MotionSync: Non-Causal Refinement of Causal Tracker for Label-Efficient 3D Perception](https://arxiv.org/abs/2608.29567)

**<font color=#1a73e8>作者：</font>** Rahul Ahuja, Bala Murali Manoghar Sai Sudhakar, Shashwata Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional box-and-track annotation is the cost bottleneck in autonomous-driving data engines, and the offline systems built to relieve it replace the online perception stack outright, so a team needing both regimes maintains and reconciles two. MotionSync makes the causal/non-causal boundary an explicit architectural seam instead. A strictly causal tracker, built on a strong published baseline and extended with innovation-driven uncertainty calibration, frame-rate-invariant kinematic association gates, and multi-hypothesis motion with learned mode selection, emits a valid online result. A non-causal pass then revises the buffered trajectories with Rauch--Tung--Striebel smoothing applied separately to pose, extent and yaw, physics-validated gap completion, and semantic pruning of ghost tracks against LiDAR point labels. The refiner never writes back, so one system serves both regimes and refinement's effect is a delta over an unaltered causal estimate. Used as an auto-labeller, a fixed 3D detector trained on 25% human labels plus MotionSync pseudo-labels reaches 96.9% of its full-supervision mean average precision (mAP) on Waymo, and at a 10% budget the non-causal pass accounts for +3.3 mAP/L2 over pseudo-labels from the same tracker's causal stage. Re-fitting the online tracker on its own refined output recovers 73% of the benefit of human supervision, while its causal output is worse supervision than no re-fitting at all. As a tracker MotionSync is at parity with the leading published offline entries on the headline metric and ahead of them on error composition, which is where a refinement pass can act at all: it reduces misses and fragmentations together, the signature of gap completion rather than of a tuned detector.

---


### 214. [Event-triggered Control and Online Learning for Networked Systems under Computational Delays](https://arxiv.org/abs/2608.29576)

**<font color=#1a73e8>作者：</font>** Xiaobing Dai, Armin Lederer, Zewen Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online learning-based control is a promising approach to control uncertain systems, where unknown components are identified during operation to improve control performance. However, resource-intensive online learning algorithms introduce non-negligible computational delays, especially when executed on systems with limited local computational resources. To mitigate this, an in-network online learning-based control structure is employed by deploying the learning-based controller on a remote computation node and connecting it via a communication channel. In this paper, control performance guarantee is first established by deriving tracking error bound for the in-network control architecture, while accounting for computational delays. The derived tracking error bound allows for diverse communication and computation strategies under a specific condition, including time-/event-triggered mechanisms. Additionally, the trade-off between communication and computation performances is shown for a given desired control performance. Furthermore, to enhance the efficiency in both communication and computation, an efficient control framework with an asynchronous event-triggered mechanism in both control and online learning is devised under the existence of computational delay. The proposed event-triggered strategy is proven to achieve the same control performance as time-triggered scenario while excluding Zeno behavior. Finally, we derive an explicit expression of the proposed event-trigger condition for exponentially stabilizable systems, and demonstrate its effectiveness through simulations.

---


### 215. [TRINITY: A Multi-Perspective Benchmark for Personal-Style Video Highlight Detection](https://arxiv.org/abs/2608.29577)

**<font color=#1a73e8>作者：</font>** Qianqian Chen, Hyun Bin Kim, Denzel Elden Wijaya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional video highlight detection relies on a narrow, event-centric definition of saliency, which often fails to generalize to unconstrained personal videos where highlights are heterogeneous and perspective-dependent. To address this, we introduce TRINITY, a multi-perspective benchmark that decomposes highlight saliency into three complementary dimensions, Event, Emotion, and Nature, within a unified temporal framework. Leveraging this multi-faceted view, we propose a shared-backbone multi-branch architecture designed for parallel multi-perspective prediction via view-specific experts. Comprehensive experiments demonstrate that our method significantly outperforms state-of-the-art baselines, achieving gains of +7.15/+3.62 mAP (rho=15%/50%) on Mr. HiSum and +10.82 mAP on YouTube Highlights. These results validate that multi-perspective modeling provides a more robust and comprehensive formulation of video saliency, especially for complex real-world scenarios. The benchmark and relevant codes will be released upon acceptance. The benchmark is available at this https URL and the code is available at this https URL.

---


### 216. [Not Safe for All: Auditing the Dialect Penalty in Text-to-Image Safety Pipelines](https://arxiv.org/abs/2608.29589)

**<font color=#1a73e8>作者：</font>** Minkyu Kim, Juhwan Choi, YoungBin Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) safety guardrails fail to generalize equitably to non-standard dialects. Evaluating 23,080 paired prompts across five English dialects, we formalize this failure as the dialect penalty, where filters trigger based on linguistic surface features rather than semantic intent. Text-level filters fail in opposing directions: NSFW-T over-flags benign dialect prompts and LatentGuard over-flags toxic ones (bias gaps up to +28.29 pp), while the OpenAI Moderation API under-detects them. A controlled typo ablation confirms this penalty originates from flagging dialectal features, not generic out-of-distribution sensitivity. The pixel-level generator is largely dialect-agnostic; the penalty enters at text processing and cascades unevenly to post-hoc guardrails. We show this bias tracks training data imbalance and is mitigable via group-balanced retraining, with an ablation attributing the gain to balanced exposure rather than to the worst-group objective of GroupDRO (group distributionally robust optimization). Current pipelines systematically fail dialect speakers, an equity failure masked by mean accuracy benchmarks. Our official code and dataset are publicly available at this https URL.
Content Warning: This paper contains offensive, toxic, or disturbing text prompts and generated images.

---


### 217. [On the Resilience of Text-to-Video Diffusion Models to Hardware Faults](https://arxiv.org/abs/2608.29598)

**<font color=#1a73e8>作者：</font>** Zachary Coalson, A M Aahad, Stella Doehring 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present the first systematic study of the resilience of text-to-video (T2V) diffusion models under random hardware-level faults. While T2V models are widely used for automated video generation due to their ability to produce high-quality, temporally coherent, and realistic videos, their iterative denoising process and spatiotemporal dependencies introduce unique failure modes. We perform an extensive fault-injection study covering both computational and memory faults across three T2V models and a representative benchmark. Our results show that (1) a single fault can degrade overall performance by up to 3.7\%, with semantic correctness more affected than perceptual quality; (2) memory faults are more damaging than computational faults, high-order exponent bits are particularly vulnerable, and the widely-used bfloat16 is more susceptible than alternative formats; and (3) 7-28\% of faults cause visible artifacts, including semantic changes such as added objects, suggesting that single faults are sufficient to alter output semantics. Our findings reveal reliability risks in deployed T2V systems and motivate further research on improving fault resilience. Code: \href{this https URL}{this https URL}.

---


### 218. [Adaptive Doubly Robust Off-Policy Evaluation for Ranking Policies under Diverse User Behavior](https://arxiv.org/abs/2608.29600)

**<font color=#1a73e8>作者：</font>** Kosuke Iguchi, Ren Kishimoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy evaluation (OPE) of ranking policies is challenging be- cause selecting and ordering multiple items from a candidate set makes the number of possible rankings grow combinatorially with the number of candidates and the ranking length. Consequently, Inverse Propensity Scoring (IPS), whose importance weight is the full-ranking probability ratio under the evaluation and logging policies, can have excessive variance. Independent IPS (IIPS) and Reward Interaction IPS (RIPS) reduce variance by imposing fixed assumptions on how users browse rankings, but may introduce bias when those assumptions mismatch actual behavior. Adaptive Inverse Propensity Scoring (AIPS) addresses this trade-off by adap- tively marginalizing importance weights over the actions that affect each position-wise reward. It attains minimum variance within a class of unbiased IPS-based estimators when the true user be- havior model is observed. However, its estimation accuracy may still degrade for longer rankings, and AIPS does not use a reward model for residual correction. We propose Adaptive Doubly Robust (ADR), which combines adaptive importance weighting with re- ward regression through a control-variate correction. We establish its unbiasedness when the true user behavior model is observed and characterize a sufficient condition under which it reduces vari- ance relative to AIPS. Across synthetic experiments with 10,000 simulations per condition, ADR improves mean squared error over AIPS and conventional ranking OPE estimators across a range of logged-data sizes and ranking lengths.

---


### 219. [Wide Learning: Learning to Reach Evidence](https://arxiv.org/abs/2608.29608)

**<font color=#1a73e8>作者：</font>** Junzhou Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning is usually evaluated after an evidence interface has been fixed. A dataset, sensor suite, query language, action set, or experimental protocol determines which observations can be obtained, and learning is judged by what it extracts from them. We study a complementary capability. A learner's state can determine which evidence-generating experiments it can reliably realise under bounded resources, even when primitive affordances remain fixed. We call this learner-relative experiment family its effective epistemic reach, and use Wide Learning for task-relevant learning-induced changes in that this http URL formalise effective reach relative to learner state, deployment budget, reliability threshold, and evaluation distribution. In a controlled construction, two hidden worlds have exactly the same public observation law. An informative diagnostic exists in a fixed five-primitive substrate. Before calibration, one address attempt realises it with probability at most $2^{-10} = 1/1024$, below a pre-specified 0.95 threshold; after calibration, held-out realisation is 1. Public-channel total variation is 0, whereas the realised diagnostic has total variation 1, and sealed binary risk moves from approximately 1/2 to 0. The construction establishes that learning can change effective epistemic reach even when primitive affordances and deployment resources are held fixed. It opens a complementary evaluation question for learning systems: not only what they infer from available evidence, but what informative evidence experience teaches them to bring within reach.

---


### 220. [nnMNet: Baseline for Martian Terrain Semantic Segmentation](https://arxiv.org/abs/2608.29609)

**<font color=#1a73e8>作者：</font>** Ming-Han Lee, Chi-Yeh Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation is a crucial task for understanding Mars, the most Earth-like planet in our solar system. However, it is challenging because the Martian surface is highly unstructured and complex, making accurate pixel-level prediction and fine-grained annotation difficult. Recent advancements in deep learning have introduced numerous methods and datasets to address these challenges. Nevertheless, the field lacks a robust, publicly available, and reproducible baseline, as well as a unified benchmark to facilitate fair evaluations. In this work, we present nnMNet, a new baseline model designed for Martian terrain semantic segmentation. Building upon nnWNet, we integrate linear attention to better capture global context and employ lightweight convolutions to reduce computational overhead. To bridge the gap between local and global representations, we introduce the Spatially-Aware Fusion Block (SAFB), which augments and combines features with diverse characteristics. Furthermore, we establish a new benchmark by curating and standardizing three high-quality datasets for thorough evaluation. nnMNet achieves new state-of-the-art 86.61%, 83.25%, and 88.24% mIoU on SynMars-TW, SynMars-Air, and MarsScapes, respectively. Our code, models, and datasets are publicly available at this https URL.

---


### 221. [See the Change, Keep the Flow: Unsupervised Action Segmentation via Spectral-Temporal Representation Learning](https://arxiv.org/abs/2608.29611)

**<font color=#1a73e8>作者：</font>** Yun Li, Jun Xiao, Cong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised action segmentation aims to discover latent action categories and their temporal organization without action annotations. Optimal transport-based methods provide structured frame-to-action assignments, however, their pseudo-label quality is fundamentally conditioned on the representation space used to construct the transport cost. We argue that reliable OT pseudo-labeling requires a representation geometry that is simultaneously sensitive to discriminative action changes and coherent along local temporal progressions. Based on this insight, we propose SpecT-OT, a spectral-temporal representation learning framework built upon an unbalanced optimal transport pseudo-labeling concept. SpecT-OT introduces a Spectral Reparameterization Projector (SRP), which parameterizes projector weights with fixed Fourier bases and learnable coefficients to improve the modeling of rapidly varying discriminative features, and Temporal Affinity Regularization (TAR), which imposes distance-aware, label-free constraints on pairwise frame affinities to stabilize local temporal structure. The two components jointly produce more discriminative and temporally stable transport costs, yielding more reliable pseudo-labels for iterative representation learning. Experiments on four benchmarks demonstrate strong performance compared with state-of-the-art methods. SpecT-OT achieves the best results on 13 of 15 metrics, including 4.1-point MoF and 7.4-point F1 gains over the baseline on Breakfast and Desktop Assembly, respectively.

---


### 222. [PrivBench: A Holistic and Modular Benchmarking Platform for Evaluating Text-to-Text Privatization](https://arxiv.org/abs/2608.29624)

**<font color=#1a73e8>作者：</font>** Stephen Meisenbacher, Andreea-Elena Bodea, Ahmet Bilal Akın 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural Language Processing methods have enabled novel solutions and advances in the field of privacy, particularly in the sub-domain of text-to-text privatization, where the goal is to transform a sensitive input text into a privatized output by ideally masking (in)directly identifiable or otherwise private information. The evaluation of text-to-text privatization, however, is not straightforward, and the extant literature has utilized a myriad of techniques and metrics to quantify the privacy-preserving capabilities of privatization methods. Seeking to unify the evaluation of text-to-text privatization, we introduce PrivBench, a holistic and modular benchmarking platform for researchers and practitioners working on text privatization. PrivBench is holistic in that it evaluates privatization on a series of defined desiderata, which are structured into modules. PrivBench is not only modular but also extensible, allowing for future updates and benchmark versions. PrivBench is user-centered and promotes competition via real-time evaluation and a live public leaderboard. The platform is free to use and openly accessible at this https URL.

---


### 223. [SPLG-Mamba: Structure-Preserving Local-Global Mamba Network for Salient Object Detection in Optical Remote Sensing Images](https://arxiv.org/abs/2608.29626)

**<font color=#1a73e8>作者：</font>** Yi Xu, Ruichao Hou, Tongwei Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Salient object detection in optical remote sensing images (ORSI-SOD) requires dense predictions that preserve object completeness and structural continuity under complex backgrounds, scale variation, and irregular object shapes. Existing methods often localize salient regions, but their predictions may still suffer from structural degradation, including fragmented, incomplete, or locally missing foreground responses. This degradation is closely related to hierarchical feature propagation, where shallow details can introduce texture-induced background responses, deep semantics may over-smooth weak structures, and uncontrolled cross-scale fusion can disturb coherent regions. To address this issue, we propose a novel Structure-Preserving Local-Global Mamba Network, SPLG-Mamba, for ORSI-SOD. Specifically, SPLG-Mamba integrates Smooth-Detail Recalibration (SDR), hierarchy-aware Local-Global Mamba, and Gated Cross-Scale Fusion (GCSF). SDR recalibrates smoothed responses and detail residuals before state-space modeling, Local-Global Mamba assigns local modeling to shallow feature levels and global modeling to deep feature levels, and GCSF controls cross-scale detail injection during decoding. Experiments on ORSSD, EORSSD, and ORSI-4199 demonstrate state-of-the-art results and improved structural completeness and continuity. The code is available at this https URL

---


### 224. [Unsupervised Multi-Scale Gromov-Wasserstein Hypergraph Alignment](https://arxiv.org/abs/2608.29635)

**<font color=#1a73e8>作者：</font>** Lutz Oettershagen, Honglian Wang, Aristides Gionis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study unsupervised hypergraph alignment, where the goal is to infer node correspondences between two hypergraphs using only structural information, without node features, labels, seed matches, or side information. Direct higher-order formulations can represent hyperedge interactions faithfully, but they can be computationally demanding and cumbersome for non-uniform hypergraphs. Graph-reduction approaches introduce a different challenge: clique expansions keep the alignment problem on the original node set but collapse all hyperedge evidence into one pairwise graph, whereas bipartite expansions preserve incidence structure but enlarge the problem from nodes to nodes plus hyperedges. We introduce FALCON (Filtration-based hypergrAph aLignment via Cross-scale Optimal traNsport), an unsupervised optimal-transport framework for hypergraph alignment. Instead of representing each hypergraph by a single collapsed clique graph, FALCON constructs a filtration-induced sequence of clique-based co-occurrence dissimilarity matrices and jointly aligns all levels through one shared multi-scale Gromov--Wasserstein (GW) objective. The shared transport plan enforces a globally consistent node correspondence across filtration levels while avoiding the auxiliary hyperedge nodes introduced by bipartite expansion. Experiments on perturbation benchmarks derived from real-world hypergraphs show that FALCON is robust to structural noise and in almost all cases outperforms strong graph- and hypergraph-alignment baselines.

---


### 225. [Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses](https://arxiv.org/abs/2608.29641)

**<font color=#1a73e8>作者：</font>** Xinke Jiang, Zhixin Zhang, Zhibang Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly solve long-horizon tasks through multi-agent harnesses in which a central agent coordinates specialized sub-agents, tools, and environments. Training the central policy in such a harness raises two challenges. First, an action label is a low-cardinality decision, whereas its args form a high-dimensional conditional sequence; optimizing both with a shared sequence-level signal can produce conflicting gradients. Second, dynamic scheduling creates interdependent sessions with branches, parallel calls, and rewritten contexts, which cannot be faithfully reduced to one flat token sequence. We introduce Harness-RL, a structured reinforcement learning framework that combines Conflict-Aware Policy Optimization (CAPO) with interface-level black-box trajectory construction. The black-box component captures Interface Call Records, builds per-session prefix trees, and aligns outcome and process rewards with trainable tokens. CAPO uses forward activations to identify parameter partitions associated with action and args tokens, then routes their policy gradients to the corresponding subspaces. Harness-RL supports both central-only and joint multi-agent training. Across seven multi-hop question answering and agentic retrieval benchmarks, it reaches average F1 scores of 42.93 and 47.79 with Qwen2.5-1.5B and Qwen2.5-3B, respectively, while ablations validate the contribution of CAPO and favor central-only optimization in the evaluated setting. Our code is available at this https URL.

---


### 226. [Reward-guided Fine-Tuning of One-Step Generative Models via Wasserstein Gradient Flow](https://arxiv.org/abs/2608.29647)

**<font color=#1a73e8>作者：</font>** Hoseong Hwang, Woorim Han, Joungin Chun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To mitigate the time complexity of generative models, one-step generative models have recently emerged through direct mapping from noise to data in a single forward pass. However, the reward-guided fine-tuning method of one-step generative models remains largely unexplored. To address this, we consider one-step generators from an optimal transport view, investigating Wasserstein Gradient Flow (WGF) for modeling smooth and controlled distributional evolution in probability space. We then propose a novel reward-guided fine-tuning of a one-step generative model via WGF. We derive a practical training method that requires no reward gradients, thereby handling both non-differentiable and differentiable rewards. Moreover, our method provides smooth and stable reward-guided distributional updates while mitigating reward hacking and mode collapse. Experiments on 2D synthetic data, CIFAR-10, and ImageNet 256$\times$256 with diverse rewards, including JPEG (in)compressibility, class probability, Black-and-White and CLIP alignment, show that our method achieves better reward alignment compared to baselines.

---


### 227. [MedSegBenchmarker: A Raw-Count-First Framework for Controlled 2D Medical Image Segmentation Benchmarks](https://arxiv.org/abs/2608.29677)

**<font color=#1a73e8>作者：</font>** Vanessa Borst, Lukas Horn, Daniel Grillmeyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid advances in MIS, fair and reproducible comparisons of segmentation models remain challenging due to heterogeneous datasets, inconsistent evaluation protocols, and rapidly evolving architectures. In particular, comparisons often implicitly assume that model rankings are invariant to data partitioning, preprocessing, metric aggregation, uncertainty estimation, and computational constraints. The lack of extensible and unified evaluation frameworks further limits systematic investigation of new models, datasets, and training paradigms. We present MEDSEGBENCHMARKER (MSB), a configuration-driven framework for controlled benchmarking of 2D MIS. It integrates duplicate and near-duplicate image detection, group-aware data splitting, YAML study specifications, resumable training, hyperparameter optimization, cross-validation, and checkpoint-based evaluation. Rather than retaining only aggregate performance measures, MSB exports sample- and class-level pixel counts and predictions together with the evaluation context. These elementary artifacts enable post-hoc analyses without repeated inference. We demonstrate MSB in a case study involving three heterogeneous 2D datasets and multiple MIS and general-purpose vision models evaluated at 256- and 512-pixel input resolutions. Reaggregation of identical predictions changes the top-ranked architecture in three of six dataset-resolution settings, despite high rank correlations between aggregation strategies. Increasing input resolution produces model- and dataset-dependent performance gains and losses that must be considered alongside empirically measured inference complexity. These results show that seemingly minor choices in evaluation and experimental setup can affect benchmark conclusions. MSB, available at GitHub, provides a practical and extensible basis for making benchmark conditions and evaluation choices explicit and reproducible.

---


### 228. [GeoRay: Gauge-Aware Feed-Forward Satellite 3D Reconstruction in the Geodetic Frame](https://arxiv.org/abs/2608.29680)

**<font color=#1a73e8>作者：</font>** Zhe Dong, Wanqing Wu, Yuzhe Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D foundation models reconstruct perspective scenes in one pass. Satellite photogrammetry needs a different product, one that domain adaptation alone does not deliver: dense surface height in an absolute geodetic frame under non-central rational polynomial cameras (RPCs). Perspective-pretrained features are not reliably observable along RPC height rays, absolute elevation carries a low-order height--datum gauge exchangeable with sensor bias to first order, and monocular and multi-view cues fail in different regions. \method{} treats all three. Lightweight ray-consistent adapters make a frozen backbone matchable along native RPC rays. An explicit datum mechanism separates relief from absolute level and is equivariant to the vertical origin by construction, so one trained model serves zero-, one-, and sparse-control inference. Calibrated inverse-variance fusion combines the two relief streams. \bench{}, our absolute-frame benchmark of eighteen systems across in-domain, cross-dataset, and cross-city tiers, scores absolute placement without registration or test-reference leakage. On 26 held-out US3D tiles, \method{} attains $2.99$\,m absolute MAE at $91.9\%$ coverage, improves completeness-aware accuracy by $46.4$ points over the strongest compliant feed-forward baseline, remains the most accurate such system under both transfer shifts, and runs in $24$\,s model-forward time per tile. Code and models will be released at this https URL

---


### 229. [A Calibration Audit of Confidence in Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2608.29705)

**<font color=#1a73e8>作者：</font>** Nanxing Nick Deng, Qing Cheng, Niclas Zeller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models emit a per-pixel confidence that downstream systems read as a reliability signal. It is trained as a loss weight, not as an uncertainty magnitude, and whether it can be used as an error prediction has not been measured. We audit seven released backbones on thirteen datasets and score the confidence on four properties, how well it ranks error, whether its level is right on average, whether it holds across the confidence range, and whether its intervals cover the truth. The confidence ranks error well, but the predicted uncertainty is too low when it is read under conditions that are not exactly those of training. The median case is off by 2.4x across all seven models, and the error prediction is further off the more confident the model is. We show that this phenomenon can appear even though the loss's optimum is reached. A released model resumed under its own loss reaches that optimum on its training data within a few hundred updates and stays overconfident on unseen frames. A power law with two constants per backbone and dataset corrects the overall magnitude of the predicted uncertainty and leaves the ranking untouched. What no rescaling reaches is the scene, which we attribute to the model's missing knowledge of scale across predictions. Every correction we tried is close to right on average and still leaves two thirds of held-out scenes outside a five-point band, because what a scene is missing is a shape rather than a shift. We release the audit protocol, its results, and the fitted constants per model and dataset. Fitted with the target dataset held out, the constants bring the median case from 2.4x off to 1.35x, and a refit on a few labelled scenes of that dataset reaches 1.12x.

---


### 230. [The Depth Flow of Token Representations Is Nonlinear and Does Not Descend Its Own Density](https://arxiv.org/abs/2608.29706)

**<font color=#1a73e8>作者：</font>** Alexandre Quemy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A token's representation is carried through the network layer by layer. The whole vocabulary carried together forms a flow. We fit this flow's equation of motion as a discrete Langevin model over corpus-mean trajectories of Pythia-160M and Pythia-410M, and score the predicted steps on held-out tokens. Linear maps are often used as cheap surrogates for a layer. The flow they summarize is not linear: a quadratic drift beats the linear linear map at every transition of both models, and the Kramers--Moyal estimator agrees wherever its neighborhoods stay local.
We then characterize the flow further. First, we show that it does not descend its own log-density. The drift instead descends a potential that is not the density. Second, the rotational component is not negligible, $4$ to $45\%$ of the explainable drift, and the circulation shows in what the flow preserves: a token keeps its angular rank across all thirteen layers while its norm rank is shuffled and its concentration rank is reversed by the last block.

---


### 231. [Higher-Dimensional Rotary Position Embedding](https://arxiv.org/abs/2608.29715)

**<font color=#1a73e8>作者：</font>** Yixing Li, Ruobing Xie, Yudong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers rely on position embedding mechanisms in long context modeling in most cases. Rotary Position Embedding (RoPE) embeds positional information with independent 2D rotations, forming relative position terms in self-attention. However, its pairwise, block-based, and decoupled structure limits deep mixing and robustness across channels. We propose HD-RoPE, which extends RoPE from independent 2D rotations to higher-dimensional rotations and introduces a Paley-I orthogonal basis to obtain balanced, isotropic, and dense phase mixing within each rotation subspace. This significantly enhances channel coupling and rotational degrees of freedom while maintaining orthogonal stability and the relative position closure property. Furthermore, HD-RoPE is easily optimized for engineering efficiency without introducing additional trainable parameters. We have conducted extensive evaluation results demonstrating that HD-RoPE achieves significant performance improvements over standard RoPE across various popular benchmarks and in both long and short contexts.

---


### 232. [XDG: Accelerated Visual Disambiguation](https://arxiv.org/abs/2608.29733)

**<font color=#1a73e8>作者：</font>** Gonglin Chen, Ben Southall, Hanyuan Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual aliasing, also known as the doppelganger problem, remains a key challenge for structure-from-motion (SfM): visually similar but physically distinct surfaces can produce incorrect image matches and degrade reconstruction quality. Previous work mitigates this issue with geometry-aware foundation-model features, but places a heavy transformer classifier on top of the backbone, making large-scale disambiguation expensive. We introduce XDG, an efficient visual disambiguation model designed for scalable SfM. Our key observation is that a 3D foundation model already performs the cross-view geometric reasoning necessary for visual disambiguation, so doppelganger classification should adapt the backbone representation directly rather than relearn pair reasoning in a separate heavy decoder. XDG fine-tunes Depth Anything 3 with lightweight LoRA adapters and repurposes its camera tokens as compact pair-level classification tokens. A compact MLP head predicts whether a candidate image pair observes the same 3D surface. Extensive experiments show that XDG provides a favorable accuracy-efficiency tradeoff: it remains competitive with the state-of-the-art disambiguation method across pairwise and reconstruction benchmarks and delivers more than a 3x inference speedup. On individual LaMAR scenes containing thousands of images, XDG saves more than 10 hours of visual disambiguation processing. Code is available at this https URL.

---


### 233. [Reactive Peripheral Modeling for Faithful Firmware Rehosting](https://arxiv.org/abs/2608.29737)

**<font color=#1a73e8>作者：</font>** Qinying Wang, Florian Hofhammer, Eduard Vlad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rehosting enables tight control and introspection for firmware testing, but existing approaches largely fail to reach deeper application states and cannot drive embedded protocol stacks beyond early-stage initialization. This limitation reflects a broader weakness in current rehosting techniques: their inability to faithfully model complex peripheral semantics and dependencies. In particular, existing work typically relies on passive approximations of peripheral behavior and overlooks three key aspects: (i) the interplay among interrupts, MMIO, and DMA; (ii) implicit state transitions within peripherals; and (iii) interactions across multiple peripherals.
To address this challenge, we propose Reactive Peripheral Modeling (RPM), an abstraction that models hardware peripherals as reactive and stateful systems. RPM captures peripheral behavior using event-condition-action semantics, enabling faithful representation of interrupt, MMIO, and DMA scheduling, implicit state transitions, and cross-peripheral interactions. We implement RPM in Bluezz for BLE firmware rehosting and fuzzing, and show that reactive modeling is necessary to reach deep protocol states. We evaluate Bluezz on representative BLE stacks, including NimBLE, Zephyr, and Nordic SoftDevice, a closed-source commercial stack. Across 18 targets, Bluezz achieves an average basic-block coverage more than 2.6 times that of prior state-of-the-art rehosting approaches. Unlike prior approaches, which remain largely confined to advertising and scanning logic, Bluezz reliably exercises connected BLE states and uncovers five previously unknown vulnerabilities that manifest only after connection establishment. Finally, we show that RPM generalizes beyond BLE to other embedded firmware running on different MCUs.

---


### 234. [Drift Calibration in Geometric Eye Tracking Systems](https://arxiv.org/abs/2608.29739)

**<font color=#1a73e8>作者：</font>** Jiaqi Liu, Zixuan Wang, Yuhong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric eye trackers can provide the spatial accuracy required for gaze-based interaction and multimodal studies, but their measurements remain sensitive to residual session-specific calibration error. Research on correcting this error is difficult to compare because methods are typically evaluated with different devices, target layouts, and error definitions. We present a calibration-focused dataset containing 163 trials from 12 participants, with separate 18-point fitting and 32-point test grids, and use it to evaluate global, local, and composite correction functions under a common spatial-extrapolation protocol. We further introduce a lightweight neural refiner that combines ranked predictions from complementary calibrators. On this controlled dataset, post-vendor correction reduces the mean angular error from $1.53^\circ$ to $1.03^\circ$ with the strongest classical composite and to $0.96^\circ$ with the refiner. In a closed-loop gaze task, lower residual error is associated with higher performance across four online correction conditions. These results provide a reproducible data-quality benchmark for using gaze as a behavioral signal in interactive modeling.

---


### 235. [GraM-Diff: A Unified Graph-Mamba Diffusion Framework for EEG-Based Alzheimer's Disease Data Generation and Diagnosis](https://arxiv.org/abs/2608.29755)

**<font color=#1a73e8>作者：</font>** M. Tanveer, Ayush Singh Rana, Sanskriti Jain 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is a promising, non-invasive, and cost-effective modality for Alzheimer's disease (AD) detection, but deep learning methods are limited by small and imbalanced clinical datasets. Generative augmentation offers a solution, yet existing approaches rely on inefficient class-specific models or fail to capture complex spatial and temporal brain dynamics. To address this, we propose GraM-Diff, a unified classifier-guided Graph-Mamba diffusion framework for EEG synthesis. It embeds Graph Convolutional Networks within a diffusion U-Net to model inter-electrode connectivity and Bidirectional Mamba state-space blocks for linear-complexity long-range temporal modeling. Latent-space classifier guidance lets a single model generate both healthy and pathological EEG within a shared representation, avoiding fragmented per-cohort pipelines. Across four EEG-based AD benchmarks, synthetic augmentation improves classification, yields superior Context-FID and correlation scores over strong generative baselines, and enhances robustness in data-scarce settings.

---


### 236. [Building the Truman Show: A TrustZone-Based Framework for Lightweight Out-of-band Kernel Security Monitoring](https://arxiv.org/abs/2608.29758)

**<font color=#1a73e8>作者：</font>** Zhenling Duan, Pan Dong, Renshuang Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing number of vulnerabilities in operating systems, together with sophisticated kernel-level threats (e.g., rootkits), has weakened the effectiveness of traditional in-kernel protection mechanisms. Since these defenses operate at the same privilege level as the kernel, they share the same attack surface and can be bypassed once the kernel is compromised. Isolation-based security approaches provide stronger protection by separating security logic from the kernel, but strict isolation often introduces semantic gaps that limit system visibility and hinder timely threat detection. In this paper, we present LOOM, a lightweight out-of-band operating system monitoring architecture built on ARM TrustZone. By leveraging TrustZone's hardware-enforced isolation, LOOM establishes a tamper-resistant monitoring environment independent of the kernel. To bridge the semantic gap, we design a lightweight semantic reconstruction mechanism in the Secure World. It selectively captures the states and behavioral patterns of critical kernel objects, such as process control blocks and kernel modules. Additionally, LOOM introduces a dual-stage hazard prevention mechanism that combines atomic memory protection with an interrupt-driven adaptive agent to detect and mitigate kernel rootkit activities. An address translation cache is further incorporated to optimize repeated address access and reduce monitoring overhead. Overall, we develop a multi-layered collaborative architecture with platform, functional, and auxiliary layers for secure and efficient kernel monitoring. A prototype of LOOM has been implemented on the Phytium D2000 platform. Experimental results indicate that LOOM incurs negligible overhead while maintaining a strong monitoring capability. Furthermore, a security capability analysis based on CVE cases demonstrates that LOOM can detect and mitigate various kernel attacks.

---


### 237. [SynCrash: A Multi-Stage Pipeline for Zero-Shot Accident Detection and Localization in Traffic Surveillance Video](https://arxiv.org/abs/2608.29759)

**<font color=#1a73e8>作者：</font>** Arkya Jyoti Bagchi, Ritul Jangir, Varun Raskar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SynCrash, a multi-stage pipeline for zero-shot accident detection, spatial localization, and collision-type classification in fixed-view CCTV surveillance video. Our approach addresses the ACCIDENT at CVPR 2026 Challenge, which requires predicting when an accident occurs, where in the frame the impact happens, and what type of collision it is, all without access to labeled real-world training data. The pipeline operates in three decoupled stages: (1) Temporal localization via a VideoMAEv2-giant backbone fine-tuned on CARLA-based synthetic clips with metadata-aware embeddings and dense sliding-window inference; (2) Spatial localization using YOLO for object detection combined with a physics-informed hybrid heuristic that leverages bounding-box overlap and trajectory-based reasoning to predict the impact point; and (3) Collision-type classification using a lightweight rule-based strategy derived from the number and configuration of detected vehicles. The key insight is that temporal understanding benefits from supervised fine-tuning on synthetic data, whereas spatial understanding is better served by pretrained object detectors and physics priors that transfer naturally across domains.

---


### 238. [ECA-BLS: An Efficient Complex-Augmented Broad Learning System](https://arxiv.org/abs/2608.29763)

**<font color=#1a73e8>作者：</font>** A. Rahaman, A. Quadir, M. Sajid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Broad Learning System (BLS) is an efficient alternative to deep architectures due to its fast training, analytical learning, and strong generalization under limited data. However, existing BLS variants are confined to real-valued representations, restricting their ability to capture nonlinear interactions and second-order statistical dependencies inherent in real-world data. Notably, no prior BLS model fully exploits the complete second-order statistics that naturally emerge when data are embedded in the complex domain. To address this limitation, this paper introduces the first complex augmented Broad Learning System (CA-BLS), which transforms real-valued inputs into phase-encoded complex representations and adopts widely linear modeling to jointly leverage covariance and pseudo-covariance information via complex conjugate augmentation. This enables effective modeling of latent nonlinearities, coherence structures, and second-order dependencies inaccessible to conventional BLS formulations. To mitigate the additional computational cost of complex augmentation, an Efficient Complex Augmented BLS (ECA-BLS) is further developed, reformulating CA-BLS entirely in the real domain while preserving its exact decision function, achieving up to 75\% fewer multiplications and over 60\% fewer additions. A rigorous theoretical analysis proves the mathematical equivalence between CA-BLS and ECA-BLS, ensuring zero theoretical loss. Extensive experiments on 26 benchmark datasets from the UCI and KEEL repositories demonstrate that ECA-BLS consistently outperforms classical BLS and recent state-of-the-art randomized neural networks in accuracy, average rank, and statistical significance, establishing augmented second-order modeling as a critical and previously missing dimension of BLS research.

---


### 239. [PruneShift: A Framework for Evaluating Decision Reliability in Structured Pruning](https://arxiv.org/abs/2608.29765)

**<font color=#1a73e8>作者：</font>** Hao Ye, Gaopeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning uses surrogate objectives because direct task evaluation over every feasible mask is too expensive. Most evaluations report average surrogate error or rank correlation on broadly sampled masks. These summaries do not directly test the mask chosen by the surrogate. We introduce PruneShift, an evaluation framework that separates broad predictive fidelity, fidelity near selector outputs, and the quality of the selected pruning decision. We first prove that Spearman and Kendall agreement can approach one while normalized selection regret remains maximal. We then derive sufficient conditions based on uniform error, selector suboptimality, decision margin, density ratio, and comparison mass. The analysis also yields a finite pool certificate with an explicit excess cost bound. Four studies test different links in this argument. External TextbookQA confirmation is heterogeneous: 7 of 20 simultaneous intervals favor the surrogate-selected mask, 6 favor its fixed comparator, and 7 cross zero. On a fixed Natural Questions pool, strict improvement holds in one of four settings. A controlled QQP experiment supports the proposed coverage mechanism in all 16 prespecified endpoints, although the sufficient bounds are conservative. Finally, a restricted OSSCAR reconstruction study on OPT-125M shows better local than broad fidelity in 68 of 75 primary endpoints. Independent fixed-mask confirmation is inconclusive in 24 of 25 endpoints and favors the comparator in one. These results show why predictive fit, decision reliability, and pruning method quality require separate evidence.

---


### 240. [GridFlow: Structured Latent Flow for Seamless City-Scale 3D Point Cloud Generation](https://arxiv.org/abs/2608.29793)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Muhammad Ibrahim, Atif Mansoor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic 3D city environments from remote sensing data is important for simulation, urban planning, and mixed reality, yet existing point cloud generation methods are limited to single objects or bounded indoor scenes and cannot handle the scale, seamless tiling, and partial observability challenges of city-scale generation. We present \ours{}, a multi-stage framework that generates dense, colored point clouds ($10^5$ points per $150\text{m}{\times}150\text{m}$ tile) at city scale, conditioned on satellite imagery, semantic segmentation maps, and digital surface models (DSM). A \emph{Grid-Aligned VAE} encodes each tile into a topology-preserving latent grid where tokens correspond to fixed spatial regions, enabling spatially coherent multi-modal conditioning and compact latent-space edge consistency that implicitly aligns thousands of boundary points for seamless cross-tile generation. A conditional rectified flow model synthesizes geometry latents from the fused multi-modal conditions, and an orientation-aware diffusion colorizer separately handles satellite-visible horizontal surfaces and occluded vertical façades. To support standardized evaluation, we build on public 3D data sources to introduce \emph{City3D-MultiGen}, a benchmark of $163$K densely annotated tiles from Melbourne and London with aligned point clouds, satellite images, semantic maps, and elevation data. Experiments show that \ours{} outperforms adapted point cloud generation baselines across all geometry metrics and produces visually coherent colored point clouds with seamless boundaries over arbitrarily large urban extents. Our benchmark details are available at this https URL

---


### 241. [R$^2$A: Learning Persona Policies Through Persona Representation Learning and Runtime Alignment](https://arxiv.org/abs/2608.29798)

**<font color=#1a73e8>作者：</font>** Mohan Zhang, Chengsong You, Xiaoyu Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The same Persona behavior can be beneficial in one context but harmful in another, causing static Persona elicitation to perform inconsistently across tasks. We introduce the Persona Selection--Realization Framework, which models behavior generation through a latent Persona state and decomposes it into Persona Selection and Persona Realization. The discrepancies between static Persona elicitation and an ideal Persona policy in these two components define the Selection Gap and Realization Gap, respectively. Building on this framework, we propose R$^2$A, a two-stage approach for learning Persona policies. Persona Representation Learning uses structured Who--How--What presentations to encode the target Persona's objective, conditional behavioral principles, and trajectory-level manifestations. Persona Runtime Alignment then removes the explicit Persona specification and jointly calibrates behavior selection and trajectory realization using task feedback. Across 12 evaluation settings covering the four principles of the Accountable-Professional Persona studied in this work, R$^2$A overall outperforms both the base model and static Persona elicitation. Ablation results further show that Persona Representation Learning is critical for preventing Runtime Alignment from producing behaviorally imbalanced policies and for achieving more stable Persona policy learning.

---


### 242. [RegionCache: Semantic-Aware Region Reuse for Efficient Multi-Turn Image Generation](https://arxiv.org/abs/2608.29809)

**<font color=#1a73e8>作者：</font>** Peizheng Li, Xin Ai, Hanyuan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world image generation often involves multi-turn editing, where users iteratively modify small regions while most image content remains unchanged. However, existing diffusion transformer (DiT)-based editing pipelines recompute the entire image at every turn, causing substantial redundant computation. Existing DiT acceleration methods further ignore semantic correspondence across prompts, leading to unnecessary recomputation or unsafe reuse that harms editing quality. To address this, we propose RegionCache, a semantic-aware reuse framework for multi-turn image editing that selectively reuses diffusion states from unchanged regions. RegionCache detects reusable regions through semantic overlap between consecutive prompts and cross-attention localization, and adopts an adaptive reuse schedule based on prompt similarity and contextual consistency. Experiments on PixArt-alpha demonstrate that RegionCache achieves 1.43x--2.55x end-to-end speedup while maintaining comparable image quality. Code is available at this https URL.

---


### 243. [PhasorNet: Learning Structure from Frequency for Real-Time Stereo Matching](https://arxiv.org/abs/2608.29819)

**<font color=#1a73e8>作者：</font>** Md Raqib Khan, Santosh Kumar Vipparthi, Subrahmanyam Murala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate stereo matching remains challenging in ill-posed regions such as fine structures, reflective, or transparent objects, where appearance cues are often ambiguous or unreliable. To tackle this, we propose PhasorNet, a lightweight yet powerful framework that boosts geometric discrimination via frequency-domain cues. At its core, the Phase-Augmented Transformer (PAT) injects Fourier-derived phase information into the attention mechanism, yielding photometrically robust, structure-preserving features that prioritize structural consistency in difficult areas. Additionally, we develop a Geometry-Context Fusion Refinement Module (GCFRM) that combines a full-resolution convolutional stream with a lightweight attention-based stream (leveraging WQA and CDGA blocks) to efficiently preserve fine details and object boundaries without excessive overhead. Training is further enhanced by a multi-scale Edge-guided High-Error Region (EHR) loss that adaptively focuses optimization on high-error and edge regions, guiding hierarchical cost volume refinement. With only 5.3M parameters, PhasorNet achieves state-of-the-art performance on the challenging ETH3D benchmark while exhibiting excellent cross-domain generalization on KITTI, delivering an efficient and practical solution for accurate real-time stereo matching.

---


### 244. [Null-Space Diffusion Restoration with Adaptive Uncertainty-Guided Fusion for Ultrasound Speckle Reduction](https://arxiv.org/abs/2608.29820)

**<font color=#1a73e8>作者：</font>** Juneyong Lee, Jaeyoung Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound B-mode imaging commonly suffers from speckle noise and artifacts, requiring a delicate balance between contrast, resolution, and preservation of anatomical structures. Although recently developed despeckling methods have achieved some progress, supervised learning approaches remain fundamentally limited by the ground truth paradox, which arises from the absence of noise-free, ground truth reference images in in vivo scenarios. Existing unsupervised diffusion-based methods typically enforce data consistency directly in the nonlinear log-compressed domain, which can disproportionately amplify background artifacts when mapped back to the envelope domain. To overcome these limitations, we propose an uncertainty-guided null-space diffusion (UGNS) framework, a novel label-free solution that enforces consistency correction on a stabilized positive-envelope proxy obtained via inverse log compression. The proposed UGNS introduces several technical novelties: (a) extraction of a structural prior in the stabilized envelope domain to produce a robust signal envelope that preserves anatomical structure, (b) development of an adaptive range-null reconstruction mechanism that uses an adaptive weight mask to preserve tissue regions via range-space projection, and (c) introduction of uncertainty-guided fusion in an adaptive way to mitigate sampling variability. Extensive and comparative experiments were conducted using the PICMUS benchmark and in vivo datasets. The results demonstrate that UGNS achieves competitive generalized contrast-to-noise ratio (gCNR) values across diverse datasets. In addition, it is successfully validated that UGNS effectively suppresses speckle noise while preserving fine spatial resolution. Code is available at this https URL.

---


### 245. [A^2Agent: Action-Aware Reinforcement Learning for Repository-Level Code Localization Agents](https://arxiv.org/abs/2608.29831)

**<font color=#1a73e8>作者：</font>** Doyeon Kim, Suyoung Bae, Yumin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Localizing issue-relevant code regions is a critical step in automated software engineering. However, due to their reliance on sparse trajectory-level signals, existing methods cannot identify which per-turn actions are effective and often discover correct code regions during exploration but fail to commit them. To address these limitations, we propose an action-aware reinforcement learning method that combines a per-turn reward sequence rewarding both the discovery and commitment of gold code regions with an action-level advantage estimation scheme that isolates each action's credit by grouping turns sharing the same exploration context. Extensive evaluations show that our method improves the average F1 over the state-of-the-art (SOTA) by 1.58% on SWE-Bench Verified and 8.55% on SWE-Bench Pro, with our 4B model outperforming baselines up to 8x larger. Our code is available at this https URL.

---


### 246. [You Know What I Mean: A Benchmark for Agentic Conversational Reference Grounding](https://arxiv.org/abs/2608.29834)

**<font color=#1a73e8>作者：</font>** Karen Fuchs, Uri Katz, Yoav Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Collaborative conversations frequently contain references whose targets are indirect rather than named: resolving "this looks like the fix discussed yesterday" requires combining conversational context with evidence from the surrounding workspace which is accessible through APIs or user interfaces. We formalize this problem as Conversational Reference Grounding (CoRG): using a given set of tools to resolve a reference in conversation to the unique external item intended by the speaker. CoRG is challenging because it combines lexical, semantic, and temporal cues distributed across the conversation and the external workspace. Agents must translate these heterogeneous signals into effective tool use: formulating strategies, discovering plausible candidates, inspecting their metadata and content, and ruling out close alternatives. We study CoRG through RepoRef, a benchmark of 400 developer-chat segments grounded in GitHub issues, pull requests, and commits across 92 repositories. Unlike single-shot retrieval tasks, RepoRef often requires multi-step tool use. Our results show that CoRG remains challenging for current agents, even the best agent reaches only 67.0% success rate, leaving one third of references unresolved. These findings position CoRG as a concrete benchmark for studying how agents search, inspect, and verify information in realistic multi-tool environments.

---


### 247. [SkillForge: Compositional Skill Synthesis with Verification-in-the-Loop for Generating Formally Verified Dafny Programs](https://arxiv.org/abs/2608.29841)

**<font color=#1a73e8>作者：</font>** Yanming Liu, Xinyue Peng, Jiannan Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generating formally verified programs from natural language remains challenging: existing approaches either produce code in a single pass without recourse when verification fails, or rely on open-ended agentic reasoning that is non-deterministic and opaque. We introduce SKILLFORGE, a framework that decomposes formal code synthesis into a library of atomic, reusable skills, each targeting a specific subtask such as specification inference, body synthesis, invariant generation, error diagnosis, or targeted repair, and defined by a prompt template, tool binding, and decidable success criterion. A verification-driven harness orchestrates these skills: it submits candidates to the Dafny verifier, diagnoses failures into structured categories, deterministically routes to the appropriate repair skill, and iterates until formal correctness is proved or a budget is exhausted. On a curated benchmark of natural language to Dafny specification pairs, SKILLFORGE substantially outperforms both state-of-the-art agentic approaches (including ReAct-style agents, MCTS-based repair, and RL-guided verification) and traditional iterative baselines, while requiring fewer tokens and lower latency. Ablation studies confirm that every skill contributes measurably, and the harness converges rapidly with the majority of programs verified on the first attempt.

---


### 248. [ContextBias: Controlled Evaluation of Bias Persistence Under Context Shift in Text-to-Image Models](https://arxiv.org/abs/2608.29847)

**<font color=#1a73e8>作者：</font>** Shaghayegh Kolli, Sina Emami, Moreno D'Incà 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models learn associations between concepts - in the case of this paper, people's professions, which we refer to as roles - and visual attributes. These associations can underpin many observed forms of stereotypical bias. A key open question in this area is whether these associations are stable or change when visual representations of people in professional roles are placed in different prompted contexts. We introduce ContextBias, a controlled evaluation framework, and ContextBench, a benchmark spanning 92 roles and 1,656 semantically controlled prompts, designed to isolate the effect of contextual variation on role-linked visual representations. Evaluating four state-of-the-art models on 66,240 generated images, we find that placing a role in a semantically unrelated context does not suppress role-linked attributes; instead, cross-role attribute concentration increases (pooled BI $+0.047$). Demographic cues, characteristic garments, and role-specific tools remain highly prevalent across context-free, related, and unrelated conditions, and are robust to semantic prompt reformulation. Scene composition and camera framing show the greatest context-sensitivity. These findings reveal a form of stereotypical persistence that remains largely invisible to context-free evaluations, highlighting the need for controlled contextual variation in bias benchmarking. Code and dataset: this https URL , this https URL

---


### 249. [Designing for the Next Click: Bandits for Real-Time Page Layout](https://arxiv.org/abs/2608.29850)

**<font color=#1a73e8>作者：</font>** Bhavtosh Rath, Harshith Narasimhamurthy, Bob Eisinger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> E-commerce platforms increasingly personalize user experiences through machine learning, yet page layout decisions remain dominated by static rules and manual curation. We present a scalable bandit-based system that optimizes product page layouts in real time while preserving human control over design intent. A contextual bandit model dynamically selects the most effective layout for each session using user, item, and category-level features. The system leverages a LinUCB-based policy to balance exploration and exploitation as it learns from live user interactions. The architecture is designed for seamless integration into large-scale web serving stacks, supporting low-latency inference and continuous model updates. The system was first tested on entry product pages. In online A/B deployments on a major retail platform, our approach achieved positive lifts in session-level performance metrics over a strong heuristic baseline. Our results demonstrate that contextual bandits can effectively optimize visual and structural aspects of product discovery for user engagement, providing a scalable path toward learning-to-design the web.

---


### 250. [MariSat: A Maritime Dataset for Instance Segmentation of Objects in Satellite and Aerial Images](https://arxiv.org/abs/2608.29852)

**<font color=#1a73e8>作者：</font>** Amir Abbes, Ines Harrabi, Lucas Justin Yirepoa Kinda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated maritime surveillance from satellite and aerial imagery requires large, precisely annotated datasets, which remain scarce for the instance-segmentation task, particularly for small vessels in cluttered port environments. We present MariSat, a new benchmark dataset of 1260 aerial and satellite images covering diverse port and coastal scenes, annotated at the pixel level for eight maritime object classes (sailboat, yacht, jet-ski, fishing boat, cruise ship, military vessel, tugboat and cargo ship). The dataset was produced through a semi-automatic annotation pipeline combining the textpromptable segmentation model SAM 3 with a cascade of geometric and colorimetric post-processing filters, followed by a manual correction and quality-control pass performed with the CVAT annotation platform. We describe the image-collection methodology, the annotation and correction process, and the resulting data organization. We also report class-wise statistics for the training, validation, and test splits. MariSat has already been used to fine-tune and benchmark segmentation and detection models (SAM 3 and YOLO11) for real-time maritime monitoring. We report detailed quantitative and per-class results for both tasks. The MariSat dataset is publicly available on GitHub : this https URL

---


> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
