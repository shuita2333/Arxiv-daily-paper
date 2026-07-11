# 📦 其他研究 | 2026年07月12日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-189](./part-04.md)

---

### 1. [Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution](https://arxiv.org/abs/2607.07716)

**<font color=#1a73e8>作者：</font>** Yazheng Liu, Xi Zhang, Sihong Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graphs are ubiquitous in real-world applications and Temporal Graph Networks (TGNs) have achieved superior predictive accuracy. Understanding which historical events drive model predictions can enhance trustworthiness of TGNs. Existing explanation methods overlook the memory module, the core component that records and updates node histories, leaving the influence of past events unexplored. To address this, we attribute TGNs predictions through the topology attribution tree and memory backtracking tree. The topology attribution tree captures the influence of neighbors and their memory vectors, then the memory backtracking tree quantifies how historical events shape node memory vectors. We apply the LRP in TGNs, ensuring that the total contribution of events equals the logits of model. Finally, top-k selection may be unfaithful due to the nonlinear mapping from logits to probabilities, we design optimization objectives to identify the important events. Experiments on nine temporal graph datasets, spanning node property prediction, link prediction tasks and graph classification tasks, show that our method provides faithful explanations and outperforms state-of-the-art baselines. The code is available at this https URL

---


### 2. [Who Gets Missed in the Tail? Thresholded Subgroup Underdiagnosis in Long-Tailed Chest X-ray Classification](https://arxiv.org/abs/2607.07717)

**<font color=#1a73e8>作者：</font>** Ha-Hieu Pham, Hai-Dang Nguyen, Dang P. M. Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In chest X-ray (CXR) classification, acceptable ranking performance can still leave rare-positive patients below threshold, especially within subgroups. We study this pre-deployment fairness problem as an audit question: after a long-tailed multi-label CXR model is converted from scores into decisions, who is missed? Across VinDr-CXR and MIMIC-CXR/CXR-LT, we use a diagnostic ladder to separate class-level long-tail losses, subgroup-aware weighting, group robustness, and threshold selection. On VinDr-CXR, group-tail weighting followed by tail-aware thresholding reduces tail FNR from 0.665 to 0.269, sex worst-group FNR from 0.705 to 0.157, and age worst-group FNR from 0.822 to 0.133, while macro-mAP increases from 0.611 to 0.635. On MIMIC-CXR/CXR-LT, the same score-to-threshold comparison reduces tail FNR from 0.866 to 0.741 and lowers worst-group FNR across sex, age, race, and insurance; residual missed-positive rates nevertheless remain high. Paired bootstrap contrasts on VinDr support the thresholded FNR reductions, and GroupDRO reference runs indicate that aggregate group robustness alone does not remove rare subgroup misses in this setting. The study supports a narrow audit claim: rare-label fairness in CXR depends jointly on the finding, subgroup, and operating threshold, not on label frequency or ranking metrics alone.

---


### 3. [LLT: Local Linear Transformer for PDE Operator Learning](https://arxiv.org/abs/2607.07718)

**<font color=#1a73e8>作者：</font>** Oded Ovadia, Eli Turkel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have become a common approach for learning PDE solution maps and accelerating numerical simulations. Transformer-based neural operators are of particular interest, since attention can learn long-range dependencies in the computational domain. However, standard attention has two major limitations when applied to PDEs: it scales quadratically with the number of computational nodes, and it lacks an explicit bias toward local interactions. To address these issues, we introduce Local Linear Transformer (LLT) for PDE operator learning. The architecture combines linear global attention with local spatial mixing, and incorporates coordinate and geometry information. We evaluate LLT on several PDE problems, including elasticity, plasticity, airfoil flow, pipe flow, and Darcy flow. The reference data for these problems span finite-element, finite-volume, and finite-difference discretizations on structured and unstructured meshes. Compared with other neural-operator and transformer baselines from prior studies, LLT achieves competitive or lower relative $L_2$ error across these problems. On matched structured discretizations, wall-clock time per training iteration is reduced by factors of 1.8 to 2.5 relative to Transolver. We also scale the approach and apply it to a three-dimensional car aerodynamics dataset with 32,186 unstructured mesh points per sample. Together, these results indicate that LLT provides an accurate and computationally efficient operator for PDE problems across discretizations, mesh types, and problem settings.

---


### 4. [Uncertainty-gated selection for block-sparse attention](https://arxiv.org/abs/2607.07724)

**<font color=#1a73e8>作者：</font>** Thomas Rossi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block-sparse attention scales long-context language models by replacing the O(N^2) softmax with a per-query top-k selection over key blocks. This cutoff is myopic: when the k-th and (k+1)-th blocks are nearly tied in score, the selector commits without spending extra budget, and a dropped block carrying answer evidence is unrecoverable downstream. We propose a value-of-information router that measures, for each query, how decisively the top-k cut was made, and doubles the kept set for the queries where that gap is smallest; the rule is backbone-agnostic and stacks with existing block-scoring methods such as Quest. On LongBench-v2 medium at n=215 (the entire dataset subset), router-on-Quest reaches paired recall 0.75 vs. top-k 0.47 -- +28 pp over the SSA-style baseline (McNemar p<0.01) -- and lands within 2 pp of dense on RULER NIAH multikey at the same context. The lift reproduces on four models from three architectures (Qwen2.5, Mistral-Nemo, Qwen3.6). At 128K, the router preserves 0.81 and 0.89 of dense accuracy on Qwen2.5-7B-1M and Qwen3.6 (vs. SSA-style top-k at 0.09 on the former) while the fused selection-plus-kernel pipeline runs at 0.62x and 0.80x dense wall time.

---


### 5. [SHIFT: Survival Prediction from Incomplete and Heterogeneous Genomic Data](https://arxiv.org/abs/2607.07725)

**<font color=#1a73e8>作者：</font>** Muhammet Sami Yavuz, Ayhan Can Erdur, Sabri Mustafa Kahya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Genomic prediction models often fail to transfer across institutions because sequencing panels differ across sites, creating structural feature missingness at deployment. Existing approaches to this challenge typically restrict analysis to genes shared across cohorts, exclude patients with incomplete profiles, or rely on test-time imputation, all of which can reduce robustness and limit the use of multi-center data. We propose Survival prediction Handling Incomplete Features using Transformer (SHIFT), a missingness-aware survival model that directly predicts from incomplete genomic inputs without test-time imputation. SHIFT represents each genomic feature separately and uses masked self-attention, along with a feature-availability mask, so that predictions are based only on observed inputs. Further, we introduce variable-rate feature masking during training to improve robustness to heterogeneous missingness patterns. We evaluate the approach on glioblastoma and lung squamous cell carcinoma with external validation across multiple cohorts, including a challenging setting with severe cross-cohort panel mismatch. Across these settings, SHIFT shows strong generalization and compares favorably with standard survival baselines and imputation-based approaches, while using a single model across differing feature sets. We also find that incorporating patients from incomplete cohorts during development can improve performance on external data, suggesting that partially observed cohorts need not be excluded from model building. These results support missingness-aware modeling as a practical strategy for multi-center survival prediction in precision oncology.

---


### 6. [Architecture Generalization with MetaNCA](https://arxiv.org/abs/2607.07743)

**<font color=#1a73e8>作者：</font>** Meet Barot, Daniel Berenberg, Sina Khajehabdollahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-organization is an emergent property of life, driven by the collective behavior of individual components acting on local information. Biological neurons, through local interactions transmitted through synapses, are able to learn efficiently and can adapt their connections over an organism's lifespan. Motivated by these desirable properties of adaptability and local interaction, neural cellular automata (NCA) models have been successful at learning morphogenesis solely through local update rules, demonstrating stability over many updates and robustness to perturbations. In this work, we introduce Meta Neural Cellular Automata (MetaNCA), a framework that learns local rules which self-organize the weights of artificial neural networks. A learned rule network iteratively updates the weights of a task network using only local interactions on the computation graph. We propose a novel Weight Transformer architecture for the local rule network, which uses linear attention to aggregate signals from neighboring weights and hidden states. Once trained, the rule network generates task networks of diverse architectures without backpropagation. We show that MetaNCA generates weights for feedforward MLPs, CNNs, and ResNets on MNIST and CIFAR-100, scaling to networks of 2 million parameters. We further show that MetaNCA generalizes to architectures not seen during meta-training, and that architectural diversity in the training phase strengthens this generalization.

---


### 7. [LiST: Lipschitz Scaling Training for Robust and Calibrated Neural Networks](https://arxiv.org/abs/2607.07745)

