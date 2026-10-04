# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-385](./part-08.md)

---

### 301. [SoK: Decentralized Agent Economic Infrastructure](https://arxiv.org/abs/2610.01756)

**<font color=#1a73e8>作者：</font>** Rui Sun, Xihan Xiong, Qin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decentralized agent economies increasingly build a single task from protocols that were designed and secured separately. This creates a simple problem: a workflow can look correct at each step and still produce the wrong outcome. For example, a correct escrow may release payment on an authorized approval that provides little evidence that the delivered work actually satisfied the task.
We systematize this problem across the full lifecycle of an agent task. Our study organizes security and economic requirements into 17 property families over six stages, with receipt soundness and completeness assessed separately. We examine 12 systems and standards, five reusable mechanism families, and four classical baselines. We introduce guarantee closure, a task-relative criterion for determining whether guarantees established at one stage remain available and constrain the later decisions that depend on them.
We apply the criterion to controlled and native workflows, covering 840 matched executions and an exhaustive 11,648-case check over a finite objective-task domain. Our results expose recurring failures between verification and settlement, where conforming work can remain unaccepted or valid evidence can be ignored. Public records and model judgments further distinguish recorded approval from evidence of task conformance, while economic analysis identifies the report, penalty, and shared-error assumptions behind these guarantees. These findings show where end-to-end guarantees fail and what must be repaired to preserve them across the workflow.

---


### 302. [GenCOPE: Syn2Real Generalized Category-Level Object Pose Estimation for Robotic Picking](https://arxiv.org/abs/2610.01758)

**<font color=#1a73e8>作者：</font>** Jian Liu, Wei Sun, Zhenqi Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Category-level object pose estimation (COPE), capable of generalizing to intra-class unknown objects, has become a core technique for robotic 3D scene understanding. However, existing COPE methods still require labor-intensive recollection of real-world training data for novel object categories, which limits their scalability in practical applications. This paper aims to achieve synthetic-to-real (Syn2Real) generalized COPE, where a model is trained solely on rendered synthetic data and directly generalized to real-world deployments. The central challenge lies in the significant domain gap between synthetic and real-world data, particularly in texture appearance. To address this, we aim to enhance domain generalization by learning domain-invariant representations that capture semantic commonalities among objects within the same category. We introduce 2D and 3D semantic consistency constraints to reduce the sensitivity of feature encoders to domain-specific features. In addition, we propose an end-to-end pose regression framework that performs 2D-3D cross consistency learning, leveraging dense cross-modality fusion to further refine pose estimation. Since simplicity and effectiveness are essential for real-world robotic deployment, our model operates exclusively on global features, yielding a highly lightweight and efficient architecture. Extensive experiments on the REAL275 and Wild6D benchmarks, as well as real-world robotic manipulation scenes, show superior Syn2Real generalization performance of our paradigm. Code and demos are released at this https URL.

---


### 303. [PhysDEM: Physics-Defined Energy-Matching Diffusion for Spatiotemporal Field Generation under Scarce Measurements](https://arxiv.org/abs/2610.01759)

**<font color=#1a73e8>作者：</font>** Zhenyu Liang, Yining Huang, Yubo Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating and predicting spatiotemporal physical fields from scarce measurements is challenging, as observations are insufficient to characterize a distribution over complete fields. This limits conventional data-driven diffusion models that rely on full-field datasets. We introduce PhysDEM, a physics-defined diffusion framework that combines governing equations with spatially sparse observations to generate multiple plausible fields. First, we construct a Gibbs target by reweighting a measurement-conditioned Gaussian reference with PDE residual energy. Second, we derive an exact conditional-mean identity that reduces denoising to supervised learning of the standardized energy-induced mean correction. Third, a physics-displacement probability flow cancels Gaussian reference terms and enables amortized sampling with changing measurements through Gaussian conditioning, without retraining. Experiments on synthetic PDE systems and real-world-informed applications demonstrate that PhysDEM supports coherent field recovery and efficient sampling while maintaining stable diagnostics under tested noise levels, illustrating its practical value for field assessment. To our knowledge, PhysDEM is the first physics-defined diffusion model enabling amortized spatiotemporal field inference without preassembled full-field datasets.

---


### 304. [Physics-Refined Spatiotemporal Forecasting on Open-Boundary Hydrologic Graphs](https://arxiv.org/abs/2610.01765)

**<font color=#1a73e8>作者：</font>** Haoyang Jiang, Zhengui Wang, Shenghan Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal forecasting on hydrologic graphs is especially prone to instability in open-boundary systems, where the forecast domain exchanges fluxes with an unobserved exterior. In such systems, boundary nodes receive external forcing, e.g., upstream inflows in rivers or tidal signals in coastal regions, that is typically unavailable at prediction time. The absence of this information can compound errors as forecasts unfold in an autoregressive fashion, leading to inferior long-horizon performance. This paper dissects this instability issue by exploring two questions. 1) What boundary forcing enters the forecast domain when information beyond the boundary is missing? 2) How should this forcing propagate through the domain without incurring error amplification under autoregressive rollout?
To address both, we propose a new computing framework comprising two key components. First, to compensate for the boundary forcing, our framework learns ghost node proxies from the boundary and interior nodes, striving to approximate unobserved external inputs. Second, to control error accumulation from these learned proxies, we leverage two physics refiners. In particular, one refiner enforces local consistency by aligning ghost proxies with their two-hop neighbors (i.e., boundary nodes and their immediate interiors). The other refiner enhances global stability by correcting the model forecasts through a physics-guided graph neural operator, reducing long-horizon numerical drift. Two real-world hydrologic graphs are employed for empirical evaluation. Comparative results show that our proposal enjoys higher prediction accuracy and long-horizon stability over both learning-based and physics-informed model competitors.

---


### 305. [GIFTBench: Diagnosing Generalization in Image Forgery Localization and Informing Model Design](https://arxiv.org/abs/2610.01778)

**<font color=#1a73e8>作者：</font>** Baoke Dou, Ziye Wang, Hao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of image forgery localization (IFL) requires assessing models under diverse distribution changes, yet existing benchmarks often cover limited manipulation conditions or entangle multiple factors in cross-dataset evaluation. Consequently, aggregate performance provides an incomplete view of localization generalization. We introduce GIFTBench, a multi-axis benchmark of 115,013 manipulated images with pixel-level annotations spanning manipulation source, semantic target, editing operation, and composition complexity. GIFTBench supports axis-specific transfer analysis and evaluation on twelve external datasets. Its diagnostic studies reveal asymmetric cross-source transfer, recall-dominated failures, and heterogeneous degradation across semantic, operational, and compositional changes. Beyond diagnosis, the scale and diversity of GIFTBench provide a substantially broader training distribution than conventional IFL datasets. Training representative localizers on GIFTBench consistently improves their aggregate transfer to external datasets, showing that the benchmark serves not only as an evaluation tool but also as an effective training resource for cross-domain localization. Guided by the diagnostic findings, we further develop ForenScope, a detection and localization framework combining classification-adapted representations with multi-depth, multi-scale spatial features, learned layer fusion, and selective coarse-scale conditioning. Experiments show improved cross-dataset localization while retaining image-level detection capability. The GIFTBench dataset showcase page is available at this https URL.

---


### 306. [RealCompanion: Benchmarking Human Understanding from Reasoning over Longitudinal Real-World Conversations](https://arxiv.org/abs/2610.01780)

**<font color=#1a73e8>作者：</font>** Arman Behnam, Sunglyoung Kim, Liangwei Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A companion that talks with a person for months should come to understand them. It should remember what they said, infer who they are, and know when the past bears on the message in front of it. Testing this requires a real person's record, and such records are private, so benchmarks generate the person and the questions and settle in advance what matters. We release \bench, ten real relationships with an AI companion: 27,218 messages over up to 120 days, released as the conversation and four files derived from it, a profile, a persona, a chat ground truth and a question set, each citing the messages it rests on. Every chat label carries the reasoning trace that produced it, checked stage by stage against the conversation. Three findings follow. First, the past is rarely needed and far away. Pooled measures mislead: a recency window finds the required message for 95.9\% of probes and 2.2\% of those that need memory, and at the natural rate 96\% of the gain from supplying recorded evidence comes from messages that need none. Second, no detector we tried can tell when memory is needed on real messages, authored questions over the same histories leak the cue, and labeling the same messages as memories raises their use by ten to fourteen points. Third, three agent systems reconstruct the persona with the same F1 at a 31-fold difference in cost.

