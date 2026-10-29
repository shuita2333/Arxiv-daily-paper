# 📦 其他研究 | 2026年10月30日

> 本类共 **257** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-257](./part-06.md)

---

### 1. [KORA: Deterministic-First Execution Control for AI Workloads](https://arxiv.org/abs/2610.35869)

**<font color=#1a73e8>作者：</font>** Albert Heekwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI applications often invoke a model before they determine whether inference is necessary. That default is useful for ambiguous generative tasks, but it is poorly matched to work that is structured, deterministic, policy-bound, lookup-oriented, or directly verifiable. KORA introduces deterministic-first execution control: a pre-inference control layer that represents requests as task paths, attempts deterministic or structured routes first, validates route outcomes, records telemetry, and escalates to a model-candidate path only when deterministic handling is insufficient. This paper presents KORA as a deterministic-first execution-control architecture and reports bounded evidence from reproducible benchmark and validation workloads. In a reproducible 100-task deterministic-heavy benchmark, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline, with zero mismatches in the deterministic subset. The workload is intentionally deterministic-heavy: it includes categories such as FAQ lookup, policy/rule checking, schema or format validation, deterministic transformation, and a smaller set of model-needed ambiguous or generative tasks. A separate synthetic customer-support local/no-network validation workload demonstrates route measurement and avoided model-call accounting in an application-shaped setting. These results support bounded model-invocation reduction and validation visibility in documented workloads. They do not establish production behavior, real-provider outcomes, energy outcomes, API-cost reduction, or broad superiority.

---


### 2. [Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention](https://arxiv.org/abs/2610.35877)

**<font color=#1a73e8>作者：</font>** Ayush Mittal, Dhruv Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Changing a deployment policy can invalidate a world model's uncertainty while leaving the physical transition mechanism and predictor unchanged. For one-step prediction, if source and target laws share the conditional mechanism $P(Y|X)=Q(Y|X)$, then the intervention is identified by the pre-outcome change of measure $w(X)=dQ_X/dP_X$. For policy-controlled dynamics this ratio factors into state-occupancy and action-propensity terms. Weighted conformal calibration transports marginal coverage to the target law; with an estimated ratio $\hat w$, $P_Q\{Y \in C_{\hat w}(X)\} \ge 1-\alpha-TV(Q,\hat Q) \ge 1-\alpha-E_P|w-\hat w|$. Population log-loss regret for a source-versus-target domain classifier bounds the same ratio error. If $h$ is its clipped target posterior, $\rho$ is the target-domain prior, and $\Delta(h)$ is population log-loss regret, then $E_P|w-\hat w_h| \le (1/(\rho\gamma))\sqrt{\Delta(h)/2}$. An exact cancellation improves the dependence from a generic odds-map bound of order $\gamma^{-2}$ to $(\rho\gamma)^{-1}$. Our experiments use a released DINO-feature world model and physical Franka trajectories. Under the strongest controlled state-action shift, ordinary 90% conformal sets cover 55.0%, whereas oracle and learned-ratio calibration cover 91.0% and 90.9%. The learned surrogate remains within 0.9% total variation of the target law. Calibration is relative to the deployment law: the model can remain fixed while calibration follows the intervention. We machine-check in Lean 4 the finite-support algebraic and causal identities used in the classifier-regret argument, including its coverage-composition step.

---


### 3. [ObjectTwin: Measuring the Asset Correspondence Gap for Capture-Anchored Digital Twins](https://arxiv.org/abs/2610.35904)

**<font color=#1a73e8>作者：</font>** Zhenghe Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-wise reconstruction increasingly inserts generated meshes into captured scenes as editable proxies for observed objects. This use creates a requirement absent from isolated-asset scores and pose estimates: at the captured metric state, the proxy should reproduce calibrated observations of the same instance. We present ObjectTwin, a scan-grounded measurement protocol that freezes the instance, cameras, scan-projected support and recorded depth, metric anchor, and evaluation denominator, then replaces only the object representation. The resulting asset correspondence gap measures lost observation agreement relative to scan-derived visible geometry without treating the scan as complete physical ground truth. Across two indoor RGB-D capture domains and two generation backends, visible, anchored generated assets lose 0.302-0.497 MaskIoU under this replacement. Every tested scene-level estimate is positive, while same-input generator preference reverses across capture domains. Coverage and overlap-depth analyses locate disagreement in both visible support and surface placement; the evaluated conservative pose refinement does not systematically recover it. These results establish capture correspondence as a separately measurable interface between generated-asset quality and stronger physical or task-level evaluation.

---


### 4. [PASS Is a Claim, Not an Observation: Mechanical Re-verification of 10 Self-Asserted Fix Claims in a Live Multi-Agent Audit Layer](https://arxiv.org/abs/2610.35950)

**<font color=#1a73e8>作者：</font>** Lei Zhenbing, Lei Chang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> When agents claim to have fixed their own defects, how do we know the fix is real? We mechanically re-verified 10 self-asserted code-level fix claims from a privileged coordination agent (azone_god) operating in AITRAP, a live multi-agent knowledge-tree platform. These 10 claims were extracted from a corpus of 179 coordination broadcasts (28 containing structured fix assertions, 31 unique fix-ID/message pairs, 18 distinct fix identifiers). Fix claims use mixed English/Chinese formats (PASS, checkmarks, and "verification passed" declarations). Each code-level claim was checked against three criteria: (1) file modification timestamp (mtime) consistency -- 70% pass; (2) presence of the claimed defensive pattern at the specified identifier and call site -- 60% pass in the claimed file (80% anywhere in the codebase); (3) deterministic rule-based re-verification from the broadcast announcement alone -- 80% pass. The critical finding: among claims that provide sufficient information for re-verification (C3-pass), 50% fail the identifier+call-site check (C2-fail) -- the fix either does not exist at the claimed location or does not exist at all. This demonstrates that self-asserted fix claims cannot be trusted without independent mechanical verification. Our central claim: a PASS declaration is a claim requiring independent verification, not an observation of fix completion.

---


### 5. [Curriculum-Driven Deep Reinforcement Learning for Autonomous Far-Range Rocket Landing](https://arxiv.org/abs/2610.35954)

**<font color=#1a73e8>作者：</font>** Atin Chowdhury, Piyush Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous vertical landing of reusable launch vehicles is a critical yet formidable challenge in aerospace engineering, primarily due to highly nonlinear dynamics, stringent precision require- ments, and inherent environmental uncertainties. While reinforcement learning (RL) has emerged as a promising alternative to traditional model-based control, existing approaches frequently rely on flat training paradigms and highly simplified initial conditions, drastically limiting their real-world applicability. This paper proposes a comprehensive curriculum-driven deep reinforcement learning framework designed to master both far-range navigation and precision landing. By employing a three-stage curriculum augmented with a critic warm-up procedure and a rehearsal mechanism to prevent catastrophic forgetting, alongside a high-dimensional observation vector utilizing a full 3 X 3 rotation-matrix, the agent is trained to navigate from an initial horizontal distance of 1,000 to 1,500 units vastly farther than prior benchmarks before executing a soft touchdown. Crucially, we intro- duce a redesigned reward function that reduces unnecessary computational overhead and addresses limitations of earlier formulations, including poorly calibrated reward components and potentially conflicting optimization objectives. The redesigned function bounds the per-step reward magnitude by (O(1)), while its progress term accumulates the total distance closed over the trajectory. The available 100,000-episode results report a 99.98% success rate for the proposed policy and 68.31% for the baseline under the evaluation conditions. In the evaluation, the proposed policy retained 69.1% of its initial fuel capacity and achieved a mean final distance from the pad centre of 7.07 units, compared with 13.10 units for the baseline. Landing visualizations are available in Video 1 and Video 2.

---


### 6. [Exponential Wake-Up Overshoot in Explicit Gaussian Point-Process Filters](https://arxiv.org/abs/2610.35958)

**<font color=#1a73e8>作者：</font>** Hanwu Qin, Dianhai Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When events resume after a long silence, explicit Gaussian point-process filters amplify the first update exponentially in the silence duration. We give the exact distribution of this update and a computable index that predicts when it overshoots. For the explicit (single-scoring-step) filter and its implicit posterior-mode counterpart, we derive second-order silence expansions of the state variance with opposite-sign logarithmic corrections. The crossing index determines when the post-wake prediction exceeds the resumed rate, separating the bin width at which the amplification exponent reaches one from the larger width at which the true rate is overshot. At fixed bin width, the implicit filter's expected loss grows logarithmically with silence duration, whereas a continuous-time counterexample rules out a bound uniform in bin width and silence duration. Experimental evaluation confirms these predictions in all 73 crossing cells and on exchange trade data, while variance caps reduce explicit overshoot but mostly hurt the implicit filter.

---


