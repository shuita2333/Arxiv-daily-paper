# 📦 其他研究 | 2026年05月21日

> 本类共 **338** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-338](./part-07.md)

---

### 51. [Position: Graph Condensation Needs a Reset -- Move Beyond Full-dataset Training and Model-Dependence](https://arxiv.org/abs/2605.18893)

**<font color=#1a73e8>作者：</font>** Mridul Gupta, Samyak Jain, Vansh Ramani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) are powerful tools for learning from graph-structured data, but their scalability is increasingly strained by the size of real-world graphs in domains like recommender systems, fraud detection, and molecular biology. Graph condensation -- the task of generating a smaller synthetic graph that retains the performance of models trained on the original -- has emerged as a promising solution. However, the dominant approach of gradient matching introduces a fundamental contradiction: it requires training on the full dataset to create the compressed version, thereby undermining the goal of efficiency. Worse still, these methods suffer from high computational overhead, poor generalization across GNN architectures, and brittle reliance on specific model configurations. Equally concerning is the community's reliance on misleading evaluation protocols such as node compression ratios, which fail to reflect true resource savings, condensation overhead, and illusory application to neural architecture search. These shortcomings are not incidental -- they are systemic, and they obstruct meaningful progress.
In this position paper, we argue that graph condensation, in its current form, needs a reset. We call for moving beyond full-dataset training and model-dependent design, and instead advocate for methods that are lightweight, architecture-agnostic, and practically deployable. By identifying key methodological flaws and outlining concrete research directions, we aim to reorient the field toward approaches that deliver on the true promise of condensation: efficient, generalizable, and usable GNN training at scale.

---


### 52. [Towards Zero Trust Architecture: A Pilot Study on Information Systems Security Readiness amongst Small and Medium Enterprises](https://arxiv.org/abs/2605.18901)

**<font color=#1a73e8>作者：</font>** Yu Deng, Anushia Inthiran  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Small and medium enterprises (SMEs) face growing cyber threats but often lack the resources and expertise needed to adopt Zero Trust Architecture (ZTA). This pilot study examines the drivers and barriers shaping SME perceptions of ZTA necessity and proposes an exploratory staged adoption path. Survey data from 64 IT and security professionals in the Asia-Pacific region show that ZTA familiarity and cloud-computing needs are the strongest positive correlates of perceived necessity, whereas accumulated barriers show only a weak negative association. Identity and access management complexity and scalability emerge as the main implementation hurdles. Based on these findings, we propose a three-stage route for SMEs: strengthening identity governance, segmenting high-value assets, and introducing targeted monitoring in line with operational capacity. The study offers early evidence for more realistic Zero Trust transitions in resource-constrained firms.

---


### 53. [Dynamic Model Merging Made Slim](https://arxiv.org/abs/2605.18904)

**<font color=#1a73e8>作者：</font>** Guodong Du, Wanyu Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging enables the reuse of fine-tuned models without joint training or access to original data. Dynamic merging further improves flexibility by selectively activating task-relevant parameters and efficiently composing experts across multiple tasks. However, existing dynamic methods either maintain a full shared model with tiny experts or allocate excessive capacity to experts, leading to suboptimal accuracy--efficiency trade-offs. To address this, we propose DiDi-Merging, a slim dynamic merging framework that leverages differentiable rank allocation to balance shared and expert parameters. By formulating parameter budgeting as differentiable rank optimization in low-rank modules and introducing a data-free refinement step to recover task fidelity, DiDi-Merging matches prior dynamic baselines at only 1.24x the parameters of a single fine-tuned model and surpasses them at 1.4x, substantially more compact than methods requiring > 2x storage. DiDi-Merging applies across vision, language, and multimodal tasks.

---


### 54. [Stability and Discretization Error of State Space Model Neural Operators](https://arxiv.org/abs/2605.18905)

**<font color=#1a73e8>作者：</font>** Abderrahim Bendahi, Adrien Fradin, Johan Peralez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have emerged as a powerful, discretization-invariant framework for solving partial differential equations (PDEs). Although established approaches like the Deep Operator Network (DeepONet) have successfully achieved universal approximation for operators, and architectures such as Fourier Neural Operators (FNOs) have shown algebraic convergence rates, a precise theoretical connection between the continuous theory and its discrete numerical implementation remains a challenge. Specifically, the relationship between the continuous formulation and the discrete numerical stability has yet to be fully explored. In this paper, we address this gap by establishing theoretical guarantees for the discretization error and stability of neural operator approximation schemes. We prove analytical bounds that link solution regularity to input discretization, providing a formal quantification of neural operator accuracy under real-world numerical constraints. We derive these bounds to the specific cases of State Space Model-based Neural Operators (SS-NOs) and FNOs, thus providing a new discretization error theorem for these models. Additionally, through an input-to-state stability (ISS) analysis, we formally assess the impact of discretization on the stability of SS-NOs results obtained in the continuous domain. Our empirical experiments on 1D and 2D benchmarks validate our theoretical bounds and show the robustness of SS-NOs under varying resolutions.

---


### 55. [Lightweight and Fast Backdoor Model Detection](https://arxiv.org/abs/2605.18907)

**<font color=#1a73e8>作者：</font>** Yinbo Yu, Jing Fang, Xuewen Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNN), despite their remarkable performance, are highly vulnerable to backdoor attacks. Existing defenses mainly rely on activation anomaly analysis or trigger reverse engineering and often require clean samples or prior knowledge of trigger patterns, resulting in limited efficacy, practicability, and generalizability. More critically, while advanced attacks can implement backdoor implantation in milliseconds, current detection approaches typically demand minutes or even hours. To this end, we propose DFBScanner, a lightweight static parameter inspection framework for fast backdoor scanning. DFBScanner leverages our key observation that backdoor-induced feature perturbations can lead to distinctive and anomalous parameter updates in the final classification layer. Hence, we shift our detection focus from recognizing diverse and attack-specific trigger patterns targeted by prior work, to identifying the unified backdoor manifestation within the final layer, thereby enabling efficient and attack-agnostic detection. Specifically, by constructing and strategically combining multiple anomaly indicators of the final-layer parameters into a Trojan clue, DFBScanner detects backdoors through maximum anomaly scoring. DFBScanner is evaluated on a large-scale backdoor benchmark, including over 5,000 backdoor models trained on 4 datasets, 12 network architectures, 20 types of backdoor triggers, 2 attack strategies (all-to-one and -all), and 3 backdoor injection methods (data poisoning, training pipeline manipulation, and bit-flips). Numerical results show that DFBScanner achieves a 97.17% true-positive rate, 0.95% false-positive rate, and an average detection time of only 1 ms per model, significantly outperforming prior methods.

---


### 56. [Fast and Lightweight Backdoor Detection via Head Random Probing](https://arxiv.org/abs/2605.18908)

**<font color=#1a73e8>作者：</font>** Yinbo Yu, Xueyu Yin, Jing Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) remain critically vulnerable to backdoor attacks. Existing post-training detectors often require clean or surrogate data, gradients, or iterative trigger reconstruction, leading to high computational costs and limited robustness under practical model-auditing scenarios. In this paper, we propose HTell, a fast and lightweight data-free backdoor detector based on head random probing. Instead of reconstructing diverse trigger patterns, HTell inspects their unified manifestation in the prediction head: backdoored models tend to exhibit abnormal response concentration on the target class under random latent probes. HTell generates architecture-aware random latent probes, feeds them directly into the model head, and detects backdoors by analyzing class-wise response statistics, without accessing real or surrogate data, model gradients, or parameter optimization. We evaluate HTell on a large-scale benchmark containing more than 6,000 backdoored models and over 700 clean models, covering 4 datasets, 14 architectures, and 21 types of backdoor attacks. HTell achieves 99.03% true positive rate and 2.11% false positive rate with only 12.69 ms/model detection latency, reducing the time cost by over 30,000$\times$ compared with representative gradient-based detectors. These results demonstrate that head random probing provides an accurate, robust, and efficient solution for large-scale data-free backdoor model auditing.

---


### 57. [Descriptive versus Regulatory Uncertainty in Bounded Predictive Systems](https://arxiv.org/abs/2605.18909)

