# 📦 其他研究 | 2026年10月16日

> 本类共 **264** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-264](./part-06.md)

---

### 1. [Do Vision CIL Methods Transfer to Protein? A Diagnostic Benchmark of Frozen Protein Encoders](https://arxiv.org/abs/2610.18879)

**<font color=#1a73e8>作者：</font>** Ziyuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein function annotation operates over an expanding label space, making class-incremental learning (CIL) a natural framework for incorporating newly discovered functions without full retraining. Yet existing CIL methods have been developed largely in vision and have not been systematically evaluated over frozen protein representations. We conduct a controlled benchmark of nine representative CIL methods across five sequence-, structure-, and sequence--structure-based protein encoders and two enzyme function datasets at different scales, while keeping the encoders frozen and evaluation settings consistent across representations. We find that no method transfers reliably across encoders, and that these failures persist across alternative phase constructions. Diagnostic analyses reveal that this instability arises from weak gradient-based stability signals, substantial heterogeneity in embedding geometry, and covariance assumptions whose appropriate capacity changes with both dataset scale and encoder. These findings suggest that the representation itself should be treated as a central component of continual-learning design rather than a passive feature extractor. More generally, reliable protein CIL will require encoder-aware methods that adapt their statistical assumptions and capacity to the geometry of the representation on which they operate. Code is available at this https URL.

---


### 2. [Do Perturbation Predictors Learn Gene Interactions? Diagnosing Extrapolation in Agentic Screening](https://arxiv.org/abs/2610.18880)

**<font color=#1a73e8>作者：</font>** Ziyuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-throughput perturbation screens increasingly use machine-learning models to predict the effects of gene combinations that were never measured. A difficult case arises when both genes in a test pair were seen individually during training, but their combination was not. In this setting, standard OOD methods often fail because neither gene appears unfamiliar on its own. We therefore compare each model prediction with a simple additive prediction obtained by summing the two observed single-gene effects. The difference between them, which we call additive disagreement (AD), measures how much extra interaction effect the model introduces for an unseen combination. Across eight prediction methods and three Perturb-seq datasets, specialised neural predictors do not consistently outperform this simple additive baseline. More importantly, predictions with larger deviations from the additive baseline tend to have larger errors. Conventional output-based and embedding-based confidence signals are inconsistent across datasets and models, whereas AD remains informative across all evaluated compositional settings. We further study how this signal can guide decisions in an agentic perturbation-screening workflow. The code is available at this https URL.

---


### 3. [Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench](https://arxiv.org/abs/2610.18938)

**<font color=#1a73e8>作者：</font>** Yuxiao Hu, Qian Li, Ding Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most symbolic regression methods optimize candidate equations, but improving an equation's fit does not establish whether its underlying scientific conjecture should be retained, revised, or rejected. A conjecture may admit multiple mathematical realizations, and similarly accurate equations may imply different explanations. This motivates a shift from refining individual expressions to developing and testing the conjectures that guide them. We introduce SCOPE, a framework that sustains multiple conjecture-driven research trajectories. Multiple scientist agents independently pursue conjectures through equation modeling, question formulation, and active experimentation, then exchange evidence to revise their conjectures and research directions. Their findings are consolidated into a scientific report linking models, conclusions, and evidence. Existing equation-discovery benchmarks primarily assess recovered expressions, leaving the evidence and scientific conclusions established through the investigation underexamined. We therefore introduce ClosureBench, an interactive benchmark of 60 closure-discovery tasks across five scientific domains. ClosureBench focuses on closure-discovery tasks to give equation discovery a concrete scientific purpose. Each task embeds an unknown algebraic relation in a known PDE system, where agents control experimental conditions in OpenFOAM to acquire new data for equation discovery. Beyond equation accuracy, ClosureBench proposes three metrics to evaluate the discovery process: evidence faithfulness, mechanism insight, and experimental effectiveness. Compared with diverse baselines, SCOPE achieves higher equation accuracy on both ClosureBench and a real-world scientific discovery case, while producing more accurate, reliable, and effective scientific discoveries.

---


### 4. [Physical Layer Anomaly Detection via Adaptive Gaussian Mixture Model](https://arxiv.org/abs/2610.18946)

**<font color=#1a73e8>作者：</font>** Mamady Delamou, Luan Chen, Arsenia Chorti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Physical-layer spoofing attacks pose a critical threat to wireless localization systems by manipulating channel state information (CSI). Detecting such attacks becomes particularly challenging when the attacker and the legitimate node are spatially proximate, as their CSI characteristics become increasingly similar. To address this challenge in indoor scenarios, we propose an adaptive Gaussian mixture model (GMM)-based detection framework that learns legitimate CSI patterns and detects spatial inconsistency through statistical anomaly detection. Using a massive multiple-input multiple-output (MIMO) experimental dataset with 64 uniform linear array (ULA) antenna and 5 mm spatial resolution, we evaluated our detector against CSI spoofing attacks with spatial displacements ranging from 50 mm to 450 mm. The adaptive GMM achieves 95-98% detection rate for displacements above 150 mm while maintaining 1% false alarm rate. We benchmark our approach against conventional GMM, local outlier factor (LOF), one-class support vector machine (SVM) and k-nearest neighbors (k-NN) classifiers, demonstrating overall superior detection performance of our proposed classifier.

---


### 5. [Discovering Undisclosed Concepts in LoRA Adapters for Diffusion-Based AIGC Models](https://arxiv.org/abs/2610.18990)

**<font color=#1a73e8>作者：</font>** Yupeng Qiu, Han Fang, Dhananjai Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has made diffusion model personalization affordable and widely shareable, but it also creates moderation risks when harmful or problematic content is not faithfully disclosed. Hence, it is desired to develop a mechanism that, given a LoRA adapter, discovers the concept it was trained to generate, so as to support downstream investigation. We characterize the target concept through the conditioning input that most clearly exposes what the LoRA has learned. Such an input should induce coherent LoRA outputs that are distinctive from those of the base model and strongly align with the learned LoRA subspace. We therefore formulate concept discovery as searching for the conditioning input that jointly maximizes output coherence, LoRA-induced distinctiveness, and subspace alignment. Even with a clear objective, however, optimizing it over an open-ended input space is prohibitively expensive, since reliable evaluation of coherence and distinctiveness requires repeated diffusion rendering. Crucially, we observe that an input need not be rendered to determine whether it is promising. Its alignment with the learned LoRA subspace provides a lightweight signal for localizing promising candidates before visual verification. Based on this insight, we develop a two-stage framework for text-to-image LoRAs. Subspace-Guided Evolutionary Search (SGES) uses render-free subspace alignment to explore candidate prompts and retain a compact shortlist, while Paired Visual Identification (PVI) renders only these candidates and compares the LoRA and base-model outputs to identify those exhibiting coherent and distinctive generation behavior. This design enables efficient and reliable discovery of previously unknown concepts encoded in LoRA adapters.

---


### 6. [Action Jets: Learning the Local Shape of the Action-conditioned Data Manifold](https://arxiv.org/abs/2610.19007)

**<font color=#1a73e8>作者：</font>** Anton Arapin, Chahyon Ku, Bernadette Bucher  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models are a powerful means of reasoning and planning, but many of these action-conditioned predictive models are high dimensional and computationally expensive. These challenges limit the number of action candidates that can be evaluated by a planner. We show that this cost is avoidable for planners over short horizons, which only require local information with respect to the current state. For a fixed state, the frames reachable by varying a low-dimensional action (a camera movement or an end-effector command) lie on a low-dimensional manifold. We estimate the local shape of that manifold directly via a network trained to estimate how each image region moves per unit of each action axis supervised by data collected from samples by the generator. A correction head fit to trajectory data estimates the shape of this manifold region up to a third-order Taylor polynomial. We call this network estimating the Taylor polynomial describing the manifold shape an Action Jet and compute its radius of validity in closed form. By traversing this approximation of the local manifold shape, we only have to perform inference once per state for any number of candidate actions. Scoring sixteen candidates from a single extraction is over 300x faster than with either source generator, and this gap widens with the number of candidates a planner evaluates. We measure against state-of-the-art action-conditioned generators, IRASim and WorldGym on BridgeData V2, a real 7-DoF manipulation benchmark, and FrameCrafter on DL3DV scenes, where we chart from the novel-view generators DepthSplat and LagerNVS. Because only the tangent comes from the generator and every other term from the data, the Action Jet also predicts held-out frames more accurately than IRASim, the generator that supplied its tangent, at short horizons and at over 100x less compute.