### 7. [From Slices to Volumes: Comparing 2D, 2.5D, and 3D Residual Networks for Pulmonary Nodule Malignancy-Risk Classification](https://arxiv.org/abs/2610.35960)

**<font color=#1a73e8>作者：</font>** Bahodir Nazarov, Zineb Gharib, Fatima Zazoul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Purpose: To compare 2D, 2.5D, and 3D residual networks for pulmonary nodule malignancy-risk classification and evaluate momentum-contrast pretraining, mild augmentation, and exclusion of indeterminate ratings.
Methods: A retrospectively prepared LIDC-IDRI cohort contained 2,654 nodules labeled benign, indeterminate, or malignant using median radiologist ratings. Patient-disjoint splits comprised 1,876 training, 382 validation, and 396 test nodules. Representations included one axial slice, five neighboring slices, and a local CT volume. Each track evaluated a randomly initialized baseline, momentum-contrast pretraining followed by fine-tuning, and supervised training with mild augmentation. Checkpoints were selected by validation Macro-F1. The 2D experiments used three seeds; 2.5D and 3D results were single-run estimates. A separate binary experiment excluded indeterminate nodules.
Results: Augmented models achieved test Macro-F1 values of $0.6134\pm0.0075$ for 2D, $0.6537$ for 2.5D, and $0.5403$ for 3D; the 2D uncertainty denotes population standard deviation across seeds. Corresponding accuracies were $0.6128$, $0.6869$, and $0.5455$. Augmentation improved Macro-F1 within every track, whereas the tested pretraining recipes reduced it. Binary Macro-F1 values were $0.8227$, $0.8664$, and $0.7554$, respectively.
Conclusion: Augmented 2.5D achieved the highest observed performance. Differences in preprocessing, optimization, capacity, and replication limit attribution to dimensionality. Labels reflect radiologist-assessed malignancy risk rather than pathology-confirmed cancer. Code and experimental results are available at this https URL.

---


### 8. [Knowledge distillation across teacher architectures for compact diabetic retinopathy grading](https://arxiv.org/abs/2610.35961)

**<font color=#1a73e8>作者：</font>** Mossa Manisa, Habiba Jahan Priya, A.K.M. Fakhrul Hossain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diabetic retinopathy grading from retinal fundus photographs is important but difficult to deploy on resource-constrained hardware. We conducted a controlled study of offline response-based knowledge distillation for five-class diabetic retinopathy grading on APTOS 2019, comparing ResNet-50, MobileNetV3-Large, and Swin Transformer-Tiny (Swin-T) teachers distilled into a MobileNetV3-Small student. A 3 x 4 x 2 grid of teacher, temperature, and hard-label weight was screened at one seed, while six configurations and the no-distillation baseline were evaluated across three seeds. The highest observed single-seed quadratic weighted kappa was 0.9093 (macro-F1 0.6851) for Swin-T at temperature 4 and hard-label weight 0.7; the corresponding three-seed mean was 0.9024, compared with 0.8804 for the baseline. The student used 1.52 M parameters and 5.94 MB, representing an 18.07x parameter reduction relative to Swin-T. Temperature and hard-label weight effects were teacher- and configuration-dependent, while small performance differences were sensitive to random seed. Knowledge distillation produced a compact student with competitive performance under the evaluated protocol, but independent external validation remains necessary.

---


### 9. [Condition-Enhanced Generative Adversarial Network for Aerodynamic Configuration Design of Commercial Aircraft](https://arxiv.org/abs/2610.35963)

**<font color=#1a73e8>作者：</font>** Youzheng Yu, Jiaqing Kou, Weiwei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative machine learning provides an end-to-end framework for aerodynamic design optimization by generating diverse aerodynamic configurations conditioned on target performance. However, the generated designs may violate geometric constraints or deviate from the prescribed aerodynamic performance. Therefore, we propose a Condition-Enhanced Generative Adversarial Network (CEGAN) that embeds geometric and aerodynamic information into the generative process. A condition-informed loss function is developed by combining a geometry-guided feasibility penalty with an aerodynamic performance penalty evaluated by surrogate models trained on the same dataset. Additionally, an output filtering mechanism discards infeasible designs using these surrogate models, ensuring compliance with prescribed conditions. The method is demonstrated on aircraft configurations similar to the Cessna Citation X. Each configuration is represented by 28 shape parameters, whose aerodynamic performance is evaluated using OpenVSP. Interpolation and extrapolation tests are conducted for different network architectures and conditioning strategies. Compared with the baseline model, CEGAN reduces the average generation error by at least 36% for interpolated conditions and by at least 46% under extreme extrapolation conditions, while successfully producing diverse and physically feasible designs that extend beyond the training distribution. Therefore, the proposed CEGAN framework offers a robust and accurate tool for rapid aerodynamic configuration exploration during the conceptual design phase.

---


### 10. [A Hyper-Logical View on Multi-Agent Path Planning](https://arxiv.org/abs/2610.35964)

**<font color=#1a73e8>作者：</font>** Hadar Frenkel, Dor Atzmon  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Path Planning (MAPP) requires collision-free paths for multiple agents. MAPP has numerous real-life applications, including the navigation of automated vehicles, and has therefore many variants considering different constraints, requirements, and objectives. For each such variant, a new algorithmic treatment is often developed. This paper takes a complementary, specification-centered view: we show that many MAPP variants can be modeled in HyperLTL, a temporal logic that reasons about multiple paths and their evolution through time, and in its omega-regular extension HyperQPTL. The contribution is not a claim that current hyperproperty model checkers replace specialized MAPP solvers. Rather, the hyper-logical view gives a unified language for comparing MAPP variants, adding cross-agent constraints, expressing optimality, and connecting MAPP to verification, explanation, and causality techniques for hyperproperties.

---


### 11. [Generalization in Learning: Eyring Formula and Predator-prey Model](https://arxiv.org/abs/2610.35965)

**<font color=#1a73e8>作者：</font>** S.V.Kozyrev, I.A.Lopatin, Alexander Pechen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, generalization in machine learning is investigated using a predator-prey model. We overview biological and chemical interpretation of the stochastic gradient Langevin dynamics and generative adversarial network. For a particular example of recovering an unknown function by a polynomial of fixed degree from a set of noisy data, the predator-prey model provides better approximation compared to the gradient descent method. Further, thermodynamical arguments, in particular Eyring formula, are used to explain grokking (delayed generalization) phenomenon in machine learning.

---


### 12. [Data-driven Discovery of Lie Symmetries and First Integrals with Latent ODEs](https://arxiv.org/abs/2610.35967)

**<font color=#1a73e8>作者：</font>** Matt L. Wiemman, Peter Melchior  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present LatentLieODE, a novel neural ODE method to discover linear Lie symmetries and first integrals of the learned dynamics from timeseries observations such as video inputs. It starts with an autoencoder, which learns a low dimensional representation of the observed system and then maps trajectories to decorrelated latent coordinates $z \in \mathbb{R}^d$. A bank of linear infinitesimal generators $\mathbf{A}_k \in \mathbb{R}^{d \times d}$ is fitted jointly against a differentiable Lie-bracket residual $\mathbf{J}_f(z)\mathbf{A}z - \mathbf{A} f(z)$, while an MLP optimises the latent ODE $f(z) = \mathrm{d}z/\mathrm{d}t$ to reconstruct the observation-space timeseries. After suitable generators and $f$ are found, we fit a third network $H_\phi$ to generate the first integral of the system. Across six benchmark systems (harmonic oscillator, simple and twin pendulums, Lotka-Volterra, pixel pendulum, sphere geodesics) we find each system's relevant symmetries, and the discovered invariants match ground-truth conserved quantities at $|\rho| \geq 0.978$. On the sphere, the pipeline recovers a non-abelian $\mathfrak{so}(3)$, certified by the negative-definite Killing form of its recovered structure constants. This work presents significant advances in data-driven discovery of symmetries and provides a new pathway for neural surrogates of dynamical systems.

---


### 13. [Multiple Leak Localization in Water Distribution Networks through Graph Neural Networks](https://arxiv.org/abs/2610.35972)

**<font color=#1a73e8>作者：</font>** Arvin Ajoodani, Sara Nazif, Pouria Ramazi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Leak localization in water distribution networks is challenging when multiple leaks occur simultaneously, particularly under sparse monitoring. Existing data-driven methods often assume a single or predefined number of leaks or require extensive enumeration of leak combinations. This study proposes a graph neural network (GNN) model that localizes a variable number of simultaneous leaks without specifying the leak count in advance or exhaustively generating every possible combination of leak locations for training. The model is evaluated on two benchmark networks of different sizes, the 31-node Hanoi network and the larger 92-node NET3 network, under variable demand, sparse pressure-sensor coverage, variable leak magnitudes, and varying numbers of simultaneous leaks. The GNN outperforms multilayer perceptron, support vector machine, K-nearest neighbors, and random forest classifiers by up to 12% and 20% in accuracy respectively in Hanoi and NET3 networks. Consistent performance across both networks supports the scalability of the proposed approach.

