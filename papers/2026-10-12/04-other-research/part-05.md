# 📦 其他研究 | 2026年10月12日

> 本类共 **329** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-329](./part-07.md)

---

### 201. [Evi-VN: Hard Region Guided Virtual Node Evidence Injection for GNN-Based Fraud Detection](https://arxiv.org/abs/2610.11665)

**<font color=#1a73e8>作者：</font>** Jiran Tao, Yifan Wu, Binyan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online platforms contain growing numbers of bots, deceptive reviewers, and scam accounts that imitate legitimate users. Such camouflage blurs graph neighborhoods and behavioral attributes, making it difficult for graph neural networks (GNNs) to distinguish both well-disguised fraudsters and legitimate users. Across diverse GNNs, we observe overlapping errors on a shared hard region, suggesting the presence of latent fraud evidence that graph topologies and standard features fail to capture. Fraud-specific GNNs can mitigate particular graph pathologies, yet they still make limited use of heterogeneous evidence such as structured records, text, images, and audio; uniform multimodal fusion may also disturb nodes already handled reliably by the graph. We propose Evi-VN to learn and correct these shared blind spots rather than build another fraud detector. To our knowledge, Evi-VN is the first graph fraud detection framework to use feature isolated evidence chains to correct hard regions shared across GNNs. Its evidence chains connect behavior, content, and context across structured, textual, visual, and acoustic sources, helping expose camouflage that graph neighborhoods may miss. Crucially, Evi-VN selectively applies this evidence only to likely hard samples via virtual class nodes, preserving both the reliable predictions and the input design of existing GNNs. Shared hard regions also let Evi-VN enhance generic, fraud-specific, and unseen GNNs even with imperfect evidence models. Experiments across bot, fake-review, refund-evidence, and telecom-fraud tasks validate these advantages.

---


### 202. [Early Signatures of Memorization in Diffusion Models via Basin Geometry and Cyclic Denoising](https://arxiv.org/abs/2610.11670)

**<font color=#1a73e8>作者：</font>** Nikhil Verma, Siddharthan Dileep, Anoop Singh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models generalize early in training and later reproduce individual training samples. Standard tests detect memorization only once one-shot generation produces near-copies, leaving a released model unaudited until its outputs fail. We show that memorization is encoded in the geometry of the learned energy landscape before it appears in generated samples, a state we call latent memorization. Using score divergence and basin volume, we find that localized basins form around training samples and separate them from held-out samples before the first memorized sample appears, with an onset that follows the same $O(n)$ scaling as the memorization time. We probe these basins with cyclic denoising, which repeatedly applies partial noising and denoising. Under the exact empirical score, we prove that cycling started near an isolated training sample recovers it and returns to it over any finite number of cycles with high probability. In trained models, cycling recovers training images from CelebA and CIFAR-10 checkpoints whose one-shot samples contain no copies, and at a CelebA checkpoint with 0.1% one-shot copies, 500 cycles raise the memorized fraction above 30%. Cycling also reveals degenerate attractors that match no single training image and fade as training proceeds, so residence in a basin does not by itself imply memorization. These findings hold on a Gaussian mixture, CelebA, and CIFAR-10 across optimizers, architectures, noise schedules, and training-set sizes, and extend to off-the-shelf Stable Diffusion v1.4, where the cycled conditional-unconditional divergence gap separates memorized from non-memorized prompts with an AUC of 0.944 and a TPR of 0.866 at 1% FPR. More broadly, what a diffusion model has memorized is a property of the geometry and stability of its learned distribution, and assessing it requires examining this structure rather than generated outputs alone.

---


### 203. [Camera-Noise Residuals for Face-Swap Detection: Redundant, Not Complementary, and Why](https://arxiv.org/abs/2610.11683)

**<font color=#1a73e8>作者：</font>** Danil Davydov, Bader Rasheed, Dmitriy Vatolin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fusing a learned camera-noise fingerprint with an RGB appearance backbone is an appealing route to generator-independent deepfake detection, because the noise residual is grounded in image-formation physics rather than in the texture statistics of a particular generator. We test, on FaceForensics++, whether a Noiseprint++ residual channel carries information \emph{complementary} to an RGB Xception backbone for face-swap detection. A three-model ablation (RGB-only, residual-only, late-fusion) shows that fusion does not improve over RGB alone and that the residual branch alone is near chance. A seven-level bottleneck diagnostic localizes the cause: the noise maps do carry a discriminative signal, but it is statistical---carried by the per-sample first and second moments (mean, variance, energy) of the residual---and the per-sample \texttt{InstanceNorm} layer placed at the noise-branch input, following the TruFor template, standardizes exactly those moments away (five-fold cross-validated AUC drops from $0.747$ to $0.554$). A context-crop control rules out cropping geometry, and two fixed-fusion variants that remove the bottleneck recover the statistical signal yet still fail to beat RGB on every dataset. We conclude that, on this manipulation distribution, the noise residual is redundant with RGB rather than complementary, and we give concrete guidance for practitioners adopting noise-residual fusion for face-swap detection.

---


### 204. [HI3D 3.0 (Twinkle3D): Object-specific 3D Asset Generation with High Resolution](https://arxiv.org/abs/2610.11685)

**<font color=#1a73e8>作者：</font>** Ziying Li, Shengchu Zhao, Huiang He 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-3D generation has become increasingly capable of producing objects that closely resemble the input image, and an outstanding challenge is to reproduce the depicted object itself, including the specific geometry that defines it. Inscriptions, brand marks, and repeated structures are frequently distorted or lost, despite being critical to object identity. We present Hi3D 3.0, an image-to-3D generation system targeting object-specific fidelity, with Twinkle3D as its geometry model for generating watertight triangle meshes at $2048^{3}$ resolution. Twinkle3D advances high-fidelity geometry generation along four dimensions. First, while O-Voxel/FaithC offers high representational precision, it often suffers from poor surface quality and non-watertight geometry. We address both issues while retaining its $2048^{3}$-level precision. Second, we scale diffusion generation to sequences of up to 300K geometric tokens through a redesigned DiT architecture and large-scale distributed training optimizations, reducing training time per step from approximately ten minutes to ten seconds. Third, subsequent refinement cannot fully compensate for errors introduced during initial generation; we therefore strengthen both global shape and local detail in the initial generation stage, and the resulting single-stage model surpasses prior two-stage pipelines with $512^{3}$ refinement. Finally, we introduce a fine-grained image-3D cross-modal interaction mechanism that strengthens correspondence between visual evidence and geometric tokens, improving the recovery of object-specific structures. We evaluate geometric fidelity using alignment metrics derived from silhouettes and normal fields. Hi3D 3.0 outperforms four commercial systems across all reported metrics, recovering 82.1% of inscribed characters at 98.2% precision, compared with 21.7% recall for the strongest competitor.

---


### 205. [Can Jev be Your Q or Policy in Reinforcement Learning?](https://arxiv.org/abs/2610.11692)

**<font color=#1a73e8>作者：</font>** Yi Ma, Tianpei Yang, Yaodong Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models supply reinforcement learning (RL) with priors that mitigate its longstanding weaknesses in sample efficiency and transfer, but their token-by-token generation makes queries sequential and costly. Jev, a recently released decision model, generates nothing and returns calibrated, typed answers in a single forward pass. Existing work studies foundation models in RL either as models to be trained or as generators to be prompted, and Jev belongs to neither category, having so far served only as a black box in single domains. How well such a model decides on its own in RL environments, and how it can improve RL as a component of training, therefore remain unaddressed. To this end, in this paper we first examine the requirements that the objects of an RL system place on the answers they consume, and establish that Jev can fulfill all of them except the cardinal use of a value function. The remaining objects form positions that admit several roles each. We then construct algorithms that employ Jev at three of these positions, as a reference policy, an exploration judge, and a replay rater, to improve sample efficiency, exploration, and learning performance. Across nine MiniGrid tasks and three Atari games, training with Jev outperforms a standard RL learner, including where the learner makes no progress alone, while the model itself remains untrained. To our knowledge, we present the first use of Jev within the RL learning process and establish a frozen decision model as a usable component of RL training, inviting further exploration of how Jev and other advanced decision models can improve RL.

---


### 206. [Structured Sentiment Analysis Using Sequence Labeling as Dependency Graph Parsing](https://arxiv.org/abs/2610.11695)