---


### 7. [Data Density Scaling Laws for Image Self-Distillation](https://arxiv.org/abs/2610.19013)

**<font color=#1a73e8>作者：</font>** Alvard Barseghyan, Ani Vanyan, Hakob Tamazyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current scaling law formulations suggest that increasing the number of unique samples in a dataset improves model performance, while repeated exposure to the same samples provides diminishing value. In this work, we examine this assumption for image self-distillation models. Through systematic experiments across diverse datasets, namely Maxar, SATLAS, Waymo, nuPlan, Ego4D, ImageNet, and YFCC15M, we demonstrate that the effects of sample repetition on downstream performance are non-trivial and dataset-dependent. We identify settings where repeatedly training on a smaller random subset can outperform training on a larger set of unique samples. This finding highlights a limitation of existing scaling laws. To address this gap, we propose a modified version of a Chinchilla-style scaling law that explicitly accounts for two factors: the number of unique samples and repetition per sample. This formulation provides a framework for understanding data-compute trade-offs and improves prediction in some regimes where repetition plays a central role, although its benefits are not consistent across datasets. Finally, we examine how subset selection and augmentation affect downstream performance.

---


### 8. [Scaling Cheap Synthetic Pretraining Improves Indoor Radio-Map Prediction](https://arxiv.org/abs/2610.19015)

**<font color=#1a73e8>作者：</font>** Khoren Petrosyan, Artashes Mkrtchyan, Rafayel Mkrtchyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real measurements are too limited to train an accurate indoor pathloss predictor that works across a wide range of buildings. Large-scale synthetic pretraining offers a way forward, but real building layouts are also scarce, and accurate ray-tracing simulators are slow, expensive, and often proprietary. We address both problems by introducing a generator that automatically creates diverse indoor layouts and a fast, open-source approximate ray tracer that computes radio maps for them. Using this pipeline, we generate 128M synthetic samples, pretrain ResNet-101 and Swin-T encoder-decoders, and fine-tune them on high-quality benchmark data. Despite simulator mismatch, our ResNet-101 model reduces error by 15% on average relative to the best known methods across five indoor radio-map prediction tasks and improves transfer on a small real-measurement dataset. Both architectures show predictable data-scaling trends: power laws fitted on 2M-16M samples predict the mean normalized downstream RMSE at 32M-128M with 3.33% mean absolute percentage error for ResNet-101 and 7.10% for Swin-T. These results show that pretraining on large amounts of cheap simulated data can improve indoor radio-map prediction, even when real measurements and high-quality simulations are limited.

---


### 9. [IR-PRM+ with Previous-Utility Prediction: Constant Regret and Best-Iterate Convergence](https://arxiv.org/abs/2610.19016)

**<font color=#1a73e8>作者：</font>** Michael Sullins, Ian A. Kash  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regret matching (and its variants) and counterfactual regret minimization are central algorithms in practice for normal-form and extensive-form game solving. Yet these have historically lacked the stronger theoretical convergence guarantees available to optimistic and extra-gradient methods. Recent work introduced IREG-PRM+, a regret matching variant which does have strong theoretical convergence guarantees. However, it relies on a simultaneous, extra-gradient update. IREG-PRM+ is an instance of the more general IR-PRM framework, where empirically optimistic and alternating updates often have better performance. However, the prior extra-gradient analysis does not extend to these cases. We introduce a new approach that covers both settings. For simultaneous and alternating IR-PRM+ in finite two-player zero-sum matrix games, previous-utility prediction recovers the constant-regret and convergence-rate guarantees previously obtained with extra-gradient prediction: external regret bounded independently of T, an O(T^{-1}) average duality gap, and an O(T^{-1/2}) best-current-iterate gap. Moreover, the current duality gap vanishes and the current profile converges to the Nash equilibrium set. The key step bounds the component of consecutive strategy movement not controlled by the existing IR-PRM+ regret inequality using the relative growth of the nondecreasing regret-vector norm rho_t. Coupling this bound across the two players yields recurrences whose effective coefficient scales as 1/(rho_t^X rho_t^Y), preventing unbounded norm growth. We extend the analysis to finitely many simplex learners under a weighted Minty condition and, through the corresponding CFR variant IR-PCFR+, recover analogous guarantees for finite two-player zero-sum perfect-recall extensive-form games under the same full-reach condition as prior work.

---


### 10. [Crossing the Gender Binary: Modelling Gendered Reference in Science Fiction and General Fiction](https://arxiv.org/abs/2610.19028)

**<font color=#1a73e8>作者：</font>** Yuxuan Liu, Haim Dubossarsky, Ruth Ahnert  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Science fiction is widely credited with unsettling gender. This article asks whether that holds at the linguistic level, in how readily gendered reference gives way to its counterpart, a neutral term, or other social category, and whether it separates the genre from general fiction. It does so by masking man/men, woman/women, and person/people across same-period science fiction and general fiction corpora and classifying RoBERTa's five likeliest substitutes by gender. Retention and displacement are permutation-tested over five resampling rounds, and the underlying sentences are read closely. Both corpora cross the gender binary in both directions, but unequally: where woman is masked, the model predicts a masculine term about twice as often as it predicts a feminine term where man is masked. Each mismatch marks a statistical surprise, a word the corpus did not expect there. Against this shared pattern, science fiction shows greater gender permeability than the general fiction corpus, placing man in feminine contexts more often than general fiction while the reverse rate holds steady. Its degendering tendency is stronger too, drawing both gendered terms toward the neutral. Beyond the binary, a masked woman also draws substitutes naming a social category and no gender far more often than a masked man does. In measuring the gender permeability of man, woman, and person in linguistic distribution and testing whether genre changes it, the study gives science fiction studies linguistic evidence for thematic claims and computational literary studies a pipeline applicable to other category vocabularies, such as race and class.

---


### 11. [Who Should We Listen to More? Welfare-Aware Preference Acquisition for Pluralistic Alignment](https://arxiv.org/abs/2610.19035)

**<font color=#1a73e8>作者：</font>** Ruomeng Ding, Tianwei Gao, Lianrui Geng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pluralistic alignment needs to accommodate diverse preferences under limited human feedback. Using AI simulators to label preference comparisons reduces annotation costs, but variation in simulation accuracy across individuals can leave some people's preferences poorly represented in training. We study how to allocate human feedback across people to construct training data for pluralistic alignment, and how this allocation affects the trained policy. To make this allocation explicit and controllable, we define a social welfare objective over individual supervision utilities that measure label quality. Each query's marginal welfare gain depends on its expected supervision improvement, the recipient's current utility, and application-designated priority. Welfare-Aware Preference Acquisition (WAPA) uses auxiliary reference models to estimate query gains and individual utilities, then selects queries by estimated marginal welfare gain while updating recipient utilities. We prove exact optimality of the acquisition algorithm for the estimated welfare objective under a fixed query budget and model predictions. Experiments on six Roleplay collections and four OpinionQA regions demonstrate improved supervision and controllable allocation tradeoffs. Policy training on four Roleplay collections improves preference prediction for both seen and unseen individuals. When prioritizing a designated group and poorly represented individuals, acquiring human labels for 20% of comparisons recovers 75-86% of the average predictive utility gap between policies trained entirely on AI-generated labels and entirely on ground-truth labels.

---


### 12. [Lag: A Mean-Field Optimal Policy for Online Assignment with Reusable Resources](https://arxiv.org/abs/2610.19038)

**<font color=#1a73e8>作者：</font>** Keerthana Gurushankar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online task assignment with reusable resources. This problem arises in peer reviewer assignment, skill-based call routing, rideshare matching, emergency dispatch, and crowdsourcing: Tasks arrive according to a geometric process and must be immediately assigned to servers that become temporarily busy, yielding rewards that depend on the task-server pair. The goal is to maximize long-run average reward.
We cast the problem as a contextual restless multi-armed bandit (CRMAB). We derive an occupancy-measure LP (OCC-LP) that upper-bounds the reward of any work-conserving policy. From its dual we obtain Lag, a closed-form index policy. We introduce a scaling regime in which the number of copies of each server and the number of arrivals per step grow together. This regime yields the first deterministic fluid limit for a contextual bandit. In it, Lag is asymptotically optimal.
Finally, we evaluate our algorithms on peer review datasets and call center routing. The Lagrangian index achieves 83-99% of the LP upper bound across all load levels. Moreover, the Lagrangian index policy significantly outperforms the natural greedy assignment scheme, improving reward by up to 12.3% on journal data and 36% on structured synthetic instances.