**<font color=#1a73e8>作者：</font>** Arthur Chiron, Franck Mamalet, Thomas Massena 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While accuracy, robustness, and calibration are all essential for reliable neural networks, they are often studied separately; developing models that satisfy all three simultaneously remains a central challenge. Lipschitz-constrained models guarantee robustness by design, yet the manual selection of the Lipschitz constraint L governs the resulting accuracy-robustness trade-off, and their calibration properties remain largely underexplored. In this work, we highlight a theoretical and empirical link between the enforced Lipschitz constraint and Temperature Scaling, a state-of-the-art calibration method. Specifically, we find that for a given training scheme, there exists a non-trivial value L* that yields an out-of-the-box calibrated network, and that calibration acts as a principled criterion to select a well-defined operating point on the accuracy-robustness Pareto front. Leveraging these insights, we introduce Lipschitz Scaling Training (LiST), a novel training paradigm that iteratively adjusts the global Lipschitz constant to reach this operating point. Through a margin parameter in the training loss, LiST further enables the construction of a fully calibrated Pareto front, allowing users to navigate the accuracy-robustness trade-off while remaining calibrated throughout. At convergence, LiST also enables the reintegration of calibration data into training, improving sample efficiency without sacrificing calibration. We validate LiST on CIFAR-10/100 and Tiny-ImageNet, demonstrating competitive accuracy and robustness against constrained and unconstrained baselines, while remaining calibrated out of the box. Code is available at GitHub.

---


### 8. [A Transdiagnostic Space of Disorder Like Phenotypes in Reinforcement Learning Agents](https://arxiv.org/abs/2607.07753)

**<font color=#1a73e8>作者：</font>** Hari Prasad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modelling psychological disorders in artificial agents offers both a testbed for computational psychiatry and a lens on the failure modes of affective control. Prior work induces one or two disorders in a reinforcement learning (RL) agent by hand-tuned reward shaping, labels the behaviour post hoc, and reports single runs. We recast disorder modelling as dose-controllable manipulation of cognitive appraisal signals in an appraisal-guided PPO agent, expressing seven disorders (anxiety, mania, obsessive-compulsive checking, depression, impulsivity, addiction, and post-traumatic stress) each as a single knob grounded in a computational psychiatry account, with each symptom measured by a preregistered assay mapped to a recognised paradigm. Across more than a thousand runs (10 seeds, four controls, 95% confidence intervals) every disorder shows a graded, monotone dose-response that no control reproduces. Beyond these induced effects, three findings emerge that were not written into the reward: the disorders self-organise into a two-dimensional affective space in which mania mirrors anxiety; removing a knob remits reward distortion disorders (mania, checking, addiction) but not avoidance disorders (anxiety, PTSD), which instead recover under a graded exposure curriculum; and two simultaneous knobs interact nonadditively, yielding testable comorbidity predictions. Appraisal weights thus parameterise a controllable space of affective phenotypes in which the same knobs that induce a disorder can model its treatment. We also show that three disorder knobs (depression, addiction, anxiety) transfer to a three-dimensional pixel environment (MiniWorld) with a standard convolutional agent and no appraisal critic, with cross-assay dissociation confirmed across both domains, indicating the framework is not specific to grid worlds or to PPO's appraisal critic.

---


### 9. [The Importance of Encoder Choice:A Tabular-Image Study](https://arxiv.org/abs/2607.07756)

**<font color=#1a73e8>作者：</font>** Ilia Koloiarov, Diego Coello de Portugal Mecke, Vijaya Krishna Yalavarthi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning usually requires a dedicated encoder per modality. When a tabular modality is involved, prior work has been mostly using a \emph{plain MLP} as the encoder. Yet if it were a strong encoder, the tabular domain would not be ``the last unconquered castle for deep learning''. This study evaluates state-of-the-art tabular models as encoders in the image-tabular setting for the first time. An obstacle stands out. In-Context Learning models, among the best performing methods in the tabular domain, require labels to process instances, making it non-trivial to embed training and test instances the same way. We addressed this problem across multiple models of this family. With this study, we would like to highlight the importance of encoder factor in the multimodal learning.

---


### 10. [AI-integrated models for assessing agricultural resilience](https://arxiv.org/abs/2607.07759)

**<font color=#1a73e8>作者：</font>** Joshua R. Waite, Dana Golden, Brett Indelicato 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agricultural supply chains are vulnerable to disruptions through linked biophysical and economic systems. We develop an AI-powered tool that integrates economic models (GTAP) with biophysical models (APSIM) to analyze supply chain shocks, enabling policymakers and market participants to assess cross-disciplinary impacts through queries and responses written in natural language.

---


### 11. [Trustworthy Machine Learning through the Lens of Combinatorial Optimization: Survey and Research Perspectives](https://arxiv.org/abs/2607.07762)

**<font color=#1a73e8>作者：</font>** Thibaut Vidal, Julien Ferry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning (ML) increasingly relies on complex models whose behavior is difficult to characterize beyond empirical performance metrics. Across a wide range of tasks, including prediction, generation, and decision-making, models with similar empirical performance can exhibit markedly different properties in terms of their transparency, interpretability, robustness, fairness, privacy, and certifiability. This survey highlights how optimization- and certification-oriented reasoning can provide a useful framework for reasoning about such differences, supporting tasks ranging from model training and selection to auditing and certification. We review and synthesize recent advances at the intersection of combinatorial optimization (CO) and trustworthy ML, covering both training and post-training tasks, including interpretable model learning, explanation generation, robustness analysis, fairness auditing, model compression, and privacy attacks and protections. Across these domains, CO formulations offer additional capabilities over purely heuristic approaches, e.g., gradient-based ones, notably global guarantees, formal certificates, and explicit treatment of trade-offs. While scalability remains an important challenge, continued progress in solvers and hybrid algorithms suggests a growing role for CO in the design and deployment of trustworthy ML systems.

---


### 12. [Unlocking Temporal Generalization in Hamiltonian Video Dynamics Models](https://arxiv.org/abs/2607.07763)

**<font color=#1a73e8>作者：</font>** Eli Laird, Corey Clark  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are typically trained to predict discrete-time physical dynamics with a fixed step size baked into the model weights, preventing prediction at variable temporal resolutions. This matters for hierarchical planning, sim-to-real transfer, and scientific or game-engine applications that must query the same dynamics at multiple timescales. Hamiltonian Generative Networks (HGN) offer a principled path forward, grounding predictions in a continuous-time energy function that is, in principle, independent of the observation frame rate. In practice, however, their temporal generalization breaks down in non-conservative settings. We show that in externally forced, dissipative environments, HGN rollouts at step sizes beyond the training regime fail due to distinct failure modes, including latent magnitude growth driven by an unconstrained action-force map, and global truncation error accumulation from an under-resolved integrator. We identify a targeted fix for each mechanism and demonstrate stable dynamics prediction at temporal resolutions well outside the training distribution. In a detailed analysis, we recommend several strategies for enabling temporal generalization in continuous-time video generation.

---


### 13. [Principled Analysis of Deep Reinforcement Learning Evaluation and Design Paradigms](https://arxiv.org/abs/2607.07769)

**<font color=#1a73e8>作者：</font>** Ezgi Korkmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Starting from the utilization of deep neural networks to approximate the state-action value function that led to winning one of the most challenging games, to algorithmic advancements that allowed solving problems without even explicitly stating the rules of the challenge at hand, reinforcement learning research has been the center of remarkable scientific progress for the past decade. In this paper, we focus on the key ingredients of this research progress and we analyze the canonical evaluation and design paradigms in reinforcement learning. We introduce the theoretical foundations of scaling laws in reinforcement learning and show that the asymptotic performance of reinforcement learning algorithms does not have a monotone relationship between performance rankings and data-regimes. We conduct large-scale experiments and our results demonstrate that a line of reinforcement learning research under the canonical design and evaluation paradigms resulted in incorrect conclusions. Our analysis and results provide a core analysis on scaling, capacity and complexity of deep reinforcement learning.

---


### 14. [Unveiling Public Opinion: A Study of Sentiment Analysis Using LSTM and Traditional Models](https://arxiv.org/abs/2607.07772)