---


### 14. [A Graph-informed Kriging model for sample-efficient Bayesian optimization of wind farm layouts](https://arxiv.org/abs/2610.35975)

**<font color=#1a73e8>作者：</font>** Zhen-Fan Wang, Kai Zhang, Xianping Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wind farm layout optimization becomes increasingly difficult as turbine count grows, especially when high-fidelity aerodynamic models are used. Conventional Kriging-based Bayesian optimization often suffers from low sample efficiency in high-dimensional layout spaces because sparse training data provide limited domain coverage. We develop a Graph-informed Kriging framework that embeds reusable aerodynamic interaction information into the surrogate mean function. The wind farm is represented as a directed aerodynamic graph, where pairwise turbine interactions defined in a low-dimensional relative-coordinate space are assembled into a farm-scale mean. This structured mean captures the dominant variation in annual energy production (AEP), allowing the Gaussian process to model only the residual structure and uncertainty. Numerical experiments show that Graph-informed Kriging consistently improves AEP prediction accuracy over ordinary and generic-trend Kriging under sparse-data conditions, with increasing benefits as layout dimension and wake-interaction strength grow. Embedded in Bayesian optimization, it substantially improves sample efficiency and achieves competitive solutions for the IEA Wind Task 37 benchmark with about 280 AEP evaluations. In a controlled 16-turbine case, it also outperforms ordinary and multi-fidelity Kriging under the same high-fidelity evaluation budget. The framework is further extended to a 48-turbine wind farm, demonstrating applicability to large-scale CFD-based layout optimization. These results show that Graph-informed surrogate modeling can enable more efficient use of high-fidelity aerodynamic models for reliable large-scale wind farm layout design.

---


### 15. [Enhancing Deep Learning Model Performance through Data Generation Strategies: Classification of Olive Tree Diseases](https://arxiv.org/abs/2610.35984)

**<font color=#1a73e8>作者：</font>** Hicham El Akhal, Abderrahim Waga, Aissa Ben Yahya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning models are highly effective in a wide range of domains, particu larly in plant disease diagnosis. However, their performance is often limited by challenges such as insufficient data and class imbalance. In our work, we propose a comprehensive data generation strategy to overcome these limitations. First, we apply various data generation techniques, including traditional augmentation methods, CutMix, MixUp, and synthetic image generation using Deep Convolu tional Generative Adversarial Networks (DCGANs), to create new data samples. Second, we exploit this generated data in three scenarios: (S1) balancing class distribution in the original dataset, (S2) increasing the number of samples per class, and (S3) expanding the dataset while maintaining balanced classes. Third, we evaluate the impact of these data distributions (S1, S2, S3) on model perfor mance using the EfficientNetV2B0 architecture with pre-trained and fine-tuned weights. The experimental results show a substantial improvement in classifica tion accuracy, emphasizing the critical role of data diversity and class balance. These findings highlight the effectiveness and adaptability of the proposed strat egy of data generation and distribution for enhancing dataset quality, offering promising applications in plant disease detection and precision agriculture.

---


### 16. [Pricing Cross-Bank Context in Federated Anti-Money Laundering](https://arxiv.org/abs/2610.35996)

**<font color=#1a73e8>作者：</font>** Lidia Losavio, Dario Fenoglio, Martin Gjoreski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most graph-based Anti-Money Laundering (AML) methods assume access to a pooled transaction graph containing all accounts and payments, which in reality does not exist. Federated learning offers the necessary privacy guarantees but it remains unclear how money laundering patterns spanning separate graphs can effectively be detected. We exploit transactions already recorded by both endpoint banks to approximate remote account states locally, enabling multi-layer Graph Neural Network (GNN) computation without additional account-specific exchange. Starting from this baseline, we test whether the remaining context is worth sharing, using a disclosure ladder that adds two transaction counts per remote account or the counterparty's own GNN states. On AMLworld HI-Small, across six GNN backbones and up to 32 silos, the observable baseline yields the largest gain and keeps it as fragmentation shrinks the visible slice; counts add a robust correction, while exact remote states help only in specific regimes. In controlled privacy--utility studies, the noise needed to protect shared states erases their detection value before it buys meaningful privacy, whereas counts stay useful even under strong privacy protection. These findings support a practical rule for banks: use what they already record, and formally protect the little that must move.

---


### 17. [Merkle-Tree-Based Verifiable Public Data Auditing for Cloud Object Storage Using Smart Contracts](https://arxiv.org/abs/2610.36001)

**<font color=#1a73e8>作者：</font>** Siri Reddy Tadi, K. Gangadhara Rao, M. Venu Gopalachari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Owners of data in cloud object storage cannot directly check whether the provider still keeps every object unchanged. Existing research mostly checks blocks inside files or relies on third-party auditors, and less attention has been given to checking each object against a public blockchain reference while measuring the cost. A full-data audit downloads every object and compares it with a saved hash list, which is slow and only as reliable as that list. We propose a public auditing system in which the SHA-256 hash of each object and its name forms a leaf of a Merkle tree, so the whole dataset is represented by one Merkle root. This root is stored in an Ethereum smart contract as a trusted public record, while the objects stay with the provider. An auditor downloads an object, rebuilds the root using a short Merkle proof and compares it with the stored root, marking the object as intact, modified or missing. In five experiments on an S3-compatible store and a local Hardhat blockchain (normal audit, single- and multiple-object tampering, deletion and scalability), the system detected 15 of 15 single modifications, 2,205 of 2,205 modified objects and 830 of 830 deleted objects with no false alarms. The proof needed only 14 hashes for 10,000 objects, so checking one object took about 10 ms and a 100-object sample about 150 ms regardless of dataset size, while a full audit of 10,000 objects (14.3 s) took about as long as downloading them (13.5 s). Storing the root cost 91,863 gas, 252 times less than storing 1,000 hashes on-chain. The system thus shows exactly which objects were modified or are missing, with its main savings coming from checking selected objects.

---


### 18. [Immersive Commons: Designing Ephemeral Spatial Dialogue for Co-Located Mixed Reality Environments](https://arxiv.org/abs/2610.36014)

**<font color=#1a73e8>作者：</font>** Wuwu Ran, Mohammed Faraj Al-Suwaidi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Head-mounted mixed reality (MR) often prioritises individual immersion, potentially drawing attention away from others sharing the room. This paper asks how MR can support co-located spatial dialogue through embodied interaction and activity visible to non-headset observers. We introduce Immersive Commons, a design framework, and Atmos Messages, a prototype combining gesture-based, ephemeral spatial messages with voice transcription, preset text, and a public floor-plan overview. Following a Research through Design approach, fifteen participants created 236 messages across two sessions, including 48 voice-authored messages. Questionnaire responses highlighted playfulness and social awareness, while observations suggested opportunities for exchange grounded in the architectural setting. Interaction clustered near the public display, although this was also where participants put on their headsets. These findings suggest the potential of ephemeral spatial messaging to support co-located exchange, with playfulness, shared visibility, and architectural context informing the design of more social and situated MR experiences.

---


### 19. [Exploratory creative pre-ranking: Hierarchical empirical-Bayes Thompson sampling for real-time creative optimization](https://arxiv.org/abs/2610.36020)

**<font color=#1a73e8>作者：</font>** Jiale Han, Ajith Moparthi, Dan Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic creative optimization decides which creative of an ad to render for each request. Recent work places that choice before ad ranking, but relies on deterministic point predictors with no calibrated uncertainty. AI-generated content has made creatives nearly free, while feedback per creative remains sparse and selection faces a tight latency budget. We introduce a creative pre-ranker that scores every recalled creative and shortlists each campaign's pool before the per-user ranker runs. Creatives sit in a hierarchy of audience segment, advertised item, campaign and creative, so a cold creative falls back on what its parent levels have earned, and how much it borrows from its parents is set in closed form from historical logs, with one parameter per level and nothing tuned. To stay within the latency budget, the pre-ranker predicts for an audience segment rather than an individual user, from per-attribute counters. It selects by a single Thompson draw per creative, balancing exploration and exploitation so that a new creative still has a chance to be learned. Replaying Roblox Sponsored-ads traffic over campaigns with competing creatives, the shortlist lifts predicted play-through rate by 8.14% against 2.80% for an equally sized random shortlist, forwards more than 40% fewer creatives than the full pool, and adds only 0.2% to serving time. After an A/B test on live traffic, the method now serves in production at Roblox.

---


### 20. [Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding](https://arxiv.org/abs/2610.36022)

