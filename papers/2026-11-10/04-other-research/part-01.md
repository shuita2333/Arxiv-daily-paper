# 📦 其他研究 | 2026年11月10日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

---

### 1. [FasterRW: An Efficient Prior-Assisted Random Walk Solver for Thermal Analysis](https://arxiv.org/abs/2611.08490)

**<font color=#1a73e8>作者：</font>** Zixiao Wang, Tianshu Hou, Chenghan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thermal simulation is becoming increasingly critical in modern IC design and manufacturing. Feynman--Kac random walk methods can estimate localized temperatures without solving the global field, but in practical settings without Dirichlet boundaries they require very long paths to control the truncation residual. This paper presents FasterRW, a continuation-value framework for accelerating Feynman--Kac thermal random walks. We prove a stopping-time residual identity showing that the expected tail after truncation equals the current attenuation weight multiplied by the temperature at the stopping location. This identity enables a prior-corrected single-point estimator: a cheap, noisy prior replaces the unknown continuation value, making the truncation bias scale with prior error rather than absolute temperature and yielding an error-controlled threshold-selection rule. For multi-point queries, FasterRW further converts cross-query pass-through tails into pseudo-samples and refines the resulting observations in prior-error coordinates through kriging. Compared with prior state-of-the-art methods, FasterRW achieves up to $28\times$ acceleration while maintaining accuracy. Our code is open-sourced at this https URL.

---


### 2. [Embedding Consistent Recurrent Neural Networks in Finite Element Simulations for Path-Dependent Damage Prediction](https://arxiv.org/abs/2611.08494)

**<font color=#1a73e8>作者：</font>** Muhammed Adil Yatkın, Mihkel Kõrgesaar, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Capturing sheet-metal localisation physics with a trained surrogate inside a finite element (FEM) solver requires the surrogate to deliver consistent predictions irrespective of the solver's strain-increment count, which is difficult to control in non-linear explicit codes. We address this by re-implementing a trained recurrent neural network (RNN) damage criterion in Fortran and embed it as a live, increment-by-increment fracture criterion inside an Abaqus/Explicit user material subroutine (VUMAT), advancing the network state alongside the solver. Two architectures are compared: a SimpleRNN and the proposed Consistent RNN (ConsRNN), whose transition function is designed so that predictions converge as the strain path is refined rather than drifting with the increment count. Both are trained on bilinear strain paths and evaluated under varying temporal discretisations and nonlinear histories. SimpleRNN predictions drift as the increment count increases, which disqualifies it for embedding; ConsRNN converges under refinement, at a substantial fixed-resolution accuracy cost relative to SimpleRNN on multilinear paths. Deployed at structural scale, the embedded ConsRNN surrogate governs element deletion in a clamped steel plate and reaches the same peak force and peak displacement as an established two-parameter fracture criterion. This pre-peak agreement is expected by construction, since no element is deleted before the peak and the two runs therefore share an identical constitutive path; the responses diverge only on the post-peak softening branch. The results establish discretisation consistency as the decisive property for embedding recurrent surrogates in explicit FEM solvers, and report the first embedding of a customised, non-standard-transition recurrent cell at structural scale.

---


### 3. [Generative Reconstruction of Full-Field Sensor States for Safety-Critical Digital Twins](https://arxiv.org/abs/2611.08499)

**<font color=#1a73e8>作者：</font>** Umme Mahbuba Nabila, Linyu Lin, Majdi I. Radaideh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate reconstruction of incomplete sensor fields is critical for state awareness in safety-critical digital twins (DTs). Thermocouples in high-temperature and radiation environments may drift, fail, or become intermittently unavailable, causing partial observability. This study develops a sparse-sensor reconstruction framework for Oregon State University's High Temperature Test Facility (HTTF) and evaluates six methods under intra- and inter-experiment protocols: three conditional generative models (i.e., a diffusion model [DM], variational autoencoder [VAE], and generative adversarial network [GAN]), two deterministic recurrent neural-network models, and ridge regression. For intra-experiment reconstruction within the PG{-}29 depressurized conduction cooldown (DCC) test, the models combine graph-based spatial encoding with gated recurrent units. The graph neural network (GNN)--gated recurrent unit (GRU) VAE achieves the lowest error, with a mean absolute error (MAE) of $11.73,^\circ$C, a root mean square error (RMSE) of $20.54,^\circ$C, and an $R^2$ of 0.98. The deterministic GNN--GRU and plain GRU obtain RMSE values of $25.26,^\circ$C and $35.22,^\circ$C, respectively, demonstrating the benefit of spatial modeling. All three generative models reduce RMSE by more than half compared with ridge regression. The DM maintains an $R^2$ of 0.94 when known sensors decrease from 91 to 45. For inter-experiment reconstruction, models trained on PG{-}27 pressurized conduction cooldown (PCC) are evaluated on PG{-}29 using section-context conditioning. The section-context DM achieves the best transfer performance, with an RMSE of $42.84,^\circ$C and an $R^2$ of 0.91. These results demonstrate the value of spatiotemporal generative modeling for missing-sensor reconstruction in safety-critical DT applications.

---


### 4. [Adaptive Depth Aggregation in Graph Transformers for Long-Range Graph Reasoning](https://arxiv.org/abs/2611.08500)

**<font color=#1a73e8>作者：</font>** Yifeng Lu, Zhen Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Transformers improve long-range node-to-node communication through global or structure-aware interactions. However, improving cross-node communication does not determine how computations produced at different depths should be combined. Standard residual streams accumulate successive computations with fixed unit coefficients shared across nodes. This fixed aggregation is a residual-interface constraint: once intermediate contributions have been produced, the interface cannot explicitly reweight them by node. We hypothesize that this constraint can create a depth-wise aggregation mismatch when the relative utility of these intermediate contributions varies across nodes and structural contexts. To study this hypothesis, we formalize Graph Transformer residual computation as a causal node-wise history of graph-propagation and feed-forward network (FFN) contributions, making depth aggregation an explicit interface choice. We realize node-adaptive aggregation over this history with Attention Residuals (AttnRes) while preserving the backbone's graph-propagation and auxiliary-state machinery. Block AttnRes reduces the routing cost of long histories relative to Full AttnRes by pooling consecutive contributions. We instantiate the interface in GPS and GRIT and evaluate it on all five ECHO tasks. Both variants achieve lower mean absolute error (MAE) than their independently tuned backbones on every task, and at least one obtains the lowest mean among all compared methods in each task. Routing-only donor-swap interventions support the mismatch hypothesis, while additional ablations examine the key design choices. Together, these results support node-adaptive depth aggregation as a useful complement to cross-node communication in long-range graph reasoning.

---


### 5. [Relic and Gumi: Governing Memory, Safety, and Continuity in Diegetic Relational Agents](https://arxiv.org/abs/2611.08504)

**<font color=#1a73e8>作者：</font>** Daniele Veri'  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Longitudinal relational agents rely on memory for continuity, but remembering can lead to intrusion, clinical overconfidence, emotional manipulation, and opacity. We present Relic, a governance architecture for diegetic relational agents, and Gumi, a subject-specific companion agent initialized and governed through Relic. The architecture separates what the system can observe, what researchers can review, what Gumi can remember, and what Gumi can say.
We describe three mechanisms. Relic represents sensitive safety signals as researcher-facing governance objects rather than user-facing explanations or agent memories. Shared Continuity Memory organizes relational markers around subject-confirmed wording, corrections, explicit follow-up permissions, and recall limits. We specify a runtime mediation layer for delivery, proactivity, session identity, output transformation, and platform allowlists; adoption across live paths remains partial. These mechanisms aim to preserve relational continuity without turning Gumi into a clinical assistant, mood tracker, general-purpose assistant, or opaque profiling system.
We contribute the architecture, object model, researcher workbench design, and a proposed evaluation framework for governed relational memory. An exploratory pilot involved the author as P1 and one external participant as P2. Weekly self-reports from P1 and researcher-led interviews with P2 provide descriptive observations of early use and perceived naturalness. The pilot does not support claims about clinical efficacy, diagnosis, therapeutic outcomes, general usability, or deployment safety. Relic provides research infrastructure intended to make relational memory, safety constraints, and agent behavior inspectable and testable.

---


### 6. [Interpretable Multifidelity Learning with Kolmogorov-Arnold Networks for Spatiotemporal Nuclear Reactor Flow Modeling](https://arxiv.org/abs/2611.08512)