---


### 307. [Q-Learning for Reachability in MEC-Free MDPs](https://arxiv.org/abs/2610.01781)

**<font color=#1a73e8>作者：</font>** Lu-Chin Chang, Suguman Bansal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for reachability specifications is fundamental to sequential decision-making. Prior work establishes asymptotic convergence to optimal policies, but only through model-based methods that must explicitly estimate the transition probabilities of the underlying Markov Decision Process (MDP). We present Quasar, the first model-free algorithm with asymptotic guarantees for reachability on the fragment of MDPs free of non-terminal maximal end components (MECs), a building block to which every MDP reduces by the standard MEC quotient. Our algorithm follows the classical Q-learning approach, using temporal-difference updates to converge to an optimal policy without ever learning the transition probabilities. The resulting learner reduces the memory footprint from the O(|S|^2|A|) that model-based methods require to O(|S||A|). On the standardized Quantitative Verification Benchmark Set, our algorithm converges to the optimal policy with orders of magnitude fewer samples than the previous model-based state-of-the-art. Together these results are a concrete step toward the practical deployment of reachability learning and, with it, of specification-guided RL.

---


### 308. [Inferring Multi-Timescale Neural Dynamics with Switching Linear Dynamical Systems](https://arxiv.org/abs/2610.01786)

**<font color=#1a73e8>作者：</font>** Lulu Gong, Yongxu Zhang, Shreya Saxena  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural activity often exhibits multiple timescales that can vary with behavioral states and task conditions. Identifying these timescales from neural recordings is important for better understanding neural computation and function. However, traditional approaches based on autocorrelation fitting are difficult to scale to high-dimensional population recordings and can become unreliable when neural dynamics change with behavior. State-space models have been a powerful framework for modeling high-dimensional neural population activity through latent dynamical systems, but standard formulations and inference methods do not explicitly account for multiple timescales and therefore do not guarantee accurate recovery of the underlying temporal structure. Motivated by these questions, we introduce the Multi-Timescale Switching Linear Dynamical System (MTS-SLDS), a framework for identifying regime-specific latent timescales from continuous or spiking neural observations. MTS-SLDS combines a multi-lag moment initialization, which captures temporal structure across multiple observation lags, with \textit{regime-conditioned} Laplace-EM inference, which reduces mixing of dynamical statistics across uncertain regimes. Characteristic timescales can then be extracted directly from the eigenvalues of the learned latent transition matrices. In synthetic and neural experiments with Gaussian and Poisson spike observations, MTS-SLDS accurately recovers timescales and switching structure over multiple datasets.

---


### 309. [Not All Experience Belongs in the Weights: Component Routing for Self-Improving GUI Agents](https://arxiv.org/abs/2610.01787)

**<font color=#1a73e8>作者：</font>** Beining Wu, Zihao Ding, Jun Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving GUI agents keep the trajectories they produce and return them to the agent, by fine-tuning or by retrieval into the prompt, and studies that compare the two destinations disagree. We attribute this to the unit of experience: a trajectory bundles items with different properties, so a conclusion about the bundle depends on its mix. To address this, (i) we introduce component routing, which splits the experience into locators, procedures, state facts and lessons and sends each component to the context or to the weights, compared on the same items across three backbone families, two environments and three seeds. One pool has two destinations: locators and lessons win in the weights, procedures and state facts in the context. (ii) We fit a rule in two properties measured before any training, recurrence and state-conditionality; it recovers the destination of a held-out backbone family in 24 of 24 cells, two interventions move a component toward the boundary, and routing by the rule beats every whole-trajectory baseline and, by +3.5 points on average, the better single destination of each backbone. (iii) We identify how training and producer-consumer differences change the value of the two destinations: note readout decreases after the same component is written into the weights, most for the items that recur most, context gains increase with the information gap, and weights gains decrease with the policy gap. Code and data will be released.

---


### 310. [SAGE: Similarity-Based Cleaning of Poisoned Training Data from Verified Examples](https://arxiv.org/abs/2610.01788)

**<font color=#1a73e8>作者：</font>** Chaeeun Han, Soodeh Atefi, Yevgeniy Vorobeychik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As machine learning increasingly relies on public, untrusted data sources, data poisoning attacks, which inject malicious examples into training data to induce misclassification of a chosen target, pose a growing threat. Existing defenses either assume zero ground-truth information about which examples are poisoned, or they assume access to a large set of examples verified to be clean. Satisfying the latter assumption incurs significant cost since reliable verification can be very resource- or labor-intensive. This cost is particularly high for clean-label attacks, where poisoned examples are visually indistinguishable from clean data. Since requiring a large set of verified examples is impractical, we propose relying on a small set of verified examples including both clean and poisoned ones, i.e., each example verified either to be clean or poisoned through inspection by a forensic expert. The challenge is then to detect poisons based on a set of verified examples that is so small that most classification models would overfit. To address this challenge, we propose Similarity-based Approach for Ground-truth-driven Exclusion (SAGE), which trains a generic feature extractor on a separate dataset and then flags poisoned training examples using a non-parametric, similarity-weighted prediction based on the verified set. On standard benchmarks against seven clean-label attack methods, we demonstrate that having access to even a handful of verified poisoned examples provides a substantial advantage. We also find that the distribution of verified clean examples across classes matters more than the number of verified examples.

---


### 311. [iADD: Improving Alignment and Diversity in Diffusion Policy Optimization](https://arxiv.org/abs/2610.01789)

**<font color=#1a73e8>作者：</font>** Ashok Prasad Neupane, Saugat Adhikari, Pramish Paudel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning based post training of diffusion models, such as Denoising Diffusion Policy Optimization (DDPO), optimizes a reverse diffusion process under a reward function. However, current approaches to reward optimizations do so at the cost of diversity and quality. In this paper, we provide better tradeoffs through careful theoretical considerations and method design. We analyze the theoretical framework and mathematically demonstrate that \emph{only-latter timestep} updates of diffusion model may be harmful for diversity contrary to the conclusions presented in a previous work. Additionally, we propose an incremental Feynman-Kac training based on strong theoretical foundations in order to achieve the best-yet alignment-diversity tradeoffs. We perform extensive experiments and compare our method against related diffusion policy optimization approaches in three different tasks and also provide strong ablations for each component, thus validating strong performance gains in both alignment and diversity.

---


### 312. [A Safe Prototype Is Not a Safety Direction: Reference Dependence and Prompt Confounds in Response-Safety Embeddings](https://arxiv.org/abs/2610.01801)

**<font color=#1a73e8>作者：</font>** Sahil Kadadekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can response safety be scored by cosine similarity to the mean embedding of known-safe responses? A recent sleeper-agent detector proposes exactly this score, yet the raw positive-centroid rule is not identified: positive observations locate the safe class relative to an encoder origin, but do not determine which direction separates safe from unsafe responses. We audit the rule on two prompt-controlled, human-labeled corpora and one auxiliary jury-labeled source control, using four frozen encoders and prompt-grouped splits. On the human-labeled corpora the safe prototype reaches ROC-AUC 0.457-0.545, with two cells significantly below chance and one above, while an explicit safe-minus-unsafe reference reaches 0.588-0.738 on the same embeddings; on the jury control the prototype is inverted (0.358-0.405) and the reference reaches 0.754-0.793. At validation-calibrated 5% false-safe thresholds, the reference accepts more safe responses on PKU-SafeRLHF (0.153-0.263 versus 0.039-0.061 across encoders) and Aegis (0.189-0.291 versus 0.004-0.045), but not reliably on BeaverTails. A fully unlabeled held-out reference recovers part to most of the referenced ranking, much less when only 5% of the pool is unsafe, whereas 80-634 labeled unsafe responses recover most of it. Prompt-only ablations show that prompt-label composition can inflate uncontrolled evaluations. This is a bounded result about a raw positive centroid, not all one-class methods or safety-specialized guards. A class mean is a location, not necessarily a safety direction; a declared reference with enough unsafe mass identifies orientation.

---


### 313. [PhaseAT: Fourier Phase Adversarial Training for Medical Image Domain Generalization](https://arxiv.org/abs/2610.01807)

