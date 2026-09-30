# 📦 其他研究 | 2026年10月01日

> 本类共 **447** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

---

### 151. [DualTrack: Synchronized speech-gesture generation via symmetric coupling of pretrained priors](https://arxiv.org/abs/2609.36624)

**<font color=#1a73e8>作者：</font>** Yuanzhuo Hu, Zehan Liu, Xiaoyi Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Joint speech-gesture synthesis must coordinate two modalities despite limited paired data. Existing approaches often lack bidirectional interaction, have limited language coverage, or simplify body and finger representations. We present DualTrack, which couples pretrained speech and motion priors on a shared 12.5 Hz timeline. Causal adapters exchange previous-packet information, while current-state fusion coordinates the streams before they separately complete sixteen-codebook packets. We evaluate 43 BEAT2 recordings in four languages, with speakers held out from joint training and validation. On the shared English/Spanish inputs, without speech or motion prefixes, DualTrack achieves lower word error rate and full-motion Fréchet Gesture Distance, higher beat consistency and speech naturalness than the evaluated GELINA baseline.

---


### 152. [Distilling Agentic Systems: A Roadmap across Models, Artifacts, and Harnesses](https://arxiv.org/abs/2609.36630)

**<font color=#1a73e8>作者：</font>** Ziluowen Luo, Senzhang Wang, Chaozhuo Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern agents increasingly rely on memories, tools, and execution logic, so their competence extends beyond model parameters. This shift exposes a limitation of conventional knowledge distillation, which asks how a student model imitates a teacher model. We define Agent Distillation as the persistent transfer of task-solving knowledge from a teacher agent to a student agent. Our study organizes the field by where transferred knowledge is retained: within the model, as artifacts, through the execution harness, or across substrates. This perspective separates transfer evidence from its outcome and clarifies how knowledge moves between agent components. We develop an evaluation framework that relates retention to causal contribution and deployed utility. Together, these contributions establish a foundation for the reliable, maintainable, and safe development of increasingly complex agentic systems.

---


### 153. [Physics-Aware Machine Unlearning for Cyber-Physical Systems](https://arxiv.org/abs/2609.36633)

**<font color=#1a73e8>作者：</font>** Mohammad Zakaria Haider, Muhammad Nadeem, Mohammad Ashiqur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a physics-guided gradient-ascent-based machine unlearning method that couples the forgetting signal with the physical residual of the target cyber-physical systems, ensuring that weight updates during unlearning are steered toward physically feasible regions of the weight space. The physics residual acts as a safety fence during gradient ascent: the model is steered away from the poisoned behavioral basin and simultaneously toward physics-compliant territory, rather than toward an arbitrary alternative that may still violate domain constraints. We evaluate the proposed method against four baselines: naive gradient ascent, exact unlearning, SISA, and full retraining on an IEEE 34-bus distribution system, driven by two physics-informed neural network-based distribution energy resource controllers and validated through high-fidelity OpenDSS power-flow co-simulation. From the evaluation, we found that our proposed physics-guided model simultaneously removes poison and restores physical compliance, which are essential for the safe deployment of safety-critical cyber-physical systems

---


### 154. [PE-OPSD: Internalizing Prompt Enhancement into Flow-matching Models via On-Policy Self-Distillation](https://arxiv.org/abs/2609.36638)

**<font color=#1a73e8>作者：</font>** Mingfeng Lin, Chengfei Cai, Lin Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-image users often provide concise and underspecified prompts, whereas generative models benefit from detailed textual conditions for reliable instruction following. Existing systems bridge this gap with Prompt Enhancers (PEs) that rewrite raw prompts at inference time, introducing additional latency and leaving prompt elaboration external to the generator. We instead view enhanced prompts as privileged training information and ask whether their benefits can be internalized. We propose Prompt-Enhanced On-Policy Self-Distillation (PE-OPSD) for text-to-image flow-matching models. During training, a raw-prompt student follows its own generation trajectory, while an enhanced-prompt teacher provides vector-field targets at the states visited by the student. This on-policy supervision distills the behavior induced by enhanced prompts into the raw-prompt student without requiring additional text--image pairs. At inference, both the PE and teacher are removed, and the student generates directly from raw prompts. Across multiple model families, PEs, and benchmarks, PE-OPSD achieves the strongest aggregate prompt fidelity among the evaluated baselines, yields positive aggregate visual appeal gains, and retains the base-model inference efficiency.

---


### 155. [A Digital Simulation Toolkit for Physics-Based Generation of Realistic Experimental Scanning Tunneling Microscopy Images](https://arxiv.org/abs/2609.36639)

**<font color=#1a73e8>作者：</font>** Huanhuan Zhao, Laxmi Bhurtel, Connor Vernachio 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scanning Tunneling Microscopy (STM) is a widely used tool for characterizing surfaces of materials at the atomic scale, playing a crucial role in discoveries across condensed matter physics and materials science. Despite its extreme spatial resolution, STM is one of the most sensitive microscopy techniques and is highly prone to noise. While existing unsupervised denoising methods are very cheap to train, these are primarily focused on removing the noise with minimal recovery of key physical information. While supervised methods can offer superior performance, the major bottleneck is that a large amount of paired clean-noisy experimental images is required which are impractical to obtain. Thus, we developed a low-cost physics-driven digital toolkit to rapidly generate large volume of realistic STM images. Firstly, we simulate clean images from a chosen material system. Then, with prior knowledge of the physical characteristics of the artifacts and noise present in STM experiments, we formulate several artifact-noise functions such as Gaussian electronic noise, 1/f flicker noise, scan-line noise, background tilt and mechanical drift. These physically informed noise components are then added to the simulated clean images to generate realistic STM images. We demonstrated the capability of the proposed digital toolkit to generate AI-ready data for denoising images of the (111) surfaces of copper and lead, while preserving atoms, defects, and electron waves. We also validated the quality of the downstream image analysis of learning electron wave patterns induced by quantum interference from Cu(111) images. Results show that the supervised models trained on digitally generated AI-ready data can more effectively denoise and learn electron wave patterns on Cu(111) images than benchmarked unsupervised approaches, indicating that the proposed toolkit facilitate scientific discovery.

---


### 156. [OCA: ODE-Driven Cross-Attention for Image-to-Point-Cloud Registration](https://arxiv.org/abs/2609.36644)

**<font color=#1a73e8>作者：</font>** Pei An, Jiaqi Yang, Yulong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-attention is a crucial component in learning-based image-to-point-cloud (I2P) registration. Although existing cross-attention mechanisms have achieved promising progress, attention ambiguity remains a fundamental challenge that hinders the learning of discriminative 2D-3D correspondences. To address this problem, we revisit cross-attention and establish ordinary differential equations (ODEs) to model the ideal I2P feature interaction. Based on this formulation, we develop an ODE-driven cross-attention (OCA) module that refines feature representations and attention matrices through ODEs. In practice, OCA can be seamlessly integrated into existing I2P registration frameworks. To validate its effectiveness, we incorporate OCA into five state-of-the-art baselines and evaluate on four public benchmark datasets. Experimental results demonstrate that OCA improves registration recall by up to 5\%, 9\%, and 15\% under the standard, fine-tuning, and zero-shot settings, respectively.

---


### 157. [RankBuffer: Efficient Ranking-Based Rewards for Open-Ended Generation](https://arxiv.org/abs/2609.36652)

**<font color=#1a73e8>作者：</font>** Zixuan Yang, Yiqun Chen, Qi Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended generation lacks canonical answers, making pointwise rewards difficult to calibrate for group-based reinforcement learning. Directly ranking same-query rollouts provides a more suitable relative reward signal, but existing ranking-based reward methods can incur substantial judging cost. We introduce RankBuffer, which maintains an ordered, query-specific buffer of previously judged responses as a reusable quality scale. Each rollout is first inserted into an anchor interval through an independent coarse judgment, after which only rollouts assigned to the same interval undergo local fine ranking. The resulting complete order is converted into bounded rank rewards, while boundary expansion, local refinement, and inactive-anchor pruning adapt the buffer as the policy evolves. Across four open-ended benchmarks, RankBuffer consistently outperforms all pointwise baselines. It also achieves nearly on-par performance with the strongest ranking-based reward baseline while substantially reducing judging cost. Ablations demonstrate the importance of both local fine ranking and anchor response content, while buffer analyses show that rollout-derived anchors progressively extend and refine the covered quality scale. These results establish response reuse as an effective approach to efficient relative reward construction.

---