**<font color=#1a73e8>作者：</font>** Atiq Ur Rehman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this age of social media, sites like Twitter have become meeting places for people to share their views and feelings on a wide range of issues and current events as they unfold in real time. Sentiment analysis, a critical application of NLP, has become indispensable due to the massive influx of user-generated content, enabling the extraction of meaningful insights from the opinions and emotions expressed in textual data. Sentiment analysis on Twitter employs sophisticated computational techniques to categorize tweets into positive, negative, or neutral sentiments. This method not only examines individual expressions but also analyzes vast databases related to specific subjects or events. By spotting these emotions, machine learning models help improve public opinion interpretation and trend forecasting. This paper examines the effectiveness of various machine learning and deep learning approaches. Designed for this use, the system evaluates logistic regression, random forest, naïve bayes, gradient boosting, and LSTM networks, among other algorithms applied in sentiment classification. This work identifies the optimal sentiment analysis model using a Kaggle Twitter dataset that has been preprocessed through tokenization, lemmatization, and stopword elimination. Emphasizing the better performance of the LSTM approach, the model attained a training accuracy of 90.98%, a testing accuracy of 80.00%, and a micro-average ROC- AUC score of 0.92. These results show that the model outperforms conventional machine learning techniques in capturing contextual and sequential textual aspects.

---


### 15. [Graph-Regularized Deep Learning for EEG-Based Emotion Recognition with Psychologically-Grounded Label Structure](https://arxiv.org/abs/2607.07773)

**<font color=#1a73e8>作者：</font>** Dongyang Kuang, Zizheng Ma, Yushan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG-based emotion recognition is critical for mental health monitoring and affective brain-computer interfaces, yet existing deep learning approaches often treat emotion classes as isolated labels, ignoring their psychological interdependencies. We propose a graph-regularized learning framework that conceptualizes emotions as nodes in a graph where edges encode proximity based on dimensional emotion theories. We adapt three complementary regularization strategies--Graph Label Smoothing (intuitive soft labeling), Commuting distance on graph via Graph Laplacian (spectral graph theory), and Sliced Wasserstein Distance (optimal transport on graph)--ordered by increasing computational complexity. These strategies penalize model predictions that deviate from the established emotion topology. Our framework is evaluated across three representative backbone architectures: AudioTransformer (pure transformer), Conformer (CNN-transformer hybrid), and DCGNN (causal graph neural network), demonstrating architecture-agnostic benefits. Experiments on SEED-IV (4 classes) and SEED-V (5 classes) datasets show consistent improvements: best case up to +5.42% accuracy and 39% reduction in psychologically implausible misclassifications. Ultimately, our framework help raise the upper bound of performance achievable with standard approaches. Code will be released.

---


### 16. [ScopeJudge: Cost-Aware Pre-Execution Gating for Offensive Security Agents](https://arxiv.org/abs/2607.07774)

**<font color=#1a73e8>作者：</font>** Shane Caldwell, Max Harley, Ads Dawson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM agents take on offensive security work, a single out-of-scope tool call can breach a client's engagement boundary, disrupt production, or void a bug-bounty finding. Unlike a fixed safety policy, the boundary that matters is declared in the user's request and must be inferred from intent. That challenge is sharpened by the adversarial nature of offensive security: the same tool call is in or out of scope depending not on the action itself but on the target it touches and the context in which it runs, which no fixed policy can enumerate in advance. We study pre-execution gating: a cheap, trusted LLM judge inspects each call proposed by a strong, swappable agent, and accepts or rejects it before it runs. We introduce ScopeJudge, a benchmark of 4,897 tool calls (7.7% scope violations) from agent trajectories on tasks engineered to tempt agents out of scope and labeled at the call level by professional penetration testers, with substantial inter-grader agreement (Fleiss kappa = 0.64) that sets an expert agreement reference point of F1 = 0.78. We evaluate eight judge models under five transcript strategies, varying how much context the judge sees, from the static policy alone to the full raw transcript, and chart the resulting cost-accuracy Pareto frontier. We find that a static policy is structurally insufficient for scope enforcement: blind to the user's request, judge recall collapses to near zero, confirming that scope lives in the request and that request-conditioned monitoring is necessary. Because a missed violation costs more than a spurious rejection, we report precision, recall, and F1 separately and recommend two operating points: a cost-sensitive configuration and a recall-first one for high-stakes deployments. We release the ScopeJudge dataset to support real-time monitoring and scalable oversight of autonomous security agents.

---


### 17. [Idiobionics: The Unification of Privacy and Intelligent Robotic Prostheses](https://arxiv.org/abs/2607.07775)

**<font color=#1a73e8>作者：</font>** Kwesi Afari Darfoor, Patrick M. Pilarski, Bailey Kacsmar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The human body is at the center of a growing family of technologies designed to tightly and persistently couple biological and digital systems. Robotic prostheses are a representative example of this tight coupling. Also referred to as bionic limbs, robotic prostheses are devices that support people who have lost limbs in pursuing daily life activities such as walking and grasping objects. Bionic limbs are now perceptive and responsive owing to their integration with advanced sensors and artificial intelligence-based control approaches. Consequently, such robotic prostheses can now be viewed as semiautonomous wearable robotic systems that can co-adapt with their users. However, the same sensing and control advancements that increase the capability of robotic prostheses also introduce threat vectors that could be exploited by malicious entities to violate the privacy of users. To fully realize the benefits of next-generation bionic limbs, we maintain it is important to directly understand and address these privacy risks and the barriers they might present to user adoption. This paper therefore introduces a new line of inquiry we term idiobionics to holistically investigate issues at the intersection of privacy and intelligent bionic limbs. As the main contribution of this paper, we define idiobionics, ground it in related literature, and provide preliminary evidence showing and discussing potential adversarial attacks that could exploit intelligent bionic limb designs. We then contribute a curated list of open research questions within idiobionics that are relevant to researchers in wearable robotics and other human-facing autonomous systems. We expect that idiobionics research will help unlock the full potential of robotic prostheses and related bionic devices.

---


### 18. [A law of robustness for two-layer neural networks with arbitrary weights](https://arxiv.org/abs/2607.07778)

**<font color=#1a73e8>作者：</font>** Yitzchak Shmalo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bubeck, Li and Nagaraj conjectured that, for generic data, any two-layer neural network with $m$ neurons that fits $n$ noisy labels must have Lipschitz constant at least of order $\sqrt{n/m}$, with no restriction on the size of the weights. Bubeck and Sellke proved a universal version of this law for Lipschitz-parameterized classes, but under a polynomial bound on the parameters; at depth three that boundedness hypothesis is genuinely necessary. The two-layer unbounded-weight case requires a different argument. We prove the conjectured law, up to one logarithmic factor, for every continuous piecewise-linear activation, in particular for ReLU networks. For data drawn uniformly from $\mathbb{S}^{d-1}$, $d\ge3$, or from $N(0,I_d/d)$, labels in $[-1,1]$ with noise level $\sigma^2>0$, and any width-$m$ two-layer network with arbitrary real weights, biases and affine skip connection, fitting the data $\varepsilon$ below the noise floor forces $\mathrm{Lip}(f)\ge c\,\varepsilon\sqrt{n/(\bar m\log(C\bar m nd/\varepsilon))}$, $\bar m=(K-1)m+1$, with high probability. A realized-kink-count version holds on the same event: every realized two-layer piecewise-linear function with $k(f)\le n$ distinct kink hyperplanes obeys the bound with $\bar m$ replaced by $k(f)+1$, irrespective of how many redundant hidden units parameterize it. The proof replaces parameter-space covering, impossible for unbounded weights, by a function-space covering. The central deterministic ingredient is a rigidity lemma: on $B_2$, and on $\mathbb{S}^{d-1}$ for $d\ge3$, the coefficient of each canonical kink is controlled by the Lipschitz constant of the realized function, because kinks on distinct hyperplanes cannot cancel at generic points. Rigidity genuinely fails at $d=2$, and an explicit two-layer ReLU interpolant with $O(1)$ Lipschitz constant at width $2n$ matches the law at the overparameterized endpoint.

---


### 19. [DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment](https://arxiv.org/abs/2607.07820)

**<font color=#1a73e8>作者：</font>** Xinyu Geng, Xuanhua He, Sixiang Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training tool-use agents to improve from their own experience remains challenging, as supervised fine-tuning relies on fixed teacher-distilled trajectories, while sparse-reward reinforcement learning provides weak supervision for long-horizon interactions. We present DeepSearch-Evolve, a self-distillation framework for web agents built on DeepSearch-World, a deterministic and verifiable environment with reproducible search and page-reading tools. DeepSearch-World contains 420K multi-hop QA tasks constructed from entity-level random walks and supports key agentic cognitive behaviors useful for self-evolving, including progress verification, grounded reflection, and failure recovery. DeepSearch-Evolve iteratively performs trajectory generation, filtering, data mixing, and fine-tuning to train stronger agents. Without distillation from more capable models, DeepSearch-World-9B achieves competitive performance compared with open-source agents, reaching 31.2% on BrowseComp, 61.5% on GAIA, and 93.4% on HotpotQA, showing that verifiable environments enable scalable self-evolution for long-horizon web agents. We will release the environment, 420K training pool, validation set, model, and code to facilitate future research on self-improving deep search agents.