**<font color=#1a73e8>作者：</font>** Muhammad Imran, Ana Ezquerro, Carlos Gómez-Rodríguez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study addresses the problem of structured sentiment analysis, whose goal is to obtain a fine-grained sentiment graph where the nodes represent spans of sentiment holders, targets, and expressions, while the arcs define the relationships among them. Our proposed approach casts the task as dependency graph parsing, but departs from traditional parsing methods by solving it through sequence labeling. To do so, we leverage recent advances in linearized graph encodings that allow each word in the input to be assigned a label, effectively capturing the structure of the dependency graph. We conducted experiments on seven datasets spanning five languages (English, Spanish, Norwegian, Basque, and Catalan), showing performance competitive with leading, more complex single-model approaches.

---


### 207. [What is the goal of unsupervised machine learning?](https://arxiv.org/abs/2610.11697)

**<font color=#1a73e8>作者：</font>** Aapo Hyvärinen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised learning is one of the main branches of machine learning. Here I argue that unlike the other branches of machine learning (supervised and reinforcement learning), unsupervised learning is a rather heterogenous field that can serve several different goals. It seems futile to try to define one single goal for unsupervised learning. I identify four different goals for unsupervised learning: 1) Estimating the distribution, 2) Generating new data points, 3) Extracting features for downstream tasks, and 4) Understanding the data.

---


### 208. [Intervention anchors and scientific verification in synthetic vascular predictive representations](https://arxiv.org/abs/2610.11704)

**<font color=#1a73e8>作者：</font>** Lingsen You, Yujun Guo, Xinyu Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complete orthogonal predictive coordinates do not by themselves bind a latent direction to a named intervention. We present a mathematical and synthetic audit motivated by vascular device-vessel suitcordance. Capacity-matched least-squares predictors were exactly equivalent under complete fixed output transforms, whereas an anchor-only observer recovered interpretations only within the span of known perturbation signatures. Six three-dimensional configurations across 64 seeds gave a maximum paired prediction discrepancy of 6.7e-15 but a median untransported edit error of 1.513. Coordinate transport removed that error. Noisy and weak anchors constrained calibration stability, and changing the representation basis required recalibration or verified transport. Across 256 additional fits in dimensions 3-24, prediction equivalence persisted within 4.0e-15. We then evaluated nine deliberate runnable fault classes across 64 seeds. All 576 faulty executions completed, but each violated at least one reconstruction, prediction, delivered-edit or scope contract; all 320 valid control records passed. Repeating a faulty implementation gave exact self-agreement despite error against the separately computed simulator expectation. For one omitted-direction defect, probe coverage followed its analytic law, and rank-aware abstention protected unsupported interpretations. Scalar-noise experiments exposed both missed weak faults and excessive rejection under narrow relative tolerances. These controls provide an executable separation of prediction, semantic support and scientific acceptance. They are synthetic numerical audits, not clinical validation, neural JEPA-Anything replication, agent learning or patient treatment-effect estimation.

---


### 209. [Does an Illumination Prior Help Face-Swap Detection? A Controlled Study of Temporal Self-Blended Images](https://arxiv.org/abs/2610.11706)

**<font color=#1a73e8>作者：</font>** Danil Davydov, Bader Rasheed, Dmitriy Vatolin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-blended images are widely used to train face-swap detectors, but primarily capture blending artifacts. We investigate whether adding illumination inconsistencies improves detection. Temporal Self-Blended Images (T-SBI) transfer lighting statistics between frames of the same video, with the mismatch controlled by luminance difference ({\Delta}L). Using five training regimes and a three-seed comparison of high- and low-{\Delta}L training, we find no evidence of illumination-specific improvements. AUC differences remain within seed variability across four datasets, and an analysis of 506,328 attribute-binned samples shows no preferential reduction in errors under harsh lighting. Instead, T-SBI shifts prediction scores, changing optimal thresholds by approximately 0.34 on FaceForensics++ and 0.30 on Celeb-DF, making comparisons at a fixed threshold misleading. However, T-SBI improves robustness to heavy JPEG compression on DFDC (AUC 0.780 versus 0.696), potentially reflecting greater reliance on low-frequency cues. These findings highlight the importance of evaluating training methods against their intended targets and accounting for threshold effects.

---


### 210. [DeltaReplay: Task-Relative Memory Reuse for Mobile GUI Agents](https://arxiv.org/abs/2610.11707)

**<font color=#1a73e8>作者：</font>** Yudong Bai, Yihong Chen, Quanming Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-augmented mobile GUI agents store successful execution trajectories and reuse them in later tasks, but a stored trajectory rarely matches a new task exactly. The new task may use different parameters, share only some of its steps with a stored trajectory, or have no relevant record in memory. Forcing the agent to use irrelevant memory can mislead it, whereas discarding memory that may still be useful deprives it of guidance from past experience. To address this dilemma, we propose DeltaReplay, a step-level memory reuse framework that decides how to use existing memory without modifying it. We observe that the reusable part of a stored record is determined not by the record itself but by its relation to the new task, mainly through two factors: page-level consistency and action-level generality. We therefore store execution trajectories as paths in a transition graph, whose nodes (pages) and edges (actions between pages) capture these two factors. At reuse time, the action on each edge is split into a task-independent operation and task-specific parameters. DeltaReplay then compares each recorded step with the new task and the current screen, and decides whether to follow it, execute it after replacing its parameters, or leave it to the base agent. On AndroidWorld and SPA-Bench, DeltaReplay improves the task success rate over a base agent with the same backbone by up to 10.3 and 25.0 percentage points, respectively. These results indicate that deciding at each step how to use retrieved memory lets agents benefit even from partially matching trajectories.

---


### 211. [4-Tensor Attention Model for Semantic Physical Reality](https://arxiv.org/abs/2610.11716)

**<font color=#1a73e8>作者：</font>** Jongwook Kim, Sangheon Yun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We describe a 4-tensor attention model that predicts the next semantic state of a scene, for video generation and robot planning. A window of states has positions (x, t) and two fibers, a semantic fiber and a temporal-context fiber, and one softmax normalizes attention jointly over the window. Frames and an agent's situation are written as those states; the encoder, the renderer, and the planner remain outside the update. To test the update on its own, we train on ROCStories, where each window poses the same next-sentence task at the semantic layer. On the validation split, with one seed per setting, the last-sentence cross-entropy on the three matched settings is lower for the 4-tensor model than for a free-running one-dimensional transformer by 5.3% at H=2, L=2, by 2.6% at H=4, L=2, and by 2.4% at H=4, L=3. At H=4, L=2 the parameter counts are nearly the same, 172.5M and 175.9M. On the same two GPUs that 4-tensor run finished in 2.4 hours and the baseline run in 45.2 hours; the baseline is trained by free-running decoding, one sequential forward pass per target token.

---


### 212. [MultiWorldBench: Do Independently Controlled Views Describe One Shared World?](https://arxiv.org/abs/2610.11723)

**<font color=#1a73e8>作者：</font>** Zhangbo Xu, Ruoxi Zhang, Rui Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiplayer world models must ensure that independently controlled views remain consistent with one shared and persistent world. We introduce MultiWorldBench, a diagnostic Minecraft benchmark containing 495 case configurations across seven task suites and ten capabilities, including independent control, cross-view motion, shared-state synchronization, persistence, structural reasoning, concurrent interaction, and delayed revisit. We evaluate Solaris, Gamma-World, and MineWorld, using Engine GT as a reference. Gamma-World achieves the highest ten-capability average among the generated systems at 21.39, followed by Solaris at 20.88 and MineWorld at 1.89, while Engine GT reaches 91.69. Gamma-World performs better on several control, shared-state, and revisit capabilities, whereas Solaris leads in cross-view motion and race-condition consistency. Nevertheless, all generated systems score at most 8.00 on state persistence and 1.33 on structural consistency, and none succeeds in spatial reasoning or building-identity preservation. Human preferences produce the same overall ranking and show strong alignment with the automatic evaluation, with a mean dimension-level Spearman correlation of 0.96. These results show that plausible individual views do not yet constitute a coherent multiplayer world.

---


### 213. [Addressing Overcommitment in the Reasoning of Gendered Economic Memes under Multimodal Ambiguity](https://arxiv.org/abs/2610.11724)

