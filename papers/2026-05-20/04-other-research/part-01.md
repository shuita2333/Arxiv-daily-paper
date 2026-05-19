# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 1. [Systematic Optimization of Real-Time Diffusion Model Inference on Apple M3 Ultra](https://arxiv.org/abs/2605.16259)

**<font color=#1a73e8>作者：</font>** Yoichi Ochiai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While real-time image generation using diffusion models has advanced rapidly on NVIDIA GPUs, systematic optimization research on non-CUDA platforms such as Apple Silicon remains extremely limited. In this study, we conducted comprehensive optimization experiments across 10 phases targeting the Apple M3 Ultra (60-core GPU, 512 GB unified memory) with the goal of achieving real-time camera img2img transformation. We explored a wide range of techniques including CoreML conversion, quantization, Token Merging, Neural Engine utilization, compact model exploration, frame interpolation, kNN search-based synthesis, pix2pix-turbo, optical flow frame skipping, and knowledge distillation, quantitatively evaluating the effectiveness of each approach. Ultimately, by combining CoreML conversion of the distillation-specialized model SDXS-512 with a 3-thread camera pipeline, we achieved real-time camera img2img transformation at 22.7 FPS at 512x512 resolution. The primary contribution of this work is the systematic demonstration that optimization insights established for CUDA are not necessarily effective on Apple Silicon's unified memory architecture. We reveal an optimization landscape fundamentally different from that of NVIDIA GPUs -- including the absence of speedup from quantization, the ineffectiveness of parallel inference, and the unsuitability of the Neural Engine for large-scale models -- and provide practical guidelines for diffusion model inference on Apple Silicon.

---


### 2. [Mirror Descent-Type Algorithms for the Variational Inequality Problem with Functional Constraints](https://arxiv.org/abs/2605.16262)

**<font color=#1a73e8>作者：</font>** Mohammad S. Alkousa, Fedor S. Stonyakin, Belal A. Alashqar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational inequalities play a key role in machine learning research, such as generative adversarial networks, reinforcement learning, adversarial training, and generative models. This paper is devoted to the constrained variational inequality problems with functional constraints (inequality-type constraints). We propose some mirror descent-type algorithms that switch between productive and non-productive steps depending on the values of the functional constraints at iterations, with many different step size rules and stopping criteria. We analyze the proposed algorithms and prove their optimal convergence rate to achieve a solution with desired accuracy, for problems with bounded and monotone operators and Lipschitz convex functional constraints. In addition, we propose a modification of the proposed algorithms by considering each functional constraint in the calculation when we have a productive step, as well as the first constraint that violates the feasibility. This modification can save the running time of algorithms when we have many functional constraints. In addition, we provide an analysis of the proposed algorithms for $\delta$-monotone operators, allowing us to apply the proposed algorithms, as a special case, to constrained minimization problems when we do not have access to the exact information about the subgradient of the objective function. Numerical experiments that illustrate the work and performance of the proposed algorithms are also given.

---


### 3. [AgentWall: A Runtime Safety Layer for Local AI Agents](https://arxiv.org/abs/2605.16265)

**<font color=#1a73e8>作者：</font>** Ashwin Aravind  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The safety of autonomous AI agents is increasingly recognized as a critical open problem. As agents transition from passive text generators to active actors capable of executing shell commands, modifying files, calling APIs, and browsing the web, the consequences of unsafe or adversarially manipulated behavior become immediate and tangible. Existing AI safety work has focused primarily on model alignment and input filtering, but these approaches do not address what happens at the moment an agent's intent becomes a real action on a real machine. This gap is especially acute in local environments, where developers run agents against their own filesystems, credentials, and infrastructure with little runtime control. This paper introduces AgentWall, a runtime safety and observability layer for local AI agents. AgentWall intercepts every proposed agent action before it reaches the host environment, evaluates it against an explicit declarative policy, requires human approval for sensitive operations, and records a complete execution trail for audit and replay. It is implemented as a policy-enforcing MCP proxy and native OpenClaw plugin, working across Claude Desktop, Cursor, Windsurf, Claude Code, and OpenClaw with a single install command. We present the design, architecture, threat model, and policy model of AgentWall, and demonstrate 92.9% policy enforcement accuracy with sub-millisecond overhead across 14 benchmark tests. AgentWall is open-source at this https URL.

---


### 4. [Video-based Social Interaction Behavior Analysis with the Simulated Interaction Task for Children (Kids-SIT)](https://arxiv.org/abs/2605.16270)

**<font color=#1a73e8>作者：</font>** Rituja Pardhi, Matthias Norden, William Saakyan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Accurately quantifying children's social interaction behavior is part of understanding their cognitive and emotional development, as well as mental health conditions. Kids-SIT is a web-based tool designed to computationally analyze children's behaviors by engaging them in a standardized video conversation scenario while their responses are video recorded. In a pre-registered study with 21 healthy children, we evaluated the potential of the Kids-SIT as an accessible paradigm for automated analysis of children's social interaction behavior. We assessed their subjective impression, as well as verbal and non-verbal responses during the Kids-SIT. Verbal content was analyzed using the LIWC tool. Three socially relevant non-verbal behaviors (gaze deviation, smiling, and nodding) were manually annotated and automatically extracted using three computational methods. We examined how well these methods capture naturalistic social interaction patterns of healthy children. We conducted an exploratory classification of healthy children (n=21) and those with social anxiety disorder (n=11) using automated behavioral features. The semantic analysis of the children's verbal responses and their post-hoc impressions indicated that the Kids-SIT successfully elicited natural social interaction behavior. Children's non-verbal behavior also showed similar pattern: they looked at their interaction partner for most of the time, particularly while listening than speaking. Smiling and gazing toward the partner occurred more frequently during the person-directed liked and disliked parts than during the picture-description phase. These non-verbal behavior patterns were captured both by manual annotations and by the computational analysis methods. In the exploratory analysis with a clinical sample, automatically extracted features enabled above-chance differentiation between children with and without SAD (AUC=0.74).

---


### 5. [Exploring Student Feedback Needs and Design Opportunities in Data Storytelling Education](https://arxiv.org/abs/2605.16271)

**<font color=#1a73e8>作者：</font>** Jennifer Posada, Taha Hassan, Lujie Karen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data storytelling workflows ask learners to integrate analytical, design, and narrative skills, but instructors rarely have the capacity to provide detailed feedback at each step. Computational and AI-assisted storytelling offers opportunities to support student learning, but how feedback should be structured effectively remains unclear. To address this gap, we conducted a two-phase participatory design study. Through participant observations (N=8) and interviews (N=6), the first phase explored learners and educators' feedback needs and challenges in a data storytelling course. The second phase conducted two design workshops (N=8/10) to design and evaluate feedback strategies (frequency, seamlessness, accountability) for Story Studio: an AI-assisted narrative storytelling application. Our findings show that participants perceived on-demand and process feedback modes as effective, but automatic and outcome feedback as slightly more persuasive. We discuss implications for designing AI-augmented storytelling systems that adapt their feedback modes to the diverse needs and expectations of students.

---


### 6. [Beyond Compliance: How AI Could Help Creative Writers by Refusing Them](https://arxiv.org/abs/2605.16272)

**<font color=#1a73e8>作者：</font>** Hua Xuan Qin, Guangzhi Zhu, Mingming Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mainstream creativity support design prioritizes compliant AI for seamless writing interactions, but concerns over inappropriate AI reliance highlight the need for designs fostering reflection on balanced AI and non-AI resource use. Theoretically, intentional AI non-compliance, refusals (saying ``no'' to requests), could introduce such reflection through friction stronger than other bypass-able solutions. Practically, refusal content/language characteristics lead to nuanced reactions. However, little research empirically focuses on nuances beyond mandatory ethical/technical constraints, on turning refusals into strategic friction for `innocuous' requests. We address this through a qualitative study with 22 creative writers, exploring reactions to refusals to common requests across writing stages (planning, translating, reviewing). Findings suggest that reflective potential depends on heterogeneous preference alignment along situational (e.g., convergent/divergent thinking phases), cognitive (e.g., domain beliefs), and relational (e.g., AI roles) dimensions. We discuss implications for creativity support, broader issues (e.g., AI addiction), and frictional/seamful AI design (e.g., integrating different compliance levels).

---


### 7. [AI-Generated 3D Environments as Speculative Mediators in More-Than-Human Design: An Exploratory Study](https://arxiv.org/abs/2605.16273)