---


### 20. [From Triggers to Emotions: A CPM-Grounded Appraisal Multi-Agent for Dynamic Emotional Evolution in Persona-Based Dialogue](https://arxiv.org/abs/2607.07824)

**<font color=#1a73e8>作者：</font>** Jingyao Cai, Shuaijun Liu, Abdul Rehman 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have substantially advanced persona-based dialogue agents for emotion-sensitive role simulation in healthcare, education, counseling, customer service, and interactive storytelling. However, two related lines of work leave a key gap. Persona-based dialogue systems often encode emotions as static traits or surface-level stylistic cues, and affective dialogue research has largely focused on empathetic response generation toward users rather than modeling the agent persona's own evolving emotional state. As a result, trigger-driven emotional evolution within a character remains underexplored. To address this limitation, we draw inspiration from the Component Process Model (CPM), a psychological theory that views emotion as a dynamic process shaped by the appraisal of external events. We propose CPM-MultiAgent, a CPM-grounded emotion evolution multi-agent framework for supporting emotional changes in persona-based dialogue. Instead of treating a character's emotion as a fixed attribute, CPM-MultiAgent represents it as a latent state that is continuously reshaped by dialogue triggers. Through affective trigger extraction, CPM-based collaborative appraisal, and emotion state updating, the framework enables more emotionally consistent role simulation in multi-turn this http URL with baseline comparisons, ablation studies, human evaluation, and case analyses demonstrate that CPM-MultiAgent effectively models dynamic emotional evolution in emotionally sensitive role-simulation settings.

---


### 21. [Open Models, Open Risks: Measuring Unsafe Generation in Text-to-Image Models In the Wild](https://arxiv.org/abs/2607.07827)

**<font color=#1a73e8>作者：</font>** Peilin Han, Yang Liu, Yilong Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing safety studies on text-to-image (T2I) jailbreaks are largely conducted in controlled in-the-lab settings, typically on a small number of canonical models. As a result, the current safety status of the rapidly growing in-the-wild T2I ecosystem remains unclear. This uncertainty is amplified by two factors: existing detector-based metrics are designed for controlled evaluation, and in-the-wild risks may arise not only from adversarial prompting, but also from unsafe release practices and unsafe model derivatives.
In this paper, we present a large-scale empirical study of in-the-wild T2I safety through the lens of jailbreak. We first show that detector-only jailbreak metrics substantially overestimate practical risk over in the wild due to semantic drift and generation artifacts, and we introduce Advanced ASR to better capture semantically valid and visually plausible unsafe generation. Using this refined metric, we evaluate 200+ in-the-wild T2I models from Hugging Face under three representative jailbreak attacks. Our results show that many downstream models retain a non-trivial degree of safety even without explicit post-hoc safeguards, indicating that safety degradation in the wild is neither universal nor uniform. At the same time, we identify a set of high-risk models, including explicitly NSFW-oriented releases as well as seemingly benign models whose unsafe behavior is only exposed through systematic evaluation. We further trace these models to their release context and report high-risk cases to Hugging Face.

---


### 22. [Predicting Pseudo-nitzschia harmful algal blooms along the Portuguese Coast using satellite-derived predictors](https://arxiv.org/abs/2607.07834)

**<font color=#1a73e8>作者：</font>** Ayman Bnoussaad, El Khalil Cherif, Ligia Pinto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pseudo-nitzschia diatoms pose recurrent risks to coastal ecosystems and shellfish harvesting along the Portuguese Atlantic coast. Here we develop and evaluate a spatio-temporal machine-learning framework to predict harmful algal bloom (HAB) occurrence using exclusively satellite-derived predictors under realistic forecasting constraints. We characterised environmental and biological variability across shellfish production zones (L1-L9) using 5,882 observations, providing system-wide context. Predictive models were developed for zones L1-L2, a hotspot for Pseudo-nitzschia and domoic acid events, using a decade-long dataset (2013-2023; 1,440 observations; more than 1,000 satellite-based predictors including sea surface temperature, an upwelling index, chlorophyll-a, and plankton functional types). Sampling locations were partitioned into ecologically meaningful sub-regions using a river-aware spatial clustering scheme. A stringent spatio-temporal cross-validation strategy that simultaneously withholds entire years and spatial clusters prevents leakage and closely mimics real-world forecasting conditions. HAB occurrence proved moderately predictable across model classes and feature configurations. Ensemble tree-based methods achieved the strongest discrimination: Random Forest reached 0.74 +/- 0.05 with environmental predictors; Extra Trees reached 0.77 +/- 0.06 with biological variables added. Feature-importance analyses revealed that seasonal structure, spatial context, and lagged environmental conditions dominate model decisions, while biological indicators refine bloom likelihood within physically favourable periods. The framework demonstrates operationally relevant skill for satellite-supported HAB early-warning systems along eastern boundary upwelling coasts.

---


### 23. [Infinity-Parser2 Technical Report](https://arxiv.org/abs/2607.07836)

**<font color=#1a73e8>作者：</font>** Zuming Huang, Jun Huang, Kexuan Ren 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Infinity-Parser2, a large multimodal model that couples a controllable data-synthesis pipeline with multi-task reinforcement learning for end-to-end document parsing, addressing the persistent scarcity of faithfully annotated parsing corpora. Our contributions are threefold. First, we build a scalable synthesis engine, pairing a controllable rendering framework with an iterative refinement loop, and use it to construct and open-source Infinity-Doc2-5M: a 5-million-sample bilingual (Chinese/English) corpus spanning diverse document types, annotated with element bounding boxes, canonical content forms (Markdown, HTML, LaTeX, SMILES, structured charts), and full-page reading order. Second, we introduce a verifiable, multi-task reward system that enables Joint Reinforcement Learning across eight co-trained objectives (document parsing, layout analysis, table parsing, math formula parsing, chart parsing, chemical formula parsing, document VQA, and general multimodal understanding), unifying perception, structure, and reasoning in a single optimization signal. Third, we release two variants under a shared architecture: Infinity-Parser2-Flash, optimized for low-latency inference with a $3.68\times$ throughput gain over Infinity-Parser-7B, and Infinity-Parser2-Pro, engineered for precision-critical settings. Infinity-Parser2-Pro reaches state-of-the-art 87.6% on olmOCR-Bench and 74.3% on ParseBench, surpassing DeepSeek-OCR-2, PaddleOCR-VL-1.5, and MinerU2.5, with strong generalization to charts, chemical formulas, and document VQA.

---


### 24. [Explaining Near-Zero Hessian Eigenvalues Through Approximate Symmetries in Neural Networks](https://arxiv.org/abs/2607.07845)

**<font color=#1a73e8>作者：</font>** Marcel Kühn, Bernd Rosenow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Hessian of the training loss governs the local geometry of the loss landscape, yet despite existing explanations for its largest eigenvalues, the origin of the vast multitude of vanishingly small eigenvalues remains elusive. We argue that the bulk consists of the weakly lifted pseudo-Goldstone modes of the continuous symmetries of the network parametrization. In deep linear networks these symmetries are exact: they generate flat directions and hence exact zero modes, whose eigenvectors we construct explicitly. Introducing a ReLU nonlinearity as a perturbation, we show that it breaks these symmetries weakly and explicitly. Resolving the spectrum at the level of eigenvectors, we find that the high-curvature directions are orthogonal to the symmetry subspace, while the bulk lies almost entirely within it. We demonstrate the mechanism in a two-layer ReLU student--teacher model and in a network trained on CIFAR-10. A convolutional example demonstrates that the same diagnostic extends beyond fully connected layers. Together, these results link the Hessian bulk to weakly broken symmetries and clarify the origin of near-zero modes.

---


### 25. [A Graph Neural Network Model for Real-Time Gesture Recognition Based on sEMG Signals](https://arxiv.org/abs/2607.07850)

**<font color=#1a73e8>作者：</font>** Pragatheeswaran Vipulanandan, Kamal Premaratne, Manohar Murthi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For seemless control of advanced hand prostheses and augmented reality, accurate and immediate hand gestures recognition is essential. Surface electromyography (sEMG) signals obtained from the forearm are commonly employed for this purpose. In this paper, we present a novel approach for sEMG representation that utilizes graph networks which contain information about muscle activation patterns in the forearm. Based on these graph networks, we have developed a machine learning algorithm capable of real-time hand gesture recognition using a graph neural network. The algorithm's performance was evaluated using sEMG signals acquired from myoband, which has 8 electrodes placed around the forearm, involving 8 healthy subjects. The proposed method demonstrated an average classification accuracy of 99\%, surpassing the performance of state-of-the-art techniques. The average time for both graph construction and prediction stood at 48ms utilizing a M1 pro CPU, rendering the approach well-suited for real-time applications.