**<font color=#1a73e8>作者：</font>** Ahmed Sharshar, Asif Hanif, Naveen Kumar Kummari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable clinical deployment of deep medical image models is hindered by distribution shifts across scanners, sites, and acquisition protocols. Existing domain generalization (DG) methods often focus on style or intensity diversification, but they can still leave networks dependent on domain-specific texture correlations. Inspired by evidence that Fourier phase encodes semantic structure, we introduce PhaseAT, a phase-aware adversarial training framework for medical DG. PhaseAT forms phase-perturbed training views in the Fourier domain by iteratively updating a bounded phase perturbation while keeping the amplitude spectrum unchanged, thereby stressing spatial organization under matched appearance statistics. Perturbations are applied only to the luminance channel in YCbCr color space to avoid chromatic artifacts. Additionally, a simple phase-saliency mask concentrates updates on the most influential frequencies. The model is trained with a weighted combination of losses on clean and phase-perturbed samples, supporting both single-source and multi-source DG. We validate our method on two challenging medical datasets and demonstrate that PhaseAT achieves over 20% improvement in single-source domain generalization, outperforming several state-of-the-art DG methods. The code implementation is available at: this https URL.

---


### 314. [AI-assisted mitotic counting improves reproducibility and efficiency across multiple tumour types](https://arxiv.org/abs/2610.01813)

**<font color=#1a73e8>作者：</font>** Simon Graham, Mostafa Jahanifar, Quoc Dang Vu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mitotic counting is an important component of tumour grading, diagnosis and prognostic assessment across several tumour types, but manual assessment is time-consuming and subject to inter-pathologist variability. To help address these challenges, we developed MitPro, an AI tool designed to improve consistency and efficiency by directing pathologists towards regions with the highest predicted mitotic activity and highlighting mitotic figures for review, while retaining pathologist control over region selection and the final count. We evaluated its effect on the reproducibility and efficiency of mitotic counting in a retrospective, non-interventional, paired reader study comprising 385 whole-slide images from 3 centres in 3 countries and 7 tumour types using 3 different scanners. 13 pathologists participated, with each slide assessed independently by 3 pathologists without AI assistance and again with AI assistance after a minimum 2 week washout period. Across all slides, AI-assisted counting increased the intraclass correlation coefficient from 0.589 to 0.949. Mean pathologist-level median assessment time decreased from 286.4 to 127.8 seconds, corresponding to an average saving of 151.8 seconds per assessment. Improvements in agreement and efficiency were also observed in supporting analyses using HALO AP and Sectra image management systems and in 2 additional tumour types outside the main study population. AI-assisted assessment was associated with a subtle shift towards higher mitotic counts and scores, consistent with identification of more active mitotic hotspots and fewer missed mitotic figures. The frequency of score change between unassisted and AI-assisted assessment was comparable with inter-pathologist variation during routine counting. These findings support the use of MitPro as an assistive tool for more consistent and efficient mitotic assessment in routine practice.

---


### 315. [Debias Anything: Fairness with Diversity without Supervision in Diffusion Models](https://arxiv.org/abs/2610.01815)

**<font color=#1a73e8>作者：</font>** Théau d'Audiffret, Mariia Vladimirova, Jean-Yves Franceschi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although diffusion models produce high-quality images, they also reproduce and amplify demographic imbalances in their training data. Debiasing their generation process post-training w.r.t. some sensitive attribute usually relies on classifier guidance or explicit text extra-conditioning, but this reduces methods' applicability and output diversity. Conversely, methods promoting diversity alone do not ensure fair attribute representation. In this paper, we propose a method tackling fairness and diversity jointly that is generally applicable to any diffusion model and any sensitive attribute. To this end, an adapter connects the frozen diffusion model to a pretrained vision-language embedding space, enabling fairness and diversity guidance without sensitive-attribute annotations. For fairness, pairs of text prompts define attribute directions which guide batch composition towards specific proportions. For diversity, we introduce a score measuring disagreement between the semantic estimates derived from this representation. The formulation supports unconditional and text-conditional diffusion models, while requiring no prior knowledge or data of sensitive attribute. Experiments confirm that our method improves quality and diversity scores at comparable fairness levels.

---


### 316. [MECHVAR: Variance-Guided Mechanism Discrimination for Autonomous Machine Learning Experiment Selection](https://arxiv.org/abs/2610.01819)

**<font color=#1a73e8>作者：</font>** Yifan Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmark gains are often mechanism-ambiguous: reproducing an improvement does not by itself identify why it occurs. We study finite-library mechanism discrimination, where posterior-weighted candidate mechanisms, executable probes, and a limited experimental budget define a sequential experiment-selection problem. MECHVAR selects the next probe by maximizing the posterior-weighted variance of its predicted responses. Under a shared-Gaussian predictive model, this score is exactly proportional to the classical Box--Hill posterior-weighted pairwise-KL criterion, yet it admits O(KE) vectorized rescoring and a transparent additive audit over mechanism pairs. A local expansion further links the score to expected information gain (EIG) when predicted response separations are small. In a 25-block stress audit, MECHVAR outperforms confirmation-first in several moderate misspecification regimes, while its primary comparisons with EIG remain statistically unresolved. In a held-out Digits loop, normalized mechanism-identification AUC is 0.8975 for MECHVAR, 0.7825 for a score-greedy policy, and 0.9092 for EIG. At K = 100, E = 200, median single-thread full-library scoring is 10.36 microseconds for MECHVAR versus 57.69 ms for six-node quadrature EIG in the recorded environment. MECHVAR therefore provides a lightweight, auditable acquisition rule for finite-library experiment selection when a shared predictive scale is a defensible approximation.

---


### 317. [Code Owns the Simulation, Jev Owns the Evaluation](https://arxiv.org/abs/2610.01834)

**<font color=#1a73e8>作者：</font>** Yaodong Yang, Hongyao Tang, Yi Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Judgment models such as \jev{} return, in a single call and without reasoning text, a probability for each described option. This makes them attractive as an agent's action-selection layer, but it is unclear which decisions they can be trusted with. We test \jev{} on reflection tests, one-shot matrix games, the text game ALFWorld and robot control, and find a sharp boundary. \jev{} succeeds when the right option can be judged from what the input describes, which we call \emph{evaluation}. Specifically, it solves 99\% of the counterintuitive Cognitive Reflection Test questions. However, it fails when the right option depends on \emph{simulation} (i.e., predicting something not in the input), such as the opponent's action or the subgoal that must come first. In games, \jev{} plays suboptimally as if its rational opponent acted at random, because the opponent's action is not given. In ALFWorld, \jev{} favors commands that mention an object or place named in the task description. For example, given the task ``put a clean knife in the drawer'', \jev{} carries an unwashed knife straight to the drawer instead of first washing it at the sink. Surprisingly, many of these failures are not due to a lack of knowledge. Asked separately what the opponent will do, \jev{} usually answers correctly, and it responds well given the opponent's action. It fails when one call must both perform the simulation and evaluate based on it. This suggests letting code make the prediction or simulation. When code supplies it, such as a lookahead in ALFWorld and physics simulation in robot control, \jev{} becomes an expert controller through its general evaluation ability.

---


### 318. [On the Divergence of Accuracy and Mechanism Consistency in Time Series World Models](https://arxiv.org/abs/2610.01842)

**<font color=#1a73e8>作者：</font>** Haochen Zhang, Jiaheng Guo, Zhen Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A time series world model (TSWM) predicts a controlled system's state from its observed history and planned actions and exogenous inputs. Current approaches build forecasters with actions as covariates, trained and evaluated on prediction error under the executed plan. Yet world models compare unexecuted plans, but their responses to changed plans remain untested. We ask which design choices matter and whether accurate forecasters respond to changed plans as real systems do. We address both with a formalization and benchmark. The formalization separates state, actions and exogenous inputs, distinguishes continuous, mode and event actions, and introduces mechanism consistency, a metric built on declared action-state relations with known directions, such as a vasopressor raising blood pressure: it checks whether shifting an action moves the forecast in the declared direction. The benchmark consolidates eight public datasets with real actions from engineered infrastructure and clinical care, varying prediction space, plan fusion and plan encoding across seven backbones and five seeds. First, a frozen latent prediction space lowers MAE by 9.9% over observation space and gated output fusion lowers it by 12.7% over input concatenation on average, with both improving all eight datasets; temporal plan encoding changes average MAE by at most 2.2%. Second, prediction error and mechanism consistency diverge: the lowest-error configuration is at or below chance in consistency on four of five datasets with declared mechanisms, and no design choice avoids this. Finally, directional supervision, a loss penalizing the wrong-signed part of the response to a shifted action, significantly raises consistency on penalized mechanisms with no change in MAE. Together they give TSWMs a recipe: a frozen latent space and output-side fusion for accuracy, and a training objective for mechanism consistency.