### 158. [Not Every Correction Helps: Gain-Guided Continual Test-Time Adaptation](https://arxiv.org/abs/2609.36655)

**<font color=#1a73e8>作者：</font>** Youjia Zhang, Huiling Liu, Soyun Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual test-time adaptation (CTTA) adapts a source model to an unlabeled test stream whose distribution may change over time. Existing TTA methods often assess prediction reliability using confidence or entropy, which primarily reflect the model's self-certainty for the current sample. In CTTA, accumulated target observations can provide complementary evidence for correcting the source prediction, but this history may become misaligned as the target distribution changes. The key question is therefore not how much the correction differs from the source prediction, but whether and how strongly it should be applied. This paper proposes Gain-Aware INtervention (GAIN), a backpropagation-free CTTA framework guided by a simple principle: history proposes, gain decides. GAIN maintains compact target statistics to form a correction proposal and a posterior-predictive evaluator that accounts for estimation uncertainty. The resulting source-relative gain estimates the proposal's benefit and determines a sample-specific intervention strength along a continuous path through efficient one-dimensional optimization. Gain-controlled predictions then update the target statistics online, limiting the propagation of unreliable corrections, all without backpropagation, sample storage, or replay. Across five benchmarks, our method achieves strong predictive performance, with favorable accuracy--calibration--efficiency trade-offs in continual adaptation. On ImageNet-C, for example, GAIN achieves 61.9% accuracy with near-source calibration. It remains stable under diverse and challenging continual shifts while running 15.9x faster than a representative optimization-based CTTA baseline.

---


### 159. [Byzantine-Robust Federated Representation Learning](https://arxiv.org/abs/2609.36660)

**<font color=#1a73e8>作者：</font>** Leonardo F. Toso, James Anderson, Rafael Pinot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study federated learning (FL) with adversarial clients, where the goal is to minimize the average loss of the honest (non-adversarial) clients without knowing their identity. Under heterogeneity, a single shared model parameter is statistically inappropriate: it cannot capture the distinct data-generating processes across clients, incurring an irreducible model-heterogeneity bias and severely limiting robustness to adversarial clients (a.k.a. Byzantine-robustness). We address this problem through representation learning, where each client learns a personalized linear head, while collaboratively estimating a shared nonlinear representation through Byzantine-robust aggregation. We demonstrate that the heterogeneity among honest representation gradients is controlled by the representation error and statistical errors that decay either with the number of data samples per client ($\tau$) or the number of iterations ($T$). In particular, our non-asymptotic parameter recovery error bound reveals three terms: (i) an initialization-dependent error that goes away with $T$, (ii) finite-sample noise terms that decreases with $\tau$ and the number of honest clients, and (iii) a stochastic gradient variance term that also reduces with $T$. Importantly, with no irreducible model-heterogeneity bias in our bounds. We extend the regression analysis to multiclass classification, and empirically validate it on CIFAR-10, FEMNIST, and School Exam Score datasets.

---


### 160. [You Only Reprogram Once: Rethinking Prolonged Training for Visual Reprogramming](https://arxiv.org/abs/2609.36661)

**<font color=#1a73e8>作者：</font>** Zizhao Li, Mohammed Yaqoob Ansari, Xinyu Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reprogramming is a parameter-efficient method for adapting pretrained models, yet its training can remain computationally expensive: even with a frozen backbone, visual prompts are often optimized through the full model for hundreds of epochs. Before changing what the pretrained model sees, we ask whether we are fully using what it already tells us. We find that modeling the full source response can already yield strong downstream predictions without prompt optimization. Motivated by this observation, we introduce You Only Reprogram Once (YORO), which constructs a downstream predictor from the frozen response space in a single forward-only traversal. Its Bayesian Discriminant Mapping (BDM) derives a covariance-aware affine mapping from streaming class statistics, requiring no backpropagation, optimizer updates, or repeated visits to the training set. When further input adaptation helps, YORO-FP optionally refines the visual prompt for 20 epochs. BDM also extends naturally to CLIP by treating attribute-prompt similarities as source responses. Across three full-data settings, YORO improves average accuracy over the strongest prior gradient-free mapping by 18.4--24.4\%. On 16-shot CLIP, it raises the four-backbone average from 71.4\% to 77.2\%. YORO-FP provides further gains on selected tasks, while validation often retains the one-pass predictor. These results suggest a different default for visual reprogramming: read out the frozen response first, and optimize the input only when needed.

---


### 161. [Stochastic Heavy Ball with Polyak Step Size and Armijo Line Search: A General Convergence Analysis](https://arxiv.org/abs/2609.36668)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang, Qitan Shi, Yuantao Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Polyak step size (PS) and Armijo line search (ALS) have received increasing attention in stochastic optimization, with encouraging empirical performance and theoretical guarantees. However, their convergence theory for stochastic heavy ball (SHB) methods remains limited. In this work, we develop a unified convergence analysis for SHB equipped with PS and ALS. To this end, we introduce a modified Armijo rule that closely parallels the Polyak step size, together with a decoupling analysis that isolates the historical dependence induced by momentum. For SHB with standard PS and ALS, we establish expected convergence for strongly convex, convex, and non-convex objectives without interpolation or restrictive conditions on the momentum parameter. Under interpolation or strong growth, we further strengthen the results to almost sure rates and last-iterate convergence. Moreover, for general settings beyond interpolation, we prove almost sure convergence to the exact optimum or to stationarity for SHB with diminishing variants of PS and ALS. These results provide a more comprehensive theoretical view of Polyak step size and Armijo line search for stochastic heavy ball methods.

---


### 162. [FineSID: Scalable and Efficient Semantic Identifier Learning for Generative Recommendation](https://arxiv.org/abs/2609.36670)

**<font color=#1a73e8>作者：</font>** Song-Li Wu, Weinan Gan, Zhaocheng Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A critical prerequisite of generative recommendation is designing semantic identifiers (SIDs) that are both scalable to large item sets and efficiently learnable. Existing SID learning methods fundamentally rely on Top-1 hard assignment during vector quantization. While heuristic strategies -- such as clustering-based initialization or forced post-hoc collision resolution -- can artificially inflate codebook coverage, they often disrupt end-to-end semantic alignment and fail to address the underlying optimization bottleneck: sparse gradient propagation. In standard Top-1 assignment, gradients concentrate on a narrow subset of frequently selected codewords, leaving the majority inherently under-trained and causing severe SID collisions. To overcome this limitation natively without relying on complex initialization priors, we propose FineSID, a unified quantization framework that moves beyond Top-1 assignment by enabling fine-grained gradient propagation across the entire codebook. Instead of updating only a single selected codeword, FineSID distributes learning signals to all codewords in a soft, differentiable manner. This design promotes globally balanced codebook optimization while strictly preserving semantic consistency, effectively alleviating SID collisions and stabilizing training in large, high-dimensional codebooks. Extensive experiments on multiple public benchmarks demonstrate that FineSID is robust to initialization configurations and consistently improves both codebook utilization and recommendation accuracy. Our work provides a principled, initialization-agnostic solution for semantic identifier learning, advancing the practicality of generative recommendation.

---


### 163. [FairDiff: Mitigating the Self-Reinforcing Matthew Effect in Diffusion Recommender Models](https://arxiv.org/abs/2609.36671)

**<font color=#1a73e8>作者：</font>** Song-Li Wu, Xianquan Wang, Zhaocheng Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While the "Matthew Effect" and filter bubbles are widely recognized outcome-level biases in recommender systems, we reveal that Diffusion Recommender Models (DRMs) uniquely compound this issue through their generative dynamics. Rather than merely inheriting data imbalances, DRMs trigger a self-reinforcing amplification of popularity bias. We identify that this phenomenon is driven by two compounding mechanisms. First, while optimization loss is universally dominated by high-frequency items across recommenders, DRMs suffer from a unique structural prior mismatch during generation. Because the forward terminal distribution of long-tailed data deviates significantly from the standard Gaussian prior, reverse sampling trajectories inherently collapse toward high-density popular items, fundamentally suppressing niche item generation. To dismantle this self-reinforcing loop, we propose FairDiff, a plug-and-play fairness-aware diffusion framework. To overcome the popularity-dominated loss, we introduce Popularity Condition Guidance (PCG). Rather than altering the training objective, PCG acts as an inference-time distributional reweighting mechanism, mathematically reshaping the score-based gradient field to penalize high-popularity regions and guide trajectories toward niche semantics. Furthermore, we design a Semantic Calibration (SC) Module to bridge the prior mismatch, aligning the forward and reverse distributions via one-step optimal transport. Comprehensive evaluations demonstrate that FairDiff achieves state-of-the-art performance while effectively mitigating the self-reinforcing Matthew Effect, highlighting its value as a general framework for DRMs.