**<font color=#1a73e8>作者：</font>** Aung Pyae  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> More-than-human design challenges anthropocentric assumptions by foregrounding non-human entities as stakeholders, yet designers face an epistemic boundary: they cannot directly access non-human experience. We present an exploratory study examining how generative AI -- specifically a text-to-3D world generation platform producing navigable environments -- may function as a speculative mediator in more-than-human design. Through a qualitative study with five participants from engineering and sustainability backgrounds engaging with AI-generated worlds derived from non-human traces, we investigate how instant exploration -- navigating generated environments within seconds -- shapes reflection, iteration, and provisional treatment of outputs. Our findings suggest that navigating AI-generated environments supports reflection-in-action distinct from evaluating static representations, while designers' epistemic stances oscillate between treating outputs as generative provocations and as authoritative representations. We propose technologically-amplified backtalk and productive provisionality as preliminary lenses for understanding how navigable AI-generated 3D environments can surface anthropocentric assumptions in more-than-human design.

---


### 8. [Designing for Engagement: How Self-Determination Theory Can Guide Digital Health Design for User Motivation](https://arxiv.org/abs/2605.16276)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhang, Rafael A. Calvo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User engagement is crucial for the efficacy of digital health and mental health interventions, yet existing design strategies for improving engagement remain heterogeneous, context-specific, and insufficiently grounded in motivational theory. In this paper, we propose a preliminary, theory-grounded design framework that draws on Self-Determination Theory (SDT) and its sub-theory, Organismic Integration Theory (OIT), to guide the design of digital health interventions for sustained user engagement. Informed by existing literature and our own empirical data from surveys (N = 438), interviews (N = 31), and co-design workshops (N = 59) with end users, the framework categorises design strategies across the adoption, interface, and task spheres of the user experience, distinguishing between those that primarily support intrinsic motivation and those that foster autonomous forms of extrinsic motivation. We argue that this distinction is critical: strategies commonly grouped under umbrella terms such as "gamification" in fact operate through different motivational channels and should be designed and evaluated accordingly. By clarifying these motivational pathways, our framework aims to support researchers and practitioners in designing digital health interventions that not only facilitate initial uptake but also enhance the internalisation of health behaviours for long-term, sustained engagement. We present this framework as a basis for discussion at this workshop, inviting expert feedback and critique to refine it as a contribution to the field.

---


### 9. [Making Sense of the Weather, Together: Collaborative Sensemaking in Severe Weather Livestreams](https://arxiv.org/abs/2605.16285)

**<font color=#1a73e8>作者：</font>** Julie A. Vera, Mark Zachry, David W. McDonald  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper examines collaborative sensemaking during severe weather events through the emerging phenomenon of "weatherfluencers" or content creators who livestream meteorological interpretation on platforms like YouTube. Drawing from sensemaking theory, crisis informatics, and platform studies, we analyze how these creators navigate the sociotechnical dynamics of interpreting severe weather in real time with distributed audiences. Through critical incident analysis of 13 Particularly Dangerous Situation (PDS) storm warnings across three prominent weatherfluencers, we identify three key practices: multi-source information triangulation, temporal bridging techniques, and platform-specific adaptations that transform entertainment interfaces into safety-critical communication channels. Our analysis shows how these practices challenge existing models of crisis communication by integrating distributed expertise, collapsing temporal frames, and reconfiguring platform affordances. This research contributes to understanding how informal emergency communicators mediate between institutional alerting systems and public needs, and how visual, multimodal crisis communication differs from text-centered approaches.

---


### 10. [Reducing Credit Assignment Variance via Counterfactual Reasoning Paths](https://arxiv.org/abs/2605.16302)

**<font color=#1a73e8>作者：</font>** Fei Ding, Yongkang Zhang, Yeling Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for multi-step reasoning with large language models (LLMs) often relies on sparse terminal rewards, leading to poor credit assignment conditions where the final feedback is evenly propagated across all intermediate decisions. This results in high gradient variance, unstable training, and numerous ineffective updates, ultimately causing the model to fail and preventing sustained improvement. We introduce a counterfactual comparison-based credit assignment framework, which samples multiple reasoning trajectories under the same input. By treating their differences as an implicit approximation of alternative decisions, we construct an implicit process-level advantage estimator that transforms sparse terminal rewards into step-sensitive learning signals. Based on this, we propose Implicit Behavior Policy Optimization (IBPO), which significantly improves training stability and performance upper bounds on mathematical and code reasoning benchmarks, pointing to a promising direction for unlocking the performance potential of LLMs.

---


### 11. [SignMuon: Communication-Efficient Distributed Muon Optimization](https://arxiv.org/abs/2605.16311)

**<font color=#1a73e8>作者：</font>** Neel Mishra, Kushagara Trivedi, Pawan Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed training of large neural networks is bottlenecked by full-precision gradient communication and by coordinatewise optimizers that ignore the matrix structure of weight tensors. We propose Sign-Muon, a 1-bit, matrix-aware optimizer that combines majority-vote sign aggregation from signSGD with the polar-step framework of Muon. Each worker forms a Muon-style direction by taking the polar factor of its momentum via a Newton--Schulz iteration, transmits only the entrywise signs, and aggregates by majority vote; an optional local polar step further enforces orthogonality at no extra communication cost.
Under spectral-norm smoothness and bounded-variance stochastic gradients, the spectral-norm normalized sign step yields an $\mathcal{O}(1/\sqrt{T})$ nonconvex rate for an $\ell_1$-based stationarity measure. With unimodal symmetric noise, majority vote across $M$ workers cuts the stochastic term by $1/\sqrt{M}$, matching signSGD. In the $\alpha$-$\beta$ model, distributed Sign-Muon needs only one integer sum-allreduce per iteration; all orthogonalization is local, giving a $32\times$ bandwidth reduction over float32 ($4\times$ for int8).
Across 330 CIFAR-10/ResNet-50 configurations Sign-Muon attains the best validation accuracy (92.15\%); its 4-GPU majority-vote variant reaches 92.02\% with 37\% less training time at matched effective batch. On nanoGPT, Sign-Muon achieves lower perplexity and better anytime performance than other sign-based baselines, with favorable weak-scaling up to 16 GPUs.

---


### 12. [When Actions Disappear: Adversarial Action Removal in Self-Play Reinforcement Learning](https://arxiv.org/abs/2605.16312)

**<font color=#1a73e8>作者：</font>** Arahan Kujur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial action masking in self-play reinforcement learning: an attacker selectively removes legal actions from a victim's action set. Unlike observation or action perturbations, removal eliminates decision options before the agent acts. Across poker games scaling from 6 to 5,531 information states and two non-poker domains, learned masking causes substantially more damage than random masking and learned perturbation baselines. The attack persists across Q-learning, PPO, NFSP, neural NFSP, and DQN victims; transfers across agents; is amplified by self-play; and shows no recovery under extended masked training. Mechanistically, the adversary targets high-value decision points, captured by reach-weighted contingent action capacity (CAC$_w$) and a value-weighted refinement CAC$_v$. These results identify action availability as a distinct robustness surface in self-play RL.

---


### 13. [A Structural Threshold in Decision Capacity Governs Collapse in Self-Play Reinforcement Learning](https://arxiv.org/abs/2605.16315)

**<font color=#1a73e8>作者：</font>** Arahan Kujur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that a threshold in decision capacity determines whether self-play reinforcement learning agents collapse under asymmetric rule perturbations. Across poker variants, matrix games, a dice game, and multiple learning algorithms, eliminating all positive-reach contingent decisions causes rapid convergence to a deterministic exploitation attractor, a fixed point at near-maximal loss. Preserving even a single positive-reach contingent decision point prevents this collapse. A frozen baseline and fixed-opponent control confirm that the mechanism is co-adaptation under constraint, not the perturbation itself. The phenomenon is timing-invariant, fully reversible upon action restoration, and intensifies under function approximation. These results establish a sharp threshold at zero reach-weighted contingent action capacity, with severity scaling continuously via reach-weighted capacity in the tested domains.

---


### 14. [Noise2Params: Unification and Parameter Determination from Noise via a Probabilistic Event Camera Model](https://arxiv.org/abs/2605.16317)