**<font color=#1a73e8>作者：</font>** Kushal Kanwar, Dushyant Singh Chauhan, Kapil Rana 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal meme understanding is increasingly used to analyze socially sensitive content, yet existing models often exhibit biased behavior when interpreting economic dependence and social roles under ambiguity. Many memes express economic relationships through sparse text or symbolic visual cues, providing insufficient evidence for gendered attribution. In such underspecified settings, models tend to rely on pretraining correlations, leading to hallucinated and stereotypical economic role assignments. In this work, we study gendered economic dependence in image-text memes through the lens of contextual sufficiency and identify epistemic overcommitment-inferring roles without adequate evidence-as a primary source of bias. We propose CGER-Net, a context-grounded multimodal framework that estimates whether the input provides sufficient evidence for gendered economic reasoning and applies evidence-gated inference to enable confident attribution when cues are explicit while favoring principled abstention otherwise. We evaluate CGER-Net on EconMeme-GE, a curated dataset of image-text memes annotated as Men, Women, Neutral, or Ambiguous. Across strong contemporary multimodal baselines, CGER-Net reduces Gender Overcommitment Rate by up to 44% on ambiguous instances while maintaining comparable accuracy on unambiguous cases. Human evaluation further shows that 79% of generated rationales are judged as epistemically aligned with the available evidence. These results highlight the importance of modeling when not to infer for reliable and responsible multimodal analysis.

---


### 214. [Onboard Marine Anomaly Detection on $Φ$sat-2: From Simulation-Based Development to In-Orbit Demonstration](https://arxiv.org/abs/2610.11735)

**<font color=#1a73e8>作者：</font>** Clotilde Szywala, Thomas Goudemant, Marjorie Bellizzi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Onboard Artificial Intelligence can improve responsiveness and bandwidth efficiency of Earth Observation systems by processing data directly on the satellite. This paper presents the experience gained from the development, onboard integration, and post-launch adaptation of a lightweight marine anomaly detection pipeline deployed on the European Space Agency's $\Phi$sat-2 mission. The application combines sea segmentation, self-supervised feature encoding of marine regions, generic anomaly detection based on deviations from a normal sea state, and optional characterization of selected anomaly types. Before launch, the pipeline was trained and validated on simulated $\Phi$sat-2 imagery to assess algorithmic performance and compatibility with resource-constrained onboard hardware. After integration and functional validation in the mission environment, early experiments on real $\Phi$sat-2 acquisitions revealed a significant mismatch between simulated and in-orbit data. The pipeline was therefore retrained on real Level-1 imagery using an improved annotation strategy to better handle ambiguous marine regions, substantially enhancing performance. Beyond demonstrating the onboard feasibility of the application, the $\Phi$sat-2 experience highlights the importance of robust annotation strategies and sensor-aware design, and shows that simulation-based development is valuable for pre-flight risk reduction, while reliable scientific validation requires representative in-orbit data and should be clearly distinguished from functional validation.

---


### 215. [Towards Unified Evaluation of Prompt Enhancers for Video Generation](https://arxiv.org/abs/2610.11736)

**<font color=#1a73e8>作者：</font>** Yawen Shao, Yubo Zhu, Ziyun Dai 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video generators can realize increasingly complex visual narratives, positioning the prompt enhancer (PE) as a critical bridge from concise user instructions and multimodal references to structured cinematic plans. However, existing PE evaluation relies on rendered videos, imposing substantial computational and human costs, slowing PE training and iteration, and conflating PE quality with downstream generator behavior. To address this gap, we introduce PEBench, the first unified benchmark for direct PE evaluation across text-to-video, image-to-video, and reference-to-video prompt enhancement. It comprises 1,100 expert-verified cases and 1,005 visual assets, spanning 35 fine-grained tasks with diverse temporal, cinematic, audiovisual, and multi-reference requirements. In addition, we develop PEBench evaluation, an evidence-grounded framework that combines modality-aware fact extraction with rubric-based assessment across 24 criteria. Our systematic evaluation of representative open- and closed-source PE methods reveals an emerging shift from fine-grained descriptive expansion toward intent-preserving cinematic planning, while the caption-reconstruction and forward-refinement methods show complementary strengths in cinematic coverage and semantic fidelity or internal coherence, respectively. Human validation shows that PEBench scores align closely with expert judgments of enhanced prompts and downstream videos from Wan3.0 and MiniMax-H3, indicating that prompt-level evaluation reliably reflects downstream utility.

---


### 216. [Uncovering and Fixing Collider Bias in Bayesian PINNs](https://arxiv.org/abs/2610.11737)

**<font color=#1a73e8>作者：</font>** Michael Obermayr, Robert Peharz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian physics-informed neural networks (B-PINNs) are a popular framework for parameter and state inference from sparse or noisy observations. They are commonly formulated via a collider structure, in which physical and trajectory parameters are assumed to be a priori independent and become coupled through virtual likelihoods on differential-equation residuals that enforce physical consistency. We show that this modeling choice can induce severe systematic bias in the posterior over physical parameters: even when the prior is favorably centered on the ground-truth parameters, the resulting posterior can drift away and concentrate far from them. As a remedy, we advocate a hierarchical chain model in which physics generates trajectories, which in turn generate observations. The chain model does not suffer from this posterior bias, but it poses a harder, so-called doubly intractable, inference problem due to a physics-dependent normalization constant. This challenge can be resolved by discretizing the underlying stochastic dynamics, after which the chain posterior can be sampled exactly with particle MCMC. We identify two distinct mechanisms characterizing the collider bias, derive analytical approximations of their magnitudes, and establish diagnostic criteria for predicting when standard B-PINNs remain reliable. Experiments confirm the predicted bias and show that the chain formulation successfully avoids it.

---


### 217. [Scalable AI Uncertainty Quantification via Generalized Laplace Active Subspaces](https://arxiv.org/abs/2610.11738)

**<font color=#1a73e8>作者：</font>** Wouter N. Edeling, Peter V. Coveney  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty quantification (UQ) is essential for deploying neural networks in scientific and high-stakes applications, but full Bayesian inference over the network parameters is computationally infeasible. We propose a low-rank generalized Laplace approximation for neural-network UQ based on a small number of data-informed curvature directions. Starting from a generalized Bayesian posterior defined through an empirical loss, we construct a local Gaussian approximation around a pretrained set of weights in this active curvature subspace. The posterior variances in the retained subspace are available in closed form, and the prior variance is calibrated by an empirical Bayes procedure. The generalized Bayesian formulation allows us to compare two posterior scalings: the standard Bayesian scaling associated with the summed negative log likelihood, and a mean-loss scaling in which the empirical loss is normalized by the number of data. A central finding is that the standard scaling induces a data-size dependent contraction of the posterior variance in the leading active directions. In regression problems, this can force the low-rank framework to retain additional weak-curvature directions in order to achieve nominal coverage of calibration data. When posterior samples are propagated through the non-linear network, these additional directions can degrade the coherence of the predictive intervals and shift the posterior predictive mean away from the pretrained model. In contrast, the generalized mean-loss scaling yields a more stable, lower dimensional active subspace and produces calibrated, coherent predictive confidence intervals. These results indicate that generalized Laplace active subspaces provide a practical and scalable route to calibrated uncertainty quantification in neural networks.

---


### 218. [Correlational Training of Morphological Neural Networks](https://arxiv.org/abs/2610.11740)

**<font color=#1a73e8>作者：</font>** Konstantinos Fotopoulos, Petros Maragos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are typically trained using first-order methods and back-propagation. It is unclear whether this approach is optimal for morphological layers whose weight Jacobians are sparse and whose resulting parameter gradients can be poor. In this work, we propose a novel weight update method for morphological neural networks inspired from the Multiplicative Weights Update (MWU) scheme. We view each morphological perceptron as an instance of the learning from experts' advice problem in logarithmic space, and use a correlation-based reward that favors inputs aligned with the desired output change, regardless of whether a strong gradient signal has reached their weight. We empirically evaluate our approach by training fully connected layers both as stand-alone models and as parts of larger transformer networks. Across nine benchmarks, correlational training yields improvements on eight, by up to 32.84 percentage points, while substantially reducing run-to-run variability.

---


### 219. [TraceRelay: Attention-Aligned Recurrence over Rolling Traces](https://arxiv.org/abs/2610.11743)