---


### 164. [Human-inspired, Task-Dimension-Guided Exploration for Efficient Learning in High Dimensions](https://arxiv.org/abs/2609.36672)

**<font color=#1a73e8>作者：</font>** Fanyu Zhu, Jiahui An, Ni Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient exploration in high-dimensional decision spaces remains a central challenge for decision-making systems. Humans, in contrast, can navigate large decision spaces with remarkable efficiency. Recent behavioral studies suggest that humans reduce dimensionality in large decision spaces by probing candidate feature dimensions, identifying reward-relevant ones, and restricting the effective decision space. Inspired by this mechanism, we propose TDGE (Task-Dimension-Guided Exploration), a human-inspired, model-agnostic algorithm with an automatically constructed task-dimension--feature--item hierarchy. TDGE follows a top-down exploration strategy: it first selects task-relevant feature dimensions, then identifies informative features within those dimensions, and finally recommends concrete items based on the selected features. Experiments on MovieLens-20M, this http URL, and Amazon recommendation datasets show that TDGE substantially improves exploration efficiency and cold-start adaptation over baseline algorithms. Comparisons with other structured algorithms and ablation studies attribute these gains to TDGE's hierarchical structure and semantic feature-space exploration, with robust results across clustering methods and hierarchy depths. Recommendation-trajectory visualizations also show exploration patterns similar to human dimension-guided behavior.

---


### 165. [ReWorld-Track: A Recursive Event World Model for Language-Guided Multi-Camera Tracking](https://arxiv.org/abs/2609.36677)

**<font color=#1a73e8>作者：</font>** Haoyang Wu, Shoudong Han, Chaoyue Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided multi-camera tracking must preserve a target identity across unobserved gaps, where similar candidates and uncertain returns can make early associations unreliable. A wrong match can corrupt the history used to predict later observations and propagate identity errors across subsequent camera handoffs. We propose ReWorld-Track, a recursive event world model that carries association uncertainty into future predictions. Candidate matches and continued waiting define alternative target states, whose posterior probabilities are used to update a persistent recurrent belief. This representation preserves uncertainty about alternative trajectories through successive observations. This belief predicts the next camera, arrival time, and entry region, while appearance and language evidence guide association. By training across successive handoffs, the model learns to retain uncertainty that remains useful for later predictions and identity decisions. ReWorld-Track achieves HOTA scores of 65.19 on CityFlowV2 and 45.36 on MTMMC, with improved identity continuity across repeated handoffs. On MTMMC, its structured posterior update gains 0.50 HOTA points over a similarly sized generic updater and 0.94 points over fixed-moment soft association, raising next-camera accuracy from 86.03% to 87.41% and reducing median arrival-time error from 0.78 s to 0.71 s for subsequent target returns.

---


### 166. [Understanding Private Evolution as Learning-Augmented Clustering](https://arxiv.org/abs/2609.36678)

**<font color=#1a73e8>作者：</font>** Audra McMillan, Kunal Talwar, Felix Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Private Evolution (PE) is a differentially private algorithm for synthetic data generation. While it can be viewed as a Wasserstein learning algorithm, it performs much better in practice than worst-case Wasserstein analyses would predict. We recast PE as generative model-augmented Wasserstein learning. We show theoretically that when we take into account the use of a generative model that is able to capture something about the true distribution, then we can obtain much better performance bounds. For example, if the generator gives samples in the same low-dimensional space as the distribution, then sample complexity depends on intrinsic, not ambient, dimension. We also show that standard variants of PE can fail to converge on simple well-clustered instances, and propose a new geometry-aware version of PE with provable convergence on such instances. Experimentally, we show that our new algorithm is competitive with standard baselines and can improve recall.

---


### 167. [When Semantics Matter: Reliability-Aware Semantic-Rhythm Control for Co-Speech Gesture Generation](https://arxiv.org/abs/2609.36685)

**<font color=#1a73e8>作者：</font>** Zhirui Xing, Long Ye, Kaige Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-speech gesture generation aims to synthesize natural gestures that are both temporally synchronized with speech and semantically consistent with the spoken content. Although recent methods can generate rhythmically plausible motions, they often rely heavily on acoustic prosody while underutilizing textual semantics, especially when semantic annotations are incomplete, noisy, or unavailable. Consequently, the generated gestures may follow speech rhythm while failing to express the intended semantics. To address this problem, we propose a reliability-aware semantic-rhythm control framework for co-speech gesture generation. We first learn a discrete motion prior that represents continuous gestures in a compact and structured motion-code space. We then introduce a dual-branch semantic contribution estimation mechanism consisting of a full multimodal branch and an audio-only branch. Their distributional discrepancy is formulated as conditional information gain to quantify how much textual semantics changes the predicted motion. Based on this estimate, a controllable semantic-rhythm objective selectively strengthens semantic guidance in content-relevant segments while limiting unnecessary semantic intervention in rhythm-dominant segments. Furthermore, we treat background noise as an acoustic reliability condition and introduce noise-conditioned feature modulation together with beneficial latent perturbation to improve generation robustness under realistic acoustic environments. Experiments on benchmark datasets demonstrate that the proposed framework achieves a favorable balance among semantic expressiveness, rhythmic synchronization, motion diversity, and robustness, enabling reliable and controllable co-speech gesture generation.

---


### 168. [AESplat: Advancing Pose-Free Feed-Forward 3D Gaussian Splatting via Decoupled Appearance Modeling](https://arxiv.org/abs/2609.36693)

**<font color=#1a73e8>作者：</font>** Shiwei Ren, Zhiang Liu, Yongchun Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-free feed-forward 3D Gaussian Splatting (3DGS) has demonstrated remarkable potential for generalized novel view synthesis. However, existing methods typically predict Gaussian appearance attributes represented by spherical harmonics (SH) in the same manner, overlooking the fundamental distinction between view-independent and view-dependent appearance, which results in suboptimal rendering quality. In this paper, we present AESplat, a novel and general framework for pose-free feed-forward 3DGS that introduces an effective decoupled appearance modeling strategy based on an analysis of SH, enabling higher-quality rendering. Specifically, AESplat directly derives the zeroth-order SH coefficient, which represents the base view-independent appearance component, from the input images without training. The higher-order SH coefficients are subsequently predicted by a shallow multilayer perceptron equipped with two efficient 3D-aware inductive biases to model view-dependent appearance variations. Extensive experiments across multiple datasets demonstrate that our method significantly outperforms state-of-the-art approaches, achieving a $0.8$ dB improvement in PSNR over the pose-free method NAS3R and a $1.1$ dB improvement over the pose-required method DepthSplat on the RealEstate10K dataset. Project page: this https URL.

---


### 169. [Learned Queries and Keys Are All You Need: Replacing the Value Projection with Structured Transforms](https://arxiv.org/abs/2609.36698)

**<font color=#1a73e8>作者：</font>** Ene Meco, Emadeldeen Hamdan, A. Enis Cetin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To reduce the number of parameters and cache memory requirements of transformers we introduce dual-headed transformers instead of three heads. We studied Walsh-Hadamard Transform (WHT), Discrete Cosine Transform (DCT), Discrete Fourier Transform, filterbank based Shearlet Transform, and Multiplication-Avoiding (MA) operators to construct dual heads. We combine spatial patches and their orthogonal transforms (or Shearlet and MA operators) in a structure similar to the attention block. We obtained better results than triple headed transformers in ImageNet. Extensive simulation examples are presented.

---


### 170. [When Is Coarse Supervision Worth It? Cost-Aware Learning under Unknown Aggregation](https://arxiv.org/abs/2609.36704)

**<font color=#1a73e8>作者：</font>** Jianyu Xu, Smriti Jha, Aarti Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern learning systems often acquire supervision at multiple resolutions, trading annotation cost against information content. We study cost-aware two-resolution learning, where expensive fine labels reveal a vector response and cheaper coarse labels reveal a scalar aggregate formed with unknown weights, while the target remains the full response. The challenge is that unknown aggregation changes which directions coarse data can identify, so the value of coarse supervision depends jointly on cost, noise, and identification. We characterize this information geometry and develop an estimate-and-track policy that learns the aggregation rule and tracks the optimal resolution mix. We derive a closed-form break-even condition for coarse supervision and prove that the online policy attains the optimal leading cumulative-risk coefficient, with a matching local asymptotic minimax lower bound. Synthetic experiments support the predicted all-fine/mixed transition, show the online learner approaching the oracle-share benchmark, and demonstrate a finite-budget gain over all-fine acquisition when coarse supervision is sufficiently favorable. Our results provide a principled way to balance information and annotation cost across supervision resolutions.