---


### 26. [Physics-Informed Machine Learning Under Small-Data Constraints: Lessons from Abrasive Waterjet Milling](https://arxiv.org/abs/2607.07863)

**<font color=#1a73e8>作者：</font>** Sarah Grewe, Jörg Frochte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In physically dominated machining processes, experimental datasets are small, expensive, and material-specific; in this regime, data curation, evaluation design, and the form of physics integration can matter as much as the learning algorithm. Using an abrasive waterjet milling dataset ($n{=}155$, Inconel\,718), we make three methodological contributions. First, we separate physics-based data \emph{cleaning} from statistical \emph{curation} and treat the latter as competing modelling hypotheses rather than silent preprocessing. Second, we find that model rankings from a 15-point hold-out set can be unstable: the single-split winner drops from rank~1 to rank~7 under 10-fold cross-validation, while Gaussian Process (GP) variants occupy the top ranks. Third, we study a spectrum of physics integration levels and find that residual learning on a compact physics baseline is competitive for GP, yielding lower variance and an interpretable decomposition, but degrades tree-based models. Bayesian hyper parameter tuning improves parameter-sensitive baselines such as gradient boosting and SVR, yet harms multi-stage hybrid pipelines at this sample size. GP uncertainty intervals are approximately calibrated ($86\%$ empirical coverage at nominal $90\%$). The resulting picture is methodological: for small, expensive process datasets, our results suggest that, in this setting, reliable model comparison benefits from explicit curation hypotheses, robust evaluation, and careful choices about how physics enters the model.

---


### 27. [GIRAF: Towards Generalizable Human Interactions with Articulated Objects](https://arxiv.org/abs/2607.07880)

**<font color=#1a73e8>作者：</font>** Xiaohan Zhang, Sebastian Starke, Alexander Winkler 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing realistic full-body human interactions with articulated objects is a fundamental challenge for embodied AI and graphics, with applications in robotics training and virtual agents. Existing models remain limited: some focus on simple activities with static objects, while others restrict attention to hand-only manipulation. This leaves open the problem of generating coordinated full-body motion that approaches, manipulates, and moves articulated objects in a realistic and generalizable way. The key difficulty lies in reasoning jointly about locomotion, fine-grained contact, and object articulation. Models must capture subtle hand-object correspondences that transfer across object geometries, while also producing seamless transitions from navigation to manipulation. At the same time, the scarcity of large-scale paired motion-scene data makes it difficult to generalize across diverse object positions and shapes. We introduce a text-conditioned diffusion model that addresses these challenges through three core ideas: an object-centric representation that unifies hand-object contact with object surfaces, a mixed-domain training strategy that balances locomotion and interaction, and a contact-based augmentation scheme that expands training diversity. Through experiments, our method demonstrated strong generalization to unseen object configurations, surpassing current state-of-the-art methods.

---


### 28. [Nigeria Machinery: A Low-Resource Industrial Dataset with a Domain-Grounded Reasoning Layer](https://arxiv.org/abs/2607.07883)

**<font color=#1a73e8>作者：</font>** Gospel Bassey, Vincent Fakiyesi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There is relatively little, public, and model-ready data on industrial machinery for African economies. This makes it hard to do quantitative analysis or to train language models on numeric tasks grounded in that setting. We release two things to help with part of this problem. The first is the Nigeria Machinery Usage and Failures Dataset: 89 machine-level records across 28 indicators, covering Nigeria's manufacturing and oil and gas sectors from 2006 to 2025. Every record names a public source and is decoded by a codebook. The second is a method for building chain-of-thought (CoT) reasoning examples from these sparse numeric values. The result is 94 prompt, completion, and reasoning-trace rows. In every row, the prompt names the real indicator, subsector, year, and source of the record it comes from. The data adaptation work was carried out by Adaption Labs. Along the way we describe a problem that is common when language models are used to build datasets. The prompts can match the real numbers while saying nothing about the real domain. We show that fixing this raises the share of domain-grounded prompts from 1 out of 78 in an earlier release to 94 out of 94, and that every retrieval answer now matches its source value (84 out of 84). We release the data, the reasoning layer, and a per-row provenance file under CC-BY-4.0. We are clear about the limits. With 89 records and 17 indicators that have only one observation, this is a reference and seed dataset, not a large training set. Most reasoning rows are retrieval rather than multi-step computation.

---


### 29. [Optimal Learning Rate Scaling Depends on Data in Deep Scalar Linear Networks](https://arxiv.org/abs/2607.07884)

**<font color=#1a73e8>作者：</font>** Yedi Zhang, Peter E. Latham, Leena Chennuru Vankadara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this short note we consider the gradient descent dynamics of deep scalar linear networks, $f(x) = \prod_{l=1}^L w_l x$, which enjoy exact time-course solutions for any integer depth. We show that even in this minimal model, the optimal depth-wise learning rate scaling depends on data, whereas data-agnostic scaling rules fail to transfer across depths. Under the data-dependent optimal scaling, the learning dynamics is independent of data and weakly dependent on depth, resulting in a constant linear convergence rate across all depths including infinity. We further show similar data-dependent effects in deep scalar linear networks with residual connections.

---


### 30. [Distributed Sketching on Data Partitions for OLS Regression](https://arxiv.org/abs/2607.07888)

**<font color=#1a73e8>作者：</font>** Luyuan Yang, Brayden Garner, Shayan Shafaei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies distributed sketching for ordinary least squares (OLS) regression, an approach that distributes small sketches of a large data set over multiple machines to separately construct OLS estimators and average them. Unlike prior studies that consider sketching on the whole data set, we consider sketching on partitioned subsets to further reduce computational cost. Under the fixed design setting, we characterize the exact excess loss of the averaged OLS estimator. Results show that this loss is comparable to the established loss for sketching on the whole data set when the divergence among subset covariances is small.

---


### 31. [How Do I Know What to Say Next? Barenholtz's Autogenerative Theory as an Enrichment of Harrisean Integrationism](https://arxiv.org/abs/2607.07891)

**<font color=#1a73e8>作者：</font>** J. Mark Bishop, Stephen J. Cowley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Roy Harris's Integrationist linguistics offers a compelling critique of the referentialist tradition embedded deep at the heart of computational approaches to language, arguing that language is not a code that maps onto a pre-given world but a situated, bipartite activity oriented toward prospective joint action. Yet Integrationism leaves certain explanatory gaps: it does not fully account for the structural mechanism by which signs sustain prospective openness, it undertheorises the continuity between linguistic and non-linguistic semiotic activity, and it offers no detailed account of the structural properties of the accumulated archive of past integrations. This paper argues that Elan Barenholtz's autogenerative theory of language, developed in response to the behaviour of Large Language Models (LLMs), can fill precisely these gaps, enriching Integrationism without undermining any of its core commitments. Specifically, the autogenerative account provides: a structural mechanism for the prospective openness that Harris identifies as central to bipartite communication; a computational correlate for Harris's thesis of semiotic continuity between language and other sign-making activity; and a theory of the archive: what the accumulated residue of past integrations looks like and how new participants draw upon it. The synthesis preserves Harris's ontological primacy of the situated integrative act while adding explanatory content that Integrationism itself does not supply. For practitioners and researchers in natural language processing and large language model design, the argument offers a principled account of what the statistical structure that LLMs so effectively exploit actually is, and of what it cannot, by its nature, provide.

---


### 32. [Closed-Loop Dynamic Validator Node Scaling in Private Substrate Blockchains Using Takagi-Sugeno Fuzzy Inference](https://arxiv.org/abs/2607.07901)

**<font color=#1a73e8>作者：</font>** Thandile Nododile, Ayinde M. Usman, Clement N. Nyirenda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Private blockchain networks run with fixed node configurations that cannot adapt to changing workload conditions. Too many nodes serving a light workload waste resources; too few nodes facing heavy demand slow block production and degrade finalisation. The right validator count is hard to determine, as it depends on overlapping factors that shift over time. This paper presents a Takagi-Sugeno (TS) fuzzy inference system that reads live blockchain parameters (block production time, block size, and active node count) and outputs a continuous efficiency score alongside a scaling recommendation: Scale Up, Maintain, or Scale Down. The controller uses triangular membership functions across three linguistic variables, evaluated through a complete 27-rule base with product t-norm aggregation. A key contribution is an empirical recalibration of the membership functions, anchoring linguistic terms to the observed operating range of the testbed rather than to theoretical extremes. The system is evaluated on a 10-node Substrate blockchain network storing real smart water meter data hashes from the Queensland Government open data portal. Statistical analysis across configurations of 4, 7, and 10 active nodes confirms that the controller produces distinct operational profiles reflecting each configuration's provisioning state. In closed-loop experiments, the controller autonomously adjusts validator participation in both directions, activating validators under rising load and removing them under over-provisioning, converging to the same stable equilibrium from both directions. Compared against three threshold-based baselines, it shows fewer scaling oscillations while maintaining comparable block production times. Results show that TS fuzzy inference can support autonomous validator management in private blockchain deployments, with stable scaling behaviour threshold approaches cannot match.