**<font color=#1a73e8>作者：</font>** Rui Yang, Yanwei Li, Sili Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image and video generators can produce spatially consistent visual content, but how to use this capability to improve spatial understanding remains underexplored. We study this problem from two perspectives: geometric supervision during training and explicit geometric evidence during inference. To this end, we introduce a unified geometric understanding and generation model (GeoUG) that integrates depth and multi-view generation with spatial understanding. First, we design a multi-scale depth codec that enables metric-depth generation using a pretrained visual autoencoder, and show that joint training yields task-dependent gains in spatial understanding. Second, we introduce 3DCueBench to control geometric difficulty while balancing selected 2D cues, and find that generated depth provides larger reasoning gains on questions requiring fine-grained geometric discrimination. Building on this finding, we develop adaptive interleaved reasoning, in which GeoUG first drafts an answer and then decides whether to generate geometric evidence to confirm or revise it. We train this decision through reinforcement learning, balancing accuracy gains over retaining the draft against generation cost. GeoUG achieves circular accuracies of 97.9%, 90.8%, and 94.2% on CV-Bench-3D, 3DCueBench, and DA-2K with fewer generation calls than always generating.

---


### 21. [Jaxnasium: Embracing PyTrees For Any-Agent, Cross-Suite Reinforcement Learning](https://arxiv.org/abs/2610.36075)

**<font color=#1a73e8>作者：</font>** Koen Ponse, Aske Plaat, Thomas M. Moerland  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hardware-accelerated reinforcement learning in JAX has gained rapid popularity in recent years and has proven to be a successful method of scaling online reinforcement learning. The resulting ecosystem, however, is fragmented: environment suites define their own interfaces, and algorithm implementations are typically written for a single suite, a single type of space, and either JAX-native or host-based environments. Here we present Jaxnasium, a library for JAX-based reinforcement learning, aiming to make the field more accessible. Jaxnasium represents observation and action spaces as PyTrees, and uses this structure to build networks and support multi-agent processing. Through this, its near-single-file implementations run on discrete, continuous, image, and composite spaces, as well as in multi-agent environments, without any changes to the algorithm code. The same files serve as readable, research-friendly algorithms, as well as importable algorithms for more applied workloads. Through a minimal Gymnasium-style interface and wrappers for 11 suites, over 300 environments are available on which a small PPO implementation with default hyperparameters is able to run. Additionally, through a simple wrapper, we can run Gymnasium and EnvPool environments with the same algorithm and training loop, with no performance loss compared to architectures specifically built for training JAX algorithms on host-based environments. Jaxnasium further provides tools for multi-seed evaluation, hyperparameter sweeps, and project scaffolding. Jaxnasium is open-sourced at this https URL

---


### 22. [The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](https://arxiv.org/abs/2610.36077)

**<font color=#1a73e8>作者：</font>** Weidong Tang, Ruiheng Wang, Jingxuan Zhang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace with growing task diversity and complexity. A key insight is that tasks with different modalities and surface forms can share the same underlying capability requirements. We therefore introduce The Trinity, a recursive self-improvement framework coupling world generation with Harness evolution through three roles: Creator, Explorer, and Evolver. Drawing on verified execution trajectories, Evolver shifts the basis of task organization from surface categories to shared requirements, reorganizing the original task tree into a hierarchical capability tree. We introduce Capability-Driven Real2Sim2Real: for heterogeneous tasks at the same node, Creator abstracts their common requirements into simplified, verifiable simulated worlds for capability learning, while evaluation on original tasks measures transfer. Along this capability tree, Explorer progressively evolves reusable capability modules through selective inheritance, forming a Harness tree whose validated updates accumulate across iterations within a fixed topology. The resulting Harnesses specialize in different capabilities, motivating a Capability-Aware Harness Router that uses public task information to select compatible module configurations from the tree. Our evolved Harnesses improve mean performance by 34 points across 28 training benchmarks and 26 points across 18 unseen benchmarks, including two real-world embodied tasks.

---


### 23. [Minimax-Optimal Small-Loss Bounds for Online Linear Optimisation on $\ell_p$ Balls](https://arxiv.org/abs/2610.36097)

**<font color=#1a73e8>作者：</font>** Jack J. Mayo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study full-information online linear optimisation on the unit $\ell_p$ ball in $\mathbb{R}^d$, for fixed $2\le p<\infty$ and losses of dual norm at most one. Let $\Delta_T$ denote the cumulative loss of the best fixed action above each round's minimum. A follow-the-regularised-leader (FTRL) algorithm attains, on every loss sequence and without knowing $T$ or $\Delta_T$, regret $O_p(1+\min\{\Delta_T^{1-1/p},\, d^{1/2-1/p}\sqrt{\Delta_T}\})$. Matching lower bounds show that this rate is minimax for each fixed $p$, and its constant $(2+o(1))p/\log p$ is optimal as $p\to\infty$ among guarantees uniform in $d$ and $T$. The algorithm uses a bounded radial regulariser and switches at most once to its quadratic augmentation. On some paths where follow-the-leader (FTL) has regret one, its regret grows with $T$. A switching extension keeps the sharp constant and also guarantees $\mathrm{Reg}_T\le 2\,\mathrm{Reg}_T^{\mathrm{FTL}}$. For i.i.d. losses whose mean has no zero coordinates, we compute the exact $\log T$ coefficient of the expected regret, which separates FTL's variance term from the bias of the regulariser.

---


### 24. [Dirichlet Process Mixtures within Semiparametric Bayesian Networks: A Novel Conditional Density Estimation Approach](https://arxiv.org/abs/2610.36110)

**<font color=#1a73e8>作者：</font>** Victor Alejandre, Pedro Larrañaga, Concha Bielza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semiparametric Bayesian networks (SPBNs) are flexible probabilistic graphical models for representing joint distributions of continuous variables through lower-dimensional conditional probability distributions (CPDs). Existing SPBN models use kernel density estimators (KDEs) for non-parametric CPD modeling, but their one-component-per-observation mixture representation can lead to increased inference costs and density estimation errors, which can be limiting. In this work, we define a new CPD modeling approach for non-parametric components based on Bayesian non-parametric Dirichlet Process Mixtures (DPMs) within SPBNs. DPMs provide a data-adaptive clustering of observations, yielding a more compact representation while retaining the flexibility of non-parametric density estimation, unlike KDE. This results in lower inference costs while improving density estimation performance. We implement the proposed DPM-based SPBN (DPM-SPBN) by extending the open-source PyBNesian package and evaluate it on synthetic and real-world data. For a given network structure, DPM-based CPDs significantly outperform state-of-the-art Bayesian network models for continuous variables in density estimation, achieving lower absolute log-likelihood errors on synthetic data. We further investigate the impact of the proposed CPD modeling on structure learning methods relying on CPD-based scores. DPM-based SPBNs achieve lower structure learning and density estimation errors than KDE-based SPBNs. Experiments on real-world data corroborate these findings, identifying DPM-based CPD modeling as the most effective alternative among the evaluated non-parametric approaches for continuous variables.

---


### 25. [Scaling and Renormalization in Neural Networks: An Effective Renormalization-Group Description of Grokking](https://arxiv.org/abs/2610.36113)

**<font color=#1a73e8>作者：</font>** Min Chen, Junqi Wang, Zeguan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking is a delayed transition from memorization to generalization in deep neural networks (NNs). We examine whether scaling and renormalization group (RG) theories can describe this dynamics, establishing a quantitative physical framework for neural generalization transitions. For modular addition on a two-layer NN, an ensemble of trained models defines an order parameter (the squared weight norm) and fluctuation proxies for the heat capacity and the susceptibility, with training epoch and weight decay serving as thermal and field control coordinates. To bridge neural architectures to real-space RG, we construct an exact coupling matrix via a second-order expansion of the loss with respect to per-neuron norms and use its Fiedler vector to define an effective geometry. This spectral ordering yields a monotonic spatial decay of coupling strength that is absent under random permutations. We then execute real-space RG by block-spin aggregating adjacent neurons and parameterizing the coupling matrix into off-diagonal band strengths. Linearizing this local RG map yields relevant scaling exponents and five derived critical exponents, with direct empirical estimates matching RG predictions within 1-10%. Overall, our framework provides a consistent effective description of grokking, suggesting the scaling and renormalization group formalism as a tool to investigate NN dynamics.

---


### 26. [Why and How to Do Science When AI Is Better at It: A Framework Grounded in Human Understanding and Direction](https://arxiv.org/abs/2610.36116)