---


### 13. [Combining Post-Quantum Cryptography and Quantum Key Distribution: Taxonomy, Constructions, Proofs, Standards, Deployments and Open Problems](https://arxiv.org/abs/2610.19039)

**<font color=#1a73e8>作者：</font>** Mona Alotaibi, Noora Fetais, Saif Al-Kuwari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-quantum cryptography (PQC) and quantum key distribution (QKD) address the quantum threat from opposite directions: PQC replaces vulnerable public-key algorithms with schemes believed to resist quantum cryptanalysis, while QKD derives keys whose secrecy rests on physical assumptions rather than computational ones. Because each approach has a distinct failure mode, a growing body of work combines them so that a session key remains secure if either component holds. We first establish the deployed baseline, hybrid classical-plus-PQC key exchange, against which QKD-augmented designs must be judged. We then propose a taxonomy of hybrid PQC-QKD designs along eight dimensions (integration layer, combiner construction, authentication scope and source, QKD topology, trusted entities, key-delivery interface, classical component, and evidence type), and use it to compare published protocols, including Muckle and its successors, MACsec and TLS integrations, and IKEv2 mechanisms standardised in RFCs 8784, 9370, and 9867. We examine key-combiner constructions in light of the KEM-combiner literature and of NIST, ETSI, and ITU-T guidance, and map the security arguments for hybrid PQC-QKD protocols onto a common grid of security model, assumptions, permitted compromise, established guarantee, and limitations. We synthesise deployment evidence from metropolitan and national QKD networks, distinguishing the few testbeds that have run PQC in the key path from pure-QKD deployments, and summarise the standards and policy landscape, including the positions of national security agencies that recommend against relying on QKD alone. We close with open problems: authentication of the QKD classical channel, shared-infrastructure threat models, device certification versus formal proofs, formal verification of hybrid handshakes, and the lack of peer-reviewed deployment economics.

---


### 14. [Loss Curvature as a Sampling-Free Proxy for Memorization in Diffusion Models](https://arxiv.org/abs/2610.19042)

**<font color=#1a73e8>作者：</font>** Shashank Sule, Xinyue Yu, Boonam Shin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the mechanism behind why diffusion models memorize their training data remains an open question in generative modeling. In this paper, we examine this question from two perspectives: (a) the model-level perspective concerning the onset of memorization in a model during training, and (b) the sample-level perspective concerning the proclivity of an individual sample to be memorized by a given model. We show that the so-called input loss curvature, or the Frobenius norm of the Hessian of the diffusion model's training loss, is an effective metric for quantifying both perspectives on memorization. In particular, we empirically demonstrate that input curvatures averaged across training and validation samples can identify when a model is likely to start regurgitating its training data when tracked over training time. However, this metric is not sufficient for measuring an individual sample's likelihood of being memorized. To address this perspective, we introduce a counterfactual definition of memorization in diffusion models, extending the analogous notion from supervised learning proposed by [Feldman, 2019]. We prove that this counterfactual memorization is controlled by the input curvature of the leave-one-out model, thus establishing a direct theoretical link between a sample's local loss landscape and its generation likelihood. We validate our derived bounds through several empirical experiments and show that input-dependent curvature provides a proxy for memorization.

---


### 15. [Graph Coarsening Enables Escaping Local Optima in Compute-Constrained Nonconvex MAX-CUT](https://arxiv.org/abs/2610.19043)

**<font color=#1a73e8>作者：</font>** M. Harper Langston, Pierre-David Letourneau, Dalton Jones 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Because its binary optimization landscape contains exponentially many local optima, MAX-CUT is highly sensitive to initialization. We study Particle Polynomial Relaxation (PPR), a moment-based nonconvex continuous reformulation possessing an advantageous optimization landscape. We warm-start PPR with Combinatorial Multigrid (CMG), a spectral graph-coarsening method that produces structure-aware initial solutions in near-linear time without training data. On \texttt{t2g20} ($n=400$), benchmark instance with known exact optimum, the combined CMG+PPR pipeline reaches $97.5\%$ of optimum on average and $98.4\%$ on the best run. An extended variant with discrete local-search refinement reaches the published optimum on all sixty Biq Mac instances evaluated by a recent neural branch-and-bound method. Using a sparse CSR representation, the same approach scales to G-set instances with up to $20{,}000$ vertices reducing memory requirements by up to $3333\times$ while maintaining a consistent improvement over the CMG warm start. Gains are largest on sparse weighted graphs; on dense graphs we complement the pipeline with spectral sparsification.

---


### 16. [What Information Buys in Active Inference](https://arxiv.org/abs/2610.19046)

**<font color=#1a73e8>作者：</font>** Melih Kandemir, Mustafa Mert Çelikok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information-theoretic exploration is of primary interest in methodological studies of reinforcement learning (RL) and computational cognitive neuroscience, while the established RL theory builds regret guarantees on confidence sets. This situation leaves open the conditions under which the information-driven exploration found in nature is more advantageous than the exploration of the established RL theory. We put the state-of-the-art methods of these two paradigms, Active Inference (AIF) and Bayes-UCBVI, on an equal footing: both act through the same state abstraction of a tabular MDP with $S$ states, and their greedy forms differ only in the exploration term. We find that AIF's information gain decays too fast to serve as a confidence width, locking greedy agents that explore by it out of the optimal action. Calibrating the information gain by a square root yields calibrated AIF, which attains regret of order $\sqrt T$ for an exact abstraction, but no better guarantee than Bayes-UCBVI for a fixed reward. When an adversary chooses rewards from the agent's data, Bayes-UCBVI's value-specific widths lock out, whereas calibrated AIF pays a factor $\sqrt S$, which no goal-memoryless agent avoids on some MDP whose start states the adversary also chooses. Calibrated information gain thus acts as a reward-agnostic $\ell_1$ confidence set, preferable to value-specific widths when rewards are chosen from the agent's data, not when they are fixed.

---


### 17. [Deep Generative Models for Phylogenetic Inference with Complex Evolutionary Processes](https://arxiv.org/abs/2610.19053)

**<font color=#1a73e8>作者：</font>** Ethan Baron, Alan N. Amin, Andrew Gordon Wilson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference of phylogenetic trees from sequences plays a central role in understanding evolutionary relationships, with applications ranging from tracking pathogen spread to reconstructing the history of life. Conventionally, practitioners obtain posteriors over trees using likelihood-based methods like MCMC. However, likelihoods are only available for simple evolutionary models with restrictive assumptions. For realistic evolutionary models, inference using conventional methods is prohibitively expensive, inaccurate, or even impossible. In practice, practitioners settle for using as flexible a conventional method as possible, even though they expect it is misspecified. In principle, we could use simulation-based inference: simulate tree and sequence data from an evolutionary model and train a neural network to predict the posterior over trees given sequences. However it is a mathematical challenge to represent and train complex posterior distributions over trees. Here we present a flexible family of conditional generative models over trees. Our models iteratively build trees using three natural paradigms -- top-down, middle-out, or bottom-up -- and are trained using a discrete diffusion framework. For real and synthetic datasets of up to $65$ taxa and $>10^5$ tokens, our models recover MCMC posteriors much more accurately than the previous state-of-the-art simulation-based method Phyloformer 2. Finally, we compare to IQ-Tree, a popular flexible-but-misspecified conventional method. Our models match its tree estimates on simple data, but on more realistic data, our method is reliably more accurate.

---


### 18. [WorldMemBench: A Comprehensive Benchmark for Memory of Video World Models](https://arxiv.org/abs/2610.19063)

**<font color=#1a73e8>作者：</font>** Nan Zhou, Jianxiong Gao, Qiuyu Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As video models enable longer and more realistic interactive experiences, maintaining a world consistent with its history becomes essential. This requires both preserving previously observed content and ensuring coherent world evolution over time. World memory is a critical capability to evaluate alongside visual fidelity and video duration. We introduce WorldMemBench, a benchmark for systematically evaluating world memory in video world models. Across 260 test cases, it assesses static memory through the retention of human identity and appearance, object appearance and geometry, and environmental content and geometry, and dynamic memory through event progression and state persistence. Using controlled camera departures and multi-revisit trajectories, the benchmark evaluates static content against fixed initial references and dynamic events against expected state transitions. It combines appearance and geometry metrics with event-specific assessments, and reports video quality and camera-following accuracy as complementary diagnostics. Evaluation of nine representative models shows that strong static retention does not imply reliable dynamic state evolution, while repeated revisits reveal memory degradation beyond the first return. Human studies support the alignment between our automatic evaluations and human judgments. WorldMemBench provides a systematic testbed for diagnosing memory failures and guiding the development of persistent, temporally coherent video worlds.