**<font color=#1a73e8>作者：</font>** Meredith Eaheart, Majdi I. Radaideh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity computational fluid dynamics (CFD) simulations of nuclear reactor systems are computationally expensive, motivating machine learning methods that reduce cost while preserving accuracy. Multifidelity surrogate modeling addresses this by combining inexpensive low-fidelity data with limited high-fidelity data. This work investigates whether the high-fidelity data required to predict the spatiotemporal mass flow rate across all 193 fuel assemblies of a pressurized water reactor (PWR) core can be reduced, comparing black-box multifidelity feedforward neural networks (MFNNs) with interpretable multifidelity Kolmogorov-Arnold Networks (MFKANs). Cross-fidelity correlation across the core is weak, making this a challenging multifidelity problem, and neither architecture predicts the transient particularly well in absolute terms. MFKAN nonetheless performs comparably to MFNN for one-time-step-forward prediction while also providing closed-form symbolic equations unavailable with MFNN. To address the scarcity of CFD transients, with only one available per fidelity level, TabDDPM-generated synthetic data was used to augment cross-fidelity forecasting. KAN and FNN achieve comparable self-evaluation accuracy (Pearson correlation of roughly 0.73--0.81), but both perform poorly at true cross-fidelity forecasting (correlations of 0.03--0.06). Assembly-level analysis shows that each assembly's forecast correlation tracks its real cross-fidelity correlation for both architectures ($r=0.840$--$0.896$ for KAN, $r=0.804$--$0.903$ for FNN), confirming that forecasting accuracy is fundamentally limited by how correlated the fidelity levels already are. Overall, KAN-based multifidelity modeling achieves accuracy consistently comparable to MFNN across all settings, while additionally providing symbolic equations that match or exceed the spline representation's accuracy.

---


### 7. [Evolutionary Adaptive Metric Learning: A Multi-Objective Framework for Learning Local Distance Functions in Nearest Neighbor Classification](https://arxiv.org/abs/2611.08549)

**<font color=#1a73e8>作者：</font>** Isaac Touza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nearest neighbour classifiers inherit the geometry of their distance function. Fixed distances and globally learned metrics apply the same geometry throughout the input space, although relevant feature directions may vary across regions. We propose EAML (Evolutionary Adaptive Metric Learning), a framework that learns instance-dependent positive-definite metrics through a low-dimensional parameterization. Each local metric combines an input-dependent diagonal scaling, generated by softmax interpolation between anchor points, with a global low-rank correlation component. A real-coded elitist genetic algorithm optimizes the parameters using a scalar objective combining leave-one-out prediction error, robustness, metric smoothness, and regularization. We establish positive definiteness, metric equivalence, existence of an optimal solution, and Lipschitz continuity of the metric field. We further investigate prediction stability, generalization bounds, and evolutionary convergence under explicit assumptions. Experiments on synthetic data with region-dependent feature relevance show that EAML can recover local metric variations and outperform global metrics. Evaluation on thirteen public datasets using nested 5-fold cross-validation reveals a more nuanced picture: EAML improves performance on selected datasets but does not significantly outperform global metric baselines overall. Additional experiments show that global diagonal metrics can be preferable under nuisance features and test-time noise. These findings identify the conditions under which evolutionary local metric learning is beneficial and highlight its practical limitations.

---


### 8. [Minimum-Sufficient Knowledge and Computation for Wind Energy Predictive Analysis](https://arxiv.org/abs/2611.08558)

**<font color=#1a73e8>作者：</font>** Purbak Sengupta, Aparna S. varde, Emil Jørgensen Njor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Resource-constrained cyber-physical decision systems often apply fixed sensing, knowledge, and computational pipelines despite state-dependent information needs. We introduce Minimum-Sufficient Knowledge and Computation (MSKC), a resource-aware computing principle: select the least-costly route meeting decision-risk and deployment constraints, escalating only when cheaper routes are insufficient. As proof of concept, we isolate adaptive knowledge routing, the decision underlying Knowledge-Guided Machine Learning (KGML), which conventionally injects external knowledge unconditionally rather than only where needed. We instantiate this for wind ramp-event predictive analysis, an edge-oriented decision-support task, evaluating local, relational, and physics-informed routes with a state-aware gate on publicly available real data from two wind farms. We establish conditions for feasibility preservation, cost dominance, and strict expected savings over always-on routing. At a 35.9% relational-knowledge injection rate, adaptive routing is statistically indistinguishable from always-on injection on the reported metrics while reducing knowledge calls by 64%, supporting sustainable, Green-IT-aligned deployment. These results support MSKC's premise that uniformly maximal intelligence is unnecessary. This offers intelligent data analysis for big data streams: the analysis itself decides, per state, how much knowledge and computation the data warrant.

---


### 9. [PINNeval: A Comprehensive Evaluation Standard for Physics-Informed Neural Networks](https://arxiv.org/abs/2611.08559)

**<font color=#1a73e8>作者：</font>** Kevin von Bargen, Hamid Ebrahimy, Tim Römer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Physics-Informed Neural Network (PINN) literature has produced a rapidly expanding catalogue of methods. We divide a PINN training pipeline systematically into four components and observe that many existing benchmarks study these components in isolation. These components are domain-importance adaptation, loss balancing, neural network architecture, and optimization scheme. Moreover, the studies set the surrounding and not considered components of the pipeline to a minimal default that is no longer representative of current best practice approaches. Conclusions drawn under such conditions may not transfer to competitive pipelines. In this work, we propose a new evaluation protocol that (1) treats the four components as an integrated system; (2) crucially requires competitive implementations of the components not under investigation; (3) specifies the metrics and reporting format; and (4) is accompanied by structured documentation that ensures the traceability of evaluations across studies. Based on this comprehensive protocol, we release PINNpipe, an innovative JAX package containing 18 different methods from the current literature as well as nine efficiently implemented benchmark problems. Using PINNpipe, we illustrate our evaluation protocol in relation to established benchmark studies and report results that challenge common assumptions.

---


### 10. [Not All Misalignment Is Alike: A Decomposed Benchmark for Emergent Misalignment](https://arxiv.org/abs/2611.08569)

**<font color=#1a73e8>作者：</font>** Afonso Domingues, Mubashara Akhtar, Bhada Yun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emergent misalignment (EM), in which fine-tuning on a narrow task induces misaligned behaviour on unrelated prompts, has been demonstrated across a wide range of datasets, model families, and training setups. Yet, most studies continue to rely on the evaluation approach introduced in the original EM paper, producing rates that are sensitive to the small set of evaluation questions used, the choice of judge, and the thresholds applied. These evaluations can also conflate misalignment with capability loss and offer little insight into the specific ways misalignment manifests. Differences in datasets, models, and fine-tuning configurations further make findings difficult to compare across studies. We introduce EMERGE, a decomposed benchmark that tracks changes in eight distinct misaligned behaviours from base to fine-tuned models. It evaluates these behaviours on out-of-domain prompts against matched benign controls and tracks capability, coherence, and refusal to account for potential confounders. Applying EMERGE to 8 open-weight models and 13 fine-tuning datasets, we find that models with similar broad misalignment rates can exhibit very different behavioural profiles that a single score cannot capture. We hope EMERGE can help establish a shared and robust standard for measuring EM, making findings more comparable and helping move research from detecting the phenomenon towards understanding it.

---


### 11. [Enhancing Academic Advisement with Case-Based Reasoning](https://arxiv.org/abs/2611.08572)

**<font color=#1a73e8>作者：</font>** Tanat Tonguthaisri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This research involved the study of an application of Case-Based Reasoning (CBR) in the field of academic advising. Academic advisement has been recognised as an important function of higher education. However, there is a widespread desire to improve the advisement services provided by many educational institutions (e.g., colleges and universities) around the world. In the last ten years, CBR expert systems have made important contributions in many domains by applying CBR methodology to a variety of areas of human problem solving. However, to date, expert advisement systems have not been successfully applied to academic advisement, which seems to be a very appropriate domain for this technology.
Academic advising is an important and time consuming task, and different tools and techniques must be used to make it an effective and efficient process. This thesis describes the design, development, and validation of a prototype case-based academic advisement recommender system that supplements the conventional advising process, and could eventually evolve to replace human academic advisors when its full potential is realised.

---


### 12. [HaNDF: Object-Conditioned Geometric Neural Hand Distance Fields](https://arxiv.org/abs/2611.08578)

**<font color=#1a73e8>作者：</font>** Zuhao Liu, Melih Darcan, Zhengdi Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose, HaNDF, object-conditional neural distance fields as data-driven priors for modeling the plausible hand-object configurations, in the product manifold of hand articulations. While recent unconditional generative priors showed success in modeling human pose, hands are versatile articulated bodies often found in interaction with other objects. This makes it crucial to develop a generative prior which can model the plausible hand poses conditioned on the object under interaction. To this end, our HaNDF proposes a geometry-aware, object-conditioned neural distance field, representing the plausible articulations in the zero-level set of a conditional field. We leverage tools from Riemannian geometry to (i) represent plausible hands in the zero level-set of an object-induced neural field, and (ii) project a given pose onto this field. Using HaNDF, we can also optimize for a plausible condition, determining the object under interaction. Our extensive evaluations demonstrate that our HaNDF provides a flexible and powerful prior for hand-object interaction, suitable for applications such as pose refinement, reconstruction under occlusion, and physically plausible manipulation synthesis.