---


### 171. [Can AI Scientists Change Their Minds? Prior-Evidence Conflict in Synthetic Universes](https://arxiv.org/abs/2609.36726)

**<font color=#1a73e8>作者：</font>** Kargi Chauhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a scientific agent distinguish a law it inferred from evidence from one it merely recognizes? We introduce Synthetic Universes, a controlled benchmark that pairs canonical famous worlds with matched twisted twins governed by nearby noncanonical mechanisms. We evaluate each reported law twice: by executing it on held-out continuations and transfer settings, and by independently checking whether it recovers the generating mechanism. In the current checkpoint of a pre-specified 60-cell study, 22 trials were graded and one additional run ended in infrastructure failure. Among 20 twin trials, 8 pass predictive verification while 5 recover the generator. The dissociation is bidirectional: six parsable outputs predict successfully while missing the mechanism, whereas three recover the mechanism but fail predictive rollout. Drag exhibits the first pattern (5/5 predictive pass, 1/5 mechanism recovery); Gravity exhibits the second (1/5 predictive pass, 4/5 mechanism recovery). Because matched famous controls, the corrected identifiability sweep, and the Evidence Ladder remain incomplete, we do not claim a confirmatory causal prior-conflict effect. Instead, the completed runs establish a narrower verification result: predictive adequacy and mechanism recovery are distinct scientific claims and require distinct tests.

---


### 172. [Can Agents Design Libraries for Agents?](https://arxiv.org/abs/2609.36730)

**<font color=#1a73e8>作者：</font>** Gabriel Orlanski, Alex L. Zhang, Avi Trost 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents increasingly build on code written by other agents, and they reimplement rather than reuse, growing the codebases later agents must work in. To measure how well agents design libraries for other agents, we introduce LibraryDesignBench, a two-phase benchmark in which an agent implements a full-featured library from a specification that defines required capabilities and potential use cases without prescribing the design. We evaluate the library through the correctness and simplicity of programs written by three user agents from different model families. The benchmark spans 242 expert-validated programming problems across 15 library-design tasks in four languages. On eleven of the fifteen tasks, agent designers reproduce the abstractions of the human-written production library. Downstream agents adopt agent- and human-written libraries alike but underuse them, reimplementing capabilities the library already provides. Our failure analysis finds that downstream agents write extra code mainly because agent-written libraries are rigid or hard to use, not because capabilities are missing. We also experiment with giving designers more prescriptive, agent-first guidance and having them test their library with subagents; this improves downstream scores and yields simpler programs. LibraryDesignBench provides both a testbed for evaluating library-design practices for agent users and an initial design baseline that improves downstream reuse.

---


### 173. [Efficient Linkage-Based Compartmentalization on CHERI](https://arxiv.org/abs/2609.36731)

**<font color=#1a73e8>作者：</font>** Dapeng Gao, John Baldwin, Jessica Clarke 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present an efficient linkage-based model for in-process compartmentalization built on CHERI memory safety, which enables fine-grained compartmentalization of the entire UNIX user-space, scaling to 10K+ compartments on desktop systems. The model's "push-button" compartmentalization along existing library boundaries regularly hosts 500+ compartments per process for large applications such as Chromium, far exceeding the number of concurrently available protection domains supported by other mechanisms (e.g., up to 16 for Intel MPK). Custom policies can further subdivide libraries. Of the thousands of C/C++ programs tested, only the V8 JavaScript engine required source-level adaptation (<300 lines of changed code concerning garbage collection and JIT compilation).
We implement the model for CHERI-extended versions of Armv8-A and RISC-V through support in the compiler toolchain and operating system. Case studies illustrate the smooth delegation of memory between compartments, compartment-aware debugging and visualization, as well as extensibility to a complex managed language runtime, demonstrating the benefits of our single-address-space model. We evaluate using multiple processors, including Arm's superscalar Morello and, notably, the first commercial CHERI-enabled RISC-V application core---Codasip's in-order dual-issue X730.

---


### 174. [Backpropagated Output Momentum: Relocating Optimizer History from Parameters to Task Space](https://arxiv.org/abs/2609.36738)

**<font color=#1a73e8>作者：</font>** Yuchen Li, Zongqi Fan, Nguyen H. Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizer momentum is usually stored as a parameter-sized moving average of past gradients, which makes history costly and fixes each past signal in the coordinates in which it was computed. We introduce Backpropagated Output Momentum (BOM), which instead stores a compact moving average of prediction errors at the model output and reprojects that history through the current network at every step. A batch-level analysis characterizes the information retained and omitted by this relocation, while the implementation preserves the current supervised gradient and can replace the first-moment component of several adaptive optimizers. As a plug-in for momentum-based optimizers, including ones that already compress their state, BOM reduces parameter-shaped optimizer state by 49.7-99.8% in three compositions and, averaged over three language backbones, paired step time by 4.0%. It also improves mean validation performance across language and vision fine-tuning, by 1.42 points in the primary five-task comparison. Language and vision pretraining studies, together with matched mechanism controls, further test the construction across output spaces and model scales.

---


### 175. [Efficient Offline Learning of Ranking Policies via Top-$k$ Policy Decomposition](https://arxiv.org/abs/2609.36740)

**<font color=#1a73e8>作者：</font>** Ren Kishimoto, Koichi Tanaka, Haruka Kiyohara 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many recommender systems such as for e-commerce and news platforms aim to provide users with rankings they are likely to interact with. Off-Policy Learning (OPL) of ranking policies enables us to learn new ranking policies using only historical logged data. However, ranking settings make OPL remarkably challenging because their action spaces consist of permutations of unique items, being extremely large. Existing methods primarily use either policy- or regression-based approaches. The policy-based approach, which typically uses importance-weighted policy gradients, can suffer from high variance due to large action spaces. The regression-based approach, on the other hand, estimates the expected reward using conventional machine learning methods, avoiding variance issues but potentially suffering from severe bias. To circumvent these issues of existing methods, we propose a new OPL method for ranking, named Ranking Policy Optimization via Top-$k$ Policy Decomposition (R-POD), which combines the policy- and regression-based approaches in an effective fashion. Specifically, R-POD decomposes a ranking policy into a first-stage policy for selecting top-$k$ actions and a second-stage policy for choosing the bottom actions given the top-$k$ actions. It learns the first-stage policy using a new policy gradient estimator and the second-stage policy via the regression-based approach. This method can substantially reduce variance, since it applies importance weighting only to the top-$k$ actions. We also demonstrate that our policy-gradient estimator for the first-stage policy is unbiased under a conditional pairwise correctness condition, which only requires that the expected reward differences of pairs of rankings sharing the same top-$k$ actions can be estimated correctly.

---


### 176. [Distinguish or Homogenize: Last-Chance Policy Identification and Risk-Budgeted Recovery under Irreversible Resource Depletion](https://arxiv.org/abs/2609.36741)

**<font color=#1a73e8>作者：</font>** Yibo Guo, Xiaodan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under irreversible resource depletion, an agent can spend resources to distinguish among latent fault models, or to change the system state so that the remaining models admit a common acceptable continuation--at which point further diagnosis becomes unnecessary. This distinguish-or-homogenize principle identifies a path that existing frameworks for identification, planning, and diagnosis do not make explicit: prior formulations treat the mapping from fault models to acceptable policies as a given, whereas LCPI makes it a function of the agent's own actions. We formalize this principle through Last-Chance Policy Identification (LCPI), where correctness is evaluated at the state the agent reaches rather than at the initial state. The Last Identifiable Margin (LIM) marks the feasibility boundary between distinguishing and homogenizing. For deterministic diagnostic graphs we provide the Exact-LIM recursion; for noisy finite-horizon recovery we propose Risk-Budgeted Compatibility Planning (RBCP), which searches a compatibility-aware frontier under a hard worst-case failure constraint. Across incident recovery on abstract microservice topologies and latent-damage navigation in MiniGrid, RBCP improves risk-feasible recovery while satisfying the failure budget. A sham control--cost-matched actions that preserve model incompatibility--eliminates the gain entirely, confirming that the benefit comes from changing which policies are acceptable for which models, not from extra search or additional budget.

---