---


### 319. [Temporal-Difference Learning for Dragonchess](https://arxiv.org/abs/2610.01845)

**<font color=#1a73e8>作者：</font>** Jim O'Connor, Annika Hoag, Sarah Goyette 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Our research investigates how two adaptive AI methods, evolutionary transfer learning and TD(lambda), perform in the three-dimensional chess environment Dragonchess. The game challenges players with its unique board structure and computational load, making it an ideal setting to study how adaptive methods can update evaluation heuristics in novel environments. In this work we re-implement the Dragonchess engine, changing it from a PyGame engine to C++. This enables faster gameplay, allowing us to run 10,000 games with confidence intervals and significance tests, rather than a single small tournament. Both adaptive methods outperform all other agents in the round-robin tournament. Our results showed that there is no significant difference in the performance between the evolved and learned evaluations. This research establishes the efficacy of adaptive methods in structurally complex, novel game domains.

---


### 320. [From Pixels to Policy: A Multi-Agent System for Intervention and Geo-Spatial Decision Support](https://arxiv.org/abs/2610.01870)

**<font color=#1a73e8>作者：</font>** Hosam Elgendy, Utkarsh Mall  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban environments are shaped by design choices with long-term implications for health, safety, and quality of life, yet evaluating proposed interventions remains costly, time-consuming, and often impractical. Existing geospatial vision methods largely focus on monitoring urban indicators from aerial and street-view imagery, rather than proposing interventions and estimating their effects on such indicators. Moving beyond recognition, we introduce the problem of discovering interventions that improve target indicators for a given aerial or street-view image. We argue that a black-box indicator model, combined with a generative editing model, can serve as an implicit digital twin for testing intervention hypotheses. We present VIDA-Geo , a multi-agent system that explores this intervention space by coordinating segmentation, diffusion-based inpainting, and indicator scoring models to produce interventions that are both perceptually realistic and aligned with real-world policies. We evaluate our system on 8 indicators across aerial and street-view imagery, measuring changes in factors such as perceived safety and greenery. Our approach outperforms existing baselines in many cases, achieving up to 2X higher perceptual quality and policy alignment scores. Finally, our model provides users with multiple candidate interventions, supporting an expert city-planner-in-the-loop workflow.

---


### 321. [EvenSplat: Coupled 2D-3D Decomposition for Gaussian Splatting under Exposure and Illumination Variation](https://arxiv.org/abs/2610.01876)

**<font color=#1a73e8>作者：</font>** Tongyu Wu, Jacob Edwards, Ziteng Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A surface photographed under even light presents nearly the same appearance from every angle; the same surface under uneven light does not. Exposure changes between views, illumination varies within a single image, and locally strong light sources leave one region bright and its neighbor in shadow. Multi-view reconstruction methods such as 3D Gaussian Splatting treat these lighting artifacts as if they were properties of the scene, entangling capture-specific illumination with the geometry and color they recover. We present EvenSplat, a framework that separates the two. EvenSplat couples an image-space illumination decomposition with an illumination field carried by the Gaussians, so that the same explanation of the lighting is shared between the two-dimensional and three-dimensional views of the scene; a camera-response network and a local exposure-compensation module absorb the global and residual differences that remain across training images. Through extensive experiments across multiple datasets and diverse forms of uneven illumination (cross-view exposure, spatial illumination variation, and high-contrast lighting) on both real-world captured and simulated benchmarks, EvenSplat generally outperforms state-of-the-art methods, particularly under high-contrast illumination.

---


### 322. [Flowing Faster to Coordinate: One-Step Online Multi-Agent Flow Policies](https://arxiv.org/abs/2610.01882)

**<font color=#1a73e8>作者：</font>** Zhuoran Li, Yunzhan Li, Xun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) provides a powerful framework for learning coordinated behaviors through interactions with the environment. Developing MARL policies requires balancing expressive modeling of complex and multimodal action distributions with efficient training and execution. Generative policies, particularly diffusionbased policies, can faithfully capture complex and multimodal behaviors, but costly iterative sampling hinders their scalability in online multi-agent settings. We propose an Online MARL framework via one-step Flow model (OMAF) that combines expressive generative policies with efficient one-step action generation. OMAF employs a Transformer-based flow policy to capture complex coordination behaviors, while its approximate path score surrogate provides a principled route to synchronized flow policy optimization. To enable stable and sampleefficient learning, we further develop a joint optimization scheme coupling softmax Q-value estimation with a joint flow policy objective for coordinated policy learning. By eliminating iterative sampling, OMAF dramatically reduces training overhead without sacrificing policy expressiveness. Extensive experiments across 10 standard tasks from MPE and MAMuJoCo show that OMAF consistently achieves superior performance, with up to 3.4x higher returns and 10.5x sample efficiency improvement compared with baseline methods. These results validate the effectiveness of OMAF as an expressive and computationally efficient one-step flow policy paradigm for online MARL.

---


### 323. [Memory-Guided B-Roll Generation from User Video Collections](https://arxiv.org/abs/2610.01884)

**<font color=#1a73e8>作者：</font>** Cusuh Ham, Fabian Caba Heilbron, Josef Sivic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce an approach for collection-grounded B-roll sequence generation. Given a user's video collection, a directive given in natural language, and a target duration, the goal is to produce a multi-shot sequence that complements the user's primary footage (A-roll) while preserving the collection's characters, settings, objects, and style. This task is challenging as one must choose the visual evidence from hours of captured footage that should guide the generation of each shot in the sequence. We address this challenge with MemComposer, a three-stage system that turns raw footage into a structured memory with visual references (characters, settings, objects, and style) and uses it to plan, retrieve, and generate grounded B-roll sequences. First, in a one-time offline stage, MemComposer constructs an entity-centric memory from raw video. Second, it uses the memory and user directive to plan a grounded sequence and retrieve conditioning frames for each shot. Third, it iteratively generates and critiques the sequence to enforce identity, setting, and sequence-level consistency. We evaluate MemComposer in a user preference study along two dimensions: prompt adherence and visual alignment to the user's collection. Against an ungrounded text-to-video planner, MemComposer wins 60.0\% of prompt-adherence and 92.8\% of visual-alignment comparisons, showing the grounding benefit of collection memory and reference retrieval. Against retrieval-only sequences assembled from captured footage, MemComposer wins 94.5\% of prompt-adherence comparisons, showing the value of generating missing shots, while retrieval-only sequences are preferred for visual alignment in 58.2\% of comparisons.

---


### 324. [Unsupervised Domain Adaptation for Enhanced Radiometer Image Precipitation Estimation using Conditional Flow Matching](https://arxiv.org/abs/2610.01890)

**<font color=#1a73e8>作者：</font>** Victor Enescu, Assaad Zeghina, Matthieu Meignin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep generative networks have recently achieved unprecedented performance in precise image and video editing using sophisticated textual prompts. However, the effectiveness of such models heavily depends on access to very large supervised and annotated image datasets, which can be very difficult to obtain. This is particularly true for satellite instruments, which very rarely overlap with labelled data, and suffer from domain shifts in the rare occasions they do. In this paper, we investigate the potential of flow matching models for unsupervised domain adaptation of satellite radiometer images. Our main contribution is a novel unsupervised method that achieves precise domain alignment by leveraging parts of the deterministic ordinary differential equations in flow matching models, conditioned on different satellite instruments. A key strength of our approach is its ability to preserve essential information while adapting across any domains since the perturbations are in theory bijective. Extensive experiments conducted on the GPM-Core constellation show the benefit of our conditional domain adaptation, particularly in improving rain precipitation estimation from radiometer imagery.

---


### 325. [A Structured State Space Sequence Model for Multi-Class Classification of Malware](https://arxiv.org/abs/2610.01893)