**<font color=#1a73e8>作者：</font>** Owen Root, Julinda Mujo, Min Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate, unified models for event cameras (ECs) remain elusive, hampering calibration and algorithm design. We develop a foundational probabilistic model for EC event detection, grounded in photon statistics, that unifies the description of static scene noise events and step response curves (S-curves) within a single analytical framework. Three formulations of the probability distributions are derived, spanning all intensity regimes: exact Poisson, saddle-point, and Gaussian. The model reveals the underlying connection between these otherwise disparate EC behaviors and clarifies the interpretation of S-curves, which we show is more nuanced than selecting a fixed probability threshold. Based on this model, we propose Noise2Params, a method for determining camera-specific values of the log-contrast threshold $B$, the lux-to-photon conversion factor $\alpha$, and the leakage term $\theta$ (found to be intensity dependent), via error minimization against observed noise-event distributions. Noise2Params requires only recordings of static, uniform scenes, offering an experimentally accessible alternative to approaches that demand specialized dynamic light sources. We further support the validity the model by training convolutional neural networks (CNNs) on synthetic noise images generated from our distributions and evaluating their ability to reconstruct static scenes from experimental data. We further demonstrate the utility of our model by showing that CNNs incorporating synthetic data outperform those trained solely on experimental data. Our framework provides a quantitative foundation for EC calibration, noise-aware algorithm design, and applications in photon-limited regimes.

---


### 15. [Investigating Action Encodings in Recurrent Neural Networks in Reinforcement Learning](https://arxiv.org/abs/2605.16318)

**<font color=#1a73e8>作者：</font>** Matthew Schlegel, Volodymyr Tkachuk, Adam White 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building and maintaining state to learn policies and value functions is critical for deploying reinforcement learning (RL) agents in the real world. Recurrent neural networks (RNNs) have become a key point of interest for the state-building problem, and several large-scale reinforcement learning agents incorporate recurrent networks. While RNNs have become a mainstay in many RL applications, many key design choices and implementation details responsible for performance improvements are often not reported. In this work, we discuss one axis on which RNN architectures can be (and have been) modified for use in RL. Specifically, we look at how action information can be incorporated into the state update function of a recurrent cell. We discuss several choices in using action information and empirically evaluate the resulting architectures on a set of illustrative domains. Finally, we discuss future work in developing recurrent cells and discuss challenges specific to the RL setting.

---


### 16. [Forecasting Medium-Horizon Alzheimer's Disease Progression: Residual Gap-Aware Transformers for 24-Month CDR-SB Change from ADNI Clinical and Biomarker Histories](https://arxiv.org/abs/2605.16319)

**<font color=#1a73e8>作者：</font>** Ran Tong, Tong Wang, Lanruo Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medium-horizon Alzheimer's disease progression prediction is difficult because future clinical scores can remain tied to baseline severity, while biomarker histories are irregular and incompletely observed. We develop an anchor-based analysis of 24-month Clinical Dementia Rating Sum of Boxes (CDR-SB) change using harmonized Alzheimer's Disease Neuroimaging Initiative (ADNI) tables. Each labeled sample is anchored at a mild cognitive impairment visit, uses only clinical and biomarker history observed at or before that anchor, and defines the response as CDR-SB at the future visit closest to 24 months within an 18--30 month window minus anchor CDR-SB. The analytic cohort contains 2,600 labeled anchors from 858 participants and 7,276 longitudinal rows. We propose a residual gap-aware transformer that combines a mixed-effects statistical reference with transformer-based residual learning from pre-anchor clinical and biomarker histories. The model uses participant-level random intercepts in the mixed-effects reference, observation-level triplet tokenization for irregular histories, and a learned nonnegative time-gap penalty inside self-attention. We compare the proposed model with a Bayesian-information-criterion-selected linear mixed-effects baseline, GRU-D, and STraTS under repeated participant-level train--test splits. Across five participant-level random seeds, the proposed model achieves the best mean test performance across all reported metrics, reducing MSE by 13.1% and increasing prediction--observation correlation by 26.4% relative to the mixed-effects baseline. It also improves over both GRU-D and STraTS in mean error and correlation. These results show that statistical anchoring and gap-aware residual learning provide a useful structure for medium-horizon Alzheimer's disease progression prediction.

---


### 17. [AdaGraph: A Graph-Native Clustering Algorithm That Overcomes the Curse of Dimensionality and Enables Scientific Discovery](https://arxiv.org/abs/2605.16320)

**<font color=#1a73e8>作者：</font>** Ahmed Elmahdi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present AdaGraph, a graph-native clustering algorithm born from the Structure-Centric Machine Learning (SC-ML) paradigm -- a new field of unsupervised learning that replaces geometry-centric (distance-based) computation with structure-centric (topology-based) computation, fundamentally dissolving the curse of dimensionality. AdaGraph operates entirely within the kNN graph topology, a representation that retains meaningful relational structure in arbitrarily high dimensions where Euclidean distance metrics become uninformative. AdaGraph requires no a priori specification of the number of clusters k, handles noise natively, and scales via the SLCD (Sample-Learn-Calibrate-Deploy) prototype-deployment framework. As its unsupervised tuning objective, AdaGraph pairs with Graph-SCOPE, the topology-based cluster validity index introduced as a separate SC-ML contribution. On 10 synthetic benchmarks spanning d=10 to d=5000, Graph-SCOPE achieves mean ARI=0.900 and correctly selects k on 9/10 datasets -- outperforming Silhouette, Davies-Bouldin, and Calinski-Harabasz -- while maintaining Kendall tau >= 0.92 with ground-truth cluster quality across all dimensionalities (Silhouette: tau ~= 0.46). We validate AdaGraph across three scientific domains: (1) gene co-expression discovery in hepatocellular carcinoma (GSE14520, 10,000 genes, 488 patients, no dimensionality reduction), where AdaGraph identifies condition-specific gene modules that WGCNA, ICA, NMF, and Spectral Biclustering fail to resolve; (2) natural language text clustering, where AdaGraph achieves ARI=0.751 on 20NG-6cat versus HDBSCAN's 0.464 (62% relative improvement); (3) materials science clustering of superconductors (145-dimensional Magpie features), perovskites, and JARVIS-DFT materials, where AdaGraph achieves the highest Graph-SCOPE on all three datasets.

---


### 18. [Language Game: Talking to Non-Human Systems](https://arxiv.org/abs/2605.16321)

**<font color=#1a73e8>作者：</font>** Yanbo Zhang, Michael Levin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language carries thought and coordination among humans but rarely reaches further along the spectrum of diverse intelligence. Yet non-neural systems -- from gene regulatory networks and microbial consortia to fungi -- are increasingly recognized as substrates of computation, decision-making and memory, making dialogue with non-human intelligence newly conceivable. Today such dialogue is attempted only by proxy: a large language model speaks on the system's behalf, so any intelligence on display originates from the model while the system itself remains silent. Here we ask whether the system can speak in its own voice. Following Wittgenstein, who located meaning in use, we treat communication as a game played with the system. Its internal dynamics are frozen as the nonlinear core of a reinforcement-learning policy, with only linear input and output interfaces trained. Through use and reward, the system's states and responses acquire meaning within the game, so playing becomes speaking. Because different architectures playing the same game optimize the same reward, their behaviors can all be read as pursuit of that reward; the game serves as a lingua franca across otherwise irreconcilable representations. Given a human prompt, a language model routes it to the game whose semantics best match it and designs an environmental state for which the desired action is the rational response, letting the system reply through its own behavior. Applied across diverse gene regulatory networks and reinforcement-learning tasks, the framework yields fluent dialogue without altering any system parameter, shows that well-trained agents of disparate origin converge on similar behavior, and reveals that specific GRN properties make a system easier or harder to talk with -- an inductive bias of the reservoir itself. Our framework opens a new route to conversing with any dynamical system on its own terms.

---


### 19. [Bi-Level Chaotic Fusion Based Graph Convolutional Network for Stock Market Prediction Interval](https://arxiv.org/abs/2605.16324)

**<font color=#1a73e8>作者：</font>** Eshwar Sai Kandimalla, Sravan Chowdary Kankanala, Sumana Bhimineni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial market forecasting is inherently uncertain, yet most deep learning approaches rely on point predictions that provide only single-value estimates without quantifying uncertainty. Such predictions are insufficient for risk-aware decision-making, as they fail to capture the range of possible outcomes and the associated confidence of this http URL problem can be solved using prediction intervals, which allow obtaining an upper and lower bound for the prediction, thus enabling uncertainty representation in the model. Yet, the current methods tend to disregard relationships between assets or cannot simultaneously ensure good calibration and sharpness of the resulting intervals in dynamically changing market regimes. In our work, we propose a spatio-temporal graph-based approach with a bi-level chaotic fusion technique to solve this problem. Our model uses separate nonlinear transformation functions to estimate the interval center and width. Additionally, a volatility-aware gating mechanism is used to make predictions dependent on the regime in which the market operates. Temporal dependencies are considered by embedding graph structures and sequentially modeling them. Training is conducted according to a Lower-Upper Bound Estimation (LUBE) objective. Our experimental results show significant improvements compared to existing baselines (LSTM, GRU, GCN, HGNN) when applied to data from 2016 to 2026 with 43 leading companies in eight sectors of the NSE. It provides the lowest Winkler score (0.0778), tightest prediction intervals (PIAW = 0.1407), and highest coverage (PICP = 96.6%), with all differences statistically significant (p < 0.001) according to the Diebold-Mariano test.

