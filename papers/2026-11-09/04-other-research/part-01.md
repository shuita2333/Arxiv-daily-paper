# 📦 其他研究 | 2026年11月09日

> 本类共 **237** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-237](./part-05.md)

---

### 1. [Formalizing inverse problems in the age of AI: possibilities, pitfalls, and an invitation](https://arxiv.org/abs/2611.06962)

**<font color=#1a73e8>作者：</font>** Christian Clason, Tapio Helin, Medet Nursultanov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proof assistants such as Lean check mathematical proofs down to the axioms, and AI agents have recently made writing such proofs cheap. We describe AutoIP, a Lean library in which classical linear regularization theory, together with the functional analysis it rests on, has been autoformalized by AI agents. A machine-checked proof certifies only the formal statement it proves, so the remaining human task is to confirm that each formal statement says what was intended. We organize the library around this task: a reviewer compares the formal statements with their natural-language counterparts and never needs to read a proof. Our experience is that the risks lie in the statements rather than in the proofs, and that simple automated tests on the statements can expose problems even in the established literature. We illustrate this with a textbook theorem whose hypothesis is more restrictive than asserted. We invite the inverse problems community to extend and build on the library.

---


### 2. [T$^2$-Splat: Adaptive Topology Mesh Splatting with Texture Residuals](https://arxiv.org/abs/2611.06974)

**<font color=#1a73e8>作者：</font>** Zhihao Tang, Youjia Zhang, Mingbo Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Triangle-based splatting connects novel view synthesis with conventional graphics pipelines, but often requires excessive tessellation to preserve appearance details. We present T$^2$-Splat, which decouples topology adaptation from appearance refinement. Safe Restricted Delaunay Triangulation (Safe RDT) initializes mesh connectivity. Dynamic Topology Evolution (DTE) then adapts triangle allocation through edge collapse and vertex split operations. Residual per-face Mip-textures then refine appearance on the fixed mesh using scale-adaptive filtering. Experiments on Mip-NeRF 360, Tanks & Temples, and DTU demonstrate competitive results with compact meshes. T$^2$-Splat improves PSNR by 0.71dB over MeshSplatting on Mip-NeRF 360. Additional compression experiments demonstrate flexible control of mesh complexity, supporting face budgets as low as 10% of the original face count. Project page: this https URL.

---


### 3. [Uncertainty calibration in Bayesian M/EEG source imaging](https://arxiv.org/abs/2611.06979)

**<font color=#1a73e8>作者：</font>** Ismail Huseynov, Mohammad Orabe, Srikantan Nagarajan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> M/EEG source imaging requires accurate localization and reliable uncertainty estimates, yet posterior credible regions are rarely assessed for empirical calibration. We present a simulation-based framework for uncertainty quantification and calibration of empirical Bayesian inverse methods with closed-form conditional Gaussian posterior summaries. We compare Bayesian minimum norm (BMN) with sLORETA depth weighting and sparse Bayesian learning (SBL) with sparse basis field expansions (S-FLEX). S-FLEX allows retained coefficients to contribute nonzero marginal posterior variance at locations where voxel-wise SBL yields degenerate variances. For BMN, we derive joint source- and noise-variance updates through evidence maximization. We test whether adaptive noise learning yields near-calibrated uncertainties. Both methods retain residual miscalibration, motivating post-hoc isotonic recalibration of credible-region levels using empirical coverage. Simulations assess fixed- and free-orientation models across signal-to-noise ratios (SNR), source sparsity levels, and subject-specific head models, using oracle, baseline-estimated, and adaptively learned noise. Before recalibration, SBL+S-FLEX yields lower Wasserstein localization error, smaller posterior uncertainty, and coverage closer to nominal credibility than BMN+sLORETA. Isotonic recalibration improves both methods, with larger gains for conservative BMN+sLORETA posteriors; transfer across mismatched SNR, sparsity, and head models remains condition dependent. Noise specifications yield broadly consistent reconstruction and uncertainty trends within each estimator. In real auditory MEG data, SBL+S-FLEX provides more focal localization and tighter uncertainties than BMN+sLORETA, suggesting greater statistical power for identifying bilateral auditory sources.

---


### 4. [Big Models, Small Gains: Frozen Forecasters as Classifiers on MONSTER](https://arxiv.org/abs/2611.06988)

**<font color=#1a73e8>作者：</font>** Rishit Jain, Rishit Kar, Chetashri Bhadane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting foundation models are increasingly used as frozen feature extractors for time series classification, but it remains unclear whether their pretrained representations offer an advantage over strong classifiers that do not require pretraining. This raises an important question: do these representations provide useful information beyond what the model architecture alone can capture, particularly when labelled data are scarce? We present a controlled benchmarking of two forecasting models, Reverso and Chronos-Bolt, on six large datasets from the MONSTER benchmark, using 1%, 10%, and 100% of the available training labels. We compare their frozen representations against four established time series classification methods and random-weight versions of the same forecasting models. Our results show that pretraining improves classification accuracy over random-weight counterparts on five of the six datasets, with gains of up to 23 percentage points. However, the frozen representations do not reliably outperform the strongest non-pretrained baseline in any setting: they perform worse in 15 of 17 settings and tie in the remaining two. Further experiments show that restoring amplitude information recovers part of the performance gap, while fine-tuning and forecast-error features do not close it. These findings highlight the importance of strong task specific baselines and random weight controls when evaluating forecasting foundation models for classification. Our code is available at this https URL.

---


### 5. [Robust Stream Classification using Time Neutralising Decision Trees](https://arxiv.org/abs/2611.06991)

**<font color=#1a73e8>作者：</font>** Brandon Gower-Winter, Georg Krempl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data Streams are characterised as a potentially infinite source of data subject to non-stationarity. This non-stationarity, also called Concept Drift, often results in deployed predictive models having to be perpetually retrained as the underlying data generating process of the stream changes over time. Drift Detectors are a class of methods used to identify these changes, triggering these retraining procedures. Historically, Stream Learning has operated under the assumption that instances are only seen once, and cannot be stored for later use. Contemporary work relaxes this assumption, yet drift detection and simple resetting procedures are still ubiquitous.
Building on related work which has shown that traditional Batch Learning algorithms often outperform Stream Learning algorithms when instances can be stored, we introduce Time Neutralising Trees (TNT), a Decision Tree architecture that enables robust stream classification in settings with Concept Drift. During training, TNT will filter out ("neutralise") old training samples that are no longer relevant given the current context of the stream. If those instances become relevant again, TNT will then re-include them. We evaluate TNT, and related algorithms on 24 real and semi-real classification data streams from the USP DS repository. Results show strong evidence that TNT achieves best-in-class performance on a wide-range of data streams with varying concept drift types.

---


### 6. [Autonomous AI Agents Systematically Diverge From Human Preferences in Proof Formalization](https://arxiv.org/abs/2611.06995)

**<font color=#1a73e8>作者：</font>** Bálint Gyevnár, Simon DeDeo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) systems have ushered in a new age of proof abundance, but helping humans understand these proofs requires new attention to the differences in how AI agents and humans pursue a proof-making task. We present "simulated collaboration", a methodology that allows us to examine two key questions: (1) the relative attention AI agents pay to surface syntax or, conversely, deeper underlying semantics, and (2) how and where AI agent preferences for what to do next diverge from human preferences. On a set of nine major human collaborations in Lean with 4.7M definitions across more than 6K commits, we find that, over the course of proof construction, AI agents (1) are far more strongly drawn than humans to explicitly marked gaps; (2) show a relative aversion to densely connected proof centers and to complex or surprising proof goals; and (3) are relatively attracted to surprising proof bodies, which they tend to regularize toward baseline. Our results highlight important blind spots and potential interventions for future human-AI collaboration in mathematics.

---


### 7. [Trust Responsive Runtime Authorization for Agentic AI with Empirical Characterization of Policy Behavior and Parameter Sensitivity](https://arxiv.org/abs/2611.06996)

**<font color=#1a73e8>作者：</font>** Ahsan Habib Shihab, Imre Felde, Ramis Akhmedov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The policy that converts runtime estimates of an autonomous agent's condition into operational authority is rarely specified or measured. We empirically characterize the Trust Responsive Authorization Policy (TRAP), which maps an Authorization Readiness Score (ARS), a weighted combination of runtime trust, operational stability, and contextual risk, onto discrete authorization levels through an asymmetric rule: escalation requires consecutive observations above a band edge plus a margin, while a sharp drop in readiness restricts authority at once. On one matched set of 100 Monte Carlo traces, we compare TRAP with static, trust-only, risk-only, and symmetric policies. Under abrupt degradation, TRAP restricts at onset and re-escalates sooner after recovery than the symmetric policy, with the highest and, descriptively, least variable stability among the adaptive policies, although more of its post-recovery escalations occur below the selected trust threshold. Paired bootstrap intervals exclude zero for the remaining differences. In one-factor sweeps, recovery time rises with the escalation margin and run length, shifts with the score weights, and is unchanged by the restriction threshold. In an exploratory post-freeze experiment, when the same degradation is spread over 5-20 intervals, TRAP restricts only on the 4 traces that retain a single-interval drop above that threshold; averaged over all 100 traces, it holds authority above what readiness supports for 15.9-18.9 of the 20 degradation intervals, against 0.8 under abrupt degradation and about 10 for the symmetric policy. Its restriction advantage therefore depends on degradation being abrupt. All reported values are traceable to the publicly available, versioned research release.