---


### 13. [AutoPYara: Next-Gen YARA Rule Generator for Malware Family Clustering](https://arxiv.org/abs/2611.08608)

**<font color=#1a73e8>作者：</font>** Mabon Ninan, Nhat Nguyen, Soumyajyoti Dutta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Millions of malware variants threaten users daily, such that clustering these samples is key for fast incident response. AutoYara is the current state-of-the-art for automatic YARA rule generation, but the task remains challenging on realistic datasets, where intra-family diversity and noisy clustering can degrade rule quality. We present AutoPYara, a solution armored with: (1) precise cluster centroid selection based on similarity hashing, and (2) an improved heuristic for estimating subclusters within a malware family using historical VirusTotal data. We implement AutoPYara as an open-source Python package (pip install autopyara) to support reproducibility and practical use. We show that AutoPYara, (1) increases rule coverage by 14 percentage points; (2) reduces variance by 7.1 percentage points, comparing the average variance AutoPYara exhibits to that of AutoYara; and (3) improves threat-hunting accuracy by 10%. AutoPYara produces robust and effective YARA rules than prior automatic approaches in practical settings.

---


### 14. [InstaGen: Group-Shared Importance Sampling for Fast Video Generation](https://arxiv.org/abs/2611.08610)

**<font color=#1a73e8>作者：</font>** Kislay Aditya Oj, Kumar Krishna Agrawal, Sri Surya Varma Datla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) are the dominant architecture for video generation, but their quadratic attention complexity results in substantial computational cost and latency. Permuted block-sparse attention (PBSA) offers a promising approach to reducing this cost by selectively computing blocks of a semantically permuted attention matrix. However, existing approaches typically select only the top few key blocks for each query block, following a top-$p$ paradigm. We find that top-$p$ selection can be highly sample inefficient in high-entropy attention regimes, which are common in video generation. In these regimes, we show that sampling can provide substantially better approximations under the same computational budget. More generally, we cast block selection as importance sampling, where the top-scoring keys form an exact set that is computed in full and the remaining keys are represented by a sample drawn in proportion to their estimated attention and reweighted by inverse sampling probability. Building on this formulation, we present InstaGen, which can be parameterized by any PBSA method: it replaces the method's block selection with an exact set plus a weighted sample. Each query cluster draws one sample shared by all its queries, so the sampled keys form blocks amenable to efficient GPU execution. In this paper, we take the SVG family of PBSA methods and show that, on Wan2.1-T2V-1.3B and Wan2.1-T2V-14B, InstaGen parameterized by SVG2 improves PSNR over SVG2 by 3.4 dB and 2 dB, respectively, at matched attention density, and by 1.6 dB and 2.2 dB at matched wall-clock time. On Wan2.1-T2V-14B, InstaGen also beats SVG-EAR by 1.1 dB PSNR at nearly the same density while running faster (1.65x against 1.48x over dense).

---


### 15. [s$^3$: Simple Scaling of Swarms via Cooperative Multi-agent RL](https://arxiv.org/abs/2611.08615)

**<font color=#1a73e8>作者：</font>** Kunal Jha, Gonçalo Faria, Shuyue Stella Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Groups can achieve more than individuals in the same amount of time, but only if their members coordinate: they must decide who works on what and what to share. However, this organization in multi-agent systems today usually comes from arbitrary, static harnesses designed a priori without adapting to agent behaviors or task specifications. We ask whether agents can instead learn to organize themselves. We introduce s$^3$, the first multi-agent reinforcement learning method in which agents decide for themselves how long to work alone and when to share findings or read teammates' messages, with no predefined organization or roles. Our s$^3$ agents learn to take different approaches, read each other's work, exhibit emergent roles that complement each other in the swarm, and generalize to bigger teams. We study both coordination, where agents must combine private information, and parallel exploration, where sharing discoveries can make search more efficient. With matched training and inference budgets, s$^3$, swarms evaluated with twice as many agents as in training solve over 25$\times$ more coordination problems than the strongest baseline, and in exploration, communicating agents reduce repeated work by nearly 50% and outperform best-of-N by up to 9.4 percentage points. Rather than being designed in advance, s$^3$ enables organization to emerge from a shared goal. This opens the door to capable systems built from many models that learn to work together.

---


### 16. [BEVCast: Path-Adaptive BEV for Efficient End-to-End Autonomous Driving](https://arxiv.org/abs/2611.08631)

**<font color=#1a73e8>作者：</font>** Qiren Wang, Mingyu Guo, Zixuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based driving models build a dense bird's-eye-view (BEV) grid and spend the same computation on every cell of it, although the vehicle crosses only a few of those cells within the planning horizon. We present BEVCast, a two-stage BEV whose resolution adapts to the predicted driving path. A coarse pass encodes the whole scene on a grid of 4.096 m cells. A heat head trained on the recorded path assigns a heat to every coarse cell and the cells with the highest heat are refined into 1.024 m cells under a fixed budget. The remaining cells keep their coarse resolution, so the trajectory head reads a mixed-resolution BEV that still covers the entire scene and needs neither an HD map nor a navigation command. Against a full grid of 1.024 m cells with the same architecture and training recipe, BEVCast at a 10% refinement budget encodes 28% of the BEV queries and needs 66% of the BEV encoder time at batch size 1. On nuScenes its mean displacement error is 1.078 m against 1.149 m and its drivable area violation rate is 1.46% against 2.29%. On NAVSIM navtest its mean displacement error is 0.577 m against 0.598 m and its extended predictive driver model score is 82.51 against 81.28. Next to published planners BEVCast reaches a comparable error on both benchmarks without a navigation command. The resolution of a driving BEV can therefore follow the task instead of the grid.

---


### 17. [FinEvolveKG: Controlled and Attributable Prompt Evolution for Financial Knowledge Graph Construction](https://arxiv.org/abs/2611.08643)

**<font color=#1a73e8>作者：</font>** Abhinav Arun, Jayita Bhattacharyya, Fabrizio Dimino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial institutions construct knowledge graphs (KGs) from shared SEC 10-Ks to serve risk analysis, portfolio management, and investment research, whose analytical needs differ. Extraction must adapt without fragmenting shared grounding, typing, and temporal rules. Hand-authored persona prompts and fine-tuning add cost. Weight-free prompt optimization offers an alternative, but unconstrained evolution of a monolithic prompt can rewrite shared rules alongside persona guidance, obscuring changes and complicating review. We introduce FinEvolveKG, a KG-construction harness separating reusable general and persona-policy blocks and mechanically confining GEPA, a reflective prompt optimizer, to the designated block. During persona adaptation, the approved general block remains byte-stable and every optimizer edit is localized to a separately versioned persona policy. A dual objective balances generic temporal-KG quality with persona-relevant facts, motifs, and multi-hop connectivity. We evaluate five mutation scopes on ticker-disjoint 10-K splits, with three seeds for the persona-conditioned arms (v3-v5) across three personas. On the three-seed mean, the complete two-stage block-constrained workflow (v4) improves over the frozen prompt baseline (v1) by 19.4-30.9% and over the tested unconstrained full-prompt workflow (v5) by 2.2-6.4%, leading v5 on both objective components and winning all nine paired-seed comparisons with the lowest seed variance in every persona. Without further optimization, v4 also exceeds v5 across all evaluated out-of-distribution (OOD) shifts. An SME audit supports using the generated triplets as ground truth; a blinded two-SME audit favors v4 over v5 in 70.1% of contrast-enriched judgments. These results show that mechanically attributable evolution can coexist with strong empirical performance, without attributing the gains causally to the boundary.

---


### 18. [From Geometry to Function: A Multi-Task LiDAR Benchmark Dataset for Semantic and Functional Parsing of Urban Facades](https://arxiv.org/abs/2611.08645)

**<font color=#1a73e8>作者：</font>** Abdiaziz Muse, Tooba Javed, Tao Pu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding building facades is central to urban digital twins, heritage modelling, and sustainable city analysis, yet existing LiDAR benchmarks stop at geometry and semantic segmentation and offer little support for reasoning about the functional role of each architectural element. We introduce HFX3D, a large-scale urban facade benchmark of approximately 492 million LiDAR points from 26 buildings in Halifax, Canada, captured across four seasons, day and night, and varied weather. Each facade is annotated at three tiers, semantic, instance, and per-instance functional attributes, making it, to our knowledge, the first facade dataset to pair geometry and semantics with functional labels. Annotations are produced by a semi-automatic pipeline that combines geometry-guided heuristics with expert validation. We benchmark representative point-based, graph-based, convolutional, and transformer architectures and find that semantic segmentation is already challenging under severe class imbalance, while instance separation of repetitive structures and functional reasoning from geometry are substantially harder. The benchmark establishes a new foundation for function-aware 3D urban understanding. Project page: this https URL ; code: this https URL

