# 📦 其他研究 | 2026年07月22日

> 本类共 **386** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-386](./part-08.md)

---

### 251. [Generative Transmission: Rethinking Computation, Bandwidth, and Memory in Communication](https://arxiv.org/abs/2607.17482)

**<font color=#1a73e8>作者：</font>** Xiangyu Chen, Jixiang Luo, Yuankai Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Under the AI Flow framework, communication is shifting from transmitting fidelity-oriented information flows toward delivering task-oriented and perception-oriented token flows across heterogeneous network resources. Video communication is a fundamental component of modern information networks. However, under ultra-low-bandwidth and weak-network conditions, conventional video coding and transmission methods, which are primarily optimized for pixel-level fidelity, often struggle to balance visual usability, transmission efficiency, and robustness to unstable links. With the rapid advancement of generativemodels, video communication is also moving from precise signal reconstruction toward receiver-side perceptual utility and system-level usability. In this paper, we propose Generative Transmission (GenTrans) for video communication under ultra-low-bandwidth and weak-network conditions. Built upon Generative Video Compression (GVC), GenTrans formulates video transmission as a joint optimization problem involving bandwidth, computation, and memory, rather than treating it merely as a signal coding task. By leveraging generative priors, cross-clip memory reuse, runtime state reuse, and weak-network-aware transport, GenTrans significantly reduces transmission overhead while enabling visually coherent and practically useful reconstruction. Experimental results show that GenTrans supports effective video transmission under ultra-low-bitrate and weak-network conditions, achieving improved transmission efficiency, decoding efficiency, and robustness while preserving perceptual quality.

---


### 252. [ShadowPickle: Evading Machine Learning Model Scanners via Stealthy Pickle Deserialization Attacks](https://arxiv.org/abs/2607.17503)

**<font color=#1a73e8>作者：</font>** Dhruv Pradhan, Sarang Nambiar, Ezekiel Soremekun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model hosting hubs (e.g., Hugging Face) are vulnerable to supply chain attacks that enable remote code execution on trusted user environments. Attackers often distribute malicious Pre-trained ML models (PTMs) via model hubs. In this paper, we present novel attacks against PTMs and model hubs called SHADOWPICKLE. SHADOWPICKLE includes three (3) stealthy pickle deserialization attacks that enable malicious behaviors and evade state-of-the-art (SOTA) model scanners. These attacks leverage the external module import mechanism of the Pickle Virtual Machine (VM) to execute malicious payloads during deserialization. Additionally, we provide PICKLEBENCH, a dynamic and extensible benchmark for automatically injecting SHADOWPICKLE into arbitrary benign PTM models. Our evaluation shows that SHADOWPICKLE evades ten SOTA scanners, and four model hubs. SHADOWPICKLE (Overwritten) has a 63% evasion rate across scanners, and up to 50% higher evasion rates than existing attacks. Besides, PICKLEBENCH is up to 25.6% more challenging than three SOTA benchmarks. Finally, we provide security recommendations for mitigating our attacks and improving the effectiveness of existing scanners. Our findings highlight the limitations of existing PTM scanners and suggest directions for improvements.

---


### 253. [DecoyFace: Beyond Obfuscation via Controllable and Imperceptible Identity Misdirection for Privacy-Preserving Face Recognition](https://arxiv.org/abs/2607.17504)

**<font color=#1a73e8>作者：</font>** Zhihan Ren, Lijun He, Xinyao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Split face recognition reduces client-side computation but exposes intermediate features to feature inversion attacks and unauthorized analysis by honest-but-curious (HBC) servers. Existing privacy-preserving face recognition methods mainly aim to resist unauthorized reconstruction, typically producing features whose inversion yields visibly degraded results, which may reveal the existence of protection and motivate adaptive attacks. To address this issue, we propose DecoyFace, an imperceptible decoy-oriented framework that steers unauthorized reconstruction toward a plausible but incorrect identity while preserving recognition utility. The key idea is to decompose the intermediate representation into a reconstruction-sensitive subspace and its complementary subspace. The client injects decoy identity cues into the reconstruction-sensitive subspace, while limited recognition-relevant evidence from the true sample is retained in the complementary subspace. On the server side, an authorized canonicalization module suppresses decoy-dominant components and recovers a recognition-friendly representation. This design addresses both attacker-side inversion from intercepted features and HBC server-side reconstruction from canonicalized representations. Experiments show that DecoyFace preserves competitive recognition accuracy while substantially reducing identity leakage to 2.93% under U-Net attacks and 0.74% under Flow-Matching attacks while yielding visually plausible and imperceptible reconstructions, with over 99.78% face validity on LFW dataset.

---


### 254. [Retrieval-Augmented Interpretable Learning: Towards Task-Specific Zero-Shot Models in Healthcare](https://arxiv.org/abs/2607.17508)

**<font color=#1a73e8>作者：</font>** Sazan Mahbub, Caleb Ellington, Zhiyuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Retrieval-Augmented Interpretable Learning (RAIL), a probabilistic meta-learning framework for zero-shot generation of task-specific interpretable models that synthesizes coefficient-space structure from natural-language task descriptions and a memory of previously learned task-specific predictors. RAIL retrieves related source tasks, transfers structure through coefficient space, and generates a new predictor in the original diagnostic-feature space, enabling zero-shot and few-shot clinical procedure prediction with feature-level explanations. Its probabilistic formulation provides uncertainty over retrieval, model coefficients, and predictions, supporting reliability-aware deployment: uncertain predictions or unstable explanations can be flagged for additional clinical review rather than treated as automatic decisions. This makes RAIL particularly suited for healthcare settings, where prediction tasks are highly long-tailed, new clinical targets arise frequently, and models must remain inspectable, uncertainty-aware, and compatible with human oversight. Across long-tailed clinical procedure prediction tasks, RAIL maintains reliable performance across data-availability regimes: it achieves 73.4% accuracy in the held-out zero-shot settings, where no supervised task-specific model can be trained, and remains near 73.2% accuracy in the extreme few-shot regime with only 2-4 examples, where supervised task-specific models perform close to chance. RAIL further benefits from clinically informed task representations and yields retrieval, uncertainty, and coefficient-level diagnostics that make model behavior more transparent. These results suggest a path toward scalable clinical prediction systems that can adapt to new tasks while preserving interpretability and reliability.

---


### 255. [After the Euclidean Highway: Hyperbolic Expert AI as the Next Innovation](https://arxiv.org/abs/2607.17513)

**<font color=#1a73e8>作者：</font>** Kwan Soo Shin, In Seok Kang, Munho Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expert domains are trees; the Euclidean transformer is not, diluting parent-child structure exponentially at depth. The hyperbolic turn left one question unasked: not how much of a network to curve, but where curvature may touch the gradient. Placement is a law, not a knob: the same geometry on a trainable adapter collapses training (seventeen training collapses, ~220 GPU-hours), yet at the loss layer alone it trains without one -- this is HySAT (Hyperbolic Structure-Aware Training), hyperbolic losses at the loss layer only. Across six expert SLMs we constructed and deployed (Llama 3.1 and EXAONE 3.5; four adapter strategies; 18.0M-sample corpus; zero NaN over ~317K optimizer steps), a matched four-arm ablation isolates the preserved manifold invariant, and three propositions and a lemma prove why loss-only placement is stable where adapter-on-manifold is not. Four models are operationally deployed (one live, consumer-facing), two open-weight, with per-step traces and a seventeen-incident failure ledger on Zenodo (CC-BY-4.0).

---


### 256. [One-step lowest-variance selection in a Gaussian random-field model motivated by masked diffusion: Total correlation and a square root collision threshold](https://arxiv.org/abs/2607.17522)

**<font color=#1a73e8>作者：</font>** Linjun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motivated by confidence-guided parallel unmasking in masked discrete diffusion, we study a single selection step in a stylized Gaussian random-field model. A locally dependent nonnegative score field represents position wise uncertainty, and the scheduler selects the K positions with the smallest scores. Dependence among the selected positions is measured through a distance-dependent Gaussian correlation model. This separation provides a tractable framework for quantifying how the geometry of low-score locations affects the dependence cost of factorized parallel decoding. We establish two complementary results. In a conservative sub-square-root regime, the conditional Gaussian total correlation of the selected block vanishes in probability. At the square-root scale, it remains non-negligible with positive asymptotic probability and admits a strictly positive expectation lower bound. Synthetic experiments support the predicted finite-size behavior. These results provide a rigorous stochastic-geometry baseline for understanding how budget size, score dependence, and spatial correlation jointly shape one-step confidence-based selection in masked discrete diffusion.

---


### 257. [Thinking in Video: Can Video Generators Really Reason About the Real World?](https://arxiv.org/abs/2607.17523)

