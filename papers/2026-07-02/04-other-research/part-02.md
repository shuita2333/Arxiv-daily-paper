# 📦 其他研究 | 2026年07月02日

> 本类共 **274** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-274](./part-06.md)

---

### 51. [When Regulation Has Memory: Hysteresis and Control Burden in Artificial Agency](https://arxiv.org/abs/2606.30975)

**<font color=#1a73e8>作者：</font>** Veronique Ziegler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive agents are usually judged by what they do, but an agent can appear stable while the internal effort required to keep it stable is increasing. This hidden regulatory burden matters for artificial agents operating under noise, delay, or changing demands: two systems may reach similar internal states while one requires much more corrective control to get there.
Here, we study whether that burden depends on history. Using a computational model of adaptive uncertainty regulation, we drive an artificial agent through a continuous change in its uncertainty target and then reverse the change without resetting the agent. This creates a simple test for carryover: does the controller respond only to the current target, or does the path by which the agent reached that target still matter?
The simulations show a clear history-dependent effect. The adaptive gain required to regulate the agent forms a reproducible hysteresis loop, meaning that the same target can require different levels of control depending on whether the agent is moving toward or returning from a more demanding regime. The timing of regulation also matters. When stabilization is available before disturbance exposure, the agent generally requires less adaptive gain than when it can only recover after disturbance has already acted.
The state-level coherence measure also shows path dependence, but the timing effect is much clearer in regulatory gain. The main difference is therefore not that anticipatory regulation produces a completely different state. Rather, it reaches comparable regulated behavior with lower modeled control demand. These results suggest that adaptive agents should be evaluated not only by whether they remain organized, but by how much regulation they must recruit to do so.

---


### 52. [Measuring Judgment Quality in Natural-Language Explanations: Evidence from Forecasting Tournaments](https://arxiv.org/abs/2606.30987)

**<font color=#1a73e8>作者：</font>** Christopher W. Karvetski, Sheldon S. Huang, Simas Kučinskas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision-makers routinely rely on expert judgments accompanied by written explanations, yet explanation quality is difficult to measure at scale. Forecasting tournaments offer a natural testing ground: probabilistic judgments are paired with natural-language rationales and scored against realized outcomes. We introduce Explanation Quality Markers (EQMs), a set of sixty theory-guided reasoning patterns scored by large language models (LLMs). In a pre-registered analysis of over 55,000 forecast-rationale pairs from a multiyear forecasting tournament, EQMs predict accuracy at both the forecast and forecaster levels, consistently outperforming pre-LLM text-analysis methods. More than 90% of statistically significant pattern-level EQM-accuracy correlations match our directional hypotheses. The signal is asymmetric: EQMs identify likely underperformers more reliably than they distinguish the very best forecasters. Benchmarked against traditional indicators of forecasting skill, EQMs are the strongest predictor at the forecast level and competitive at the forecaster level, though weaker than prior accuracy. Human ratings of rationale quality are less consistently correlated with accuracy and place disproportionate weight on rationale length. Results transfer to an independent forecasting study. EQMs provide a scalable, interpretable method for extracting judgment-relevant information from written explanations.

---


### 53. [Wait, am I Being Fair? Characterizing Deductive Stereotyping and Mitigating It with Fair-GCG](https://arxiv.org/abs/2606.30989)

**<font color=#1a73e8>作者：</font>** Naihao Deng, Yilun Zhu, Joan Nwatu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Warning: This paper contains several toxic and offensive statements. While reasoning generally improves fairness in recent large language models (LLMs), failures persist. In this work, we identify a failure mode, deductive stereotyping, in which models apply population-level statistical regularities to individual cases, producing logically coherent yet socially biased inferences. We provide a statistical interpretation of this phenomenon. To steer models toward fairness-aware reasoning, we propose a reasoning-time injection framework. We further introduce Fair-GCG to systematically discover effective injection phrases. Injection phrases discovered by Fair-GCG improve performance across multiple fairness benchmarks, generalize from smaller to larger LLMs, improves reasoning-level fairness, reduces bias in open-ended generation, and transfer to real-world fairness-sensitive tasks.

---


### 54. [Multistage Defer Trees for Hybrid Interpretability: If at First You Can't Succeed, Tree Again](https://arxiv.org/abs/2606.30995)

**<font color=#1a73e8>作者：</font>** Zakk Heile, Hayden McTavish, Margo Seltzer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that well-optimized individual decision trees can match complex black box models in some settings, primarily in noisy domains. For the remaining settings, however, complex ensembled compositions of trees often achieve higher accuracy at the cost of interpretability, leaving practitioners with difficult modeling decisions along an accuracy-interpretability tradeoff. Ideally, we would like to classify as much of the data as possible with one or a small number of trees, achieving interpretability for most samples while maintaining state-of-the-art accuracy. We introduce Multistage Defer Trees: a sequence of sparse decision trees that each make predictions for most samples, while deferring a small proportion to the next tree in the sequence or, ultimately, to a black box. We demonstrate that we can train this model class to match the performance of complex tree-based ensembles while routing most samples through only one or a small number of sparse decision trees. We discuss a range of techniques for training these models while maintaining simplicity. Our method expands the accuracy--interpretability frontier in settings where single-tree methods remain insufficient, demonstrating that even when complex models are necessary, they need not be fully opaque.

---


### 55. [Estimating Supply Incrementality in Two-sided Marketplaces: A Causal Machine Learning Approach](https://arxiv.org/abs/2606.30999)

**<font color=#1a73e8>作者：</font>** Yufei Wu, Daniel Schmierer, Dan Zylberglejd  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In two-sided marketplaces with heterogeneous products, it is important to understand the causal relationship between additional supply and marketplace outcomes, such as the total quantity transacted or transaction value in the marketplace. This paper studies a causal machine learning approach to estimating this relationship across product segments. We use the Airbnb marketplace as an example, focusing on the impact of additional listing supply on total bookings, but the methodology applies to other two-sided marketplaces. Our approach combines double/debiased machine learning with a hierarchical Bayesian framework that leverages pre-existing knowledge as priors. We construct tractable and informative features for the model by leveraging measures of product segment similarity from the geospatial literature. We find that such a model provides plausible estimates of the marketplace returns to additional supply and strong out of sample performance.

---


### 56. [Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization](https://arxiv.org/abs/2606.31002)

**<font color=#1a73e8>作者：</font>** Ke Zhang, Patricio Gallardo Candela, Sudhir Murthy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theorem-proving benchmarks evaluate proof search against fixed formal statements, but natural-language-to-Lean formalization must generate the formal statement itself. In this setting, compilation is only a validity check: a Lean declaration may type-check while omitting hypotheses, changing domains, or expressing a vacuous claim. We study faithful statement formalization as both an evaluation problem and a bottleneck-attribution problem. On a 400-entry graduate-level benchmark spanning real analysis, complex analysis, topology, and algebra, our protocol combines Lean compilation, cross-model semantic judging, and human expert calibration. The resulting picture is different from compile-rate evaluation: a full tool-augmented agent reaches 89.5% compilation but only 60.5% consensus faithfulness, exposing a 29.0-point compile-pass but consensus-unfaithful gap. Targeted human audits support the metric as a conservative decision boundary: across available case-level audits, 96.0% of consensus-positive outputs are human-confirmed faithful, while 82.4% of compile-pass consensus-negative outputs are human-confirmed semantic failures. Under this metric, existing one-shot formalizer models and prover-oriented Lean models remain low, suggesting that formal validity, proof-oriented Lean competence, and faithful statement generation should be reported separately. We then use a full $2^3$ factorial design to decompose three recurring interventions in formalization pipelines: parametric expert drafting, Mathlib/context search, and Lean elaboration feedback. Elaboration feedback is the largest validity intervention, but it also exposes a larger compile-pass semantic-failure bucket; search mainly improves grounding and selectivity; and fine-tuned drafting is largely substitutable in this tool stack once feedback and grounding are available.

---


### 57. [Auditing Generalization in AI-Generated Video Detection: A Six-Control Protocol and the VidAudit Toolkit](https://arxiv.org/abs/2606.31004)