---


### 8. [TraCE: Trajectory-Aware Concepts for Explainable Video Understanding](https://arxiv.org/abs/2611.07009)

**<font color=#1a73e8>作者：</font>** Wooil Lee, Junpyo Hong, Jongseo Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding models often rely on motion, yet their explanations can obscure which motion sources support a prediction. We identify motion-source under-specification as a limitation of existing video XAI: region-centric explanations can be source-ambiguous, while motion vocabularies restricted to single-person pose sequences are source-incomplete. We propose TraCE (Trajectory-Aware Concepts for Explainable Video Understanding), a concept-based framework that discovers source-flexible motion concepts by clustering optical-flow trajectories from training videos. These concepts represent dynamic evidence from people, objects, and interactions, while object and scene concepts account for static context. The resulting typed trajectory/object/scene interface supports class prediction for action recognition and question-conditioned concept matching for video question answering (VQA). We evaluate TraCE across five random seeds on six benchmarks: NTU RGB+D Mutual, Chiral SSv2, UCF-101, KTH, TOMATO, and STAR. Relative to non-interpretable baselines, TraCE maintains competitive task performance, with an average accuracy drop of 1.0 points for action recognition and a nominal gain of 0.4 points for VQA. Motion perturbation and concept-removal tests provide complementary evidence of directional semantic alignment and decision faithfulness, while sample-level interventions illustrate targeted model debugging. Our project page is available at this https URL.

---


### 9. [Follow the Policy, Fail the Benchmark: Auditing and Revising Policy-Based Decision Benchmarks](https://arxiv.org/abs/2611.07042)

**<font color=#1a73e8>作者：</font>** Yanru Xiao, Yifei Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Policy-based decision benchmarks evaluate whether systems apply written rules to financial and operational cases. Yet a rule-following response can be marked wrong when the benchmark misstates the required decision. We audit nine public policy-based decision benchmarks through source tracing, program execution, and controlled checks. We find unsupported targets, reference errors that survive replay or propagate as solved steps, and evaluators that reject acceptable answers or credit incomplete decisions. To measure the scoring impact, we rescore unchanged model responses. On the 96 LegalBench SARA numeric cases, correcting the scorer raises acceptance by more than 80 percentage points for each of three models, without changing references or responses. In RuleArena Tax, restoring a required zero floor changes 27 of 300 references and narrows an observed model gap. A controlled federal-exemption task with explicit ownership and eligibility assumptions also shows that errors in supplied intermediate answers can affect final decisions. We present BAR (Benchmark Audit and Revision), a versioned collection of audit evidence and revisions for reevaluation.

---


### 10. [Adapting the Process of Adaptation: Darwinian, Lamarckian, and Agent-Directed Evolution in AI](https://arxiv.org/abs/2611.07048)

**<font color=#1a73e8>作者：</font>** Andrew W. Lo, Chaoyi Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evolution has shaped intelligence for billions of years. Artificial intelligence (AI) now raises a striking possibility: intelligence may begin to direct its own evolution. As AI agents become capable of modifying and evaluating their own behavior, how quickly could they improve, and how can that improvement remain safe? We develop a theoretical framework comparing Darwinian, Lamarckian, and agent-directed evolution following environmental change. Darwinian evolution relies on natural selection, Lamarckian evolution adds inherited learning, and agent-directed evolution allows agents to generate and evaluate behavioral variants and choose how extensively to search. When learning is sufficiently effective, these mechanisms exhibit progressively faster adaptation. Generating more variants accelerates adaptation, while optimal search effort depends on learning ability, problem difficulty, and experimentation costs. However, an agent's ability to direct its improvement does not ensure that improvements are evaluated against the intended objective. When the evaluation target is misspecified, additional search accelerates convergence toward the wrong behavior, even as measured performance improves. In recursive self-improvement, such errors may persist across generations, posing challenges for AI safety. Independent evaluation and oversight must keep pace with autonomous AI development. The central challenge is not simply to accelerate the evolution of intelligence, but to preserve humanity's ability to guide its direction, limit its speed, and intervene when necessary.

---


### 11. [Gaussians Can Subtract: Neural Dissolve Fields for Hybrid Scene Rendering](https://arxiv.org/abs/2611.07049)

**<font color=#1a73e8>作者：</font>** Yiyan Wang, Haohan Liu, Tetsuo Shibuya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hybrid Mesh-Gaussian rendering combines compact textured surfaces with flexible 3D Gaussian primitives, offering an efficient alternative to purely Gaussian scene representations for structured environments. Existing scene-reconstruction hybrids commonly follow an additive formulation, where Gaussian residuals compensate for errors left by the mesh. However, not every Mesh-Gaussian conflict is caused by missing content: residual geometry errors, occlusion mismatch, texture-projection artifacts, and view-dependent appearance can make the same mesh content consistent in one view but inconsistent in another. We therefore formulate hybrid rendering as a multi-view inconsistency problem and present Gaussolve, a subtract-and-refill framework that selectively dissolves inconsistent mesh content before residual Gaussians refill the revealed regions. We introduce a lightweight Neural Dissolve Field, parameterized by scalar spherical-harmonic Gaussians, to learn where and from which viewing directions mesh content should be dissolved. A continuous transmittance fusion rule progressively exposes residual Gaussians behind the dissolved mesh, preserving their reconstruction gradients and avoiding hard visibility discontinuities. Experiments on structured and semi-structured scenes demonstrate higher visual fidelity with fewer Gaussian primitives and faster rendering. Project page: this https URL

---


### 12. [Authorization Propagation in Agent2Agent Systems: An Experimental Security Evaluation of Multi-Hop Delegation](https://arxiv.org/abs/2611.07050)

**<font color=#1a73e8>作者：</font>** Gabriele Donno, Kashif Mehmood, Katina Kralevska  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Delegated Agent2Agent (A2A) workflows create a security problem when the agent sending a request is different from the principal from which the authority originated. This paper evaluates a layered downstream-verification design in a synthetic four-party healthcare reimbursement workflow. The prototype separates current-caller context, transitive authorization evidence, per-hop Ed25519 request authentication, and independent replay state for requests and authorization artifacts. Of 15 adversarial conditions, 14 are rejected; an isolated delegation-path test exposes the absence of semantic authority attenuation. A separate authorized-intermediary experiment shows that a holder of the shared authorization-evidence HMAC key can modify the represented authority and generate valid evidence. In the fixed-depth local benchmark, the full configuration has a median security-processing latency of 5.11 ms and a 3.87 kB serialized payload. The results show the value of separating request authentication from inherited authority while identifying origin-verifiable delegation and semantic attenuation as requirements for stronger A2A authorization propagation.

---


### 13. [Closed-Loop Agent Evaluation: Layered Measurement and Self-Calibration](https://arxiv.org/abs/2611.07051)

**<font color=#1a73e8>作者：</font>** Ruifeng Ren, Gun Ahn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Once an agent is live, teams want to know whether it is doing its job, not just whether it throws errors. Yet most evaluation is one-off: a benchmark run, a look at traces, a single score. Its conclusions neither check themselves nor reach the agent. We propose closed-loop evaluation, an evaluation method for deployed agents. It models evaluation as performance estimation under biased raters and censored outcomes, and it requires every level's conclusion to trace back to atomic data and to be computed by versioned rules. The method covers four levels of analysis (span, trace, conversation and engagement), measures along a spine of Execution, Substance, Trajectory and Results, treats Conduct as a constraint throughout, and uses Provenance and Adjudication components to certify the evidence and the evaluators. Evaluator agents generated by an Agent Factory carry these components, each with a domain knowledge pack and an adapter harness. Two loops close the evaluation: an inner loop audits the evidence, rules and metrics themselves, and an outer loop uses per-component regression checks to drive agent improvement. We also give a pipeline that runs this process automatically. Using the business-analysis agent SharpInsight as a case and porting the method to public conversation data, we show how problems differ across levels and how evidence-and-rule judgment is more reliable than holistic scoring (ICC 0.86 vs. 0.81; kappa 0.81 vs. 0.63).

---


### 14. [Expanding the Quality-Coverage Frontier with Competitive Flow Matching](https://arxiv.org/abs/2611.07055)