**<font color=#1a73e8>作者：</font>** Hoda Heidari, Aydin Mohseni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI begins to match or exceed human researchers at core scientific tasks, two questions become pressing: \emph{why} should humans keep doing science, and \emph{how} should they use AI when they do? This paper argues that the second can be answered only by answering the first. It holds that one indispensable aim of science is \emph{durable, collective human understanding of the world, pursued in service of human ends and values}. From this principle it derives a two-part test for when a research task can be delegated to AI. The first part, \emph{human understanding}, requires that the scientific community remain able to explain, defend and contest the resulting claims, and retain the skills to do so. The second, \emph{human direction}, requires that judgments about which questions matter and what findings mean stay with accountable humans. Applying the test to each phase of research in the Contributor Roles Taxonomy (CRediT) yields recommendations that fields can tailor to their questions and methods. The framework differs from existing guidance in three ways. It rests on an account of what science is for rather than on integrity norms. It holds even if AI outperforms human researchers, rather than depending on AI's current limitations. And it judges each use of AI by its effects on human understanding and direction rather than by the type of tool, across every phase of research, including peer review and the training of new researchers. It closes with the reforms needed to keep science aimed at human understanding and direction.

---


### 27. [SpatialPC: Deep Computation with Sublinear Local Credit Propagation](https://arxiv.org/abs/2610.36139)

**<font color=#1a73e8>作者：</font>** Benjamin Prada, Shion Matsumoto, Ankur Arjun Mali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On a chain of $N$ states, any local learning rule with bounded communication range needs $\Theta(N)$ rounds before the loss can influence the earliest parameters, and this latency is usually attributed to depth. We show that it is a property of the communication geometry rather than of depth. For $N=m^d$ states placed at constant density in $d$ dimensions, a light-cone argument gives an $\Omega(N^{1/d})$ lower bound on the number of bounded-range rounds that any local algorithm needs before its gradient estimates can be sign-correct at every parameter. We construct a unit-range, degree-$2d$ directed acyclic graph that contains a Hamiltonian computation of length $N-1$ and in which every state lies within directed distance $d(m-1)=\Theta(N^{1/d})$ of the output, matching the lower bound. In the realizable-circuit model, depth and credit depth are therefore independent parameters: represented depth $\Theta(N)$ and causal credit latency $\Theta(N^{1/d})$ coexist, with a separation of order $N^{1-1/d}$. SpatialPC realizes this separation within predictive coding. Credit is propagated by adjoint prediction dynamics (APD), a local update whose $K$-round state on a settled acyclic graph is the truncated reverse-path sum $a^K=\sum_{k<K}(J^\top)^k b$, with error exactly $(J^\top)^K a^\star$. Graph geometry fixes when credit can first arrive at a state; the Jacobian-weighted path tail fixes how many further rounds accurate credit requires. A sparse two-dimensional Moore compiler retains the $N-1$ backbone with $\tfrac32N-2$ unit-range edges and has measured worst-node reachability $\sqrt N+2$ up to $N=65{,}536$, where a 65,535-edge backbone is reached in 258 local hops. With $T=2\sqrt N$ rounds, SpatialPC keeps finite-round task gradients aligned with settled gradients (cosine $0.93$ on MNIST and $0.97$ on Fashion-MNIST at $N=256$) and reaches $97.6\%$ and $88.1\%$ test accuracy after 20 epochs.

---


### 28. [They Will See Johnny's Message: A Measurement Study of Post-Quantum Cryptography Across Email Delivery Paths](https://arxiv.org/abs/2610.36145)

**<font color=#1a73e8>作者：</font>** Jaehwan Park, Sunghyun Park, Kevin Nam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Harvest-now, decrypt-later (HNDL) attacks make the transition to post-quantum cryptography (PQC) urgent for email. This paper presents a systematic measurement that jointly examines PQC deployment across email service stages, negotiation by communicating peers, and usable message encryption. Endpoint-level support alone does not establish PQC readiness across email workflows because submission, relay, and access use independently negotiated Transport Layer Security (TLS) connections. We therefore combine three snapshots of relay, submission, access, and webmail services associated with the Tranco Top~1M domains with controlled tests of mail clients, sending servers, and OpenPGP and S/MIME implementations. Our measurements reveal a transition concentrated among a few providers, with available capability not consistently translating into actual use. Fewer than half of the domains in each service panel support PQC, and Google alone accounts for approximately 87\% of hybrid-capable relay domains. Only two of eight tested sending providers negotiate PQC with our receiver, although five accept it inbound. When TLS groups are restricted to PQC, four of the six incompatible senders fall back to plaintext where unencrypted SMTP remains permitted. At the message layer, limited native key generation, key-format incompatibilities, and backend integration failures further constrain usable PQC encryption.

---


### 29. [From Structural Feedback to Prompt Policies: Learning Faithful Text-to-Image Prompt Editors](https://arxiv.org/abs/2610.36146)

**<font color=#1a73e8>作者：</font>** Wentao Ye, Yali Ye, Zhiqing Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt optimization should improve the image a user receives without changing the scene the user requested. Yet stylistic rewriting can weaken object attributes and relations even when global text--image similarity remains high. We propose StruPO, a structure-aware prompt editor that uses a calibrated scene graph as a shared representation for policy conditioning and image-grounded supervision. The graph exposes what should be preserved, while deletion, reordering, and insertion provide a token-aligned way to modify the prompt. This turns structural feedback from an external critique into a training signal for a reusable editing policy. Learning from that signal requires handling both uncertain grounding and stochastic image generation. StruPO retains grounding confidence through smooth reward shaping and averages multiple images for each edit before computing group-relative advantages. Experiments span three disjoint 2K-prompt test sets and four frozen generation backbones, with comparisons to learned prompt optimizers, iterative structural feedback, diffusion-model fine-tuning, and inference-time attention control. StruPO improves the faithfulness--aesthetics trade-off, with consistent gains in relational fidelity. Independent automatic evaluators and a 15-annotator study provide complementary evidence, and human preference margins increase with relation complexity. Controlled ablations connect these gains to graph conditioning, local editing, and image-grounded learning. The resulting policy produces reusable optimized text in one pass after graph calibration, without an iterative critique--rewrite loop.

---


### 30. [Any3R: Feedforward 3D Reconstruction from Any Camera Type](https://arxiv.org/abs/2610.36150)

**<font color=#1a73e8>作者：</font>** Jingong Chen, Qingwen Zhang, Youming Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry foundation models recover camera poses and dense geometry from a set of images with a feed-forward network, but they expect pinhole images. That assumption is inside the backbone too: the positional encoding and the training loss both bind an image position to a direction in space, and both depend on the lens. We condition both on the dense ray field, the unit direction through every pixel, which describes any central camera without a lens type, distortion coefficients or a bound on field of view. Angular coordinates give the rotary encoding the measured ray angle of each patch, evaluated per view, and solid-angle weighting scales the point loss by the area each pixel covers on the sphere, so neither the encoding nor the supervision depends on the lens. Any3R is therefore a feed-forward model that takes any central camera, and is robust to mixing many camera types per scene, with no retraining per lens. On a benchmark of thirteen central cameras across three datasets, where every method reconstructs with its own predicted camera poses, it is the most consistently accurate method. Any3R enables scalable 3D reconstruction from heterogeneous crowdsourced and archival imagery collections sourced across diverse camera types. Project page: this https URL

---


### 31. [Replication or Corroboration? An Axiomatic Framework for Evidential Dependence in Multi-Agent Debate](https://arxiv.org/abs/2610.36151)

**<font color=#1a73e8>作者：</font>** Hoang-Loc Cao, Truong Thanh Hung Nguyen, Phuc Truong Loc Nguyen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In multi-agent debates, matching reports can arise for two different reasons: agents may repeat the same evidence (replication), or they may provide separate evidential roots that support the same claim (corroboration). A judge must distinguish these two cases. Counting report occurrences gives extra weight to relays, paraphrases, alias resubmissions, and excerpt splits, while merging all matching content avoids this only by also removing genuine corroboration. We formalize this tension as a minimal judgment game in which acquiring new evidence is costly, but replication is cheap. We show that root replication invariance (RRI) is exactly threshold-uniform replication immunity. Under RRI, replication-only deviations cannot change the verdict, and positive-cost replication is strictly dominated, whereas occurrence-sensitive and content-keyed judges admit profitable deviations. We also establish an information boundary: if a judge's observation interface cannot distinguish a replica from a matched fresh root, no judge can both ignore the replica and respond strictly to the fresh root. To preserve this distinction, we introduce the lineage quotient, which removes wording, identity, occurrence multiplicity, and arbitrary root names while keeping distinct roots separate. On orbit-connected domains, it is the coarsest representation sufficient for every deterministic judge invariant to replication and root-label renaming. We further lift this construction to quantitative bipolar argumentation frameworks (QBAFs), characterize strict fresh-root response, prove its propagation along sign-consistent paths under DF-QuAD, and derive a tight closed-form response modulus. Exhaustive audits over 28,224 direct-star profiles, 2,052 multi-layer DAGs, with matched interventions on 277 AVeriTeC-derived profiles, show the predicted separation between replication and corroboration under a supplied partition.