---


### 19. [An Anatomy-guided 3D Segmentation Pipeline for Prostate Surgical Phantoms from CT Scans](https://arxiv.org/abs/2611.08652)

**<font color=#1a73e8>作者：</font>** Iven Chen, Kuan-I Chung, Ayberk Acar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full autonomy has been a long-term goal in robotic surgery and a near-to-medium-term goal for prostatectomy. Due to the relatively closed structure of the procedure, its standard-of-care robotic/laparoscopic solutions, and procedure economics, prostate procedures are an optimal early target for surgical automation. Prototyping and testing of possible solutions is done in constructed laboratory phantoms, either synthetic tissues or animal phantoms. To enable measurement of perceptual and robotic motion error, phantoms undergo volumetric imaging; these images are critical to both a potential deployed automatic system, used in planning motion and treatment (cutting, ablation, suturing, etc.), as well as post-hoc assessment of system performance. Rapid iteration on these phantom models yields small, inconsistent datasets, while the current workflow for human annotation is often anatomically unreliable and prohibitively time-consuming, rendering deep learning unsuitable at reasonable scales. To address these limitations, we present an automated 3D segmentation pipeline that uses classical medical image-processing techniques to encode the known anatomy of the phantoms as explicit geometric and intensity priors, which requires no training corpus and is transferred to each new phantom revision without re-annotation. Across 57 scans spanning multiple phantom revisions, our pipeline recovers the capsule interior at 0.83 median Dice on 11 contrast-suppressed scans and detects all 32 annotated focal lesions without false positives, completing a full scan in 2-8 minutes on commodity CPU hardware versus 1-2 hours by hand.

---


### 20. [Scoring, Not Learning: Decomposing Catalog-Consolidation Gains in Web-Scraped Retail Product Recognition](https://arxiv.org/abs/2611.08655)

**<font color=#1a73e8>作者：</font>** Kaden Leis, Xiang Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retail product catalogs assembled from web image search are cheap to build and pervasively noisy: queries return packaging shots instead of products, and entries proliferate under names that cannot be distinguished visually. Consolidating such a catalog can look like an alternative to scaling the model. We show this is not a comparison between two ways of improving a recognizer, but between improving a recognizer and changing what counts as correct. We study a public archive of 165,769 cheese images across 1,824 query-named entries. A packaging filter and near-duplicate removal reduce it to a 998-class recognition set on one fixed, group-aware split. Canonicalizing entries to their base type (844 classes) raises top-1 accuracy by 4.0 points. Scoring the unchanged model against the merged label space, by summing its predicted probability within each canonical group, recovers +4.27 points with no retraining (+4.25 over six seeds). Retraining on the consolidated catalog then adds -0.10$\pm$0.53, +0.08$\pm$0.65 and -0.10$\pm$0.65 points at 28, 50 and 88 M parameters, indistinguishable from zero at every capacity ($\pm$ is the across-seed standard deviation). That component is specific, not mechanical: random merges with the identical size profile yield only +0.68 points, and the three backbones agree to within 0.1 points. But it is overwhelmingly category coarsening, not alias correction: across the 37 merged groups, type coarsenings supply 94% of the gain and alias collapses only 7%. We also detect no interaction between consolidation and backbone size: tripling backbone parameters is worth +1.50$\pm$0.57 points on the raw catalog and +1.42$\pm$00.44 on the canonical one, a within-seed interaction of -0.08 [-0.79,+0.63]. On this archive, the reported consolidation gain primarily reflects the evaluation label space, and separating that out costs one evaluation

---


### 21. [Higher Order Component Attribution via Learned Surrogates in High Energy Physics](https://arxiv.org/abs/2611.08656)

**<font color=#1a73e8>作者：</font>** Lauri Laatu, Aritra Bal, Benedikt Maier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Experimental High Energy Physics (HEP) has adopted the transformer architecture for identification of jets, particularly the state-of-the-art Particle Transformer (ParT) which injects explicit information about particle correlations into the attention mechanism. While able to achieve state-of-the-art results in accuracy, interpretability to its effectiveness has been limited. In this paper we propose component attribution methods using Kolmogorov-Arnold Networks (KANs) that directly tie back to the physical descriptors of jets, to probe whether mechanisms such as Multi-Head Attention (MHA), or the ParT architecture, are able to learn these as discriminating features.

---


### 22. [JEPAhead: From Inpainting to Causal Forecasting for Urban Driving](https://arxiv.org/abs/2611.08657)

**<font color=#1a73e8>作者：</font>** Daniel G. P. Petrini, Davi Pincinato, Fabio Grassiotto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We fine-tune a pre-trained V-JEPA1 predictor from bidirectional latent inpainting to action-free causal forecasting while keeping the encoder frozen. Using contiguous past observations, horizon-aligned targets, and group-level causal attention, the model forecasts eight future token groups, corresponding to sixteen frames, in one forward pass. On CARLA Town12, it retrieves the correct future among 591 candidates in 69.0% of cases, compared with 55.3% for persistence, with greater gains at longer horizons and on tokens exhibiting greater change. It also outperforms a compact predictor trained from scratch with six times fewer parameters. Semantic analysis indicates driving-relevant information in predicted features: a fixed linear probe trained on real encoder tokens achieves 0.16 mIoU on patches undergoing semantic-class changes, versus 0.13 for persistence. Vehicle-conditioned retrieval improves over persistence by 15 percentage points at the longest horizon. Pixel-space evaluation shows modest L1 gains but little improvement under LPIPS, motivating direct evaluation through latent and semantic measures alongside an oracle reconstruction reference. These findings support further investigation of latent forecasting for driving perception, while downstream utility remains unverified.

---


### 23. [Transporting the Past: An Optimal Transport View of Backtracking Counterfactuals](https://arxiv.org/abs/2611.08682)

**<font color=#1a73e8>作者：</font>** Zhangyi Liu, Pouria Fatemi, Suvrit Sra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study backtracking counterfactual inference for Structural Causal Models (SCMs) through the lens of optimal transport. In SCMs, a factual observation generally induces a posterior distribution over exogenous variables, making counterfactual inference inherently distributional. We introduce two complementary frameworks that transport this posterior onto the set of exogenous configurations satisfying a desired counterfactual query. The first constructs a natural pointwise projection and is suitable when the transported exogenous distribution can be used directly. The second enforces mutual independence among counterfactual exogenous variables, so that the transported variables remain interpretable as genuine exogenous noises of the same SCM. We show that both frameworks are consistent with the original backtracking counterfactual principle, and we propose marginal, penalty-based, and hard-constrained solvers for finite-posterior settings. Synthetic experiments on non-bijective SCMs illustrate the geometry of the problem and reveal trade-offs among transport cost, counterfactual constraint satisfaction, and preservation of exogenous independence.

---


### 24. [Does a Trading Policy Need to Know What It Trades? Microstructure Invariance and Zero-Shot Transfer of Execution Policies](https://arxiv.org/abs/2611.08701)

**<font color=#1a73e8>作者：</font>** Hieu Tran, Hong Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Execution algorithms are calibrated asset by asset, because the queues, trade rates and bid-ask spreads they face differ by orders of magnitude across assets. For reinforcement learning this is zero-shot generalisation across contexts of very different scales, and microstructure invariance proposes a normalisation fixed by theory: measured in each asset's own units of time, size and price, markets look alike. In an exact order-by-order replay of public Nasdaq data, we train policies once, on 954 stocks in 2019, to choose between waiting in the queue and crossing the spread, and evaluate them unchanged on 1,964 unseen stocks in 2020-21, 2,629 stocks in 2025-26, crypto pairs and a second exchange. First, a policy that sees a stock only through its recent trade rate, trade size, spread and price increment (tick) costs within 0.015 spreads per share (a fifth of what learning saves) of a policy whose training data included the stock, and the stock's own history does not help it; it comes within a similar margin of policies trained on the second exchange when every episode counts equally, and within a wider one on crypto. Second, in mean cost before fees, invariant units beat raw units, z-scores and asset descriptors, but by under a basis point: most of their advantage is information and a common cost scale that a learner can also take as plain inputs, and none of the representations tested extrapolates to unseen spread regimes. Third, a near-zero transfer gap to a pooled comparator is weak evidence that a representation is right: we show that such a comparator detects only a small share of what a poor representation loses, and confirm it in synthetic markets and on pendulums.

---


### 25. [Contextuality and Contradictions: Exploring Real-World Identifications of AI-Generated Writing](https://arxiv.org/abs/2611.08704)