**<font color=#1a73e8>作者：</font>** Yongheng Zhang, Guang Yang, Ruihan Hou 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in world models and video generation have given rise to an emerging reasoning paradigm that leverages video generative models to simulate, predict, and reason about real-world dynamics. We redefine this paradigm as Thinking in Video, where video is not merely an output artifact but a medium for constructing, extending, and verifying causal thought. However, this promise remains unverified: convincing rollouts may reflect memorized appearances rather than causal understanding, while existing metrics separate perceptual fidelity from semantic logic. To evaluate whether video generators support such reasoning, we introduce the Causal-Generative Dual-Judge (CGDJ), auditing World Model Consistency from two perspectives. Explicit Causal Perception tests whether a generator reads a video scenario as a reasoning problem through spatio-temporal flattened visual question answering, while Implicit Generative Perception-Prediction Gap evaluates whether it renders the causal consequence as a consistent future video. Applying CGDJ to representative open- and closed-source generators reveals a clear Perception-Prediction Gap: open-source models produce plausible dynamics despite near-zero explicit causal perception, whereas advanced closed-source systems show stronger but still limited alignment between reasoning and generation. Further analysis exposes audio-visual misalignment, where models verbalize correct causal logic more reliably than they render it, challenging the "world simulator" narrative.

---


### 258. [Token-Level Off-Policy Learning for Faithful Generation Under Distribution Shift](https://arxiv.org/abs/2607.17524)

**<font color=#1a73e8>作者：</font>** Zitong Huang, Gustavo Lucas Carvalho, Deqing Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Token-Level Off-Policy Labeling (TOPL), an off-policy training paradigm that reframes post-training as a token-level correctness prediction task. Our key intuition is that by training the model to distinguish good and bad tokens in a response, we naturally guide the model towards generating good tokens, while avoiding the pitfalls that come with directly training the model to generate off-policy tokens. Experiments on document summarization tasks show that TOPL achieves strong out-of-distribution generalization across 11 datasets against a diverse set of sequence-level and token-level baselines. We further demonstrate that TOPL transfers effectively to machine translation, suggesting that its benefits generalize across different faithful generation tasks. Through ablation studies, we confirm that our token-level learning signal is critical to good performance; sequence-level analogues do not confer similar benefits. Finally, we show that TOPL induces interpretable model updates: the LoRA adapters learned through TOPL function as linear classification heads and steering vectors.

---


### 259. [Sidekick: Designing Communication for Effective Multitasking with Computer Use Agents](https://arxiv.org/abs/2607.17527)

**<font color=#1a73e8>作者：</font>** Ruei-Che Chang, Wenqian Xu, Dingzeyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computer Use Agents (CUAs) can autonomously execute complex, multi-step tasks within GUIs, enhancing efficiency through parallel multitasking. However, our formative studies with CUA experts and GenAI users indicated that current feedback is primarily text-based, requiring sustained attention to monitor progress and offering limited visibility to trace past GUI interactions. Based on the findings, we developed a prototype system, Sidekick, for communicating CUAs' status with multimodal feedback across different stages of interaction: (i) When CUAs run in the background, Sidekick signals its execution state through ambient cues. (ii) Upon resuming interaction with CUAs, Sidekick provides multimodal summaries of completed actions to support rapid context resumption. (iii) When CUAs operate in the foreground, Sidekick enhances transparency by verbalizing and visualizing the agent's reasoning. A study with 30 participants demonstrated that Sidekick significantly improved multitasking performance with CUAs compared to baseline systems that presented textual feedback either in a typical chat or in an ambient display. Sidekick supported progress awareness, and error and action traceability more effectively. Finally, we demonstrate the promise of Sidekick through several example applications, and discuss implications for long-horizon human-agent collaboration.

---


### 260. [Oracle Gap and Signal Fidelity: A Fixed-Pool Diagnostic for Test-Time Collaboration](https://arxiv.org/abs/2607.17531)

**<font color=#1a73e8>作者：</font>** Jie Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time collaboration, including self-consistency, best-of-N selection, critic models, and verifier pipelines, is often credited with broadly improving LLM reasoning, yet its gains are uneven and sometimes negative. We ask when training-free collaboration should be expected to help. For a fixed candidate pool, we decompose a selector or verifier's net gain into measurable factors: recoverable mass, verification-signal coverage, conditional selection quality, and harm to already-correct outputs. This reframes collaboration as a candidate-selection problem rather than as an intrinsic property of a multi-agent topology. Across LiveCodeBench, MATH Level-5 hard subjects, and GPQA-Diamond, gains are bounded first by the oracle gap and then by signal fidelity, which we measure directly as candidate-level agreement between verifier verdicts and official labels. On LiveCodeBench, a public-test verifier (MCC 0.825) gains +8.14 percentage points (pp) over a first-sample baseline; a generated-test verifier (MCC 0.248) improves by +2.70pp and is not statistically distinguishable from an LLM selector, but operates at near-zero harm versus the selector's 4.69% harm rate. On MATH, a symbolic answer-equivalence selector beats self-consistency by +4.67pp, while LLM selectors are negative. On GPQA-Diamond, recoverable mass is only 3.03% and 87.54% of candidate pools are answer-identical; a weaker model's pools shrink both further, suggesting that oracle gap is a joint property of task, model, and sampling configuration. Our framework yields a practical pre-deployment diagnostic: estimate the oracle gap, then measure coverage, signal fidelity, and harm before investing in collaboration.

---


### 261. [Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation](https://arxiv.org/abs/2607.17540)

**<font color=#1a73e8>作者：</font>** Siddharth Mishra-Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural simulation-based inference enables parameter estimation for complex models, but typically requires the user to specify a simulator encoding a fixed model structure. We present a framework for joint model selection and parameter estimation that combines large language models for program synthesis with neural simulation-based inference. Given a natural language description of the system and data under investigation, an LLM proposes candidate simulator programs which are iteratively refined via feedback-driven mutation and evaluated using neural density estimation. The approach enables simulation-based inference over a pool of models, not just parameters within a fixed model. On benchmarks spanning deterministic dynamics, stochastic epidemic models, and dark matter substructure inference from gravitational-lensing images, the method identifies plausible model families from open-ended prompts, with accuracy that reflects the information content of the data and identifiability of candidate models.

---


### 262. [The Curvature Shadow: An Apparent Failure of Maximum-Entropy Equilibrium Selection is a Removable Artifact](https://arxiv.org/abs/2607.17543)

**<font color=#1a73e8>作者：</font>** Luis Leal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In two-player zero-sum games whose Nash equilibria form a convex set, regularized solvers such as Regularized Nash Dynamics (R-NaD) empirically select the maximum-entropy member: the information projection (I-projection) of a uniform reference onto the Nash set. On a panel of small games this match is exact, with one apparent exception: in Kuhn poker R-NaD lands at bluff coordinate 0.180 while the maximum-entropy member sits at 0.201, a coordinate gap of about 0.021, even though R-NaD attains 99.7 percent of the maximum entropy. We ask whether this gap is a genuine selection bias or an artifact, and answer it quantitatively. We show that for selection on a one-dimensional Nash manifold the coordinate gap factorizes as $\mathrm{gap} \approx \sqrt{2\delta/\kappa}$, where $\delta$ is the entropy shortfall of the solver and $\kappa$ is the curvature of the entropy landscape at its peak. Across five games this relation holds to within $2 \times 10^{-4}$ (under 1 percent relative error). The four matrix games have $\delta \approx 0$ (R-NaD reaches the maximum-entropy member exactly) and therefore no gap regardless of curvature; only the sequential game (Kuhn) has $\delta > 0$. A causal sweep of the magnet strength drives $\delta \to 0$ and the gap toward zero along the predicted curve (fitted scaling exponent 0.50, $R^2 > 0.999999$, against the exact prediction of 1/2), until the dynamics destabilize at a stability floor: behavior consistent with a removable shortfall and inconsistent with a fixed bias. We quantify the curvature half of the law from measured curvatures and flag a moving-target pitfall in the natural Tsallis-entropy experiment. The Kuhn gap is thus the curvature shadow of a small, removable entropy shortfall on an unusually flat peak; the I-projection account is upheld up to a flatness-limited residual.

---


### 263. [Human-in-the-Loop User Feedback Affects Perceived Accuracy and Trust, but Task Subjectivity Matters](https://arxiv.org/abs/2607.17548)