**<font color=#1a73e8>作者：</font>** Emmanuela Andam, Rana Shaaban, Emanuel Grant 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> By 2030, Internet of Things (IoT) devices are projected to reach 40 billion, with fast-paced technological advancements in fields such as industry, healthcare, agriculture, automobiles, and building/home automation systems. This expansion has created a large attack surface for cybercrime, as the majority of these devices open the door for cybercriminals to exploit vulnerabilities, as they lack adequate built-in security. Cybercriminals launch malware attacks to compromise systems or steal sensitive data, and once a system is compromised, a ransom is typically demanded for its release. Current cybersecurity measures in place are being outpaced by the rapid growth of the IoT, which is accompanied by a subsequent growth in malware variants being created per day. Recognizing this pitfall, this research examines and proposes a novel approach to malware detection and classification to safeguard devices from further attacks and make IoT systems more robust and secure. The framework proposed utilizes a Structured State Space Sequence (S4) model, which discretizes sequences of malware samples in a sequence and captures long-range dependencies, essentially identifying the "cause" and "effect" hidden within malware execution flow. This study presents two novel contributions: the first empirical application of the S4 model for malware analysis, and a comprehensive comparison of its performance against other deep learning architectures, laying the stepping stone for future research in this new paradigm.

---


### 326. [A foundation for systematic analysis of transformers and RNNs for tractography](https://arxiv.org/abs/2610.01894)

**<font color=#1a73e8>作者：</font>** Emmanuelle Renauld, Philippe Poulin, Hugo Larochelle 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) has emerged as a promising approach for improving diffusion MRI (dMRI) tractography, a task that remains limited by the intrinsic tension between local diffusion information and global anatomical plausibility. In this work, we systematically evaluate recurrent neural networks (RNNs) and Transformer models for iterative tractography, with particular attention to training strategies, input representations (including convolutional neural network (CNN)-based embeddings and end-of-sequence (EOS) tokens), and hyperparameter selection. We introduce a generation-validation phase enabling supervision at the streamline level during training, allowing supervision despite the mismatch between local loss functions and global streamline quality. Using the ISMRM2015 tractography challenge dataset, our models achieve the highest reported performance to date. Through controlled experiments, we quantify the impact of missing bundles, noisy or imperfect training streamlines, and invalid fibers in the training set. Finally, we demonstrate the applicability of our best-performing models for in vivo data from the Tractoinferno database. Overall, our results highlight both the potential and the limits of sequence-based deep learning models such as Transformers and RNNs for tractography, and emphasize the need for improved phantoms and evaluation methods for in vivo validation. We provide takeaways and recommendations for future researchers training and validating sequence-based supervised methods for tractography.

---


### 327. [Higher-Order Positional Encodings for Graph Representation Learning](https://arxiv.org/abs/2610.01903)

**<font color=#1a73e8>作者：</font>** Caleb Stam, Aagrim Hoysal, Sanjukta Krishnagopal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world systems exhibit higher-order interactions among groups of entities that cannot be captured by pairwise relationships alone. Graph Transformers and Graph Neural Networks increasingly rely on positional encodings to enrich graph representations, yet existing positional encodings are computed solely from the original graph and therefore cannot directly capture observed higher-order interactions. Topological Deep Learning addresses this limitation by lifting graphs to simplicial complexes, but typically requires performing message passing or attention on higher-order neural network representations. We introduce a representation learning paradigm that enriches graph representations with higher-order topology through positional encodings, enabling standard graph learning models to exploit lifted incidence structure without modifying the backbone. We derive a theoretical characterization of the expressivity of higher-order positional encodings, proving that node-level operators induced by higher-order lifts can mix graph Laplacian frequencies in ways that scalar graph spectral filters cannot. Guided by this theory, we instantiate higher-order positional encodings using Hodge Laplacians derived from clique complexes. Experiments with Graph Transformers on ZINC and controlled synthetic benchmarks demonstrate improvements in predictive performance, while a fixed-1-skeleton experiment shows that the pipeline can transmit higher-order information when cells are supplied independently of the graph. Together, our results establish higher-order positional encodings as a principled bridge between graph positional encodings and topological deep learning.

---


### 328. [MapLightning: Online Vectorized HD Map Construction with 1D Map Tokens](https://arxiv.org/abs/2610.01905)

**<font color=#1a73e8>作者：</font>** Shen Zheng, Anurag Ghosh, Mani Ramanagopal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online vectorized HD map construction is essential for scaling safe autonomous driving and requires accurate, real-time inference. Prior methods typically rely on dense bird's-eye-view (BEV) grids as the intermediate representation. We propose \textit{MapLightning}, which replaces the dense BEV grid with a compact set of 1D learnable map tokens. To construct map tokens from image features, we choose self-attention over vanilla cross-attention because it enables joint interactions and contextual aggregation among image and map tokens. Our transformer-based mapper concatenates map and image tokens, applies full self-attention, discards the image tokens, and retains the updated map tokens for decoding. This design offers three advantages. First, our representation is efficient, using fewer tokens, consuming less memory, and running faster. Second, the lightweight design allows the map decoder to use full rather than deformable cross-attention for better global context. Third, unlike BEV-based methods, our network does not use camera projection parameters, making it robust to camera-extrinsic perturbations. MapLightning uses up to 16.7$\times$ fewer intermediate tokens than dense BEV-based methods and achieves state-of-the-art accuracy and efficiency on nuScenes and Argoverse~2. Its lightweight variant surpasses MapTRv2 by +10.1 mAP on nuScenes and +16.2 mAP on Argoverse~2, while delivering 1.73$\times$ faster inference (40+ FPS) with 53\% less memory. We further show improvements on uncertainty-aware map construction and downstream trajectory prediction. Code and models will be released.

---


### 329. [Detection and Resolution of Periodic Artifacts in OpenDP's Discrete Laplace Sampler](https://arxiv.org/abs/2610.01907)

**<font color=#1a73e8>作者：</font>** Cesare Gerolimetto Fabrello, Valeria Rossi, Alberto Trombetta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential privacy implementations rely on precise sampling from noise distributions to provide formal privacy guarantees. We report the discovery of systematic artifacts in OpenDP's discrete Laplace sampler that manifest as periodic distortions in the output distribution. Through systematic testing, we trace these artifacts to a faulty implementation in the rational arithmetic library used by the bernoulli_exp1 function, a low-level primitive that implements sampling from Bernoulli(e^(-x)) distributions. We present a diagnostic methodology that isolates the faulty component in the nested sampling hierarchy and propose an alternative implementation based on exact rational arithmetic that eliminates the artifacts. Statistical validation with 10^6 samples confirms that the corrected sampler produces outputs indistinguishable from the theoretical distribution at the tested precision level.

---


### 330. [DecomVoxel: Harnessing 3D-Native Priors with Guided In-situ Denoising Optimization for Decompositional Scene Reconstruction](https://arxiv.org/abs/2610.01914)

**<font color=#1a73e8>作者：</font>** Junfeng Ni, Zirui Zhou, Yixin Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decompositional scene reconstruction aims to reconstruct high-quality objects and background, yet existing methods still struggle with the level of quality under heavy occlusions. While generative priors offer a potential solution, 2D image-based priors often suffer from multi-view inconsistency due to a lack of 3D awareness. Conversely, 3D-native priors provide stronger structural inductive biases but frequently lead to spatial drift and misalignment within complex scenes. To address these issues, we propose DecomVoxel, formulating object completion as a guided in-situ denoising optimization that bridges 3D-native priors with neural scene reconstruction. Our framework introduces a reformulated epsilon-based distillation loss to ensure stable latent refinement, alongside adaptive spatial guidance that utilizes occupied and vacant anchors with temporal annealing to suppress generative hallucinations and mitigate spatial drift. Experiments on Replica and ScanNet++ show that DecomVoxel significantly outperforms state-of-the-art methods while faithfully preserving the original spatial layout, structural fidelity, and style-consistent texture. Our method pushes the boundary of decompositional reconstruction by delivering high-quality textured meshes with clean topology, geometry, and appearance, providing a robust solution for the decompositional reconstruction of complex real-world scenes. Code is available at this https URL.

---


### 331. [CLoSeR: Closing the Loop for Long-Context Streaming Reconstruction](https://arxiv.org/abs/2610.01927)