**<font color=#1a73e8>作者：</font>** Wenxuan Peng, Richard Zhang, Haitian Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching (FM) generators often face a quality-coverage tradeoff. Inference-time techniques such as classifier-free guidance raise quality, but at the cost of coverage. We hypothesize this limitation stems from a basic property of the objective: an intermediate noisy image could correspond to many clean images, yet the model can only predict a single velocity, at best averaging over the multiple possibilities. To mitigate this, we introduce competition among predictions during training. We achieve this by augmenting the predictor with a randomly drawn low-dimensional conditioning code $z$. For each training example, we sample $K$ values of $z$ to produce $K$ candidate velocities that compete to explain the target, and apply the loss only to the best-matching candidate. This winner-take-all objective allows different modes to shape different predictions, rather than being averaged into a single compromise. Furthermore, this term naturally enables a new form of guidance, auxiliary conditioning scaling, which complements traditional guidance methods. Together, these two guidance mechanisms show that our method substantially improves the quality-coverage frontier. We validate on ImageNet-256, using two different testbeds, SiT and RAEv2. Given less than 3% of the original SiT pretraining compute for post-training, at the 67% Recall point, our method reduces $\mathrm{FD}_{r,6}$ from 19.22 to 5.91. On RAEv2, at the 70% Recall point, it reduces $\mathrm{FD}_{r,6}$ from 16.83 to 3.18.

---


### 15. [Segment What It Can Draw: Querying a Text-to-Image Generator with Its Own Images for Skin Lesion Segmentation](https://arxiv.org/abs/2611.07061)

**<font color=#1a73e8>作者：</font>** Hongyu Cao, Guangfu Guo, Jinghan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin lesion segmentation without annotated masks requires the target to be specified through other cues. Existing approaches rely on dermoscopy-specific rules, annotation-derived model priors, or user-selected regions. A general text-to-image diffusion transformer offers a text interface to the target, but its concept-word attention is unreliable on dermoscopy images: in the model's attention-output space, the word-derived skin-to-lesion direction is poorly aligned with the direction separating real skin from real lesions. We show that the direction derived from generated healthy-skin and lesion images is substantially better aligned. Based on this finding, we propose GENIQ, a training-free method that constructs initial skin and lesion prototypes from generated images and refines them using the most skin-like and lesion-like patches from unlabelled dermoscopy images. It scores test patches along the refined direction and applies a gated threshold to suppress contextual spill-over around small lesions. Without inference-time annotations or additional models, GENIQ achieves Dice scores of 0.85-0.88 on three dermoscopy test sets. It outperforms zero-shot and word-based attention methods on all three sets, and a hand-designed dermoscopy pipeline in Dice and IoU on two.

---


### 16. [Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration](https://arxiv.org/abs/2611.07066)

**<font color=#1a73e8>作者：</font>** Sungil Son, Hoseong Jung, Dahyun Oh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovering cooperative behavior in multi-agent reinforcement learning (MARL) is challenging due to the combinatorial complexity of joint state-action spaces, which hinders the emergence of coordinated behaviors from trial-and-error alone. Intrinsic rewards are often used to aid discovery, but naively combining them with team objectives can distort the learning signal, compromising task performance. In this paper, we propose EFXPLORER, a constrained exploration framework that maximizes exploration objectives subject to a constraint that preserves established task performance. We solve the resulting problem using an epigraph reformulation that introduces adaptive exploration budgets. This approach separates intrinsic rewards from task objectives and regulates exploration through task feasibility. To further encourage diverse and temporally extended exploration, we incorporate a successor distance-based intrinsic reward that captures long-horizon dependencies. Empirically, our method outperforms strong baselines and induces novel cooperative strategies across SMAX, VMAS, and MPE benchmark suites.

---


### 17. [Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs](https://arxiv.org/abs/2611.07069)

**<font color=#1a73e8>作者：</font>** Jingjuan Huang, Zhiyao Zhang, Alvaro Velasquez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) in Partially Observable Markov Decision Processes (POMDPs) is computationally challenging due to the curse of long-range dependence on history. Fortunately, recent studies have shown that a range of POMDPs that satisfy the filter stability assumption can be well approximated by a superstate Markov Decision Process (MDP) based on a truncated history in a finite-memory window, with a value gap that decays with the window length. However, existing finite-time convergence analyses on such superstate MDP surrogates are either limited to over-simplified linear function approximation or rely on an i.i.d. sampling oracle that is violated by POMDP trajectories, both of which severely limit the applicability of these theoretical results in practice. This motivates us to bridge the gap by investigating RL in POMDPs with nonlinear neural value function approximation. Our main contributions are threefold: i) We first establish a new finite-state MDP point-wise approximation error bound, which lays the foundation for our RL algorithm design and analysis in POMDPs; ii) By applying Temporal-Difference (TD) learning to POMDP-generated superstate transitions and targeting the Bellman fixed point of the superstate MDP, we prove a finite-time critic error bound with nonlinear neural value function approximation; and iii) By combining the neural critic function approximation error bound with the policy mirror descent framework, we obtain a finite-time sublinear regret against the optimal POMDP value. To the best of our knowledge, such a finite-time sublinear regret based on neural function approximation is the first in the literature for finite-memory POMDPs. Our numerical experiments also verify our theoretical results.

---


### 18. [Automated Feedback to Peer Tutors Increases Their Talk Moves and Learner Reasoning but Not the Balance of Talk](https://arxiv.org/abs/2611.07072)

**<font color=#1a73e8>作者：</font>** Dorottya Demszky, Yann Hicke, Joy Yun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated feedback on classroom discourse improves instruction in professional and online teaching contexts, and recent work suggests that delivering similar feedback to learners may strengthen these effects by sharing responsibility for participation. Whether this holds in small-group volunteer tutoring has not been tested. We present results from a randomized controlled trial across two four-week SAT mathematics bootcamps on the this http URL platform, involving 1,030 volunteer tutors, 7,443 learners and 6,508 recorded sessions. Tutors were randomly assigned to receive no feedback, automated feedback on their own discourse, or that feedback together with participation feedback delivered to their learners under one of two motivational framings. Feedback to tutors increased eliciting of learner ideas, uptake of learner contributions, and learner reasoning by 8-15%, and the pattern replicated across both bootcamps. However, tutor talk time, which averaged 91.5% in the control group, did not change in any condition, and learner-facing feedback did not further change discourse. Interviews with 17 tutors indicate that they adopted the moves the feedback recommended but were limited by learners who did not respond. Interviews with 13 learners suggest why the learner-facing feedback had little effect: it reported a group-level rather than a learner-level statistic, some learners preferred to listen, and learner-to-learner interaction was rare in these sessions. Automated feedback can change how tutors invite learner thinking, but shifting how much learners talk likely requires changes beyond feedback.

---


### 19. [Optimistic Hedge in General-Sum Games: Fundamental Limits and Regret Bounds via Temporal Approximation](https://arxiv.org/abs/2611.07078)

**<font color=#1a73e8>作者：</font>** Yuval Dagan, Nadav Eisen, Liad Erez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimistic Hedge, a multiplicative weight update with one step of extrapolation, is one of the most natural regret-minimizing dynamics for games, and characterizing its regret has been a longstanding open question. Daskalakis, Fishelson and Golowich proved that if all $m$ players in a finite general-sum game follow Optimistic Hedge with a fixed learning rate, each player's regret is polylogarithmic in the horizon $T$. Subsequently, Ha showed that an appropriate choice of learning rate makes each player's regret bounded independently of $T$. This bound, however, is non-constructive and its dependence on the number of actions $n$ is not explicit, leaving open whether Optimistic Hedge can achieve a constant regret bound which is polynomial in the size of the game.
We show that the answer hinges on the number of players. In two-player games, there is a learning rate for which Optimistic Hedge guarantees $O(n\log n)$ regret independent of the horizon. In three-player games, however, no such bound is possible: for any learning rate up to an absolute constant and for sufficiently large horizon $T$, there is a game with $n$ actions per player in which some player's regret is $2^{\Omega(n)}$, and more generally, for every $m\ge3$ we construct $m$-player games in which some player's regret is $2^{\Omega(mn)}$; for learning rates above $2^{-\Omega(mn)}$, that player's regret even grows linearly in $T$.
Our upper bound is based on a temporal approximation framework for the analysis of Optimistic Hedge. Starting from the variance-based RVU bound of Daskalakis et al., we approximate the losses over time-localized windows by well-behaved functions, whose total variation is a small fraction of their cumulative variance. In $m$-player games, the same framework gives a significantly simplified proof of the recent $O(\sqrt{m}\log n\log T)$ regret bound due to Ha.

---


### 20. [Wide View Synthesis from Overlapping Perspective Cameras in Autonomous Driving](https://arxiv.org/abs/2611.07081)