---


### 20. [Phase Transitions in Driven Informational Systems: A Two-Field Perspective on Learning Theory and Non-Equilibrium Chemistry](https://arxiv.org/abs/2605.16325)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Phase-transition phenomena in deep learning (grokking, emergent capabilities, and ontological reorganization under context shift) have been studied through several lenses, including representational compression, singular learning theory, and information-theoretic progress measures. Independently, non-equilibrium statistical physics has identified phase transitions in driven chemical reaction networks underlying prebiotic selection, with empirical signatures that are difficult to reproduce within single-field gradient accounts.
We propose a perspective in which both classes of phenomena admit a common description as driven informational systems: stochastic processes governed by two gradient fields, an entropy production rate Sigma and an information quasi-potential Phi_I := -ln p*, where p* is the stationary density. Within this framework we introduce two candidate order parameters: an adversarial breakdown threshold alpha_dagger and a self-referential coupling threshold kappa_c.
The joint scaling of (alpha_dagger, kappa_c) defines a candidate universality class with exponents (gamma_1, gamma_2). We outline the geometric structure of this framework, identify falsifiable predictions distinguishing it from single-field alternatives, and show consistency with recent empirical findings (2024--2026) on alignment transitions, adversarial breakdown scaling, and partial introspection in large language models.

---


### 21. [Preference Instability in Reward Models: Detection and Mitigation via Sparse Autoencoders](https://arxiv.org/abs/2605.16339)

**<font color=#1a73e8>作者：</font>** Shunchang Liu, Xin Chen, Belen Martin Urcelay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference learning in large language models relies on reward models as proxies for human judgment. However, these models frequently exhibit preference instability, producing contradictory preference assignments in response to subtle, meaning-preserving input variations. We analyze this instability at the representation level under three semantic-preserving perturbation types: paraphrasing, pattern injection, and backdoor triggers. We attribute this instability to over-reliance on predictive yet brittle features, which we term unstable features, and isolate them via Sparse Autoencoders (SAEs) in a sparse latent space where benign and perturbed inputs activate distinctly separable patterns. Building on this separability, we propose two SAE-based instability mitigation strategies: SAE Feature Steering, which identifies and suppresses anomalously activated features at inference, and SAE Residual Correction, which learns adaptive adjustments over SAE features to restore correct preferences. Our methods substantially reduce incorrect preference assignments on harmlessness and hallucination benchmarks while preserving benign performance and general utility on other tasks, without retraining the reward model. Our code and data are available in \url{this https URL}.

---


### 22. [Orth-Dion: Eliminating Geometric Mismatch in Distributed Low-Rank Spectral Optimization](https://arxiv.org/abs/2605.16341)

**<font color=#1a73e8>作者：</font>** Tatsuhiro Nakamori, Laura Gomezjurado Gonzalez, Ganesh Talluri 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank gradient compression reduces communication in distributed training by representing updates with rank-$r$ factors. Dion is a recent method that approximates Muon, a spectral optimizer that orthogonalizes momentum, using one step of power iteration followed by column normalization (rescaling each column of the right factor to unit length). This makes it compatible with fully sharded data parallel training, but it converges more slowly than full-rank spectral methods. We show that this gap is geometric: column normalization does not yield the rank-$r$ polar factor that Muon implicitly targets, so the resulting direction violates the dual-norm constraint of the low-rank spectral geometry, and the rate picks up an extra factor of $\sqrt{r}$ even though the low-rank approximation of the gradient itself is accurate. The same mismatch enters the smoothness term and the error-feedback recursion in the analysis, which has a knock-on effect on empirical performance. We propose Orth-Dion, which replaces column normalization with QR orthogonalization of the right factor. Under non-Euclidean smoothness, with $L_r$ the curvature constant along rank-$r$ directions, Orth-Dion attains rate $O(\sqrt{L_r/T})$, matching exact spectral methods at the same per-step communication cost as Dion. The proof removes the bounded-drift assumption common in prior error-feedback analyses via a self-consistent fixed-point argument, and uses a time-averaged contraction that only requires the error sequence to contract on average rather than at every step. Experiments on large-scale language model pre-training validate the predicted $\sqrt{r}$ scaling and show that Orth-Dion closes the convergence gap to Muon at Dion's communication cost.

---


### 23. [Flow-Direct: Feedback-Efficient and Reusable Guidance for Flow Models via Non-Parametric Guidance Field](https://arxiv.org/abs/2605.16348)

**<font color=#1a73e8>作者：</font>** Kim Yong Tan, Yueming Lyu, Ivor Tsang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training-free guidance enables pre-trained diffusion and flow models to optimize application-specific objectives using feedback from external black-box reward functions. However, existing methods are feedback-inefficient because reward feedback is used only transiently to inform a localized gradient approximation or a discrete search decision, and is subsequently discarded. To address this limitation, we propose Flow-Direct, a framework that guides the generation process via a persistent guidance field. Theoretically, this guidance field is analytically derived from the log-density ratio between the base and reward-weighted target distributions; it transports the pre-trained distribution to the target distribution. In practice, the field is implemented as a non-parametric estimator constructed from all accumulated reward-evaluated samples. As more samples are collected during optimization, this empirical guidance field becomes increasingly accurate. This persistent formulation yields two major advantages. First, Flow-Direct is highly feedback-efficient: because every evaluated sample is used to refine the global guidance field, no reward information is wasted. Second, the framework is naturally reusable: once optimization is complete, the collected dataset defines a reusable guidance field for generating novel target samples without additional reward evaluations, and distinct guidance fields can be combined to generate samples that simultaneously satisfy multiple objectives.

---


### 24. [Federated Nested Learning: Collaborative Training of Self-Referential Memories for Test-Time Adaptation](https://arxiv.org/abs/2605.16350)

**<font color=#1a73e8>作者：</font>** Hong Chen, Pengcheng Wu, Yuanguo Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We rethink Federated Learning (FL) from a nested learning perspective, framing the core challenge as how to collaboratively learn optimization rules, not just static models, to tackle Non-IID client data. To address this, we propose Federated Nested Learning (FedNL), a novel framework that reformulates FL as a three-level nested optimization system. FedNL embeds Titans-based linear attention into FL, enabling clients to perform lightweight, zero-shot test-time adaptation by treating a delta rule as an online gradient step. Experiments on Non-IID MMLU and long-context benchmarks show that FedNL achieves competitive performance in short-context reasoning, enhances the performance of long-context retrieval and streaming Cross-Entropy, and maintains constant inference memory.

---


### 25. [PIMSM: Physics-Informed Multi-Scale Mamba for Stable Neural Representations under Distribution Shift](https://arxiv.org/abs/2605.16351)

**<font color=#1a73e8>作者：</font>** Sangyoon Bae, Shinjae Yoo, Jiook Cha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific foundation models are expected to reuse representations under changes in dataset, acquisition protocol, and deployment domain, yet many sequence backbones treat scientific temporal structure as an unconstrained pattern to be fitted. We argue that this misses a central property of natural dynamical systems: neural and atmospheric time series are organized by interacting processes across multiple physical timescales, and failure to preserve this multiscale structure contributes to brittleness under distribution shift. We formalize this failure mode as temporal kernel mismatch, where a model fits in-distribution dynamics with an effective memory policy that is not anchored to the signal's physical timescales, leading to representation drift and degraded transfer. We propose Physics-Informed Multi-Scale Mamba (PIMSM), a state-space architecture that maps spectrum-estimated transition points between frequency regimes (knee frequencies) to scale-specific discretization parameters and anchors them to acquisition time units. On Human Connectome Project fMRI, PIMSM improves robustness and representation stability under severe temporal-context truncation, extreme low-resource transfer, and resting-state-to-task-state generalization. Without modality-specific adaptation, the same architecture also attains the lowest variable-wise MAE across all reported horizons and variables on Weather-5K held-out-station spatial out-of-distribution forecasting. These results support temporal-scale alignment as a practical inductive bias for scientific foundation models that must preserve structure, not only fit correlations, under deployment shift.