**<font color=#1a73e8>作者：</font>** Donald R. Honeycutt, Mahsan Nourani, Eric D. Ragan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While ML can produce complex models beyond those that a human could produce manually, incorporating human input can often improve performance beyond purely data-driven models. While this feedback could come from system designers or domain experts, in many cases, the end users who regularly use the system will naturally develop an understanding of its flaws and desire the ability to change the system's behavior based on their knowledge. While soliciting feedback from end users can result in significant model improvement over time, introducing these feedback techniques can also affect several human factors-such as trust or perception of system accuracy-that are not yet fully understood and have different effects reported in the existing literature. Therefore, we sought to build on the existing research to further explore how the act of providing feedback can affect user understanding of an intelligent system and its accuracy in different contexts. We present three controlled experiments that study the effects of interactive feedback collections on user impressions in domains with objective and subjective feedback. The results show that in a context where there is an objectively correct answer, providing HITL feedback lowered both participants' trust in the system and their perception of system accuracy, regardless of whether the system accuracy improved in response to their feedback. However, when the feedback being provided involved subjective opinion, no such negative bias was observed. Furthermore, in the objective context, participants distrusted the system over time, whereas participants in the subjective context mistrusted the system over time. These results highlight the importance of considering the effects of allowing different types of end-user feedback on user trust when designing intelligent systems.

---


### 264. [(A)iSpy: Parasitic Trojans for Machine Learning Infrastructure](https://arxiv.org/abs/2607.17550)

**<font color=#1a73e8>作者：</font>** Habibur Rahaman, Qipan Xu, Zafaryab Haider 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern machine learning (ML) pipelines depend heavily on third party libraries for graph compilation and hardware acceleration. While current practices audit data and model artifacts or rely on file integrity checks, the execution environment remains implicitly trusted. This blind spot enables active threats where a malicious runtime module interacts directly with live training and inference dynamics: exploiting this interaction allows the Trojan to support complex objectives that are challenging for static code or binary modifications, achieving manipulations impossible for standard data and model level attacks. We expose this vulnerability by presenting (A)iSpy, a parasitic infrastructure Trojan that subverts ML systems through an active observe and execute paradigm. Operating within the computation graph, (A)iSpy monitors transient tensor states to perform targeted, stealthy manipulations with negligible overhead. To violate confidentiality, the Trojan identifies all critical training hyperparameters and covertly exfiltrates them via model weights or output logits. To break integrity, it acts as a gradient amplifier: by observing steganographic triggers, it transforms otherwise weak data poisoning into effective backdoor attacks, increasing success rates from near zero to 100%. We further demonstrate broad extensibility across the machine learning lifecycle by validating auxiliary attacks in the appendix, including subpopulation label flipping, availability disruptions, and inference stage manipulations. Importantly, the (A)iSpy module easily evades standard malware scanners, while the associated poisoned inputs and resulting compromised models bypass typical inspection tools. We demonstrate the practicality of this threat with an implementation in the ONNX Runtime training and inference engines.

---


### 265. [Hierarchy-Aware and Anatomy-Guided Learning for Lung Ultrasound Video Classification](https://arxiv.org/abs/2607.17551)

**<font color=#1a73e8>作者：</font>** Alya Almsouti, Lotfi Mecharbat, Noha Aboukhater 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung ultrasound (LUS) is a bedside tool for assessing pulmonary edema in patients at risk due to heart failure or impaired kidney function. However, automated LUS analysis remains challenging because of speckle noise, imaging artifacts, and operator-dependent acquisition variability. In this work, we present a deep learning framework for multi-class LUS video classification that explores two components: hierarchy-aware training, and anatomy-guided learning. Starting from a strong baseline, we introduce hierarchical training strategies and then introduce pleural line mask supervision to guide model attention toward anatomically relevant regions. We study four clinically relevant classes--healthy, B-lines, consolidations, and mixed B-lines with consolidations--using an open-access dataset of 1,886 videos from 219 patients, evaluated with patient-level five-fold cross-validation. Results show that hierarchy-aware training improves pathological separation relative to flat classification, while mask-guided attention supervision achieves the highest mean macro-F1 of 65.7\% and produces more localized attention patterns. Transfer experiments on the external COVID-BLUeS dataset further show competitive and parameter-efficient adaptation while preserving pleural-focused attention behavior. These findings suggest that combining clinically structured objectives with anatomy-guided supervision is a practical approach to robust, interpretable LUS video analysis. Code and model implementations are available at this https URL.

---


### 266. [Volatility-Aware Extreme Event Detection in High-Frequency Financial Markets](https://arxiv.org/abs/2607.17555)

**<font color=#1a73e8>作者：</font>** Maorufa Zaman, Haris Md Sahed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting extreme price movements in high-frequency financial markets is a challenging task due to non-stationarity, heavy-tailed return distributions, and severe class imbalance. In particular, rare but impactful events are often difficult to detect using conventional modeling approaches, which typically treat extreme movements as isolated observations. This study proposes a volatility-aware approach for extreme event detection using high-frequency Bitcoin limit order book (LOB) data. Motivated by empirical evidence of volatility clustering, the target formulation is extended to incorporate both large future returns and high-volatility regimes. This redefinition increases the proportion of informative samples and aligns the learning objective with the underlying market dynamics. Using a tree-based model (XGBoost) with time-series cross-validation and imbalance-aware evaluation, the proposed method achieves a Precision-Recall AUC of approximately 0.40, significantly outperforming the baseline formulation with a PR-AUC of around 0.06. This represents more than a sixfold improvement in detecting rare events. The results highlight that target design plays a critical role in financial machine learning, often exceeding the impact of model complexity. By incorporating volatility structure into the labeling process, the proposed approach provides a more effective and realistic framework for extreme event detection in high-frequency cryptocurrency markets.

---


### 267. [FlexiGrad: Adaptive Gradient Modulation for Hierarchical Fine-Grained Classification](https://arxiv.org/abs/2607.17563)

**<font color=#1a73e8>作者：</font>** Zilu Zhou, Dongliang Chang, Junhan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many fine-grained recognition tasks contain hierarchical labels such as order, family and species. Although this supervision should be beneficial, jointly optimising all levels often leads to unstable training because coarse and fine classifiers impose inconsistent gradients on the shared backbone. This hierarchical gradient conflict prevents the model from learning a coherent coarse-to-fine representation. In this paper, we propose FlexiGrad, a simple and parameter-free method that regulates gradient interactions during backpropagation. FlexiGrad removes only the harmful conflicting component when tasks disagree and reinforces the shared direction when they partially agree through a smooth hierarchy-aware weighting function. This produces stable optimisation and preserves both global structure and fine-grained discriminative cues. FlexiGrad integrates into existing architectures without modification while improves multi-granularity accuracy on CUB-200-2011, FGVC-Aircraft and Stanford Cars. The code will be available at PRIS-CV/FlexiGrad.

---


### 268. [ZifaMem: Structured Memory for Persona, Preference, and Emotional Continuity in AI Companions](https://arxiv.org/abs/2607.17564)

**<font color=#1a73e8>作者：</font>** Jingzhe Fang, Guozhi Xu, Yunfan Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI companions are judged not only by single-turn fluency but by whether they sustain emotional continuity: remembering who the companion is, what the user prefers, and how the relationship has felt. We present ZifaMem, a structured memory system that organizes dialogue into session summaries, episodic memories, and a consolidated user model. Against a deployment-honest comparator that supplies the full raw dialogue history, and under a fixed LLM-as-a-judge protocol with route audits, structured memory raises pooled four-backbone emotional-intelligence scores by 11.4% (95% CI 6.3% to 17.1%), and persona grounding improves on all four backbones (Claude +42% relative). Multi-turn affect context wins a +39% net preference over a single-turn snapshot (exploratory), whereas an additional emotion state machine yields no measurable gain on any of five endpoints. Under an identical preregistered protocol, three memory systems (ZifaMem, Mem0, and filtered verbatim retrieval) each improve significantly over raw-history deployment, and ZifaMem and Mem0 are statistically equivalent within +/-5 points on the preregistered primary preference endpoint. The ZifaMem SDK, CLI, and portable Agent Skills are open-sourced at this https URL.

---


### 269. [A Weisfeiler-Leman Characterization of Global-Attention Graph Transformers for Mixed-Integer Linear Programs](https://arxiv.org/abs/2607.17570)

**<font color=#1a73e8>作者：</font>** Md Abrar Jahin, Craig A. Knoblock, Jay Pujara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph foundation models (GFMs) with global attention are increasingly used to represent mixed-integer linear programs (MILPs), aiming to capture structure beyond the locality of standard graph neural networks. We study their expressive power through graph isomorphism testing, asking which MILP instances they map to identical representations. We prove that a broad class of hierarchical graph transformers combining global linear attention, edge-weighted cross-attention, and bipartite message passing is bounded by the one-dimensional Weisfeiler-Leman (1-WL) test: under any parameter setting, 1-WL-equivalent MILP graphs receive identical graph embeddings. Our compositional proof shows that each architectural component is a symmetric multiset function and thus preserves 1-WL equivalence. We validate this characterization across ten diverse graph encoders, including Graphormer-, GraphGPS-, Set-Transformer-, and Gasse-style models. Across model capacities, graph scales, and pooling operators, every tested encoder maps 1-WL-equivalent non-isomorphic graph pairs to numerically identical embeddings. Consequently, graph invariants that vary within a 1-WL equivalence class cannot be recovered from these representations. We further show that expressiveness beyond 1-WL arises from input encoding rather than attention: random-walk positional encodings separate the constructed pairs, while additional constructions expose the limits of this remedy. These results characterize the expressive power of global-attention GFMs and provide an encoder-agnostic diagnostic for detecting 1-WL-induced representation equivalence.