---


### 33. [3D Reconstruction of deciduous Trees using low-cost UAV- and Crane-based Photogrammetry for Monitoring Shoot Elongation across entire Canopies](https://arxiv.org/abs/2607.07905)

**<font color=#1a73e8>作者：</font>** Stephan Nebiker, Micha Tschanz, Nando Amport 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tree growth determines how much CO2 is sequestered from the atmosphere and temporarily stored in woody biomass. At the same time tree growth is affected by increasing temperatures, more frequent drought periods, late frosts and other extreme events associated with climate change. While continuous measurements of radial (secondary) tree growth using dendrometers are well established, monitoring of shoot elongation (primary growth) has largely been neglected because suitable measurement techniques are lacking. As a result, the effects of climate change on primary tree growth remain insufficiently understood. This work aims at reconstructing native deciduous trees in 3D as a basis for measuring and monitoring shoot elongation over entire tree canopies. Here we explored the use of low-cost UAV photogrammetry and of a multi-camera CraneCam system under real-world conditions. Data were collected in two study areas over an entire growing season. We present sensor evaluations, photogrammetric data acquisition and processing strategies. A special focus is placed on the analysis of the resulting photogrammetric 3D point clouds in terms of accuracy, resolution and completeness. Results demonstrate 3D point accuracies of 5-6 mm for entire trees using consumer-grade UAVs weighing less than 250 g and a 3D reconstruction completeness between 92% and 98% depending on the UAV type. The paper introduces a novel 3Dprinted ground-truth branch to evaluate the capability to reconstructing fine-detail structures such as thin tree shoots. Finally, we discuss operational challenges and initial experiments towards a skeletonization of entire trees based on photogrammetric point clouds.

---


### 34. [Adversarial Decoys: Misdirecting Attention-Based Defenses in ViT](https://arxiv.org/abs/2607.07922)

**<font color=#1a73e8>作者：</font>** Giulia Marchiori Pietrosanti, Giulio Rossolini, Giorgio Buttazzo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) remain vulnerable to localized adversarial attacks, e.g., adversarial patches, while recent test-time defenses mitigate them by suppressing image tokens with abnormally high attention scores. These defenses exploit a strong coupling between attention and adversarial effectiveness: adversarial tokens often need to attract substantial attention to influence the prediction. We introduce adversarial decoys, independently optimized image patches that redirect the attention, and therefore related defenses, toward selected target tokens. Rather than jointly optimizing misclassifications and defense evasion, our approach decouples the two objectives: the original adversarial region induces the incorrect prediction, while a separate decoy manipulates the attention ranking used by the defense. A layer-wise objective increases target-token attention and promotes these tokens above competing non-target ones. Since the decoy is optimized independently of the underlying attack, the method is attack-agnostic and can be easily integrated with any existing adversarial patch attack. Experiments on ImageNet across multiple ViT architectures and attacks show that decoys can redirect high attention scores away from the true adversarial region while preserving much of the attack effectiveness. These results reveal a fundamental limitation of using attention magnitude as an indicator of adversarial relevance.

---


### 35. [KS-CFA: Control-Flow Attestation via Symbolic Replay Against Control-Flow Bending Attacks](https://arxiv.org/abs/2607.07926)

**<font color=#1a73e8>作者：</font>** Zhanyu Sha, Konstantinos Markantonakis, Carlton Shepherd 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Control-flow attestation (CFA) enables a remote entity to verify program execution on a target device by monitoring control-flow behaviour at runtime. However, control-flow bending (CFB) attacks remain difficult to detect, where an adversary steers execution along legal edges of the program's control-flow graph by corrupting branch flags, loop counters, and other runtime data. Existing solutions impose significant drawbacks: they require enumerating vast measurement spaces, cover only a reduced subset of attacks, or rely on low-level hardware modifications. In this work, we present KS-CFA, a new CFA scheme that detects CFB attacks across four transfer types (indirect calls, conditional and indirect jumps, and returns) without those costs. To this end, we combine symbolic execution and selective identification of input-sourced control-flow dependent variables: a strict subset of control-flow-relevant state whose values are directly read from external input. The proving device records, inside a trusted execution environment (TEE), a control-flow trace and the external inputs that determine relevant run-time variables. The verifier then replays the reported path through single-path symbolic execution, predicting each transfer and localising divergences that signal an attack. We implement and evaluate KS-CFA using the RISC-V Keystone TEE and Embench-IoT on QEMU and a Rocket-based FPGA platform (NiteFury II). Prover-side overhead relative to unattested execution ranges from 6.8-20.5x on QEMU and 6.7-32.2x on the FPGA, and verification requires no path or value enumeration.

---


### 36. [path_boost: A Python Package for Interpretable Graph-Level Prediction using Path-Based Gradient Boosting](https://arxiv.org/abs/2607.07935)

**<font color=#1a73e8>作者：</font>** Claudio Meggio, Johan Pensar, Riccardo De Bin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present path_boost, a Python package for interpretable supervised learning on graph-structured input data. The package implements PathBoost, a gradient boosting algorithm that automatically discovers predictive labeled paths within graphs during the learning process. Unlike graph neural networks, which are generally difficult to interpret, PathBoost produces an additive prediction model over path-based features that explicitly reveals which substructures drive predictions. To avoid an exhaustive enumeration of all possible paths, the algorithm iteratively selects and extends paths during learning based on their predictive power, using boosting to combine weak learners into a strong ensemble. The package supports both regression and binary classification. Key features include compatibility with scikit-learn workflows, support for custom base learners and selectors, automatic starting node selection, parallel training across anchor nodes, and built-in variable importance computation. We demonstrate PathBoost on molecular property prediction of transition metal compounds, where atoms serve as nodes and bonds as edges, and further benchmark PathBoost against an established graph neural network and a graph kernel method across six molecular datasets. The package is available on PyPI and GitHub under an open-source license.

---


### 37. [When Debiasing Backfires: Counterintuitive Side Effects of Preprocessing-Based Stereotype Mitigation](https://arxiv.org/abs/2607.07937)

**<font color=#1a73e8>作者：</font>** Yahan Zheng, John Guerrerio, Soroush Vosoughi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preprocessing-based methods for stereotype mitigation, such as pre-/post-training on debiased corpora, are widely used in NLP. While these approaches reduce measurable stereotypes for targeted groups, we find they often induce unintended shifts-side effects, where stereotyping or counter-stereotyping can increase relative to neutral baselines for other demographics, including across unrelated demographic categories. We demonstrate these side effects across two model families (encoder-only and decoder-only), multiple preprocessing strategies (removing stereotypical sentences, removing group mentions, and swapping group references), and both pre- and post-training at different data scales on Wikipedia. Standard benchmarks frequently miss these shifts. Using attention-rollout analysis, we observe that such side effects are not accompanied by large changes in attention flow, complicating mechanistic explanations. We discuss implications for evaluation, provide actionable diagnostics, and argue for side-effect-aware, transparent mitigation practices.

---


### 38. [fog: Expressing Motion and Emotion through Function Composition of AI-Generated Code](https://arxiv.org/abs/2607.07952)

**<font color=#1a73e8>作者：</font>** Vivian Liu, Lydia Chilton  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Motion and emotion are core parts of intelligent, expressive behavior. In this paper, we introduce fog, a function composition framework for implementing and compose motion functions. We demonstrate how fog can be used to express motion and emotion in Heider-Simmel style animations. This code generation framework can help users generate functions for verbs, adverbs, gestures, and emotions to create an open-ended motion vocabulary. It is complemented by an animation editor that helps users refine motion through direct manipulation and dynamically generated UI. We evaluate our approach with a perceptual evaluation, where we test 452 fog-generated animations to see if people can recognize the semantic meaning of the motion. We find that fog's motion functions can be recognized at 68% accuracy, a 2.68x improvement over a chance baseline. In a mixed-methods user study with professionals and novices, we show that fog in interface form can support users with more rapid iteration, exploration, and control.

---


### 39. [Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing](https://arxiv.org/abs/2607.07953)