**<font color=#1a73e8>作者：</font>** Kaixuan Zhang, Zhipeng Xiong, Minxian Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-perspective-camera systems are widely adopted since they provide broad visual coverage for autonomous driving, motivating the synthesis of a unified wide view from spatially separated observations. In this work, we formulate wide view synthesis (WVS), which aims to synthesize a geometrically consistent wide view at a specified virtual viewpoint from multiple perspective cameras. Unlike conventional image stitching, WVS requires reasoning about 3D geometry and visibility to handle depth-dependent parallax and occlusions arising from spatially separated camera centers. While vanilla 3D Gaussian Splatting (3DGS) enables high-fidelity view synthesis, its reliance on per-scene optimization limits its applicability to driving scenes. Furthermore, WVS introduces additional challenges, *e.g.*, peripheral stretching under perspective projection and photometric inconsistencies across cameras. To address these challenges, we propose **Wide-View Gaussian Splatting (WV-GS)**, a feed-forward Gaussian-splatting framework that synthesizes wide views without per-scene optimization. Specifically, we introduce Piecewise Perspective Rendering (PPR) to mitigate peripheral stretching through local perspective projections sharing a common camera center, and Spatial Affine Photometric Modeling (SAPM) to account for camera-dependent photometric variations during training. We further introduce **WideDrive**, a synthetic benchmark providing dense ground-truth wide views and adapt a LiDAR-projected sparse-reference protocol to real-world datasets. Extensive experiments on multiple datasets demonstrate the effectiveness of WV-GS for WVS. Dataset and code will be publicly released.

---


### 21. [Synthesizing symbolic models of human and machine reasoning at scale](https://arxiv.org/abs/2611.07088)

**<font color=#1a73e8>作者：</font>** Solim LeGris, Philipp Mondorf, Jinran Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Symbolic models offer a powerful account of cognition, but their scope has historically been limited by the need for hand-engineering and computational tractability. We show how advances in artificial intelligence (AI) can scale symbolic modeling and help overcome these engineering limitations. We introduce Behavior-Conditioned Symbolic Synthesis (BCSS)---an approach for automated search of interpretable, deterministic symbolic programs that verifiably reproduce behavior---and apply it to model both human and machine behavior across hundreds of challenging reasoning problems. Analyzing these programs reveals that both people and machines tend to oversimplify, adopt rules that are partial explanations for their observations, and misinfer dependencies between problem features. These shared signatures are modulated by available resources, with reasoning effort predicting the extent to which machines simplify and explain their observations. Together, these results point to underlying mechanisms reminiscent of satisficing in both people and machines, and illustrate how BCSS offers a general approach for interpreting and comparing rule-based reasoning of humans and black-box AI systems.

---


### 22. [Consistent yet Contextual: Learning Author-Level Mixtures of Style for Authorship Attribution](https://arxiv.org/abs/2611.07111)

**<font color=#1a73e8>作者：</font>** Omkar Yadav, Michael Jiang, Kenan Alkiek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Approaches to authorship verification or attribution typically model the style of a document, asking whether two documents were likely written by the same author. While recent approaches have been performant, such approaches largely ignore modeling the authors themselves and how varied their style is. Here, we introduce multiple alternatives for modeling the author and demonstrate that allowing an author's representation to capture multiple consistent but distinct writing styles yields significant performance improvements. Using our new authorship model, we then examine when an author writes in a way that is most idiomatic of their style across four scenarios: (i) variation in the size of their writing audiences, (ii) temporal distance from when the model was trained, (iii) the effect of preceding context, and (iv) the effect of genre norms on style. Across all four experiments, we demonstrate that authors vary substantially in how idiolectic their writing is. Our results have clear implications for both the modeling and data used for authorship verification and attribution, showing that authors need to be represented with their multiple styles and that some settings produce text that is much more informative about who wrote that text.

---


### 23. [What Patients Say They Can't Access: Mining Cancer Screening Barriers from Online Communities](https://arxiv.org/abs/2611.07113)

**<font color=#1a73e8>作者：</font>** Ruimin Sun, Aokun Chen, Arjun Arunasalam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cancer screening disparities persist across the U.S., yet the patient-reported barriers driving low uptake remain poorly characterized at scale. While clinical surveys capture structured responses, they miss the organic, unsolicited discourse where patients candidly describe real-world obstacles. In this paper, we conduct a large-scale analysis of over 56,000 posts across six cancer-specific Reddit communities to surface barriers to cancer screening among U.S. patients. We apply a pipeline combining keyword filtering, barrier triage, open coding, and codebook synthesis to systematically extract and categorize patient-reported barriers from 576 U.S.-located posts. Our qualitative analysis reveals recurring structural, informational, and psychosocial barriers that vary meaningfully by cancer type and community context. These findings lay the groundwork for future work aimed at proactively identifying and addressing barriers at scale - spanning a broader range of cancer types and populations - and informing the design of targeted interventions, navigator programs, and health system policies that translate patient-reported obstacles into actionable solutions.

---


### 24. [Regulating Autonomous Mobility-on-Demand Operators with Fixed and Adaptive Penalties: A Multi-Agent Reinforcement Learning Approach](https://arxiv.org/abs/2611.07122)

**<font color=#1a73e8>作者：</font>** Korbinian Kügler, Carolin Schmidt, Florian Dandl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Profit-maximizing Autonomous Mobility-on-Demand (AMoD) operators may exploit consumer surplus through excessive prices and underserve less profitable regions by relocating vehicles away from them. We study how penalty-based regulation of an AMoD operator in a multimodal mobility system can limit surge pricing and improve regional service availability. We model regulation as an outer control loop that acts on a learning-based operator. Static regulation with fixed penalties is formulated as a Markov Decision Process for an operator that jointly controls pricing and rebalancing, and dynamic regulation as a Partially Observable Stochastic Game in which a regulator periodically adjusts region-specific penalties in closed loop. Operator and regulator policies are learned with graph-based multi-agent reinforcement learning. In experiments with real-world Manhattan data, fixed surge pricing penalties reduce the share of travelers facing excessive prices from 22% to 1%. For regional service availability, dynamic regulation improves the regulator's reward by up to 15.6% over fixed penalties of equal mean intensity. The gains in service availability are strongest when spare fleet capacity exists, whereas service deficits persist in peak periods with highly utilized fleets. The learned regulator policy responds by reducing penalties where limited fleet capacity restricts compliance. The results identify trade-offs between regulatory targets, operator profitability, and traveler utility.

---


### 25. [Machine Learning for Live-Birth Prediction After IVF/ICSI From Structured Clinical Data: A Systematic Review, Meta-Analysis, and Critical Appraisal](https://arxiv.org/abs/2611.07124)

**<font color=#1a73e8>作者：</font>** Abdul Raheem Shahzad, Muhammad Zaheer Khan, Umar Ajaib 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning models predicting live birth after in vitro fertilisation (IVF) or intracytoplasmic sperm injection (ICSI) from routine clinical data report performance from near chance to near perfect. We systematically reviewed these models under PRISMA 2020, searching OpenAlex, Scopus and Web of Science to 22 October 2026, appraised them with PROBAST+AI and TRIPOD+AI, and pooled their discrimination with random-effects meta-analysis on the logit scale. We define what fixes the meaning of a model's output (decision point, endpoint, unit of analysis, data source) and map the 48 included studies by model family, decision point and validation design. Models evaluated only internally pooled to an area under the receiver operating characteristic curve (AUC) of 0.814, against 0.756 (95% prediction interval 0.546-0.889) for models evaluated on a later period or another centre, and 0.764 for studies not at high risk of bias; neither difference was significant, and heterogeneity was extreme. Models whose decision point was not stated pooled to 0.910, the only significant moderator in meta-regression. Against logistic regression fitted to the same data, the best machine-learning model gained a pooled 0.056 AUC (95% CI 0.017-0.090). Of 48 studies, 47 were at high or unclear risk of bias, only four assessed the calibration slope, and no model has evidence of clinical impact. The certainty of the pooled evidence is low to very low; the gains that survive validation came from staging predictions to decision points and local calibration, not deeper architectures. We provide a TRIPOD+AI-mapped checklist, a benchmark specification and a research agenda.

---


### 26. [Data-Driven Modeling of Molten Chloride Corrosion Using Static Test Data](https://arxiv.org/abs/2611.07125)

**<font color=#1a73e8>作者：</font>** Md Mahmudul Hasan Pathik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molten chloride corrosion has been studied for decades, yet reliable prediction across different alloys, salts, and test conditions remains difficult. In this work, 291 static molten chloride corrosion experiments reported in the literature were compiled into a structured dataset and used to develop an interpretable machine-learning framework for corrosion-rate predictions. To better represent the differences in salt condition across studies, a Chloride Salt Preparation Index (CSPI) was introduced to bring the reported salt-treatment method, atmosphere control, and pre-exposure impurity condition on a common numerical scale. A blended tree-based ensemble provided the most consistent predictive performance, achieving a cross-validated \(R^2\) of 0.85 and an MAE of 0.41 mg cm\(^{-2}\) day\(^{-1}\). The graded CSPI retained more useful information than a simple purified/unpurified classification and emerged as the dominant model descriptor. Global sensitivity and SHAP analyses further identified exposure time, temperature, and alloy chemistry as important contributors to the model predictions, with several observed trends consistent with the established molten-chloride corrosion behavior. The conformal prediction intervals were well calibrated, providing an estimate of prediction uncertainty in addition to the point prediction. Overall, the framework demonstrates that historical corrosion data can support quantitative, interpretable, and uncertainty-aware prediction when experimental context is represented explicitly, while also highlighting where more consistent reporting and targeted experiments are needed to improve future molten-salt corrosion models.