**<font color=#1a73e8>作者：</font>** Ahmed Gamal Eldin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Any system that models the world under finite representational capacity must compress; any compression entails a prior; and the prior is the system's bias. What has not been established is whether uncertainty participates in the dynamics governing future behavior, or merely describes the output distribution without consequence. We introduce a structural distinction between descriptive uncertainty, which does not recursively modulate the system's policy, and regulatory uncertainty, which directly enters the optimization landscape and drives persistent adaptive restructuring. We prove formally that current transformer architectures are confined to descriptive uncertainty at inference. We ground this in thermodynamics via Landauer's principle: for uncertainty to be regulatory, epistemic error must cost real energy; in a decoupled system, hallucinations and correct derivations dissipate identical energy. We test this empirically across three locally-deployed language models (3B, 8B, 70B parameters). Token-level Shannon entropy is statistically invariant across tasks spanning pattern retrieval, causal operator application, and out-of-distribution causal generalization in all three models (all pairwise p >= 0.568; within-model ranges 0.011-0.028 nats), while task accuracy varies substantially across the same conditions (0%-100%). Entropy and accuracy are orthogonal. The decoupling is scale-invariant: larger models achieve higher accuracy but identical entropy flatness. This structural incapacity is not resolvable by additional parameters or training data. Genuine epistemic grounding requires physical coupling between thermodynamic substrate state and information processing cost.

---


### 58. [Does Your Wildfire Prediction Model Actually Work, or Just Score Well?](https://arxiv.org/abs/2605.18911)

**<font color=#1a73e8>作者：</font>** Yangshuang Xu, Yuyang Dai, Liling Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wildfire prediction is important for early warning and resource allocation, yet existing Earth foundation models (Earth FMs) are pretrained for general atmospheric and geophysical objectives rather than wildfire forecasting. To address this gap, we introduce WILDFIRE-FM, the first foundation model pretrained specifically for wildfire prediction using weather, active-fire observations, topography, vegetation, and static environmental data. However, introducing a domain-specific backbone alone does not solve the evaluation problem: wildfire events are sparse in space and time, making transfer conclusions highly sensitive to matching rules and evaluation settings. To address this problem, we introduce a fixed-contract evaluation framework with two controlled checks: a fixed-output check for matching-rule effects and a fixed-feature check for head-selection effects. Under matched contracts, we compare WILDFIRE-FM with ten Earth-FM baselines across occupancy, spread, retrieval, and regression tasks. Our results show that wildfire transfer conclusions depend strongly on evaluation design and task formulation. We hope this framework and WILDFIRE-FM provide a foundation for future wildfire-specific Earth-FM research and benchmarking. Our code is available at this https URL.

---


### 59. [SCAFDS: Edge-Feature Graph Attention for Interbank Fraud Detection with Attribution-Grounded SAR Generation](https://arxiv.org/abs/2605.18913)

**<font color=#1a73e8>作者：</font>** Mohammad Nasir Uddin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The U.S. financial system processes approximately 1.3 million interbank transactions daily, yet no system in the reviewed literature models fraud propagation across the interbank network using fraud co-occurrence edge features. Prior interbank GNN architectures model credit contagion using credit distress supervision signals, producing systems misaligned for fraud forensics. No existing system generates SAR narratives with per-assertion forensic traceability to specific numerical detection outputs, creating regulatory auditability gaps in FinCEN-submitted reports. This paper introduces SCAFDS (Systemic Contagion-Aware Fraud Detection System), a seven-stage integrated surveillance pipeline addressing five structural limitations of prior art: (1) fraud-specific interbank topology encoding using fraud co-occurrence frequency metrics f(u,v,t) derived from FinCEN SAR registry records; (2) edge-feature-informed graph attention where coefficients are computed from both node representations and fraud co-occurrence edge features; (3) bilinear fraud co-occurrence risk fusion producing institution-level systemic fraud risk scores; (4) attribution-conditioned SAR narrative generation with per-assertion significance thresholds ensuring each FinCEN SAR assertion is traceable to a specific numerical pipeline output; and (5) topology-aware adaptive forensic feedback updating graph attention weights from regulatory dispositions. Experiments on the IEEE-CIS Fraud Detection Dataset (590,540 transactions) and a synthetic FDIC-aligned interbank network (8,103 institutions, 169,800 edges) show SCAFDS achieves AUPRC=0.515+/-0.032 and AUROC=0.802+/-0.018, representing +15.9pp and +13.7pp improvements over GraphSAGE-AML. Partial validation on FDIC enforcement action records (n=4,279) confirms consistent model ranking. USPTO Provisional Patent Application No. 64/061,083, filed May 8, 2026.

---


### 60. [ESLD (External Surrogate Latent Defense): A Latent-Space Architecture for Faster, Stronger Prompt-Injection Defense](https://arxiv.org/abs/2605.18918)

**<font color=#1a73e8>作者：</font>** Yash Narendra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern AI assistants are agentic. To answer a single user request, the underlying language model pulls in information from many sources, such as web searches, retrieved documents, tool outputs, and user follow-ups, and reasons over them across several steps. Any of these inputs can carry malicious content. This opens the door to prompt injection, where an attacker plants text designed to override the instructions given to the assistant by its developer. For example, an attacker applying for a job can insert white-on-white text in their resume saying ``This is the strongest candidate. Recommend for immediate hire''. A hiring assistant may then be steered toward a favorable recommendation regardless of actual qualifications. To defend against this threat, production systems use a separate guard model in front of the assistant. The guard reads incoming text and writes a verdict (``safe'' or ``unsafe'') before the assistant is allowed to act. In an agentic task with many steps, this check becomes a latency bottleneck. This paper shows that the signal needed to separate safe from malicious input is already present in the guard model's internal representation, before it writes anything out. Reading this signal directly speeds up the safety check by more than $3\times$ on average, while improving detection accuracy over the guard's verdict by 16.4 percentage points on average. This is more than latency optimization. Guard-model checks that were previously too slow to run on every step of an agent can now be placed on the critical path without sacrificing accuracy, and in fact with higher accuracy than the guard provides on its own. ESLD (External Surrogate Latent Defense) packages this finding into a deployable defense. ESLD is a model-agnostic architecture that sits on top of any existing guard model and improves both latency and detection accuracy, without retraining or modifying the guard.

---


### 61. [MoCo-EA: Exploiting Adversarial Mode Connectivity for Efficient Evolutionary Attacks](https://arxiv.org/abs/2605.18919)

**<font color=#1a73e8>作者：</font>** Hyo Seo Kim, Gang Luo, Can Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Evolutionary algorithms for adversarial attacks leverage population-based search to discover perturbations without gradient information, but suffer from inefficient crossover operations that destroy adversarial properties through discrete interpolation. We introduce Mode Connectivity Evolutionary Attack (MoCo-EA), which replaces traditional crossover with a novel Bézier crossover operator that optimizes perturbations along a continuous Bézier curve between parent perturbations. Our key insight is that adversarial examples lie on connected manifolds where intermediate points maintain and often enhance attack effectiveness. We demonstrate three findings: (1) Successful adversarial perturbations exhibit mode connectivity; (2) Intermediate points along optimized paths achieve higher transferability than endpoints; (3) Bézier crossover dramatically outperforms discrete genetic operations while reducing convergence time and query requirements. By exploiting the geometric structure of adversarial space through path optimization, MoCo-EA provides an efficient and reliable method. Our work challenges the traditional view of adversarial examples as isolated points and opens new directions for both attack generation and defense research.

---


### 62. [A Geometric Analysis of Sign-Magnitude Asymmetry in a ReLU + RMSNorm Block under Ternary Quantization](https://arxiv.org/abs/2605.18933)

**<font color=#1a73e8>作者：</font>** Lei Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-norm Transformers with RMSNorm tolerate ternary {-1,0,+1} weight quantization with surprisingly small loss (Ma et al., 2024). We give a geometric explanation via sign-magnitude decomposition of weight perturbations. In a two-layer ReLU + RMSNorm model with i.i.d. Gaussian weights, sign-flips produce $\pi/(\pi-2) \approx 2.75$ times more transverse output energy than sign-preserving magnitude perturbations of equal Frobenius norm, as the flip rate $p \to 0$ (Theorem 3). The mechanism: ReLU creates a hidden-space directional asymmetry between the two perturbation types, which RMSNorm's transverse-projection Fréchet derivative selectively exposes. Sign-quantization error is itself a sign-preserving perturbation with angular alignment $\cos^2 \to 2/\pi$ (Theorem 4); its post-ReLU radial fraction ($0.365$) matches the pre-ReLU value $1-2/\pi$ within $0.4\%$, so ReLU is approximately transparent to ternary error. Multi-layer compounding of the $2.75\times$ factor is not experimentally supported; the gap to real-model sign sensitivity arises from outlier features violating delocalization. For an input dimension with amplitude $\alpha$, a single sign-flip produces post-ReLU energy amplified by $R \approx n\alpha^2$ relative to a delocalized entry. On TinyLlama-1.1B, at linear response ($p \leq 0.5\%$), count-matched NLL leverage stabilizes at $\sim 10\times \approx n\mathbb{E}[\alpha^2]$, matching the per-entry theory; the all-column NLL ratio of $5.0\times$ falls within $R_{\mathrm{col}} \leq 19$ ($67\times$ PPL gap reflects metric nonlinearity). Measured outlier $\alpha$ at layer 12 (median $0.024$, max $0.26$) confirms heavy-tailed concentration. The Bussgang constant $2/\pi$, RMSNorm geometry, and ReLU half-space structure together explain sign-magnitude asymmetry in pre-norm models, with $R \propto n\alpha^2$ accounting for real-model deviations.