**<font color=#1a73e8>作者：</font>** Mert Onur Cakiroglu, Zhihe Lu, Mehmet Dalkilic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated video detection benchmarks such as GenVidBench and AIGVDBench are the de facto leaderboards, yet most evaluation protocols leave uncontrolled confounds that can inflate reported generalization. As an existence proof, a three-feature clip-length classifier reaches a leave-one-generator-out (LOGO) AUC of 0.998 on GenVidBench under unaudited evaluation, while measuring nothing about motion. A 20-paper survey finds none applying all six standard controls that would catch this, so we combine them into an audited protocol and apply it to six representative feature sources (three published detectors and three repurposed signal sources), re-running it cross-dataset on AIGVDBench. The audit both debunks and certifies: the trivial classifier collapses to near chance (0.529), a CLIP baseline is caught carrying dataset identity, and the 2025 forensic detector WaveRep clears the floor at out-of-distribution LOGO AUC 0.996 with chance-level real-vs-real coherence. At a deployable FPR of 0.1%, multiple high-AUC methods fall to single-digit recall and the leaderboard order changes, so we recommend an audited tuple (AUC, above-floor margin, operating-point recall, and calibration) over a single number. As a white-box positive control, we add TemporalSpec (codec motion vectors); via cross-substrate feature fusion (XSFF), a second substrate adds genuine complementarity that survives the audit. We release VidAudit, to our knowledge the largest unified and audited detector collection for this task, providing 14 detectors behind one plugin API, a leaderboard, and Croissant metadata, available at this https URL. Together, the protocol and toolkit move evaluation from leaderboard rank toward whether a result measures what it claims.

---


### 58. [Dense Structural Priors for Sparse Functional Landmark Localization in Surgical Videos](https://arxiv.org/abs/2606.31007)

**<font color=#1a73e8>作者：</font>** Chenyan Jing, Hao Ding, Lalithkumar Seenivasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models such as SAM 3 can provide transferable object-level structure across diverse surgical video conditions, but segmentation outputs do not explicitly encode the action-conditioned semantics that define functional surgical landmarks. Estimating instrument extent and geometry differs from localizing the tip or anchor relevant to clipping, grasping, or dissecting. We investigate vision foundation model-enabled sparse action-aware landmark localization, using zero-shot, point-prompted structural masks to provide dense instrument-level context without manual pixel-level mask annotations. We propose a lightweight refinement framework that uses SAM 3 as a structural prior. A coarse multi-frame network predicts tip and anchor prompts, generating non-oracle masks that are fused with visual and heatmap features to refine functional landmark predictions. We compare direct mask-augmented supervision, prediction-derived mask-prior refinement, and auxiliary mask supervision to examine how vision foundation model-derived structure should enter a precision-oriented localization system. Experiments on 7,867 clips from 60 surgical videos spanning YouTube, Cholec80, HeiChole, SurgVU, and CRCD evaluate the approach under heterogeneous conditions. Without manual pixel-level mask annotations for training, the proposed model achieves overall F1 scores of 72.4% for tip and 58.0% for anchor localization. Directly imposing masks on heatmap targets biases learning toward broad tool regions, whereas prediction-derived priors and auxiliary supervision provide effective intermediate structural guidance for action-dependent landmark prediction.

---


### 59. [Dual Sparse Aggregation Transformer for Multispectral Object Detection](https://arxiv.org/abs/2606.31015)

**<font color=#1a73e8>作者：</font>** Wencong Wu, Xiuwei Zhang, Hanlin Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based approaches have obtained excellent performance in multispectral object detection tasks due to their ability to model long-range dependencies and capture complementary information. However, previous transformer-based multispectral detection methods tend to use all available tokens for similarity calculation, which results in redundant information interaction from irrelevant areas, leading to degraded detection performance. To overcome this challenge, we propose a novel Dual Sparse Aggregation Transformer (DSAFormer) for multispectral object detection, which consists of a Dual Sparse Transformer (DSFormer) and a Learnable Addition Fusion Block (LAFB). Specifically, the DSFormer is designed to exploit and boost cross-modal complementary information, thereby improving detection performance. It incorporates three key components: A Spatial Sparse Multi-Head Cross-Attention (SSMHCA) mechanism selectively captures cross-modal relationships at the spatial level by reserving only the high query-key similarity scores, eliminating irrelevant interactions. A Channel Sparse Multi-Head Cross-Attention (CSMHCA) mechanism performs similar sparse calculations at the channel level to enhance feature representation and filter out low matching query-key. A Multi-Scale Feature Refinement Layer (MSFRL) is developed to aggregate hierarchical features and suppress redundant information. To effectively fuse multimodal features, the LAFB is introduced to aggregate intramodal and intermodal feature information by feature reweighting. Extensive experimental results have demonstrated that our proposed DSAFormer achieves better detection performance against state-of-the-art methods on four public datasets, including the MFAD, FLIR, M$^3$FD, and LLVIP. The source code of our DSAFormer will be released at this https URL.

---


### 60. [WarpI2I: Image Warping for Image-to-Image Translation](https://arxiv.org/abs/2606.31018)

**<font color=#1a73e8>作者：</font>** Shen Zheng, Anurag Ghosh, Gaurav Parmar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-image (I2I) translation has achieved strong results in tasks like human relighting and driving scene translation using latent diffusion models (LDMs). However, compact LDMs often struggle to preserve fine-grained structures because the encoder compresses high-resolution inputs into a spatially downsampled latent space. To address this issue, we propose a simple saliency-guided warp-unwarp framework that reallocates spatial representation toward salient regions before encoding, enabling better preservation of structural details without increasing latent resolution. The warped image is processed by the original diffusion model and then mapped back via an inverse warp. In addition, we propose a simple and efficient outpainting-based synthetic data generation pipeline to produce high-quality paired data for image relighting. Our method is model-agnostic, requires no architectural modification, and introduces negligible computational overhead. Experiments on human relighting, driving scene relighting, and translation demonstrate improved structural preservation, lighting faithfulness, and image quality, with our framework extending naturally to video via frame-by-frame application with good temporal stability. Project Webpage: this https URL

---


### 61. [Certified Speculative Execution for Untrusted AI Agents](https://arxiv.org/abs/2606.31023)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Qiliang Jiang, Shuning Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hard-constrained sequential decision systems have no certified way to spend the test-time compute of modern AI: executing the multi-step drafts of a learned policy or a frozen LLM forfeits the feasibility guarantee a trusted solver provides, while invoking the solver at every step forfeits the speed the AI offers. Certificate-Gated Prefix Acceptance (CGPA) closes this gap with a certified speculative-execution contract for untrusted AI agents: a trusted verifier rejects constraint-violating transitions exactly, a conformally calibrated value boundary gates the longest low-cost prefix within a per-segment regret budget, and the rest defers to the solver, so safety, regret, and speed decouple by construction. The contract drives every untrusted proposal source - adversarial drafters and six heterogeneous frozen LLMs (including a 12B model that violates constraints in 98% of direct rollouts) - to zero applied violations; a certificate-aware learned boundary, conformally calibrated, drives mean regret three orders of magnitude below unguarded acceptance, to within sampling noise of the stepwise oracle (95% CI spanning zero), and under calendar shift a learned proposal source overtakes it on 15 of 18 held-out days. On a deployment-scale unit-commitment instance it turns a frozen 8B LLM into a 2.96x per-episode wall-clock speedup at 2.1% regret, outpacing the domain heuristic (1.79x) and a safe receding-horizon baseline (1.07x): the more capable the untrusted source, the faster the certified system, at guarantees that never change.

---


### 62. [Offline Reinforcement Learning for Fluid Controls: Data-based Multi-observational Policy Extraction](https://arxiv.org/abs/2606.31025)

**<font color=#1a73e8>作者：</font>** Deepak Akhare, Luning Sun, Xin-Yang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active flow control is a fundamental application in engineering. Recent advances in deep reinforcement learning have made progress in this field. However, the classical online RL approaches require extensive real-time interactions with the high fidelity environment, while each sensor configuration change necessitates whole policy retraining. All these factors result in prohibitive computational costs for real-world applications. In this work, we propose a novel offline RL framework that addresses both challenges through data-driven policy extraction. We develop a sensor position-conditioned architecture that enables a single policy network to adapt seamlessly to multiple sensor arrangements. The position-conditioned approach incorporated spatial relationship modeling through Point Attention layers to ensure the generalizability to varying sensor placements. We demonstrate the framework on two representative problems, mitigating chaoticity in the Kuramoto-Sivashinsky equation and flow control over airfoils governed by the Navier-Stokes equation. The result demonstrates that the policy extraction from the dataset provides unprecedented flexibility for sensor placement optimization. This approach represents a significant step towards adaptive, intelligent flow control systems.