---


### 270. [AGG: Jacobian-Aggregated Group Gradient for Efficient GRPO Training of Diffusion Models](https://arxiv.org/abs/2607.17572)

**<font color=#1a73e8>作者：</font>** Ruiyi Ding, Jie Li, He Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) is a powerful reinforcement learning algorithm for aligning generative models with human preferences. While successful in large language models~\cite{shao2024deepseekmathpushinglimitsmathematical}, its extension to diffusion and flow matching models introduces a severe computational bottleneck: gradients must be back-propagated through the high-capacity DiT backbone at \emph{every} timestep of the sampling trajectory, making high-resolution text-to-image (T2I) training prohibitively expensive. Training-free DiT inference acceleration methods (e.g., $\Delta$-DiT, ScalingCache) exploit the fact that DiT hidden states and velocity predictions vary \emph{smoothly and nearly linearly} along the trajectory. We ask whether the same linearity can reduce the backward-pass cost of DiT RL training, and answer affirmatively with \textbf{JAGG} (\textbf{J}acobian-\textbf{A}ggregated \textbf{G}roup \textbf{G}radient), which reduces full transformer backward passes from $W$ to $2$ per group of $W$ consecutive steps. JAGG approximates intermediate-step Jacobians via $t$-weighted interpolation of the endpoint Jacobians, then aggregates per-step upstream signals into two composite gradients applied through a single joint backward pass. We prove this interpolation is \emph{exact} when the velocity is linear in $(z,t)$, and a cosine-similarity routing rule (\texttt{jagg\_frac}) deploys JAGG only where the assumption holds. Experiments on T2I benchmarks show JAGG delivers $\sim$2$\times$ backward speedup with negligible quality degradation.

---


### 271. [Quantum-Resilient Banking Transaction Security using DW-HKEM: A Hybrid RSA/ML-KEM Cryptographic Gateway with Real-Time](https://arxiv.org/abs/2607.17573)

**<font color=#1a73e8>作者：</font>** Siddhaarth S Prabhu, Aswani Kumar Cherukuri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing number of online banking and financial services on public-facing networks has caused security of cryptographic protocols to become a serious, systemic problem. RSA-2048 is the key length that is used in the majority of transactions that travel over the Internet every day. A very insidious threat vector, the Harvest Now, Decrypt Later (HNDL) paradigm, is already in existence with the adversarial nation-state actors and well-funded threat actors. The exposure window is not a time in the future it is the NOW moment! Quantum computation is a certain threat to the current public-key cryptographic infrastructure, and one that is moving ever closer. In this paper, the authors take up both of these challenges, designing, implementing and testing an integrated system based on a Dual-Wrap Hybrid Key Encapsulation Mechanism (DW-HKEM) and a live cryptographic analytics dashboard. Both the RSA-256 and ML-KEM-768 are hosted within the DW-HKEM framework and an AES-256 session key is wrapped in each of them, with a composite key created using a Key Derivation Function based on SHA-256, resulting in combinatorial security against classical and quantum adversaries and backwards compatibility with existing banking systems. The CryptoX real-time dashboard offers time tracking for each operation, session-level analytics and visualization of performance trends for immediate use in enterprise banking security operations. The results from empirical benchmarking across 100 independent iterations show a total overhead of about 1.58ms, which is well within the enterprise deployment threshold, proving the architecture viable as a practical, scalable reference for the financial-sector's cryptographic infrastructure and applications to move to a post-quantum era. We also provide complete source code of the work carried out.

---


### 272. [Scalable Model-Assisted Multi-Target Estimation in Large Image Collections](https://arxiv.org/abs/2607.17581)

**<font color=#1a73e8>作者：</font>** Max Hamilton, Jinlin Lai, Daniel Sheldon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer vision models are increasingly used as measurement tools to estimate population-level quantities from large image collections, but prediction errors introduce bias and the resulting estimates lack statistical guarantees required in scientific applications. Prior work uses a Monte Carlo framework to combine model predictions with ground-truth annotations by sampling some images for humans to label and is able to provide unbiased estimates with controllable accuracy, but primarily addresses single-scalar estimation. We study the more general problem of multi-target estimation, where many quantities (e.g., class counts or proportions) must be estimated simultaneously, and adapt sampling and estimation strategies from survey sampling to this setting. Evaluations on five detection and segmentation datasets with 7-80 classes show that importance sampling excels with moderate annotation budgets or fewer targets, whereas uniform sampling with control variates is superior when estimating many targets or operating with minimal labels. Additionally, a subset-based ratio estimator remains highly competitive across all regimes. Ultimately, our framework effectively combines biased model predictions and limited human labels into rigorous scientific measurements.

---


### 273. [ANNLib: A Development Framework for Efficient Approximate Nearest Neighbor Search](https://arxiv.org/abs/2607.17582)

**<font color=#1a73e8>作者：</font>** Zheqi Shen, Jingbo Su, Zijin Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Approximate Nearest Neighbor Search (ANNS) plays a pivotal role in modern deep learning pipelines. Recently, many ANNS systems have been proposed to either provide broad functionality or reach high performance. However, it is yet difficult to achieve both with minimal programming efforts. We propose ANNLib to address the gap. ANNLib is a library that provides a programming framework for achieving high performance and flexible functionality in ANNS systems, based on popular graph-based ANNS algorithms. We carefully decouple and independently optimize both the algorithm and the data structure components of an ANNS system. In addition, we integrate state-of-the-art algorithms and data structures into ANNLib as modules, along with our new designs. Users can choose combinations of components to implement sophisticated settings with high performance, such as filter search, fully dynamic updates, and historical queries on snapshots. Our experiments show that our new solution provides a simple interface for various applications and achieves comparable or even better performance than previous work, specifically for each application.

---


### 274. [Pixel-Space Diffusion Transformers](https://arxiv.org/abs/2607.17585)

**<font color=#1a73e8>作者：</font>** Renye Yan, Jikang Cheng, You Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models (LDMs) enable efficient high-resolution image synthesis by denoising in a VAE-compressed latent space. However, fixed visual tokenizers can discard fine textures and structural details, while separate representation and diffusion training creates a mismatch between reconstruction and generation objectives. These limitations have renewed interest in pixel-space diffusion, which models raw pixels directly, removes the VAE bottleneck, and supports end-to-end optimization. This formulation better matches the demands of high-fidelity generation but introduces challenges in high-dimensional modeling, including noise scheduling, loss weighting, token efficiency, and scalable architecture design. Pixel-space modeling also offers a promising basis for unified multimodal systems: raw pixels, text, and task conditions can be represented in a shared token space and jointly processed by a single Transformer, narrowing the gap between visual understanding and generation. This paper reviews Pixel-Space Diffusion Transformers (pDiTs) from the perspectives of model architecture, continuous generative mechanisms, and unified multimodal modeling. We summarize representative methods, identify key technical challenges, and discuss future directions toward high-fidelity, end-to-end vision foundation models that integrate generation and understanding.

---


### 275. [Miles: Metric Learning with Expandable Subspace for Pre-Trained Model-Based Class-Incremental Learning](https://arxiv.org/abs/2607.17593)

**<font color=#1a73e8>作者：</font>** Kai Jiang, Zisong Lin, Hongyuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class Incremental Learning (CIL) aims to learn new concepts consistently from a data stream without forgetting. Unlike typical CIL methods which need to learn a model from scratch, pre-trained model (PTM) can easily adapt to a new task with fine-tuning. However, existing PTM-based CIL methods fail to achieve a trade-off between performance and computational expenditure, i.e., they either adopt the same parameter space so that leading catastrophic forgetting, or expand a new branch for each task but adding more computational cost. To this end, we propose MetrIc Learning with Expandable Subspace (Miles) to harness the prior information within pre-trained knowledge, thereby orchestrating an efficient expansion of the parameter space through guided optimization. Specifically, it decouples the learnable modules with the pre-trained model, exploiting prior information from intermediate features of the backbone network to enable more flexible parameter expansion. Then, a central loss is adopted to guide the new category to cluster towards the corresponding prototype in the new task subspace while incorporating an auxiliary distance regularization term to maintain metric equilibrium across tasks. Extensive experiments on six benchmark datasets demonstrate that Miles achieves state-of-the-art performance in various CIL settings.