---


### 26. [TailedTS: Benchmark Dataset for Heavy-Tailed Time Series Prediction and Periodicity Quantification](https://arxiv.org/abs/2605.16361)

**<font color=#1a73e8>作者：</font>** Xinyu Chen, HanQin Cai, Lijun Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present TailedTS, a large-scale benchmark dataset derived from Wikipedia hourly page view observations throughout 2024, specifically designed to test time series forecasting models under heavy-tailed, zero-inflated, and non-Gaussian conditions. The dataset comprises approximately 24.69 billion data points spanning roughly 3 million unique Wikipedia pages per month, stored in high-efficiency Apache Parquet format. Wikipedia traffic follows a pronounced power-law distribution where roughly 5% of pages account for over 70% of total page views, creating a natural and rigorous testbed for model robustness against extreme volatility that are absent from or underrepresented in existing benchmarks such as M4, M5, and UCI electricity datasets. TailedTS enables several research tasks. First, we introduce a periodicity quantification framework based on sparse autoregression with sparsity and non-negativity constraints, revealing that frequently-viewed pages exhibit significantly weaker periodic structure than their less-viewed counterparts, showing direct implications for server allocation and traffic forecasting on large digital platforms. Second, we provide standardized prediction benchmarks evaluated under a suite of non-Gaussian loss functions, including $\ell_1$-norm, Huber, quantile, and $\ell_p$-norm losses, demonstrating that standard Gaussian-based estimators degrade substantially on high-volume page categories, while robust alternatives provide consistent gains across all traffic scales. TailedTS is publicly available at this https URL.

---


### 27. [When Is Rank-1 Steering Cheap? Geometry, Granularity, and Budgeted Search](https://arxiv.org/abs/2605.16362)

**<font color=#1a73e8>作者：</font>** John T. Robertson, Jianing Zhu, Haris Vikalo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering offers a lightweight way to control LLMs without retraining, but its effectiveness varies sharply across concepts. Prior work often reads this variability as evidence that many concepts are not captured by a single steering direction. We argue instead that much of it reflects search difficulty: a useful rank-1 intervention often exists, but finding it can be expensive.
We formalize rank-1 steering as a budget-constrained optimization over intervention layer and coefficient. Across concepts and model families, prompt-boundary directional alignment predicts where effective interventions occur, enabling geometry-guided search that reaches high utility with substantially fewer evaluations, reducing the trials needed to recover 95\% of best-found utility by 39.8\% on average across three model families. To explain why some concepts remain expensive even under better search, we introduce \emph{concept granularity}, a measure of directional heterogeneity across contrastive contexts. Granularity distinguishes concepts whose difference vectors share a stable global direction from those where prompts agree locally within each input but the utility-maximizing direction rotates systematically across inputs. Higher granularity is associated with slower convergence and lower best-found performance (Pearson $r{=}0.44$ with trials-to-95\%, $r{=}{-}0.46$ with best-found utility, both $p<0.001$).
We present \textit{GRACE}, a Granularity- and Representation-Aware Concept Engineering framework that uses activation geometry to diagnose the dominant source of steering difficulty, select the appropriate remedy, and allocate optimization effort efficiently. Our results shift the frame from ``\textit{when does rank-1 fail?}'' to ``\textit{when is rank-1 cheap and stable?}'', turning activation geometry from a descriptive tool into an actionable prior for LLM control.

---


### 28. [ORACLE: Anticipating Scams from Partial Trajectories in Streaming App Usage](https://arxiv.org/abs/2605.16363)

**<font color=#1a73e8>作者：</font>** Wenbo Gao, Songbai Tan, Zhongan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smartphone scams are increasingly prevalent and typically manifest as multi-stage, cross-application processes with gradually emerging intent. Effective intervention thus requires anticipating scams before the intent becomes explicit. This is inherently challenging, as decisions must rely on partial trajectories with temporally distributed evidence. In this paper, we propose \textbf{ORACLE} Online Reasoning for Anticipating Cross-temporal Latent thrEats, the first agentic framework for early scam anticipation from \textit{streaming app-usage} trajectories. To support this setting, we curate a real-world long-horizon benchmark of streaming app-usage trajectories, covering 12 scam types, spanning extended periods (15 days on average), involving diverse applications (95 apps), and interleaving normal and scam behaviors. To address fragmented evidence, we introduce a self-evolving context manager that adaptively consolidates entity-centric interactions over time, enabling more effective reconstruction of cross-temporal evidence from partial observations. To enhance sensitivity to latent early-stage signals, we propose an on-policy self-distillation scheme in which a teacher model, conditioned on summarized anti-scam reflections and clues by skills, supervises a student model without access to such reflections. This scheme thereby distills evidence-informed knowledge and improves recognition of emerging fraud patterns from partial trajectories. Experiments show that \method{} consistently improves early scam anticipation, yielding timely warnings while reducing false alerts in realistic streaming scenarios.

---


### 29. [Machine Learning-Based Pre-Test Risk Stratification for PCR-Confirmed Chlamydia Using Patient-Reported Data and Urine Biomarkers](https://arxiv.org/abs/2605.16365)

**<font color=#1a73e8>作者：</font>** Mehrab Mahdian, Marko Lehes, Katrin Krolov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early identification of individuals at elevated risk of Chlamydia trachomatis infection may enable optimal use of molecular testing in resource-aware screening. We evaluate the feasibility of pre-test risk stratification (PTRS) using machine-learning models trained on routinely available, non-invasive clinical data.
A curated dataset of 93 urine samples with PCR reference labels was analyzed using three feature groups: patient-reported history and symptoms, urine biomarkers from standard urinalysis, and their combination. Five supervised classifiers were evaluated using stratified 5-fold cross-validation with out-of-fold probability estimates. Performance was assessed using area under the receiver operating characteristic curve (AUC) and threshold-dependent metrics, with uncertainty quantified via bootstrap confidence intervals.
Models using only patient-reported data showed moderate discrimination (AUC up to 0.72). Urine biomarker-based models demonstrated slightly lower peak discrimination but more consistent performance, with ensemble methods yielding the strongest results. Combining feature groups marginally increased the peak AUC and reduced performance variability across models, indicating improved robustness.
Findings indicate that urine biomarkers provide a reliable predictive signal for PTRS that is complementary to patient-reported information, while feature integration enhances robustness. This work supports the integration of non-invasive, routinely available information for PTRS into screening workflows, including decentralized or home-based PCR contexts, to optimize testing prioritization.

---


### 30. [SwordBench: Evaluating Orthogonality of Steering Image Representations](https://arxiv.org/abs/2605.16372)

**<font color=#1a73e8>作者：</font>** Vladimir Zaigrajew, Dawid Pludowski, Hubert Baniecki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Steering or intervening on model representations at inference time to correct predictions is essential for AI interpretability and safety, yet existing evaluation protocols are limited to ambiguous language modeling tasks. To address this gap, we introduce SwordBench, a benchmark for steering image representations of vision models across multiple backbones and concept removal tasks. Beyond a unified benchmarking suite, we propose new evaluation notions that uncover the second-order effects of orthogonalization among concept activation vectors for pragmatic steering. Specifically, cross-concept robustness measures the stability of concept detection performance across inputs orthogonalized against alternative concepts, and collateral damage quantifies whether steering inadvertently affects model performance on a downstream task for inputs lacking the bias. We find that although a linear support vector machine exhibits superior separability and orthogonality, it fails to achieve zero collateral damage, often trailing sparse autoencoders. In simpler regimes, both standard baselines and optimization-based methods fail to achieve perfect steering. The source code will be made available soon on GitHub.

---


### 31. [Cross-Source Supervision for Bone Infection Segmentation in Dual-Modality PET-CT](https://arxiv.org/abs/2605.16373)

**<font color=#1a73e8>作者：</font>** Zonglin Yang, Xiaolei Diao, Jishizhan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early and accurate diagnosis and lesion localization of bone infections are crucial for clinical treatment. PET-CT integrates anatomical information from CT with metabolic information from PET, making it an important imaging modality for diagnosing bone infections. However, accurate lesion segmentation remains challenging due to indistinct lesion boundaries and inconsistencies in annotations generated by different experts or automated systems. In this work, we investigate multimodal segmentation of bone infections under annotation discrepancy. We develop a bimodal end-to-end segmentation framework that integrates PET metabolic signals and CT bone-window anatomy through an early-fusion multimodal this http URL mitigate performance inflation caused by inter-slice correlation in small datasets, this study discards traditional two-dimensional evaluation methods and implements a rigorous patient-level 3D volumetric evaluation and cross-validation. Furthermore, instead of forcing a singular consensus, we propose a decoupled dual-source learning framework where parallel models are trained on independent expert annotations driven by high-sensitivity and high-specificity clinical intents. Experimental results objectively report performance variations at the patient level (Mean + SD and Mean - SD), demonstrating the effectiveness of multimodal PET-CT fusion. The cross-evaluation matrix quantitatively reveals how models successfully internalize distinct expert diagnostic philosophies, providing a robust, diversity-preserving paradigm for clinical AI deployment in bone infection segmentation.