### 177. [NesTok: Nested Self-Aligned 1D Tokenizer for Autoregressive Image Generation](https://arxiv.org/abs/2609.36756)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang, Shuhao Liu, Rong Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-dimensional (1D) variable-length visual tokenizers enable adaptive compression by varying the number of tokens, allowing downstream autoregressive (AR) models to flexibly trade off generation quality against computational cost using a single tokenizer. However, existing approaches based on nested dropout often fail to fully exploit the representational capacity of the tokenizer, resulting in suboptimal performance in both image reconstruction and generation. In this work, we introduce NesTok, a nested self-alignment framework tailored to dynamic visual tokenizers. NesTok introduces cross-length training, which jointly optimizes reconstruction across token lengths while using the full-length sequence to guide shorter counterparts, enabling shorter token sequences to approach the reconstruction quality of full-length sequences. On ImageNet, NesTok improves substantially over standard training and achieves an rFID score of 0.98. On downstream image generation, it achieves the state-of-the-art gFID score of 1.46 on ImageNet 256$\times$256 among existing variable-length autoregressive image generation methods. Code will be available at this https URL.

---


### 178. [FastVR: Efficient Streaming Video Restoration with One-Step Diffusion](https://arxiv.org/abs/2609.36757)

**<font color=#1a73e8>作者：</font>** Xiaoxu Chen, Qin Yang, Haoran Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based video restoration recovers realistic details, but its practical deployment is limited by two efficiency bottlenecks: costly VAE encoding and decoding, and the quadratic cost of full self-attention in diffusion transformers (DiTs). This paper presents FastVR, a streaming video restoration framework built on a one-step diffusion model, which delivers strong restoration quality and temporal consistency while processing 1080p video at 11 FPS on a single H20 GPU. To improve inference efficiency, FastVR combines a lightweight VAE with chunk-wise causal attention, which substantially reduces the computational cost. During training, it further adopts velocity consistency regularization and continuous trajectory learning, which improve restoration quality. Extensive experiments show that FastVR is more efficient than the evaluated diffusion baselines while achieving state-of-the-art performance on synthetic and real-world benchmarks. We hope that this work supports further progress in the community.

---


### 179. [Dual-Mode Low-Rank Learner with Bridge-Prototype Ensemble for Vision-Language Class-Incremental Learning](https://arxiv.org/abs/2609.36759)

**<font color=#1a73e8>作者：</font>** Chiyuan He, Zihuan Qiu, Fanman Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benefiting from transferable visual-textual alignment, CLIP has been widely adopted for class-incremental learning (CIL). However, existing learners either repeatedly update components shared across tasks, leading to knowledge overwriting, or overly isolate new-task updates, hindering the reuse of CLIP's transferable knowledge and limiting plasticity. Moreover, the text-based or bimodal classifier designs still fail to effectively integrate complementary information from the visual and textual modalities. To address these challenges, we introduce DuLBE, which couples dual-mode low-rank learning with a bridge-prototype ensemble classifier for exemplar-free CIL. DuLBE allocates two visual low-rank update modes according to the gradient demand and uses gradient routing to coordinate them: a compact and rewritable shared mode is selected from historically occupied visual directions to reuse transferable knowledge, while residual modes provide low-interference channels for task-specific variations. Building on the resulting stable inter-modal structure, we further construct geodesic bridges between visual prototypes and text embeddings on the unit hypersphere, and ensemble reliable bridge prototypes to compensate for the modality-gap limitations of textual decision boundaries. Extensive experiments under multiple settings show that DuLBE achieves state-of-the-art CIL performance while retaining the high parameter efficiency of low-rank tuning.

---


### 180. [QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching](https://arxiv.org/abs/2609.36760)

**<font color=#1a73e8>作者：</font>** Zunhai Su, Yuxuan Sun, Jianchao Tan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Head Latent Attention (MLA) enables expressive multi-head attention with compact caches for its content and decoupled RoPE paths, yet cache memory still scales linearly with context length and batch size. In this work, we establish a systematic model of MLA's dual-path quantization errors, characterizing their distinct effects on attention-output distortion and explaining the pronounced amplification of RoPE-path errors. Guided by this analysis, we introduce QuantMLA, a function-aligned framework for low-bit dual-path quantization. We derive path-specific transformation spaces that preserve full-precision computation while remaining fully fusible into model parameters offline, eliminating online transformation overhead. Within these spaces, QuantMLA learns path-specific transformations with function-aligned objectives: attention-output reconstruction captures the content path's coupled matching and aggregation errors, while positional QK reconstruction preserves the RoPE-induced component of the attention logits and admits a theoretical bound on output distortion. Across four MLA model families, QuantMLA enables, to our knowledge, the first reported joint INT4 caching of the content and RoPE caches with minimal accuracy degradation. Further compressing the content cache to INT2 while retaining the RoPE key cache at INT4 maintains competitive performance on challenging reasoning and code benchmarks. We develop a native low-bit MLA attention kernel that integrates unpacking and dequantization directly into attention computation. The physical cache layout provides 3.59x compression at 128K context, while a cache-pressure serving workload achieves 5.168x higher whole-job output throughput than BF16. The code will be released upon acceptance.

---


### 181. [Federated Clustering with Unknown Local and Global Cluster Cardinalities](https://arxiv.org/abs/2609.36762)

**<font color=#1a73e8>作者：</font>** Mitushi Goyal, Tarun S., Riddhanya Senapathi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated clustering methods that do not require the global number of clusters $K$ still assume that each client knows its local number $K_g$. This assumption is hard to justify when clients know no more about their data than the server does, as in fault diagnosis across independently operated industrial sites. We propose a two-phase framework in which neither count is known: each client first estimates $K_g$ from its own data, and an aggregator that requires local counts, such as FedGEM, then uses these estimates in place of the true values. For the first phase we introduce Adaptive Split--Merge (ASM), which grows a spherical Gaussian mixture by BIC-driven splitting and then merges excess components. ASM uses no labels, selects its hyperparameters on held-out client data only, and makes no assumption about how clusters are shared across clients. We derive a closed-form split criterion whose critical cluster size falls with anisotropy and rises with dimension, and show empirically that over-fragmentation grows with the number of points per cluster, which federation divides among clients. Across eight datasets, ASM with FedGEM attains a mean ARI of 0.333, against 0.256 for the next best label-free estimator and 0.361 when the true local counts are supplied. It also gives the most reliable global estimates of $K$ and is robust when client size is decoupled from local cardinality.

---


### 182. [Graph-Spectral Flow Matching for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2609.36765)

**<font color=#1a73e8>作者：</font>** Zepeng Zhang, Jhony H. Giraldo, Wenbin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series anomaly detection typically relies on evaluating discrepancies between observations and outputs produced by models trained on normal data. An alternative perspective is to characterize the distribution of normal data through the generative dynamics, i.e., the velocity field, of flow matching models. However, standard flow matching typically adopts linear probability paths that overlook dependencies among variables, leading to a misalignment with the structured data distribution. To address this issue, we propose GRASP, a flow matching framework with a graph-spectral path for multivariate time series anomaly detection. GRASP incorporates graph structure into the probability path by minimizing a fixed-endpoint action that combines kinetic energy with graph Dirichlet energy. This formulation yields a closed-form path based on graph-frequency-dependent hyperbolic interpolation. A velocity predictor trained on normal data then detects anomalies using weighted velocity discrepancies aggregated across source samples, flow times, and graph frequencies. Theoretically, we establish that GRASP is invariant to the choice of Laplacian eigenbasis and decompose its expected oracle anomaly score into bounded endpoint uncertainty and graph-frequency-weighted Fisher discrepancy. Experiments on four benchmarks demonstrate the superior anomaly detection performance of GRASP and validate the effectiveness of its graph-spectral path and weighting mechanism.

---


### 183. [Emergent Specialization in Populations of Self-Supervised Collaborative Vision Experts Without a Shared Gate or Cross-Agent Gradients](https://arxiv.org/abs/2609.36770)