**<font color=#1a73e8>作者：</font>** Michelle Morgenstern, Julia Witte Zimmerman, Tabia Tanzin Prama 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI-generated content spreads into nearly every domain of human interaction, practices and discourses of AI detection, both formal and informal, have become an everyday part of how people interact with text and with each other. In this paper, we explore the real-world practices and discourses of AI identification that have emerged in response to a shifting discursive landscape where the human provenance of a text can no longer be taken for granted. We pair qualitative coding with computational analysis of lexical change, grounded in linguistic anthropological perspectives on language and communication, to investigate AI identifications among English Wikipedia editors and students. We find that these identifications draw on a diversity of evidentiary types, from discrete textual features and judgments about content to circular sense-making claims and presumptions about the author's moral character, and that they are contradictory, dynamic, and contextually dependent. In practice, what often motivates an AI identification is not the presence of any specific textual element, but pragmatic infelicity: a perceived mismatch between the elements present and those deemed appropriate within the text's particular context. Consequently, real-world identifications of AI-generated writing do not merely neutrally point out the perceived presence of "AI-like" features, but can be leveraged as a discursive resource to maintain and define sociolinguistic norms: what can be said in a given context, what is appropriate, and, ultimately, what is human. Further, the design and implementation of systems and tools that treat AI-likeness as a context-free property of text may therefore inherit, and enforce at scale, the norms of whichever contexts they were trained on.

---


### 26. [An Educated Guess: Deriving Statistically Aligned Gradient Estimates for Zeroth-Order Optimisation](https://arxiv.org/abs/2611.08712)

**<font color=#1a73e8>作者：</font>** Justus Huebotter, Serge Thill, Marcel van Gerven 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As novel hardware architectures are explored for the purposes of machine learning, including neuromorphic chips, asynchronous systems, and ASICs, effective learning algorithms are highly desirable. While backpropagation is the standard for differentiation on standard hardware, its requirement for global synchrony and exact differentiability limits the exploration of exotic algorithms on non-traditional substrates and devices. Zeroth-order (ZO) optimisation methods, such as SPSA and weight perturbation, offer a compelling alternative by estimating gradients through inference-only passes; however, these methods have historically suffered due to the `curse of dimensionality', where random perturbations become increasingly misaligned with the true gradient in high-dimensional spaces. In this work, we move beyond blind random noise by deriving zeroth-order search directions from activation geometry available during the forward pass. This leads to a family of Spectral Zeroth-Order methods, SZO-$\kappa$, whose directions solve local response-based gradient-guessing objectives under explicit stochastic assumptions. These methods explore feature-supported directions that are more likely to produce informative loss responses. Using multilayer and convolutional networks, we analyse gradient alignment, bias-variance structure, and training stability of these methods relative to standard perturbation baselines and backpropagation.

---


### 27. [eSharp: Diffusion-based Sharp Monocular Metric Event-to-Depth Estimation](https://arxiv.org/abs/2611.08731)

**<font color=#1a73e8>作者：</font>** Qiushi Dai, Aniket Dashpute, Yuhao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Depth perception is fundamental for autonomous navigation, industrial inspection, and mixed-reality systems. It often operates under strict constraints on power and form factor. In such cases, monocular depth estimation (MDE) is often used. Even as recent advances continue to improve monocular depth quality, conventional frame-based MDE systems remain challenged by fast motion and high-dynamic-range scenes. This work introduces eSharp, an MDE framework that addresses these problems using an event camera. eSharp repurposes pretrained diffusion priors for event-only MDE and produces accurate metric depth with unparalleled sharpness on real data. Real-world event datasets provide only sparse LiDAR depth maps for ground-truth supervision, making dense prediction challenging. We address this limitation through cross-modal distillation, using LiDAR-calibrated dense pseudo-labels generated from a spatially co-registered frame camera to train eSharp. Experiments show that eSharp outperforms prior event-to-depth baselines in both metric-depth accuracy and spatial fidelity, establishing diffusion models as a promising foundation for event-driven 3D perception.

---


### 28. [FishSense Lite: A Camera-Based, Single Laser Hardware Framework with Software System for In Situ Fish Length Measurement](https://arxiv.org/abs/2611.08732)

**<font color=#1a73e8>作者：</font>** Christopher L. Crutchfield, Kyle Hu, Nathan Hui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fish stock assessments need fish lengths paired with species from far more places than trained surveyors can reach. Recreational divers already visit many of those places, but measuring a fish underwater has required trained observers or specialist equipment. We present FishSense Lite, which recovers fish length from a single photograph taken with a recreational dive camera, a dive laser pointer, and a 3D-printed mount. The diver aims the laser at a fish and takes a picture; afterward, the dot's position in the image gives the range to the fish, and the range turns the fish's size in the image into a length. A citizen-science program, trained by the system's builders, taught its own divers and collected lengths paired with species for 73 wild fish across seven open-water dives. On seven wild fish also measured by an underwater stereo-imaging system, the two instruments agreed without detectable bias (mean difference +0.8%). On rigid targets of known length, FishSense Lite recovered every target to within 1.3%, and 99% of 1,055 frames fell within a 15% error budget. From the error sources we measure, we derive a field protocol: calibrate against a dive slate on every dive, photograph fish within 15 degrees of perpendicular and beyond 1 m, and take at least ten frames of each.

---


### 29. [On Differentially Private Mechanisms for Linear Regression](https://arxiv.org/abs/2611.08737)

**<font color=#1a73e8>作者：</font>** Bardiya Aryanfard, Monika Henzinger, Farhood Rostamkhani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the classic least-squares linear regression problem under differential privacy (DP) in the batch and the continual observation setting. In the latter setting, the mechanism receives a stream of $n$ data points $(x_i,y_i)$ ($x_i\in\mathbb{R}^d$ and $y_i\in\mathbb{R}$) and must output an estimate of the optimal parameters at each time step $i$. Although differentially private linear regression has been extensively studied in the batch setting, the problem remains underexplored for the continual setting, with prior work being restricted to constrained linear regression and update time polynomial in $n$.
In this work, we introduce ContinualAdaSSP, the first mechanism for unconstrained linear regression under continual differential privacy. Our mechanism's suboptimality gap is proportional to $\sqrt{d}\operatorname{polylog}(n)$. It requires $O(d^2\log{n})$ space and $O(d^2\log{n}+d^{\omega})$ update time, where $d$ is the dimension of the input space.
We also study fundamental limits of differentially private linear regression by showing the first lower bounds for the box-constrained least-squares linear regression problem. Our lower bounds are proportional to $\min(n,\frac{\sqrt{d}}{\log^{1.5}d})$ for $(1,O(\frac{1}{n}))$-DP, and $\min(n,\frac{d}{\epsilon})$ for $\epsilon$-DP, and are derived using a reduction from a fingerprinting code problem from [Peter et al., 2024], providing new insights into the inherent hardness of this canonical task.
Our experimental evaluation on real-world datasets shows that the accuracy of our continual observation mechanism clearly outperforms any other known differentially private mechanism for this problem such as rerunning the batch algorithm at each time step.

---


### 30. [I Don't Care How You Hide It, I Care What You Do: Runtime Detection of Malicious ML Models](https://arxiv.org/abs/2611.08745)

**<font color=#1a73e8>作者：</font>** Hala Ali, Andrew Case  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pre-trained machine learning (ML) models shared through public platforms can be weaponized to execute malicious payloads during loading or inference. Existing scanners prove inadequate for detecting malicious models as they rely on static analysis and function denylists, support limited serialization formats, and miss attacks that replace denylisted functions with equivalent alternatives, exploit unsupported loading paths, or abuse legitimate framework APIs. To address this problem, we present ModelShield, the first runtime behavioral detection system for malicious ML models that attributes observed system-level behavior to specific model operations. It combines application-level instrumentation of ML framework APIs with eBPF-based syscall tracing, tracking model behavior across spawned threads and processes to separate model-triggered activity from environment noise. Attributed syscall sequences are classified using 195 detection patterns mapped to MITRE ATT&CK techniques. We implemented ModelShield to support 17 ML frameworks and 36 formats. On an independent dataset, it is the only evaluated tool to achieve zero false positives, with false negatives limited to payloads that produce no malicious runtime behavior. It detected all 29 published evasion variants spanning function substitution, loading-path obfuscation, and TensorFlow API abuse, where no existing scanner achieved complete coverage. Across 145,000 models scanned from public platforms, it captured 41 malicious models on Hugging Face, including a reverse-shell payload and a payload that performed host reconnaissance and outbound exfiltration. Among these, ModelScan, PickleScan, Fickling, and ModelAudit detected only 29%, 56%, 80%, and 93%, respectively. Despite runtime overhead, ModelShield has a median analysis time of 12.3 seconds, with 90% of scans completing within 35.5 seconds, making it practical for hub-scale screening.

---


### 31. [Random Symbolic Boosting: A Geometric Approach to Symbolic Regression](https://arxiv.org/abs/2611.08753)