---


### 63. [OTCache: Optimal Transport for Geometry-Aware Caching in Diffusion Models](https://arxiv.org/abs/2606.31026)

**<font color=#1a73e8>作者：</font>** Huanlin Gao, Fang Zhao, Qiang Hui 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose OTCache, a training-free framework for accelerating diffusion sampling via caching schedule prediction. Existing graph-based caching methods reduce redundant computation by optimizing shortest-path objectives, but rely on an additive independence assumption, which often breaks down in the low NFE regime. To address this issue, OTCache models caching schedules across inference budgets as a smooth evolution in policy space, inspired by Optimal Transport (OT). The framework consists of three stages: (1) obtaining a high-fidelity \textbf{reference schedule} using a graph-based caching method under a conservative budget; (2) performing a lightweight anchor search under an extreme low-budget setting via Optuna optimization with an end-to-end perceptual objective; and (3) predicting schedules for target budgets via quantile interpolation between the reference and anchor policies using continuous warping representations. Experiments on FLUX.1 [dev], Qwen-Image, and HunyuanVideo show that OTCache achieves 4.5x, 4.7x, and 3.66x acceleration, respectively, while consistently improving generation fidelity over state-of-the-art caching baselines. This work provides a new perspective on accelerating diffusion models through Optimal-Transport-inspired schedule modeling. Code:this https URL

---


### 64. [TerraDiT-$Ω$: Unified Spatial Control for Satellite Image Synthesis with Any Geospatial Primitive](https://arxiv.org/abs/2606.31029)

**<font color=#1a73e8>作者：</font>** Brian Wei, Srikumar Sastry, Daniel Cher 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models have achieved remarkable progress, yet applying them to satellite imagery remains challenging. Unlike natural imagery, satellite scenes are structured by spatially complex and semantically distinct geometries. Prior work addresses this complexity by adapting natural image frameworks using dense rasters or sparse prompts, trading off annotation cost and fidelity while breaking compatibility with vector primitives commonly used to represent geographic information. We introduce TerraDiT-$\Omega$, a unified spatial control framework that generates satellite imagery directly from any native geospatial primitive. By jointly leveraging precise annotations (polygons, polylines) and coarser ones (bounding boxes, points), the model supports controllable layouts across varying annotation budgets, broadening applicability to design tasks such as urban planning while remaining naturally compatible with end-to-end GeoAI workflows. To effectively leverage these primitives during generation, we propose Geometry-Aware Local Attention, a conditioning mechanism that injects explicit geometric cues into the attention space. Across all conditioning formats, our approach consistently outperforms both dense-control and sparse-control baselines. Furthermore, this flexibility enables controllable synthetic data augmentation using a single generative model, improving downstream performance on land-cover segmentation, object detection, road graph extraction, and scene classification. Code, data, and weights are available at this https URL.

---


### 65. [A Semantic-Layer-Mediated Agent for Natural Language to SQL over Heterogeneous Enterprise Databases](https://arxiv.org/abs/2606.31041)

**<font color=#1a73e8>作者：</font>** Ha Jeong Kim, Saksonita Khoeurn, Ye Ji Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language-to-SQL (NL2SQL) over real-world enterprise databases remains significantly more challenging than on academic benchmarks. Enterprise schemas often contain hundreds of physical tables with cryptic column names, heterogeneous SQL dialects, and complex analytical workloads requiring nested aggregations, temporal reasoning, and multi-table joins. We present a semantic-layer-mediated NL2SQL agent that decouples semantic intent from physical SQL execution. Rather than generating SQL directly over raw schemas, the agent reasons over a curated semantic layer through a compact intermediate representation called the Semantic Model Query (SMQ). A deterministic compiler translates each SMQ into dialect-specific SQL, providing verified building blocks that the agent composes into the final query. The system employs a constrained think-act loop, supports SQLite, BigQuery, and Snowflake backends, and is integrated into an end-to-end evaluation framework. Using Gemini 3 Pro, the system achieves 94.15% execution accuracy on the 547-task Spider2-snow benchmark, ranking third on the official leaderboard and substantially outperforming schema-only approaches. We describe the system architecture, SMQ representation, agent workflow, evaluation results, and discuss semantic-layer quality and the trade-off between improved grounding and overfitting.

---


### 66. [Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation](https://arxiv.org/abs/2606.31043)

**<font color=#1a73e8>作者：</font>** Ethan Hirschowitz, Fabio Ramos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We propose \textbf{Warp RL}, a policy adaptation method that replaces additive residuals with an invertible, state-conditioned transformation of the base policy's action distribution. Instantiated with monotonic rational-quadratic spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization, strictly generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.

---


### 67. [LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents](https://arxiv.org/abs/2606.31045)

**<font color=#1a73e8>作者：</font>** Jingpu Yang, Fengxian Ji, Zhengzhao Lai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific embodied agents are increasingly capable of carrying out laboratory procedures, but executing these procedures safely in dynamic laboratory environments remains challenging. Current safety approaches often overlook the intermediate step of transforming laboratory natural language, including safety rules, manuals, protocols, and standard operating procedures, into machine-checkable runtime constraints. We introduce LabGuard (Laboratory Guard), a language-to-execution safety suite that grounds natural-language laboratory rules into executable specifications and deploys them as runtime guards. LabGuard includes three core components: LabGuard-IR, which defines a typed executable representation; LabGuard-Bench, which provides 812 supervised annotations expanded from 203 seed laboratory rules; and LabGuard-Grounder, which maps natural-language laboratory rules into LabGuard-IR. The resulting IR instances are handled by the LabGuard Pipeline, which compiles them into runtime monitors and applies them at the controller boundary. Experiments show that LabGuard generalizes to unseen laboratory-rule sources, achieves 79.4 task-scope F1, and reduces unsafe events from 39.5% to 23.8% after monitor compilation. In LabUtopia, its runtime monitors integrate with ACT, keeping interventions below 0.5% while preserving task success.

---


### 68. [Learning Video Dynamics with Predictive Differentiable Rendering](https://arxiv.org/abs/2606.31050)

**<font color=#1a73e8>作者：</font>** Yujin Tang, Tian Zhou, Xin Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How to accurately predict a high-fidelity future world? While the visual world is inherently continuous, existing deterministic video prediction models operate in discrete pixel space and are mainly optimized with pixel-wise mean squared error (MSE), which often leads to over-smoothed predictions and a lack of fine-grained visual details. To address these limitations, we propose Predictive Differentiable Rendering (PDR), a novel end-to-end video prediction paradigm that bridges the gap between discrete and continuous representations. Inspired by recent progress in 3D reconstruction with 3D Gaussian Splatting, we introduce PredGS, a lightweight and plug-and-play adapter based on 2D Gaussian representation, which could be seamlessly integrated with existing pixel space predictors, significantly improving spatial detail preservation with negligible computational overhead. Furthermore, we develop predgsplat, a CUDA-accelerated differentiable 2D Gaussian renderer supporting arbitrary channels. Each Gaussian is defined by 5 + C learnable parameters (position, scale, rotation, and C channel amplitudes) and achieves up to 10x faster rendering than the baseline. Optimized by a combined L1 and SSIM loss, PDR overcomes the inherent blurring tendencies of MSE Loss, significantly enhancing the prediction performance. Extensive experiments on diverse real-world benchmarks, including TaxiBJ, WeatherBench, KTH, and Human3.6M, demonstrate that PDR consistently surpasses existing methods, delivering superior detail preservation, visual fidelity, and predictive accuracy.

---


### 69. [Reference-Based Prosody and Rhythm Evaluation for Spoken Dialogue Systems](https://arxiv.org/abs/2606.31055)