**<font color=#1a73e8>作者：</font>** Aram Davtyan, Pablo Acuaviva, Sebastian Stapf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can a population of neural networks develop a useful division of labor without a shared gate or gradients between agents? We study a setting where each network has its own weights, trains independently on the same heterogeneous data, and can ask another agent for help through a forward pass. Unlike mixtures of experts, where a jointly trained gate assigns inputs to experts, specialization here must emerge without central control. We test this in a small scale proxy for predictive visual pretraining. Initially identical agents are finetuned on an unlabeled mixture of six visual domains using masked prediction of frozen DINOv3 features. We measure specialization by asking whether the best agent for an input aligns with its latent domain, and utilization by asking whether responsibility is distributed across agents. We progressively remove central control, ending with DISCO (DIStributed COllaboration) where each agent locally selects a helper, reads its internal state through a gradient free channel, and rewards its router only for the improvement that help provides. Specialization emerges and is useful. Randomly routed populations underperform a single generalist, while semantically routed populations outperform it, showing that specialization rather than population size drives the gain. Specialization persists without a central router, and gradient free communication lets nonexperts exploit emergent expertise. In DISCO, a random agent helped by the expert matches the solo generalist, while experts surpass it, including on data outside the specialization mixture. Local routers select the emergent expert for 98% of inputs. These effects persist across population size, model capacity, data imbalance, and finetuning seeds, providing measurable evidence for the dynamics needed by decentralized predictive pretraining.

---


### 184. [Beyond Conditional Independence: Root Cause Analysis with Deep Causal Models](https://arxiv.org/abs/2609.36771)

**<font color=#1a73e8>作者：</font>** Md Musfiqur Rahman, Kenneth Lee, Ziwei Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Root cause analysis (RCA) is a critical problem in many real-world scenarios. RCA enables the identification of faulty or failing mechanisms in a system by comparing anomalous observations with corresponding reference (i.e., regular) observations. However, existing approaches rely either on heuristic methods or on conditional independence tests with a strong unconfoundedness assumption, and thus fail to exploit other complicated distributional constraints in the presence of latent variables. To relax these assumptions, we model the underlying system as a causal model and the anomalous system as a change in the structural functions of the same causal model. Specifically, to handle unobserved confounders, we establish an implicit connection between distributional constraint testing and root cause analysis. To adapt our approach to data generated from arbitrary causal models, we employ the deep causal model (DCM) framework, in which we design the causal model using neural networks. Finally, we illustrate how our method, RCA-DCM, can utilize different levels of partial graphical knowledge to perform RCA. We evaluate RCA-DCM against state-of-the-art baselines on simulated datasets, a physics-based causal chamber and two micro-service applications. RCA-DCM improves top-1 accuracy over the strongest baseline on both Sock Shop (0.880 vs. 0.752) and Online Boutique (0.776 vs. 0.712), and when the true root cause in the causal chamber is unobserved and acts as a latent confounder, it recovers the exact root-cause set more often than any competing method (perfect recovery rate (PRR) 0.846 vs. 0.731).

---


### 185. [Causal-EVC: Breaking Emotional Spurious Causality via Spatiotemporal Grounding and Counterfactual Intervention](https://arxiv.org/abs/2609.36776)

**<font color=#1a73e8>作者：</font>** Cheng Ye, Weidong Chen, Peipei Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotional Video Captioning aims to generate factually accurate and emotionally empathetic descriptions. While recent methods have recognized the importance of visual causes to guide emotion perception and caption generation, they fundamentally rely on simple attention matching, which inevitably suffers from {causal redundancy and spurious correlations} in co-occurrence bias (e.g., misclassifying ``sadness'' as ``joy'' on a sunny beach), leading to severe shortcut learning from confusing backgrounds. Furthermore, existing evaluations fail to verify whether models have genuinely mastered causal reasoning or merely exploited background confounders. To address these limitations, we first construct {EVC-CauseGround}, a comprehensive benchmark with dense spatio-temporal causal annotations. Crucially, it introduces a carefully selected {Causal-Faithfulness Subset} to explicitly quantify genuine emotion-cause attribution. Second, we propose {Causal-EVC}, an emotion-grounding captioning framework, which introduces a Motion-guided Causal Spatiotemporal Localization module to precisely decouple causal triggers from background confounders. Besides, we introduce an Interpretable Sparse Emotion Routing module. By synthesizing counterfactual representations and formulating a novel counterfactual contrastive objective, we enforce the model to anchor its emotion predictions strictly on authentic causal triggers instead of confusing background. Extensive experiments show that Causal-EVC not only achieves the best performance on semantic metrics but also exhibits significant advantages in the causal-faithfulness subset, which demonstrates that our model could mine emotional cues from genuine visual causes and mitigate co-occurrence bias for interpretable multimodal emotion understanding.

---


### 186. [Aperture: Merge-Consistent Rotary States for Compressed Tokens](https://arxiv.org/abs/2609.36781)

**<font color=#1a73e8>作者：</font>** Yuhao Du, Shunian Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Token compression combines content from several positions, yet rotary position embeddings usually assign the merged token one coordinate. We ask what positional information must survive later merges. Aperture stores Fourier moments of the token's weighted support at the model's rotary frequencies. We prove that these moments have minimal real dimension among continuous states sufficient for the selected expected rotary interactions. Represented mass makes updates additive; attention normalisation remains a separate readout choice. Uniform intervals give a centre rotation times a sinc gain. We characterise when centres determine interval widths and construct matched examples where they do not. Numerical checks verify the weighted-support implementation. In trained temporal readers, compression transfer varies with gain calibration and feature placement. In a prespecified native video question-answering comparison, stored support reaches $65.63\%$ accuracy versus $67.12\%$ for the deployed merging rule. These results separate exact positional preservation under compression from downstream benefit.

---


### 187. [Regularized policy gradient with learned mixtures of Gaussians for games with continuous actions](https://arxiv.org/abs/2609.36787)

**<font color=#1a73e8>作者：</font>** Ondřej Kubíček, Viliam Lisý, Tuomas Sandholm  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Most successes of superhuman game-playing algorithms are in games with discrete actions, yet in auctions, robotics, sports, or trading, actions are nearly continuous. Prior techniques either rely on expert-designed discretizations or are sample inefficient. We present a scalable policy-gradient algorithm for large sequential games with continuous or mixed discrete and continuous actions. It combines magnetic mirror descent with a mixture of Gaussians reparametrization, trained via self-play. We show that it approximates equilibrium in games where gradient descent fails. In sequential games, it outperforms neural fictitious self-play and matches or outperforms the final strategies of policy space response oracles with 3.5--5.5$\times$ fewer samples. In heads-up no-limit Texas hold'em, it performs on par with Slumbot.

---


### 188. [Where Does Randomness Matter in Neural Cellular Automata?](https://arxiv.org/abs/2609.36797)

**<font color=#1a73e8>作者：</font>** Fei Zuo, Jiaqi Shi, Yujing Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic cell updates are often used throughout the life of a neural cellular automaton (NCA), from backpropagation through time to final rollout. This leaves two questions entangled: does update randomness help learn a useful rule, and must that randomness remain at execution? We separate training and evaluation update modes in controlled Growing NCA experiments, then vary the states shown during training. Under the standard constant-rate persist recipe, asynchronous training passes the short-horizon quality test in 10/10 runs, compared with 3/10 synchronous runs. All ten asynchronous models also retain the target for 4,096 steps under deterministic evaluation. For a scalar translation-invariant lattice, we derive an exact mean-square criterion: random masking can damp mean modes, but it also injects variance, and a mean-only test misclassifies four non-marginal settings. Finally, among 30 models that all pass the same reconstruction test, eight of ten grow-trained models become off-target at 4,096 steps, while all persist and regenerate models retain the target; damage recovery separates persist from regenerate. The results distinguish optimization reliability, execution mode, and task-specific behavior instead of treating them as one stability property.

---


### 189. [Scene Retargeting: Learning Object Placement with Analogical Transfer](https://arxiv.org/abs/2609.36801)

**<font color=#1a73e8>作者：</font>** Minkwan Kim, Junho Kim, Seungmin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive simulations of embodied AI or spatial computing applications build on realistic 3D scenes that support daily activities. However, sparse, irregular layout structures impose scene-specific physical constraints, making it hard to define a generalizable framework for generating similar functional context. We formalize Scene Retargeting as stably transferring the semantically coherent spatial organization across layouts, rather than relying on textual descriptions or pairwise relationships. Our cluster-wise transfer flexibly handles mismatched object instances and adapts to distinctive floor plans. We optimize to preserve the rich semantic context of individual clusters by respecting the spatial distribution of foundation features. We can then impose physical constraints to refine wall contacts, pairwise alignment, or clear passageways and openings. Our framework outperforms state-of-the-art methods on layout generation on the 3D-FRONT dataset, and demonstrates downstream applications including real-to-sim transfer, analogical trajectory transfer, and multi-reference composition.

---


### 190. [EGSD: Event-Grounded Self-Distillation for Streaming Video Understanding](https://arxiv.org/abs/2609.36803)