**<font color=#1a73e8>作者：</font>** Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present TraceRelay, an attention-aligned recurrent architecture that distributes persistent representations over a rolling sequence of low-dimensional traces. Local right looking attention forms increments from lower-layer representations; delivery is delayed until all attended inputs are in the causal past. A fixed additive phase recurrence accumulates the delayed increments, and left-looking attention reads the resulting residual augmented stream. A stride-wise prefix sum supports parallel prefill and bounded-buffer continuation. We study 36 small-model runs on Equal Repeats, bounded Dyck closing-type prediction, and causal Most-Freq generation, using three seeds per setting. At trained length 256, Equal Repeats models with recurrent phase inheritance reach 98.81-99.69% accuracy versus 50.73-51.63% for separately trained variants without inheritance, despite the latter receiving more updates. Accuracy drops sharply at lengths beyond the training range. At the longest evaluated lengths, models with more dimensions in the middle layer's recurrent traces perform better on Dyck (76.34% versus 55.49% close accuracy at length 4096), whereas models with fewer trace dimensions perform better on five-symbol Most-Freq (70.74% versus 55.60% exact generation at length 1024). These contrasting cases motivate further study of how the size of recurrent representations should be chosen for different tasks, without establishing a general rule across tasks or model configurations.

---


### 220. [The Ball and the Box: Two Geometries of Computation in Superposition](https://arxiv.org/abs/2610.11744)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Lequan Lin, Dai Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural representations can encode more features than they have dimensions, a phenomenon known as superposition. We study the dimension needed to compute Boolean gates from such representations. For a single threshold layer with a Gaussian random dictionary and uniformly random sparse Boolean inputs, we derive sharp dimension thresholds under two error criteria. A vanishing expected error count can require more dimensions than correctness of every output with high probability. Shared reads explain the gap: rare realizations can produce many errors at once. The expected-count threshold has ball geometry, while joint reliability has box geometry when a gate is evaluated on every feature tuple. Optimizing shared readout weights and biases gives explicit thresholds for conjunction, disjunction, and majority. For pairwise conjunction, the analysis also describes the transition near the threshold, in agreement with exact simulations.

---


### 221. [Streaming-Aware Diffusion for Real-Time Video Super-Resolution via Cross-Step Attention](https://arxiv.org/abs/2610.11746)

**<font color=#1a73e8>作者：</font>** Harris Partaourides, Sotirios Chatzis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time video super-resolution requires high spatio-temporal fidelity under strict latency constraints, challenging diffusion models due to their iterative sampling cost and limited temporal coordination. We propose a streaming-aware framework that adapts pretrained single-image latent diffusion models for efficient video super-resolution (VSR) by exploiting the sequential structure of video streams. Our Cross-Step Attention mechanism reuses intermediate denoising features across adjacent frames and diffusion steps, enabling temporal information exchange without explicit temporal modeling. We further introduce Trajectory-Coupled Diffusion Scheduling, which aligns adjacent diffusion states and provides cleaner intermediate representations for cross-step conditioning, improving temporal coherence. These components are integrated into a streaming inference pipeline that incrementally propagates latent states across frames, reducing the effective computational complexity from $O(N \cdot S)$ to $O(N + S)$ for $N$ frames and $S$ diffusion steps. Experiments on REDS4 and YouHQ40-Test demonstrate improved perceptual quality and temporal realism while maintaining frame-wise stability. Our method achieves over 40 FPS at $512 \times 512$ resolution after cold start, enabling real-time VSR without explicit temporal modeling.

---


### 222. [Where Draft Trees Lose Target Mass: Exit-Guided Speculative Decoding](https://arxiv.org/abs/2610.11750)

**<font color=#1a73e8>作者：</font>** Shijing Hu, Xuancheng Ren, Zhihui Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tree-based speculative decoding verifies multiple draft continuations in one target-model pass, but finite trees built from draft scores face a fundamental draft-target mismatch. We ask whether better exact verification can increase acceptance on a fixed tree and how target feedback can improve the tree itself. Through a target-flow view, we identify a canonical exit law and prove that one plus target coverage sharply bounds the expected output-block length, including the bonus token, of any exact path verifier. All optimal verifiers share the same exit and bonus-token law, already attained by representative predraw-and-follow and sequential residual verifiers. This yields Tree Exit Verification (TEV), an exact, level-parallel procedure using one exit-node decision and one bonus-token decision. The exit law also identifies missing target probability, providing node-level feedback for Exit-Guided Draft-Tree Training (ExitTrain) on inference-time draft trees. Experiments across dialogue, code, and mathematical reasoning validate fixed-tree equivalence: ExitTrain increases average output-block length by 13%, while TEV reduces verifier-stage latency by 15%, yielding a 14% end-to-end speedup over DDTree. Our results distinguish two opportunities: better draft trees for higher acceptance and more direct verification for lower latency. Code: this https URL.

---


### 223. [Dino Forcing Flow Models: Do not denoise what you can predict](https://arxiv.org/abs/2610.11751)

**<font color=#1a73e8>作者：</font>** Arijit Ghosh, Lucas Degeorge, Paul Couairon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-denoising pretrained representations such as DINO can substantially improve the training speed and quality of flow matching models, but it introduces a second denoising trajectory and requires carefully designed schedules. We propose a simpler alternative: predict the pretrained representation directly, then condition the model on its own prediction. This removes the need for a second ODE and any representation-specific denoising schedules, while retaining the benefits of representation guidance. Our approach converges substantially faster and achieves better generation quality as measured by FID score. On ImageNet, it outperforms the state of the art in latent space at 2x fewer epochs than prior methods; in pixel space, it improves FID over comparable prior methods by more than 20%. These results support a simple principle: do not denoise what you can predict. Our code is openly available at this https URL.

---


### 224. [What Output-Only Review Cannot Verify: Study Contracts for Research Agents](https://arxiv.org/abs/2610.11754)

**<font color=#1a73e8>作者：</font>** Eitan Waks, Ben Glocker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Some defects in an AI-generated study can be identified from its artifacts; others require knowledge of what was approved before execution. We propose study contracts that bind declared experimental choices, run obligations and claim scope to recorded execution evidence, and distinguish this contract-relative verification from scientific truth. A diagnostic using eight self-authored clean/mutated pairs illustrates the information boundary. A deterministic checker applying a registered, fault-specific rule to approved and executed objects detected all eight registered mutations. Across eighteen recorded judge aliases given individual metadata-filtered packages without pair context or the registry-selected fault label, 104 of 144 mutated evaluation cases received defect flags; the remaining cases comprised 32 abstentions and eight terminal failures, with no explicit clean decisions on mutated cases. Some packages retained approval and execution fields, including digests. The prompt instructed judges to abstain when evidence was insufficient. These results characterize a deliberately information-asymmetric development setting; they do not isolate the effect of authoritative information from differences in task specification and rule selection, and they are not comparative verifier quality or agent reward hacking. We identify full-information comparisons, legitimate-adaptation controls and closed-loop agent evaluations as necessary tests of whether contract checks improve useful compliant completion under optimization.

---


### 225. [SR-TTA: Spatial-Redundancy Test-Time Adaptation for Interference-Robust Respiration Sensing](https://arxiv.org/abs/2610.11755)

**<font color=#1a73e8>作者：</font>** Jingyuan Liu, Zheng Chang, Haoqiu Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Future 6G networks aim to expose sensing as a native service by reusing communication infrastructure. We study respiration sensing on a cell-free massive multiple-input multiple-output (MIMO) base station, where a 64-antenna channel must be fused into a breathing waveform. The state-of-the-art hand-crafted fusion is near-optimal in benign conditions. It collapses, however, under strong in-band motion interference, whose frequency falls inside the respiration band. We show that a learned complex-weight beamformer recovers respiration by spatial nulling, and that the remaining gap to a per-recording oracle can be closed at deployment by label-free test-time adaptation. Crucially, we identify which label-free signal makes this work. Frequency- and variance-based criteria cannot separate an in-band interferer from breathing. Our spatial-redundancy test-time adaptation (SR-TTA), which maximizes consistency across random antenna subsets under an out-of-band spectral veto, preserves benign performance in our tests. The respiration-rate error drops from 5.8 to 0.8 breaths per minute (bpm) under simulated in-band interference, and the pipeline maps onto the Open Radio Access Network (O-RAN) architecture as O-RAN distributed-unit (O-DU) range-gating, an adaptation xApp, and a calibration rApp. On real testbed recordings, a one-time cross-subject calibration plus SR-TTA reduces failures from 47% to 7%, drawing level with the hand-crafted combiner using label-free test-time adaptation.