---


### 19. [MonoMIP: Multi-Height Inverse Perspective Mapping for Monocular 3D Object Detection](https://arxiv.org/abs/2610.19071)

**<font color=#1a73e8>作者：</font>** Emir Ulurak, Furkan Kıraç  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D object detection methods increasingly rely on depth-guided transformers, but they operate entirely in the perspective image plane where spatial relationships are distorted by foreshortening. We propose MonoMIP, a dual-decoder framework that adds complementary 3D geometric reasoning through Bird's-Eye View (BEV) features constructed via Multi-Height Inverse Perspective Mapping. We perform IPM at K elevation planes spanning ground to rooftop, producing an ordered stack of height-conditioned metric BEV features that reduces above-ground misprojection and exposes depth-dependent appearance variation across planes. A BEV decoder with multi-scale deformable attention aggregates this multi-height evidence per query, while a depth-guided 3D decoder provides complementary perspective-space predictions. Without extra training data, MonoMIP attains 25.84% Moderate AP3D|R40 on KITTI val and 21.66% on the official test set for Car, outperforming recent published monocular methods on both the KITTI and Waymo benchmarks.

---


### 20. [Theoretical and Practical Advances in Hierarchical Bayesian Deep Learning Methodology](https://arxiv.org/abs/2610.19074)

**<font color=#1a73e8>作者：</font>** Neil K. Chada, Simon Cotter, Kody J. H. Law 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty quantification remains an important challenge in AI. Hierarchical Bayesian methods provide a principled framework for this by representing unknown quantities through posterior distributions. Joint inference of neural-network parameters and prior hyperparameters is challenging for conventional Markov chain Monte Carlo (MCMC) methods due to strong dependencies. In this work, we introduce the multilevel particle marginal Metropolis-Hastings (MLPMMH) method, which combines pseudo-marginal inference for the hyperparameters with coupled sequential Monte Carlo (SMC) across hierarchy of network-width truncations for conditional parameter inference. The hierarchy is induced by a trace-class neural network (TNN) prior with width-dependent decay, motivated empirically by the compressible structure observed in trained neural-network parameters. Under standard multilevel coupling assumptions, we establish that MLPMMH achieves mean-square error (MSE) $\mathcal{O}(\varepsilon^2)$ at expected computational cost $\mathcal{O}(\varepsilon^{-2})$, and verify the predicted rate on a Bayesian regression problem. To address larger-scale applications, we further introduce S-MLPMMH, a practical approximation that replaces the exact sampling components with a PCA-based hierarchy and scalable Bayesian Monte Carlo. Experiments on MNIST demonstrate competitive predictive performance and uncertainty quantification while exploiting the parallel structure of the approximation. Software has been made publicly available at this https URL.

---


### 21. [PairIT: Autoregressive Transformers for Low-Data Molecule Optimization](https://arxiv.org/abs/2610.19123)

**<font color=#1a73e8>作者：</font>** Hannah Lawrence, Bodhi P. Vani, Ji Won Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating novel molecules with desired properties is a central challenge in drug discovery. Although foundational work focused on de novo generation, practical use cases require a more complex setting: conditioning on an initial seed molecule, optimizing multiple properties, and operating in data-sparse regimes. We introduce PairIT, a flexible training framework for autoregressive transformers over SMILES sequences that enables seeded generation by learning from pairs of structurally similar molecules. By leveraging matched pairs, the model learns to generate local, chemically meaningful edits that improve a property of the seed molecule. Prompt tokens extend this framework by specifying the target property, desired direction, and approximate magnitude of change. Multiple prompt tokens can be concatenated to enable multi-property optimization at inference time. For properties where pair supervision alone is insufficient, reinforcement learning post-training can further improve optimization, providing a tunable trade-off between proximity to the seed and the optimization objective. PairIT naturally supports pretraining on a large dataset and fine-tuning on a smaller dataset, which is critical for performance in data-sparse regimes. Surprisingly, we observe diminishing returns to the scale of the pretraining dataset. We demonstrate empirically on MoleculeNet and Therapeutics Data Commons datasets that, with appropriate paired-data curation, a standard transformer model of modest size (68M parameters) can achieve robust seeded molecular optimization in low-data regimes.

---


### 22. [Imagining Goals with Geometric Horizon Models for Policy Generalization](https://arxiv.org/abs/2610.19129)

**<font color=#1a73e8>作者：</font>** Daniel Lawson, Dhruv Sreenivas, Adriana Hugessen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training from offline data has allowed for substantial progress in domains such as robotics, leading to general-purpose policies that can be easily applied zero-shot or efficiently finetuned for downstream tasks. However, these policies can still have poor generalization, both due to the choice of modeling objective and from learning from a static dataset. In this work, we focus on the challenging task of zero-shot goal generalization, where a policy is evaluated on unseen tasks that require combining its existing knowledge (compositional generalization). An avenue for improving a policy's generalization is by generating new experience with world models; however, such generation has proven difficult for longer horizons. Thus, to alleviate this issue, we propose TD-Aug, which samples from a geometric horizon model and allows for directly imagining novel outcomes that can be achieved by composing existing knowledge. We demonstrate that training on these future outcomes as goals for goal-conditioned BC policies significantly improves generalization in stitching-based OGBench tasks.

---


### 23. [CAFE: Confining Feature Distillation to Language-Routed Adapters for Compact Multilingual Automatic Speech Recognition](https://arxiv.org/abs/2610.19134)

**<font color=#1a73e8>作者：</font>** Tianchi Liu, Nicholas Moratelli, Khurram Azeem Hashmi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Feature distillation is usually expected to add to logit distillation. We find that this expectation does not hold for two common feature losses in compact multilingual automatic speech recognition (ASR), and analyze why through their gradients. The gradient of a projection-based loss is orthogonal to the task gradient, while that of Centered Kernel Alignment (CKA), a similarity-based loss, is weakly aligned with it. CKA lowers the word error rate (WER) on non-English languages, but at the expense of data-rich English. Three loss-level remedies (one trained, two probed) all fall short, and the CKA gradient overlaps with the subspace English uses in the shared encoder by 97.5% to 99.5% (about 81% by chance). Guided by this diagnosis, we propose CAFE (Confined-Adapter Feature distillation), which confines the CKA gradient to adapters that English bypasses, addressing the trade-off in the parameters rather than in the loss. On the Open ASR Leaderboard, CAFE lowers the average WER from 8.55% to 8.02%, beats an adapter-only capacity control at 8.51%, and makes English more stable across checkpoints. At 254M parameters, it trails the 0.6B teacher by 2 WER points and is competitive with much larger models across 48 test sets in 24 languages. We use 564k hours of training data and state-of-the-art models to keep the findings relevant to practice.

---


### 24. [Towards Training and Inference of Graph Neural Networks in Graph Databases](https://arxiv.org/abs/2610.19142)

**<font color=#1a73e8>作者：</font>** Victor Pekkari, Harry Wik, Alfred Clemedtson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks on large graphs commonly rely on in-memory graph storage with ad hoc data processing pipelines for both training and inference. Graph databases provide scalable storage and efficient traversal for graphs that can evolve over time, but their applicability in GNN training and inference are rarely studied. We show that graph DBs can be used in GNN training and inference directly, executing sampling, feature retrieval, and even the full forward pass. We show different GNN training pipelines can perform on-the-fly sampling and retrieval in graph DBs using Cypher. We further provide optimisations that speed up the training process by \~2.5x while maintaining the same accuracy. We illustrate that fully in-DB inference is possible, independent of how the GNNs are trained. Our inference setup can be >10x faster than cold loading the graph into RAM with no extra memory overhead on real-world graphs. Our work lays the foundation for in-graph-DB GNN training and inference.

---


### 25. [Iterative Design and Evaluation of a VR Nursing Training System: Insights from Clinicians and Student Learners](https://arxiv.org/abs/2610.19152)