**<font color=#1a73e8>作者：</font>** Ashish Hallur, Thomas Thebaud, Georgi Tinchev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech (S2S) AI agents are advancing rapidly, yet evaluation lacks interpretable speech-native measures for conversational prosody and rhythm. Because $F_0$, speaking rate, articulation rate, and pausing shift with model-predicted speaker traits and interaction state, pooled human statistics can be poorly calibrated for evaluating a particular output. Using 4000+ hours of dyadic English conversation from the Seamless Interaction dataset, we construct matched reference regimes for $F_0$ mean, $F_0$ expressivity, speech rate, articulation rate, pause ratio, and mean pause duration. We then define a percentile-based evaluation protocol: extract the same metrics from an S2S output waveform, compare them to the closest matched human reference stratum, and report percentile deviations or 5th-95th percentile out-of-regime flags. On held-out human rows, pooled references over-flag state-conditioned $F_0$ expressivity and rhythm, while matched references return flag rates closer to the nominal 10% and make deviation direction interpretable. These outputs serve as behavioral plausibility checks that complement, rather than replace, perceptual and user-centered evaluation.

---


### 70. [Exploring the relationship between team institutional composition and novelty in academic papers based on fine-grained knowledge entities](https://arxiv.org/abs/2606.31058)

**<font color=#1a73e8>作者：</font>** Ziling Chen, Chengzhi Zhang, Heng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The composition of author teams is an important factor influencing the novelty of academic papers. However, existing studies have paid limited attention to the role of institutional composition, and most novelty measures remain at a general level, making it difficult to explain the specific sources and types of novelty in papers. Taking the field of natural language processing as an example, this study investigates the relationship between team institutional composition and the fine-grained novelty of academic papers. Author teams are classified into three types: academic institutions, industrial institutions, and mixed academic and industrial institutions. Four types of fine-grained knowledge entities are extracted from full-text papers, including methods, datasets, tools, and metrics. The novelty of papers is then measured based on entity combinations, and pairwise combinations of different entity types are further analyzed to examine their contributions to novel papers. The results show that, in the field of natural language processing, collaboration between industrial and academic institutions is more likely to produce novel papers than purely industrial collaboration. From the perspective of fine-grained knowledge entities, mixed academic and industrial teams pay more attention to the novelty of method-metric combinations, whereas industrial teams pay more attention to the novelty of method-tool combinations. This study reveals the relationship between institutional team composition and paper novelty through fine-grained novelty measurement, providing useful evidence for improving paper quality and promoting industry-academia-research collaboration.

---


### 71. [Diffusion-Based Material Regularization for Physics-Based Inverse Rendering](https://arxiv.org/abs/2606.31065)

**<font color=#1a73e8>作者：</font>** Jingwang Ling, Lifan Wu, Feng Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing physics-based 3D assets -- geometry, materials, and illumination -- from multi-view images is a core problem in computer graphics and vision, and a prerequisite for realistic relighting and editing. Physics-based inverse rendering offers an accurate image-formation model, but is severely underconstrained: without strong priors, illumination is baked into materials, and reconstructions generalize poorly to novel views and lighting. Data-driven diffusion models, in contrast, predict visually plausible materials, yet their predictions rarely satisfy the rendering equation and are not directly usable for physics-based rendering. We bridge these two paradigms rather than replacing either. Our key idea is to treat the predictions of a state-of-the-art diffusion model not as target material values but as a similarity kernel for optimization: we introduce a regularization loss that penalizes deviations in the optimized material over surface regions where the diffusion predictions are near-constant, while leaving the optimization free to match the input images. Built on this regularizer, our end-to-end pipeline jointly reconstructs geometry, materials, and illumination, yielding high-quality assets that drop into standard rendering pipelines and relight faithfully. On the Synthetic4Relight, Stanford-ORB, and DTC-Synthetic datasets, our method significantly outperforms state-of-the-art baselines in both reconstruction accuracy and relighting quality.

---


### 72. [Secure-CHG: A Comprehensive Framework for Robust and Fair Federated Learning via Hybrid Defense and Contribution-Aware Trust](https://arxiv.org/abs/2606.31066)

**<font color=#1a73e8>作者：</font>** Guanming Che, Qiang Wang, Jian Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is highly susceptible to stealthy backdoor attacks, which aim to force a model into predicting an attacker-chosen target class for inputs containing a specific trigger. However, existing statistical defenses primarily focus on the early stages of model convergence. In this paper, we identify a fundamental vulnerability termed ``Late-stage Failure.'' We demonstrate that as the global model converges, decaying gradient norms render malicious and benign updates morphologically indistinguishable. This vanishing statistical variance effectively blinds traditional defenses, enabling adaptive adversaries to remain dormant and subsequently hijack the training process. To overcome these constraints, we propose Secure-CHG, a hybrid framework that pivots the defense paradigm from superficial morphological detection toward intrinsic semantic contribution verification. Secure-CHG employs an adaptive defense pipeline: a cascaded statistical filter stabilizes optimization during the early oscillatory phase, while a novel CHG-Shapley mechanism takes over during late-stage convergence. By leveraging sample hardness (i.e., local training loss) to project updates into a composite Hardness-Gradient space, it effectively amplifies adversarial semantic traces, enabling the isolation of stealthy attackers even as gradient norms vanish. Furthermore, we derive a closed-form solution for CHG-Shapley, facilitating low-complexity, retraining-free node valuation and trust-modulated aggregation. Extensive evaluations on CIFAR-10, MedMNIST, and NEU-SDDB demonstrate that Secure-CHG effectively mitigates Late-stage Failure. Specifically, it significantly suppresses advanced backdoor attacks, reducing their attack success rate by 2.3$\times$ and 2.0$\times$ relative to the mainstream Krum and Trimmed Mean baselines, respectively.

---


### 73. [Hybrid Unet-Transformer Model for Generating Stress and Strain Fields from Composite Geometrics](https://arxiv.org/abs/2606.31068)

**<font color=#1a73e8>作者：</font>** Shrey Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of stress and strain fields in hierarchical composite microstructures is critical for physics-informed material design, yet conventional finite element method (FEM) simulations are computationally prohibitive at scale, requiring minutes to days per evaluation. In this work, we propose a hybrid UNet-Transformer architecture that predicts complex mechanical field distributions directly from composite microstructure geometry images, serving as an efficient surrogate for FEM across ten distinct stress and strain field types spanning diverse two-phase composite configurations including square, hexagonal, and triangular tessellations, multiple boundary conditions, and high-resolution geometries. Results demonstrate that the proposed architecture achieves strong predictive performance across the majority of subdatasets, with peak accuracy on periodic tessellation geometries reaching R2=0.9991, SSIM=0.9936, and MAE=0.0050 on the boundary condition subdataset and the triangular tessellation subdataset respectively. Across six of the eight evaluated subdatasets, MAE remains below 0.05 on the normalized [0,1] pixel scale. Encoder attention analysis via Grad-CAM and Grad-CAM++ confirms that the model develops physically meaningful internal representations, localizing attention at mechanically critical regions including phase boundaries, ligament junctions, and indenter contact zones without explicit structural supervision. Performance degrades on irregular square-grid geometries with sparse soft-phase inclusions, with the S11 normal stress subdataset yielding R2=0.7735 and SSIM=0.7126, consistent with the known limitation of smooth-loss image translation models in reproducing sharp stress discontinuities.

---


### 74. [Hierarchical 3D Scene Graph Construction and Belief-based Planning for Semantic Navigation](https://arxiv.org/abs/2606.31071)

**<font color=#1a73e8>作者：</font>** Bing Wu, Zuyao Chen, Changwen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic navigation is a fundamental task for embodied agents operating in unseen environments, requiring both semantic understanding and long-term decision-making. Recent foundation models have empowered agents with rich semantic priors for this task. However, without structured global representations, decision-making often falls back on local observations and greedy strategies, resulting in inefficient exploration and myopic behaviors, especially in long-distance navigation. To address these challenges, we propose a zero-shot semantic navigation framework. Our method incrementally maintains an online Hierarchical 3D Scene Graph (HSG) to form a multi-granular semantic topology over objects, zones, and regions, serving as a compact state abstraction for global planning. Building on this memory, we introduce a hierarchical belief-based planning framework that fuses semantic priors with exploration evidence on the HSG, and performs finite-horizon rollouts on an HSG-based simulator to explicitly estimate the long-term expected returns of candidate macro-actions. This enables globally consistent decisions and reduces redundant backtracking. Extensive experiments in high-fidelity simulation environments across multiple tasks and datasets demonstrate that our method outperforms existing state-of-the-art methods, particularly in long-distance scenarios, where our approach improves SR and SPL by an average of 9.4\% and 5.0\%, respectively.

---


### 75. [Triospect: A Three-Dimensional Framework for Robust Statistical AI-Generated Text Detection Against Diverse Attacks](https://arxiv.org/abs/2606.31074)