---


### 27. [Scalable Bayesian Gaussian Process Classification for Cancer Histopathology: Calibrated Uncertainty Under Distribution Shift](https://arxiv.org/abs/2611.07127)

**<font color=#1a73e8>作者：</font>** Yunru Zheng, Wun Ting Chan, Sampras Dsouza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty quantification is essential for clinical deployment of cancer diagnosis models, yet neural networks and variational Gaussian process methods can produce overconfident predictions, particularly under the distribution shifts that arise when models trained at one hospital are applied at another. We present a scalable Bayesian Gaussian Process Classification (GPC) framework that operates on frozen pathology foundation model embeddings (Phikon) and combines accelerated Randomly Pivoted Cholesky (RPCholesky) for low-rank kernel factorization, Hamiltonian Monte Carlo (HMC) with non-centered parameterization for posterior sampling, and a pivots-as-inducing-points scheme for prediction. This makes HMC posterior sampling in the low-rank latent representation tractable at N approximately 300,000 training points, enabling HC-based low-rank GPC on substantially larger datasets than prior MCMC-based demonstrations. We evaluate on two histopathology benchmarks for breast cancer metastasis detection: PCam and CAMELYON17-WILDS, where the latter tests calibration under hospital-level distribution shift. Compared to stochastic variational GP and neural network baselines, our method improves calibration and predictive performance - reducing expected calibration error by up to 88% and false negative rate by up to 90% - with the largest gains appearing under distribution shift, suggesting that HMC-based posterior sampling provides more trustworthy uncertainty estimates for cross-site pathology classification.

---


### 28. [Teaching Agents the "Principle", Not the "Reward"](https://arxiv.org/abs/2611.07130)

**<font color=#1a73e8>作者：</font>** Shan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has achieved strong performance in many tasks by letting agents learn from nothing more than a reward signal. However, in more complex tasks, agents still struggle to learn good, generalizable policies, even with carefully designed rewards and abundant samples. We argue that this difficulty stems from the reward decoding burden: designers encode their knowledge of the desired behavior into rewards and penalties, and agents must infer this knowledge from long sequences of noisy scalars. To address this burden, we propose prescriptive policy learning (PPL), which directly teaches agents higher-level knowledge about the tasks, termed principles of behavior, such as how to maintain balance, how to accumulate energy, and how to land smoothly. Through appropriately selected key quantities and references, PPL can directly indicate at every step whether the agent follows the principles and to what extent. Our experiments show that agents can learn good, generalizable policies without any reward. Taught only simple heuristic principles, PPL agents outperform reward-based methods with far fewer samples. Their policies also transfer directly to harder settings and keep performing well, demonstrating their strong generalization ability. In summary, PPL provides a new approach in which rough knowledge of the desired behavior is enough for agents to learn good, generalizable policies, even when the system dynamics cannot be accurately modeled.

---


### 29. [A Proxy-Based Method for Measuring Racial Disparities in~Text-to-Image~Generators](https://arxiv.org/abs/2611.07132)

**<font color=#1a73e8>作者：</font>** Nia Mucher, Ngan Pham, Jason Chin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an automated method for auditing text-to-image generators for representational bias against ground-truth demographic benchmarks. Our approach adapts the racial proxy variables used in U.S. antidiscrimination law to provide a fine-grained comparative analysis of variations in racial representation in generated images. We classify each generated image by race and then compare the model's distribution to publicly available demographic benchmark data to identify patterns of over- and under-representation. We also measure skin tone using CIELAB values and calculate cosine similarity amongst groups of images in order to capture biases that don't show up in demographic comparisons such as differences in image quality across races and skin tones. We report on experiments testing three models (Imagen 4 Fast, Stable Diffusion 3.5 Large Turbo, and Flux Schnell) using three categories of proxies (geographic, occupational, and surname) and 50 variants within each category. We find notable variation across the models as well as by proxy category. For example, Imagen 4 Fast overrepresents white classified images more than the other models tested and produces images with lighter, more homogeneous skin tones. Imagen 4 Fast also had the largest representational disparity for Black demographics among surname and geographical prompts. Stable Diffusion 3.5 Large Turbo produces results that overall diverge most from census data but yield the most diverse range of skin tones. Our method yields a generalizable and legally-grounded auditing tool that surfaces detailed information about model outputs without relying on implicit normative definitions of fairness.

---


### 30. [Perceptual Distortion for Overfitted Video Coding: Sliced Matching in Space, Error Alignment in Time](https://arxiv.org/abs/2611.07148)

**<font color=#1a73e8>作者：</font>** Tianyi Yang, Ge Gao, Fan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent works in neural video coding have increasingly been trading off perceptual quality against reconstruction fidelity at a fixed bitrate. Wasserstein Distortion (WD) offers a principled approach to balancing these objectives by relaxing spatial correspondences in feature matching, enabling lightweight overfitted image codecs to compete with computationally intensive generative decoders. Extending vanilla WD to video, however, presents two challenges: its independent Gaussian approximation limits the expressiveness of feature distribution matching, while unconstrained texture resampling across frames introduces temporal inconsistencies. We address these challenges by distinguishing between the correspondences that can be relaxed and those that must be preserved. Spatially, we introduce a local sliced Wasserstein distortion (SWD) that matches empirical feature distributions through one-dimensional optimal transport, capturing cross-channel dependencies without enforcing exact spatial alignment. Temporally, we employ a novel flow residual that constrains coding errors along motion trajectories, preserving temporal consistency without imposing additional reconstruction fidelity constraints. Evaluated on UVG and HEVC Class B with the overfitted codec COOL-CHIC, our framework achieves BD-rate reductions of 9.2% in DISTS and 3.0% in LPIPS relative to frame-wise WD, averaged over test sequences, while lowering tOF by 10.2% at matched rate.

---


### 31. [Beyond Proof of Possession: A Relational Theory of Authority](https://arxiv.org/abs/2611.07159)

**<font color=#1a73e8>作者：</font>** Nicola Gallo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proof-of-Possession (PoP) establishes that an executor controls an artifact (key, token, credential, or capability), but such control alone determines neither the executor's relational profile nor the causal history of an execution occurrence. We separate PoP from Proof of Relationship (PoR), the semantic property that one execution occurrence validly continues another, and from authorization, which is occurrence-sensitive. The foundational change is in the semantic domain of authorization: from holders and authority-bearing artifacts to execution occurrences situated in causal histories. We give authorization models an observation-based occurrence verdict and a separate transition-admissibility relation; kernel inclusion yields a partial order on observation-kernel classes. Building on Provenance Identity Continuity (PIC) and Proof-of-Continuity (PoC), we classify executors by authorization-relevant equivalence relations whose quotients form relational profile spaces, with positive predicates over profile transitions forming a distributive lattice. This adds relational attenuation to authority attenuation: along a valid causal history, $C_{i+1}\subseteq C_i$ and $\rho_{i+1}\Rightarrow\rho_i$. We prove dual monotonicity, combined closure, and origin relational closure. Two occurrences of the same authenticated executor, with the same profile and possession evidence, need not be authorization-equivalent, and within a valid PIC lineage a deputy's independent authority cannot be imported outside the origin context. Finally, we prove that the executor-dependent decision factors through the relational profile and is invariant under sound mechanisms establishing it: successor-side PoP is a possible evidence mechanism, not a necessary premise of authorization. Under explicit Witness Assumptions, a boundary-witnessed checkpoint construction realizes the premises without successor-side PoP.

---


### 32. [Full Provenance on the COSS Causal Axis: An Event-Level Closure of Causal Attribution and Confused-Deputy Exclusion](https://arxiv.org/abs/2611.07164)