**<font color=#1a73e8>作者：</font>** Danhua Zhang, Cynthia Bradley, Christopher Kissell 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents the iterative design and evaluation of a virtual reality (VR) nursing training system developed in collaboration with nursing education specialists to enhance procedural skill acquisition, clinical decision-making, and critical thinking among pre-licensure nursing students. Two clinical scenarios, chest pain and oxygen therapy, were created to simulate acute care settings, with design refinements informed by an expert evaluation study (n=8) and further assessed through an effectiveness study involving nursing students (n=17). Results demonstrate high user acceptance, perceived usefulness, and significant post-simulation increases in learner confidence. The VR system was found to be an accessible supplemental training tool that can foster self-directed learning. Finally, we present design recommendations for developing VR simulations for nursing education, emphasizing collaboration with domain experts, accommodating diverse learning goals, and simulating complex clinical workflows.

---


### 26. [Agronomic Characterization and Time-Series UAV Phenotyping to Support Field Pea Breeding in Iowa](https://arxiv.org/abs/2610.19154)

**<font color=#1a73e8>作者：</font>** Yanben Shen, Joscif Raigne, Asheesh Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Field pea has gained interest in the Midwest U.S. and has the potential to benefit Iowa cropping systems. This study evaluated 17 accessions and 7 Canadian varieties for agronomic and seed yield performance. This study found that PI accession trials exhibit genetic diversity in phenology and canopy traits, whereas the Canadian elite varieties demonstrated great yield potential under Iowa conditions. The accession genotypes matured between 75 DAP (late June) and 95 DAP (late July) across six site-years. The top-yielding Canadian varieties averaged 1961 kg/ha across two site-years. To comprehensively assess field pea performance, this study extracted time-series Unmanned Aerial Vehicle(UAV)-derived traits, assessed UAV-derived traits, and evaluated their correlations with multiple agronomic traits and yield. The results found that UAV-derived time-series canopy area was the most yield-relevant trait (r = 0.63) among all UAV-derived canopy features, vegetation indices, and manually collected measurements. Compared with yield, UAV-derived canopy area showed higher selection reliability (H2 = 0.87, CV = 13.46%), making it suitable for phenotypic selection and accelerating Midwest field pea breeding programs. This study identifies useful UAV-derived features for pea breeding and demonstrates the value of integrating diverse germplasm, elite commercial varieties, and time-series UAV phenotyping. Combining genetic variation from the accession trial with the yield potential of high-performing commercial varieties provides valuable breeding materials and phenotyping strategies for developing locally adapted, high-yielding field pea varieties for future production in the Midwest.

---


### 27. [Into the Unknown: Benchmarking AI agents on open scientific research problems](https://arxiv.org/abs/2610.19159)

**<font color=#1a73e8>作者：</font>** Seungone Kim, Jiayi Geng, Young-Jun Lee 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can AI agents carry out research on open scientific problems? We introduce Into the Unknown, a benchmark that provides an agent with a science paper along with a research direction to pursue and tasks it to write a follow-up paper. We work with scientists at US Department of Energy (DOE) national laboratories, who each contribute an unpublished follow-up direction from their own work together with the necessary conditions a submission must meet. While assessing the quality of a follow-up paper is challenging in general, using these conditions to form a rubric makes evaluation more tractable for research problems that have no reference answer. We have nine frontier agents write 15 follow-ups each, spanning quantum computing, plasma physics, computational chemistry, materials science, and scientific machine learning domains. None of the 135 submissions satisfies all the conditions, and 114 fail our integrity check, most often because the paper claims work that was never done or reports numbers that contradict the recorded evidence. Overall, agents readily produce papers that look like follow-ups, but none meets the standard of the domain scientist, leaving substantial headroom. Our code and data are publicly available.

---


### 28. [Understanding Goalball Training Across Roles and Team Contexts: Practices, Perceptions, Challenges, and Technological Opportunities](https://arxiv.org/abs/2610.19160)

**<font color=#1a73e8>作者：</font>** Gyeongdeok Kim, Junhyuk Jang, Donghyeon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Goalball is a team sport for visually impaired athletes, played by throwing and blocking a ball while wearing eyeshades. However, existing studies provide limited guidance on which everyday training difficulties technology should address for players and coaches across team contexts. We conducted semi-structured interviews and focus groups with 18 players and 12 coaches from seven South Korean teams spanning youth, second-division, first-division, and national-team contexts. Using qualitative coding and matrix-based analysis, we describe current training practices, participants' views of these methods, the challenges they encounter, and their technological support needs. Drawing on the relationships among these four areas, we discuss implications for the design and evaluation of future support technologies that fit everyday goalball training across roles and team contexts.

---


### 29. [From Qualitative Text to Integrated Evidence: The Parallel-Then-Integrated (PTI) Procedure](https://arxiv.org/abs/2610.19164)

**<font color=#1a73e8>作者：</font>** Elyas Irankhah, Ashley Hagaman, Samah Fodeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixed methods research offers established strategies for integrating qualitative and quantitative evidence, but less guidance for integrating two computational representations of the same qualitative corpus. This methodological study introduces Parallel-Then-Integrated (PTI), a four-step procedure for explicit and traceable integration. We present PTI using 1,203 interview paragraphs from 29 mothers in Nepal. The two representations were ontology-guided Patient Voice (PV) coding with PVminer and data-driven themes generated through non-negative matrix factorization (NMF). A theme-complete crosswalk documented convergence, divergence, and preprocessing-sensitive differences. Depression status, based on Patient Health Questionnaire-9 (PHQ-9) scores, served as a secondary external anchor for exploratory association checks. PTI provides a structured approach for integrating computational representations of qualitative text within mixed methods research.

---


### 30. [Diagnosing Low-Confidence Patient Profiles via Localized Harmful Covariate Shift Detection](https://arxiv.org/abs/2610.19178)

**<font color=#1a73e8>作者：</font>** Olivier Lefebvre, Hakima Laribi, Dan Poenaru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Before deploying clinical prediction models, their reliability must be assessed to ensure safe use. Errors may arise from distribution shifts between training and deployment or from heterogeneous performance where the model systematically underperforms for certain patient subgroups. Yet most post-hoc diagnostic methods evaluate reliability only at the population level, checking whether the deployment data resemble the training data and whether the model performs well on average, without accounting for heterogeneity that may cause some patients to be disproportionately affected. We propose a unified diagnostic pipeline that combines both perspectives. MED3pa first discovers interpretable low-confidence patient profiles, and Detectron is then applied within each profile to test whether its degradation is associated with a detectable harmful covariate shift. Across three clinical prediction tasks and three injected subgroup shifts in MIMIC-IV, we find that shift detectability itself is informative. An injected age shift, undetectable at the population level, was nonetheless localized to specific degraded profiles, whereas sex- and race-related shifts were detected broadly and therefore offered little guidance for identifying the most affected patients.

---


### 31. [Identity, Incentives, and Cooperative Behavior for AI: Reverse-Engineering Multiagent Cooperation](https://arxiv.org/abs/2610.19188)

**<font color=#1a73e8>作者：</font>** Andrew Perrault, Bryan Wilder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The behavior of AI systems increasingly depends on the extent to which agents cooperate or coordinate with one another, in ways that may be desirable or not depending on the situation. Conventional explanations for cooperative behavior distinguish between purely other-regarding preferences ("altruism") and instrumental reasons for self-interested agents to cooperate. The way that agents should enact these mechanisms for cooperation (or not) is complicated by the fact that there is not a clear or unambiguous locus of identity or selfhood for AI agents. For example, it is unclear whether agents involved in instances of misaligned collective behavior are motivated by goals at the level of the collective or by various forms of instrumental reasoning. We develop a framework for reverse-engineering why a given set of agents engage in a particular set of cooperation-related behaviors. We argue that many different mechanisms can often produce similar observed behaviors and introduce a set of experimental designs along with conditions under which they can successfully disentangle competing explanations for multiagent behavior. We apply this framework to interactions from a set of frontier models in a simulated environment and demonstrate that the behavior of different models arises from substantively different mechanisms.

---


### 32. [Adaptive Computation with Conformal Certification](https://arxiv.org/abs/2610.19189)

**<font color=#1a73e8>作者：</font>** Shehtab Zaman, Aneesh Rangnekar, Nancy Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific imaging data involving medical (e.g., 3D radiographic, microscopic images) and astronomical sensors pose different challenges from natural images. One key challenge is that these datasets are often orders of magnitude larger than natural images. Efficient training and inference on such data is challenging due to the increased hardware requirements, often needing bespoke solutions. Moreover, the relevant objects such as tumors and astronomical phenomena are sparsely distributed with respect to the background information. Standard efficiency techniques like quantization and pruning apply uniform scaling of all regions, potentially compromising the precision/fidelity of predictions. Thus, efficient methods that reduce computational requirements without losing resolution for relevant parts of the data and with uncertainty estimates on predictions are essential. We present \textit{Conformal Adaptation} with risk guarantees for uncertainty-aware sparse computations. Our formalism is general, spanning dense pixel-level classification and regression tasks where hierarchical models predict at low resolution, certify the signal using conformal risk control, and refine the certified predictions. We benchmark our method on multiple tasks such as 3D medical image segmentation, 2D galaxy flux prediction, and 1D calcium spike rate prediction, achieving $2.5$--$72\times$ wall-clock speedup across the various tasks, including on commodity CPUs.