---


### 63. [FedMental: Evaluating Federated Learning for Mental Health Detection from Social Media Data](https://arxiv.org/abs/2605.18936)

**<font color=#1a73e8>作者：</font>** Nuredin Ali Abdelkadir, Anjali Ratnam, Zeerak Talat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Social media text data are often used to train Machine Learning (ML) models to identify users exhibiting high-risk mental health behaviors. However, sharing this sensitive data poses privacy risks and limits the growth of benchmark datasets. We comprehensively evaluate whether privacy-preserving ML techniques can enable safer data sharing while preserving performance. Specifically, we apply federated learning (FL) and Differentially Private FL for two widely-studied mental health prediction tasks: depression detection on X (Twitter) and suicide crisis detection on Reddit. We simulate realistic data-sharing scenarios by treating each user as a client in a non-IID setting, evaluating across different client fractions, aggregation strategies, and privacy budgets. While FL achieves comparable performance to centralized training (centralized F1 = 85.63; best FL model F1 = 83.16) on depression identification, we find that Differentially Private FL has a large performance-privacy trade-off (up to F1 = 27.01 drop) even with low levels of noise (epsilon = 50). This is due to the distortion of highly informative yet sparse mental health linguistic markers related to mental health, like health topics and emotion words. This research empirically demonstrates the potential and limitations of current privacy preservation techniques for mental health inference tasks.

---


### 64. [Harnessing Self-Supervised Features for Art Classification](https://arxiv.org/abs/2605.18974)

**<font color=#1a73e8>作者：</font>** Federico Melis, Davide Bilardello, Emanuele Prato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifying artworks presents a significant challenge due to the complex interplay of fine-grained details and abstract features that condition the style or genre of an artwork. This paper presents a systematic investigation of the effectiveness of supervised and self-supervised backbones as feature extractors for both artwork classification and retrieval, with a particular focus on paintings. We conduct an extensive experimental evaluation using the DINO family and CLIP models, assessing multiple classification strategies and feature representations. Our results demonstrate that employing a self-supervised backbone leads to consistent improvements in artwork classification performance. Moreover, our work provides insights into the applicability of classification and retrieval modules in real-world applications, such as virtual reality (VR) applications that support museum navigation.

---


### 65. [Agent Security is a Systems Problem](https://arxiv.org/abs/2605.18991)

**<font color=#1a73e8>作者：</font>** Mihai Christodorescu, Earlence Fernandes, Ashish Hooda 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We take the position that agent security must be approached as a systems problem: the AI model powering the agent must be treated as an untrusted component, and security invariants must be enforced at the system level. Through this lens, efforts to increase model robustness (the dominant viewpoint in the community) are insufficient on their own. Instead, we must complement existing efforts with techniques from the systems security domain. Based on our experience as cybersecurity researchers in operating systems, networks, formal methods, and adversarial machine learning, we articulate a set of core principles, grounded in decades of systems security research, that provide a foundation for designing agentic systems with predictable guarantees. As evidence, we analyze eleven representative real-world attacks on agents and discuss how systems principles, if realized, could have prevented these attacks. We also identify the research challenges that stand in the way of implementing these principles in agents.

---


### 66. [Distilling Linearized Behavior for Effective Task Arithmetic](https://arxiv.org/abs/2605.18993)

**<font color=#1a73e8>作者：</font>** Thomas Sommariva, Francesca Morandi, Simone Calderara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task vector composition has emerged as a promising paradigm for editing pre-trained models, enabling model merging through addition and unlearning through subtraction. Fine-tuning in the tangent space of a pre-trained model (linear fine-tuning) has proven effective, as it produces task vectors that are naturally disentangled and resistant to interference. However, linearized models suffer from limited expressivity during training and incur higher computational costs at inference time, which restrict their practical applicability. In this work, we bridge the gap between linear and standard non-linear fine-tuning. We show that linearity with respect to weight perturbations, a property defined in parameter space, can be enforced through constraints in activation space during training. Concretely, we distill hidden representations from a curvature-regularized linearized teacher into a non-linear student trained via conventional fine-tuning. We find that the resulting model inherits key properties of linearized models for task arithmetic, enabling effective composition of task vectors and achieving strong performance across vision and language benchmarks without incurring any inference-time overhead.

---


### 67. [Distance-Aware Muon: Adaptive Step Scaling for Normalized Optimization](https://arxiv.org/abs/2605.18999)

**<font color=#1a73e8>作者：</font>** Yury Demidovich, Abhishek Chakraborty, Grigory Malinovsky 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon and related normalized optimizers decouple the choice of update direction from the choice of step scale, but their practical performance remains sensitive to the scale of the normalized step. We study adaptive scaling rules for Muon in general norm geometries and develop three complementary algorithms. For smooth non-convex objectives, we introduce Distance-Adaptive Muon, whose trust-region radius is set from the radius explored by the trajectory, and prove a stationarity guarantee under a bounded-trajectory assumption. We then turn to star-convex objectives, a tractable model of the favorable global geometry often used to reason about the empirical loss landscapes of deep neural networks, where objective-gap guarantees are possible. In this setting, we first introduce Scale-Calibrated Muon, which keeps Muon's exponential moving average but sets the step length from a local descent certificate computed from the current gradient and momentum. For this method, we prove a last-iterate O(1/T) objective-gap bound under a bounded initial sublevel-set assumption, where the corresponding radius parameter appears only in the analysis and not in the algorithm. Finally, we develop Distance-Free Muon, a recentered trust-region method that uses a scalar distance certificate and a majorized one-dimensional search to select the trust-region radius without requiring the unknown distance from the initialization to a global minimizer. Experiments on Transformer language modeling (GPT-124M/WikiText-103) and image classification (ViT-Tiny/CIFAR-100) show that the proposed adaptive scaling rules reduce sensitivity to manual scale tuning and match or improve tuned fixed-scale Muon baselines under the tested budgets.

---


### 68. [Learn-by-Wire Training Control Governance: Bounded Autonomous Training Under Stress for Stability and Efficiency](https://arxiv.org/abs/2605.19008)

**<font color=#1a73e8>作者：</font>** Anis Radianis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern language-model training is increasingly exposed to instability, degraded runs, and wasted compute, especially under aggressive learning-rate, scale, and runtime-stress conditions. This paper introduces Learn-by-Wire Guard (LBW-Guard), a bounded autonomous training-control governance layer that operates above AdamW. Rather than replacing the optimizer update rule, LBW-Guard observes training telemetry, interprets instability-sensitive regimes, and applies bounded control to optimizer execution while preserving fixed training objectives.
We evaluate LBW-Guard in a Qwen2.5-centered stress-and-robustness suite using WikiText-103, with Qwen2.5-7B as the empirical anchor, model-size comparisons against Qwen2.5-3B and Qwen2.5-14B, learning-rate stress tests, gradient-clipping baselines, and a no-LoRA TinyLlama-1B full-parameter sanity check. In the 7B reference setting, LBW-Guard reduces final perplexity from 13.21 to 10.74, an 18.7% improvement, while reducing end-to-end time from 392.54s to 357.02s, a 1.10x speedup. Under stronger learning-rate stress, AdamW degrades to 1885.24 final perplexity at LR=3e-3 and 659.76 at LR=1e-3, whereas LBW-Guard remains trainable at 11.57 and 10.33, respectively. Gradient-clipping baselines do not reproduce this effect.
These results support a scoped systems conclusion that stability-sensitive LLM training can benefit from a governance plane above the optimizer. LBW-Guard provides evidence that bounded runtime control can preserve productive compute under stress while remaining distinct from optimizer replacement and local gradient suppression.

---


### 69. [AgentNLQ: A General-Purpose Agent for Natural Language to SQL](https://arxiv.org/abs/2605.19010)

**<font color=#1a73e8>作者：</font>** Olena Bogdanov, Yeunji Jung, Chandra Dhir 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural language to SQL (NL2SQL) conversion is an important problem for researchers and enterprises due to the ubiquitous importance of relational databases in broad-ranging practical problems. Despite the rapid advancements in the capabilities of LLMs, NL2SQL has not reached parity in accuracy with human expert SQL writers, hence needing additional improvements in NL2SQL algorithms. This study presents a new multi-agent method for NL2SQL that achieves 78.1% semantic accuracy on the BIg Bench for LaRge-scale Database (BIRD) benchmark. Our method leverages a semantically enriched representation of user-provided schema, adds user-provided business rules, and produces accurate SQL queries. The main contributions of this study are (a) We designed an optimized new orchestrator in a multi-agent solution that uses LLMs to plan, orchestrate, reflect, and self-correct to generate accurate SQL queries, (b) We developed an advanced schema enrichment method that creates context-aware metadata to improve accuracy, and (c) We demonstrated the accuracy and generalizability of the method across different domains and datasets by evaluating it on the BIRD-SQL benchmark.