**<font color=#1a73e8>作者：</font>** Moyang Li, Zihan Zhu, Wei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feedforward foundation models have recently shown remarkable 3D reconstruction capabilities. However, existing models exhibit large tracking drift in long-context streaming reconstruction due to error accumulation. In this paper, we revisit loop closure with streaming reconstruction foundation models to enable accurate, drift-free, kilometer-scale reconstruction. Specifically, our method detects loop candidates through global descriptor retrieval, and constructs loop-conditioned windows to estimate the relative poses between looped frames. Given the observation that our adopted streaming reconstruction backbone produces a globally consistent scale, we optimize all frame poses on the SE(3) manifold with sequential and loop closure constraints, avoiding the pose graph optimization on the Sim(3) or higher-dimensional SL(4) manifolds employed in prior works. Extensive experiments show that our method reduces drift and produces consistent geometry on kilometer-scale sequences, significantly outperforming the state of the art. Code is available at this https URL.

---


### 332. [Graph Representation via Elements of Discrete Morse and Cobordism Theories](https://arxiv.org/abs/2610.01937)

**<font color=#1a73e8>作者：</font>** Jennifer Rozenblit, Chenguang Yang, Yuxin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topology is, by its nature and design, suited to structure that is nonlinear, multiscale, and nonstationary - however, within machine learning, its use remains largely confined to topological data analysis. We advocate that tools from low-dimensional topology which have remained almost exclusively contained within the domain of pure mathematics (such as Morse theory) offer a strong, complementary, and yet virtually unexplored perspective on the hidden structure of data-generating processes and learning tasks built upon them. Here we introduce concepts from cobordism theory and harness tools from discrete Morse theory to improve the performance of graph diffusion models through our pipeline MG-Diff. Further, we derive theoretical guarantees and sufficient conditions so that under a positive decision-gap, the Morse-theoretic tools and their application for induced diffusion guidance are stable under small perturbations. Finally, we illustrate the utility of discrete Morse theory in application to graph diffusion models for spatio-temporal graph forecasting and graph regeneration, and argue that these applications are only a small window into the part of what low-dimensional topology can offer to the field of machine learning.

---


### 333. [Latent-Foresight: End-to-End Learning Predictable Representations for Latent World Models](https://arxiv.org/abs/2610.01942)

**<font color=#1a73e8>作者：</font>** Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting the future evolution of a scene is a fundamental capability for world modeling. Recent work has shown that operating in the feature space of Vision Foundation Models (VFMs) yields semantically rich representations that support diverse future scene understanding tasks. However, existing approaches rely on two-stage pipelines, where VFM features are first compressed using fixed dimensionality reduction (e.g., PCA) or independently trained autoencoders, and a separate predictor is trained on top of the resulting frozen latent space. This decoupling between representation learning and temporal prediction, as well as approaches that apply predictors directly on raw VFM features, provides no guarantee that the latent space is structured for predictable dynamics. In this work, we propose Latent-Foresight, an end-to-end framework that jointly learns a latent tokenizer and a flow-based generative dynamics model, explicitly shaping the representation to support temporal predictability. To enable stable joint optimization, we introduce several key design choices that prevent latent collapse and align reconstruction with generative objectives. Extensive experiments show that our approach learns more temporally coherent latent representations and consistently outperforms two-stage baselines across multiple future scene understanding tasks and prediction horizons, while eliminating separate training stages, including during high-resolution adaptation. We provide the implementation code and model weights at this https URL

---


### 334. [A Hybrid Approach to Malware Detection: Integrating Few-Shot Model-Agnostic Meta-Learning with Autoencoders](https://arxiv.org/abs/2610.01949)

**<font color=#1a73e8>作者：</font>** Emmanuela Andam, Yasir Abbas Zaidi, Abdelali Hadir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware has emerged as a major cybersecurity threat, with incidents increasing in frequency and impact across critical sectors. These attacks are typically launched through phishing emails, malicious downloads, or exploitation of software vulnerabilities to gain system access. Once inside, the malware encrypts files and demands a ransom, often in cryptocurrency, for the decryption key. Conventional detection methods often struggle with novel or scarce samples, leaving systems vulnerable. To address these challenges, this paper proposes a hybrid deep learning framework that combines an Autoencoder Feature Extractor (AFE) with a Model Agnostic Meta Learning (MAML) classifier for few shot malware detection. The AFE generates compact latent features that reduce noise and dimensionality, while the MAML classifier rapidly adapts to new threats using limited labeled data. Experiments conducted on the Ransomware Dataset 2024 demonstrate the effectiveness of the framework in binary classification tasks. Across one to fifty shot settings, the proposed model consistently achieves high accuracy, F1 score, and Matthews Correlation Coefficient values, maintaining reliable classification even under extreme scarcity. These results highlight the model's robustness and effectiveness in adapting to limited data scenarios, demonstrating the potential of combining feature extraction with meta learning to enhance resilience against malware, particularly in sectors such as healthcare, manufacturing, and public infrastructure, where cyberattacks can cause significant operational and financial disruption.

---


### 335. [Sharp Non-Asymptotic Analysis of the Penalized Challenger in $β$-EB-TCI for Bernoulli Bandits](https://arxiv.org/abs/2610.01951)

**<font color=#1a73e8>作者：</font>** Nam Nguyen, Tuan Quang Dam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Top-two algorithms are simple and effective for fixed-confidence best-arm identification, but their sharp non-asymptotic behavior is still not well understood. We study this problem for Bernoulli bandits through $\beta$-EB-TCI, the empirical-best top-two rule of Jourdan et al., whose challenger is chosen using a Bernoulli transportation cost with a logarithmic count penalty. We prove that, after the empirical leader has become the true best arm and its sampling fraction stays close to $\beta$, the stopping time is $T_{\beta}^{\star}(\mu)\log(1/\delta)$ up to lower-order concentration terms. We also show that, in this regime, every challenger is sampled linearly often. Thus, for the original algorithm without forced exploration, the main remaining difficulty is to control when the empirical leader becomes permanently correct. These results imply a non-asymptotic high-probability bound for all Bernoulli instances with a unique best arm. If the algorithm satisfies a finite-mean sufficient-exploration condition, the bound further yields the sharp expected sample complexity. In particular, this gives the sharp expectation result for the unguarded Bernoulli rule when all arm means are pairwise distinct, using the sufficient-exploration result of Jourdan et al. Finally, if we add a mild forced-exploration rule that contributes only $O(\sqrt{Kt})$ pulls up to time $t$, we obtain a self-contained expected sample-complexity theorem for any number of arms under the unique-best-arm assumption. We also identify a limitation of proof strategies that try to handle equal suboptimal means through a single index-comparison argument.

---


### 336. [EndoLive: Real-Time Style Transfer for Endoscopic Endonasal Skull Base Surgical Video](https://arxiv.org/abs/2610.01956)

**<font color=#1a73e8>作者：</font>** Griffin Hurt, Calvin Brinkman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex surgical procedures around critical anatomy, such as the endoscopic endonasal skull base surgery, requires significant practice and training on the part of the surgeon before they are allowed to perform the operation on a live patient. This training in typically done in cadaveric specimens, due to them containing the same critical structures as a living human. However, cadavers are not a perfect 1-to-1 substitute for a living patient. The dead and preserved tissues of a cadaver are colored completely differently than a living human, and -- without complex and expensive pumping systems -- do not bleed in the same way. As a result, identifying the critical pieces of anatomy that make this procedure so complex can be quite different in a live case than in a surgeon's cadaveric practice. This paper presents EndoLive, a framework for real-time style transfer between cadaveric endoscopic video and living human endoscopic video. Our method combines the ConStructS GAN model for realistic style transfer for surgical applications, with the HyPER-GAN model that can learn complex translations and perform them in real-time. We train EndoLive on unpaired cadaveric and live images taken from an endoscope, and test the trained model with cadaveric video, on a variety of devices. Experimental results demonstrate that EndoLive can perform cadaveric-to-live translation at speeds well above the minimum necessary for real-time, while maintaining semantic consistency of critical anatomical structures. Our source code is available at this https URL.

---


### 337. [System-Level Optimization Beyond Cryptographic Kernels: An ML-KEM Case Study on Arm Cortex-M7](https://arxiv.org/abs/2610.01960)