---


### 226. [Skill-V: Verifiable Self-Evolving Skill Library for Interactive Agents](https://arxiv.org/abs/2610.11781)

**<font color=#1a73e8>作者：</font>** Jie Ma, Zhipeng Qian, Yufei Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive agents can turn experience into reusable skills, yet existing self-evolving skill libraries primarily improve by accumulating new knowledge. Failures may lead to new skills, while previously stored skills are less often revisited as new evidence arrives. However, growth alone does not ensure reliability, as a retrieved skill may be inapplicable under the current task conditions, and an existing skill may encode a mis-specified operational boundary. Reliable skill evolution therefore requires not only adding knowledge, but also testing and revising what is already stored. We introduce Skill-V, a verifiable self-evolving skill library. To make stored knowledge testable, we propose representing skills as versioned, falsifiable contracts that link semantic intent to observable behavioral criteria. We use environment outcomes to drive library evolution. Specifically, task failures motivate skill addition, while disagreements between contract evaluations and task outcomes guide revisions to existing skill boundaries. To validate these revisions, we require them to preserve protected semantic constraints and satisfy non-regression criteria for rubric-outcome metrics on historical replay evidence. Finally, we employ an applicability-aware filter to exclude candidates judged confidently inapplicable to the current task. Across ALFWorld and WebShop, Skill-V achieves success rates of 95.3% and 85.9%, respectively, while maintaining a more compact skill library than growth-oriented baselines. Applicability-aware filtering reduces incorrect skill invocations, and outcome-grounded revisions correct mis-specified skill boundaries without degrading performance on previously observed evidence. These results show that reliable skill evolution requires more than accumulating experience: the library must learn which knowledge to retain, when to revise it, and when it should be applied.

---


### 227. [In-Ride Alcohol-Impairment Detection in E-Scooterists with False-Alarm Control](https://arxiv.org/abs/2610.11783)

**<font color=#1a73e8>作者：</font>** Marco Capuccini, Rahul Rajendra Pai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shared e-scooter services have become a widely adopted urban transport mode. While most users ride responsibly, alcohol intoxication stands out among the factors contributing to severe crashes. Nonetheless, countermeasures remain limited to single-point reaction tests and night bans that suspend the service altogether. This paper proposes a new approach in which onboard sensors evaluate the rider as the trip unfolds, raising an alarm as soon as enough evidence of impairment has accumulated. Specifically, we introduce a detector that operates on inertial and throttle measurements, with a provable bound on the rate of false alarms. Experiments on sensor data from 141 rides, in which 25 participants rode while sober and at two target blood alcohol concentration levels, confirm that the bound holds, whereas baselines and ablations either exceed it or lose detection performance, and in some cases delay the alarm. At a bound of 0.023, the detector identifies 91% of the rides performed at the higher concentration and 50% of those at the lower one, with median detection times of 25 and 27 seconds, respectively. We further show that an embedded implementation meets the real-time requirement, making mitigation actions feasible onboard, without requiring data to leave the vehicle. Overall, this work lays the ground for interventions that reach impaired riders as soon as possible, sparing the sober ones the burden of a pre-ride test or the suspension of the service at night, while letting operators budget false alarms against user experience.

---


### 228. [From Sparse Representations to Behavioral Insights for Multimodal Depression Assessment](https://arxiv.org/abs/2610.11787)

**<font color=#1a73e8>作者：</font>** Guimin Hu, Zihao Song, Jiachen Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal depression assessment offers a promising approach to analyzing behavioral patterns associated with depression. However, existing methods often rely on dense and opaque multimodal representations, making it difficult to interpret the behavioral patterns underlying their predictions. In this work, we introduce BehavDep, a sparse factor-based framework that decomposes multimodal behavioral representations into sparse latent factors and associates them with behaviorally meaningful concepts through a semantic bridge. To address the mismatch between user-level annotations and heterogeneous video-level behaviors, BehavDep further learns video-level depression tendency scores under weak supervision and aggregates information across multiple observations for user-level assessment. Extensive experiments demonstrate that BehavDep achieves the best overall assessment performance while revealing complementary modality contributions, heterogeneous behavioral patterns across observations, and prediction responses to concept-level editing. These results show that BehavDep provides a structured and interpretable approach to analyzing multimodal behavioral representations for depression assessment.

---


### 229. [Phase-aware video generation for physics-grounded dynamics and interactions](https://arxiv.org/abs/2610.11791)

**<font color=#1a73e8>作者：</font>** Jingfeng Ou, Kun Wang, Rui Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating physically plausible videos for solid-gas dynamics is challenging as different phases exhibit distinct dynamics yet remain coupled through physical interactions. We present PAVG, a Phase-Aware Video Generator for solid-gas dynamics and interactions. It employs a dual-branch architecture to explicitly model the distinct dynamics of solids and gases, while spatiotemporal cross-attention captures their physical interactions. This design enables PAVG to preserve phasespecific motion characteristics while producing physically consistent responses across phases. To facilitate this task, we further construct a simulation corpus comprising over 700K physical trajectories across diverse solid, gas, and solid-gas interaction scenarios. Extensive evaluations demonstrate that our PAVG produces videos with improved motion adherence, physical plausibility, and visual quality compared with existing approaches.

---


### 230. [PRAXIS: Learning Dynamics of Self-Improving Models with Symbolic Archives](https://arxiv.org/abs/2610.11803)

**<font color=#1a73e8>作者：</font>** Venkat Margapuri, Mustafa Teber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-improving learning systems adapt data selection, optimization, and auxiliary symbolic components, inducing nonstationary objectives outside standard learning assumptions. We introduce \textsc{PRAXIS}, a co-evolutionary framework that models generators, learners, and symbolic archives as interacting dynamical processes. We prove that KL-constrained generator updates and controlled archive-weight movement bound one-step objective drift, that archive updates suppress a program relative to any fixed comparator with a persistent cumulative utility advantage under sub-Gaussian noise, and that stochastic gradient descent achieves an average-stationarity guarantee whose degradation is governed by cumulative objective drift. Experiments across visual robustness, relational graph reasoning, and algorithmic graph reasoning exhibit generator stabilization, decreasing learner loss, and archive concentration consistent with these theoretical mechanisms.

---


### 231. [Fast Pose Tracking of Rigid Objects with Compact Pose Graph Optimization](https://arxiv.org/abs/2610.11815)

**<font color=#1a73e8>作者：</font>** Xiaojie Zhang, Tom Fischer, Viktor Larsson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking a novel object's 6D pose over long horizons currently requires either expensive onboarding or a reconstruction maintained throughout the sequence. This makes current trackers impractical for robotic manipulation and augmented reality, which need trackers that are ready to use and run in real time. We show that a lightweight tracking module can be applied on top of a wide range of correspondence estimation methods to keep drifts bounded while maintaining fast runtime. Our key idea is to avoid point-based optimization in the pose graph and operate only on relative pose constraints, which we weight by a derived uncertainty from the geometric alignment. This makes optimization independent of the number of correspondences while avoiding the direct inclusion of noisy point measurements, leading to fast and robust long-term tracking. Across four real-world benchmarks, our approach achieves tracking accuracy comparable to reconstruction-based trackers with a fraction of the optimization cost. Overall, these results suggest that a compact and reliable pose graph optimization can provide long-horizon consistency at substantially lower computational cost.

---


### 232. [Self-Supervised Speech Representations for Cross-Speaker Dysarthria Detection During Awake Craniotomy](https://arxiv.org/abs/2610.11825)

**<font color=#1a73e8>作者：</font>** Kanthila Chinmayi, Abdallah Nassib, Misy Harrison 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting intra-operative speech impairment during awake craniotomy is essential for preserving language function. However, automated detection remains challenging because operating-room recordings contain substantial acoustic interference, clinically relevant speech events are rare, and available cohorts are small and heterogeneous across speakers. This study presents a systematic component-wise evaluation of a pipeline for distinguishing dysarthric from no-trouble speech in the DATABRASE corpus of awake-craniotomy recordings. The pipeline incorporates speaker diarization to isolate patient speech, a multi-view representation combining handcrafted acoustic descriptors with multilayer wav2vec 2.0 embeddings, speaker-conditional normalization and transferability-based feature selection to improve cross-speaker robustness, and a cascaded classifier comprising a gradient-boosted first stage and a neural second stage. Evaluation was conducted under strict speaker-independent conditions using leave-one-speaker-out cross-validation. The results show that cross-speaker performance is influenced more strongly by the speech representation than by classifier choice. The AUCs of three classifiers differed by no more than 4.7%, whereas replacing conventional acoustic descriptors with the multilayer self-supervised representation produced AUC improvements of 18.2%-26.1%. Diarization-conditioned feature extraction and the proposed classifier cascade provided additional consistent gains. These findings indicate that reliable patient-specific speech isolation and strong pretrained representations are more important than increased classifier complexity in low-resource intra-operative settings. They also quantify the potential performance gains that may be achieved through patient-specific preoperative calibration.