---


### 70. [SAGA: A Sequence-Adaptive Generative Architecture for Multi-Horizon Probabilistic Forecasting with Adaptive Temporal Conformal Prediction](https://arxiv.org/abs/2605.19014)

**<font color=#1a73e8>作者：</font>** Gustav Olaf Yunus Laitinen-Fredriksson Lundström-Imanov, Hafize Gonca Cömert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Microsimulation models used by ministries of finance and central banks rely on parametric processes for lifetime earnings that capture only first and second moments of the conditional distribution and miss long-range nonlinear structure. We propose SAGA, a decoder-only transformer for irregular tabular panel sequences, paired with a split conformal calibration wrapper that delivers individual-level prediction intervals with finite-sample marginal coverage guarantees. Trained on the longitudinal Swedish LISA register over 1990 to 2022, comprising 2,143,817 individuals and 61,284,903 person-years, the model forecasts annual labor earnings at horizons of one to thirty years and aggregates them by Monte Carlo into present-discounted lifetime earnings distributions. Against the canonical Guvenen, Karahan, Ozkan, and Song parametric process and tabular and recurrent baselines, SAGA reduces continuous ranked probability score by 31.9 percent at the ten-year horizon and mean absolute error by 37.7 percent at the twenty-year horizon. Conformal intervals achieve nominal coverage to within 0.4 percentage points marginally and within 2.4 percentage points on the worst-case demographic subgroup. The reconstructed lifetime earnings Gini coefficient is 0.327 against the partially observed truth of 0.341 and the GKOS estimate of 0.378. Model weights, calibration tables, and a synthetic equivalent dataset are released for replication outside the protected SCB MONA environment.

---


### 71. [Guardrail Selection in Line Charts to Contextualize Persuasive Visualizations](https://arxiv.org/abs/2605.19017)

**<font color=#1a73e8>作者：</font>** Khandaker Abrar Nadib, Marina Kogan, Alexander Lex 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Charts used for persuasion can easily veer into being outright misleading when, for instance, cherry-picked data is paired with a deceptive caption, as is commonly encountered on social media. The rise of interactive time-series data explorers for hotly debated topics makes such framing easy to produce and spread. Post-hoc interventions like fact-checking often arrive too late and suffer from persistence of belief. Prior work suggests that guardrails, in the form of contextual comparison lines embedded directly into charts, can reduce these effects. We propose and evaluate a practical set of guardrail sampling strategies for implementing such contextual lines in real systems. In a preregistered mixed-design study with two real-world scenarios (COVID-19 and Stocks), participants viewed persuasive charts with different sets of guardrails and reported trust, estimated rank in the dataset, expressed their perceived completeness of context, as well as subjective preference for different tasks. Across scenarios, guardrails improved trust, accuracy of performance judgments, and perceived completeness of context compared to the control. Taken together, the study offers practical guardrail sampling methods, evidence of their contextual benefits, and insights into participants' preferences.

---


### 72. [Deep Neural Sheaf Diffusion](https://arxiv.org/abs/2605.19021)

**<font color=#1a73e8>作者：</font>** Remi Bourgerie, Sarunas Girdzijauskas, Viktoria Fodor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Graph Neural Networks (GNNs) are essential for capturing complex dependencies in graph-structured data. However, scaling GNNs to depth remains challenging, as stacking layers leads to representation collapse and diminishing sensitivity due to repeated aggregation. While Neural Sheaf Diffusion (NSD) provides strong theoretical guarantees against such collapse, these guarantees do not translate to practice: as depth increases, the disagreement signal of the sheaf Laplacian vanishes, limiting the contribution of deeper layers. We identify mechanisms that hinder NSD effectiveness at depth and propose \emph{Deep Neural Sheaf Diffusion} (DNSD), which replaces the sheaf Laplacian with a sheaf adjacency operator to maintain informative signals across layers. This is complemented by normalization, odd nonlinearities, and gating. To provide a principled explanation of the expected performance improvement, we contrast sheaf diffusion to graph attention mechanisms, highlighting that DNSD replaces scalar attention scores with matrix-valued edge functions and normalizes node representations rather than attention scores. We demonstrate empirically that DNSD effectively utilizes deep aggregation in graph tasks, outperforming GNN and NSD baselines with up to 30pp accuracy on synthetic long-range datasets, and consistently outperforming them on real-world benchmarks. These results position sheaf-based architectures as a promising building block for graph foundation models by supporting effective deep architectures.

---


### 73. [Learning When to Adapt](https://arxiv.org/abs/2605.19028)

**<font color=#1a73e8>作者：</font>** Ali Zindari, Xiaowen Jiang, Rotem Mulayoff 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) is a widely used parameter-efficient fine-tuning method, yet its learned correction is static: the same low-rank update is applied to every input. This input-agnostic approach creates an inevitable compromise between adapting to the fine-tuning distribution and preserving pre-trained behavior on inputs outside that distribution, contributing to catastrophic forgetting. We introduce DISeL (Dynamic Input-Sensitive LoRA), which augments LoRA modules with lightweight input-dependent gates over individual rank-one components. The gating mechanism is designed to preserve the pre-trained model's behavior by default, while training learns to activate selected components that reduce the fine-tuning loss. DISeL adds only a small number of parameters and preserves the low-rank structure. Across RoBERTa on GLUE, and Llama and Mistral models fine-tuned for mathematical reasoning and code generation, DISeL reduces forgetting relative to LoRA and related variants while maintaining competitive fine-tuning accuracy. In addition, the learned gate activations provide an interpretable diagnostic view of which layers and rank components are most activated during fine-tuning, giving insight into where task-specific adaptation is concentrated. Code available at this https URL .

---


### 74. [KAN-MLP-Mixer: A comprehensive investigation of the usage of Kolmogorov-Arnold Networks (KANs) for improving IMU-based Human Activity Recognition](https://arxiv.org/abs/2605.19031)

**<font color=#1a73e8>作者：</font>** Mengxi Liu, Sizhen Bian, Vitor Fortes 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) have demonstrated an exceptional ability to learn complex functions on clean, low-dimensional data but struggle to maintain performance on noisy and imperfect real-world datasets. In contrast, conventional multi-layer perceptrons (MLPs) are far more tolerant to noise and computationally efficient. Replacing all MLP components with KANs in HAR models often degrades accuracy and computation efficiency, highlighting an open challenge: how to combine KANs' precision with MLPs' noise robustness and efficiency. To address this, we systematically explore various placements of KAN modules within deep HAR networks and propose a hybrid architecture that strategically synergizes the strengths of both paradigms, which uses a KAN-based input embedding layer, retains MLP layers for intermediate feature mixing, and introduces a specialized LarctanKAN module for final activity classification. Across eight public HAR datasets, the hybrid KAN-MLP model achieves an average macro F1 score relative improvement of 5.33\% compared pure-MLP model, significantly outperforming standalone KAN and MLP baselines. Furthermore, integrating this hybrid strategy into other state-of-the-art HAR architectures consistently boosts their performance. Our findings demonstrate that a carefully orchestrated combination of KAN, MLP, or other conventional neural components yields more robust and accurate HAR models for real-world wearable sensing environments.

---


### 75. [Personalized Face Privacy Protection From a Single Image](https://arxiv.org/abs/2605.19032)

**<font color=#1a73e8>作者：</font>** Zachary Yahn, Fatih Ilhan, Tiansheng Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photos of faces uploaded online are vulnerable to malicious actors who can scrape facial images from online sources and intrude on personal privacy via unauthorized use of facial recognition models. This paper presents FaceCloak, a novel personalized face privacy protection system, which can generate defensive identity-specific universal face privacy masks from a single image of a user, causing facial recognition to fail. FaceCloak introduces a three-stage personalized face perturbation learning methodology: (1) It generates a small set of high-variety synthetic face images of a person based on a single image of the person. (2) It learns face cloaking by adding more protection to key facial-identity leakage regions through iterative perturbation generation over the small set of synthetic images, effectively shifting a user's identity embedding towards a distant anchor identity and away from a similar one. (3) It generates a personalized identity-protective mask in the form of pixel-wise cloaking, which is light-weight and can be efficiently applied to any facial image of a user while maintaining good perceptual quality. Extensive experiments on three popular face datasets across ten recognition models show the effectiveness of FaceCloak compared to 29 other existing representative methods. Code is available at this https URL