**<font color=#1a73e8>作者：</font>** José R. Ortegaa, José Manuel Muñoz Contreras, Leonardo Trujillo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic models offer interpretability, but their construction through generational evolution can be computationally expensive. This article presents Random Symbolic Boosting (RSB), a method that constructs explicit additive symbolic models via boosting over populations of randomly generated syntax trees, eliminating the need for generational evolution. The idea combines two observations: high-dimensional spaces can be spanned by enough linearly independent vectors, and the semantics of syntax trees can be directly manipulated as such vectors. It is shown that, for Ordinary Least Squares, the boosting process guarantees a monotonic reduction of the training error for both regression and classification. Furthermore, an adaptive geometric early stopping mechanism is introduced. It is based on the angle between the prediction and target vectors, is independent of the problems scale, and requires no adjustments across tasks. Evaluated on a standard benchmark for symbolic regression, the method is located at the Pareto-optimal point between predictive accuracy and training time, ranking first on the real-world datasets. Additionally, it was tested on a large tabular classification benchmark with 200 problems, achieving competitive results.

---


### 32. [Goals as a Representational Layer for Human-AI Collaboration](https://arxiv.org/abs/2611.08757)

**<font color=#1a73e8>作者：</font>** Gaia Molinaro, Lev Tankelevitch, Sean Rintel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Goals are central to how people, teams, and organizations structure their work. Yet, while generative artificial intelligence (AI) systems increasingly operate across a worker's context, information about why a person is pursuing a task, beyond local prompts and interactions, is typically missing. We argue that goals should become an explicit representational layer mediating interactions among people, AI systems, and organizations. Because human goals are hierarchical, partially latent, and dynamically evolving, such a layer must be multidimensional, both grounded in human articulation and inferred from available evidence, and continuously updated. A goal layer could connect immediate requests to broader outcomes, improve the organization and retrieval of relevant context, support reflection and coordination, and provide a foundation for training, aligning, and evaluating AI systems in terms of human-centered outcomes. We highlight these opportunities while identifying open challenges involving goal inference, socio-cognitive frictions, alignment, privacy, and governance.

---


### 33. [MEDALLION: Manifold Embedding Distillation and Attributions for Low-dimensional Latent InterpretatiON](https://arxiv.org/abs/2611.08767)

**<font color=#1a73e8>作者：</font>** Vicky Jung, Claire M. He, Irene Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction is widely used to visualize high-dimensional data and guide scientific discovery, yet interpreting which original features contribute to low-dimensional representations remains challenging, particularly for black-box methods such as t-SNE and UMAP. We introduce \textbf{MEDALLION} (Manifold Embedding Distillation and Attributions for Low-dimensional Latent InterpretatiON), a novel framework for interpreting low-dimensional embeddings through knowledge distillation and neural feature attribution. MEDALLION distills any given embedding with a neural encoder which we explain via a broad range of existing neural feature attribution methods. Through experiments on MNIST and applications in single-cell transcriptomics, we show MEDALLION provides informative feature attributions that cast additional insights into the underlying embedding and compare its performance with existing interpretability approaches.

---


### 34. [Federated training performs as well as centralized for 3D Latent Diffusion for Diagnosis-Conditioned Brain MRI Synthesis](https://arxiv.org/abs/2611.08771)

**<font color=#1a73e8>作者：</font>** Abhijith Shaji, Paul Kurian, Greg Ver Steeg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models of brain MRI are useful to understand brain conditions, and to enrich scarce and imbalanced neuroimaging data. However, training these models requires large, multi-site training sets, which is challenging. Federated learning (FL) allows for training deep learning models without sharing data. We show that training a 3D conditional latent model federatedly (where data is kept private at each site) performs similarly to centralized training (where all the data have been copied to a single site). We evaluate three metrics: conditional fidelity (how well generated MRIs perform in classification), diversity (how the generated images match the real data distribution, using MultiScale-SSIM), and realism (how close generated images are to real images, using Fréchet Inception Distance). Our results show that federated training is a viable route to develop multi-site generative models of brain MRI.

---


### 35. [Gain-Dependent Entropy Characterization of a Zener Avalanche Noise TRNG via Dual NIST Standards: Toward Low-Cost Hardware Entropy for ICS Deployments](https://arxiv.org/abs/2611.08774)

**<font color=#1a73e8>作者：</font>** Rishabh Das  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> True random number generators based on Zener avalanche noise offer a low-cost entropy source for industrial control system and IoT edge devices, yet the relationship between amplifier gain, coupling capacitance, and entropy quality remains uncharacterized under current NIST standards. This paper presents a comprehensive entropy assessment of an op-amp-based Zener avalanche noise generator across five gain configurations and two coupling capacitor values, evaluated against the NIST SP 800-22 statistical test suite and the SP~800-90B entropy source assessment using 1.44 billion raw bits per configuration. We identify a three-phase autocorrelation structure, attributed to comparator saturation-recovery dynamics, consistent across all gain settings. A direct-current substitution experiment, replacing the Zener diode with a stable voltage source at the same bias point, reduces switching activity by approximately 97%, confirming that Zener avalanche noise, rather than amplifier self-excitation, is the necessary entropy source. The coupling capacitor is further shown to govern comparator overdrive and entropy quality independent of this source mechanism, with the smaller capacitance improving entropy, throughput, and bias. The combined results identify an optimal gain configuration achieving a perfect statistical test score, NIST-compliant min-entropy, and peak entropy throughput at a bill-of-materials cost under five dollars, offering practical design guidance for low-cost entropy sources in industrial and embedded deployments.

---


### 36. [On Lipschitz Explosion in Deep Neural Networks with Normalization: Consequences for Optimization and Adversarial Robustness](https://arxiv.org/abs/2611.08775)

**<font color=#1a73e8>作者：</font>** Ashkan Soleymani, Reyhaneh Hosseinpourkhoshkbari, Hadi Daneshmand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a network look stable at every layer and still be exponentially unstable as a whole? The Lipschitz constant of a neural network is a basic stability quantity appearing in optimization guarantees, generalization bounds, and robustness certificates. Deep networks naturally admit two such notions, input Lipschitzness, measuring sensitivity to data perturbations, and parameter Lipschitzness, measuring sensitivity to weight perturbations. We prove that, for deep networks with normalization layers, with batch normalization as the canonical example, both Lipschitz constants can grow exponentially with depth and hence with parameter dimension, even under strong per-layer norm control such as $\|W_\ell\|_2\le 1$, and already for linear activations. Thus, a mechanism widely used to stabilize training can create severe worst-case instabilities that are invisible locally, i.e., from layerwise norm bounds alone. Parameter-Lipschitz explosion turns Lipschitz-dependent nonsmooth optimization guarantees into exponential-in-dimension bounds for deep normalized networks, while input-Lipschitz explosion makes worst-case Lipschitz-based generalization and robustness certificates vacuous. The latter also yields a concrete rank-separation mechanism for adversarial vulnerability. The theory predicts that perturbations introducing new singular directions should be amplified much more strongly than perturbations at the same noise level that remain within the input's original singular subspace. Experiments on MNIST, Fashion-MNIST, and CIFAR-10 support this prediction, showing that rank-creating perturbations cause substantially sharper drops in accuracy, confidence, and margins than same-subspace perturbations.

---


### 37. [Semantic Conditional Similarity (SCS): A Formal Mathematical Framework](https://arxiv.org/abs/2611.08778)

**<font color=#1a73e8>作者：</font>** Mehmet Murat Albayrakoğlu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic Textual Similarity (STS) operates on document pairs, returning a single scalar per comparison. In a multi-document setting where several sources may have contributed to one or more targets, pairwise STS cannot disentangle each source's marginal semantic contribution from their shared vocabulary. In this paper, Semantic Conditional Similarity (SCS) is introduced as a conditional form of STS that computes similarity between two documents after eliminating semantic elements shared with a third via set-theoretic operations. SCS makes four contributions: 1) it introduces directionality, partitioning pairwise relations into lateral (inter-source) and vertical (source-to-target) classes; 2) conditioning induces role-dependent asymmetry by extending the comparison domain from unordered pairs to ordered, conditioned triples of a target, a reference, and a conditioning document; 3) SCS introduces inter-document conditioning by subtracting shared content from a third document, complementing the intra-document conditioning in recent C-STS work; and 4) the set-theoretic decomposition achieves threshold-free partitioning of shared and residual content, requiring no arbitrary similarity cutoff. Although developed for the $n \to 1$ configuration, the framework extends to $1 \to n$ via vertical role reversal and to $m \to n$ via independent composition of source- and target-side conditioning. With the established $1 \to 1$ case, these span the full spectrum of document cardinality. SCS scores should be interpreted ordinally, as rankings of marginal contributions rather than absolute measurements. The broader implication is that metric space axioms commonly assumed in similarity formalizations constrain expressiveness in role-differentiated multi-document settings, and that extending the domain to conditioned triples can recover information that pairwise-symmetric comparisons suppress.