---


### 32. [Lost or Hidden? A Concept-Level Forgetting in Supervised Continual Learning](https://arxiv.org/abs/2605.16374)

**<font color=#1a73e8>作者：</font>** Katarzyna Filus, Kamil Faber, Roberto Corizzo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning studies how models can adapt to new tasks while retaining previously acquired knowledge. Although a broad spectrum of methods has been proposed to mitigate catastrophic forgetting, the field remains predominantly performance-driven, with limited insight into what forgetting actually corresponds to within the vision model's representation space. Prior work has primarily analyzed forgetting through task-level performance or coarse measures of representational drift, without disentangling output-level accessibility from changes in finer-grained internal structure. To this end, we propose a diagnostic framework that leverages Sparse Autoencoders (SAEs) to define a task-anchored latent feature space, enabling analysis of how task-specific information evolves at a finer granularity, where individual SAE latents are treated as concept proxies for recurring and relatively disentangled visual patterns in the model's internal computations. Within this framework, we decompose forgetting into apparent concept deletion, recoverability, and decodability. We show that a large portion of seemingly lost concept-level information can often be recovered under linearity assumption, with concept decodability degrading as more tasks are introduced. Overall, our findings suggest that a significant part of concept-level forgetting can be attributed to changes in the representational accessibility rather than complete information erasure.

---


### 33. [An Information-Theoretic Criterion for Efficient Data Synthesis](https://arxiv.org/abs/2605.16379)

**<font color=#1a73e8>作者：</font>** Hanyu Li, Zhengqi Sun, Xiaotie Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data becomes crucial for large language model training, but its effectiveness is highly inconsistent. We provide an information-theoretic account of this inconsistency: synthetic data improves a model only when the generation-training loop is information-open, i.e., shaped by external signals (verifiers, environments, or rubrics) that inject task-relevant information beyond the model's current distribution. When the loop is information-closed (relying on the model's own outputs without such signals), the data processing inequality ensures that task-relevant information can only decrease, making collapse a predicted outcome. Among information-open pipelines, both efficiency and generalization hinge on the meta-level of supervision: a coarser signal such as binary correctness treats all acceptable outputs as equivalent, so the behavior it teaches is not tied to any particular domain or surface form and generalizes naturally across tasks and domains. These observations lead to a guiding thesis: learning preferentially converges to the most information-efficient signal component available, which accelerates learning when that component is the intended one, but causes reward hacking when a spurious pattern happens to be simpler.

---


### 34. [ReTAMamba: Reliability-Aware Temporal Aggregation with Mamba for Irregular Clinical Time Series Prediction](https://arxiv.org/abs/2605.16380)

**<font color=#1a73e8>作者：</font>** Jinwoong Kim, Sangjin Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical time-series data are difficult to model with methods designed for regular sequences because they exhibit irregular sampling, frequent missing values, and heterogeneous observation patterns across variables. Existing approaches commonly use observation masks and time-gap information, but they do not continuously capture the decaying reliability of past observations or consistently organize multi-resolution information within a coherent temporal context during aggregation. To address these limitations, we propose Reliability-aware Temporal Aggregation with Mamba (ReTAMamba), which reconstructs clinical time series as time-variable token sequences, estimates observation reliability from missingness and elapsed time, and augments interval summaries with statistical descriptors. Chronological Weaving is used to integrate short- and long-term temporal information within a coherent temporal context, and a budgeted token router is applied to constrain sequence length while preserving informative summaries. Experiments on MIMIC-IV, eICU, and PhysioNet 2012 show that ReTAMamba consistently improves AUPRC over strong baselines, with average relative gains of 7.51%, 7.80%, and 10.15%, respectively. Cohort-level and patient-level analyses on eICU further showed that the learned mean decay for more dynamic signals, such as heart rate and blood pressure, was 24.3% larger than that for relatively static signals, such as laboratory test variables. These findings suggest that effective prediction in irregular clinical time series requires modeling not only what was measured, but also when and how it was observed, including information freshness and observation timeliness.

---


### 35. [StreamPro: From Reactive Perception to Proactive Decision-Making in Streaming Video](https://arxiv.org/abs/2605.16381)

**<font color=#1a73e8>作者：</font>** Ao Li, Zihan Xiao, Zihao Yue 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive streaming video understanding requires models to continuously process video streams and decide when to respond, rather than merely what to respond. This naturally introduces a decision-making problem under partial observations, where models must balance early prediction against sufficient evidence. However, existing benchmarks largely follow a "see-then-answer" paradigm, where responses are triggered only after explicit evidence appears, effectively reducing proactive reasoning to delayed perception. As a result, they fail to evaluate a model's ability to make timely and reliable decisions under incomplete observations. Moreover, training proactive models is inherently challenging due to the extreme imbalance between silence and response signals in streaming trajectories, as well as the need to jointly optimize response correctness and timing. To address these challenges, we introduce StreamPro-Bench, a new benchmark that evaluates streaming models from three complementary perspectives: Perception Understanding, Temporal Reasoning, and Proactive Agency, where the last measures a model's ability to make early yet reliable decisions under partial observations. We further propose StreamPro, a two-stage training framework for proactive learning. First, we introduce CB-Stream Loss to mitigate the severe supervision imbalance during supervised fine-tuning (SFT). Then, we apply Group Relative Policy Optimization (GRPO) with a multi-grained reward design that involves both turn-level and trajectory-level rewards. Experiments show that StreamPro significantly improves proactive performance. On StreamPro-Bench, it achieves 41.5, substantially outperforming the previous best (10.4), while also maintaining strong performance on real-time streaming benchmarks, achieving 78.9 on StreamingBench-RTVU.

---


### 36. [A neurosymbolic Approach with Epistemic Deep Learning for Hierarchical Image Classification](https://arxiv.org/abs/2605.16383)

**<font color=#1a73e8>作者：</font>** Ezel Kilicdere, Shireen Kudukkil Manchingal, Fabio Cuzzolin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks achieve high accuracy on image classification tasks. Yet, they often produce overconfident predictions as which fail to express epistemic uncertainty, and frequently violate logical or structural constraints present in the data. These limitations are particularly pronounced in hierarchical classification, where predictions across fine and coarse levels must remain coherent. We propose, for the first time, a unified neurosymbolic and epistemic modelling framework that augments Swin Transformers with focal set reasoning and differentiable fuzzy logic. Rather than treating labels as isolated categories, our method induces data-driven focal sets within the learnt embedding space, which helps capture epistemic uncertainty over multiple plausible fine-grained classes. These focal sets form the basis of a belief-theoretic layer that uses fuzzy membership functions and t-norm conjunctions to encourage consistency between fine- and coarse-grained predictions. A learnable loss further balances calibration, mass regularisation, and logical consistency, allowing the model to adaptively trade off symbolic structure with data-driven evidence. In experiments on hierarchical image classification, our framework maintains accuracy on par with transformer baselines while providing more calibrated and interpretable predictions, reducing overconfidence and enforcing high logical consistency across hierarchical outputs. Our experimental results show that combining focal set reasoning with fuzzy logic provides a practical step toward deep learning models that are both accurate and epistemically aware.

---


### 37. [Mutual Enhancement Between Global Tokens and Patch Tokens: From Theory to Practice](https://arxiv.org/abs/2605.16384)

**<font color=#1a73e8>作者：</font>** Xiusheng Huang, Xin Jiang, Jun Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and effective discrete image tokenization is crucial for long image sequence processing. However, current methods rigidly compress all content at a fixed rate, ignoring the variable information density of images and leading to either redundancy or information loss. Inspired by information entropy, we propose TaTok, a Theoretically grounded adaptive image Tokenization framework. We rigorously identify two key drawbacks in existing methods: information insufficiency when reconstructing images with patch tokens alone, and information redundancy among patch tokens. To address these, we introduce global tokens that model mutual information across patch tokens, and a Dynamic Token Filtering (DTF) algorithm based on cumulative conditional entropy to eliminate redundancy. Experiments confirm TaTok's state-of-the-art performance, delivering a 1.3x gFID improvement and 8.7x inference speedup. By allocating tokens according to information richness, TaTok enables more compressed yet accurate image tokenization, offering valuable insights for future research.