---


### 233. [Probability-Signature Dynamics: Unpacking Modular Addition Learning Within Two-Layer Networks](https://arxiv.org/abs/2610.11833)

**<font color=#1a73e8>作者：</font>** Yunji Wang, Junjie Yao, Linyu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural networks trained on modular addition tasks often develop Fourier-structured representations that support exact generalization. While prior work has identified these Fourier circuits, the mechanism by which gradient-based training selects them from the data distribution remains unclear. We address this question using probability signatures, which express leading gradient interactions through conditional statistics of the training distribution. For modular addition, these signatures are cyclic shift operators and are diagonalized by the discrete Fourier transform, yielding approximately decoupled Fourier-mode dynamics. This explains the emergence of Fourier sparsity, frequency matching, and phase alignment. The same framework resolves a puzzle under label noise: corrupted examples can show faster early loss decrease than clean examples, despite lacking a coherent generalization rule. We show that noise increases conditional label collisions, strengthening early shared-coordinate reinforcement. Finally, this method can be applied to other operators. Taking XOR as an example, we observed the predicted frequency in experiments.

---


### 234. [Recovery Guarantees for Posterior Sampling of One-Bit Compressed Sensing](https://arxiv.org/abs/2610.11834)

**<font color=#1a73e8>作者：</font>** Jing Ma, Yujia Wu, Zhaoqiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the sample complexity of noisy one-bit compressed sensing for signals drawn from a prior distribution. By characterizing the effective distributional complexity of the prior via its approximate covering number, we prove that posterior sampling achieves accurate recovery with high probability when the number of measurements scales with the logarithm of the approximate covering number, up to a one-bit separation gap factor. This upper bound is robust to learned prior mismatch. Specifically, we show that posterior sampling with an approximate prior remains reliable, provided that the learned prior distribution is sufficiently close to the true signal distribution in Wasserstein distance. In addition, we establish a sample complexity lower bound for any reliable method of noisy one-bit compressed sensing, showing that our upper bound is nearly matched in its main prior dependent term. To approximate the ideal posterior sampling process for real world scenarios, we instantiate posterior sampling through a plug-and-play algorithm with diffusion priors. Experiments on the FFHQ and ImageNet datasets demonstrate the effectiveness of our proposed approach.

---


### 235. [ConventionPlay: Capability-Limited Training for Robust Ad-Hoc Collaboration](https://arxiv.org/abs/2610.11842)

**<font color=#1a73e8>作者：</font>** Abhishek Sriraman, Eleni Vasilaki, Robert Loftin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Ad-hoc collaboration often requires agents to identify and adhere to some shared convention within a cooperative task. Existing work on reinforcement learning (RL) for ad-hoc collaboration focuses on training agents that adapt to the conventions established by their partners. These methods fail to consider the possibility that while some partners might follow only a single fixed convention, others may themselves be capable of adapting to multiple conventions. Here we present ConventionPlay, an RL-based approach that teaches agents to discover their partner's optimal convention by training against a learned population of partners that exhibit different degrees of adaptability across conventions. Some of these partners follow a single, fixed convention, while others are able to adapt to a subset of the possible conventions for the task in question. The existence of partners that support a limited subset of conventions forces agents trained against this population to actively probe their partner's capabilities, and steer their partner towards the most effective joint strategy that they are capable of following. Our experimental results demonstrate that agents trained via ConventionPlay achieve superior performance to existing ad-hoc collaboration methods against test populations of partners that are compatible with multiple conventions.

---


### 236. [Open-Vocabulary Audio-Visual Event Localization via Complex-Valued Fusion](https://arxiv.org/abs/2610.11846)

**<font color=#1a73e8>作者：</font>** Anirudh Praveen, Koteswar Rao Jerripothula, Pratik Joshi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-Vocabulary Audio-Visual Event Localization (OV-AVEL) labels each video segment with an event class, including classes that were never seen during training. The dominant pipeline uses a frozen multimodal foundation model (e.g. ImageBind) to embed the visual frame, the audio mel-spectrogram, and each candidate class name into a shared space, then computes two cosine similarities for each segment against each class: visual-text and audio-text. Existing methods then collapse this pair into a single scalar score with a fixed rule (geometric mean, weighted average) before taking the argmax. Instead, we compute complex-valued similarities and learn their fusion using a complex-valued neural network (CVNN). Each modality's standard representation becomes the real part of our pipeline, and a paired companion stream supplies the imaginary part. We use imaginary part of iHSV for visual modality and CycleGAN-translated phase spectrogram for audio modality as these companion streams. This results in two complex similarities, which are then fused. While the vision and audio encoders remain frozen, only the temporal-attention blocks and the fusion CVNN are trained. The four-stream complex architecture sets a new state of the art on both OV-AVEL benchmarks. On the open (unseen-class) split of OV-AVEBench we reach 66.5/59.1/54.1% Acc/Seg-F1/Event-F1 (+1.6/+4.1/+6.6 over the previously reported fine-tuned baseline), with consistent gains for seen classes as well. We also modify AVE dataset for this task and observe that our architecture reaches 60.7/51.9/50.4% Acc/Seg-F1/Event-F1, achieving state-of-the-art OV-AVEL results on it as well. We also propose a two-stream alternative, which also sees great improvements over the baseline.

---


### 237. [VEDJE: Video-Efficient Discriminative Joint Encoder for Scalable Video-Text Retrieval](https://arxiv.org/abs/2610.11850)

**<font color=#1a73e8>作者：</font>** Shahaf Wagner, Gabriele Serussi, Dan Ben Ami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding the right video often requires distinguishing similar scenes in which different events occur. Joint matching improves retrieval, but processing rich video representations for each query is costly. VEDJE compresses features within sampled frames while keeping their representations separate in a reusable cache. Feature-change prediction supplies an auxiliary training signal that improves retrieval from the compressed cache without adding work at query time. On MSR-VTT, MSVD, DiDeMo, and ActivityNet, VEDJE improves R@1 over matched first-stage retrievers in both retrieval directions. On MSR-VTT, it reaches 59.8 text-to-video R@1 with a fine-tuned VideoCLIP-XL first stage. In the VideoPrism configuration, shrinking the per-video cache fourfold to 12 KiB preserves text-to-video recall within 0.2 points. These results show that accurate video search can operate on compact evidence, encoded once and reused as new queries arrive.

---


### 238. [DADP: Dynamic Activity-Dependent Pruning, A Reverse Hebbian-Inspired Structural Pruning Method](https://arxiv.org/abs/2610.11853)

**<font color=#1a73e8>作者：</font>** Bhushan Deshpande  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural networks are heavily over-parameterized. This redundancy incurs substantial compute and memory overhead during training and inference. Existing pruning methods rely on post-hoc magnitude thresholds or static initialization heuristics. Consequently, they often require manual per-layer sparsity targets or expensive retraining cycles. We propose Dynamic Activity-Dependent Pruning (DADP), a biologically inspired structural plasticity mechanism. During training, DADP measures connection importance via the accumulated product of pre-synaptic activations and post-synaptic error gradients. Using a single global threshold instead of fixed layer budgets, DADP dynamically allocates sparsity across network depth while naturally inducing neuron- and channel-level pruning. Across MLP, VGG-16, ResNet-18, BiLSTM-CRF, and MiniBERT architectures, DADP matches or outperforms Magnitude, SNIP and RigL, retaining 73.67% accuracy (dense baseline: 76.06%) at 99% sparsity on ResNet-18. Finally, matrix-based Shannon entropy and effective rank measurements confirm that DADP preserves latent feature diversity at extreme sparsities without representation collapse.

---