---


### 38. [Aligning, Fast and Slow: A Control-Theoretic Oversight Framework for Long-Horizon Trajectories and Maintained Deployments](https://arxiv.org/abs/2611.08781)

**<font color=#1a73e8>作者：</font>** Stephen Peng, Vineet Jagadeesan Nair, Noah Broestl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can pass checks on individual tasks while retaining memory or code changes that alter their later behavior. We introduce a control-theoretic framework that couples a fast loop controlling proposed actions with a slow loop reviewing persistent changes and reassessing configurations after model or tool updates. When measurement errors and changes between checks are bounded and controllers can enforce their decisions, we derive a deployment-level bound and a rule for dividing review effort. In simulation, dividing a fixed review budget between both loops reduces mean maximum departure from intended behavior roughly twelvefold compared with review confined to individual runs. In coding stress tests with authored memories and five matched seeds, combined controls reduce mean severity on a 0-3 scale from 0.325 without gates to 0.117, resolving 33 of 120 issues versus 35 without gates; in trading stress tests, combined controls reduce mean shortfall in low-emission purchases from 0.892 without gates to 0.107. The overall framework helps developers and auditors compare and enforce oversight designs, while the agent studies test component controls rather than the full deployment-level guarantee.

---


### 39. [Extrapolation Matters: Sparse-Only Depth Completion Beyond LiDAR Coverage](https://arxiv.org/abs/2611.08782)

**<font color=#1a73e8>作者：</font>** Maximilian Jansen, Gasser Elazab, Praveen Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extrapolation beyond LiDAR coverage is an important yet under-evaluated challenge of depth completion. In real camera--LiDAR systems, partial sensor overlap, occlusions, and limited field coverage often leave large image regions weakly observed or completely unobserved by LiDAR. Thus, we investigate depth completion in this beyond-coverage regime using only sparse supervision from raw single-sweep LiDAR, without dense depth labels, LiDAR accumulation, or pseudo-LiDAR generation. Our approach leverages a frozen monocular depth foundation model, lightweight per-frame alignment to sparse LiDAR geometry, and a refinement module that fuses the aligned prior with sparse LiDAR anchors to predict dense metric depth. To regularize learning under raw sparse supervision, we introduce a high-frequency normal-consistency loss defined as the image-space gradient of the per-pixel normal cosine discrepancy. This term penalizes spatial variation in scalar angular error; it does not directly match changes in neighboring normal vectors. We further introduce an evaluation protocol that explicitly separates LiDAR-supported and beyond-coverage regions, revealing extrapolative behavior that conventional depth-completion metrics can obscure. Our method achieves strong depth accuracy beyond LiDAR coverage while remaining competitive in LiDAR-covered regions, providing a practical way to deploy monocular foundation priors in multi-sensor systems.

---


### 40. [Training Stability under Adaptive Curricula](https://arxiv.org/abs/2611.08787)

**<font color=#1a73e8>作者：</font>** Johan Obando-Ceron, Walter Mayor, Michael Dennis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised Environment Design (UED) approaches train reinforcement learning (RL) agents on diverse curricula that may evolve with their capabilities. While prior work has largely focused on how these curricula are constructed, we study whether their students remain trainable under the resulting distributions. Across multiple UED mechanisms, environment complexities, and extended training horizons, we identify recurring learner-side pathologies, including parameter growth, degraded value--outcome ordering, and loss of representational diversity, that accompany stagnation and performance degradation. These findings connect limitations in UED to optimization failures previously identified in conventional deep RL, while showing how adaptive curricula couple the learner's optimization state to its future training distribution. Controlled interventions show that mitigating selected pathologies improves learning. Stabilizing the learner improves long-horizon performance and zero-shot generalization without changing the curriculum rule or increasing environment interaction. Our results establish learner trainability as a complementary design principle for UED. Effective curricula require students that remain capable of learning from the distributions they produce.

---


### 41. [Not All Latents Are Equal: Importance-Weighted Latent Graph Generation](https://arxiv.org/abs/2611.08788)

**<font color=#1a73e8>作者：</font>** Biraaj Rout, Jay Revolinsky, Han Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph generation has shown tremendous effectiveness in modeling complex scientific tasks ranging from molecule generation to optimized circuit design. Most recent advancements have developed models that learn to denoise noisy graphs using either discrete diffusion or flow matching. However, discrete graph diffusion scales quadratically with the number of nodes, making it difficult to use such models on larger graphs. On the other hand, latent graph generation instead seeks to denoise noisy graph latents, which scale better to more nodes due to their lower dimension. However, in practice, latent graph generation models lag behind their discrete counterparts in performance. We study this problem, finding that it is caused by the unequal distribution of that different latent dimensions have on graph reconstruction. the impact. We observe that the vast majority of impact is contained in only a smaller number of latent dimensions. Since equal emphasis is placed on reconstructing the entire latent in the loss function, existing models are optimized to reconstruct information irrelevant to the downstream task. To tackle this problem, we propose Latent Importance Reweighting ({\bf LIR)} which weights each latent dimensions via it's importance to final graph reconstruction. Importance is calculated as the relative influence of a single latent unit on graph reconstruction, which is represented via the Jacobian of the decoder relative to the latent. Our method is model-agnostic and requires no additional model parameters or hyperparameters. Experiments show that LIR can boost performance and lead to faster training convergence when applied to two different autoencoders on various benchmark datasets. Code: this https URL

---


### 42. [TopoSHAP: Shapley for Explainable and Efficient Topological Deep Learning](https://arxiv.org/abs/2611.08789)

**<font color=#1a73e8>作者：</font>** Mathilde Papillon, Nina Miolane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topological deep learning (TDL) extends learning on graphs, such as molecules or social networks, to higher-order structures, such as rings in a molecule or groups in a social network. Explaining which of these structures drive a model's predictions, and which architectural components matter most for its performance, remains challenging. We introduce TopoSHAP, an efficient and general explanation framework that addresses both questions across topological domains and model architectures. TopoSHAP-cell assigns Shapley values to topological data cells and extracts compact explanations. These explanations match or outperform graph-based counterparts on GraphXAI benchmark data while running up to 112$\times$ faster. They also reveal advantageous topological feature design, leading to measured improvements in explanation recovery and predictive accuracy. On the architecture side, TopoSHAP-neighbor explains how neighborhoods contribute to model performance, and turns these evaluations into a backward-elimination search that identifies smaller, competitive architectures early in training. This is up to $11.3\times$ cheaper than traditional TDL training sweeps.

---


### 43. [MotionBench-XAI: Benchmarking What Shapes Shapley Explanations in Spatiotemporal Machine Learning](https://arxiv.org/abs/2611.08797)

**<font color=#1a73e8>作者：</font>** Mathilde Papillon, Louisa Cornelis, Nina Miolane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting outcomes from spatiotemporal data, such as assessing Parkinson's severity from human motion, often requires explainability in addition to accuracy. Practitioners need to know what drove the prediction, whether it be spatial (a body joint), temporal (a specific window), or both. Shapley values are attributions computed by treating input features as players in a cooperative game and measuring how the model output changes as coalitions of players are removed. Computing them involves choosing what counts as players, how absent players are imputed, and how the game is evaluated. How these choices affect explanation quality is poorly understood for spatiotemporal data, and real data carries no ground-truth attributions to check against. We present MotionBench-XAI, a benchmark built on i) five synthetic spatiotemporal datasets with exact ground-truth Shapley values, ii) three real datasets across clinical gait, electrocardiogram, and audio, iii) ten attribution methods across three player sets, and iv) three trained architectures. We show that grouping features into players, across time, space, or both, matters more than the choice of imputer. Generative imputers improve explanations only when their conditional models are accurate. On real data, the standard proxy metrics select contradictory best methods. We distill these findings into practical insights and provide an open-source pipeline.

---


### 44. [Driver Takeovers and Longitudinal Responses Analysis from Naturalistic Driving](https://arxiv.org/abs/2611.08798)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Hao Zhou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As Level 2 advanced driver-assistance systems (ADAS) become more widely used, understanding driver-system interaction is increasingly important for traffic safety. However, limited real-world data make these interactions difficult to study. We present ADAS-TO, a naturalistic dataset of 16,446 takeover clips from 364 drivers across 2,585 different drives. It combines road video, vehicle kinematics, driver inputs, and ADAS status. To analyze takeover behavior, we retained 6,206 manually reviewed takeover events during continued lane keeping or car following. We excluded events in which the driver intentionally changed lanes, turned, or made a stop beyond the ADAS's capabilities (e.g., at a red light or stop sign) shortly after takeover. Drivers began intervening before ADAS disengaged in 65.6% of takeovers involving braking or steering. When the ego vehicle was still closing on a lead vehicle at disengagement, longitudinal safety margins often narrowed further after the transfer to manual control. Among 2,031 such events, 78.5% had a lower minimum time-to-collision (TTC) in the five seconds after disengagement than in the five seconds before it. For events involving braking, the mean TTC trajectory reached its minimum about 1.2 s after disengagement. We model the subsequent braking response using a Gazis-Herman-Rothery (GHR) car-following law. Its median five-second spacing root-mean-square error is 1.34 m with observed lead motion and 1.84 m with predicted lead motion. The fitted model expresses braking as a response to looming, with stronger responses at higher speeds and shorter gaps. Applied before takeover, it shows that greater looming than predicted by the human-response reference is associated with disengagement. These findings support continued assessment of longitudinal safety after ADAS disengagement, while the driver's braking response develops.