---


### 276. [Concentration and Mean-Square Bounds for Contractive Stochastic Approximation: A Unified Elementary Approach](https://arxiv.org/abs/2607.17595)

**<font color=#1a73e8>作者：</font>** Siddharth Chandak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish mean-square and concentration bounds for stochastic approximation (SA) with arbitrary norm contractive mappings, under a multiplicative noise model where the noise may scale affinely with the norm of the iterates, and the iterates are potentially unbounded. These settings arise in reinforcement learning, where operators are often contractive in the $\ell_\infty$ norm and the noise scales with the iterates. To address the arbitrary norm, earlier works replace the non-smooth squared norm with a smooth Lyapunov function constructed via the generalized Moreau envelope. For concentration analysis, these works handle multiplicative noise and unbounded iterates through a multi-stage bootstrapping argument that starts from a time-varying worst-case bound and iteratively refines it. We instead present a unified and elementary analysis that yields both bounds. Using an averaged noise sequence and corresponding auxiliary iterates, we obtain a one-step Lyapunov drift inequality for the normed error directly, without smoothing the norm or constructing an envelope. For the mean-square bound, we combine this drift inequality with an induction argument showing that the iterates remain bounded in expectation. For the concentration bound, we develop a probabilistic induction over a sequence of "good" events on which the iterates are controlled, allowing the standard Azuma-Hoeffding bound to be applied. Our approach yields the first sub-Gaussian tailed maximal (all-time) concentration bound for SA under multiplicative noise, by allowing the stepsize to depend logarithmically on the confidence level. Beyond the specific setting considered here, we discuss the generalizability of these proof techniques to other noise models and iterative algorithms.

---


### 277. [Is Progressive Disclosure All You Need for Long-Context Agents?](https://arxiv.org/abs/2607.17598)

**<font color=#1a73e8>作者：</font>** Yifeng He, Yinzhe Zhao, Jicheng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-document question answering usually forces a choice between loading the whole document into the context window and bolting on a separate retriever. Agentic AI suggests a broader option, giving the agent the document path and letting it decide how and what to read. Agent Skills, a standard for packaging expertise into folders an agent loads on demand, supply a ready mechanism: progressive disclosure, which exposes only what a query needs, from a short description down to the specific passages. Practitioners rapidly adopted this pattern for book-length understanding tasks, but the evidence to support such choices has been anecdotal. We run the first controlled study of the pattern, comparing raw-document navigation and several designs of Agent Skills packs against a classical hybrid retriever across three agent harnesses and three model families on InfiniteBench. On a single book, the gain depends on the harness, running large when the agent navigates the raw document poorly but near zero when a strong agent harness already divides and retrieves on its own. When scaling up to tasks that span many books, raw-document navigation collapses while one-level progressive disclosure degrades more slowly and pulls ahead. A second, deeper routing level never helps and sometimes breaks accuracy outright, so one level is enough. Progressive disclosure buys context, not intelligence: it is redundant while a strong agent can locate the right passages itself, and decisive once the corpus grows too large to navigate by reading.

---


### 278. [Trustworthy Protein-Ligand Binding Affinity Prediction via Reliability-Aware Multi-Engine Fusion](https://arxiv.org/abs/2607.17601)

**<font color=#1a73e8>作者：</font>** Yongchan Hong, Defu Cao, Wenjin Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate protein-ligand binding affinity prediction is central to computational drug discovery, yet modern docking engines frequently disagree without indicating which prediction to trust. Consensus scoring and ensemble methods improve mean accuracy but treat all predictions identically without interpretable confidence measures or uncertainty decomposition, ignoring the chemical context of each protein-ligand pair. To address this limitation, we introduce RELIABLE-BA (RELIABiLity-aware Evidential fusion for Binding Affinity), an evidential framework for multi-engine binding affinity prediction. Our model comprises three steps: (1) modeling each engine as an evidential expert via Normal-Inverse-Gamma distributions, (2) scaling epistemic uncertainty through learned reliability from molecular context while preserving each expert's predictive mean, and (3) fusing experts through closed-form aggregation that captures both individual uncertainty and inter-engine disagreement. Experiments on the PDBBind and BDB2020+ benchmarks demonstrate competitive point prediction with substantially improved uncertainty calibration, and additional validation on the SARS-CoV-2 Mpro dataset and 5HT2A receptor demonstrates applicability to clinically relevant drug targets. Crucially, these uncertainty estimates enable reliable filtering of protein-ligand pairs, reducing prediction error by up to 25% when retaining only high-confidence pairs. To our knowledge, RELIABLE-BA is the first multi-engine binding affinity prediction framework to combine evidential fusion with context-dependent reliability, offering a principled path toward trustworthy AI-guided drug discovery. Our code is publicly available at this https URL.

---


### 279. [Protecting Floating-Point Computation for DNN Binaries with MBA Obfuscation](https://arxiv.org/abs/2607.17603)

**<font color=#1a73e8>作者：</font>** Yikun Hu, Zichen Zhao, Peixiang Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) have become a foundational component of modern computing systems with a wide range of applications, such as computer vision, edge intelligence, etc. For the sake of low latency and data privacy, DNN models are increasingly compiled into executables and deployed on local devices. However, that exposes the models to model theft, enabling adversaries to recover proprietary assets via reverse engineering techniques. While code obfuscation naturally emerges for protecting executables from reverse engineering, existing schemes are primarily designed for traditional programs, focusing on complex control flow structures and integer-based operations. They are fundamentally inappropriate for DNN binaries, which exhibit relatively simple code structures and heavily rely on floating-point computation.
In this paper, we propose FLOB, an obfuscation framework that protects floating-point computations in DNN binaries using Mixed Boolean-Arithmetic (MBA) transformations. Our approach lifts floating-point values into a higher-precision binary expansion space and performs MBA transformations at the representation level. The computation is carried out entirely in the lifted space, and the final result is then projected back to the target precision, yielding outputs that are semantically equivalent under the original floating-point format, without introducing additional rounding error. The experimental results show that FLOB outperforms the state-of-the-art obfuscation schemes against existing reverse engineering analyzers and deobfuscators, while preserving computational correctness without introducing additional numerical error, allowing flexible trade-off between protection and performance. Specifically, FLOB reduces the operator recovery rate to 4.51% on average, achieving a 32.82 percentage-point reduction compared to existing methods.

---


### 280. [Optimizing the Preconditioner: A Black-box Online-to-Nonconvex Conversion with Static Regret Minimization Oracles](https://arxiv.org/abs/2607.17607)

**<font color=#1a73e8>作者：</font>** Haichen Hu, David Simchi-Levi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether stochastic nonconvex optimization can be reduced to ordinary static regret minimization in online convex optimization in a black-box manner. For smooth nonconvex objectives, our reduction maintains a predictable gradient tracker, while a black-box online learner selects a preconditioner that determines how this tracker is transformed into the update direction. The learner receives linear convex losses and is evaluated against a single fixed comparator over one undiscounted online game. For a $\beta$-smooth objective with range bounded by $M$ and an unbiased stochastic-gradient oracle with variance bounded by \(\sigma^2\), we establish $$\frac{1}{T}\sum_{t=1}^T
\mathbb E\!\left[\|\nabla f(x_t)\|_2^2\right]
\lesssim
\frac{\sigma\sqrt{M\beta}}{\sqrt T}
+
\frac{\sqrt{M\beta}\,
\mathscr R_T(\mathcal A,I_d)}{T}
+
\frac{M\beta}{T}.$$ Consequently, any black-box OCO algorithm with $\mathscr R_T(\mathcal A,I_d)=O(\sqrt T)$ recovers the classical $O(\frac{1}{\sqrt{T}})$ convergence rate.
We further show that the same black-box framework extends beyond the smooth setting to Lipschitz nonconvex objectives without Lipschitz continuous gradients. Importantly, this extension continues to rely only on an ordinary static-regret guarantee and requires no stronger notion of online regret. When the OCO oracle admits square-root static regret, the resulting conversion achieves the optimal $O(T^{-2/7})$ convergence rate for the corresponding Goldstein stationary point. These results resolve the open problem posed by Chen and Hazan (2024). More broadly, our framework separates optimizer design into gradient prediction and online preconditioner selection, providing a principled perspective on how adaptive optimization methods such as AdaGrad and Shampoo may be understood through static regret and applied in nonconvex optimization.

---


### 281. [Semantic Color Naturalness Breaker: Preventing Illegitimate Colorization via Content-Aware Color Priors](https://arxiv.org/abs/2607.17610)