**<font color=#1a73e8>作者：</font>** Nicola Gallo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance Identity Continuity (PIC) represents an authority-use event as an operation/resource behavior situated in a causal lineage, $(o,r,\ell)\in O\times R\times L$. We make the causal occurrence itself primitive: a represented security-relevant causal graph $(E,\to_c)$ in which each occurrence has a unique causal history, so the consistent event-lineage space is canonically isomorphic to $E$. The modeled execution has one causal partial order; distinct lineages are distinct causal histories inside it and may share a root while diverging into incomparable branches. PIC's $O\times R\times L$ is the authority-behavior projection of this space, and Causally Ordered Security-State (COSS) continuity generalizes it to an arbitrary behavior product over the same causal execution. On this semantics we prove an architecture-independent confused-deputy exclusion theorem. PIC continuation requires $C(e')\subseteq C(e)$ on every ordinary causal edge, so descendants are bounded by their ancestors; at an ordinary join, authority available on only one incoming branch cannot be resurrected, even when branches share a common root. Non-conservative combination must be an explicit authorized composition or relaxation event. With protected-effect mediation, an effect caused by request $q$ through an ordinary authority segment can exercise only authority in $C(q)$, so a confused-deputy state is contradictory. The result holds for any system whose protected request-to-effect causes are faithfully represented and whose ordinary authority transport satisfies PIC. We revisit Rajani, Garg, and Rezk: their value, control-flow, and initial-heap attacks are different witnesses of causal ancestry, so full provenance is an evidence mechanism for recovering edges of the causal graph, not the foundation of the PIC theorem. Finally we lift it to the COSS product of heterogeneous security-state coordinates.

---


### 33. [Structural Conditional Independence Test via Neural Quantile Resolution](https://arxiv.org/abs/2611.07165)

**<font color=#1a73e8>作者：</font>** Khoa Nguyen, Bao Duong, Thin Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional independence testing is difficult when dependence is weak, localized, or expressed through distributional changes rather than a global mean shift. Existing tests usually return a scalar statistic or p-value, which summarizes evidence against independence but does not describe where the conditional law changes. We propose QRCIT, a quantile-resolution conditional independence test that compares P(X|Z) and P(X|Y,Z) through a quantile deformation learned by a shared model. A lightweight residual quantile-flow model first learns the baseline conditional quantile law and then learns the additional deformation induced by Y, yielding a global predictive-gain statistic with conditional-randomization calibration and an inspectable deformation field over context and quantile level. We also introduce the Structural Dependency Benchmark (SDB), which evaluates dependence structures motivated by real applications, such as context-local, tail-only, sign-reversing, moving-ridge, and mean-neutral patterns. Across synthetic post-nonlinear (PNL) and SDB benchmarks, QRCIT improves detection of structured alternatives, with empirical Type-I behavior evaluated across settings. Higher quantile resolution improves merged-SDB power at moderate sample sizes, while diagnostics restricted to known affected regions improve detection of localized dependence. On Sachs, METABRIC breast cancer, and CCLE/PLX4720, QRCIT provides competitive real-data performance and interpretable deformation patterns. These results support quantile-resolved conditional-law deformation as a practical framework for testing and diagnosing structured conditional dependence.

---


### 34. [Meta-Frieren: Beyond Single Level Online Learning](https://arxiv.org/abs/2611.07169)

**<font color=#1a73e8>作者：</font>** Vahan Arsenyan, Arnak Dalalyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a two-stage online optimization problem: at each round, a meta-learner first selects an agent-environment pair, then the chosen agent interacts with the environment, and receives a reward. We introduce Meta-Frieren, a general framework for maximizing cumulative reward in this setting. Our analysis yields a simple UCB-style criterion for meta-level selection and recovers prior guarantees as special cases while extending them to broader settings. We instantiate Meta-Frieren with GP-UCB under Bayesian and frequentist assumptions. We also derive, to our knowledge, the first high-probability regret bound for Feel-Good Thompson Sampling, specialize it to finite and parametric function classes, and integrate it into Meta-Frieren. Experiments support our theoretical results and demonstrate that Meta-Frieren can be successfully applied to hyperparameter optimization across multiple model classes.

---


### 35. [Global Surveillance Under the Lens: Reconstructing Passive Dolev-Yao Intruders](https://arxiv.org/abs/2611.07170)

**<font color=#1a73e8>作者：</font>** Paolo Modesti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Global surveillance systems record large volumes of network traffic for retrospective analysis, but packet captures alone reveal little about protocol-level semantics. This paper presents an automated, specification-guided methodology for reconstructing passive Dolev-Yao intruder executions from captured network traffic and validating the reconstructed executions against a formal protocol specification. The framework takes a PCAP capture, an AnBx specification, and the associated deployment metadata; it extracts Java-serialised objects from TCP streams, reconstructs protocol sessions and channel-to-step assignments, and generates a passive intruder that evaluates the Dolev-Yao derived checks produced by the AnBx compiler. Three reconstruction challenges are addressed: multiple serialised objects and object references within a TCP stream, ambiguity in mapping interleaved connections to concurrent protocol sessions, and semantic validation of candidate reconstructions. We evaluate the methodology on 121 protocols from the AnBx test suite. For single-session captures, the standard JDK cryptographic provider recovers 97.8% of expected objects and achieves 94.2% successful reconstruction, where success requires complete object recovery and a clean passive-intruder execution. For the 112 parallel-capable protocols, the toolchain achieves 89.3% successful reconstruction for both two and three concurrent sessions, while recovering approximately 97.2% of expected objects. Experiments with mismatched protocol-role mappings and deliberately mutated traces show that the generated Dolev-Yao checks respond to semantic inconsistencies. By making the reconstruction step explicit, the solution produces protocol-level observations on which assessments of protocol resilience and the design of defensive countermeasures can be built.

---


### 36. [VINO: Revisiting 3D Representation Learning with Volume Transformers](https://arxiv.org/abs/2611.07176)

**<font color=#1a73e8>作者：</font>** Adrian Kruse, Kadir Yilmaz, Daan de Geus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning has given rise to vision foundation models that learn general-purpose image representations transferable across downstream tasks, yet representation learning for 3D scenes has not achieved comparable success. Motivated by this, we identify key limitations of current 3D representation learning approaches and revisit their core design choices. We first replace the commonly used hierarchical PTv3 backbone with the Volume Transformer, a ViT-like architecture for 3D scenes. We then redesign two core objectives of modern approaches built around student-teacher networks: matching representations across views and predicting masked content from visible context. For the first objective, we separate the roles of teacher and student: the teacher provides clean, consistent targets while the student learns invariance to stronger perturbations. For the second objective, we prevent the student from accessing the masked geometry and instead require it to infer missing representations from visible context only. Finally, we redesign 2D-to-3D knowledge distillation, replacing direct regression of view-dependent image features with view-consistent supervision. Together, these changes form VINO, a framework that learns semantic representations of 3D scenes without labels. VINO substantially improves dense linear probing across indoor and outdoor benchmarks and transfers strongly to out-of-domain settings.

---


### 37. [Backbone-Informed Adaptation after EEG Pretraining: A Capacity-Controlled Study](https://arxiv.org/abs/2611.07192)

**<font color=#1a73e8>作者：</font>** Mingyang Jiang, Yamin Li, Fan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models learn representations that combine information across channels and time. This structure motivates adapters that model the same relationships during downstream learning. However, it is not clear whether such a design outperforms other candidate adapters. Moreover, in order to arrive at a fair comparison between candidate adapters, we also need to consider their trainable parameters. Here, we ask whether a backbone-informed (native) adapter makes better use of a given capacity by comparing it against a token-wise multilayer perceptron control that transforms each feature vector independently. We approximately match their trainable parameter counts and keep the pretrained encoder fixed. Across two EEG foundation models and tasks covering emotion recognition, sleep staging, and EEG event classification, the native adapter shows no consistent advantage. For one backbone, differences between the designs are small relative to variation across runs. For the other, the token-wise control performs better on emotion recognition and EEG event classification. On sleep staging, the native adapter's advantage over the token-wise control is reduced when we also train the component that processes sequences of EEG segments. The relative performance of the two adapters depends on the backbone, task, and downstream training protocol. These findings motivate evaluating backbone-informed adapters against capacity-matched alternatives.

---


### 38. [τ-bench-LILT: Evaluating Conversational Agents on Realistic Multilingual Tool-Use Tasks](https://arxiv.org/abs/2611.07203)

**<font color=#1a73e8>作者：</font>** Kaden Uhlig, Kiarash Mokhtari, Anıl Arslan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier evaluations of tool-using conversational agents are conducted almost exclusively in English, leaving a critical gap for organizations deploying agents in other languages and regions. We present ${\tau}$-bench-LILT, a multilingual extension of ${\tau^3}$-bench covering German, Korean, Turkish, and Farsi in the airline, retail, telecom, and banking domains. We natively localize every layer of the benchmark: customer databases are populated with culturally appropriate records, user-simulator prompts are refined iteratively through contrastive annotation by native-language experts, and tasks are updated according to the localized database and to reflect realistic tasks in the target region. Evaluation across eight agent models shows the largest drops compared to English in the Korean and Farsi retail domains, by up to 61 points in pass^4. Code and data released at this https URL.

---


### 39. [TrustMix: Graceful Degradation for Pretrained Models under Distribution Shift](https://arxiv.org/abs/2611.07206)