---


### 45. [The Matthews Correlation Coefficient: Fifty years](https://arxiv.org/abs/2611.08799)

**<font color=#1a73e8>作者：</font>** Jesus S. Aguilar-Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fifty years after its introduction, the Matthews Correlation Coefficient (MCC) remains central -and debated- in binary classification. This survey offers a comprehensive retrospective and an in-depth analysis of MCC, covering its historical development, mathematical foundations, and implications for practice. We clarify long-standing misconceptions, formalize its equivalences (to Pearson's correlation and to Chi2 in 2x2 tables), and examine its behavior under class imbalance. Beyond MCC, we develop analytical (derivatives) and graphical (contour plots) frameworks that generalize to any confusion-matrix-based metric. These frameworks expose structural properties -bias, robustness, sensitivity- that scalar summaries conceal, and they provide actionable guidance for selecting and interpreting performance measures in applications where reliability and fairness matter. Together, our results position MCC within a broader toolkit while clarifying when it is informative -and when alternatives may be preferable.

---


### 46. [Scale as a Modality: Multi-Scale Pixel-Space Diffusion Transformers](https://arxiv.org/abs/2611.08802)

**<font color=#1a73e8>作者：</font>** Ruibo Chen, Kaishen Wang, Tianyi Xiong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models rely on pretrained autoencoders that introduce lossy compression and constrain spatial granularity. Pixel-space diffusion avoids this bottleneck and enables flexible tokenization at multiple spatial scales, yet existing approaches largely adopt two-level coarse-to-fine architectures with limited cross-scale interaction. We introduce MS-pDiT, a multi-scale pixel-space diffusion transformer that treats spatial scale as a modality. MS-pDiT tokenizes the same noisy image at multiple patch sizes, processes each scale in a dedicated transformer stream, and enables bidirectional information exchange through compacted MM-DiT-style joint attention, with attention cost independent of the finest patch size. This design establishes the number of scales as a new architectural scaling dimension. On ImageNet $256\times256$, increasing the number of scales from two to five consistently improves FID from 4.39 to 2.31, 2.26, and 2.19, while adding an intermediate scale substantially outperforms increasing depth under comparable parameter budgets. Further analysis highlights the importance of bidirectional cross-scale interaction and late introduction of fine-grained streams. MS-pDiT achieves FID scores of 1.43 and 1.44 on ImageNet $256\times256$ and $512\times512$, respectively, and naturally extends to text-to-image generation, achieving 0.86 on GenEval and 83.9 on DPG-Bench.

---


### 47. [Impact of color in computer and human-based object recognition under occlusion](https://arxiv.org/abs/2611.08808)

**<font color=#1a73e8>作者：</font>** Courtney M. King, Elissa Aminoff, Daniel D. Leeds  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partial occlusions challenge object recognition in both human and computer vision (CV), but the impact is largely dependent on the occlusion and model design. Properties relating to color are particularly important in biological recognition and frequently leveraged for camouflage, however there are still open questions about what makes them effective and how they translate to CV. This work studies partial occlusions that create camouflage, including those that blend in with target objects or with scenes, which alter object representations in distinct ways. Experiments evaluate recognition performance on both human participants and models ranging from convolutional neural networks (CNNs) to transformers, and additional analysis is performed on models to uncover trends in processing and object representations under multiple occlusion types. Novel metrics offer explainability of model behavior under occlusion: non-occlusion precision (NOP) and non-occlusion recall (NOR) measure alignment of model activations with and without occlusion, and activation in occlusion (AIO) measures the percentage of activations that occur in occluded regions. Findings show that human recognition, and most transformers, are negatively impacted by generated camouflaging occluders, with scene-based camouflage performing worse than object-based. Classical CNNs show a strong opposite trend, performing the worst on neutral-colored occlusions, suggesting that contextually-related colors, particularly scene-based, benefit object recognition rather than disrupting shape or boundary cues. Additionally, generated camouflaging occluders for training augmentation improves robustness to unseen camouflage for selected CNN model, and occlusion metrics suggest trends about learned mechanisms. Findings have interesting implications for alignment in human and computer vision, model vulnerabilities, and explainability.

---


### 48. [Global Solar Siting from Geospatial Embeddings](https://arxiv.org/abs/2611.08831)

**<font color=#1a73e8>作者：</font>** Abdullah Rehman, Quentin Paletta, Rui Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global solar photovoltaic (PV) capacity is rapidly growing, helping decrease our emissions and dependence on fossil fuels. However, optimally siting a solar plant remains challenging, requiring anticipation of geographical, urban, and infrastructure needs. Current methods rely on multi-criteria decision analysis (MCDA) using hand-picked geophysical layers and solar-resource products, however these strategies are not geographically transferable and do not capture the practical requirements of solar sites. We use geospatial embeddings, dense vectors representing geophysical properties of a location, to analyse 38,591 existing solar sites and the land they were built on to learn the latent solar suitability signal. We assess a set of linear and non-linear models and select a soft-voting ensemble of a random forest and a multilayer perceptron (RF+MLP ensemble), chosen for accuracy and large scale deployability. Validated against future installations in thirteen countries, the ensemble separates existing solar sites from random land with a median ROC-AUC of 0.90. Compared with published MCDA strategies, the ensemble increases ROC-AUC by 0.06-0.30 in every country. The ranking also concentrates real deployment: the most-suitable 20% of land holds 84% of estimated generation (annual energy yield) and 67% of installed capacity (potential power output). After applying standard siting constraints, 5.6% of global land (9.8% if cropland is permitted) remains highly suited to solar. The global 10 m resolution solar suitability dataset and code can be found here: this https URL.

---


### 49. [Solver-Admitted Metamorphic Testing of Learned Network Optimization Surrogates](https://arxiv.org/abs/2611.08837)

**<font color=#1a73e8>作者：</font>** Vineet Jagadeesan Nair, Stephen Peng, Arun Ravindran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equivalent encodings of an optimization problem can produce different learned predictions. Interpreting these differences requires accounting for numerical error and multiple optima. We construct metamorphic tests for optimization solver surrogates with explicit eligibility conditions, output alignment, and numerical thresholds. Reference-solver agreement and independent constraint checks determine which sampled pairs enter the audit. We study alternating-current optimal power flow (AC-OPF), the traveling salesman problem (TSP), the capacitated vehicle routing problem (CVRP), and maximum independent set (MIS). Across five grids, GridSFM-Open violates each of 13 relations on at least one grid, and 12 by more than twice the threshold. Randomly initialized copies of the grid models fail nearly the same relations, so the failures do not require training. Source patches and input canonicalization remove selected discrepancies, but no intervention establishes preserved accuracy and feasibility within the declared margin on every grid. In routing, Policy Optimization with Multiple Optima (POMO) has a single-pass rotation/reflection violation rate that rises from 12.7% to 89.5% between 20 and 100 cities. Graph-Based Diffusion Solvers for Combinatorial Optimization (DIFUSCO) violates the MIS disjoint-union relation on 35.6% of draws. Post hoc normalization within connected components removes these violations on the tested graphs. These findings support reporting metamorphic consistency alongside optimality, feasibility, and accuracy, and validating repair quality separately from consistency.

---


### 50. [The APL Doesn't Fall Far From The Tree: Unsupervised Artefact Prototype Learning in Histopathology](https://arxiv.org/abs/2611.08838)

**<font color=#1a73e8>作者：</font>** Emilia Agasi, Charlie Gourley, C. Simon Herrington 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histopathology foundation models provide rich representations of tissue morphology, but technical artefacts in whole slide images introduce noise that may impact diagnostic accuracy. We introduce Artefact Prototype Learning (APL), a novel approach to detecting these artefacts that exploits the geometry of pre-trained embedding spaces without manual labels or fine-tuning. Rather than treating artefacts as isolated outliers, APL computes prototypes of out-of-distribution patches and uses them to distinguish artefact-associated patterns from tissue. Evaluation on a single-centre dataset shows that APL outperforms prior methods GrandQC and HistoART in detecting artefacts such as blur, dark spots, slide edges and pen marks, but struggles with tissue folds and blood. These results show that frozen pre-trained embeddings already carry information that allows artefact detection without expensive labels or vast computational resources.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