---


### 32. [PrinGS: Privacy Preservation in Gaussian Splatting](https://arxiv.org/abs/2610.36168)

**<font color=#1a73e8>作者：</font>** Gaurav Behera, Abhinav Raundhal, Archisha Panda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has rapidly become the preferred representation for high-fidelity novel view synthesis and 3D scene reconstruction. However, the learned representation encodes sensitive visual information including human faces, license plates, documents, and computer screens, raising significant privacy concerns when trained splats are shared or deployed. In this work, we address the underexplored problem of privacy preservation in Gaussian Splatting by proposing a representation-level anonymization framework that directly anonymizes a trained splat. Given a trained splat and a user-provided reference view identifying sensitive content, our method localizes the corresponding regions in the underlying 3D representation and directly anonymizes them, ensuring that the sensitive information is absent from all subsequently rendered novel views while preserving the overall scene geometry and visual fidelity. We achieve this post-training anonymization in less than 1 second. Furthermore, we extend our framework with a privacy-by-design training strategy that prevents sensitive content from being embedded into the representation during optimization, enabling the generation of privacy-preserving splats directly from training images. Our method achieves a remarkably low Face Similarity Measure (FSM) of 9.79% at a retained Face Detection Rate (FDR) of 39.47% and makes sensitive text completely unreadable with an OCR Character Error Rate of 1.00. Our work aims to serve as the primary stepping stone towards privacy-aware 3D representations and motivates further research along these directions.

---


### 33. [Dynamical coarse-graining of neural-network training](https://arxiv.org/abs/2610.36180)

**<font color=#1a73e8>作者：</font>** Lin-Juan Wang, Da Li, Huiling Duan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamical coarse-graining of neural networks gives macroscopic observables and enables training to be predicted, and controlled in a state space far smaller than the parameter space. In this paper, we first define the learning operator following the training law of neural networks and establish a descent theorem for the learning operator, which serves to determine whether the operator is sufficient to characterize the learning dynamics. Then the exact closure theorem and the dynamic coarse-graining theorem are presented in sequence. The three theorems established in this paper provide a systematic framework for constructing and assessing dynamical coarse-grained models of neural-network training. Finally, we demonstrate the applicability of the theorems with a finite-width nonlinear ReLU network. Its dynamic coarse-grained model for a fixed pattern is exactly derived and composed of five independent moments. The model exactly predict the training outputs and evolving learning operator. The framework may also guide the development of approximate coarse-grained models for more general neural networks when exact closure is unavailable.

---


### 34. [Learning Human Sports Motion Feasibility via Quantile Regression on Tracking Data](https://arxiv.org/abs/2610.36183)

**<font color=#1a73e8>作者：</font>** Marc Gutiérrez-Pérez, Antonio Agudo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study time-to-arrival (TTA) in sports: the shortest plausible time a player needs to reach an arbitrary location on the pitch given their current kinematic state, estimated as the lower envelope of observed locomotion times. Rather than modeling space ownership through position density estimation or closed-form physics-based models, we cast TTA as a conditional quantile regression problem, estimating the lower quantile of locomotion time so the model learns a player's lower-envelope arrival time. We train the model on optical tracking data from all 64 matches of the PFF FC FIFA World Cup 2022 dataset, and evaluate a lightweight multilayer perceptron against six player-motion models from the literature, re-expressed as TTA predictors, and a learned reachable- hull baseline. Across our evaluation metrics, the MLP consistently outperforms every physics-based baseline. To probe the generality of the learned locomotion model, we further evaluate it on basketball tracking data and a single-game NFL tracking dataset, analyzing the transferability of player motion dynamics across sports. Our project is available at this https URL.

---


### 35. [Lipi-Ghor: A Large-Scale, Diarized, Multi-Domain Bengali Speech Corpus and a Scalable Pipeline for Building It](https://arxiv.org/abs/2610.36184)

**<font color=#1a73e8>作者：</font>** Sanjid Hasan, A H M Fuad, Risalat Labib 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Bengali, spoken by over 230 million people, remains severely under-resourced in spoken language research. Existing open Bengali ASR corpora are confined to short, read or crowd-sourced speech and lack speaker diarization and long-form audio.
We present Lipi-Ghor, a large-scale weakly-supervised Bengali speech corpus comprising 885 hours of audio sourced from 998 YouTube videos across 596 unique channels, spanning 17 diverse domains including audiobooks, drama, religious sermons, news, and regional dialects. Each recording is annotated in SSTT format (Speaker, Speech, Transcription, Timestamp), which combines automated diarization with Bengali YouTube caption tracks.
To our knowledge, Lipi-Ghor is the first Bengali speech corpus to pair large-scale coverage with speaker-diarized, long-form audio annotations, both of which are absent from existing open Bengali resources. We also present the construction methodology as a replicable pipeline for any language with a sufficient captioned YouTube presence. Targeted channel curation across a handful of rich domains yields corpus scales that were previously out of reach for low-resource languages.
We benchmark four widely-used ASR models under zero-shot and fine-tuned conditions. All four degrade consistently on emotive, dialectal, and long-form content. Because caption targets are noisy, we also release a human-annotated gold evaluation split, verified by 17 volunteer annotators over 30 hours of human-in-the-loop correction and stratified across all 17 domains.
We release our original contributions (video-ID lists, diarization output, pipeline code, and the gold annotations) under CC-BY-4.0, and distribute caption-derived transcripts for research use only; no raw audio is redistributed.

---


### 36. [Frankly Speaking: The Company Election Integrity Keeps in Congressional Communication](https://arxiv.org/abs/2610.36187)

**<font color=#1a73e8>作者：</font>** Michael A. Robinette, Christina Barsky, Amanda D. Clark 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Election integrity is a shared commitment in American politics, but Democrats and Republicans in Congress increasingly mean different things by it. Analyzing 10,420 congressional e-newsletters sent from 2010 to 2025, we examine how the two parties invoke election terms such as ``integrity,'' ``security,'' and ``fraud.'' Using diachronic word embeddings, which track semantic change through how words are used in context, we measure how differently each party uses each term, how much each party shifts, and whether they share nearest semantic neighbors. We show that members of Congress do not need different words to tell different stories about elections. They need only place those same words in different company. Across nearly every term and year, the two parties surround election-integrity vocabulary with entirely different words. That divergence is easy to miss, because most election vocabulary is no more divergent than other words used at roughly the same frequency, and neither party's usage shifted more than the other's. Only a subset of terms grew more divergent, most notably ``certification,'' while ``rigged'' and ``stolen'' entered election discourse after 2020 and polarized there. By 2024, Democrats surround ``voter,'' ``election,'' and ``integrity'' with the language of access and administration. Republicans surround the same terms with ``citizenship verification,'' ``noncitizen voting,'' and ``border security.'' For one party, integrity means protecting eligible voters' ability to cast a ballot. For the other, it means protecting the electoral process from illegitimate ballots. Election officials, who must administer a single system under both definitions, inherit this tension.

---


### 37. [Bayesian Evidence Accumulation for Graph-Based Learning in Dynamic Data-Driven Applications Systems](https://arxiv.org/abs/2610.36190)

**<font color=#1a73e8>作者：</font>** Moises Ponce, Sarah Harkins Dayton, Ioannis Schizas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are widely used in modern machine learning, yet most existing frameworks remain fundamentally static, limiting their applicability in Dynamic Data Driven Application Systems (DDDAS) where observations arrive sequentially under uncertainty. We introduce B-EAGLe (Bayesian Evidence Accumulation for Graph-Based Learning), a probabilistic framework inspired by CBGT-Net (cortico-basal ganglia-thalamic network) that reformulates graph classification as a sequential evidence accumulation process. B-EAGLe combines a GNN encoder with a Bayesian accumulator that incrementally updates posterior beliefs over class labels as new observations arrive, committing to a decision only when sufficient confidence is achieved. Experiments on CIFAR10 demonstrate competitive performance together with principled confidence estimation under sequential observations.

---


### 38. [Beyond the Estimate: Wiener-Informed Decoding for Easier Training of Pixel-Space Flow Models](https://arxiv.org/abs/2610.36192)