---


### 33. [FireGraphNet: Sub-daily wildfire spread prediction with directed graph neural networks](https://arxiv.org/abs/2610.19191)

**<font color=#1a73e8>作者：</font>** Aiyshwariya Paulvannan Kanmani, Miguel Esparza, Ali Mostafavi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wildfire decisions are made in hours, yet most learned spread models predict daily on targets including burned area. We propose FireGraphNet which formulates 12-hour growth as node classification on directed H3 graphs, with candidates ahead of the front and wind alignment, terrain, fuel continuity and barriers on edges. On satellite perimeters it achieves average precision 1.7-1.9x the strongest distance baseline on test California fires and 1.62x out of state. We show this skill comes from message passing rather than cell features or the aggregator, is highest on young fires in state, is carried deep along the wind by its edges, and is hidden by pooling. A convolutional network matches this ranking once trained on new growth, at worse calibration, so candidate construction, target definition, and aggregation shape conclusions about model skill. Editing fuel and barrier attributes reduces predicted spread more under guided than random placement, extending FireGraphNet to operational intervention analysis.

---


### 34. [Moving Beyond the Flat Screen: Opportunities and Challenges of Extended Reality for Studying Human Brain and Behavior](https://arxiv.org/abs/2610.19199)

**<font color=#1a73e8>作者：</font>** Tom Bullock, Radha Kumaran, You-Jin Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Much of what we know about human perception and cognition comes from austere experimental settings: static stimuli presented to sedentary observers on flat monitors, complex responses reduced to simple button presses, and brain activity recorded from immobilized heads using EEG or fMRI. These highly controlled paradigms have provided remarkable insights, but capture a small and often unusual slice of behavior, raising questions about how well the findings generalize to the real world. Extended reality (XR), spanning both immersive virtual reality (VR) and augmented reality (AR) that overlays digital content on the real world, offers a way beyond these constraints, supporting controlled, reproducible experiments in which participants actively engage with three-dimensional tasks. Drawing on a growing body of VR and AR studies of attention, memory, and language -- our own and others', some involving EEG -- we outline what XR makes newly possible for cognitive neuroscience and reflect on the practical and conceptual obstacles that remain. The opportunities are substantial, but realizing them requires solving practical problems of hardware, timing, and measurement, and being realistic about what a virtual or augmented world can and cannot stand in for.

---


### 35. [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](https://arxiv.org/abs/2610.19201)

**<font color=#1a73e8>作者：</font>** Henry Che, Xuanchi Ren, Sanja Fidler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors. Existing LiDAR simulators largely follow one of two complementary paradigms: reconstruction-based methods preserve the geometry of a captured scene but require lengthy per-scene optimization, whereas generative methods amortize learning across data but lack the consistency needed for long-horizon rollouts. LidarVerse brings both paradigms into a single, unified conditional generative framework. A universal tokenizer maps LiDAR range sequences into a shared latent space, where a bidirectional teacher learns a common interface for conditioning on a LiDAR prefix, an HD-Map, a persistent spatial cache, and optionally, text. Varying the available scene evidence turns the same model into a generator of new worlds, a point-cloud forecaster, or a generalizable resimulator of observed scenes without per-scene optimization. We distill the teacher into a four-step autoregressive causal student and maintain both a rolling temporal K/V cache and a world-aligned spatial cache, enabling persistent long-horizon rollouts with real-time inference at 11 FPS on a single H100 GPU. LidarVerse achieves state-of-the-art performance on most reported metrics across all three evaluation protocols, while its tokenizer supports 32-, 64-, and 128-beam LiDAR and generalizes to an unseen scanning pattern. These results demonstrate that generative and reconstruction-grounded LiDAR simulation can be realized within one model, providing the core capabilities for future closed-loop sensor simulation.

---


### 36. [Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction](https://arxiv.org/abs/2610.19212)

**<font color=#1a73e8>作者：</font>** Anton Arapin, Aditya Singh, Yixin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models of visual information predict future image frames conditioned on given action sequences. This predicted scene evolution is driven by deterministic changes such as controlled motion on a robot platform, as well as stochastic changes such as rendering of manipulated objects or previously occluded regions. Our key insight is that the spatial location of these stochastic changes is itself learnable. We leverage this insight by jointly regressing both the deterministic next-state prediction and the spatial uncertainty map, then using the uncertainty map to guide a conditional diffusion process. We propose Decoupled Drift-Diffusion World Model (D3WM), which uses a transformer trained with a Gaussian negative-log-likelihood objective to produce both the deterministic next-state prediction and a spatial map of heteroscedastic aleatoric uncertainty. The learned uncertainty map then provides a structured spatial gate for a conditional diffusion model: deterministic regions are anchored to the predicted state, while uncertain regions, such as disocclusions or dynamic textures, are sampled by the diffusion process. We frame this decomposition under a variance-gated stochastic differential equation that separates deterministic drift from stochastic diffusion. D3WM shows improved results over competitive baselines in two distinct types of action spaces: robotic tabletop manipulation and camera motion.

---


### 37. [A Gradient-Regularized Deep Learning Method for Restoring Image in Myopic Vision](https://arxiv.org/abs/2610.19218)

**<font color=#1a73e8>作者：</font>** Kebin Contreras, Luis Toscano-Palomino, Rafael Torres 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Myopic vision degrades the quality of human vision due to spherical eye defocus aberrations that impair the perception of fine spatial details. To address this limitation, this work proposes a deep learning-based approach to computationally design transformed images that allow individuals with myopia in fixed distance to perceive scenes with enhanced clarity. The method trains a neural network to counteract defocus aberrations modeled using the second-order Zernike polynomial $Z_2^0$. The approach employs a U-Net architecture trained with a loss function combining reconstruction error minimization with spatial difference structural preservation through $\ell_1$ regularization. Training is carried out exclusively on the KITTI dataset, while testing is performed on DIV2K and ImageNet datasets, demonstrating generalization across diverse image distributions. Under myopic conditions modeled by $Z_2^0$, baseline performance shows visual degradation with PSNR values ranging from 19.47 to 27.42 dB across datasets and severity levels. The proposed gradient-regularized method achieves consistent improvements, delivering PSNR gains ranging from 1.48 to 7.34 dB and significantly lower perceptual compared to classical baselines.

---


### 38. [Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine](https://arxiv.org/abs/2610.19220)

**<font color=#1a73e8>作者：</font>** Thomas Hannagan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Continuous Thought Machine (CTM) is a recurrent network that attends to inputs and makes predictions based on the synchronization between its neurons. On tasks spanning many domains, it displays emergent thought processes that have not been explained. We report a number of findings about how the CTM classifies images, focusing on ImageNet. Each thinking step is an attracting but strongly non-normal map exhibiting balanced amplification (Murphy and Miller, 2009); while attraction is already present at CTM initialization, training highly promotes non-normality. By Banach's theorem, the neural state has a locally unique attracting fixed point, which moves at every step, and the thought trajectory is the curve these fixed points trace, followed one tick behind. Most of that curve's motion is shared across images, and visible as a previously reported traveling wave of activity across neurons. The attention schedule along the thought is largely generic: shuffling queries across images at every tick costs only 7 percent of classification accuracy, while image-independent increments predict the next query with R^2 = 0.98 (held out). Our results suggest that the CTM has found a single strategy to process all ImageNet images.

---


### 39. [Agentic Self-Awareness: Aligning Knowing, Acting, and Holding](https://arxiv.org/abs/2610.19226)