---


### 38. [Stabilizing Temporal Inference Dynamics for Online Surgical Phase Recognition](https://arxiv.org/abs/2605.16387)

**<font color=#1a73e8>作者：</font>** Yang Liu, Ning Zhu, Jingjing Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online Surgical Phase Recognition (SPR) models can reach high frame-wise accuracy, yet their predictions often lack temporal stability, fragmenting workflow understanding and reducing the reliability of downstream assistance. We show that this instability is not random noise but arises from two mechanisms: early misclassifications corrupt temporal feature states and propagate forward to form error cascades, and phase transitions follow evidence-accumulation dynamics whereas most online SPR systems rely on memoryless frame-wise decisions, making them sensitive to transient confidence fluctuations. We propose a unified Train-Inference-Evaluation framework that explicitly stabilizes temporal inference dynamics using model-agnostic, plug-and-play components. For training, the Temporal Error-Cascade (TEC) loss suppresses error onset and mitigates forward error propagation by stabilizing temporal feature evolution. For inference, the Evidence-Gated Transition Predictor (EGTP) enforces evidence-driven state transitions, allowing phase changes only when accumulated evidence exceeds a confidence boundary. For evaluation, we introduce the Temporal Fragmentation Index (TFI), a reliability-aware metric that quantifies instability-induced temporal disagreement beyond conventional frame-wise and token-based measures. Experiments on Cholec80 and AutoLaparo across three representative backbones show that the proposed framework substantially improves temporal stability and reduces prediction fragmentation, while maintaining or modestly improving frame-wise performance.

---


### 39. [ChronoSC: Task-Oriented Semantic Communication via Temporal-to-Color Encoding](https://arxiv.org/abs/2605.16388)

**<font color=#1a73e8>作者：</font>** Phuc H. Nguyen, Trung T. Nguyen, Quy N. Duong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic communication (SC) aims to reduce transmission overhead by conveying task-relevant information rather than raw data. However, existing SC approaches for video largely focus on pixel-level reconstruction or rely on complex spatiotemporal pipelines, leading to excessive bandwidth usage and latency that are unsuitable for low-resource deployments. In this paper, we propose ChronoSC, a task-oriented semantic communication framework for Video Question Answering (VideoQA). ChronoSC introduces Chrono-Color Stacking, a lightweight and lossless projection scheme that encodes temporal video dynamics into a single static image, enabling extreme temporal compression before transmission. This compact semantic representation is transmitted using a lightweight Deep Joint Source-Channel Coding (DeepJSCC) transceiver and explicitly reconstructed at the receiver. Unlike latent-space methods, explicit visual reconstruction enables the direct reuse of pre-trained vision-language models; specifically, a pre-trained BLIP model is employed to infer answers from noisy, reconstructed chrono-images. Experiments on the CLEVRER dataset show that ChronoSC achieves up to 192 times bandwidth reduction compared to raw video transmission while maintaining high VideoQA accuracy.

---


### 40. [Inducing Spatial Locality in Vision Transformers through the Training Protocol](https://arxiv.org/abs/2605.16390)

**<font color=#1a73e8>作者：</font>** Eduardo Santiago Toledo, Asael Fabian Martínez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate whether the training protocol can induce spatial locality in the early layers of a Vision Transformer (ViT) trained from scratch, without large-scale pretraining. Keeping the architecture and optimization procedure fixed, we compare a Baseline protocol with a Modern protocol (AutoAugment/ColorJitter, CutMix, and Label Smoothing) on CIFAR-10, CIFAR-100, and Tiny-ImageNet, characterizing each attention head via Mean Attention Distance (MAD) and normalized entropy. Across all three datasets, the Modern protocol produces more local and more concentrated attention in early layers; on CIFAR-100, the minimum MAD drops from 0.316 (Baseline) to 0.008 (Modern). To identify the source of this effect, we conduct an ablation study on CIFAR-100 by adding or removing each component individually. The results identify CutMix as the determining component within our experiments: all conditions with CutMix exhibit MAD 0.024, while all conditions without CutMix remain at MAD 0.210. AutoAugment and Label Smoothing show no independent effect on locality. Taken together, these findings suggest that the pressure to classify from partial image regions, induced by CutMix, can promote the emergence of local attention in Vision Transformers.

---


### 41. [Vision Transformer-Conditioned UNet for Domain-Adaptive Semantic Segmentation](https://arxiv.org/abs/2605.16393)

**<font color=#1a73e8>作者：</font>** Joel Valdivia Ortega, Tingying Peng, Marion Jasnin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation is essential for analysing anatomical features in biomedical research, yet a performance gap remains for Vision Transformers (ViTs) in the field, particularly for sparse, fine-structured, and low signal-to-noise targets. We attribute this challenge in part to the lightweight pixel decoders commonly used in promptable ViT models, who may lack the local inductive bias needed for high-precision biomedical masks. We bridge this gap by introducing ViTC-UNet, which conditions a UNet on frozen pre-trained ViT representations through learnable tokens and a two-way attention decoder. This combines ViT global visual priors with the local inductive bias and high-resolution decoding capacity of UNets, while avoiding end-to-end ViT fine-tuning even in cross-domain settings. ViTC-UNet outperforms baseline results in semantic segmentation tasks across MRI and CT modalities, demonstrating that structure-conditioned UNet decoding can efficiently adapt large-scale visual priors to high-complexity biomedical segmentation.

---


### 42. [Beyond MMSE: Enhancing PnP Restoration with ProxiMAP](https://arxiv.org/abs/2605.16396)

**<font color=#1a73e8>作者：</font>** Kenta Vert, Giacomo Meanti, Scott Pesme 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plug-and-Play (PnP) methods have become standard tools for solving imaging inverse problems by replacing the intractable maximum a posteriori (MAP) denoiser with the MMSE one. While this mismatch has been widely treated as unavoidable, recent works have sought to close this gap by targeting the MAP with diffusion-model scores. We show this is problematic in practice: learned scores do not match the true ones, so MAP-targeting iterations converge to cartoon-like images rather than realistic ones, and better results are obtained by stopping short of convergence. We turn this observation into a design principle and introduce ProxiMAP, an iterative MAP approximation whose noise schedule keeps the iterate's residual noise matched to the denoiser's training noise. This keeps the denoiser in-distribution where its score is reliable, and yields implicit early stopping that avoids the failure mode above. ProxiMAP is a modular drop-in replacement for MMSE denoisers in standard PnP algorithms and consistently sharpens reconstructions across deblurring, inpainting, super-resolution, and phase retrieval. Building on the same principle, we propose a hybrid variant that applies ProxiMAP only in the late iterations of PnP, where the denoiser is most reliable -- matching or exceeding the full-replacement variant at a fraction of the cost.

---


### 43. [Trajectory-Aware Adaptive Inference in Object Detection Models](https://arxiv.org/abs/2605.16397)

**<font color=#1a73e8>作者：</font>** Grigorios Papanikolaou, Ioannis Kontopoulos, Giannis Spiliopoulos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The increasing integration of sensors in autonomous maritime navigation has led to large-scale multimodal datasets, raising challenges in achieving efficient real-time perception. In such systems, object detection and trajectory perception of nearby vessels are tightly coupled, particularly in dynamic environments such as maritime navigation. However, the efficiency of object detection models during inference remains an often-overlooked aspect. To this end, we build upon an existing object detection framework by incorporating GPS trajectory data into the inference process to enable input-adaptive computation. Specifically, we introduce an early-exit mechanism in a YOLOv8-based detector that incorporates motion cues - such as inter-vessel distances. Frames of vessels that are separated by short distances, converging with high speed, are processed using the full model, while only a subset of the network's architecture is activated otherwise. The difficulty degree (or scene complexity) of a frame or set of frames per second is evaluated by leveraging inter-object distance and the rate at which the distance between them decreases. Experimental results demonstrate that this strategy maintains satisfactory detection performance while significantly reducing inference time and computational cost, thus enabling a flexible trade-off between accuracy and efficiency compared to full-model inference.

---


### 44. [Stable and Near-Reversible Diffusion ODE Solvers for Image Editing](https://arxiv.org/abs/2605.16399)