### 239. [Pose-Free Feed-Forward 3D Inpainting via Learnable Mask Attention and Support Token Refinement](https://arxiv.org/abs/2610.11857)

**<font color=#1a73e8>作者：</font>** Jingyi Pan, Dan Xu, Qiong Luo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene inpainting aims to recover missing or occluded regions in edited 3D scenes, while ensuring geometric and textural consistency. Existing approaches, however, typically require accurately calibrated camera poses, which restricts their applicability in casual, in-the-wild scenarios and introduces additional preprocessing overhead. To overcome this limitation, we present FreeInpaint, a novel feed-forward framework that generates complete and 3D-consistent scenes directly from unposed multi-view images with masked regions. At its core, FreeInpaint extends a 3D foundation model to propagate masked regions from a reference view to other unposed views, bridging 3D reconstruction and scene inpainting while preserving the model's native ability to recover camera poses and scene geometry. Our method addresses two key challenges in adapting feed-forward 3D foundation models to masked inputs. First, masked regions can corrupt cross-view correspondence reasoning, degrading pose estimation and geometry recovery. To address this, we introduce a Learnable Mask Attention mechanism that preserves the spatial anchoring of reliable observations while allowing masked regions to progressively absorb useful context in deeper layers. Second, under severe occlusions, a single forward pass often lacks sufficient appearance evidence for high-fidelity completion. Therefore, we propose a Support Token Refinement strategy, which injects diffusion-generated support evidence as confidence-weighted auxiliary tokens to refine under-observed regions while preserving the original spatial anchor. Extensive experiments across diverse datasets demonstrate that FreeInpaint achieves superior inpainting quality, eliminating the reliance on pre-computed camera poses while keeping a fast inference speed. The project page is this https URL.

---


### 240. [Understanding Latent-Dimension Scaling in Dynamical-System Learning through Spectral Reliability](https://arxiv.org/abs/2610.11866)

**<font color=#1a73e8>作者：</font>** Itsushi Sakata, Yuta Miyauchi, Yoshinobu Kawahara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In deep learning, approximation theory motivates increasing representation size. We ask whether this benefit extends to dynamics learning through autoregressive prediction. We analyze the learned time evolution through the eigenstructure of Koopman operators, using relative residuals to detect spurious eigenpairs arising even as one-step error falls. For bounded Koopman operators, we show that minimal residuals over learned dictionary spaces converge pointwise to their full-space counterparts as these spaces approximate the observable space in $L^2$. Our hypothesis is that Koopman spectral reliability helps explain how consistently rollout error decreases with increasing dimension. We compare two models of a shared Koopman autoencoder trained alternately for reconstruction and latent evolution, using latent-prediction loss (one-step prediction errors in latent coordinates) or spectral-residual loss (relative residuals of candidate eigenpairs). Across six chaotic systems, both models reduced median windowed rollout error from smallest to largest dimension. The spectral-residual model achieved lower medians than the latent-prediction model for all systems and dimensions, and its median fell by a larger factor in every system. Its median decreased monotonically with dimension in four systems, against one for latent prediction. Against four baseline families, its mean valid prediction times were nearly always longer. At the largest dimension under two-stage training, we compared eigenvalue positions with each learned dictionary's residual contours. Spectral-residual eigenvalues concentrated in low-residual regions, whereas latent-prediction eigenvalues also appeared in high-residual regions, consistent with the hypothesis.

---


### 241. [Secure Aggregate Encryption with Identity-Based Authentication for Multi-Vendor FPGA Cloud Deployment](https://arxiv.org/abs/2610.11873)

**<font color=#1a73e8>作者：</font>** Mukta Debnath, Krishnendu Guha, Debasri Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure deployment of FPGA bitstreams in heterogeneous multi-vendor cloud infrastructures requires scalable authorization, authenticated device access, and bitstream protection throughout the deployment lifecycle. Existing approaches typically address these functions through separate mechanisms, increasing coordination and key management requirements. This paper presents SAEID, a secure FPGA deployment framework that integrates aggregate authorization, certificate-free identity-based device authentication, and identity bound bitstream verification within a pairing based cryptographic framework, with symmetric cryptography used for session binding and AES 256 GCM based bitstream protection. Building on AgEID, an aggregate encryption scheme that enables individual decryption for authorized FPGA devices, SAEID extends the underlying framework to heterogeneous multi vendor deployments by supporting multiple FPGA vendors and IP providers, capability-aware authorization, and dynamic device membership. SAEID provides protection against unauthorized access to future deployments after device revocation and to prior deployments by newly enrolled devices, while retaining constant-size aggregate ciphertexts within each vendor domain and individual decryption. Experimental results demonstrate the practical performance of SAEID, with identity-based device authentication completing in approximately 4.35 ms and device membership updates requiring 4.95 to 5.09 micro seconds for device addition. The aggregate-encryption component exhibits scalable behavior with increasing device-set size. The complete SAEID software decryption path was also validated on a physical ZC702 Cortex A9 platform, requiring 191.126 ms. These results demonstrate scalable aggregate authorization with bounded authentication and dynamic-membership overhead for secure multi-vendor FPGA deployment.

---


### 242. [Relative Patch Response Learning for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2610.11876)

**<font color=#1a73e8>作者：</font>** Tianyu Wang, Ouxiang Li, Yanbin Hao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models can now synthesize highly realistic images, simultaneously increasing the risks of misinformation and visual forgery. Therefore, detecting AI-generated images becomes more essential, and a reliable detector must generalize to unseen generators and stay robust to unseen perturbations in the wild. Existing detectors are typically trained on either independently collected real and generated images or aligned real-generated pairs designed to mitigate content bias. Building on aligned pairs, recent methods form a mixed view by replacing some patches of the real image with their generated counterparts. However, we find that self-attention lets real and generated patches interact, so the feature of each patch no longer reflects its own source alone. This contextual shift makes a per-patch source label an imprecise target. To this end, we propose Relative Patch Response Learning (PRL). Instead of labeling each patch, PRL compares the same patch across two mixed views of an aligned pair and learns from its patch response, the change of its score between the views. (i) To give precise supervision under the contextual shift, a relative response objective measures the responses of source-changed patches against those of source-unchanged patches, which respond to the shift alone. (ii) To provide a reliable reference for the shift, a reference coherence objective keeps each group of source-unchanged patches moving as a whole. (iii) Since the two views contain different amounts of generated content, an area ranking objective asks the view with the larger generated area to have a higher mean patch score. Extensive experiments demonstrate the superior performance of PRL, which surpasses the best prior methods by 4.3% and 5.9% in average balanced accuracy across eight standard and three in-the-wild benchmarks, respectively.

---


### 243. [How Is Automated Research Evaluated? A Survey of Benchmarks and Evaluation Practices](https://arxiv.org/abs/2610.11877)

**<font color=#1a73e8>作者：</font>** Liulei Zhang, Dejing Zhou, Chuyue Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated research systems support literature synthesis, ideation, experiments, writing, and peer review, but their evaluation is dispersed across tasks, benchmarks, and studies that are difficult to compare directly. We review this literature from the perspective of evaluation design and evidence, covering six targets: literature synthesis, research ideation, executable workflows, scholarly writing and communication, automatic peer review, and end-to-end research. We compare task construction, evidence sources, evaluators, and scoring procedures to explain the capabilities assessed by different designs. Our synthesis highlights three recurring lessons: output checks, process checks, and human studies provide complementary information; evaluator calibration is specific to the property being assessed; and resource budgets and attempt selection are integral to interpreting performance comparisons. We identify diagnostic evaluation designs and documented gaps in supporting evidence, and translate these comparisons into reporting and audit recommendations for specific evaluation settings. The survey helps readers navigate existing evaluations, select appropriate benchmarks, and design subsequent studies.

---


### 244. [STcubeOperator: A Framework for Analyzing Spatiotemporal Event Data](https://arxiv.org/abs/2610.11894)