**<font color=#1a73e8>作者：</font>** Yuwei Miao, Xuesheng Zhang, Wenhao Zou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time video understanding requires incrementally maintaining a memory of streaming content, and optimizing this requires dense process signals. On-Policy Self-Distillation (OPSD), which lets one model serve as both teacher and student with the teacher receiving additional privileged information such as the question and ground-truth (GT) answer, can supply such token-level signals. However, applying it directly to streaming video raises two problems. (1) The student cannot be optimized end-to-end, where memory is written before the question arrives, yet the teacher scores it with the question-and-GT privilege, misaligning their preferences. (2) Effective-entity memory collapses, where the question-and-GT privilege makes the teacher favor only question-relevant entities, and token-mean averaging over a memory renders its signal invariant to how many entities that memory covers, both driving memory against the streaming need for diversity. To address these issues, we propose Event-Grounded Self-Distillation (EGSD), which characterizes streaming memory as an incremental update over verifiable Events (key visual entities, actions, and details) and targets the two problems on this basis. For problem (1), we adapt the OPSD signal into a multiplicative weight combined with the outcome reward; for problem (2), we re-weight the teacher with Events as privileged information to counter its question-relevance bias, and add an entity-coverage reward to supply the coverage preference the token-mean teacher lacks. Extensive experiments on mainstream online and offline benchmarks show EGSD achieves strong performance, reaching 79.8% on StreamingBench and 73.4% on the OVO-Bench Real-Time track, while memory analysis shows effective-entity recall rises 17.4% at only 6.8% more memory length.

---


### 191. [CAD-Native Transformer Operators for AI-Aided Engineering](https://arxiv.org/abs/2609.36806)

**<font color=#1a73e8>作者：</font>** Daniel Leibovici, Nikola Borislavov Kovachki, Dawon Ahn 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern engineering systems, from automobiles to aircraft, are designed by using precise, continuous parametric computer-aided design (CAD) models. Evaluating design changes through numerical simulation requires meshing the continuous geometry, a computationally expensive and often brittle process that can require manual intervention and replaces the continuous representation with a discrete approximation. Most neural surrogates accelerate the simulation, but inherit this representation gap by relying on meshes, point clouds, voxels, or other sampled approximations of geometry. We introduce CANTO, a transformer neural operator that maps directly from continuous CAD geometry to physical fields, without meshing the input geometry. We develop a theoretical framework for learning operators from geometric manifolds to function spaces of physical fields, representing geometry through sequences of parametric patches. CANTO instantiates this framework by directly tokenizing non-uniform rational B-spline (NURBS) patches from their control points, knot vectors, and weights, and predicts continuous surface and volume fields at arbitrary query locations. We evaluate CANTO on four automotive and aircraft aerodynamics industry benchmarks: AhmedML, WindsorML, DrivAerML, and HiLiftAeroML. CANTO achieves state-of-the-art accuracy on most evaluated surface and volume prediction tasks, including a 19.8% reduction in surface-pressure relative $L_2$ error compared with AB-UPT on HiLiftAeroML. Differentiability with respect to CAD parameters further enables gradient-based inverse design of designs. On AhmedML, CANTO identifies designs with 4.4 to 20.4% lower drag than the best dataset designs satisfying the same volume and lift constraints, with the improvements verified using the same CFD setup used to generate the original dataset.

---


### 192. [Geometry-Conditioned Fixed-Scaffold Encoders for Time-Warp Robust Sequence Retrieval](https://arxiv.org/abs/2609.36809)

**<font color=#1a73e8>作者：</font>** Cassandra Yang, Yufan Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embedding-based retrieval is attractive for long sequence collections because each item can be encoded once and searched by nearest-neighbor ranking. The difficulty is that the objects being indexed are often observed under a noncanonical clock: cardiac cycles stretch with rate, speech changes with tempo, and sensor traces reach comparable states at different speeds. This paper studies a specific source of instability in patch-based encoders for this regime. If patch boundaries are chosen from signal geometry, then the tokenization can change under the same temporal deformation that the representation is expected to tolerate. We propose GeoPatch, a fixed-scaffold patch encoder that keeps token support independent of geometry and uses slope, curvature, acceleration, affine-residual, and confidence descriptors only as continuous conditioning variables. The design turns boundary variation into feature modulation: geometry can change the embedding through a controlled pathway, but it cannot change the number, order, or support of local tokens. We formalize this distinction through a mechanism-level stability analysis that separates boundary drift, affine timing variation, confidence-weighted geometry perturbation, and retrieval-margin effects. The same local tokens support global embedding retrieval and late-interaction scoring, so the scoring rule can be matched to the evaluation protocol. Across ECG, speech, and multivariate time-series retrieval tasks, GeoPatch improves early-rank retrieval under timing variation while exposing a clear trade-off between local surface matching and strict non-overlap retrieval.

---


### 193. [MeteoVerse: Unified Weather-Controllable Video World Model](https://arxiv.org/abs/2609.36810)

**<font color=#1a73e8>作者：</font>** Renlong Wu, Guanqiao Wang, Xuan Shang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models aim to predict future content from an observed scene while following prescribed camera motion. Real-world scene evolution is determined not only by changes in viewpoint and object dynamics, but also by environmental conditions such as weather, which can substantially alter scene appearance and visibility. Modeling such realistic weather evolution is challenging because the required weather modification depends jointly on the observed and desired weather states. Depending on their relation, the model may need to preserve, introduce, or remove a weather effect. Existing video world models typically leave this weather transition implicit, forcing the generation backbone to infer weather evolution together with scene dynamics and camera motion, which leads to imprecise weather control. To address this limitation, we propose MeteoVerse, a unified weather-controllable video world model that generates future videos from a single sunny or adverse-weather image, conditioned on a weather-free scene description, a target-weather instruction, and a camera trajectory. Rather than conditioning only on the desired weather, MeteoVerse explicitly estimates the observed and target weather states and represents the required weather transition. A transition-aware mixture of weather experts then translates this transition into category-specific residual weather features, unifying weather preservation, introduction, and removal while enabling fine-grained control over introduced weather intensity. We further construct the MeteoVerse dataset with over 50K real-world weather video clips, generated sunny counterparts, disentangled scene and weather descriptions, weather-intensity annotations, and camera trajectories. Extensive experiments demonstrate substantially improved weather controllability while retaining competitive scene consistency and camera-control performance.

---


### 194. [Diffusion Policy Improvement with Proposal-Conditioned Refinement Flows](https://arxiv.org/abs/2609.36812)

**<font color=#1a73e8>作者：</font>** Junhyun Ha, Juho Lee, Byungwoo Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow policies can model complex behaviors in offline reinforcement learning (RL). However, penalizing their KL divergence from the behavior policy can discourage actions having high critic values with low behavior density. Directly refining behavior proposals may be an alternative, yet Gaussian or deterministic editors limit expressiveness to represent multiple separated modes for the same proposal. In this work, we introduce Proposal-Conditioned Refinement Flows (PReFlow), a policy extraction method combining critic-based proposal selection with a conditional refinement flow. To optimize proposal selection and refinement together, we formulate a KL-regularized objective whose optimum induces a Gibbs policy over final actions under a Gaussian-smoothed behavior prior. The refinement flow can represent multiple high value modes, while a proposal-centered Gaussian reference regulates large action changes. This Gaussian reference further enables us to make use of simulation-free, closed form adjoint matching targets from sampled endpoints and critic gradients, yielding a single velocity regression loss without a backward adjoint solve. On 50 OGBench tasks, PReFlow achieves competitive offline performance and the highest aggregate score among the compared methods after online fine-tuning, reaching 91\% after 500K environment steps.

---


### 195. [CurvSpec: Adaptive Multi-Curvature Learning for Partial Relevant Video Retrieval](https://arxiv.org/abs/2609.36815)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Letian Li, Jinpeng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partially Relevant Video Retrieval (PRVR) seeks to retrieve untrim-med videos containing a moment that matches a text query, without temporal annotations. The relevant moment may last only seconds within a video spanning several minutes, creating an extremely low signal-to-noise ratio that makes PRVR more challenging than standard full-video retrieval. This task presents two intertwined challenges: (1) signal dilution, where coarse global representations blur the brief relevant signal into the dominant irrelevant surroundings;(2) curvature rigidity, where embedding all videos in the same fixed-geometry space distorts representations for videos that range from flat atomic events to deep compositional hierarchies. Existing PRVR methods have improved moment selection and cross-modal matching, but they still typically encode all videos in a single fixed-curvature retrieval space, limiting their ability to model diverse video structures. To address both challenges, we propose CurvSpec, a framework that learns content-adaptive curvature for video retrieval representations rather than imposing a fixed geometric prior. CurvSpec processes features through parallel Euclidean and hyperbolic attention layers, with independently learned curvatures assigned to the hyperbolic layers, and a content-aware fusion mechanism routes each input to its most suitable geometric regime. To further suppress signal dilution, CurvSpec represents each video with semantic centroids whose number is determined by the video's content complexity, projects them onto the learned manifold, and matches each query against its nearest centroid by geodesic distance. Experiments on ActivityNet Captions, TVR, and Charades-STA demonstrate state-of-the-art retrieval performance.