**<font color=#1a73e8>作者：</font>** Guangsheng Bao, Lihua Rong, Yanbin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing AI-generated text detectors are vulnerable to attacks that manipulate textual characteristics. In this study, we propose a novel Triospect Detection Framework by using additional perspectives of content (core ideas) and expression (stylistic elements) within a given text. Experiments on two benchmarks involving 17 attacks, 12 domains, and 17 source models demonstrate that Triospect is robust against these attacks. It improves the strong baseline by a significant margin of 22.3% (AUROC) and 13% (TPR01) on the Humanize-16K after-attack subset, and by 9.1% (AUROC) and 22% (TPR01) on the adversarial RAID. This framework marks a pioneering effort in statistical methods to enhance detection reliability against attacks. We release our data and code at this https URL.

---


### 76. [AnyMatch: Supercharging Universal Multi-Modal Image Matching with Large-Scale Single-View Images](https://arxiv.org/abs/2606.31077)

**<font color=#1a73e8>作者：</font>** Meng Yang, Zizhuo Li, Linfeng Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal image matching is essential for visual localization and multi-sensor fusion, but it is hindered by the scarcity of large-scale training data with precise geometric annotations. Existing real-world datasets suffer from prohibitive costs, limited scene diversity, and errors in SfM-MVS pipelines, while synthetic methods struggle to maintain 3D geometric consistency or achieve photorealistic appearance. To address this, we propose AnyMatch, a novel framework that leverages abundant, easily accessible single-view images at minimal cost to generate rich multi-modal training data. AnyMatch integrates monocular depth estimation, 3D reprojection, diffusion-based inpainting, and crossmodal image translation to synthesize multi-view, multi-modal image pairs with 3D geometric fidelity. Crucially, our method provides annotations that strictly adhere to 3D geometric consistency through explicit 3D reprojection, avoiding SfM-MVS error accumulation. Furthermore, AnyMatch offers strong scalability, enabling controllable scene diversity and annotation difficulty via adjustable input and camera parameters. We construct Any-syn, a large-scale synthetic multi-modal dataset using AnyMatch. Experimental results show that matching networks (e.g., LoFTR, EDM, RoMa) fine-tuned on Any-syn achieve substantial performance gains on multi-modal benchmarks, exhibiting superior generalization and robustness compared to models trained on existing data.

---


### 77. [Fleet: Few Shots Lead Effective AI-generated Image Detection](https://arxiv.org/abs/2606.31082)

**<font color=#1a73e8>作者：</font>** Jiaan Wang, Sirui Liu, Yu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image (AIGI) detection is undergoing a critical transition from laboratory benchmarks to open-world adversarial defense. The prevalent paradigm focuses on finding static feature spaces, assuming that some invariant artifacts learned from historical data can achieve universal zero-shot generalization. While achieving saturation on several AIGI benchmarks, this static hypothesis suffers a severe performance drop against rapidly evolving generators (e.g., SD3, Nano Banana Pro). To address these limitations, we propose that the field should expand beyond "static generalization" to a new paradigm of "dynamic adaptation". We introduce Fleet, a framework that pioneers a dynamic paradigm of continuous few-shot evolution, enabling rapid alignment with emerging generative threats. Fleet improves few-shot adaptation by replacing unconstrained feature updates with constrained routing correction, where avoidance routing redirects novel AI samples away from Non-AI-dominated routes within decoupled subspaces. To validate this, we present Treasure, a benchmark spanning 64 models and 360k images, featuring diverse architectures and 20 closed-source commercial engines. Experiments reveal that while static SOTA methods fail catastrophically on modern generators, Fleet restores performance from 20.4% to 73.1% with only 10-shot adaptation on "Doubao Seedream 4.0". Code and data are available at this https URL .

---


### 78. [DDIAgents: Mechanism-Conditioned Context Flow for Drug-Drug Interaction Prediction](https://arxiv.org/abs/2606.31085)

**<font color=#1a73e8>作者：</font>** Zhenqian Shen, Yu Liu, Xiaoyi Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Drug-drug interaction (DDI) prediction is essential for medication safety, yet it requires reasoning over heterogeneous biomedical evidence whose relevance changes across interaction mechanisms. We propose DDIAgents, a mechanism-conditioned multi-agent framework that performs DDI prediction through dynamic knowledge orchestration. Given a drug pair, a planner agent instantiates specialized expert agents, routes mechanism-relevant knowledge sources to each agent, and aggregates their analyses through a conclusion agent. By adapting context flow to the inferred interaction mechanism, DDIAgents reduces irrelevant information, supports complementary expert reasoning, and produces interpretable agent-level rationales. Extensive experiments on realistic DDI prediction benchmarks show that DDIAgents consistently outperforms existing feature-based, graph-based, LLM-based, and agent-based baselines. Beyond prediction performance, DDIAgents demonstrates how multi-agent systems can organize heterogeneous scientific knowledge for adaptive and interpretable AI4Science reasoning.

---


### 79. [CasaMaestro: Multi-View Panoramas for House-Scale 3D Reconstruction](https://arxiv.org/abs/2606.31086)

**<font color=#1a73e8>作者：</font>** Yuzhou Ji, Xiaotian Yang, Zhipeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rise of home-deployed embodied AI systems is driving a growing need for fast, metric 3D reconstruction of residential spaces to support navigation, interaction, and long-horizon task execution. However, the commonly used pinhole-camera 3D reconstruction pipelines struggle to model large indoor residences efficiently due to their limited field of view, to which achieving full coverage across multiple rooms often requires thousands of images and incurs drift from long chains of incremental alignment. In this work, we present CasaMaestro (Spanish words meaning ``house'' and ``master''), a feedforward model that can take only twenty to fifty sparse multi-view indoor panoramas as input and directly predicts metric depth along with camera poses, allowing fast point-cloud reconstruction of the entire house with full coverage. CasaMaestro is the first model that supports house-scale reconstruction with multi-view panoramas. Experiments show that CasaMaestro can robustly provide high quality results in both real-world and synthetic scenes, which can serve as a strong foundation for acquiring house-scale 3D indoor assets to be applied in close-loop simulation.

---


### 80. [When Reranking Hurts: Uncertainty-Based Gating for Few-Shot Reranking](https://arxiv.org/abs/2606.31087)

**<font color=#1a73e8>作者：</font>** Orian Dabod, Amir Cohen, Gabriel Stanovsky  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Few-shot selection typically assumes that reranking retrieved examples always improves performance. We challenge this view by identifying that the expensive reranking step can in fact degrade performance. Instead, we propose \emph{Training-Free Gated Reranking}, which decides whether to rerank the few-shot examples based on the model's uncertainty. Extensive experiments across 8 LLMs, covering 7 NLU datasets and 9 MT domain-language combinations, demonstrate that our approach reduces computational costs by 15\%-80\% while improving average performance by up to 2\%. These findings indicate that higher computational cost does not guarantee better performance, and that reranking is most beneficial when targeted at high-uncertainty instances.

---


### 81. [Towards Flexible, Natural, Efficient Interaction for Conversational Talking Face Generation](https://arxiv.org/abs/2606.31088)

**<font color=#1a73e8>作者：</font>** Baiqin Wang, Sen Chen, Jiankuo Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conversational talking face generation has recently attracted increasing attention, aiming to synthesize interactive talking videos where characters speak, listen, and respond dynamically to each other. This task presents three core challenges: 1) Flexibility: enabling multi-round dialogues with an arbitrary number of participants; 2) Naturalness: maintaining coherent motion and appropriate non-verbal feedback throughout the interaction; and 3) Efficiency: achieving real-time generation and low computation overhead for long-term continuous online conversation. Despite recent advances, existing methods still fall short in balancing all three requirements. To bridge this gap, we introduce InterTalk, a novel and efficient framework designed for highly interactive conversational talking face generation. Built upon a motion-based architecture, InterTalk supports real-time conversation synthesis. Our method achieves strong flexibility by explicitly modeling multi-round conversational dynamics among each participant, eliminating constraints on their numbers. To enhance interactivity, we incorporate motion feedback from multiple participants and introduce an iterative generation strategy for more natural behaviors. Besides, we disentangle motion into several facial components, enabling targeted refinements for natural response such as precise lip sync and realistic eye blinking. Finally, we construct a new multi-person conversational dataset and enrich it with 3D face-based data augmentation. Extensive experiments demonstrate that InterTalk achieves superior interaction quality while maintaining real-time performance at 30 FPS.