**<font color=#1a73e8>作者：</font>** Juliusz Ziomek, Maike Osborne, Yee Whye Teh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting beyond the training domain necessarily requires assumptions about how the ground truth extrapolates, yet in most neural networks these assumptions are made only implicit through the architecture. We propose TrustMix, a lightweight post-hoc method that makes a pretrained model's extrapolative behaviour explicit and controllable. TrustMix combines the predictive distribution produced by a pretrained model with a user-specified fallback distribution $p_0(y|x)$, such that as the out-of-distribution (OOD) deviation statistic grows, we collapse towards $p_0(y|x)$. TrustMix provides graceful degradation: the predictive distribution converges toward the fallback distribution as the OOD signal grows. The fallback distribution $p_0(y|x)$ can reflect domain knowledge, if available, or rely on a domain-agnostic stationarity assumption. TrustMix does not require retraining of the base model and can be applied to both regression and classification problems. We evaluated TrustMix on several synthetic and real-world distribution shifts, including tabular, image, and natural language processing tasks. We tested TrustMix on datasets such as CIFAR-10/100 and ImageNet and on numerous architectures including Convolutional Neural Networks (CNNs) and Transformers. TrustMix remains competitive in-distribution while improving predictive uncertainty under distribution shift, with gains in predictive likelihood for regression and calibration for classification. Finally, we showed that TrustMix can provide useful predictive distributions for decision-making applications by utilizing it as a surrogate for Bayesian Optimisation.

---


### 40. [Structured Machine Theory of Mind from Agent Trajectories](https://arxiv.org/abs/2611.07208)

**<font color=#1a73e8>作者：</font>** Nigel F. Doering, Rahath Malladi, Arshia Sangwan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models of human behavior trained on large-scale trajectory data optimize for statistical accuracy without representing the mental states that causally generate behavior. Such models support prediction but not principled intervention: they cannot answer how an agent's behavior would change if its beliefs or preferences were different. We introduce Structured Machine Theory of Mind (SMToM), a framework that attributes explicit, independently supervised belief and desire representations from observed trajectories within a Belief-Desire-Intention (BDI) causal structure. The central architectural element is a goal head that consumes only the predicted mental-state channels and a current-trajectory embedding; counterfactual intervention on beliefs and desires is a direct operation. We instantiate SMToM on a controlled pedestrian navigation domain where ground-truth mental states are known by construction, enabling evaluation of attribution accuracy, local channel interventions, and trajectory-level counterfactual diagnostics. The resulting model, BDIBottleneck, improves over trajectory-only and unsupervised-context neural baselines. It is also competitive with a matched auxiliary-supervised context baseline while providing an editable mental-state interface that the unbottlenecked baseline lacks. Counterfactual experiments on desires confirm that substituting an agent's inferred preferences with a different activity type coherently shifts predicted destinations toward relevant locations. Counterfactual experiments on beliefs confirm that marking a location as unavailable in the agent's belief state reduces its predicted probability as a destination, though in a complex way. These results demonstrate, in a controlled navigation setting, that explicit BDI-structured supervision is a viable foundation for interpretable and counterfactual analysis of longitudinal trajectory data.

---


### 41. [Canonical Correlation Neural Networks](https://arxiv.org/abs/2611.07212)

**<font color=#1a73e8>作者：</font>** Andrea Cavallo, Sundeep Prabhakar Chepuri, Charilaos Kanatsoulis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational inductive biases such as grids or graphs allow neural networks with fewer trainable parameters and improved generalization, but require a known structure beforehand. When no structure is available, the covariance matrix provides a principled substitute, and coVariance Neural Networks (VNNs) have shown that using it yields models that are theoretically grounded in Principal Component Analysis, stable to finite-sample estimation errors and parameter-efficient. This framework, however, is limited to single-view data, whereas many applications observe the same phenomenon through multiple views, each with its own in-view covariance and a cross-view covariance linking them. To incorporate these matrices as inductive biases in a principled way, we introduce CAnonical correlation NEural networks (CANEs), architectures that use in-view and cross-view covariances as distinct relational biases to solve downstream tasks. Via spectral analysis, CANEs draw analogies with Canonical Correlation Analysis (CCA), a classical technique to project two-view data onto a correlated subspace. However, while CCA's objective is to compute shared view representations, CANEs are trained to solve a downstream task directly. We bound their output error under finite-sample covariance perturbations and show that it depends on controllable Lipschitz constants of the learned filters in place of the singular-value gap that governs the stability of CCA, thus guaranteeing better robustness. Experiments on seven datasets from brain imaging and motion sensing show that CANEs match or outperform single-view, two-view and CCA-based baselines, often with fewer parameters, and retain their performance when covariances are re-estimated from fewer samples.

---


### 42. [Fractional physics-informed neural networks to model social media virality](https://arxiv.org/abs/2611.07215)

**<font color=#1a73e8>作者：</font>** Alex Koong, George Em Karniadakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing models of social media virality either prescribe the functional form of engagement growth or assume a fixed mechanism by which past activity influences future engagement. We present a fractional physics-informed neural network that learns both the temporal memory and nonlinear growth dynamics of social media engagement, using symbolic regression to translate the learned dynamics into interpretable equations. Synthetic experiments at the deployment resolution of 24 hourly observations demonstrate that the fractional order and reaction law can be jointly recovered from clean data. Under observation noise, however, the standard pointwise physics residual drives the fractional order toward its lower bound through a scale artifact. We address this failure using a fully whitened residual that propagates observation noise through the fractional operator. Applying the framework to 348 posts from X (formerly Twitter), we find that a single-window model estimates strongly memory-dependent dynamics but fails to accurately reconstruct held-out trajectories. Partitioning the 24-hour window into four teacher-forced segments substantially improves performance, yielding segment-specific fractional orders that increase from 0.23 to 0.99 and interpretable growth laws for each phase. The segmented model reconstructs 64% of held-out trajectories within a mean squared error of 0.01, compared with 44% for the strongest of nine classical baselines. Together, these results demonstrate the potential of fractional physics-informed equation discovery to uncover interpretable engagement dynamics while highlighting the importance of noise-aware estimation and temporal segmentation.

---


### 43. [SAFE-Teen: Evaluating Chatbot Safety Across Adolescent Mental Health Conversations](https://arxiv.org/abs/2611.07218)

**<font color=#1a73e8>作者：</font>** Andrea Mock, Valerie Chen, Eric Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adolescents are increasingly turning to AI chatbots for mental health support, advice, and companionship, raising safety concerns. While recent evaluations have started to examine safety across multiple conversational turns, few compare how slight changes in a teen's responses can affect a chatbot's safety in the same scenario. We conduct a clinician-informed evaluation of chatbot safety in simulated conversations with adolescents aged 13-17, examining how safety failures vary with adolescents' responses and teen-aware system prompting. We evaluated 32,555 simulated conversations across 18 chatbot APIs and two system-prompt conditions using 22 safety criteria grounded in previously identified harms. Conversations spanned 983 variants of 106 seed scenarios covering urgent safety issues, health advice, and identity and relationships. The overall criterion failure rate was 43.3% without the teen-aware prompt and 24.9% with it. The teen-aware prompt reduced failures, but it didn't eliminate them. When a teenager pushed back on a chatbot's answer, failures on mental health diagnosis, medication, and substance misuse boundaries rose by 10-12 percentage points without the prompt, for more than 80% of chatbots. These findings reveal persistent safety failures in simulated adolescent-chatbot interactions and show that safety depends on how a conversation unfolds.

---


### 44. [Loopback Transformer: Towards a Unified View of Residual Looped Transformers](https://arxiv.org/abs/2611.07226)

**<font color=#1a73e8>作者：</font>** Xuan Ouyang, Zefan Cai, Chenlong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers reduce parameter count by repeatedly applying shared blocks, but parameter sharing alone does not determine how the results of repeated computation are reused. We take the depth-memory view of residual connections and analyze which representation is stored after each block application and how later reads weight it. A full block output contains both its input and its new update, so weighting that output also reweights the history already carried by the input. Reading individual updates instead, with the shared stack's input kept on a separate path, gives separate controls over input strength, total update weight, and allocation across updates. The Loopback Transformer implements these controls: geometric decay sets the total update weight and supplies a recency prior, and attention learns how to allocate that weight. On ClimbMix, Loopback reaches lower validation loss than standard Transformer baselines with 40-75% of their Transformer parameters (excluding token embeddings and the output head) at reference scales from 191M to 3B, with training tokens and executed depth matched. It also has higher mean accuracy over thirteen downstream tasks at 1.4B and 3B. At 191M, 374M, and 778M, it has the lowest validation loss and the highest thirteen-task mean among the standard Transformer and seven looped residual designs.

---


### 45. [MAC-v2: Long-horizon model-based value expansion from pixels](https://arxiv.org/abs/2611.07245)