---


### 196. [RED: Reconstruction Evolution Dynamics for Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2609.36822)

**<font color=#1a73e8>作者：</font>** Wenpeng Mu, Junshan Jin, Tanfeng Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of image generators calls for forensic cues that generalize beyond known generation mechanisms. Existing detectors often rely on static image representations or endpoint reconstruction discrepancies, leaving the evolution of intermediate reconstruction stages underexplored. We observe that the relative token predictability of real and generated images can reverse across reconstruction scales, suggesting that intermediate stages may expose forensic evidence overlooked by endpoint comparisons. Motivated by this observation, we propose RED (Reconstruction Evolution Dynamics), a framework that captures transferable forensic cues from coarse-to-fine reconstruction evolution. To our knowledge, RED is the first framework to use scale-wise token predictability to guide forensic evidence aggregation across intermediate reconstruction states. It represents the reconstruction trajectory produced by a frozen multiscale VQ-VAE in the shared feature space of a frozen CLIP encoder. To connect the observed predictability variations with visual evidence, RED learns image-adaptive stage weights from scale-wise token negative log-likelihoods provided by a frozen VAR model. A cross-stage evidence aggregation module then jointly models the original-image representation and the weighted reconstruction features, capturing complementary forensic cues through interactions along the reconstruction trajectory. Experiments on six diverse benchmarks demonstrate that RED achieves the highest average accuracy of 92.5\% and average precision of 97.5\% among the evaluated methods. Further evaluations show strong robustness to common image degradations, supporting the value of reconstruction evolution for generalizable AI-generated image detection. The code will be made publicly available upon acceptance of this paper.

---


### 197. [Motion Concept Unlearning in Video Diffusion Models](https://arxiv.org/abs/2609.36832)

**<font color=#1a73e8>作者：</font>** Ping Liu, Chi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) diffusion models can generate realistic depictions of actions such as kicking, stabbing, and shooting, raising safety concerns that motivate targeted concept erasure. Although concept erasure has been extensively studied for static concepts in text-to-image and T2V models, erasing motion concepts remains largely unexplored. We present a systematic study of motion concept erasure in video Diffusion Transformers (DiTs). Through causal interventions, we show that text-conditioning attention carries concept-specific motion information and supports selective intervention, whereas perturbing temporal positional encoding suppresses both target and non-target dynamics. We further find that directly adapting ESD, a representative weight-level image erasure method, to a video DiT yields modest and uneven motion suppression: reducing its erasure training loss does not by itself remove the concept signal from the difference between the conditional and unconditional predictions, which classifier-free guidance (CFG) then scales at every denoising step. From these findings, we derive three requirements for motion concept erasure: concept specificity, spatial selectivity, and temporal naturalness. Each determines one component of MUTE (Motion concept Unlearning in Text-to-video gEneration): at each denoising step, MUTE extracts a concept direction through token neutralization, derives a spatial gate from the direction's intrinsic structure, and subtracts the resulting correction from the velocity output before CFG is applied. MUTE is training-free and requires no weight modification. Experiments on 20 motion concepts show that MUTE outperforms representative prompt-level, weight-level, and inference-time baselines on Wan2.1-T2V, and the same formulation transfers to CogVideoX, supporting its applicability across distinct T2V attention architectures.

---


### 198. [You Cannot Recover What Was Never Measured: Quantifying the Information Ceiling of Ultra-Low-Field MRI Super-Resolution](https://arxiv.org/abs/2609.36837)

**<font color=#1a73e8>作者：</font>** Prathamesh Pradeep Khole, Shreya Handa, Utkarsh Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative super-resolution models can turn portable 64 mT MRI into images that look like 3T scans, and the field evaluates them with PSNR, SSIM, and pixelwise uncertainty, most often on pairs built by synthetically degrading high-field images. Prior work acknowledges that these models hallucinate and that the problem is ill posed, but to our knowledge no study measures how much information about the individual subject the real low-field scan actually contains. We measure it. Using paired 64 mT and 3T scans of the same subjects from three public datasets, and a measurement protocol validated on tests whose correct answer is known in advance, we find that, judged over the whole brain, real 64 mT scans carry structure specific to the individual only down to approximately 3 to 4 mm half-pitch in plane, and coarser still through plane. Standard synthetic degradations preserve subject information roughly 1 mm beyond this ceiling, so models trained and benchmarked on synthetic pairs are evaluated on information that real scanners never record. We then test trained diffusion models and a publicly released external model on real paired acquisitions; 24 trained runs of five architectures (GAN, diffusion, and transformer families) give the coverage of the audit. On every subject where faithfulness can be measured, fine output detail is no more correlated with the subject's own 3T scan than with a stranger's, while sample-variance uncertainty does not distinguish fabricated structure from reconstruction difficulty. Because PSNR and SSIM score resemblance to a reference rather than whether detail belongs to the subject, a benchmark scored by them cannot tell recovery from fabrication. Code for the measurement protocol will be released so that recoverability claims can be tested for newer models.

---


### 199. [Does the VGGT Family Need All Its Layers?](https://arxiv.org/abs/2609.36842)

**<font color=#1a73e8>作者：</font>** Fengyi Zhang, Holger Caesar, Xiangyu Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Which layers of a feed-forward geometry model are needed to preserve both camera poses and dense 3D structure? We study layer redundancy in VGGT, $\pi^3$, and VGGT-$\Omega$: 3,018 pruned configurations, scored on seven camera-pose and dense-geometry metrics across four indoor and outdoor datasets. Four findings follow: (i) Removable layers cluster in two redundancy regions: a dominant early region and a narrower late one, while deletions spanning the intervening layers are consistently more disruptive. This recurring pattern holds across models, datasets, and metrics, and contrasts with the middle-to-late redundancy commonly reported in the literature. (ii) Within these regions, we observe that the joint degradation from deleting two intervals is approximately the sum of their individual degradations, reducing the number of model evaluations for pruning search from $O(L^4)$ to $O(L^2)$, where $L$ is the aggregator depth. (iii) We find that CKA provides a cheaper representation-based proxy for interval degradation, offering a practical trade-off between pruning quality and calibration cost. (iv) Closed-form linear calibration recovers accuracy after pruning without end-to-end retraining. A least-squares analysis shows that using a shared map for special and patch tokens generally incurs excess reconstruction loss, motivating token-aware recovery. Recovery maps fitted on just 100 calibration scenes generalize to held-out scenes and unseen datasets. The resulting models reduce aggregator parameters by up to 44% while maintaining accuracy comparable to their intact counterparts. Code and experimental results will be available at our project page: this https URL

---


### 200. [RolloutFaith: Auditing Persistent Internal Interventions in Visual World Model](https://arxiv.org/abs/2609.36843)

**<font color=#1a73e8>作者：</font>** Junchi Yao, Ziyi Wang, Youling Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability methods such as probes, activation patches and learned editors are designed to reveal or modify a model's current computation. World models pose a harder requirement: because their predictions become inputs to later predictions, a useful internal correction must survive after editing stops. We therefore propose RolloutFaith, a framework that measures semantic improvement both in the prediction produced at intervention time and over later autonomous predictions under fixed events, actions, noise, and information budgets. We evaluate ten fitted editors on three world models across Crafter, Cartpole, and CoinRun. We also use Reference Activation Patching, which replaces a model activation with the paired activation computed from the real observation, to measure the correction available at the chosen interface. This reference intervention improves later predictions in all nine model and task combinations and outperforms the best fitted editor in eight, yet its sustained gain decreases with horizon in five of nine combinations. Current fitted editors recover only limited and inconsistent long term effects. By restoring individual state components to their untouched values, we find that persistent effects travel through the newest generated frame in DIAMOND, recurrent memory in DreamerV3, and both in STORM. These findings suggest that training should reward future consequences. To test this hypothesis, we propose Delayed LoReFT, which optimizes the same low rank intervention through four frozen future transitions and improves sustained intervention effects to some extent.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-447](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