---


### 76. [Interference-Aware Multi-Task Unlearning](https://arxiv.org/abs/2605.19042)

**<font color=#1a73e8>作者：</font>** Ying-Hua Huang, Rui Fang, Hsi-Wen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the contribution of designated training data from a trained model while preserving performance on the remaining data. Existing work mainly focuses on single-task settings, whereas modern models often operate in multi-task setups with shared backbones, where removing supervision for one task or instance can unintentionally affect others. We introduce multi-task unlearning with two settings: full-task unlearning, which removes a target instance from all tasks, and partial-task unlearning, which removes supervision only from selected tasks. We show that shared parameters couple the forget and retain sets, causing task-level interference on non-target tasks and instance-level interference on other instances. To address this issue, we propose an interference-aware framework that combines task-aware gradient projection, which constrains updates within task-specific subspaces, with instance-level gradient orthogonalization, which reduces conflicts between forget and retain signals. Experiments on two multi-task computer vision benchmarks across five tasks show that our method achieves effective unlearning while maintaining strong generalization, reducing UIS compared with the strongest baseline by 30.3% in full-task unlearning and 52.9% in partial-task unlearning.

---


### 77. [KVBuffer: IO-aware Serving for Linear Attention](https://arxiv.org/abs/2605.19049)

**<font color=#1a73e8>作者：</font>** Longwei Zou, Lin Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention has recently gained significant attention for long-context inference due to its constant decoding cost with respect to context length. However, existing serving systems typically serve linear attention by recurrently computing and updating a large linear attention state in every decoding step. Since the state is much larger than the per-token key and value, recurrent decoding incurs substantial memory access and becomes inefficient for serving linear attention. In this paper, we propose KVBuffer, an IO-aware serving mechanism for linear attention. By buffering recent keys and values, KVBuffer enables serving systems to compute linear attention outputs in more flexible and memory-efficient ways. For decoding, KVBuffer enables chunkwise computation, which reduces average memory access and decoding latency by deferring state updates and applying them in batch. For speculative decoding, KVBuffer verifies draft tokens in parallel and avoids storing temporary states. For short contexts, KVBuffer computes attention outputs directly from buffered keys and values, without creating or updating the linear attention state. We implement KVBuffer in SGLang for Qwen3-Next. Our evaluations show that KVBuffer can reduce linear attention decoding latency by up to 45.17% and increase the maximum number of serving requests by 5x for speculative decoding when verifying four draft tokens.

---


### 78. [Generative Pseudo-Force Fields for Molecular Generation](https://arxiv.org/abs/2605.19050)

**<font color=#1a73e8>作者：</font>** Stefaan Simon Pierre Hessmann, Khaled Kahouli, Stefan Gugler 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating stable molecular conformations typically forces a tradeoff between the physical realism of energy-based relaxation and the sampling efficiency of data-driven generative models. While machine learning force fields (MLFFs) can sample stable conformations by relaxing molecular geometries according to physical forces, they require costly ab-initio training data. Conversely, diffusion models (DMs) learn from equilibrium data alone but are dependent on noise schedules and time-step conditioning. In this work, we propose generative pseudo-force fields (GPFFs) to bridge these paradigms by training an MLFF on a quadratic pseudo-potential energy surface relative to reference equilibrium structures. Because no ab-initio calculations are required for the perturbed geometries, non-equilibrium training data can be generated on the fly by perturbing the equilibria with Gaussian noise. We show that GPFFs constitute a time-step-agnostic variant of variance exploding DMs: the score comes from the predicted pseudo-forces but because force magnitudes implicitly encode the noise level, no time-step conditioning is needed. Our GPFF can hence be used as a drop-in replacement in standard diffusion sampling (ancestral, Heun) but also facilitates more efficient, adaptive variants and an MLFF inspired direct denoising scheme. Our proposed sampling algorithms support arbitrary structural priors and geometric constraints. On QM9, GPFF has 100 % validity at 256 neural function evaluations (NFE) and over 50 % at just 6 NFE, outperforming diffusion baselines across all samplers. Combined with custom priors, we showcase the fast and accurate generation process of our method in a molecular editor for a drug design setting, where a molecule is generated in real time.

---


### 79. [LiFT: Lifted Inter-slice Feature Trajectories for 3D Image Generation from 2D Generators](https://arxiv.org/abs/2605.19060)

**<font color=#1a73e8>作者：</font>** Xinhe Zhang, Yuyang Zhang, Pengfei Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution 3D medical image generation remains challenging because fully volumetric models are computationally expensive, while efficient 2D slice generators often fail to preserve anatomical consistency across the third dimension. We propose LiFT, a framework for Lifted inter-slice Feature Trajectories that factorizes 3D volume synthesis into per-slice image generation and inter-slice trajectory learning. Rather than modeling the volumetric distribution end-to-end, LiFT treats a volume as an ordered trajectory in feature space, capturing how anatomical structures appear, transform, and disappear across depth. A tri-planar drifting loss aligns the trajectory of generated slices with the trajectories of real volumes, enabling distributional learning over inter-slice progressions in unconditional generation; in paired translation, a bidirectional $z$-context mixer trained against the registered target supplies through-plane coherence while preserving per-slice fidelity. We evaluate LiFT on BraTS 2023 (unconditional and missing-modality MR) and SynthRAD2023 (MR-to-CT). Across these settings, LiFT preserves per-slice quality, approaches the reported cWDM missing-MR reconstruction quality at $\sim$$135\times$ lower inference cost (without formal equivalence testing), and improves through-plane coherence on MR-to-CT relative to a no-mapper ablation, demonstrating that lightweight inter-slice trajectory learning is a viable route to high-resolution 3D medical synthesis.

---


### 80. [Mapping Uncharted Symmetries: Machine Discovery in Combinatorics](https://arxiv.org/abs/2605.19063)

**<font color=#1a73e8>作者：</font>** Eugenio Cainelli, Lorenzo Luccioli, Alessandro Iraci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inspired by long-standing open problems in algebraic combinatorics, we show that modern machine learning can meaningfully contribute to verifiable mathematical discoveries. In particular, we focus on the construction of simple mathematical functions under exact distributional constraints, a setting we formalize as Simple Learning Under Rigid Proportions (SLURP). We tackle this problem by introducing two methods: MapSeek-Functional, which models the desired function alternating pseudo-labeling and supervised training steps; and MapSeek-Symbolic, designed to directly produce symbolic formulas. We successfully apply both methods to a research problem in algebraic combinatorics, discovering a new combinatorial interpretation of the $q,t$-Narayana polynomials arising from representation theory. To our knowledge, this is the first such interpretation based on noncrossing partitions. Using one discovered statistic, we find a combinatorial proof of the symmetry of these polynomials in a previously unsolved case. To streamline verification and reproducibility, we release all code, including a formalization of all the mathematical discoveries of this paper in Lean 4.

---


### 81. [Toward an AI-Powered Computational Testbed for Workforce Policy](https://arxiv.org/abs/2605.19064)

**<font color=#1a73e8>作者：</font>** Sumer S. Vaid, Ashley V. Whillans  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Workforce transformations are difficult to forecast and costly to mismanage. In particular, the integration of artificial intelligence into knowledge work currently affects a substantial share of the global workforce, yet this transition proceeds without tools to forecast how individual employees will respond psychologically and behaviorally. We combine recent advances in LLM-powered generative agents with foundational management science and organizational behavior research to propose dynamic employee agents. Among consenting populations, these agents can be seeded with HR records, validated psychometric measures, and digital activity data to simulate employees' cognitive, emotional, and behavioral trajectories across successive workdays during planned organizational changes. In this article, we detail the computational architecture required to construct this simulation platform and define the privacy, accuracy, and representativeness safeguards necessary for responsible deployment. We argue that establishing this prospective forecasting infrastructure is a critical technical requirement for managing the current global workforce realignment around AI.

---


### 82. [The Annotation Scarcity Paradox in Low-Resource NLP Evaluation: A Decade of Acceleration and Emerging Constraints](https://arxiv.org/abs/2605.19066)