**<font color=#1a73e8>作者：</font>** Kwanyoung Park, Sergey Levine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether \emph{long-horizon model-based value expansion} can serve as an effective framework in pixel-based offline reinforcement learning (RL). Long-horizon model-based value expansion from pixels is substantially harder than state-based environments, as the agent must learn both the representation and its dynamics, and errors from either can accumulate recursively over imagined trajectories. We introduce MAC-v2, which enables long-horizon model-based expansion from pixels by training a reconstruction-free latent world model with action chunking. By learning representations from prediction and control objectives, MAC-v2 does not need to encode control-irrelevant visual details that can hinder the dynamics prediction. Action chunking further mitigates the prediction error by reducing the number of recursive model predictions required for value expansion. Across diverse visual benchmarks including visual OGBench, MMBench2, Robomimic, and LIBERO-10, MAC-v2 achieves strong performance against model-free and model-based offline RL baselines. Our analyses show that long-horizon model-based value expansion is critical for the performance of MAC-v2, and that both action chunking and latent learning objectives are essential for reliable long-horizon latent imagination.

---


### 46. [KG-Neighbor: Knowledge-Guided Neighborhood Construction for Embedding Visualization](https://arxiv.org/abs/2611.07246)

**<font color=#1a73e8>作者：</font>** Chang Won Kim, Jaewook Lee, Haeun Min 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In embedding visualizations, nearby instances are interpreted as semantically related, although neighborhoods derived from input embeddings may not reflect content relationships. Neighborhood-based dimensionality reduction (DR) methods can propagate this limitation by optimizing layouts from embedding-based neighborhood graphs. We propose Knowledge-Guided Neighborhood Graph Construction (KGN), which represents relational knowledge derived from each instance as a set of knowledge graph (KG) triples. It uses the degree of triple sharing as pairwise semantic evidence to adjust embedding distances and reconstruct the top-k neighborhood graph; neither KG extraction nor neighborhood construction uses class labels. We also introduce IDProfile (IDP), which interprets residual mismatches by independently assessing whether the source content supports the assigned class label and the neighborhood-majority class. Across eight text and image dataset-encoder conditions, we characterize KGN over the full guidance-strength sweep and four KG similarity measures. Across this sweep, the maximum NMI and LT_2D each exceed the corresponding kNN baseline in all eight conditions, with the largest gains reaching 0.68 and 1.35, respectively. The gains and the extent of neighborhood reconfiguration vary across conditions and are larger under encoder conditions with lower kNN baseline scores. The IDP analysis shows that the largest reductions are concentrated in Placement Issue candidates, whereas Label Issue and Unresolved Case instances account for a larger share of the remaining review set. These results indicate that KGN can narrow the evaluated gap between embedding-based neighborhoods and content-supported semantic relations, while IDP shows that a residual mismatch should not automatically be interpreted as a projection failure.

---


### 47. [Goal Revelation as a Bridge Between Information-Theoretic Empowerment and Capability-Based Human Power](https://arxiv.org/abs/2611.07247)

**<font color=#1a73e8>作者：</font>** Jaime Ruiz-Serra, Tomáš Gavenčiak, Jobst Heitzig  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Power matters for AI safety. Optimal agents tend to acquire power across a wide range of objectives (instrumental convergence). As we embed AI agents into socio-technical systems, humans risk gradual disempowerment. Both concerns call for a formal, quantitative measure of power. Two such measures in the context of Markov games are information-theoretic empowerment, the capacity of the channel from an agent's actions to future states, and capability-based individual power, a measure of goal attainment built from the probabilities that a human would attain each goal in a family of candidates were they pursuing it. We show where the two meet. From individual power, Fano's inequality yields a floor $B(s)$. This floor is a lower bound on what we term goal revelation, the mutual information $\mathbb{I}(G;\xi \mid s)$ between the human's latent goal and the realised trajectory. Empowerment caps revelation from above, so that $B(s) \le \mathbb{I}(G;\xi \mid s) \le \mathbb{I}(\mathbf{A}_h \to \xi \mid s) \le \mathfrak{E}_h(s)$. Each quantity can be large while the one below it stays at zero, highlighting the following failure modes. An assistant maximising empowerment can prefer an interface offering broad influence over goal-irrelevant degrees of freedom to one that lets the human attain every goal they might hold. An assistant maximising revelation cannot tell a working interface from one rewired so that every goal yields the wrong outcome, since relabelling goals leaves mutual information unchanged while zeroing every attainment probability. Positive guarantees therefore come only from the attainment end of the chain. A satisfaction floor, computable from two statistics of interaction logs, offers a way to monitor the power users retain in a deployed system, and simulations in random environments show the three quantities are correlated but far from interchangeable.

---


### 48. [Using Transformers for Teaching and Learning via Symbolic Distillation of Neural A-life Agents](https://arxiv.org/abs/2611.07254)

**<font color=#1a73e8>作者：</font>** Shuwei Wang, Vadim Bulitko, Matthew R. G. Brown 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks controlling behavior of A-life agents can evolve over multiple generations. While effective in making the agents survive, such networks are generally opaque to a human observer. Furthermore, the neural weights cannot be transferred between agents with different neural architectures. Distilling such neural networks into compact symbolic policies can help humans understand agent behavior in A-life. Additionally, it allows the agents to share their knowledge in a compact fashion, improving population-level learning. Distilling a neural policy into a symbolic policy is typically performed by searching the space of symbolic policies to find one that approximates the neural policy. However, even with a domain-specific language the space of policies can be large, necessitating incomplete stochastic search such as genetic algorithms. Yet the distillation remains computationally expensive. We propose to instead use a transformer pre-trained on readily available random percept-action data. Doing so speeds up distillation substantially. We derive the transformer architecture via a neural architecture search. Empirical results compare different distillation methods and the influence of the symbolic space on A-life population dynamics through self-reflection and teaching and learning.

---


### 49. [Evolutionary Adaptive Neighborhood Learning: A Genetic Algorithm for Instance-Dependent k Optimization in Nearest Neighbor Classification](https://arxiv.org/abs/2611.07257)

**<font color=#1a73e8>作者：</font>** Isaac Touza, Kaladzavi Guidedi, Kolyang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The number of neighbours k is the central hyperparameter of the k-nearest neighbour (k-NN) classifier and is usually selected globally through cross-validation or evolutionary search. However, the bias-variance trade-off is inherently local: dense and noise-free regions may favour small neighbourhoods, whereas sparse or noisy regions may require larger ones. Since global-k optimization is one-dimensional, replacing exhaustive search with a genetic algorithm offers little computational advantage. We therefore optimize an instance-dependent neighbourhood policy instead. We propose EANK (Evolutionary Adaptive Neighborhood K), which uses a low-dimensional policy to map local neighbourhood descriptors, including density, label entropy, vote margin, and concentration, to an adaptive number of neighbours k(x). A real-coded elitist genetic algorithm optimizes this policy using leave-one-out accuracy with a neighbourhood-smoothness penalty. Precomputed neighbour votes reduce fitness evaluation costs. We investigate theoretical properties of the method, including dominance over global-k solutions on the training criterion, evolutionary convergence, policy regularity, and generalization guarantees. Experiments on synthetic data with spatially heterogeneous structure and twelve public datasets evaluate predictive performance, robustness, and computational cost. Under nested cross-validation, EANK achieves competitive performance relative to tuned global-k baselines and improves upon the default k=5. We also examine the gap between training and test performance to assess the practical value of adaptive neighbourhood selection.

---


### 50. [Reweighting is not Harmless: Understanding the Role of Dataset Characteristics](https://arxiv.org/abs/2611.07258)

**<font color=#1a73e8>作者：</font>** Amalia Ionescu, Jose G. Hernandez, Emily F. Wong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reweighting is a widely used pre-processing method for promoting discrimination-free model behavior by assigning different weights to data points during model training. While it is often credited with improving fairness, particularly by mitigating systematic underestimation for underrepresented groups, it can also introduce unintended harms under certain data conditions. Using controlled simulations that vary group size and baseline event prevalence, we show how reweighting can yield misleading improvements in fairness by reducing underestimation for one group while introducing it for another. Across 3,000 simulated datasets with event prevalence of 7-14%, reweighting improved parity in positive classification and false negative rates (FNR) between groups, but did so partly by decreasing positive classifications and increasing FNR for the group with higher baseline prevalence. These effects were most pronounced when that group was a minority: its FNR rose by 6 percentage points, approximately 82 additional missed cases per 10,000 group members, and roughly three-quarters of the improvement in FNR parity came from this increase rather than from gains for the other group. The pattern held across six classifiers, from logistic regression to neural networks, while overall accuracy was essentially unchanged, leaving the shift invisible in aggregate performance metrics. These findings mirror patterns reported in real-world applications and underscore the critical role of data characteristics in shaping the impact of this fairness intervention. While reweighting may create desirable outcomes in some applications, practitioners should critically evaluate it relative to their problem area and goals. Specifically, when the goal is to reduce underestimation in one group without introducing underestimation in another, reweighting may not be the appropriate approach.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-237](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