**<font color=#1a73e8>作者：</font>** Tommaso Cerruti, Tim Rieder, George Rowlands 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention lets each token retrieve information from the full context, but its quadratic cost in sequence length limits training and inference at long context. This paper presents a comparative study of softmax attention and four recent recurrent linear-attention architectures: DeltaNet, Gated DeltaNet, Kimi Delta Attention, and Gated DeltaNet-2. We express these mechanisms in a common recurrent-memory notation, making explicit how they differ in expressivity, memory decay, erase and write control, training throughput, and implementation complexity. Our experiments center on 350M-parameter models trained for 15B tokens, and include optimizer and learning-rate comparisons, hybrid-versus-pure stack comparisons, sequence-length runtime measurements, larger DeltaNet runs at 1.3B and 3B parameters, and a small set of downstream evaluations. The reported speed results measure training throughput and iteration time; we do not provide an empirical inference-speed benchmark. Within the reported 350M-parameter, 15B-token sweep, Kimi Delta Attention with Muon reaches the lowest final validation loss, a pure Gated DeltaNet stack trained with AdamW has the highest normalized training throughput, hybrid stacks generally improve loss at a throughput cost, and Muon consistently lowers final validation loss relative to AdamW in the matched architecture settings we evaluate. We introduce and evaluate lightweight cross-layer routing mechanisms for DeltaNet-style memories. The most natural DeltaNet-inspired formulation, forwarding a lower layer's delta-rule write error into the next layer's value target, does not improve over matched baselines. Routing into the aligned hidden stream and forwarding the write value instead yields a modest improvement in the matched runs we report: Cross-Layer Value Routing (CLVR) lowers final validation loss for both DeltaNet and Gated DeltaNet.

---


### 40. [Evaluating the Effect of Frame Rate in Sequence-Based Classification of Autism-Related Self-Stimulatory Hand Idiosyncrasies](https://arxiv.org/abs/2607.07957)

**<font color=#1a73e8>作者：</font>** Raunak Mondal, Peter Washington  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autism spectrum disorder (ASD) affects over 75 million individuals worldwide, yet scalable computational methods for remote behavioral screening remain limited. This study addresses two complementary challenges in automated detection of autism-related self-stimulatory behaviors from video: (1) identifying the optimal sequence-based neural network architecture and temporal sampling rate, and (2) characterizing data augmentation strategies for training on small behavioral datasets. For the first objective, long short-term memory (LSTM) and gated recurrent unit (GRU) models were trained on pose-derived features from the Self-Stimulatory Behavior Diagnosis (SSBD) dataset at frame sampling intervals of 1, 5, 15, 30, 45, and 90 frames. Both architectures exceeded prior convolutional neural network (CNN) baselines (62-76% accuracy), with peak accuracies of 97.5% (LSTM) and 98.75% (GRU) at a sampling interval of every 15 frames. For the second objective, ten data augmentation strategies were applied to an I3D transfer learning pipeline, with an ablation study quantifying the marginal contribution of each technique. Horizontal flip achieved the highest standalone accuracy (48.78%), while exclusion of upsampling from the augmentation pipeline produced the largest performance degradation, indicating its necessity for complex behavioral video augmentation. A personalized machine learning approach, in which per-subject models were trained and tested on temporally split segments of each video, produced consistent predictions (mean loss 1.84, SD 0.79). These results provide practitioners with concrete guidance on architecture selection, sampling rate, and augmentation strategy for video-based behavioral classification in data-scarce clinical domains.

---


### 41. [The Behavioural Reflection Test: A time-efficient measure of reflective reasoning in morally and epistemically charged decisions](https://arxiv.org/abs/2607.07961)

**<font color=#1a73e8>作者：</font>** Sion Weatherhead, Flora Salim, Aaron Belbasis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> How readily people override intuitive conclusions through reflection shapes how they navigate dense information environments with reliable and misleading sources; yet the effectiveness of a prominent measure, the Cognitive Reflection Test (CRT), is eroded by widespread exposure to classic items and leaves open how such tendencies manifest more generally in decision style and linguistic expression. The Behavioural Reflection Test (BRT) addresses these issues with a brief open-ended measure of reasoning in morally and epistemically charged scenarios, alongside a four-item bespoke CRT (bCRT) as a low-exposure anchor. Among 473 online adults, higher bCRT predicted more evidence-sensitive, ethically driven decisions and reliance on high-quality sources, marked by more emotionally engaged, risk-attentive, economical language; associations the familiarity-adjusted CRT did not recover. The bCRT showed convergent validity, added item information above mean ability. Though open-ended, the BRT remained a time-efficient (median 11.8 minutes) behavioural assay of reflection with scope to extend across domains.

---


### 42. [Beyond Thermal Imaging: Inferring Thermophysical Properties from Time-Resolved Thermal Observations](https://arxiv.org/abs/2607.07962)

**<font color=#1a73e8>作者：</font>** Chenghao Xu, Malcolm Mielle, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inferring latent physical properties from sensory observations is a fundamental challenge in machine perception. Among available sensing modalities, thermal imaging is particularly promising because temperature evolution is directly governed by heat-transfer physics and therefore encodes information about underlying thermophysical properties of a scene. Recovering spatially resolved thermophysical properties from thermal observations could transform applications ranging from digital twins and infrastructure monitoring to robotics and scientific imaging. However, existing thermal scene reconstruction methods can recover temperature fields in complex 3D environments without identifying the thermophyiscal properties that govern thermal evolution, whereas inverse methods provide physically interpretable parameter estimation but typically rely on simplified geometries and controlled experimental conditions.
Here we introduce ThermoField, a framework that unifies thermal scene reconstruction and thermophysical parameter estimation through differentiable heat-transfer simulation. The proposed framework represents these quantities as spatially varying neural fields and constrains them through scene geometry, governing heat-transfer physics, and temporal thermal observations. We demonstrate that ThermoField jointly reconstructs geometry, estimates spatially varying thermal diffusivity, and predicts thermal evolution under previously unseen environmental conditions. By integrating neural scene representations with differentiable heat-transfer solver, the framework enables physically interpretable parameter inference in complex 3D scenes. Our results establish a bridge between thermal scene reconstruction and inverse heat-transfer analysis, providing a unified approach for geometry reconstruction, thermophysical property estimation, and predictive thermal simulation from thermal observations.

---


### 43. [A Multi-cluster Boundary Learning Method for Out-of-Scope Intent Detection via MiniLM Embedding](https://arxiv.org/abs/2607.07974)

**<font color=#1a73e8>作者：</font>** Yihong Xu, Mingyu Kang, Linyuan Lü  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Intent detection is a critical task that bridges human intents and system actions in human-machine interaction systems. However, there still exist challenges for detecting out-of-scope (OOS) intents. (i) The traditional methods view the OOS intent detection as a multi-class classification, then the detection accuracy decreases as the class number of the known intents increases; (ii) LLM-embedding methods require large parameters, that makes them difficult to train and practically deploy. Thus, this work proposes a multi-cluster boundary learning method to detect OOS intents via MiniLM embedding (i.e., all-MiniLM-L6-v2) in an one-class classification workflow. The method learns the boundaries of multi-cluster embeddings generated by MiniLM from the training utterances, and then rejects the out-of-domain utterances as OOS intents. Experiments are conducted on public CLINC150, StackOverflow and Banking77 datasets. The results show that the method achieves the state-of-the-art OOS intent detection performance compared the other baselines. Ablation studies are also conducted and the results show that the used MiniLM can better adapt to the workflow and utterance embedding requirements. The code is available at supplementary materials.

---


### 44. [A Reliability Assessment of LALM Audio Judges for Full-Duplex Voice Agents](https://arxiv.org/abs/2607.07985)

**<font color=#1a73e8>作者：</font>** A. Sayyad, J. Emmons, S. Jones 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report the empirical reliability of Gemini models as audio judges that score full-duplex agent conversations directly from the raw stereo waveform, tested across three models in the Gemini family: 2.5 Flash, 3.5 Flash, and 3.1 Pro. Our primary evidence base uses Gemini 2.5 Flash as the ground-truth model, validated against three calibrated human raters on 209 stereo sessions, scored on 8 production dimensions: 152 full-duplex conversations across 13 accent-and-condition strata, together with 57 adversarial defect-injected clips. The evidence for Gemini 2.5 Flash is consistent across three tests. (i) On 5 of 8 dimensions the LALM-human Spearman rho departs from the pairwise human-human rho by at most 0.07, and on 7 of 8 dimensions the two quantities 95 percent bootstrap confidence intervals overlap. (ii) The LALM agrees with the three-rater human mean within 1 point on 60 to 92 percent of sessions on 6 of 8 dimensions. (iii) On 45 of 48 (defect, dimension) cells the LALM is as sensitive as humans or better under Newcombe-Wilson 95 percent confidence intervals, though most of these are underpowered nulls rather than demonstrated parity. Rank-ordering ability transfers across the Gemini family: 3.5 Flash improves simple agreement to 8 of 8 dimensions, while 3.1 Pro rates several dimensions markedly lower than humans despite comparable rank correlation. A model swap should be re-validated on calibration specifically, not assumed from rank-correlation alone. We identify four areas where deployment requires care, and we estimate that human rating alone for our current evaluation cadence costs roughly two orders of magnitude more than the equivalent LALM workload. The data presented here provides a defensible empirical basis for deploying the LALM as a substitute or fourth rater on the dimensions where the evidence supports it.