---


### 82. [Anchoring on Reality: Breaking the Pseudo-Target Ceiling in Makeup Transfer](https://arxiv.org/abs/2606.31089)

**<font color=#1a73e8>作者：</font>** Bo Wei, Xianhui Lin, Yi Dong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Makeup transfer applies a reference cosmetic style to a source face while preserving its identity and geometry. However, this task is severely hindered by the lack of real paired training data. Current methods rely on either weak priors or synthetic pseudo-targets from large-scale editing models. These paradigms provide suboptimal guidance, often leading to degraded fine-grained details, synthetic artifacts, and identity drift. To this end, we propose Anchoring on Reality Makeup Transfer (ART), a two-stage framework with a reality-anchored refinement cycle. In Stage I, the model is initialized with pseudo-targets to establish basic semantic alignment and global makeup placement. Crucially, Stage II shifts supervision from pseudo-targets to the real reference, reconstructing it from its bare-skin counterpart through a differentiable cycle that penalizes any omitted detail and overrides synthetic artifacts. Furthermore, we introduce MakeupFaces2K (MF2K), the first 2K-resolution in-the-wild makeup portrait dataset comprising 8,573 images. Extensive experiments demonstrate that our method achieves superior makeup fidelity, strong background stability, and robust identity preservation, especially for complex makeup styles.

---


### 83. [Do Not Break the Vessels: Structure-Preserving Mean Flow for Vascular Image Translation](https://arxiv.org/abs/2606.31095)

**<font color=#1a73e8>作者：</font>** Changjin Sun, Zhuo Hu, Kaini Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing anatomically faithful vascular structures from clinically accessible imaging modalities is of substantial clinical significance. However, existing cross-modal translation methods mainly emphasize pixel-level fidelity or visual realism and treat structure preservation as a property of the final output rather than an invariant of the generative process. This limitation often leads to structural discontinuities and artifacts, compromising anatomical coherence and clinical reliability. In this work, we propose a Structure-Preserving Mean Flow (SPMF) framework that formulates vascular image translation as a topology-invariant transport process. Based on a structural invariance principle, we derive an orthogonality constraint on the flow velocity field that formally separates appearance transport from topological distortion. We implement this constraint as a time-weighted surrogate objective within a Brownian bridge diffusion model to preserve topology at every diffusion step. Moreover, we propose a Prototype-Guided Structural Refinement (PGSR) module to align degraded inference-time structures with reliable training-time structures. Experiments on paired NIRII-to-2PF and fundus datasets demonstrate consistent improvements over state-of-the-art methods, achieving peak PSNR values of 24.96 dB and 24.83 dB, respectively.

---


### 84. [Horizon3D: Sparse Radar-Camera Fusion for Long-Range 3D Perception in Autonomous Driving](https://arxiv.org/abs/2606.31096)

**<font color=#1a73e8>作者：</font>** Geonho Bang, Geunju Baek, Dongyoung Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-range 3D object detection is critical for safe autonomous driving at highway speeds, yet existing radar-camera fusion methods remain limited at extended ranges. BEV-based methods capture scene-level context but incur rapidly growing computation and often lose fine-grained object detail, while query-based methods are efficient but provide limited scene-level context. Temporal fusion further requires both multi-frame accumulation for sparse distant observations and object-level motion modeling for fast-moving objects. We propose Horizon3D, a sparse radar-camera fusion framework for long-range 3D object detection that combines Gaussian primitives with sparse BEV features. Horizon3D initializes Gaussian primitives at radar- and camera-estimated object keypoints using Keypoint-Guided Gaussian Initialization, refines them through Object-Centric Sparse Fusion, and splats them onto the BEV plane to fuse object-level detail with sparse radar BEV context. It further introduces Dual-Path Temporal Fusion, which aggregates temporal cues through a BEV path for scene-level accumulation and a Gaussian path for object-level motion propagation. Experiments on TruckScenes show that Horizon3D achieves state-of-the-art radar-camera 3D detection performance. On the validation set, it outperforms the previous best method by +3.0 NDS and +1.6 mAP while maintaining competitive inference speed.

---


### 85. [TaxoMIL: Taxonomy-Constrained Learning for Hierarchical Whole Slide Image Analysis](https://arxiv.org/abs/2606.31100)

**<font color=#1a73e8>作者：</font>** Chaeyeon Lee, Khang Nguyen Quoc, Jinsol Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole slide image (WSI) analysis is central to computational pathology, with multiple instance learning (MIL) emerging as the standard pipeline for slide-level diagnosis. However, conventional approaches formulate WSI diagnosis as a flat classification task over discrete labels, contradicting the inherently hierarchical, coarse-to-fine nature of clinical reasoning. Although recent hierarchical classifiers and vision-language models (VLMs) have sought to address this structural gap, they either fail to capture semantic continuity between related diagnoses or suffer from unconstrained text generation that produces taxonomic hallucinations and parent-child label violations. To address these limitations, we propose TaxoMIL, a taxonomy-constrained framework that reformulates WSI diagnosis as a multi-granularity text generation task. TaxoMIL utilizes a dual-head Transformer decoder to generate coarse- and fine-level diagnostic text, and introduces taxonomy-guided objectives that explicitly structure the label embedding space and strictly ground slide-level visual representations within the clinical taxonomy. Extensive experiments across three diverse WSI datasets demonstrate that TaxoMIL consistently outperforms state-of-the-art MIL classifiers and VLM-based generative methods, yielding accurate and hierarchy-aware diagnostic predictions. The code is released at this https URL

---


### 86. [InfiniVerse: Occupancy Guided Unbounded Scene Generation for Autonomous Driving](https://arxiv.org/abs/2606.31109)

**<font color=#1a73e8>作者：</font>** Xiaoyu Ye, Leheng Li, Xinyu Ji 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic, controllable, and temporally coherent urban environments is a critical yet unresolved challenge in the autonomous driving community. In this paper, we introduce InfiniVerse, a unified pipeline for long-range, 2D-3D-aligned, and controllable synthesis of dynamic urban scenes from a single frame. In practice, our approach first reconstructs a 3D occupancy representation from the input multi-view frame. This representation serves as a foundation for autoregressive scene extension along arbitrary trajectories. Subsequently, a video diffusion model translates the coarse occupancy grid into realistic, spatiotemporally consistent video sequences. Moreover, we propose a hierarchical sketch-and-refine paradigm, in which the generated videos are re-projected as image-conditioned feedback to enhance the 3D occupancy representation, establishing cross-modal alignment and mutual enhancement between the visual and spatial domains. Extensive evaluations on the Waymo Open Dataset and nuScenes demonstrate that InfiniVerse achieves state-of-the-art performance, with a FID of 6.4 and FVD of 67.97, significantly outperforming existing benchmarks in both duration and stability.

---


### 87. [Explaining Machine Learning and Memorization with Statistical Mechanics](https://arxiv.org/abs/2606.31110)

**<font color=#1a73e8>作者：</font>** Robin Theriault  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial neural networks (NNs) and machine learning (ML) algorithms are poorly understood from a theoretical perspective, which makes it difficult to fully realize their potential and overcome their weaknesses. For instance, ML algorithms train NN weights by moving them along a low-dimensional subspace of their allowed values, but this implicitly low-dimensional learning structure is not properly exploited to improve training because its nature is not well understood. Moreover, trained NNs are easily confused by pervasive adversarial attacks whose theoretical underpinnings are still unclear. This thesis aims to improve our theoretical understanding of NNs and ML, with a particular focus on adversarial attacks and implicitly low-dimensional learning. For this purpose, we use mathematical tools from statistical mechanics to study different types of NNs and ways in which they can fit the data. In particular, we study two classes of models that fit the data with various degrees of learning and memorization: dense associative memory (DAM) and restricted Boltzmann machines (RBM). In the process, we investigate connections between different versions of these models that are useful to make analytical investigations more efficient.

---


### 88. [What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR](https://arxiv.org/abs/2606.31112)