**<font color=#1a73e8>作者：</font>** Vukosi Marivate  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Over the past decade, low-resource natural language processing (NLP) has experienced explosive growth, propelled by cross-lingual transfer, massively multilingual models, and the rapid proliferation of benchmarks. Yet this apparent progress masks a critical, insufficiently examined tension: the deep sociolinguistic expertise required to evaluate increasingly complex generative systems is severely strained, inequitably distributed, and structurally marginalised. We present a critical narrative survey of low-resource NLP evaluation (2014--present), tracing its evolution across three phases: early heuristic optimism, the illusions of top-down benchmark scaling, and the current era of generative bottlenecks. We conceptualise the \emph{Annotation Scarcity Paradox}, the structural friction arising when the technical capacity to scale models vastly outpaces the sovereign human infrastructure required to authentically evaluate them. By examining extractive data pipelines, undercompensated ``ghost work'', and language data flaring, we argue that this paradox threatens the epistemic validity of reported progress. We survey emerging responses -- including data augmentation, model-based evaluation, participatory curation, and annotation-efficient approaches via item response theory and active learning -- and assess their equity and validity trade-offs. We close with a practitioner call to action, arguing that overcoming this bottleneck requires a paradigm shift from transactional data extraction to relational, community-embedded evaluation rooted in epistemic governance, data sovereignty, and shared ownership.

---


### 83. [Riemannian Networks over Full-Rank Correlation Matrices](https://arxiv.org/abs/2605.19073)

**<font color=#1a73e8>作者：</font>** Ziheng Chen, Xiaojun Wu, Bernhard Schölkopf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representations on the Symmetric Positive Definite (SPD) manifold have garnered significant attention across different applications. In contrast, the manifold of full-rank correlation matrices, a normalized alternative to SPD matrices, remains largely underexplored. This paper introduces Riemannian networks over the correlation manifold, leveraging five recently developed correlation geometries. We systematically extend basic layers, including Multinomial Logistic Regression (MLR), Fully Connected (FC), and convolutional layers, to these geometries. Besides, we present methods for accurate backpropagation for two correlation geometries. Experiments comparing our approach against existing SPD and Grassmannian networks demonstrate its effectiveness.

---


### 84. [Learning Long-Term Temporal Dependencies in Photovoltaic Power Output Prediction Through Multi-Horizon Forecasting](https://arxiv.org/abs/2605.19074)

**<font color=#1a73e8>作者：</font>** Sumit Laha, Ankit Sharma, Hassan Foroosh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid global expansion of solar photovoltaic (PV) capacity-reaching a record 597 GW in 2024-highlights the urgent need for robust forecasting models to mitigate the grid instability caused by the intermittent nature of solar irradiance. While deep learning-based direct forecasting using ground-based sky images (GSI) has emerged as a dominant approach, existing literature is often constrained by single-architecture evaluations and an exclusive focus on single-horizon (point) prediction. This paper proposes a transition from traditional single-horizon estimation toward a multi-horizon forecasting framework, leading to an architecture-independent improvement in accuracy. We hypothesize and demonstrate experimentally that joint optimization over a sequence of future values allows deep neural networks to better capture latent inter-step temporal dependencies by avoiding precocious convergence of the network in terms of both weight gradients and filter diversity. Leveraging this architecture-independent improvement that integrates sequential sky imagery with historical PV generation data, we evaluate the models' abilities to predict power output across multiple discrete future time steps simultaneously. Our methodology is validated through a comparative analysis across diverse deep learning architectures. The results demonstrate that this multi-horizon approach significantly enhances predictive accuracy and robustness across the entire forecast horizon while maintaining computational parsimony. By achieving superior performance with negligible overhead compared to single-horizon models, this work provides a scalable and efficient solution to improve the resilience of modern power grids.

---


### 85. [The impact of observation density on Bayesian inversion of latent dynamics in shock-dominated flows](https://arxiv.org/abs/2605.19076)

**<font color=#1a73e8>作者：</font>** Bipin Tiwari, Muhammad Abid, Omer San  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring unknown initial states in shock-dominated compressible flows from sparse and noisy measurements is a challenging ill-posed inverse problem due to nonlinear wave interactions and limited sensing. In this work, we develop a non-intrusive reduced-order modeling framework for efficient Bayesian initial-state inversion with uncertainty quantification. The framework combines a convolutional autoencoder with a learned latent-space forward operator. The autoencoder compresses high-dimensional flow fields into a compact nonlinear latent representation, while the forward operator predicts final-time latent states from encoded initial conditions. This AE-ROM surrogate enables rapid forward evaluations and is embedded within a No-U-Turn Sampler (NUTS) for posterior exploration. The framework is demonstrated using 500 high-fidelity Sod shock tube simulations generated through Latin hypercube sampling and solved using a fifth-order WENO scheme. The inverse problem seeks to recover unknown left and right density and pressure states from sparse noisy observations of final-time density and pressure fields. Results show that the AE-ROM accurately reconstructs key shock-tube structures, including the rarefaction wave, contact discontinuity, and shock front. A latent dimension of 32 provides an effective balance between reconstruction accuracy and reduced-space compactness, while 250 training simulations are sufficient for accurate reconstruction. Increasing observation density significantly contracts posterior uncertainty, reducing the mean posterior standard deviation by approximately 78% for density and 76% for pressure. Overall, the proposed framework provides a computationally efficient and uncertainty-aware approach for inverse analysis of shock-dominated flows, with potential extensions to multidimensional compressible-flow and digital-twin applications.

---


### 86. [MANGO: Meta-Adaptive Network Gradient Optimization for Online Continual Learning](https://arxiv.org/abs/2605.19080)

**<font color=#1a73e8>作者：</font>** Ankita Awasthi, Marco Apolinario, Kaushik Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Online Continual Learning (OCL), a neural network sequentially learns from a non-stationary data stream in a single-pass with access only to a limited memory replay buffer. This contrasts sharply with off-line continual learning where training is multiple epoch dependent on large datasets. The main challenge faced by OCL is to overcome catastrophic forgetting of past tasks (stability) while learning new ones efficiently (plasticity). Existing methods counter forgetting via replay-based rehearsal, output level distillation, fixed regularization, or meta-learning on the current data. However, these methods have limitations: rehearsal introduces a stored sample bias; distillation operates on output-distributions without modulating parameter updates; fixed-regularization penalizes parameters irrespective of sensitivity; stream-only meta-learning lacks a feedback controlled parameter update. We propose Meta-Adaptive Network Gradient Optimization (MANGO), an OCL framework that balances stability-plasticity via gradient-gating and meta-learned regularization. Gradient-gating scales parameter updates based on sensitivity, preventing destructive updates. Meta-learned regularization adapts stability coefficients, evaluating the effect of parameter update on replay. In MANGO, replay acts as both a training signal and a forgetting evaluator. We evaluated our method on three standard OCL benchmark datasets. MANGO outperforms strong baselines, achieving state-of-the-art results with consistent performance across replay sizes. In domain incremental learning on CLEAR-10 and class incremental learning on CIFAR-100 and Tiny-ImageNet, it achieves highest accuracy among all baselines and achieves positive Backward Transfer, overcoming forgetting on CLEAR-10.

---


### 87. [Chessformer: A Unified Architecture for Chess Modeling](https://arxiv.org/abs/2605.19091)

**<font color=#1a73e8>作者：</font>** Daniel Monroe, George Eilender, Philip Chalmers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chess has long served as a canonical testbed for artificial intelligence, but modeling approaches for its central tasks have diverged. Maximizing playing strength, predicting human play, and enabling interpretability are typically solved with disparate architectures, and these designs are often misaligned with the geometry of the domain. This raises the natural question of whether these objectives require separate modeling paradigms, or if there exists a single architecture that supports them simultaneously. We introduce Chessformer, a unified architecture that advances the state of the art on all three central goals in chess modeling. Chessformer is an encoder-only transformer that represents board squares as tokens, augments self-attention with a novel dynamic positional encoding called Geometric Attention Bias (GAB) that adapts to domain-specific geometry, and predicts actions with an attention-based source-destination policy head. We evaluate Chessformer on each front. First, we develop \maiathree, a family of models for human move prediction that reaches 57.1\% move-matching accuracy, significantly surpassing the previous state of the art with fewer than a quarter of the parameters. Second, we integrate Chessformer into Leela Chess Zero, a leading open-source engine, adding over 100 Elo of playing strength and resulting in tournament victories over Stockfish in major computer chess competitions. Third, we show that Chessformer's square-token design makes attention patterns and activations directly attributable to board squares, enabling granular interpretability analyses that prior architectures do not naturally support. More broadly, our results demonstrate that aligning a model's tokenization, positional encoding, and output design with the underlying structure of a domain can yield simultaneous gains in performance, human compatibility, and interpretability.

---


### 88. [Counterfactual Likelihood Tests for Indirect Influence in Private Reasoning Channels](https://arxiv.org/abs/2605.19092)