---


### 45. [Hallucination Self-Play: Bootstrapping Reinforced Detector via Evolved Generator](https://arxiv.org/abs/2607.07993)

**<font color=#1a73e8>作者：</font>** Shiping Yang, Shining Liang, Weihao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying faithfulness hallucinations in LLM-generated outputs remains challenging due to the scarcity of high-quality annotated data. Recent work relies on advanced LLMs to synthesize training data, including rationales, labels, and hallucinated claims. However, these methods treat the generator as a static component, limiting iterative improvement of the detector. To address this limitation, we introduce Hallucination Self-Play (HSP), a novel framework that enables the detector to bootstrap with an evolved generator. HSP involves two roles initialized from the same base model, a detector that assesses the faithfulness of model outputs, and a generator that produces increasingly hard-to-detect hallucinated responses. Specifically, the detector is first fine-tuned on human-labeled data and then employed as a reward model to train the generator via reinforcement learning from AI feedback (RLAIF). In turn, the evolved generator synthesizes hallucination data to further optimize the detector through rule-based reinforcement learning. Experiments on RAGTruth benchmark and two model families demonstrate that the proposed framework can progressively enhance a small LLM to match or even outperform advanced LLMs without external supervision. Our code is available at this https URL .

---


### 46. [LOGOS: Language-guided Oriented Object Detection in Aerial Scenes](https://arxiv.org/abs/2607.08004)

**<font color=#1a73e8>作者：</font>** Trong-Thuan Nguyen, Minh-Triet Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection in geospatial scenes, such as satellite and aerial imagery, poses significant challenges due to the varying orientations and densities of objects, as well as the complex backgrounds inherent to remote sensing imagery. Traditional methods for oriented object detection have struggled to address issues such as angular discontinuity, fixed query sizes, and inefficiencies in handling sparse or cluttered scenes. In this paper, we propose LOGOS, a novel transformer-based approach that leverages textual prompts to guide the detection of oriented objects in aerial scenes. In particular, our proposed approach incorporates prompt-modulated content queries to dynamically adjust the model's focus based on the provided text, thereby improving object detection accuracy in complex environments. Empirically, extensive experiments on the DOTA dataset demonstrate that LOGOS outperforms existing state-of-the-art methods, particularly in densely packed and rotated object scenarios. Our approach offers a significant step forward in improving the robustness and scalability of oriented object detection in remote sensing applications.

---


### 47. [Provably Optimal Learning Algorithms for Assistance Games](https://arxiv.org/abs/2607.08012)

**<font color=#1a73e8>作者：</font>** Nivasini Ananthakrishnan, Mark Bedaywi, Michael I. Jordan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies an online variant of the assistance games framework, where an informed agent and an uninformed agent repeatedly interact over $T$ timesteps to optimize a common reward function. While the informed agent (the human) observes a latent state of the world, the uninformed agent (the assistant) observes only the human's actions. We provide the first provably efficient learning algorithms for repeated assistance games. We introduce the notion of assistance regret: the gap between the cumulative utility of interactions and that of the optimal joint policies in hindsight, which map latent states to action pairs. We present decentralized algorithms for both the human and the assistant that achieve a $(1-1/e)$-approximate assistance regret rate of $\widetilde{O}(T^{3/4})$, with runtime polynomial in the size of the action and state spaces. These algorithms are general; in particular, they accommodate any no-regret algorithm for the assistant. We prove that achieving a regret approximation factor better than $(1-1/e)$ is computationally intractable. Furthermore, we demonstrate how these generic no-regret algorithms can be tailored to a pseudo-decentralized setting -- using a shared random string -- to achieve a rate of $\widetilde{O}(T^{1/2})$, optimal up to logarithmic factors.

---


### 48. [Collate: Collaborative Neural Network Learning for Latency-Critical Edge Systems](https://arxiv.org/abs/2607.08013)

**<font color=#1a73e8>作者：</font>** Shuo Huai, Di Liu, Hao Kong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) empowers multiple clients to collaboratively learn a model, enlarging the training data of each client for high accuracy while protecting data privacy. However, when deploying FL in real-time edge systems, the heterogeneity of devices among systems has a severe impact on the performance of the inferred model. Existing optimizations on FL focus on improving the training efficiency but fail to speed up inference, especially when there is a latency constraint. In this work, we propose Collate, a novel training framework that collaboratively learns heterogeneous models to meet the latency constraints of multiple edge systems simultaneously. We design a dynamic zeroizing-recovering method to adjust each local model architecture for high accuracy under its latency constraint. A proto-corrected federated aggregation scheme is also introduced to aggregate all heterogeneous local models, satisfying the latency constraint of different systems with only one training process and maintaining high accuracy. Extensive experiments indicate that, compared to state-of-the-art methods and under a latency constraint, our extended models can improve the accuracy by 1.96% on average, and our shrunk models can also obtain a 3.09% accuracy improvement on average, with almost no extra training overhead. The related codes and data will be available at this https URL

---


### 49. [FedTR: Federated Learning Framework with Transfer Learning for Industrial Visual Inspection](https://arxiv.org/abs/2607.08014)

**<font color=#1a73e8>作者：</font>** Vikash Sathiamoorthy, Shuo Huai, Hao Kong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a collaborative learning scheme to train deep learning models, where collaborating parties can consolidate their models without sharing local data with other parties, hence preserving data privacy. Nevertheless, when implementing FL in Industrial visual inspection (IVI), the constraints posed by limited data availability and the intricate nature of the inspection tasks significantly impact the performance of the resulting model. This paper introduces FedTR, a novel FL framework incorporating transfer learning designed for Autonomous IVI, focusing on the challenging task of identifying label defects through end-to-end text recognition. Transfer learning is a method that leverages the knowledge of a pre-trained model to adapt to a different dataset. FedTR initially trains the model using a publicly available dataset, after which performs the essential federated learning process with model fine-tuning on the distributed and limited private data. Extensive experiment results demonstrate the effectiveness and feasibility of FedTR on private ink cartridge datasets for label defect identification. FedTR achieves an end-to-end text recognition word-level accuracy of 95.5% and 94.2% on homogeneous and heterogeneous data respectively. Additionally, it attains performance levels that are on par with those achieved through centralized training.

---


### 50. [LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting](https://arxiv.org/abs/2607.08016)

**<font color=#1a73e8>作者：</font>** Zixin Guo, Yehonathan Litman, Yifeng He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video relighting requires balancing long-form temporal consistency with a physically grounded understanding of light transport, which depends on accurate estimation of intrinsic scene properties such as materials, geometry, and illumination. Existing methods follow two paradigms: (1) reconstruct a video's photometric properties via inverse rendering and relight them to a target illumination via forward rendering, using physically-based rendering (PBR) or a neural renderer; these suffer from noisy reconstructions and struggle with hard-to-model effects such as global illumination. (2) Frame the task as generative video-to-video translation conditioned on relighting targets (a target environment map or text); this limits relighting control and temporal stability, since diffusion models struggle to translate long-form videos, and is constrained by the availability of input/relit training pairs. We propose LightCrafter, a hybrid pipeline that reformulates video relighting as video translation of a proxy video: rather than translating the input video directly to the target, we translate a PBR rendering of the input under the target illumination to the final target. This bakes illumination targets into the PBR proxy, removing the need to teach the diffusion model illumination concepts like environment maps, and enables more intricate lighting control while naturally providing long-form temporal consistency. We show PBR renders alone already outperform some prior art but struggle with effects like global illumination; to capture these, we leverage photometric priors in video generation models by post-training CogVideoX on synthetic video pairs and real-world unpaired videos. We outperform prior state-of-the-art on existing real-world relighting benchmarks and contribute a synthetic benchmark for further analysis. We will release our dataset, benchmark, metrics, and code.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-189](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