**<font color=#1a73e8>作者：</font>** Hawau Olamide Toyin, Srinivasan Umesh, Hanan Aldarmaki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ASR systems have been often reported to underperform on atypical speech. An often conflated compounding factor is the existence of two valid transcription references: verbatim (actual produced speech, including repetitions/prolongations) and intended (the canonical form of the text with disfluencies removed) in atypical speech recognition depending on context and use-case. Most ASR evaluations conflate this duality into a single ground truth and reward systems that delete disfluencies, ignoring verbatim faithfulness. We benchmark 11 ASR models from encoder-decoder, CTC and transducer families using both verbatim and intended references on atypical stuttered speech as a case study. Our quantitative assessment underlines the disparity in model performance and rankings using the two transcript styles. Through this analysis, we highlight the importance of selecting a suitable transcription reference for valid model selection depending on the use-case, particularly for atypical ASR.

---


### 89. [Revealing Safety-Critical Scenarios for UTM via Transformer](https://arxiv.org/abs/2606.31114)

**<font color=#1a73e8>作者：</font>** Huaze Tang, Bill Zeng, Chao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unmanned Traffic Management (UTM) systems are cloud-based platforms designed to manage and coordinate multiple aerial vehicles remotely. UTM systems are safety-critical which cannot tolerate failures like crash or collision. To reveal latent vulnerabilities, there are neither optimal failure-exposing demonstrations nor clear reward signals. Additionally, UTM's self-healing capability introduces the ``long-tail effect'' of critical failures. We propose framing UTM vulnerability discovery as a sequence modeling problem amenable to transformer-based RL architectures. Our approach leverages attention mechanisms to directly model the relationship among system states, and predict optimal actions. Our framework introduces a Policy Model that generates targeted test scenarios and an Action Sampler that enforces domain constraints. We use a risk-based reward function to guide exploration. Through extensive evaluation on a 700-hour simulation study, we demonstrate an 8$\times$ improvement in vulnerability discovery efficiency compared to expert-guided testing. It also discovers critical edge cases that traditional methods have missed.

---


### 90. [JacobianAvatar: Temporally Consistent Semi-rigid Avatar Reconstruction from a Monocular Video](https://arxiv.org/abs/2606.31115)

**<font color=#1a73e8>作者：</font>** Changyeon Won, Min-Gyu Park, Seonghwan Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic human avatars in complex motions--such as clothing dynamics--requires modeling of global and local deformations which remains challenging in monocular settings. We address this problem by leveraging neural Jacobian fields (NJFs) for representing semi-rigid deformations. We train self-supervised neural networks for predicting Jacobian matrices that give the pose-dependent deformations, by solving a Poisson equation. However, monocular input presents several difficulties such as self-occluded regions and invisible surfaces. To address these issues, we introduce three key components: a constrained Poisson solver, signed distance-based Jacobian regularization, and a deformation-guided residual flow loss, which together suppress boundary artifacts, recover frequently occluded regions such as armpits and thighs, and enforce temporal consistency during motion. Experiments on benchmark and in-the-wild videos demonstrate that our method generates temporally stable and geometrically coherent avatars, outperforming state-of-the-art approaches.

---


### 91. [Visualizing High-Dimensional Graph Embeddings via Informed Multi-View Projections](https://arxiv.org/abs/2606.31119)

**<font color=#1a73e8>作者：</font>** Ya Ji, Xuefeng Li, Timo Brand 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphs are commonly visualized in 2D, where humans readily interpret spatial relationships, yet such layouts often distort higher-dimensional structure. We propose to embed graphs in high-dimensional space and search for informative 2D viewpoints that optimize aesthetic and readability metrics (e.g., edge crossings and angular resolution), enabled by a novel differentiable surrogate for edge crossings. Numerical experiments show that these viewpoints consistently outperform standard 2D layouts, and can even surpass methods explicitly designed to optimize these metrics. We further introduce DataFly, an interactive system for exploring multiple candidate viewpoints through seamless navigation. A usability study demonstrates that our approach reveals structural patterns that remain hidden in conventional 2D visualizations.

---


### 92. [WildProp: Visual Estimation of Wildlife Body Proportions at Scale](https://arxiv.org/abs/2606.31125)

**<font color=#1a73e8>作者：</font>** Mustafa Chasmai, Aaron Sun, Subhransu Maji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Population-level morphometric measurements underpin ecological and evolutionary studies but traditionally require controlled imaging or physical specimen handling, limiting scalability. We present WildProp, a training-free framework that estimates wildlife body proportion distributions directly from large-scale, unconstrained image repositories. We cast morphometric estimation as a retrieval-driven correspondence problem: given a single user-annotated canonical image, WildProp performs pose-aware retrieval using foundation model features, transfers part endpoints via dense patch-level matching, filters predictions using geometric consistency, and aggregates measurements across retrieved images to estimate population-level ratio distributions. Unlike supervised keypoint pipelines, our approach adapts to arbitrary species and user-defined parts without per-species training. Evaluations on three large morphometric datasets spanning birds and amphibians show median relative errors of 10-20%. We further highlight the broad applicability of our approach through a number of case studies measuring various proportions across diverse taxa, including birds, frogs, insects, and flowers. Ablations demonstrate that pose-aware retrieval is critical for stable estimation, while robust aggregation mitigates keypoint and pose noise. Our results indicate that carefully curated 2D correspondences over web-scale imagery can provide scalable morphometric proxies for comparative and subgroup analyses across taxa, geography, and seasonality.

---


### 93. [Can Tabular In-Context Learners Generalize to Biomolecular Property Prediction?](https://arxiv.org/abs/2606.31126)

**<font color=#1a73e8>作者：</font>** Davy Guan, Lu Zhang, Asiri Wijesinghe 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting biomolecular properties from limited labeled data is a central bottleneck in protein engineering and small-molecule design. As strong pretrained encoders now supply rich fixed-length representations, the difficulty has shifted from representation learning to building a data-efficient predictor for the few-shot regime. Tabular foundation models such as TabPFN3 and TabICL are unlikely candidates for this role: they are in-context learners pretrained on synthetic tables drawn from random causal graphs, a generative prior with no obvious correspondence to the processes that produce protein sequences or molecular graphs. That this tabular, causal inductive bias should transfer to biomolecular data at all is unintuitive, yet we find it does. Treating each method as a predictor-representation pair, we evaluate across two domains. Over a fixed ESMC representation, tabular in-context learning is consistently competitive for protein fitness regression on ProteinGym and a diverse esterase dataset. For small-molecule classification with ECFP/RDKit descriptors, no single pairing dominates across TDC ADMET, MoleculeNet, FS-Mol, and DrugOOD; representation choice becomes a primary determinant, as expected when the predictor's own prior is indifferent to molecular structure. We conclude that tabular foundation models are strong performers on biomolecular prediction tasks, but that their performance depends strongly on the sequence or molecular representation used.

---


### 94. [SkillSpotter: Pose-Aware Multi-View Skilled Action Detection and Grading in Ego-Exo Videos](https://arxiv.org/abs/2606.31127)

**<font color=#1a73e8>作者：</font>** Björn Braun, Christian Holz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To enable personalized, real-time coaching using Augmented Reality glasses or fixed camera setups in domains such as sports, cooking, or music, a system must understand not just what a person does, but how well they execute an activity. In an ego-exo video setting, this requires simultaneously detecting individual skilled actions and classifying each as correct or needing improvement, which Ego-Exo4D's proficiency demonstration benchmark formalized. We first adapt seven state-of-the-art temporal action detection architectures to this task, extend the evaluation protocol to disentangle detection from grading, and show that existing methods grade near-randomly. We then introduce SkillSpotter, a pose-aware multi-view architecture that jointly detects and grades skilled actions through three task-specific modules: (1) adaptive temporal suppression to handle the varying density of skilled actions across diverse activities, (2) gated 3D body pose fusion to leverage body kinematics as a complementary signal to visual features, and (3) bidirectional cross-view attention to combine ego and exo views effectively. SkillSpotter improves class-specific mAP from 12.40 to 21.82 (+76%) and balanced accuracy from 55.99% to 60.40% over the best baseline. SkillSpotter's modules transfer to other temporal action detection models with consistent gains, and our method generalizes beyond Ego-Exo4D to HoloAssist. Code: this https URL

---


### 95. [Scenario Generation for Testing of Autonomous Driving Systems Using Real-World Failure Records](https://arxiv.org/abs/2606.31131)