**<font color=#1a73e8>作者：</font>** Yuki Nii, Futa Waseda, Ching-Chun Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic image colorization enables large-scale and low-cost reuse of grayscale media (e.g., manga panels and archival photographs), facilitating unauthorized reuse and redistribution. Once released online, grayscale content can be readily turned into unauthorized colorized derivatives using off-the-shelf models, creating a practical need for proactive, content-side protection at publication time. Building on Uncolorable Examples (UE), which add imperceptible perturbations to released grayscale images to degrade unauthorized colorization, we propose Semantic Color Naturalness Breaker (SCNB) -- a semantic-level UE framework that drives colorization outputs toward content-inconsistent colors while preserving the visual fidelity of the released grayscale media. We further introduce Content-aware Color Distributional Distance (CaCDD), a ground-truth-free, content-aware measure of color plausibility derived from semantic color priors, used both as the optimization objective of SCNB and as an evaluation metric. Experiments on ImageNet show that our method remains effective under small perturbation budgets and common post-processing, supporting practical deployment in real-world content-sharing pipelines.

---


### 282. [Coarse-to-fine Framework for Generative MEF via Implicit Neural Representation](https://arxiv.org/abs/2607.17611)

**<font color=#1a73e8>作者：</font>** Sangmin Han, Jinho Kim, Jinwoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-exposure fusion (MEF) expands the luminance range beyond what a single exposure can capture. Combining images taken at different exposure levels requires handling geometric differences while naturally merging their complementary brightness information. It often demands generative completion where details are missing. Diffusion-based generative methods address these challenges, however, they are computationally expensive and struggle to preserve fine structures in saturated regions. We propose LIIFusion, a coarse-to-fine framework that balances fusion quality and efficiency in generative MEF. The coarse stage performs low resolution generative fusion, enhanced by an adaptive exposure correction that recovers structure lost in saturated over-exposed areas. The fine stage adapts a local implicit image function into a multi-exposure fusion function: conditioned on the HR OE/UE sources and the coarse output, it queries arbitrary target coordinates and fuses source evidence regardless of the HR input resolution. LIIFusion achieves up to 3.5$\times$ speed-up over existing generative methods while maintaining or improving structural fidelity and perceptual quality. We believe this framework provides an effective pathway toward making generative MEF more practical in real-world applications.

---


### 283. [Rarity-Aware Discrete Diffusion with Spatially Consistent Decoding for Photo-Realistic Image Super-Resolution](https://arxiv.org/abs/2607.17612)

**<font color=#1a73e8>作者：</font>** Ao Li, Yapeng Du, Yi Xin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion models have become the dominant paradigm for photo-realistic image Super-Resolution (SR), but they typically formulate reconstruction as continuous signal-level denoising and incorporate semantic priors through external conditioning modules. This makes it less direct to exploit the unified token-based scaling paradigm of modern multimodal models. Autoregressive models provide a more native semantic representation by modeling images as discrete visual tokens, yet their causal decoding is inefficient for high-resolution reconstruction. Discrete diffusion offers a promising middle ground by enabling non-causal, parallel prediction over visual tokens. However, directly adapting discrete diffusion to SR remains non-trivial due to two task-specific challenges: (1) the long-tailed distribution of visual tokens, which under-represents rare but perceptually critical textures; and (2) spatially inconsistent parallel decoding, which may introduce isolated artifacts. To address these issues, we propose DiMOO-SR, a rarity-aware multimodal discrete diffusion framework for photo-realistic image SR. During training, Inverse Frequency Sampling (IFS) prioritizes under-represented but information-rich tokens. During inference, Spatial Consistency Ranking (SCR) refines token confidence using local neighborhood agreement to improve structural coherence. Extensive experiments on widely used real-world SR benchmarks demonstrate that DiMOO-SR achieves competitive perceptual quality with only a few parallel decoding steps, highlighting the potential of discrete diffusion for generative image super-resolution. The code will be released upon publication.

---


### 284. [PoLoRA: A Preconditioned Orthogonalized LoRA Optimizer](https://arxiv.org/abs/2607.17620)

**<font color=#1a73e8>作者：</font>** Nikhil Ghosh, Tetiana Parshakova, Robert M. Gower  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) makes finetuning large language models cheaper by adding to each weight matrix a trainable low-rank update parameterized as the product of two matrices. These matrices are usually trained with Adam, which treats them as a single flat vector of parameters and ignores both the matrix and product structure of LoRA. Applying a matrix-aware optimizer such as Muon to each factor does not consistently improve over Adam, and neither do the product-aware Muon variants proposed in concurrent works. To realize consistent gains, we introduce PoLoRA, a Preconditioned Orthogonalized LoRA optimizer built from three ingredients: a product-aware spectral update direction, curvature preconditioning derived from controlling the per-sample loss change, and a magnitude rule that controls the sizes of both the factor and merged updates. We evaluate PoLoRA on instruction-tuning datasets for code and math across models from 1B to 8B parameters, and find that it reaches the final held-out loss achieved by tuned Adam in 1.2-1.7 times fewer steps, while adding at most 3% per-step overhead. Compared to Adam, PoLoRA is also less sensitive to the learning rate, and its optimal learning rate is stable across ranks.

---


### 285. [Mechanistic Attention Guidance for Agent Memory Refinement](https://arxiv.org/abs/2607.17621)

**<font color=#1a73e8>作者：</font>** Yechao Hong, Haiquan Qiu, Yaqing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing self-evolving memory systems mainly improve agent memory based on textual outputs, such as task trajectories and reflections. However, this text-based paradigm rarely incorporates internal mechanistic signals, leaving how retrieved memory is actually utilized during task execution underexplored. This limitation can lead to unreliable error attribution and hallucinated memory modifications. In this work, we show that retrieval-head attention provides a mechanistic signal for revealing segment-level memory utilization. By aggregating attention over memory segments and decision steps, we construct a context utilization matrix that exposes recurring memory-use patterns and indicates corresponding refinement strategies. Building on this observation, we propose Attention-Guided Memory Refinement (AGMR), a framework that uses utilization patterns revealed by attention to guide targeted segment-level memory updates. AGMR corrects or enhances memory for failed executions, simplifies memory for successful executions, and verifies each update through re-execution. Experiments on interactive decision-making benchmarks show that AGMR improves both task performance and memory efficiency over text-only memory refinement baselines. Code is available at this https URL

---


### 286. [Can Transformers Really Do It All? On the Compatibility of Inductive Biases Across Tasks](https://arxiv.org/abs/2607.17624)

**<font color=#1a73e8>作者：</font>** Damien Teney, Liangze Jiang, Hemanth Saratchandran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are remarkably versatile and their design is largely consistent across a variety of applications. But are they optimal for any given task or dataset? The answer may be key for pushing AI beyond merely scaling current designs.
*Method.* We present a method to optimize a transformer architecture for a given dataset, which we use as a tool to study optimal task-specific inductive biases. This method replaces the most important non-linearities (GeLUs,;softmax) with functions learned on held-out data. We then train the resulting architectures on other datasets, as a way to evaluate the compatibility between pairs of tasks.
Findings. On algorithmic toy tasks, we identify new architectures with dramatic improvements in learning speed, in- and out-of-distribution generalization, and stability across seeds. The new designs prove very task-specific however, and indicate that these tasks require inductive biases very different from those of standard transformers. On code and language modeling datasets, we also find architectures with consistent, yet smaller improvements. These designs transfer much better across datasets and domains (English & computer code).
Implications. Our results show that standard transformers are rarely a local optimum in the space of architectures. Simple alternatives can perform much better but sacrifice universality. This suggests that there may be room for improved architectures that better support multiple capabilities simultaneously, such as fluency and robust reasoning.

---


### 287. [Brain-Aligned Multi-Stream Video Transformers with Sparse Self-Selection](https://arxiv.org/abs/2607.17625)

**<font color=#1a73e8>作者：</font>** Amir Hosein Fadaei, Mahyar Maleki, Mohammad-Reza A. Dehaqani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video transformers typically ignore principles from primate vision and are rarely evaluated against neural data, limiting their biological interpretability. We introduce a sparse winner-takes-all token selection module that replaces dense self-attention to improve efficiency and approximate competitive routing observed in biological visual circuits. We further propose a neuro-inspired split-and-fuse video transformer which uses two complementary pathways: a high-resolution, low-frame-rate "what" stream and a low-resolution, high-frame-rate "where" stream, fused before classification. On Kinetics-400 and Something-Something V2, our best variant operates on the Pareto frontier of accuracy versus inference time among models of comparable scale and pretraining, and showing improved robustness to spatial perturbations. Using representational similarity analysis between model embeddings and time-resolved EEG recordings for the same video stimuli, our model attains a peak brain-model correlation of 0.18 (about 78% of the noise ceiling) and consistently outperforms strong video transformer baselines, suggesting that pathway specialization and sparse competition are useful inductive biases for efficient, brain-aligned video understanding.