**<font color=#1a73e8>作者：</font>** Julius Rauscher, Lucas Joos, Mark Rohonyi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The analysis of spatiotemporal event data is essential for informed decision-making in domains such as disaster response, conflict analysis, or intelligence investigations. However, the complexity and interdependence of spatial, temporal, and multiple thematic attributes pose significant challenges for both analysis and visualization. While space-time cubes (STCs) present a powerful integrated visualization technique to analyze this kind of data, existing approaches often lack support for complex exploratory workflows, thus limiting the ability to derive meaningful insights. We address this gap by introducing STcubeOperator, a novel framework that models analysis tasks through space-time cube operations, considering them in context of visualizations, interactions, and computational choices, and implement them in an interactive visual analytics environment. By expressing analysis tasks as a sequence of multiple elementary operations--such as filtering, chopping, and flattening--our approach enables analysts to dynamically explore data from different perspectives. We further provide an open-source prototype implementing the operations in a 3D interactive environment to facilitate task-based exploratory analysis of spatiotemporal event data. We demonstrate the applicability of our framework with a case study based on real-world data on strategic and military operations in the Russia-Ukrainian War, showing its capabilities to reveal spatiotemporal patterns. An expert user study (n=8) shows how specific tasks can be solved with our framework, highlights the versatility of our approach, and provides valuable insights on which operations experienced analysts utilize in practice.

---


### 245. [Puffin: Probabilistic Learning of Spatial Detail From Coarse Observations](https://arxiv.org/abs/2610.11914)

**<font color=#1a73e8>作者：</font>** Chaitanya Jobanputra, Sebastian Vollmer, Gerrit Großmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution socioeconomic variables are important for applications such as urban planning, public health, disaster response, and resource allocation. In practice, however, these variables are often observed only at a coarse spatial resolution. We introduce Puffin, a probabilistic framework for statistical disaggregation that raises the resolution of coarse totals using high-resolution satellite embeddings as covariates. Instead of predicting a single value for each fine-resolution subregion, Puffin learns a probability distribution and is trained through an aggregation-aware likelihood. At inference, Puffin conditions these predictions on the observed regional total and splits it among the subregions. The resulting fine-scale estimates are consistent with the observed aggregate and come with calibrated uncertainty, without requiring fine-resolution labels for training. We evaluate Puffin on German and US census, employment, and election data across population, jobs, and other count variables, and study when statistical disaggregation succeeds or fails across regions, countries, and targets.

---


### 246. [From Public Posts to AI-Search Citations: Measuring the Fragility of AI Search](https://arxiv.org/abs/2610.11932)

**<font color=#1a73e8>作者：</font>** Qi Liu, Geng Hong, Xinyang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As more users ask AI systems for information, AI-search platforms are becoming a common gateway to web information. Unlike traditional search, which maps keywords to ranked pages, AI search retrieves pages, filters sources, selects citations, and generates answers before users see sources. This selection layer may amplify source bias and turn source choice into a security question. If a platform repeatedly cites domains where new users can publish posts easily, ordinary publication on those domains can become an indirect path into AI-search citations and answer text. Measuring this path is hard: platforms reveal little about citation selection, citations change over time, and the web contains so much background content that later answer changes are hard to attribute to our posts.
We present a measurement framework for identifying and measuring this low-barrier publication path, combining cross-platform citation mapping, publication-barrier testing, and marker-controlled publication experiments. Across 10 AI-search platforms, we analyze 17,211 citation instances over 6,356 unique source domains and find: (1) citations concentrate in platform-specific sources, with top-20 domains capturing 20.5--70.8% of per-platform citations, and 15 of 22 tested publication platforms tied to cited source domains had low or medium barriers for both account setup and posting; (2) in our experiments, ordinary publication on preferred platforms changed what entered AI-search outputs: 8 of 10 platforms cited a fabricated concept within seven days, and one high-preference-platform article had greater citation impact than over 20 matched low-preference posts; and (3) this path is commercially available: a $14 GEO purchase produced 13 public posts, and one AI-search platform cited GEO-posted content with our designed markers within one hour.

---


### 247. [Interval-valued SHAP in Tree-Based Models](https://arxiv.org/abs/2610.11953)

**<font color=#1a73e8>作者：</font>** Chenrui Zhu, Vu-Linh Nguyen, Marie-Hélène Masson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shapley values are among the most popular feature-attribution explanations. Efficient approaches for computing/estimating Shapley values for tree-based models, which are state-of-the-art for tabular data sets, have been developed. However, it is known that Shapley values can be (highly) unrobust due to small and realistic changes. In this paper, we propose an imprecise Dirichlet model (IDM) based method to analyze the robustness of Shapley values in decision trees and random forests. Technically, it is done by quantifying and analyzing the interval-valued Shapley values when a few unannotated instances are randomly introduced to the leaves of the trees. The interval-valued Shapley values can be defined following common principles in handling incomplete data: the pessimistic and averaging principles. We derive various theoretical results that lead to efficient computation of the interval-valued Shapley values. We also show that the proposed method can be straightforwardly generalized to the case of Banzhaf values. We then present various case studies and experiments to illustrate the behaviour of the proposed interval-valued Shapley values and their applications in debiasing uninformative features.

---


### 248. [Stochastic Grouping Conformal Prediction for Effective Subgroup Reliability](https://arxiv.org/abs/2610.11957)

**<font color=#1a73e8>作者：</font>** Meihui Zhong, Wenxin Tai, Ting Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction offers a distribution-free coverage guarantee, making it especially attractive for clinical applications. Standard conformal prediction, however, provides such guarantees only at the population level, and its prediction sets can exhibit coverage disparities across clinically important subgroups. A natural remedy is to calibrate within predefined groups. However, this can require access to sensitive subgroup attributes and is prone to a worst-group bottleneck: protecting the most difficult subgroup can inflate prediction sets for all, increasing cognitive burden on decision makers. To this end, we propose Stochastic Grouping Conformal Prediction (SGCP), a conformal framework for subgroup-reliable uncertainty quantification. It learns a stochastic grouping map that allows each sample to draw calibration information from others with similar calibration behavior, yielding a local score law that boosts reliability across subpopulations. We prove that SGCP retains the standard coverage guarantee. Experiments on synthetic and real-world benchmarks show that it consistently reduces subgroup coverage gaps while achieving smaller or comparable prediction set sizes relative to existing baselines.

---


### 249. [Learning Which Correspondences to Trust: Confidence-Weighted Event-Camera Localization in LiDAR Maps](https://arxiv.org/abs/2610.11967)

**<font color=#1a73e8>作者：</font>** Panagiotis Kiousis, Kuangyi Chen, Jun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localizing an event camera against a pre-built LiDAR map can be cast as dense optical-flow estimation between a rendered depth view and an event image, followed by a Perspective-n-Point (PnP) solver over the induced 3D-2D correspondences. Existing pipelines rely on geometric consensus during pose estimation, but do not explicitly model the reliability or pose informativeness, i.e., how strongly a correspondence constrains the camera pose, of individual correspondences. We show that the natural way to learn it -- using the per-correspondence error to constrain the learning of confidence -- suffers from a depth-dependent bias: small pixel errors reside predominantly at large depths and do not lead to high pose informativeness. Instead, in our method (CELL), we learn a per-correspondence confidence end-to-end through the pose, using a differentiable probabilistic PnP whose log-partition term encourages weight configurations that yield a better-constrained pose distribution. The learned confidence is used in three ways: (i) it reweights the flow supervision in a decoupled training scheme that keeps pose gradients out of the flow/edge backbone; (ii) it drives a probabilistic correspondence selection at test time; and (iii) together with the network's edge-probability it weights a final edge-matching refinement. We further design a partial-completion depth representation that adds signal without hallucinating across large gaps. On M3ED and DSEC our full system improves over the LEAR baseline on the majority of the evaluated sequences: it reduces the median translation error by up to 26.9% and the median rotation error by up to 15.8%.

---


### 250. [Example-driven Parametrisations for Bayesian Shape Optimisation](https://arxiv.org/abs/2610.11984)

**<font color=#1a73e8>作者：</font>** Gabriel Diaz-Aylwin, Joseph Neighbor, Abiel Malkani Talwar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimisation is the natural tool for shape design when objectives are expensive and non-differentiable, but it needs a compact yet expressive parameterisation of the search space. Hand-crafting one is a complex endeavour requiring domain expertise, and often yields implicit infeasible regions, artificial bounds, and coupled, unordered coordinates. We instead learn the parameterisation from a collection of existing designs, applying principal component analysis to the deformations between shapes. The result is a linear, interpretable search space in which the number of components explicitly trades expressivity against dimensionality. Across aerofoils, wings, and radio-frequency cavities, spanning 2D geometry to 3D aerodynamics and electromagnetics, we show improved sample efficiency and the ability to explore beyond the confines of hand-crafted baselines.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-329](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