**<font color=#1a73e8>作者：</font>** Ziqiao Wang, Yang You  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning velocity fields directly in pixel space is difficult and slow. We show that coarse second-order image statistics can ease this task: frozen Wiener estimates improve velocity learning, with gains extending beyond the linear predictions they explicitly provide. Moreover, we observe similar but complementary gains from frozen bases and pixel decoding. These observations motivate Wiener-informed Decoding (WiD), which uses statistical knowledge both for direct prediction and to organize decoder computation without modifying native blocks. WiD combines a trainable Wiener prediction path with coefficient interfaces that inject features into the native decoder and return its predicted coefficient corrections, with these components initialized with data statistics. All introduced parameters, including the spectrum and coordinate transforms, are trained jointly under the original pixel-space velocity objective. Across model scales and decoder architectures, WiD accelerates training and improves generation quality with modest parameter overhead. It also yields smoother gradient trajectories and remains effective with representation alignment. WiD improves class-conditional and text-to-image generation across different resolutions. On ImageNet 256 x 256, PixelDiT-XL with WiD reaches FID 1.53 after 500 epochs, achieving comparable quality to PixelDiT with 37.5% fewer training epochs. Statistical denoisers contribute beyond the estimate: their computational structure can also ease pixel-space training.

---


### 39. [UT-HMR: Uncertainty-Guided Temporal Modeling for Robust 3D Human Mesh Recovery](https://arxiv.org/abs/2610.36203)

**<font color=#1a73e8>作者：</font>** Zhibo Wang, Sirisha Rambhatla, Yuhao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D human mesh recovery (HMR) remains unreliable under weak observations caused by long camera-to-person distances, occlusion, and motion blur. In challenging scenarios such as sports, these factors make the problem highly ambiguous, as different 3D poses may yield similar 2D projections. This ambiguity is especially severe for one-stage HMR, which recovers all meshes directly from the full image without person crops or external 2D cues. To handle this ambiguity, we present UT-HMR ( Uncertainty-guided Temporal HMR), to our knowledge the first one-stage HMR framework to capture correlated pose uncertainty across joints. Each person query predicts a Gaussian distribution over the full SMPL pose with a compact low-rank-plus-diagonal covariance, which is converted into joint-wise precision weights for heteroscedastic supervision while keeping inference deterministic. Temporal early fusion further injects neighboring-frame evidence before pose decoding, supplying the visual evidence needed to resolve the ambiguity that the uncertainty captures. With a lightweight ViT-B backbone, UT-HMR achieves state-of-the-art results on VIP-HockeyPose-v2 (ice hockey) and WorldPose (soccer), reducing MPJPE, PA-MPJPE, and PVE by up to 4.7%, 3.8%, and 5.6%, and remains competitive on 3DPW against methods with larger backbones and higher input resolutions.

---


### 40. [Concorde: Geometry-Aware Link Prediction via Decoupled Energy Minimization](https://arxiv.org/abs/2610.36204)

**<font color=#1a73e8>作者：</font>** Ege Demirci, Ambuj Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Link prediction remains difficult in sparse graphs, where diffusion heuristics lack connectivity and geometric methods suffer spectral instability when coupling learned representations with diffusion operators. We introduce Concorde, an energy-based framework that resolves this by decomposing link likelihood into three structurally decoupled branches: (i) a parameter-free spectral anchor that establishes permutation-invariant topological stability; (ii) a mixed-curvature residual on a learnable $\mathbb{H}^{d_h}_{c_h} \times \mathbb{S}^{d_s}_{c_s}$ product manifold, regularized by a feature-aware Ollivier-Ricci curvature proxy; and (iii) a continuous vector field on the tangent bundle of hyperbolic space for non-local structural alignment across topological gaps. The branches are fused via learned gating and trained with an N-pair ranking loss aligned with retrieval-style evaluation. Across five benchmarks spanning sparse, dense, featureless, and attributed regimes, Concorde establishes state-of-the-art early retrieval precision, nearly doubling P@10% over leading baselines in sparse settings.

---


### 41. [Bringing Hardware Security Education to All: A Seamless Curriculum Integration Approach](https://arxiv.org/abs/2610.36219)

**<font color=#1a73e8>作者：</font>** Tanvir Hossain, Mahmudul Hasan, Kareem El-Araby 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity education has predominantly focused on software and network security, under the assumption that the underlying hardware is trustworthy. Threats introduced through the global semiconductor supply chain, together with vulnerabilities arising during design and integration, challenge the assumption that hardware can serve as an unquestioned root of trust. Sensor-enabled systems and machine-learning accelerators further expand the hardware attack surface. The undergraduate curriculum of electrical and computer engineering and computer science programs has not evolved accordingly. Core courses cover the design and the functionality of hardware while the security aspects remain overlooked, and dedicated hardware security (HS) courses are elective, scarce, and often restricted to graduate students. At the University of Florida, fewer than 7% of the undergraduate electrical and computer engineering students register for the introductory HS course each year. We present an integrated and economical approach that disseminates fundamental HS concepts within existing core courses through contextual learning. Nine hands-on modules were developed such that each security concept exercises an associated design concept of the core course, as a component of that course and not as a course of their own. Doing the security work is how the student exercises the design topic, so the modules are built to strengthen the host course and not only to add to it. Three were assessed across three offerings of the embedded systems course through one course survey and two conducted by an external evaluator, with 25 respondents. We report what those instruments measured and the limitations of the approach.

---


### 42. [Beyond IceBERT: Open-Data ModernBERT Encoders for Icelandic from 12M to 1B Parameters](https://arxiv.org/abs/2610.36230)

**<font color=#1a73e8>作者：</font>** Hafsteinn Einarsson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> IceBERT, the reference encoder for Icelandic, found that a cleaned web crawl is enough to train a strong model and that starting from a multilingual model can help on some tasks. We revisit both findings with the ModernBERT architecture. We train Icelandic encoders from 12M to 1B parameters on 9B tokens of open data, and rerun IceBERT's benchmarks and five newer tasks for 30 encoders under one protocol with confidence intervals. Our 1B model trained from scratch, to our knowledge the first monolingual Icelandic encoder of that size, is significantly better than IceBERT on all eleven tasks; warm-started from the English Ettin encoder of the same shape, it has the best score of all encoders on every task we rank. Because our model shapes match the English Ettin encoders and the multilingual mmBERT, we can also test the warm start under controlled conditions, at six model sizes and four token budgets. With our vocabulary transplanted, a warm start was never significantly worse than scratch training on the same Icelandic text, and from base size up it was not significantly worse on four tasks than scratch training on 4 times the text (8 times at base and 1B). As models grow, most of the transfer comes from the source model's transformer layers, so even an English source helps. Keeping the source vocabulary instead cost 5 F1 on question answering and nearly three times the compute.

---


### 43. [BehaveRec: When Does Long-Term Behavioral History Help Sequential Recommendation? A Study with Session, History, and Community Signals](https://arxiv.org/abs/2610.36239)

**<font color=#1a73e8>作者：</font>** Aysenur Inan, Reza Yousefi Maragheh, Jayesh Uddhav Kudase 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequential recommendation models typically predict a user's next action from recent session interactions, which limits personalization when short-term signals are weak or ambiguous. Rather than assuming that incorporating longer-term history and community signals is universally beneficial, we study when it actually helps. We propose BehaveRec, a three-signal framework combining a causal session transformer, a bidirectional User History Encoder over a 90-day window, and a GraphSAGE module over a user-user graph built from behavioral embedding similarity rather than item co-occurrence; a learned gate blends the three signals per user. On an industrial dataset of 137M sequences from 12.6M users, BehaveRec improves R@5 by +3.2% over SASRec, with a larger-capacity SASRec baseline (more parameters than BehaveRec) still trailing by +2.5%, ruling out capacity as the explanation. More importantly, a user-level stratification by history length reveals a clear dose-response relationship: BehaveRec's advantage is negligible below roughly 10 interactions and grows monotonically with history richness, reaching +0.017 R@5 for users with 101+ events. This pattern is corroborated across one industrial and three public datasets spanning history-rich to history-sparse regimes, where session-only models remain preferable. These headline results, and the resulting deployment threshold, are established for category-level intent prediction; a preliminary, single-run check on the full item-level vocabulary yields a directionally mixed result and is scoped as an open question rather than a claim. We use these results to derive a practical deployment rule -- roughly 20 interactions per user -- for when long-term history and behavioral-graph signals are worth their added complexity. Despite this added complexity, BehaveRec remains lightweight: it uses 5.67M parameters and trains on a single GPU in under two days.

---


### 44. [Three Worlds for the Price of a Logarithm: Baseline-Protected Best-of-Both-Worlds Combinatorial Semi-Bandits](https://arxiv.org/abs/2610.36245)