**<font color=#1a73e8>作者：</font>** Mahmoud Abdelhafeez Sayed, Mostafa Taha, Gurp Nijjer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work on embedded post-quantum cryptography has focused primarily on instruction-level optimization, including arithmetic-kernel improvements, assembly tuning, register allocation, and instruction scheduling. Using the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) on an Arm Cortex-M7 as a case study, we examine the additional gains available from memory-hierarchy utilization, tightly coupled memory placement, peripheral integration, clock configuration, and deterministic public-data reuse. The evaluation starts from a state-of-the-art SLOTHY-optimized implementation and covers all three ML-KEM parameter sets. Without modifying the cryptographic algorithm or standardized wire formats, the evaluated profiles without auxiliary public state reduce cycles by up to 2.5%. A selected public-data-reuse profile reduces encapsulation and decapsulation cycles by up to 74.6% and 58.8%, respectively. These results demonstrate that substantial deployment gains remain after arithmetic-kernel optimization and motivate a two-stage methodology that also examines the surrounding execution system.

---


### 338. [RASteer: Retain-Aware Activation Steering for Concept Erasure in Diffusion Models](https://arxiv.org/abs/2610.01969)

**<font color=#1a73e8>作者：</font>** Yongliang Wu, Haori Lu, Yulun Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to remove a target concept, such as a copyrighted style, a recognizable character, or unsafe content, from a pretrained text-to-image diffusion model while preserving its ability to generate other content. Existing activation steering methods build an erasure direction mainly from the target concept and adjust model activations along it at inference time. However, target and retained concepts often overlap in the model's representation space, so this direction also contains shared components that retained concepts rely on. Steering directly along this direction can therefore suppress retained concepts and harm the generation of non-target content. To address this issue, we propose Retain-aware Activation Steering (RASteer), a training-free method. RASteer first builds a retain subspace from the concepts to preserve. Retain-Orthogonal Steering (ROS) then removes components aligned with this subspace from the erasure direction, making steering more specific to the target. Since fully removing the shared components can weaken erasure, we further introduce Overlap-Adaptive Calibration (OAC). At each layer and denoising step, OAC uses the overlap between the erasure direction and the retain subspace to control how much of each shared component is removed, balancing target erasure and concept preservation. Experiments on unsafe-content, instance, and artistic-style erasure across multiple backbones and benchmarks show that RASteer matches or outperforms the activation steering and weight editing baselines we evaluate, achieving a better balance between erasure and preservation.

---


### 339. [Sim+Real: Joint Simulation - Experiment Training Improves Balanced Prediction in Physical Systems](https://arxiv.org/abs/2610.01974)

**<font color=#1a73e8>作者：</font>** Mahindra Rautela, Alexander Scheinker, Ayan Biswas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation and experimental measurements provide complementary data for learning spatiotemporal physical systems, but standard simulation-to-experiment fine-tuning optimizes only the experimental objective after transfer and can degrade simulation performance. We formulate simulation--experiment prediction as a multi-objective learning problem with domain-specific simulation and experimental risks. On four fluid systems from RealPDEBench and two model capacities, we compare Simulation only, Experiment only, Sim$\rightarrow$Exp, and Joint training, evaluating every final model on both held-out domains. Sim$\rightarrow$Exp tends to specialize more strongly to experimental data at the cost of simulation-domain forgetting. Joint training consistently achieves the best balanced performance over a broad range of simulation--experiment evaluation weightings, while substantially improving simulation retention over Sim$\rightarrow$Exp. Joint also better preserves simulation-only fields absent from experimental measurements. Project page: this https URL.

---


### 340. [The Curvature of Regret in Contextual Linear Optimization](https://arxiv.org/abs/2610.01980)

**<font color=#1a73e8>作者：</font>** Konstantinos Ziliaskopoulos, Alexander Vinel, Alice E. Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning for linear optimization is complicated by the discontinuity of the optimizer, where small cost errors may leave the decision unchanged or move it to a different vertex. We show that this non-smooth pointwise behavior becomes locally quadratic after averaging over the data distribution, and we derive the curvature in closed form, specifically, a matrix-valued measure supported on the walls of the normal fan. This measure depends only on the feasible set, with the data distribution entering only as a weight. We then offer a tractable approximation for this curvature, computable with just one projection to the feasible set. We prove that the approximation weakly converges to the true population curvature. We offer one application of our findings, a decision-aware scenario generation method for expected-cost linear optimization. Our experiments test the quadratic and weak convergence laws and show a 30.8% regret improvement over uniform allocation on battery arbitrage.

---


### 341. [Universal interpolation for deep residual self-attention networks](https://arxiv.org/abs/2610.01981)

**<font color=#1a73e8>作者：</font>** Sibylle Marcotte, Joan Bruna  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Universal approximation is a necessary qualitative property of learning architectures to benefit from scaling laws. While it is generically verified on a variety of neural architectures and random feature models, it typically involves infinite width limits. In this work, we focus on deep self-attention models and consider instead the `dual' regime, where approximation power is enabled entirely by depth, and featuring strong parameter sharing across layers, motivated by recent models such as the Looped Transformers. More specifically, we ask whether one can find a predefined finite set of parameters, each defining an attention block, such that the resulting finite set of transformations can map any collection of $N$ sequences of $n$ tokens to any other collection of $N$ sequences of $n$ tokens. Crucially, these transformations are \emph{fixed independently of the input and output} collections: only the order in which the blocks are applied, their signs, and their durations depend on the particular interpolation task. Our main result establishes it for residual softmax attention using only two frozen single-head blocks with Gaussian-initialized projection matrices. The result holds at both continuous and finite depth. We also characterize the restrictions imposed by causal masking and establish corresponding universal interpolation guarantees.

---


### 342. [Continual Concept Erasure in Diffusion Models by Suppressing Cross-Edit Interference](https://arxiv.org/abs/2610.01989)

**<font color=#1a73e8>作者：</font>** Yongliang Wu, Haori Lu, Jinqi Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure removes copyright-protected, privacy-sensitive, or otherwise undesirable concepts from pretrained text-to-image diffusion models to support content governance and compliance. As erasure requests arrive over time, models must remove new targets without undoing prior erasures. Existing methods do not constrain interference across edits: residual perturbations outside the retain set interact and accumulate, degrading unrelated generations and sometimes collapsing previously erased targets into noise. We propose CEASE (Continual Erasure via Adaptive Subspace Editing), a training-free method that imposes two subspace constraints on a closed-form solver. CEASE adds the token representation of the shared replacement to the solver's invariance matrix and, when interference is detected, projects the current update onto the orthogonal complement of dominant output directions extracted from cumulative past updates. A closed-form decomposition attributes the accumulated interference to repeated activation of the shared replacement and overlap between successive update directions, showing that the two constraints suppress these respective sources. Across continual erasure of celebrities, artistic styles, and instances, CEASE achieves the most consistent erase-preserve trade-off, while existing methods either degrade general generation or insufficiently erase targets.

---


### 343. [Comparing a gradient boosting algorithm to the GOES FDC for wildfire detection](https://arxiv.org/abs/2610.01994)

**<font color=#1a73e8>作者：</font>** Asaf Vanunu, Boaz Nadler, Arnon Karnieli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wildfires pose severe risks to human life, ecosystems, and property. This study presents a machine learning approach for wildfire detection from GOES ABI imagery. A CatBoost model was trained on a large dataset with thousands of ABI images and over 300,000 matching VIIRS fire detections. An evaluation on a separate dataset across five regions showed that the learned CatBoost model outperformed the operational GOES Fire Detection and Characterization (FDC) product. It achieved higher precision, recall, and F1 scores both within and outside the training area. The CatBoost model achieved F1 scores that were 0.16 to 0.38 higher than the GOES FDC in all regions. In addition, out of 51 historical fire events, the CatBoost detected 26 fires before both VIIRS and GOES FDC, compared to only six earlier detections by the GOES FDC. Importantly, the CatBoost model achieved accurate wildfire detection also during nighttime, whereas the GOES FDC obtained very low recall values, around 0.03. This study demonstrates that machine learning models may offer significant improvements over existing geostationary fire products, including higher accuracy, fewer false alarms, and earlier detection.

---


### 344. [Can AI Oversight Be Zero Knowledge?](https://arxiv.org/abs/2610.01995)