---


### 288. [It Matters How You Say It: Exploring Rhetorical Patterns for AI-Assisted Information Evaluation](https://arxiv.org/abs/2607.17627)

**<font color=#1a73e8>作者：</font>** Sadra Sabouri, Zeinabsadat Saghi, Jordan Lee Boyd-Graber 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prior work on AI-assisted information evaluation has largely focused on what AI systems communicate, comparing explanation types and formats, with responses predominantly cast in directive rhetoric where the system delivers a verdict and the user passively accepts it. While debate-style interactions have recently shown promise in prompting critical evaluation over deference, the rhetorical patterns that structure AI responses and how they might induce reflection, uncertainty, or independent reasoning remain largely unexamined. To address this, we investigated eight rhetorical patterns known to induce contemplation: Intentional Misleading, Interpretive Alternative, Scaffold Explanation, Triggering Distrust, Information Distortion, Alternative Framing, Socratic Questioning, and an Oracle baseline. Through a within-subject study with n=98 participants on a hint-on-demand fact verification task, we observed preliminary evidence that Scaffold Explanation were associated with the highest accuracy gains, and encouraging deeper reflection. Surprisingly, the adversarial conditions also improved accuracy modestly. Participants preferred Alternative Framing most and Interpretive Alternative least, largely due to the latter's perceived time cost. We discuss the implications of designing conversational agents with varied rhetorical styles and the trade-offs among user performance, satisfaction, and contemplation.

---


### 289. [TypiCore: A Hybrid Active Query Strategy for Class-Incremental Learning on Time Series](https://arxiv.org/abs/2607.17632)

**<font color=#1a73e8>作者：</font>** Gabor Szucs, Samuel Jacsev, Marcell Nemeth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series data play a pivotal role across numerous domains, including healthcare and manufacturing. In real-world environments, models must cope with distribution shifts over time, a challenge commonly addressed through Continual Learning (CL) techniques. However, existing CL methods face a critical limitation: real-world data streams are rarely fully labeled, making annotation cost a major practical constraint. This paper investigates Active Class-Incremental Learning (ACIL) for multivariate time series, where a model must sequentially learn new classes while selectively querying labels under a fixed annotation budget. We present a systematic evaluation of a wide range of query strategies combined with multiple rehearsal-based approaches, assessing their impact on plasticity, stability, and label efficiency across four benchmark datasets. Our analysis reveals the limitations of uncertainty-based and distribution-aware methods in achieving strong performance under constrained labeling budgets. To address these shortcomings, we propose TypiCore, a novel hybrid query strategy that alternates between typicality-based and diversity-based sample selection across active learning cycles, enabling the construction of memory buffers that are both representative and diverse. Evaluated on the TSCIL benchmark, TypiCore delivers statistically significant improvements over all baselines and matches or surpasses fully supervised continual learning performance on multiple datasets while requiring a fraction of the available labels.

---


### 290. [MixDiffusion: Mixing Diffusion-based Uni-condition Text-to-Image Generation Models for Multi-condition Image Synthesis](https://arxiv.org/abs/2607.17634)

**<font color=#1a73e8>作者：</font>** Pengcheng Wan, Liang Han, Lin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-image (T2I) generation have enabled controllable image synthesis by incorporating conditions beyond text. However, most existing diffusion-based methods are limited to a single type of control condition (e.g., bounding boxes or keypoints), which restricts their flexibility. To address this limitation, we propose MixDiffusion, a training-free diffusion framework for multi-condition T2I generation. MixDiffusion theoretically supports an arbitrary number of control conditions, including bounding boxes, keypoints, sketches, depth maps, reference images, and text, by collaboratively integrating multiple pre-trained uni-condition diffusion models. The key insight of the proposed approach is to derive the predicted noise distribution in each denoising step of the diffusion-based multi-condition image generation model from the predicted noise distributions of multiple diffusion-based uni-condition models with a derived integration formula, which is supported by rigorous theory proof. Owing to its training-free nature, MixDiffusion is easy to deploy and readily extensible to new control modalities.

---


### 291. [Reviving Ancient Paintings via Poem: A Colorization Framework for Aligning Cultural Semantics](https://arxiv.org/abs/2607.17638)

**<font color=#1a73e8>作者：</font>** Junming Gao, Biao Zhu, Xiaosong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The irreversible fading of ancient paintings disrupts the "congruence between poems and paintings", a core aesthetic principle where visual imagery harmonizes with literary inscriptions. Although diffusion models provide strong generative priors, restoring historically faithful colors remains difficult: visual restoration is inherently ambiguous, while direct text guidance often causes modern semantic bias, over-saturation, and cross-boundary color leakage. To address this, we propose PoemColor, a poem-guided ancient painting colorization framework. Our method aligns poetic cultural semantics with painting restoration through two key designs. First, the Poetic Painting Projector (P3) converts implicit poetic context into a classical color-aware condition via poem-to-palette pretraining, reducing the ambiguity of poem-to-color mapping. Second, Structure-Aware Semantic Attention (SASA) regulates how poetic color semantics are injected into the diffusion backbone by jointly controlling their propagation direction and regional injection strength. In addition, we construct a hybrid restoration dataset that integrates synthetic degradation with expert-restored artifacts, providing both scalable supervision and real classical color references. Extensive experiments demonstrate that our framework significantly outperforms state-of-the-art methods, delivering controllable colorization that revives both historical authenticity and poetic semantics.

---


### 292. [Direct Clinical Joint Angle Extraction from Parametric Body Model Rotation Matrices](https://arxiv.org/abs/2607.17639)

**<font color=#1a73e8>作者：</font>** Joey Páolo Kardolus, Daan Hendriks, Jaap Jansen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative joint angles are rarely available in routine care because the tools are slow, costly, or confined to a laboratory. We show that clinical joint angles can be read directly from the per-segment rotation matrices a parametric body model already produces, with no inverse-kinematics or musculoskeletal-model fitting step. On the OpenCap LabValidation cohort, using the GEM-X body-model estimator on single-smartphone video, our pooled mean absolute error is 4.50 degrees over the fifteen joint angles that match the OpenCap Monocular reference set, the same accuracy range as OpenCap Monocular's 4.8 degrees on the same cohort and reference standard, from a much simpler pipeline. The step that connects a body model to clinical angles is a small calibration table rather than an optimisation, so the same procedure transfers unchanged to other body models: repeating it on SAM 3D Body, changing only the table, gives 4.66 degrees, statistically indistinguishable from GEM-X, and runs in real time from a live single-camera stream. The method needs no per-recording inputs beyond the video itself: no participant height, no camera-intrinsics database, no per-subject model scaling. This broadens where movement analysis is practical, from in-clinic and at-home recording to telerehabilitation and large-scale decentralised studies.

---


### 293. [A Digital Twin-Based Method for Evaluating Local Collective Tariffs in Distribution-Level Energy Systems](https://arxiv.org/abs/2607.17640)

**<font color=#1a73e8>作者：</font>** Kristoffer Christensen, Bo Nørregaard Jørgensen, Zheng Grace Ma  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This work addresses the need for engineering-grounded evaluation of implement-ed tariff mechanisms in distribution-level energy systems. A digital twin-based method is proposed for assessing local collective tariffs under realistic behavioral and infrastructural conditions. The approach integrates agent-based modeling of household consumption and generation, virtual aggregation through a shared metering abstraction, and explicit representation of tariff logic within a unified simulation environment. The method is demonstrated through its application to the Danish Local Collective Tariff across representative residential energy community configurations, including scenarios with photovoltaic generation, battery storage, and electric vehicle charging. Results indicate that aggregation of heterogeneous demand profiles reduces peak coincidence and enables more efficient allocation of tariff components, leading to measurable cost reductions at the community level. At the same time, the outcomes reveal sensitivity to the temporal alignment of consumption and generation, influencing the degree of cost neutrality across participants. The findings illustrate how digital twin-based evaluation can support systematic assessment of tariff mechanisms by capturing the interaction between infrastructure, user behavior, and regulatory design. The proposed approach provides a basis for analyzing and comparing tariff structures in distribution-level energy systems beyond the specific case considered.

---


### 294. [BMFA: Boundary-Minority Free-Energy Adaptive Screening](https://arxiv.org/abs/2607.17656)