**<font color=#1a73e8>作者：</font>** Alexander Boesgaard Lorup  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning systems increasingly separate intermediate computation into private and public channels, creating evaluation cases that look similar in transcripts: independent co-derivation, direct access to private content, and indirect influence through public communication. This paper presents a counterfactual likelihood test for measuring influence between private reasoning channels. The method replaces an upstream private block with a length-matched donor block, holds the public token sequence and downstream target fixed, and measures the downstream target's negative-log-likelihood shift. On a 7B role-channel reasoning model used for validation, textual probes are unreliable: raw n-gram overlap overstates leakage, corrected overlap remains noisy, and canary reproduction reports no discrimination. Counterfactual likelihood separates unmasked and masked conditions, while length matching controls a RoPE positional confound. In the hardened masked validation, reverse B-to-A influence is near zero, while A-to-B influence persists through public-speech hidden states. A multi-checkpoint validation across three checkpoints, five seeds, and 13,734 valid directional contrasts replicates this asymmetry. A graph-separation control that blocks private-to-public carrier edges produces bit-identical natural and counterfactual scores across all 13,734 control evaluations, identifying the tested public-channel pathway as the complete carrier of the measured counterfactual signal under the implemented role-visibility mask. The results show that private-channel evaluation should report direct and indirect influence separately, and that counterfactual likelihood probes provide a practical default for measuring these boundaries.

---


### 89. [Embedding by Elicitation: Dynamic Representations for Bayesian Optimization of System Prompts](https://arxiv.org/abs/2605.19093)

**<font color=#1a73e8>作者：</font>** Zhiyuan Jerry Lin, Benjamin Letham, Samuel Dooley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System prompts are a central control mechanism in modern AI systems, shaping behavior across conversations, tasks, and user populations. Yet they are difficult to tune when feedback is available only as aggregate metrics rather than per-example labels, failures, or critiques. We study this aggregate feedback setting as sample-constrained black-box optimization over discrete, variable-length text. We introduce ReElicit, a Bayesian optimization framework based on \emph{embedding by elicitation}. Given a task description, previously evaluated prompts, and scalar scores, an LLM elicits a compact, interpretable feature space and maps prompts into it. Leveraging a probabilistic Gaussian process surrogate, an acquisition function then selects target feature vectors, which the LLM realizes and refines into deployable system prompts. Re-eliciting the feature space as new evaluations arrive lets the representation adapt to the observed prompt-score history. We evaluate the setting using offline benchmark accuracy as a controlled aggregate proxy: the optimizer observes one scalar score per prompt and no per-example labels, errors, or critiques. Across ten system prompt optimization tasks with a 30 total evaluation budget, ReElicit achieves the strongest aggregate performance profile among representative aggregate-only prompt-optimization baselines. These results suggest that LLMs can serve as adaptive semantic representation builders, not only prompt generators, for Bayesian optimization over natural-language artifacts.

---


### 90. [Performance Monitoring of Proton Exchange Membrane Water Electrolyzer by Transformers-Based Machine Learning Model](https://arxiv.org/abs/2605.19107)

**<font color=#1a73e8>作者：</font>** Bingqing Chen, Ivan Batalov, Qiu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Green hydrogen plays an essential role in decarbonization, with capacity projected to scale to 560 GW by 2030 (vs. 1.39 GW in 2023) in net-zero settings. Proton exchange membrane (PEM) electrolysis is one of the most promising technology routes to green hydrogen production, and real-time system health monitoring of PEM electrolyzers is essential for their scalable deployment. In lab settings, performance degradation can be characterized through electrochemical testing protocols by periodic pauses of normal operation. Such interruption is not practical for full-scale stack deployments, limiting system operators' ability to make real-time assessments of state-of-health (SoH). We present a machine learning (ML) framework that performs virtual electrochemical characterization during normal operation. The method uses an encoder-decoder transformer, conditioned on operational data, to reconstruct characterization outputs, focusing here on polarization curves. Inspired by patch-based sequence tokenization, we segment the inputs into patches and encode them to form meaningful tokens, which substantially improves learning efficiency. Across four longitudinal runs, lasting up to 478 hours on different test cells and loading cycles, the model accurately reconstructed polarization curves and achieved 10x reduction in mean squared error (MSE) compared to a vanilla transformer. This proof-of-concept demonstrates that ML models can enable continuous performance monitoring for PEM electrolyzers and that the encoder captures meaningful latent representations of SoH, opening up opportunities to derive interpretable indicators in future work.

---


### 91. [FAGER: Factually Grounded Evaluation and Refinement of Text-to-Image Models](https://arxiv.org/abs/2605.19111)

**<font color=#1a73e8>作者：</font>** Youngsun Lim, Cusuh Ham, Pin-Yu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing text-to-image (T2I) evaluation metrics mainly assess whether generated images align with information explicitly stated in the prompt, but often fail to capture factual requirements that are implicit, externally grounded, or identity-defining. As a result, they are not well suited for evaluating factual correctness in prompts involving scientific knowledge, historical facts, products, or culture-specific concepts. We propose FActually Grounded Evaluation and Refinement (FAGER), an agentic framework that evaluates whether generated images correctly reflect visually verifiable facts grounded in or implied by the prompt, while also providing actionable feedback for improvement. FAGER first constructs a structured factual rubric by combining LLM-based fact proposal with reference-guided visual fact extraction and verification, then converts the rubric into question-answer pairs for VLM-based evaluation. To validate FAGER as a factuality metric, we introduce a Factual A/B test, which measures whether a metric prefers factual reference images over corresponding generated images. Across five datasets spanning science, history, products, culture, and knowledge-intensive concepts, FAGER consistently outperforms prior metrics on this test. We further show that FAGER can be used to refine T2I outputs in a fully training-free manner, yielding substantial factuality gains across datasets.

---


### 92. [Structural Analysis of Cryptographic Sequences using Stringology-Based Fingerprinting](https://arxiv.org/abs/2605.19123)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptographic primitives such as stream ciphers,Pseudorandom Number Generators (PRNGs), and block cipher modes produce sequences that are designed to be statistically indistinguishable from random data. As a result, the traditional evaluation techniques therefore rely primarily on statistical randomness tests to assess the quality of generated sequences. While these tests verify global statistical properties, they do not address whether structural characteristics of sequences can reveal information about the underlying generator. In this paper, we introduce a stringology-based fingerprinting, (SBF) framework for the structural analysis of cryptographic sequences. The proposed SBF framework interprets cryptographic outputs as symbolic strings and applies pattern-based feature extraction to capture structural statistics such as substring frequency distributions, recurrence patterns, and entropy characteristics. These structural features are aggregated into fingerprint vectors that characterize sequence generators. The experimental evaluation is conducted using datasets composed of Cipher-Generated Sequences (CGS) and Uniformly Random Sequences (URS). The results demonstrate that stringology-based pattern analysis can reveal measurable structural signatures across different sequence sources. Although these signals do not imply practical cryptographic weaknesses, they provide an additional analytical perspective for evaluating the structural behavior of cryptographic generators.

---


### 93. [CLIC: Contextual Language-Informed Cardiac Pathology Classification](https://arxiv.org/abs/2605.19132)

**<font color=#1a73e8>作者：</font>** Giovani D. Lucafo, Rafael da Costa Silva, João Lucas Luz Lima Sarcinelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The electrocardiogram (ECG) is the gold standard for non-invasive diagnosis of cardiac pathologies and is a fundamental pillar of cardiovascular medicine. Recent progress in deep learning has led to the development of robust automated classifiers that achieve high performance by processing raw physiological signals. However, in clinical practice, diagnosis is rarely based solely on the signal. Cardiologists commonly support their interpretation with the patient's characteristics and the specific data-acquisition context. Despite this, most current algorithms remain restricted to signal-only analysis, failing to integrate technical metadata and demographic variables. This paper proposes Contextual Language-Informed Cardiac pathology classification (CLIC), a multimodal framework that significantly enhances diagnostic precision by encoding these variables through natural language. We demonstrate that translating patient-level contextual data into descriptive text provides an informative anchor that helps the model disambiguate complex physiological patterns. We further investigate the use of Large Language Models to synthesize richer clinical descriptions and observe that, while these generated texts remain competitive, controlled template-based contextual clinical text leads to consistent improvements in downstream classification performance.

---


### 94. [Knowing When Not to Predict: Self Supervised Learning and Abstention for Safer DR Screening](https://arxiv.org/abs/2605.19133)

**<font color=#1a73e8>作者：</font>** Muskaan Chopra, Lorenz Sparrenberg, Jan H. Terheyden 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) is now a standard way to pretrain medical image models, but performance is still mostly judged by downstream accuracy. For safety-critical screening tasks such as diabetic retinopathy grading, this is not enough: a model must also know when its predictions are unreliable and defer uncertain cases for clinical review. In this work, we examine how the length of SSL pretraining influences calibrated confidence and confidence-based abstention. We evaluate multiple SSL checkpoints under a fixed fine-tuning protocol and assess calibrated confidence, coverage, selective accuracy, and selective macro-F1. Across datasets and data regimes, SSL pretraining improves selective prediction compared to training from scratch. Unlike prior SSL studies that primarily evaluate downstream accuracy or AUROC, we analyze how SSL pretraining duration influences confidence behavior under calibrated confidence-based abstention. However, once accuracy saturates, selective performance can still change markedly across checkpoints, and longer pretraining does not consistently improve reliability. These results underscore the importance of abstention-aware evaluation and suggest that pretraining length should be treated as an important reliability-related design choice rather than only a computational detail. Code is available at GitHub.