**<font color=#1a73e8>作者：</font>** Anjali Parashar, Chuchu Fan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To ensure safe on-road behavior, pre-deployment testing and failure discovery of Autonomous Driving Systems (ADS) is crucial. Present day simulation based testing methods focus largely on mathematical models for efficient search of optimal scenarios, assuming a fixed scenario representation. On the other hand, real-world testing involves substantial manual effort to design scenario templates for testing. These templates represent distinct failure scenarios consisting of pre-deployment vehicle movements, map types, etc. Historical failure records for ADS are a reliable source of real-world failure conditions, which can be used for scenario generation. In this work, we propose a scenario generation pipeline using categorical and contextual information available from historical records in natural language format. Our approach consists of modular LLM based synthetic scenario generation, compatible with the testing constraints of a given system. We successfully apply our method to generate a diverse set of scenarios for testing autonomous navigation on Metadrive simulator using the NHTSA ADS crash records. Our approach results in accurate and diverse scenario generation with a combination of 4 road types, 3 non ego vehicle movement types, including on road anomalies in the form of working zones. Generated scenarios align with the provided testing conditions, and reveals interesting failures of the system within a limited testing budget of 20 scenarios. Code is available at this https URL.

---


### 96. [MSNN-LINet: Cross-Modal Learning via Continuous Linear Integration](https://arxiv.org/abs/2606.31135)

**<font color=#1a73e8>作者：</font>** Gabriel Clinger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LINet (Linear Integration Network), a Multi-Stream Neural Network (MSNN) for RGB-D scene classification. Current multi-modal architectures treat feature fusion as a discrete, ad-hoc event: early fusion entangles representations prematurely, late fusion isolates them until the final layer, and hybrid or attention-based methods require architectural guesswork to place intermediate fusion blocks. LINet addresses this structural compromise by maintaining three dedicated parallel streams (RGB, depth, and integration) where a novel Linear Integration Convolution (LIConv2d) operator enables continuous cross-modal learning at every layer. The integration stream receives raw filtered signals from both modality streams and combines them before the nonlinear activation threshold, conceptually inspired by somatic integration preceding the neuronal firing decision. Implementing continuous integration exposes a critical initialization pathology: Kaiming initialization of the bridging weights scrambles gradients before they reach the stream backbones, producing a failure mode that resembles overfitting but is corrupted gradient flow. A 1/N constant initialization mitigates this. We employ progressive modality dropout, a curriculum adapted to continuous fusion in which blanking probability increases from zero, preventing pathway collapse, a form of negative co-learning, by forcing robust independent stream representations. Trained from scratch on SUN RGB-D 19-class scene classification, LINet reaches 45.2% mean class accuracy at ResNet18 scale, outperforming prior from-scratch results, and rises to 49.6% with in-domain RGB-D (ScanNet) pretraining.

---


### 97. [FROST: Training-Free Few-Shot Segmentation with Frozen Features and Nonparametric Statistics](https://arxiv.org/abs/2606.31136)

**<font color=#1a73e8>作者：</font>** Junghwan Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot segmentation asks a model to delineate a target class in a query image from only a handful of annotated examples, a setting most acute in remote sensing, where labels are scarce and the imagery departs sharply from the natural images on which vision backbones are pretrained. Prevailing approaches either train a segmenter on labelled episodes, which raises accuracy within the training distribution but binds the model to it, or reduce each class to a lossy summary of frozen features, a single prototype, a few cluster prototypes, or a discrete clustering, none of which preserves the internal structure of a multimodal class. We argue that a class is better described by a distribution than by a point, and that frozen self-supervised features already carry enough structure to estimate that distribution directly. We introduce FROST, a training-free few-shot segmenter that treats the reference foreground and background as two point clouds on the unit sphere of frozen DINOv3 features and labels each query token by a nonparametric density ratio, with a threshold the Bayes rule fixes at zero under equal priors. Because the variance of a density estimate shrinks as its sample grows, the decision sharpens as references accumulate, and every remaining quantity from the kernel bandwidth to the spatial gate is read from the support set rather than tuned. We develop FROST for overhead imagery, where a class is typically a scatter of many small and dissimilar instances that a density tracks but a lossy summary blurs. Across seventeen remote-sensing benchmarks FROST surpasses both training-free and learning-based methods, leading by 5.6 mIoU from a single annotated example and widening its lead as the support set grows, all while remaining among the smallest models compared. Code is available at this https URL.

---


### 98. [A Bayesian Filtering Approach for Learning Lagrangian Dynamics from Noisy Measurements](https://arxiv.org/abs/2606.31137)

**<font color=#1a73e8>作者：</font>** Kundan Kumar, Shreya Das, Simo Särkkä  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a Bayesian filtering-based approach for learning the dynamics of a physical system from partial, noisy measurements. We model the system dynamics using a Lagrangian mechanics formulation. As in Lagrangian neural networks (LNNs), we parameterize the kinetic and potential energies with neural networks. The unknown external forces in the Lagrangian formulation are modeled as white Gaussian noise. The corresponding Euler--Lagrange equations then yield a continuous-time stochastic state-space model (SSM) that describes the system dynamics. The neural network parameters and system states are then jointly learned via a maximum-likelihood method using Gaussian-approximation-based Bayesian filters. The effectiveness of the proposed method is demonstrated on pendulum and Duffing oscillator examples, and its performance is compared with conventional LNNs and with approximate Bayesian filters using known system models.

---


### 99. [WaterGen: Decoupling Scene and Medium in Underwater Image Generation](https://arxiv.org/abs/2606.31147)

**<font color=#1a73e8>作者：</font>** Jiayi Wu, Tianfu Wang, Tianyi Xiong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater computer vision tasks, such as detection, restoration, and segmentation, are limited by the scarcity of large-scale and diverse training data. We introduce WaterGen, a method for generating large-scale, realistic, and diverse underwater images that provides independent control of the scene and water medium conditions. Our approach treats underwater image generation as the decoupled control of two factors: realistic and diverse scene content (what is in the image), and accurate and controllable water medium effects (what the water does to the image). Existing methods generally achieve only part of this objective: they either provide controllability with limited realism or diversity, or generate realistic scenes without accurately and independently modeling water-medium effects. Our key insight, that allows us to avoid this compromise, is that scene generation and medium modeling can be decoupled within a latent diffusion framework, enabling diverse scene generation together with accurate and controllable underwater appearance. To do this, we decompose underwater image synthesis into two stages. First, we fine-tune the latent diffusion U-Net using degradation-free underwater images so that it learns to generate diverse and realistic latent embeddings of underwater scene content without medium-induced degradation. Second, we formulate the physically accurate medium degradation synthesis as a conditional decoding process applied to these latent embeddings. This decoupled design allows our model to generate diverse scenes with full control of underwater appearance. We leverage WaterGen to build large-scale synthetic underwater datasets that are diverse in scene structures and accurate in water effects and pseudo-labels. We demonstrate that our synthetic data consistently improve downstream performance in underwater restoration and semantic segmentation.

---


### 100. [PruneGround: Plug-and-play Spatial Pruning for 3D Visual Grounding](https://arxiv.org/abs/2606.31148)

**<font color=#1a73e8>作者：</font>** Duc Cao Dinh, Khai Le-Duc, Florent Draye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Visual Grounding (3DVG) aims to localize target objects in 3D scenes given natural language descriptions. Existing approaches typically perform reasoning over the entire scene, leading to ambiguous predictions and high computational cost, especially in cluttered environments. We observe that many referential expressions rely on local spatial context and often correspond to restricted spatial regions rather than the full scene. Motivated by this insight, we propose PruneGround, an effective plug-and-play framework for 3DVG built upon three key components. First, we introduce Language-Guided Spatial Pruning (LGSP), which leverages a frozen Vision Language Model (VLM) to identify language-relevant regions, thereby reducing spatial computation and grounding candidates in the narrower search space. Second, we propose MultiView-Conditioned Description Reformulation (MCDR), which decomposes complex expressions into simplified target-anchor relations and augments missing spatial cues through multi-view reasoning. Finally, we propose LLM-Grounder, which repurposes a detection-pretrained spatial LLM into a language-conditioned grounding model by aligning point cloud and linguistic representations within the pruned region. Extensive experiments on the three most popular point cloud benchmarks demonstrate that our method achieves state-of-the-art results on all three ScanRefer settings and on 9 out of 10 Nr3D/Sr3D settings. Code and models are publicly available: this https URL

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-274](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