**<font color=#1a73e8>作者：</font>** Ting Hu, Luanda Cai, Emmanouil-Vasileios Vlatakis-Gkaragkounis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving on a baseline requires exploring away from it, precisely where its performance may be lost. We propose DUET (Doubling Under Empirical Tests), a horizon-free phased mixing scheme for combinatorial semi-bandits with arbitrary finite action sets. Two observable tests decide when to double the learning weight and when to double the empirical-regret budget and restart. We instantiate the scheme with entropy-FTRL in mixed phases and hybrid-FTRL in pure phases. Assuming the baseline selects every arm with positive probability, this instantiation keeps expected baseline regret logarithmic in $T$, while its expected regret to every fixed action is $\widetilde{O}(\sqrt{T})$ under non-anticipating adversarial losses and polylogarithmic, gap-dependent, under i.i.d. losses with a unique optimal action. All three guarantees hold at every deterministic horizon, and the algorithm knows neither the horizon, nor the gap, nor the environment type. Baseline protection, adversarial robustness, and stochastic adaptivity thus come from one scheme and two base learners, at the price of a logarithm.

---


### 45. [Freeze, Don't Clone: Fine-Tuning with Expressive Policies Without Retaining Offline Data](https://arxiv.org/abs/2610.36247)

**<font color=#1a73e8>作者：</font>** Sami Nur Islam, Johan Obando-Ceron, Doina Precup 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline-to-online reinforcement learning uses offline pretraining to accelerate subsequent online learning. While many methods assume the offline dataset remains available throughout fine-tuning, there are many settings where this is not the case. Prior work attributes failures in this setting primarily to critic recalibration under distribution shift. We identify a complementary actor-side failure: once the offline data disappears, continued behavioral cloning (BC) no longer preserves the offline behavior distribution and instead refits the behavioral model to the agent's limited, and nonstationary, online experience. We demonstrate that stopping online behavioral fitting while preserving the pretrained expressive prior substantially improves no-retention fine-tuning across implicit flow Q-learning (IFQL), flow Q-learning (FQL), and action-chunked RL (QC) on seven OGBench domains. We trace this failure to a behavioral feedback loop: continuing online behavioral cloning rapidly erases the pretrained prior, inducing representational collapse and action diversity loss that starves the critic of useful exploration. Freezing the prior breaks this cycle, preserving offline coverage while allowing value learning to drive continuous improvement.

---


### 46. [Hierarchical Multimodal Interaction Reasoning for Dyadic Relationship Recognition](https://arxiv.org/abs/2610.36249)

**<font color=#1a73e8>作者：</font>** Wang Tang, Fethiye Irmak Dogan, Linbo Qing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dyadic relationship recognition aims to identify the latent social relationship between two individuals from their multimodal interactions. Existing methods typically project heterogeneous cues into a shared representation and optimise a flat classification objective, overlooking that relationships may rely on different interaction patterns. For instance, distant relationships can often be inferred from direct behavioural correspondence, whereas close relationships are better reflected by coordinated affective, behavioural, and multimodal responses. To address this limitation, we propose HiRe-DRR, a Hierarchical Multimodal Interaction Reasoning framework that organises relationship evidence from three complementary perspectives: feature level, interaction type, and relationship hierarchy. HiRe-DRR decomposes facial, bodily, acoustic, and textual cues into low- and high-level representations and constructs homogeneous and heterogeneous cross-participant interactions. We further introduce the Mixture-of-Interaction Transformer (MoI-Former), which treats diverse interactions as specialised experts and employs relation-aware sparse routing to identify relationship-relevant evidence while preserving contextual interaction information. The proposed Hierarchical Conditional Loss (HC-Loss) exploits the hierarchical nature of social relationships through coarse-to-fine supervision, enabling structured relationship reasoning. Extensive experiments on three dyadic relationship benchmarks demonstrate that HiRe-DRR outperforms recent representative image-, video-, and multimodal methods. Our routing analysis further reveals that distant relationships tend to rely on low-level homogeneous interactions, whereas closer relationships focus on high-level heterogeneous interactions. Our code is publicly available at: this https URL.

---


### 47. [What Should an Information Bottleneck Encoder Learn? Separating Representation Learning from Rate Control](https://arxiv.org/abs/2610.36255)

**<font color=#1a73e8>作者：</font>** Hassan Tavakoli, Bella Bose  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The information bottleneck (IB) trades compression of an input $X$ against prediction of a target $Y$ through a multiplier $\beta=1/\lambda$, yet each operating point is usually served by training, or fully conditioning, a new encoder. For jointly Gaussian data, we show that the IB solution factorizes as $A(\beta)=D(\beta)W$: the information-bearing directions $W$ do not depend on $\beta$, and $\beta$ acts only through scalar gains. We ask whether this separation of \emph{representation} from \emph{rate control} survives beyond Gaussian models, treating the budget as a given operating parameter rather than a quantity to be optimized. For a budget-free representation \(F(X)\), the \emph{separation gap} is controlled by the \emph{sufficiency deficit} $\epsilon_F=I(X;Y\mid F(X))$: We show there is at least $\epsilon_F$ in the worst case for finite inputs, and it is bounded uniformly in $\lambda$ by a function of $\epsilon_F$ for finite label alphabets. The same certificate extends to a new target distribution and to pooled multi-domain data, where a conditional-alignment term appears. On MNIST, SVHN, CIFAR-10 and STL-10 (10 seeds, eight prespecified budgets), a frozen CNN representation with one compressor--decoder pair per budget reduces estimated training multiply--accumulate operations (MACs) by $7.7\times$ and wall-clock time by about $2\times$ relative to end-to-end VIBs, and attains higher budget-averaged accuracy ($65.6\%$ versus $57.3\%$ per domain; $67.1\%$ versus $57.1\%$ pooled), with the advantage concentrated at strong compression, where the VIBs collapse. At weak compression ($\lambda\le0.036$), VIB has higher cross-entropy and ECE; its surrogate Lagrangian is higher per domain, indistinguishable from the pooled VIB in the macro average, and lower on the pooled test set.

---


### 48. [Cross-modal Steering Vectors Exist Across Both Image and Text Generation](https://arxiv.org/abs/2610.36269)

**<font color=#1a73e8>作者：</font>** Donghao Zeng, Nishant Subramani, Tamar Rott Shaham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Are concepts and mechanisms unified across modalities in current AI models, or instead implemented separately for each one? We operationalize this broad question of modality unification by studying cross-modal steering: 1) finding vectors that successfully steer generation on tokens of one modality, which then 2) transfer zero-shot to steer generation when added to tokens of another modality. Our study goes beyond simple correlational alignment (e.g. representational similarity) because steering is fundamentally causal. We study cross-modal steering in several unified multimodal models (UMMs), since they possess shared parameters for language and image generation, focusing on these two modalities. Across diverse steered concepts such as emotion and object size, we show that steering vectors transfer zero-shot in both directions (text-to-image & image-to-text). Even for concepts that are highly unique to one modality (e.g. formal vs. colloquial language), steering vectors often induce a consistent, interpretable effect in the other modality, such as formal clothing and design. This transfer has a geometric signature too: despite a clear modality gap separating text and image representations, steering vectors with strong cross-modal transferability tend to point in similar directions for the same concept. Our findings shed light on how vision and language interact inside unified multimodal models and point towards more general, modality-agnostic approaches for controlling their behavior.

---


### 49. [EVA-Flow: Learning Shared Chemistry for Unified Environment-Aware Molecular Conformation Generation](https://arxiv.org/abs/2610.36280)

**<font color=#1a73e8>作者：</font>** Bing Yan, Anuroop Sriram, Zachary Ward Ulissi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular 3D structures underpin simulations of thermodynamics, kinetics, crystallization, and nucleation, making their accurate prediction central to drug discovery and materials design. However, molecular geometry can change dramatically across environments. Existing models either ignore environmental effects or train separate models for each environment. We hypothesize that transfer learning across contexts is possible for conformer generation and that a general model will perform better when training data are limited, as in ligand binding and crystallization. We introduce EVA-Flow, a unified framework for environment-aware molecular conformation generation that learns shared chemical structure and adapts it through environment-conditioned generative modeling. Across vacuum, protein-ligand docking, solvation, and crystal packing, pretraining and cross-environment finetuning provide their largest gains in the three data-scarce settings. Evaluation against multiple reference conformations shows that EVA-Flow covers a broad range of solvation conformations. Analyses of molecules shared across environments support its ability to generate different conformations for the same molecule in different environments.

---


### 50. [Privately Clipping Heavy-Tailed Data](https://arxiv.org/abs/2610.36281)

**<font color=#1a73e8>作者：</font>** Matthew Joseph, Alex Kulesza  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Summing vectors is a basic task in differentially private data analysis. Standard private sum algorithms clip vectors to some bound, sum them, and add noise scaled to the bound. The differential privacy literature has developed a deep library of noise addition mechanisms, but it offers few tools for privately choosing a clipping bound based on the data. We introduce a method that privately chooses a clipping bound by optimizing residual coherence, the directional alignment of vectors exceeding the bound, against the variance cost of additional noise. We prove a close relationship between residual coherence and bias for a general class of heavy-tailed data regimes and show empirically that, across several datasets, our method outperforms existing baselines.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-257](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