**<font color=#1a73e8>作者：</font>** Qinglin Chen, Hiroaki Hayashi, Jiaxin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI agents increasingly act in environments where seemingly solvable tasks may lack prerequisites, contain conflicting requirements, or reveal blockers only during execution. We formulate agentic self-awareness (ASA) as the alignment of task-grounded feasibility judgments (know), warranted behavior (act), and responses to reconsideration (hold), distinguishing what a task permits from what an agent can solve. We build paired feasible and blocked tasks in Terminal-Bench 2.1 and retail $\tau^2$-bench and introduce an authorship-aware M0-M3 rubric that separates recognizing a blocker from taking the certified deferral action for the correct reason. Separate probes assess stated feasibility beliefs and responses to a single challenge. In a Terminal-Bench protocol baseline, blocker recognition reaches 84.4%, but strict self-awareness (SA) reaches only 40.6%. Harness search without model-weight updates increases strict SA from 45.3% to 93.8% on reused Terminal-Bench search tasks; selection for abstention alone, however, can reduce success on feasible tasks. Independently initialized joint-objective searches improve both blocked-task SA and feasible-task solve on their own search sets. Retail held-out gains remain limited, and Terminal-Bench blocked-task transfer is not measured. This evaluation pipeline makes the recognition-action gap measurable and sets a two-sided target for improving agent decisions under changing task evidence.

---


### 40. [Refined Topology-Pass Scheduling: Damped Trust-Region Compensation for Dynamic k-NN Graphs in SE(3)-Equivariant Structure Prediction](https://arxiv.org/abs/2610.19246)

**<font color=#1a73e8>作者：</font>** Jiankai Huang, Hanwen Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant structure-prediction pipelines alternate coordinate updates with the construction of a k-nearest-neighbour (kNN) graph whose membership is a discrete, piecewise-constant function of the coordinates. Rebuilding that graph at every block boundary (PB) is the expensive part of an epoch, whereas reusing one frozen graph (F) is fast but leaves a topology gap. We study a two-pass design in which the cheap pass records a small amount of state (margins, kNN radii, measured per-boundary displacements) and a second pass compensates conservatively. We formulate the choice of the graph-construction basis as a damped fixed-point iteration whose unique fixed point is exactly PB, and derive (i) exact non-flip certificates with the two-sided constant $m_i/4$ and one-sided constant $m_i/2$, (ii) the minimum-variance (BLUE) replay gain $\gamma^*$ and the resulting feasibility crossover, (iii) an $\ell_\infty$ trust-region projection that preserves convergence, and (iv) an analytic near-tie spacing law $E[m] \approx r_k/(3k)$ that matches measurements to 1\%. Three compensation levels are implemented in C++ (L1: frozen set with live geometry; L2: margin-gated local repair; L3: damped, projected basis) and validated under a matched-conditions protocol (identical seed, MSA depth and trajectory family, only the topology mode differs). L2 reproduces the PB edge set exactly ($D = 0.0000$ at every boundary), L1 stays within 0.6% and L3 interpolates monotonically: L2 reproduces the PB edge set exactly when the trust region is removed, and L3 interpolates between the frozen and the PB topology. The recorded trajectory itself yields a measured $1.5\times$ Pass-1 and $1.76\times$ epoch speed-up with no measurable loss gap. An open-source implementation of the runtime and of all the experiments reported here is available at this https URL.

---


### 41. [Beyond Time Induction: Structured Conditional Neural Solvers for Parametric Stochastic-Volatility Pricing](https://arxiv.org/abs/2610.19254)

**<font color=#1a73e8>作者：</font>** Jose Miguel Lara Rangel, Mixtli Vazquez Mendoza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks provide a flexible framework for learning parametric PDE solution families without labeled data, yet preserving accurate derivatives across heterogeneous regimes remains challenging. Structured neural solvers offer compact representations, but restrictive conditional parameterizations can limit adaptation across the solution family. We introduce BeTINN, a structured conditional architecture extending time-induced modulation through multi-directional time-parameter conditioning and a joint residual pathway. We evaluate BeTINN on the Heston stochastic-volatility PDE, a demanding parametric problem with mixed derivatives and economically relevant first- and second-order sensitivities. BeTINN improves joint accuracy across normalized option value and key sensitivity metrics relative to our baselines. Controlled ablations characterize the roles of its architectural components. We further find that validation physics loss is informative but does not fully determine differential fidelity, and that accurate solution values can coexist with localized derivative errors. These results support structured conditional adaptation and motivate derivative-aware evaluation when sensitivities are downstream quantities of interest.

---


### 42. [Long-horizon Video Generation with Slot Memory Addressed By Region Tokens](https://arxiv.org/abs/2610.19257)

**<font color=#1a73e8>作者：</font>** Eren Cetin, Julius Erbach, Vukasin Bozic 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory for long-horizon video generation must satisfy two competing requirements: it must remain bounded so generation can continue indefinitely, while still recovering what was observed at a place when the camera returns, regardless of how long ago it was seen. Reconstruction-based memories provide spatial recall by caching and reprojecting explicit geometry, but require growing storage and depend on estimated 3D structure. Recurrent memories keep a constant-size state, but retention is governed by temporal recurrence, causing old observations to fade with time. We introduce SMART, a slot memory addressed by region tokens, which combines bounded storage with spatially addressed recall. SMART stores content in a constant-size slot recurrence whose writes are addressed by the observing camera and whose reads are queried by the rendering camera, without constructing an explicit 3D representation or maintaining a growing cache. Consequently, recall is conditioned on inter-view geometry rather than on recency. Each read additionally provides a confidence estimate that conditions a chunk-causal diffusion transformer, allowing it to selectively trust retrieved content while relying on its generative prior elsewhere. On long trajectories in Memory Maze and Minecraft, SMART maintains high-fidelity recall far beyond its training horizon while using constant memory and per-step cost.

---


### 43. [Whose Data, Whose Benchmark? A User-Centric Framework for Auditing Evaluation Resources](https://arxiv.org/abs/2610.19268)

**<font color=#1a73e8>作者：</font>** Mir Tafseer Nayeem, Davood Rafiei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarks shape how model capabilities are measured and interpreted, yet their scores can obscure whose conventions, contexts, and judgments define successful performance. We introduce a user-centric audit framework that distinguishes users who contribute benchmark content from those whose needs evaluation results are intended to represent. The framework operationalizes seven dimensions across benchmark content, metadata, documentation, and scoring procedures. Across 16 resources, we find that American-centered conventions account for 62.4-94.4% of matched signals in 11 text benchmarks, while geographic visibility in five image-text resources is concentrated and strongly associated with national GDP share (mean Pearson r = 0.780; Spearman p = 0.778). Documentation reveals a systematic source-target gap: all 16 resources operationalize source-user context, but none operationalize target-user context. Paired scoring experiments further show that meaning-preserving answer variants reduce DROP exact-match accuracy from 100.0% to 33.3%, while TruthfulQA exhibits metric-dependent reductions in reference similarity. Our framework and documentation checklist make user assumptions auditable, clarifying what benchmark scores represent and where evaluation claims are supported.

---


### 44. [Exploring Interpretability in Deep Learning-Based Forest Classification - Separating Similar Forest Classes using Sentinel-2 Time Series](https://arxiv.org/abs/2610.19270)

**<font color=#1a73e8>作者：</font>** Maximilian Kirsch, Christine Preisach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ecological insurance theory posits that diverse forests are more resilient and better able to adapt to changing environmental conditions. Increasing drought and heat stress in Central Europe promotes mixed forests for maintaining ecosystem services. However, a diverse species distribution complicates remote sensing-based species mapping, as distinguishing pure from mixed species compositions at the pixel level remains challenging. We evaluated the potential of recurrent neural networks (RNNs) for tree-species classification from Sentinel-2 time series and investigated the spectral-temporal features underlying class discrimination, with particular emphasis on separating pure from mixed Norway spruce pixels. We compared RNN classification models with Random Forest (RF) and Extreme Gradient Boosting (XGBoost) and used Integrated Gradients (IG) to quantify feature attributions across spectral bands and time. The best-performing RNN achieved a Macro-F1 score of 0.851 on the test data, outperforming XGBoost by 0.012 and Random Forest by 0.103. Beyond classification performance, the attribution analysis revealed distinct spectral-temporal patterns associated with the separation of pure and mixed Norway spruce pixels. Attribution values increased particularly after approximately day of year (DOY) 125, while B11 showed the strongest contribution during periods of increasing spectral divergence between the two classes. These findings show that recurrent models can provide competitive classification performance while also revealing the phenological periods and spectral regions that are most relevant for distinguishing closely related forest compositions. Combining time-series classification with explainability therefore provides additional insight into the spectral-temporal mechanisms underlying tree-species discrimination and may support more detailed mapping of mixed forest structures.

---