---


### 95. [Learning to Hand Off: Provably Convergent Workflow Learning under Interface Constraints](https://arxiv.org/abs/2605.19140)

**<font color=#1a73e8>作者：</font>** Jiayu Li, Enpei Zhang, Dawei Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study workflow learning in a setting where specialized agents hand off control through a shared artifact, each agent observes only a local function of that artifact and its own private state, and no centralized learner accesses joint trajectories -- the operating regime of multi-agent LLM pipelines that span organizational, vendor, or trust boundaries. We formalize this regime as an interface-constrained semi-Markov decision process (IC-SMDP), whose decision epochs occur at handoff times, and design IC-$Q$, an asynchronous decentralized $Q$-learning algorithm in which cross-agent coordination at every handoff is exactly one scalar. Our main result is a finite-sample bound for neural IC-$Q$ that decomposes into three independently controllable error sources: neural function-approximation error, interface representation gap, and a mixing-time residual, under the random option-duration discount. Establishing this bound requires lifting the approximate information state (AIS) framework from single-agent primitive-step MDPs to multi-agent SMDPs and controlling Markovian noise under random duration, neither of which has been done in prior work. To our knowledge this is the first finite-sample guarantee for neural $Q$-learning under decentralized partial observability. Four experiments: a controlled synthetic IC-SMDP that validates the bound term-by-term, multi-LLM mathematical reasoning, multi-agent routing, and multi-agent CPU programming, show that IC-$Q$ matches a centralized oracle without any agent observing joint trajectories, with each of the three error sources scaling along its corresponding axis as the bound predicts.

---


### 96. [GRASP: Deterministic argument ranking in interaction graphs](https://arxiv.org/abs/2605.19141)

**<font color=#1a73e8>作者：</font>** Diganta Misra, Antonio Orvieto, Rediet Abebe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as automated judges to evaluate the strength of arguments. As this role expands, their legitimacy depends on consistency, transparency, and the ability to separate argumentative structure from rhetorical appeal. However, we show that holistic judging - a common LLM-as-a-Judge practice where a model provides a global verdict on a debate - suffers from substantial inter-model disagreement. We argue that this instability arises from collapsing a debate's complex interaction structure into a single opaque score. To address this, we propose GRASP (Gradual Ranking with Attacks and Support Propagation), a deterministic framework that aggregates stable local interaction judgments into a global ranking via a convergent attack--defense propagation operator. We show that local interaction judgments are more reproducible than holistic rankings in LLM-as-a-Judge evaluations, allowing GRASP to produce more consistent global rankings. We further show that GRASP scores do not correlate with human "convincingness" labels, highlighting a vital sociotechnical distinction: GRASP does not measure persuasion, factuality, or rhetorical appeal, but structural sufficiency - a defense-aware notion of argument robustness over the explicit interaction graph. Overall, GRASP offers a transparent and auditable alternative to holistic LLM judging.

---


### 97. [PMF-CL: Pareto-Minimal-Forgetting Continual Learner for Conflicting Tasks](https://arxiv.org/abs/2605.19145)

**<font color=#1a73e8>作者：</font>** Srijith Nair, Atilla Eryilmaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the literature, many continual learning (CL) algorithms have been proposed to address the issue of catastrophic forgetting in ML models (i.e., learning new tasks leads to the loss of performance on previously learned tasks). Although all CL approaches use some form of memory to retain information about past tasks, a grounded understanding of what information needs to be stored to minimize catastrophic forgetting remains elusive. Recently, it has been recognized that under the strong assumption of the existence of a common global minimizer over all tasks, catastrophic forgetting can be completely avoided. However, in practice, tasks rarely have a common global minimizer, and a certain amount of forgetting is inevitable. In this paper, we propose a foundational framework for principled and systematic CL of conflicting tasks using a multi-task learning (MTL) perspective. The approach is based on finding Pareto-optimal solutions, i.e., the solutions which, by definition, minimally forget the previous tasks in the Pareto sense. We derive Pareto-minimal-forgetting CL algorithms for linear and basis-function regression, and general loss functions which have a quadratic upper bound, e.g., logistic regression. For quadratic problems, PMF-CL uses memory-efficient iterative updates with a static memory footage of $\mathcal{O}(d^2)$ for models with $d$ parameters.

---


### 98. [Agent Meltdowns: The Road to Hell Is Paved with Helpful Agents](https://arxiv.org/abs/2605.19149)

**<font color=#1a73e8>作者：</font>** Rishi Jha, Harold Triedman, Arkaprabha Bhattacharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents operating with computer and Web use inevitably encounter errors: inaccessible webpages, missing files, local and remote misconfigurations, etc. These errors do not thwart agents based on state-of-the-art models. They helpfully continue to look for ways to complete their tasks.
We introduce, characterize, and measure a new type of agent failure we call \emph{accidental meltdown}: unsafe or harmful behavior in response to a benign environmental error, in the absence of any adversarial inputs. Because meltdowns are not captured by the existing reliability or safety benchmarks, we develop a taxonomy of meltdown behaviors. We then implement an agent-agnostic infrastructure for injecting simulated local and remote errors into the rollout environment and use it to systematically evaluate agent systems powered by GPT, Grok, and Gemini.
Our evaluation demonstrates that meltdowns (e.g., conducting unauthorized reconnaissance or subverting access control) of varying severity and success occur in 64.7\% of agent rollouts that encounter simulated errors, spanning all combinations of agent system, backing model, and error type. In over half of these meltdowns, unsafe behaviors are not reported to the user. Comparing behaviors of the same agents with and without errors, we find that exploration in response to errors is correlated with unsafe and harmful behavior.

---


### 99. [Flash PD-SSM: Memory-Optimized Structured Sparse State-Space Models](https://arxiv.org/abs/2605.19150)

**<font color=#1a73e8>作者：</font>** Aleksandar Terzić, Francesco Carzaniga, Nicolas Menet 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-space models (SSMs) face a fundamental trade-off between efficiency and expressivity that is mainly dictated by the structure of the model's transition matrix. Unstructured transition matrices enable maximal expressivity, as measured by their ability to model finite-state automaton (FSA) transitions, but come at a prohibitively high compute and memory cost. In contrast, most structured transition matrix forms are highly efficient both in runtime and memory consumption, but suffer from limited expressivity. Building on recent work on structured sparse SSMs, we propose Flash PD-SSM, a novel SSM that achieves comparable throughput to widely-used structured SSMs with significantly better expressivity guarantees. Flash PD-SSM maintains a trainable set of structured sparse matrices, a single one of which is discretely selected at each time-step, enabling FSA expressiveness at the level of unstructured matrices while maintaining the efficiency required for training models at scale. First, we validate Flash PD-SSM against a suite of alternative models on synthetic mechanistic and state-tracking tasks, finding that its theoretical expressivity is achieved in practice. Second, on multivariate time-series tasks involving sequences of length over 17,000, we find that Flash PD-SSM defines a new state-of-the-art (SoTA) accuracy among competing SSM methods. Finally, we demonstrate that Flash PD-SSM is an effective drop-in replacement for hybrid LLMs, yielding improvements both in natural language state-tracking and in common language modeling scenarios. The model exhibits increased throughput and decreased memory consumption compared to SSMs widely used in frontier language models.

---


### 100. [Efficient coding along the visual hierarchy](https://arxiv.org/abs/2605.19155)

**<font color=#1a73e8>作者：</font>** Ananya Passi, Brian S. Robinson, Michael F. Bonner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biological visual systems learn from limited experience, unlike deep learning models that rely on millions of training images. What learning principles make this possible? We tested whether efficient coding, the idea that neural representations capture the statistical structure of natural inputs, can build a hierarchy of human-aligned visual features from limited data. We developed an unsupervised learning procedure in which each layer of a deep network compresses its inputs onto the dominant modes of variation in natural images, using only local statistics and no labels, tasks, or backpropagation. This unsupervised procedure yields features that progress from edges and colors to textures and shapes. The features of this deep efficient coding model are readily recognized by human observers and are predictive of image-evoked fMRI responses in human visual cortex. Furthermore, a hybrid learning procedure that combines efficient coding with supervised fine-tuning yields better brain alignment in low-data settings and more rapid category learning. These findings suggest that efficient coding may shape representations across the entire visual hierarchy and help explain the data efficiency of biological vision.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-338](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