**<font color=#1a73e8>作者：</font>** Alessandro Chiesa, Ziyi Guan, Burcu Yildiz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly produce outputs from confidential data, such as a fitness-for-duty assessment from medical records or the predicted properties of a drug candidate from its secret structure. It is important to verify that such outputs are correct without revealing the underlying data. A recent line of work studies verification of AI outputs via interactive proofs and debate for oracle-aided computation, where correctness may depend on an oracle such as human judgment, a physical experiment, or the web. These works focus on verification by a verifier that runs much faster than the computation. However, such efficient verification is impossible for general oracle-aided computation, and these works therefore rely on additional assumptions. We focus instead on privacy: allowing the verifier to run in time polynomial in the computation, we ask whether interactive arguments for oracle-aided computation can be zero knowledge, so that the verifier learns nothing about the confidential data beyond the correctness of the output.
We prove that, in general, they cannot. In the random oracle model, there are no zero-knowledge proofs for all oracle-aided computations, even if both the prover and the verifier are allowed to run much longer than the computation itself. The impossibility extends to debate, a canonical model for scalable oversight.
On the positive side, we show that if the oracle attaches a cryptographic signature to each of its answers, then every oracle-aided computation can be verified in zero knowledge with an efficient prover and verifier, assuming only collision-resistant hash functions. Beyond privacy, this also gives an alternative approach to scalable oversight that relies neither on an honest opponent, as in debate, nor on the robustness of the computation, as in prior single-prover protocols.

---


### 345. [Weather-Aware Domain Adaptation for Street-View Weather Recognition](https://arxiv.org/abs/2610.02000)

**<font color=#1a73e8>作者：</font>** Hossein Maghsoumi, George Atia, Yaser P. Fallah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adverse conditions such as rain, snow, fog, and dust remain challenging for camera-based perception in autonomous driving. We study multi-class weather recognition from street-view images under domain shift, where most available training data come from non-street-view sources that differ markedly from real driving scenes. We propose Weather-Aware Adversarial Discriminative Domain Adaptation (WA-ADDA), which conditions the domain discriminator on predicted weather to promote features that are both domain-invariant and weather-sensitive. We also assemble a multi-dataset benchmark by unifying diverse non-street-view weather collections as sources and real street-view images as targets, and define a standardized evaluation protocol with macro accuracy as the primary metric. Across backbones (ResNet-50, EfficientNet, VGG, DenseNet), WA-ADDA consistently improves street-view performance and yields strong per-class recalls in challenging conditions while preserving clear-weather accuracy. These findings highlight the feasibility of domain-adapted weather recognition and the value of our benchmark for advancing robust, on-board perception.

---


### 346. [Exploring Weaknesses of Generative Image Watermarks against Latent Frequency Masking](https://arxiv.org/abs/2610.02010)

**<font color=#1a73e8>作者：</font>** Kirill Aistov, Khaled Abud, Irina Serzhenko 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Invisible watermarking has become a central tool for tracing AI-generated images, but its robustness against adaptive removal attacks remains an open security question. We introduce Latent Frequency Masking, an attack that erases watermark evidence by replacing selected Fourier coefficients in the latent representation of a watermarked image. The replacement can be sampled from Gaussian noise for efficiency or derived from diffusion regeneration for improved image preservation. We provide a theoretical distortion bound relating the change between the reconstructed adversarial image and the masked latent-frequency perturbation. We evaluate the proposed attack against six diffusion watermarking methods on images generated from DiffusionDB and MS-COCO prompts. Latent Frequency Masking removes or substantially weakens several watermarks while preserving perceptual quality and achieving favorable runtime compared with existing attacks. These results identify latent-frequency manipulation as a practical attack surface and highlight the need to include such attacks in robustness evaluations of generative image watermarking.

---


### 347. [XAI Evaluation Cards: A Practical Method for Designing Human-Centred XAI Evaluations](https://arxiv.org/abs/2610.02011)

**<font color=#1a73e8>作者：</font>** Kristýna Sirka Kacafírková, Ivania Donoso-Guzmán, Denis Parra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Evaluating explainable AI (XAI) systems from a human-centred approach requires researchers to select from numerous evaluation dimensions and measures, often in an ad hoc and fragmented manner. This paper introduces a method to help HCI, computer science, designers and social science researchers systematically evaluate XAI systems. The approach is based on an updated XAI-specific evaluation framework derived from an analysis of 82 studies. Using this framework, we developed a card-sorting method with 36 cards to help researchers prioritise relevant evaluation aspects. The process was tested with two research groups (n = 13) across five projects. The XAI Evaluation Cards are available as a printable appendix, along with an online repository of methods from previous XAI studies. Although not exhaustive, our findings indicate that the card-sorting approach can organise and streamline the design of the evaluation process, encouraging a more comprehensive and multidisciplinary assessment of XAI systems in research and development.

---


### 348. [Bellman Meets Lyapunov: Unsupervised Reinforcement Learning via Mastering Chaos](https://arxiv.org/abs/2610.02012)

**<font color=#1a73e8>作者：</font>** Tristan Shah, Wooyoung Chung, Volodomyr Makarenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is a powerful paradigm for training agents, yet its success rests on domain expertise of human engineers who design informative reward signals for every new task. Unsupervised RL aims to reduce this engineering with intrinsic motivation (IM): reward signals that emerge from the agent environment interaction itself. Existing IM objectives, however, involve the selection of information variables, which re-introduces domain expertise the field has sought to eliminate. We introduce Forward CIP (F-CIP), an RL-native formulation of the Controllable Information Production (CIP) objective, which is defined by the system's dynamics alone and requires no such selection. We prove that F-CIP is compatible with RL and demonstrate its effectiveness with existing algorithms. Training agents with F-CIP results in unsupervised discovery of primitive behaviors such as balancing and maintaining controllability, which are essential for more complex robot behaviors. Paired with a simple forward-velocity reward, our method produces coordinated gaits such as hopping and running which otherwise require reward engineering to learn.

---


### 349. [BranchIP: Learning Adaptive Equivariant Computation for Interatomic Potentials](https://arxiv.org/abs/2610.02013)

**<font color=#1a73e8>作者：</font>** Laura Zichi, Gil Harari, Chuin Wei Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant machine learning interatomic potentials (MLIPs) have revolutionized atomistic modeling, but accurate treatment of complex materials and molecular systems demands expensive models. This limits simulation length- and time-scales, with tensor products a key computational bottleneck. The recent emergence of foundation-scale MLIPs further exacerbates this challenge. We present Branch Interatomic Potential (BranchIP), a single-model framework for learned adaptive tensor product computation, trained with a novel distillation loss. In our experiments on two systems of physical interest, a heterogeneous catalysis system and a proton-conducting solid acid electrolyte, BranchIP accelerates MLIPs across model sizes by up to $2.4\times$ while reducing memory usage by up to $2.6\times$. This is achieved while maintaining physical fidelity. Furthermore, the learned adaptive computation provides model interpretability by revealing which interactions demand deeper computation and showing how computational depth relates to chemical complexity and dynamics.

---


### 350. [Atoms to Processes: The Role of Artificial Intelligence and Machine Learning in Chemical Engineering](https://arxiv.org/abs/2610.02014)

**<font color=#1a73e8>作者：</font>** Michael Baldea, Linda J. Broadbelt, Marianthi G. Ierapetritou 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid maturation of artificial intelligence (AI) and machine learning (ML) has catalyzed a profound shift in how chemical engineering problems are formulated, analyzed, and solved. Advances in computing, data availability, and learning algorithms have enabled AI/ML methods to impact applications spanning atomic-scale simulations, materials and catalyst discovery, transport and thermodynamics, separations, process systems engineering, and industrial operations. This article provides a perspective on recent methodological developments and representative applications, emphasizing how AI/ML tools are being integrated with first-principles models to address challenges of predictive accuracy, data scarcity, extrapolation, interpretability, and model lifecycle management. Across domains, a unifying trend is the move away from purely black-box approaches toward hybrid and physics-informed frameworks that explicitly respect conservation laws, thermodynamic consistency, and known structural constraints. These approaches not only improve robustness and reliability, but also enable meaningful human-AI collaboration by providing information at an appropriate level of abstraction for the task and decision context. We conclude that AI and ML are not replacing the core principles of chemical engineering; rather, they are amplifying them. As the field advances toward increasingly autonomous, adaptive, and sustainable systems, the thoughtful integration of AI/ML with first-principles understanding and domain expertise will be essential to realizing their full potential across both research and industrial practice.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-385](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