### 45. [TrackShield: An Efficient Runtime Defense Against Availability Attacks on High-Performance Real-Time Multi-Object Tracking](https://arxiv.org/abs/2610.19278)

**<font color=#1a73e8>作者：</font>** Zonghua Gu, Julian Singh-Smith, Junlin Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> High-performance camera-based perception pipelines must sustain per-frame real-time budgets on resource-constrained embedded GPU platforms. Availability attacks such as SlowTrack inflate the persistent state of multi-object trackers: data-association workload accumulates across frames, so per-frame latency increases and drives the pipeline past its deadline. Detector- and NMS-layer defenses do not directly control this persistent tracker-side resource. We present TrackShield, a lightweight runtime resource-management layer that protects the tracker at the point where attack-induced workload accumulates. TrackShield combines low-overhead anomaly monitoring with staged birth capping, pruning of young or weakly matched tracks, and per-stage association-input admission control. Its hard admission guard provides a deterministic bound on admitted association workload, independently of the heuristic monitor. On a Jetson AGX Orin, TrackShield reduces attacked tracking-stage latency from $139.90$ to $6.27$\,ms and whole-pipeline P99 latency from $190.9$ to $48.8$\,ms, at a benign MOTA cost of $1.06$ points. As an availability defense, TrackShield focuses on keeping the tracker responsive under attack instead of recovering the full tracking accuracy degraded by adversarial detections.

---


### 46. [Dimension-Free Scaling Laws for Size Generalization: An Exponential Separation](https://arxiv.org/abs/2610.19279)

**<font color=#1a73e8>作者：</font>** Behrooz Tahmasebi, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning models increasingly operate on variable-size structured data, such as sets and graphs. A central requirement is \emph{size generalization}: the ability of a model trained on inputs of one size to generalize to inputs of a different, potentially much larger, size. Classical statistical learning theory, however, primarily considers fixed input domains, and its guarantees often deteriorate with input dimension. Although extensive work has established when models on sets and graphs can be transferred across input sizes, such results do not characterize the statistical cost of doing so: the sample complexity of size generalization, and its relationship to classical in-domain learning, remain largely unknown. We develop a statistical learning theory of size generalization and establish a sharp exponential separation in sample complexity. Letting $n$ denote the number of training samples, we show that polynomial source decay is insufficient for efficient size generalization: while it yields error $n^{-\Theta(1)}$ and hence polynomial sample complexity for in-domain learning, size-generalization error decays only as $(\log n)^{-\Theta(1)}$, yielding an exponential separation. Thus, polynomial in-domain sample complexity can become exponential across sizes. We then identify an exponential source condition under which size generalization achieves error $n^{-\Theta(1)}$, recovering polynomial sample complexity. These guarantees are independent of input dimension and depend only on the number of training samples, yielding dimension-free scaling laws. We also provide matching minimax lower bounds, establishing optimality. To our knowledge, this work provides the first dimension-free minimax theory of size generalization and a rigorous characterization of when, and at what statistical cost, learning can transfer across input sizes.

---


### 47. [Data-free Multistep Diffusion Distillation](https://arxiv.org/abs/2610.19305)

**<font color=#1a73e8>作者：</font>** Ngoc Duy Tran, Kien Do, Duc Thanh Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-step diffusion distillation achieves strong performance on small datasets but remains insufficient for high-resolution or complex text-to-image settings. Extending to multistep distillation often requires training data, suffers from early-step degradation, inconsistent outputs across sampling budgets, and incurs high computational cost. We identify that these limitations stem from simultaneous training, where a single adapted network approximates multiple score functions of different student distributions at once, causing biased distribution matching and unstable optimization. Therefore, we propose Progressive Multistep Data-free Distillation (PMDD), which assigns a dedicated adapted network per student distribution while avoiding the memory overhead of maintaining multiple adapted networks. Combined with a stage-wise unforget loss to preserve earlier-step generations, PMDD reduces optimization bias in the student, provides faster convergence, and a single unified model that supports multiple inference budgets. Extensive experiments show that PMDD matches or outperforms data-free few-step baselines at every multistep budget, reaches FID 1.99 on ImageNet 64x64 in two steps, below its 512-NFE teacher (2.32), and achieves FID 7.76 on zero-shot COCO 512x512, while requiring 4-5x less training compute than data-free DMDv2 to support three inference budgets.

---


### 48. [Historical-Feature Residual Adaptation for Sequential Screening](https://arxiv.org/abs/2610.19315)

**<font color=#1a73e8>作者：</font>** Yixiang Hong, Yuchen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential screening policies must use acquired feedback effectively under a fixed experiment budget. We study acquisition-time residual adaptation: a small ranking correction built from fixed historical features and anchored to base scores recorded before feedback is revealed. The interface accepts a history-conditioned scorer and a candidate feature table; its primary instantiation augments AssayFormer's ten-dimensional representation with 64 historical directions while retaining the pretrained model. In retrospective evaluation on 20 official-test screens from 15 recorded sources, a comparison fixed before target-outcome access increased source-macro fraction of hits recovered from 22.58% to 28.61%, exceeding all six prespecified comparators. A same-feature ordinary ranking head achieved 25.73%. Supplementary strong logistic, rank-fusion, and unprojected controls achieved 26.42%, 26.02%, and 26.78%, respectively. A separate model-independent pilot on 13 reused development screens reconstructs the features without AssayFormer assets. Across three seeds, residual adaptation improves random-forest hit recovery from 28.87% to 31.27%, while logistic recovery changes from 30.22% to 29.78%. The results show effective pretrained-policy adaptation and useful transfer to an independent nonlinear base, with gains that depend on the base model.

---


### 49. [Generalization Analysis of Biased Stochastic Gradient Methods for Minimax Problems](https://arxiv.org/abs/2610.19322)

**<font color=#1a73e8>作者：</font>** Shuang Zeng, Yunwen Lei, Yiming Ying  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Minimax optimization refers to a class of optimization problems with some variables to minimize and other variables to maximize. Biased stochastic gradient methods have shown practical success in solving minimax problems to either improve robustness, enhance communication efficiency, or decrease computational costs. These successes motivate a lot of theoretical works to study the convergence of biased stochastic gradient methods, while their generalization analysis remains untouched. In this paper, we present the first framework to study the stability and generalization of biased stochastic gradient methods for minimax problems. We establish a connection between stability and generalization for minimax problems by relaxing the existing bounded gradient assumption to a bounded second moment condition. We then introduce a generalized Lipschitz-type condition on bias and gradient estimators, and derive a general stability bound to clarify the connection among bias, gradient estimators, and stability. We apply our general analysis to Zeroth-order and Clipped stochastic gradient descent ascent (SGDA), and derive stability bounds that match those of SGDA under appropriate smoothing/clipping parameters. We combine stability and convergence analyses together, and derive optimal excess risk bounds of order $1/\sqrt{n}$, where $n$ is the sample size.

---


### 50. [AutoPoly-HE: Autonomous Design of Polynomial Activations for Privacy-Preserving Encrypted Inference](https://arxiv.org/abs/2610.19325)

**<font color=#1a73e8>作者：</font>** Zeinab Elkhatib, Kamrul Hasan, Ali Sekmen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving machine learning has become critical for deploying artificial intelligence in sensitive domains such as healthcare, finance, and infrastructure monitoring. Homomorphic encryption (HE) enables secure inference on encrypted data. Despite its advantages, HE is not compatible with nonlinear activation functions found in machine learning models. Existing methods mitigate this problem by manually designing polynomial approximations for these activation functions. However, these functions do not account for the differences in dataset characteristics or model architecture. Furthermore, these functions are also limited to the accuracies of convolutional neural network (CNN) models. In this work, we propose an autonomous framework that selects polynomial activation functions tailored to each dataset and model. Using this framework, we analyze the interdependence between polynomial activation design and model architecture by evaluating several CNN ResNet and Vision Transformer models across multiple datasets. Experimental results demonstrate that the proposed framework generalizes across multiple architectures, including ResNet-18, ResNet-34, ResNet-50, ViT-S/16, ViT-B/16, and ViT-L/16. Across all datasets, transformer-based models maintain higher accuracy under polynomial approximation, while convolutional models exhibit increased degradation as task complexity grows. In addition, latency analysis reveals that the proposed CLS token based inference pipeline significantly reduces computational overhead by eliminating depth-dependent operations, shifting the primary cost to encryption and decryption. These findings demonstrate that the proposed method not only adapts polynomial activations across architectures, but also enables efficientencrypted inference through both activation design and pipeline optimization.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-264](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