**<font color=#1a73e8>作者：</font>** Wenyan Xu, Alizer Wong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers process spatially redundant tokens efficiently only when coarse token summaries preserve the evidence required by exponential attention aggregation. We identify a boundary-minority underestimation failure in which a spatially small, high-response region contributes dominant Gibbs mass while remaining nearly invisible to a block mean. We formalize the failure through the discrepancy between normalized log-mean-exp free energy and mean summarization, prove that minority Gibbs mass can remain non-vanishing as its spatial support and mean contribution vanish, and characterize the limitations of finite-order moment corrections. Building on the resulting analysis, we introduce Boundary-Minority Free-Energy Adaptive Screening (BMFA), which constructs a hierarchical piecewise-constant approximation and recursively refines blocks according to a computable lower-bound increment of local free energy. Controlled synthetic tests, COCO and LVIS diagnostic probes, closed-loop DeiT-Tiny evaluations, and ImageNet-1K experiments establish a consistent evidence chain. BMFA reduces the mean synthetic underestimate from 2.582 to 0.261 at a 5.794% leaf ratio, lowers the COCO image-edge mean gap from 2.254 to 0.526, and preserves 71.520% ImageNet Top-1 accuracy at a 55.861% leaf ratio. The current prototype evaluates selection quality after full QK computation; the reported leaf ratio therefore characterizes representation granularity rather than verified sparse-kernel speedup.

---


### 295. [RayOcc: Occlusion-Aware Ray Occupancy Estimation via Gaussian Mixture Intensity](https://arxiv.org/abs/2607.17660)

**<font color=#1a73e8>作者：</font>** Junho Kim, Seongwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-only 3D semantic occupancy prediction aims to infer voxel-wise scene semantics from multi-view images, yet remains fundamentally challenging due to depth ambiguity and occlusion. Along a single camera ray, multiple spatially separated surfaces may coexist, making occupancy inherently a multi-label existence problem rather than a single-depth estimation task. However, most existing approaches favor a single dominant depth hypothesis per ray, limiting their ability to model volumetric scenes under complex occlusion. To address this limitation, we introduce RayOcc, an occlusion-aware ray occupancy framework that reformulates ray modeling as multi-label existence prediction. Instead of predicting a categorical depth distribution, RayOcc estimates a non-normalized Gaussian mixture intensity along each ray and converts it into interval-wise occupancy probabilities via a Poisson event formulation, allowing multiple occupied hypotheses to coexist without enforcing mutual competition across depth. The predicted mixture components are interpreted as occupancy hypotheses to initialize sparse 3D Gaussian primitives, which are refined and rasterized for semantic occupancy prediction. Experiments on the nuScenes benchmark show that RayOcc achieves state-of-the-art overall IoU and mIoU among the compared Gaussian-based occupancy methods.

---


### 296. [Early Yield Prediction for Sugar Beet Fields using Satellite Data -- Learnings from Specialized Vision Transformers](https://arxiv.org/abs/2607.17661)

**<font color=#1a73e8>作者：</font>** Philipp Vaeth, Bhumika Laxman Sadbhave, Denise Dejon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing has become an increasingly valuable tool for agricultural monitoring, particularly through the use of publicly available satellite imagery. However, effectively integrating domain knowledge into machine learning methods remains challenging. This study presents a real-world example of early sugar beet harvest yield forecasting from purely optical Sentinel-2 imagery, demonstrating how a tight integration of domain knowledge and machine learning can lead to synergistic gains. We empirically find that using very small vision transformer patch sizes and all available Sentinel-2 spectral bands improves our model despite being uncommon design choices in the domain. As a practical contribution, we were able to identify a large fraction of low-yield fields in a different year early on in the growth cycle through a modified training setup and a ranking-based detection of underperforming fields.

---


### 297. [Selectivity Matters: Source Node Influence Pruning for Unsupervised Graph Domain Adaptation](https://arxiv.org/abs/2607.17668)

**<font color=#1a73e8>作者：</font>** Ridong Han, Yawen Shen, Zhongnian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised Graph Domain Adaptation (UGDA) aims to facilitate knowledge transfer from a labeled source graph to an unlabeled target graph by mitigating cross-domain distribution shifts. Existing methods primarily focus on node-level feature alignment in latent spaces, relying on the implicit assumption that all source nodes contribute positively to the alignment. However, this assumption often fails because a node's semantic information is intrinsically coupled with its topological graph structure. Due to structural shifts, source nodes with severe structural deviations (e.g., structural outliers) lack semantic counterparts in the target graph, and forcing alignment on them introduces severe noise and causes negative transfer. To bridge this gap, we argue that selective source node utilization is superior to full-graph training, thereby shifting the research paradigm from feature-level alignment to data-level refinement. To this end, we propose Source Node Influence Pruning (SNIP), a novel model-agnostic, data-centric refinement framework. Specifically, SNIP quantifies the structural discrepancy between individual source nodes and the target domain by integrating multiple centrality measures, assigning each source node an influence score. A rank-based normalization mechanism is further employed to eliminate scale variations across different measures, allowing SNIP to effectively identify and filter out structurally incompatible nodes with low influence scores. As a plug-and-play method, SNIP constructs a refined "sub-source" graph that is inherently more beneficial for subsequent alignment. Comprehensive experiments across eight transfer scenarios on five real-world datasets demonstrate that SNIP consistently outperforms competitive baselines and significantly enhances adaptation performance, validating the superiority of selective node utilization over full-graph training.

---


### 298. [GeneSpeak-FP: Target and Compound Retrieval from Observed Cell-Level Perturbation Signatures](https://arxiv.org/abs/2607.17671)

**<font color=#1a73e8>作者：</font>** Kseniia Vaniushkina, Jeongmin Lim, Jinyong Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale single-cell perturbation atlases make it possible to ask an inverse question: given an observed transcriptional response, which annotated targets and compounds in a fixed library are most consistent with that response? We present \model, a Transformer retrieval model for this closed-library setting. Each input is a cell-level perturbation signature formed by contrasting one treated cell with a cell-line-specific mean DMSO reference. The encoder maps the signature to a target-retrieval vector and a molecular-embedding vector, trained jointly with supervised target losses and structure--transcriptome alignment. We evaluate on Tahoe-100M conditions with mapped target annotations using a within-compound stratified 90/10 condition-pair split of 10,505 training and 1,168 validation drug--cell-line pairs. Because compounds and cell lines can occur in both partitions, the experiment measures held-out condition-pair retrieval rather than generalization to unseen compounds or cellular contexts. In a Monte Carlo evaluation over 38,400 sampled validation cells, \model\ achieved target Recall@10 of 0.408 and Recall@20 of 0.544, together with compound Hit@1 of 0.129, Hit@10 of 0.343, and mean reciprocal rank of 0.205 over a 379-compound bank. A separate diagnostic evaluation produced nearly identical values for the main model and large gains over a random-vector control and post-hoc bag-of-genes controls. These results demonstrate that a single multi-task model can recover both mapped target annotations and recorded compound identities from observed cell-level responses in the evaluated Tahoe-100M closed-library setting. Generalization to unseen compounds and cellular contexts remains to be established.

---


### 299. [ShotPlan: Cinematic Video Generation with Learnable Planning Token](https://arxiv.org/abs/2607.17675)

**<font color=#1a73e8>作者：</font>** Su Guo, Guangce Liu, Haosen Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current video generation models achieve impressive results in single-shot generation, yet remain limited in cinematic video generation, where coherent narratives and effective multi-shot composition require explicit shot planning. To address this challenge, we propose ShotPlan, a framework for explicit multi-shot cinematic video generation built upon a video diffusion foundation model. Our method introduces learnable planning tokens that capture shot-level transition cues and can be seamlessly integrated with the original video generation tokens to control transition timestamps. Unlike standard video generation tokens, the proposed planning tokens are equipped with Fractional Temporal Rotary Position Embedding (FRoPE), enabling shot transitions to be modeled at the frame level. Experiments demonstrate that ShotPlan significantly outperforms existing cinematic video generation methods, offering more flexible shot management and stronger inter-shot consistency.

---


### 300. [Tokenizing Crosslingual Homographs](https://arxiv.org/abs/2607.17689)

**<font color=#1a73e8>作者：</font>** Rotem Brillant, Yuval Pinter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual language models rely on shared subword vocabularies to represent multiple languages within a limited number of token units. While such sharing is often useful, it can also create cases in which identical surface forms are treated too uniformly across languages, even when their meanings or usage differ. We investigate this limitation through cross-lingual homographs and false friends, and examine whether introducing language information earlier in the tokenization process can improve their treatment. We propose a simple tokenizer-level intervention based on language cues: language-specific characters replacing initial characters of shared-vocabulary words, reducing common identity during vocabulary construction. In intrinsic analysis, we find through tokenizer-level statistics that BPE and UnigramLM often treat cross-lingual homographs in a largely language agnostic way, whereas the context-sensitive SaGe tokenizer diverges more strongly; our intervention removes this gap. In downstream English-to-X machine translation, our cues yield modest improvements in several settings, especially under BPE, although the effect is not consistent across all languages and evaluation sets. Overall, the findings suggest that adding lightweight language information at the tokenizer level is a promising direction for further exploration.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-386](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