**<font color=#1a73e8>作者：</font>** Barbora Barancikova, Daniil Shmelev, Cristopher Salvi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The inversion of diffusion models plays a central role in image editing. Algebraically reversible ODE solvers provide an appealing approach to diffusion inversion for text-guided image editing, by eliminating the inversion error inherent in DDIM-based editing pipelines. However, empirical results indicate that reversibility alone is insufficient. As edits require larger semantic or visual changes, reversible diffusion solvers often exhibit instabilities and suffer sharp drops in output quality. In this paper, we show that the trade-off between exact reversibility and numerical stability manifests empirically as a trade-off between background preservation and prompt alignment in image editing. We then investigate the use of near-reversible Runge-Kutta methods as a more stable alternative to exactly reversible diffusion schemes. When combined with a vector-field smoothing strategy, the resulting approach improves edit fidelity, remains stable under large edits, and largely retains the background-preservation benefits of reversible solvers.

---


### 45. [CADS: Conformal Adaptive Decision System for Cost-Efficient Image Classification](https://arxiv.org/abs/2605.16401)

**<font color=#1a73e8>作者：</font>** Turkoglu Mikael, Bary Tim, Thielens Vincent 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While high-capacity AI models have advanced state-of-the-art performance, their practical deployment is often hindered by high inference costs, environmental impact, and a "one-size-fits-all" approach that ignores varying sample complexity. In clinical settings for instance, the waste of computational resources on routine cases is a significant barrier to sustainable AI. In this paper, we introduce the Conformal Adaptive Decision System (CADS), a sequential multi-model algorithm designed to optimize resource allocation by efficiently sampling models based on the estimated data complexity. CADS leverages conformal prediction to quantify image uncertainty at runtime. CADS provides a mathematically grounded framework for balancing the cost-accuracy dilemma that dynamically routes samples through a model cascade, ranging from lightweight "Scout" models to high-capacity "Oracle" architectures. Validated on two datasets, CADS demonstrated superior efficiency and accuracy at a computational cost that can be up to 12 times lower than heavy-model inference. By accurately routing samples based on real-time complexity, CADS ensures high diagnostic reliability while drastically reducing the economic and environmental footprint of AI.

---


### 46. [Hybrid Quantum-MambaVision: A Quantum-enhanced State Space Model for Calibrated Mixed-type Wafer Defect Detection](https://arxiv.org/abs/2605.16404)

**<font color=#1a73e8>作者：</font>** Satwik Sai Prakash Sahoo, Jyoti Prakash Sahoo, Ting Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting actionable knowledge from industrial visual data is fundamentally bottlenecked by extreme class imbalance and the prohibitive computational complexity of modern foundation models. In semi-conductor manufacturing, identifying multi-label wafer defects is a complex spatial data mining task where overlapping patterns obscure critical root-cause signals. While Vision Transformers (ViTs) excel at global dependency extraction, their quadratic scaling renders them inefficient for high-throughput, real-time anomaly detection. To overcome these computational barriers, this paper introduces Hybrid Quantum-MambaVision, a highly efficient architecture tailored for spatial knowledge discovery. We integrate a linear-complexity State-Space Model (SSM) backbone with a Parameterized Quantum Context Adapter (QCA) and Low-Rank Adaptation (LoRA). The Mamba backbone efficiently captures long-range spatial dependencies, while the quantum adapter maps compressed latent features into a high-dimensional Hilbert space to disentangle complex, overlapping signatures. On the highly imbalanced MixedWM38 dataset, Hybrid Quantum-MambaVision achieves exceptional multi-label classification performance, significantly reducing the error rate on complex multi-defect topologies compared to classical baselines. The quantum regularizer acts as a profound uncertainty calibrator, substantially reducing Maximum Calibration Error (MCE) and minimizing expected false-positive costs. This work establishes a scalable Quantum-Classical hybrid paradigm for efficient representation learning in industrial data mining.

---


### 47. [Concepts Worth Having: Refining VLM-Guided Concept Bottleneck Models with Minimal Annotations](https://arxiv.org/abs/2605.16405)

**<font color=#1a73e8>作者：</font>** Nicola Debole, Andrea Passerini, Stefano Teso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept-bottleneck models (CBMs) are neural classifiers that compute predictions from high-level concepts extracted from the input. CBMs ensure stakeholders can understand the concepts -- and the predictions they entail -- by learning these from concept-level annotations, which are however seldom available. Recent CBM architectures work around this issue by obtaining annotations from Vision-Language Models (VLMs). While greatly broadening applicability, doing so can yield lower quality concepts and therefore less interpretable models. We strike for a middle ground by introducing Vision-plus-Human-guided CBM (VH-CBM), a hybrid approach that exploits both VLMs and a small amount of dense annotations. VH-CBM employs a Gaussian Process in the VLM's embedding space, which captures useful global information about the target domain, to propagate the expert's supervision to any target data point. Our empirical evaluation shows how VH-CBM predicts more accurate concepts than VLM-guided CBMs even when annotating as little as 1% of the data, while sporting better concept calibration and supporting active learning.

---


### 48. [Contrastive-SDXL: Annotation-Preserving Night-Time Augmentation for Pedestrian Detection](https://arxiv.org/abs/2605.16406)

**<font color=#1a73e8>作者：</font>** Franky George, Muhammad Khalid, Adil Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Night-time pedestrian detection remains challenging because labelled night-time data are limited and large illumination differences make daytime-only trained detectors unreliable. Latent diffusion models (LDMs) provide a powerful basis for image-to-image translation and cross-domain augmentation, but their effectiveness in safety-critical perception depends on whether detector-relevant objects and local semantic structure are preserved when translating between source and target domains. In this work, we present Contrastive-SDXL, a day-to-night augmentation framework for night-time pedestrian detection built on SDXL-Turbo and fine-tuned using Low-Rank Adaptation (LoRA). To preserve semantic correspondence between daytime inputs and translated night-time images, we introduce a patch-wise semantic contrastive loss guided by a pretrained DINOv2 encoder rather than generator encoder features. Multi-level DINOv2 self-attention maps enforce both local and global semantic consistency, while an object consistency loss explicitly encourages pedestrian preservation. Contrastive-SDXL produces realistic night-time images, achieving a Frechet Inception Distance (FID) of 22.5. Detectors trained with our synthetic images obtain a 6-7% reduction in miss rate compared with a daytime-only baseline, approaching the performance of detectors trained on real night-time data. These results demonstrate that consistency-driven diffusion augmentation can effectively support safety-critical night-time pedestrian this http URL

---


### 49. [Visual Search Patterns in 3D Pancreatic Imaging: An Eye Tracking Study](https://arxiv.org/abs/2605.16408)

**<font color=#1a73e8>作者：</font>** Anna Anikina, Leila Khaertdinova, Trine Balschmidt 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Eye tracking has emerged as a powerful tool for examining visual perception and search strategies in various domains, including medicine. While it is relatively straightforward to apply in 2D settings, its use in 3D medical imaging remains challenging and not yet well explored. This gap is particularly relevant for radiology, where volumetric images such as computed tomography (CT) scans are routinely read by medical experts. Radiologists typically interpret these images by navigating through hundreds of 2D slices, most often viewed in the axial projection. A taxonomy of eye movement data during navigation through a CT volume could be valuable to understand how radiologists approach diagnostic tasks. As an example of the derived taxonomy, we asked two radiologists to search abdominal CTs of the pancreas. We collect eye tracking data and align eye gaze movements with slice navigation to visualize the representation of the pancreas through volume and analyze clinicians' gaze behavior in both space and time.

---


### 50. [NERVE: A Neuromorphic Vision and Radar Ensemble for Multi-Sensor Fusion Research](https://arxiv.org/abs/2605.16414)

**<font color=#1a73e8>作者：</font>** Omar Mansour, Pietro Martinello, Ethan Milon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present NERVE (Neuromorphic Vision and Radar Ensemble), a multi-sensor dataset comprising 257 minutes of synchronized recordings from five sensors: two Dynamic Vision Sensors (DVS), an RGB-D camera, and two Radar units (24GHz and 77GHz). Captured across 12 measurement days in office environments, NERVE contains around 600GB of uncompressed temporally aligned data with around 914,000 frames and around 9.6 million RGB COCO-formatted annotations covering 16 relevant object categories. To evaluate multi-modal fusion, we construct a DVS+Radar subset for human detection and distance estimation. Baseline experiments using feed-forward and recurrent detectors show that combining DVS with 77GHz Radar consistently improves detection, with recurrent models achieving up to 47.5% mAP and mean absolute Radar distance errors below 1.8m against LiDAR ground truth.

---


> [!TIP]
> 当前位于：**1-50**（第 1/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
