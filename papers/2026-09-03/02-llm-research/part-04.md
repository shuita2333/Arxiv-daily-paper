# 🧠 大模型相关研究 | 2026年09月03日

> 本类共 **295** 篇论文：已确认 **283** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-295](./part-06.md)

---

### 151. [Are You Thinking What I am Thinking? : Examining Conceptual Separation in Neural Architectures](https://arxiv.org/abs/2609.00764)

**<font color=#1a73e8>作者：</font>** Jaee Ponde, Roshni Agarwal, Subhashis Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are increasingly employed to identify both well-defined and ambiguous concepts, yet output-level metrics reveal little about how those concepts are represented internally. Our study asks if these networks exhibit \textit{conceptual separation}: if examples of the same concept form coherent representations, and whether related concepts lie closer together in the representation space. We examine this conceptual organisation in Convolutional Neural Networks (CNNs) and Large Language Models (LLMs) through geometric and distributional analysis of their internal activations. In CNNs, familiar ImageNet concepts form coherent and semantically ordered representations, while this coherence weakens for unseen concepts and suffers within-class domain shift. In LLMs, clearly distinct domains remain well separated, related subdomains move closer together, and the distinction between ambiguous topics collapses at both the mean and covariance level. These results suggest that conceptual separation can reveal structure that output accuracy alone cannot, and may serve as a useful diagnostic of how robustly a model represents the concepts it is asked to identify. Code and data available on \href{this https URL}{GitHub}.

---


### 152. [DiagEvo: Diagnosis-Guided Self-Evolution via Hierarchical Error Memory](https://arxiv.org/abs/2609.00768)

**<font color=#1a73e8>作者：</font>** Xincheng Wei, Yifan Ding, Yoshua Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-play is an effective paradigm for language-model self-evolution, but without guidance, solver performance can plateau or decline across rounds. Unguided methods steer question generation with signals such as difficulty, learnability, or diversity. These signals keep questions challenging and varied but do not specify which unresolved reasoning weaknesses later rounds should target. Guided methods obtain direction from external task resources, including human examples, document corpora, or specified difficulty targets, and therefore rely on task information supplied outside the self-play loop. We show that the needed direction can instead be derived from the solver's own failure history. We introduce DiagEvo, whose diagnostician extracts recurring error causes from this history and stores them in a hierarchical error-cause memory. The memory groups related causes under skill nodes and tracks each as Active or Mastered according to self-consistency on targeted questions. The challenger uses these states and recurrence counts to balance cause-targeted generation with free exploration. Double-confidence filtering retains intermediate-difficulty questions only when the most common solver answer has a clear vote lead. DiagEvo derives its curriculum from information produced during self-play, without external task resources. With the default 4B diagnostician, DiagEvo outperforms every baseline in mean accuracy across all nine benchmarks for each of the three solvers: Qwen3-4B, Qwen3-8B, and OctoThinker-8B. On Qwen3-8B, it reaches 72.3% mean accuracy across five mathematical reasoning benchmarks, 4.5 percentage points above R-Zero. Its mean accuracy across all nine benchmarks is 57.4%, 1.1 percentage points above DARC. Ablations show that the hierarchical error-cause memory and double-confidence filtering both contribute to these gains.

---


### 153. [Solaris: Towards Interfaces That Are Generated, Not Coded](https://arxiv.org/abs/2609.00776)

**<font color=#1a73e8>作者：</font>** Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital interfaces are traditionally implemented through intermediate representations such as code, requiring their appearance and behavior to be specified in advance. We introduce Solaris, an interface world model that instead generates an interactive UI directly, frame by frame, in response to user actions. Solaris treats mouse interactions as conditioning signals and autoregressively synthesizes the resulting visual state at interactive speeds. To enable real-time generation while maintaining visual coherence over extended interactions, we combine autoregressive frame generation with few-step distillation and training on the model's own outputs. A language model complements the visual world model by interpreting user intent and specifying how interactions should affect the generated environment, separating high-level reasoning from visual rendering. By generating both the appearance and behavior of an interface dynamically, Solaris enables open-ended interactions that need not be explicitly programmed in advance. We view interface world models as a step toward a new paradigm for software, where interfaces are generated and adapted continuously around user intent rather than implemented as fixed collections of predefined states and

---


### 154. [Forbid Your Attention: Fooling Multimodal Large Language Models by Selectively Removing Intrinsic Focus in Spectral Domain](https://arxiv.org/abs/2609.00788)

**<font color=#1a73e8>作者：</font>** Daizong Liu, Junhao Dong, Zhiyuan Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have extended the capability of large language models (LLMs) to process more contextual multimodal information, showing remarkable progress in diverse realistic multimodal applications. Despite their strong perception and reasoning abilities, recent studies reveal that MLLMs remain highly vulnerable to adversarial inputs, especially those targeting visual components. However, existing attacks mainly focus on global perturbations, lacking an understanding of how MLLMs internally interpret visual structures. In this paper, we make the attempt to investigate the intrinsic focus of MLLMs in the frequency domain and discover that their predictions are particularly sensitive to phase information, which encodes essential structural and semantic cues. Based on this observation, we propose a novel phase-aware adversarial attack framework that explicitly restricts adversarial perturbations to structure-relevant phase regions to suppress the MLLMs' focus for effective and imperceptible attacks. To further amplify the structural influence, we also introduce an auxiliary adversarial prompt learning module to guide multimodal misalignment around phase-sensitive regions, misleading the MLLM's attention toward targeted structural patterns. Extensive experiments on multiple representative MLLM models and datasets demonstrate the superior effectiveness of our method compared to existing attacks.

---


### 155. [RISA: Response Inspection and Selective Actions for Refusal Calibration in Large Language Models](https://arxiv.org/abs/2609.00790)

**<font color=#1a73e8>作者：</font>** Wenhan Chang, Tianqing Zhu, Ping Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable refusal behavior requires Large Language Models (LLMs) to reject harmful prompts with only answering benign ones. Incorrect refusal behavior can either expose users to harmful responses or prevent users from obtaining useful answers. Training-time alignment improves refusal behavior by updating model parameters with safety data, but requires additional computation and training. In contrast, inference-time alignment aims to modify LLM behavior during inference without updating the underlying model parameters. Existing inference-time methods mainly rely on in-context safety prompting, activation steering, or decoding control. However, most of them intervene without first determining whether the initial response is already appropriate, potentially altering a correct refusal or a useful answer. Effective selective intervention therefore requires identifying prompt intent beyond sensitive keywords, covering semantic variations that fixed rules may miss, and adapting the verifier to different base models. To address these challenges, we propose Response Inspection and Selective Actions (RISA), an inference-time framework that inspects the initial response and selectively corrects refusal errors without updating the base model. RISA first uses fixed contextual rules to assign refusal scores to clear cases. For unmatched cases, it derives a refusal score from the final-layer prompt hidden state using a calibrated linear probe. To adapt to different base models, RISA separately calibrates the probe score, representation-support boundary, and action thresholds. At runtime, RISA combines the prompt score with the initial refusal status and applies an action policy to intervene only when necessary. Experimental results demonstrate that RISA improves refusal reliability while largely preserving model utility, offering a practical solution for response-aware refusal calibration in LLMs.

---


### 156. [Instella-MoE Technical Report](https://arxiv.org/abs/2609.00791)

**<font color=#1a73e8>作者：</font>** Jiang Liu, Sudhanshu Ranjan, Prakamya Mishra 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce Instella-MoE, a fully open Mixture-of-Experts (MoE) language model with 16 billion total parameters and 2.8 billion active parameters per token, trained entirely from scratch on AMD Instinct MI300X and MI325X GPUs. Instella-MoE combines a sparsely activated MoE design with architectural and system-level innovations, including Gated Multi-head Latent Attention (Gated MLA) and FarSkip-Collective connectivity, enabling efficient large-scale training and inference. The model is developed through a multi-stage pipeline comprising pre-training, mid-training, long-context extension, supervised fine-tuning with feedback-driven data curation, direct preference optimization, and reinforcement learning with Multi-Teacher On-Policy Distillation. Instella-MoE achieves an average score of 76.7 across standard pre-training benchmarks, outperforming prior fully open models including OLMo-3-7B, SmolLM3-3B, and OLMoE-1B-7B, while remaining competitive with open-weight MoE and dense baselines at comparable active-parameter scales, including Moonlight-16B-A3B and Qwen3.5-4B. After post-training, our final Think checkpoint achieves an average score of 73.2 across instruction-following, reasoning, math, coding, and chat benchmarks, outperforming both fully open and open-weight models with comparable or larger active parameter counts in our evaluation. To support transparent and reproducible research, we release the complete Instella-MoE model flow, including model weights, training configurations, data mixtures, and training code. Together, these contributions establish Instella-MoE a strong, fully open foundation for efficient, high-performing MoE models and reproducible research.

---


### 157. [SFAD: Speculative Factuality-Aware Decoding](https://arxiv.org/abs/2609.00796)

**<font color=#1a73e8>作者：</font>** Guanqiao Chen, Di Wang, Lijie Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As one of the most critical challenges in large language models, contextual faithfulness directly determines their reliability in knowledge-intensive applications. This task is particularly challenging as it requires balancing factual consistency with generation efficiency. Contrastive decoding methods require dual forward passes (with and without context) to compare model outputs, doubling inference computational overhead, while post-training alignment demands extensive reinforcement learning with substantial computational overhead. To address this challenge, we present \textbf{SFAD}, a speculative decoding framework that enhances contextual faithfulness without inference degradation. We first construct \textbf{ConFide}, a preference dataset with fine-grained atomic perturbations, to train a context-faithful draft model via Direct Preference Optimization. During inference, Epistemic Friction detects potential hallucinations by quantifying distributional tension weighted by specialist certainty. When friction exceeds the threshold, Asymmetric Logit Steering refines the target distribution through residual-based logit injection; otherwise, standard speculation proceeds. Extensive experiments demonstrate that SFAD substantially improves faithfulness while achieving $2.48\times$ speedup, offering a practical solution for efficient LLMs.

---


### 158. [Towards a Reliable and Practical Eval Pipeline](https://arxiv.org/abs/2609.00805)

**<font color=#1a73e8>作者：</font>** Emma Thuong Nguyen, Abhishek Ghose  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based software systems increasingly require effective "evals" as quality gates in the development lifecycle. However, existing work typically addresses individual aspects of eval reliability rather than the full set of practical requirements. We present an end-to-end eval pipeline that combines eval checklist creation, with learned aggregation for checklist responses, to improve agreement across LLM judges and accuracy against human judgments. The framework additionally pro- vides self-consistency, explanations, and prediction uncertainty, and we empirically demonstrate its effectiveness.

---


### 159. [One Policy, Any Budget: Internalizing Budget-Aware Search via Reinforcement Learning](https://arxiv.org/abs/2609.00813)

**<font color=#1a73e8>作者：</font>** Xiaowei Sun, Jin Li, Yili Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While reinforcement learning has enabled LLM-based search agents to invoke external tools, existing methods train under fixed budgets and cannot adapt when constraints vary at deployment. We propose AnySearch, a framework that enables a single policy to perform budget-aware search under any budget constraint through a training scaffold and curriculum reinforcement learning. In the first phase, we train the agent with explicit budget state injection and structured reasoning prompts that guide efficient allocation under linearly decaying budgets. In the second phase, the scaffold is removed and the agent learns to operate autonomously under adaptively sampled budget constraints, matching inference conditions. Both phases are optimized with a composite reward that couples answer accuracy with budget efficiency through absolute and relative signals, where an adaptive weight amplifies the efficiency signal for high-accuracy queries and attenuates it for low-accuracy ones. Extensive experiments on seven general and multi-hop QA benchmarks show that our method outperforms baselines across all budget scales, generalizes to unseen constraints beyond the training range, and achieves superior tool productivity without excessive token overhead. Our code is available at this https URL.

---


### 160. [AnalysisBank: An Expert Analysis Pattern Library for Financial Report Generation](https://arxiv.org/abs/2609.00818)

**<font color=#1a73e8>作者：</font>** Yajing Yang, Yunshan Ma, Kelvin J.L. Koa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We argue that financial report generation should operate at the analytical rather than structural level, composing content from data-derived insights rather than high-level topics or sections. To this end, we propose AnalysisBank, which distills expert reports into a reusable library of Analyses, each pairing a data signal, an analytical move, and the expert span it was derived from. At inference time, AnalysisBank matches input signals to library entries and applies the retrieved moves to compose the report. A study of Analyses distilled from 550 expert reports reveals a heavy-tailed distribution of 47-52 signal types spanning 13 move types. On two financial benchmarks across four LLM backbones, AnalysisBank increases the proportion of novel, data-grounded insights by 1.7-3.7x over structural-level baselines. Transfer to scientific writing suggests that the distinction generalizes beyond finance. Code and the distilled Analysis library are available at this https URL.

---


### 161. [Visual Attention Faithfulness in Vision-Language Models is Heterogeneous](https://arxiv.org/abs/2609.00830)

**<font color=#1a73e8>作者：</font>** Xurui Song, Weishi Wang, Zhongqi Yue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whether attention weights faithfully reflect model reasoning has been actively debated in NLP, yet this question remains largely unexplored for the visual modality in Vision-Language Models (VLMs). We address this gap through causal perturbation analysis on current VLMs, evaluating both the comprehensiveness and sufficiency gap of attention-ranked visual tokens. Our analysis reveals that visual attention faithfulness is heterogeneous, manifesting in three distinct processing modes: Faithful-Sufficient, where top-$k$ attention tokens are both necessary and sufficient for prediction; Faithful-Distributed, where they are necessary but broader visual context remains required; and Non-Focal, where no localized attention region is individually necessary while visual information remains an essential trigger for prediction. Furthermore, human-annotated ground-truth regions satisfy comprehensiveness in only $\sim 60$% of cases compared with model attention rankings, revealing systematic divergence between model visual reliance and human intuition. We demonstrate these patterns across both general VQA on VQAv2 and document tasks on VRDU and ChartQA, showing that visual attention faithfulness varies systematically with processing demands and model architectures rather than being uniformly faithful or unfaithful.

---


### 162. [Staged Linguistic Seeding: Grounded Query Expansion for Verified-Unit QA in AI Contact Centers](https://arxiv.org/abs/2609.00844)

**<font color=#1a73e8>作者：</font>** Hyeonseop Yoon, Jeong-Eun Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Customer-service QA in an AI contact center (AICC) runs under deployment constraints that benchmark QA misses: tight voice-hotline latency and a high cost for unsupported or wrong automatic answers. We deploy a system that answers only from a closed set of verified QA units: it returns a retrieved unit verbatim, or routes to clarify, abstain, or handoff. The index is enriched offline by staged linguistic seeding (SLS): a human authors a per-unit world-grounded slot recipe, gpt-4.1-mini renders it into variants, and a light human gate filters them. One methodology is reused across both domains, so inference stays a single retrieval pass with no query-time generation. On held-out query variants from two industrial domains, SLS lifts hybrid R@1 to 0.881/0.930 (+0.27/+0.34), with gains across all five retrievers tested. At the same gpt-4.1-mini generation budget, SLS beats doc2query by +0.20/+0.32, while cross-provenance evaluation provides additional evidence of transfer across generated-query distributions. Verified-unit answering also removes free-form generation's unsupported-content surface (7-13% versus approximately 0%). We report this as an application study, including negative results.

---


### 163. [Towards Generalizable Visually Grounded Exploration of Household Devices](https://arxiv.org/abs/2609.00845)

**<font color=#1a73e8>作者：</font>** Linhao Zheng, Zeming Liu, Wangke Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Vision-Language Models (VLMs) have demonstrated impressive capabilities in static visual recognition and high-level semantic reasoning. However, current embodied exploration paradigms still heavily rely on imitation learning from human-annotated trajectories, which severely limits agents' generalization ability. The key bottleneck of realizing general autonomous embodied agents lies in Generalizable Visually Grounded Exploration: the ability to operate novel devices without manuals or specific training by actively grounding abstract world knowledge into fine-grained visual affordances. Yet, existing benchmarks fail to evaluate this capability: they generally rely on explicit documents and annotated trajectories, neglecting the dynamic Hypothesis-Interaction-Refinement process essential for functional device operation. To bridge this gap, we introduce VGEBench, a comprehensive benchmark designed to evaluate the generalizable visually grounded exploration capabilities of VLMs. Unlike static datasets, we construct a Logic-Driven State Machine framework. This framework simulates multi-turn interaction loops, compelling agents to achieve goals by active visual perception and feedback-driven correction. Experimental results demonstrate that existing VLMs face significant challenges in translating semantic knowledge into physical execution and maintaining long-horizon state tracking.

---


### 164. [Verifiable Disaster Storylines and Causal Knowledge Graphs: A Citation-Grounded Pipeline from Heterogeneous Humanitarian Sources](https://arxiv.org/abs/2609.00858)

**<font color=#1a73e8>作者：</font>** Ivan Decostanzi, Michele Ronco, Sergio Consoli 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective humanitarian response depends on the rapid synthesis of heterogeneous, high-volume information sources - a task that routinely exceeds human analytical capacity in the critical early hours of a crisis. We present a pipeline that combines structured disaster records from EM-DAT with unstructured documents from ReliefWeb and the European Media Monitor (EMM) to produce source-grounded disaster storylines and causal knowledge graphs supporting situational awareness for responders and analysts. Using Retrieval-Augmented Generation, the pipeline extracts structured storylines - tabular event profiles covering 17 fields, from severity and key drivers to child-sensitive impact indicators - and constructs causal knowledge graphs where each node and edge is enriched with citation-grounded explanatory narratives, enabling full traceability back to primary sources. We evaluate the system on three diverse crisis use cases through a human evaluation involving 9 domain expert and 9 non-expert evaluators. Results confirm high retrieval precision, strong faithfulness of extracted causal relations, and a clear expert preference for citation-grounded components over ungrounded alternatives. The pipeline is designed to scale to the full EM-DAT catalogue, with the goal of publicly releasing a narrative-enriched version of the database.

---


### 165. [Reinforcement Learning Enhanced LLM Agents for Complex Vehicle Routing Problems](https://arxiv.org/abs/2609.00859)

**<font color=#1a73e8>作者：</font>** Yi Chen, Zikang Yu, Jiahai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vehicle Routing Problems (VRPs) are fundamental combinatorial optimization problems with widespread applications in various scenarios. The advanced optimization solvers can effectively solve such problems. However, modeling complex VRP variants for solvers often requires substantial domain expertise, which limits the accessibility of advanced optimization technologies. In this paper, we propose Reinforcement Learning Enhanced LLMAgents(RLEA), a multi-agent framework designed to automate the modeling of complex VRPs. RLEA introduces a lightweight neural Planner trained with Soft Q-learning to efficiently orchestrate the actions of LLM-based agents. In addition, we equip the system with an evolutionary memory module and retrieval-augmented generation, enabling the agent to leverage both accumulated experience and external solver knowledge during program generation and refinement for solving VRPs. We evaluated 48 distinct VRP variants across various solvers. The experimental results demonstrate that RLEA outperforms the previous state-of-the-ar method, achieving a 16.67% higher success rate while significantly reducing runtime errors. These results validate that integrating reinforcement learning with LLM-based reasoning is highly effective for automated optimization modeling. The appendix is available at: this https URL.

---


### 166. [MemoryWalker: Stop Training Agents on Contexts They Never Saw](https://arxiv.org/abs/2609.00865)

**<font color=#1a73e8>作者：</font>** Zinco J, Xunjie Zhu, Shen Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production agent harnesses such as Claude Code and Qwen-Agent compress context during rollout, but training under compression creates a conditioning problem: every eviction branches the effective history, so the learning object is a tree rather than a sequence. Existing linearizations either retain the rightmost path, causing time-travel leakage, or replay a depth-first traversal, causing train-inference mismatch. We introduce two exact, gradient-equivalent corrections: LogitTree, a segmented K-forward traversal, and a packed 4D attention mask. LogitTree requires K+1 backward passes; the 4D mask requires a custom kernel and white-box eviction records. We also propose SDCC (Self-Distillation for Conditioning Consistency), a single-backward-pass variational relaxation. At each eviction, it minimizes forward KL between the compressed student and a stop-gradient teacher on the reconstructed pre-eviction prefix. A residual per-junction KL of epsilon_KL gives an O(sqrt(epsilon_KL)) bound on the train-deployment total-variation gap. SDCC also applies to black-box harnesses. On seven web-search benchmarks with TC-RAG, AgentFold, MemexRL, Claude Code, and OpenCode, naive training inflates the train-rollout log-probability gap, especially on eviction-heavy batches. The exact methods stay at the no-compression floor, and SDCC substantially closes the gap, with lower logit drift and higher rollout rewards.

---


### 167. [Benchmarking Vision-Language Models for Automated Pathology Diagnosis and Report Generation](https://arxiv.org/abs/2609.00866)

**<font color=#1a73e8>作者：</font>** Yumi Lee, Harim Oh, Hyoryung Kim 等 55 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of vision-language models (VLMs) has accelerated progress in computational pathology; however, whole-slide image (WSI)-based pathology report generation remains limited by the scarcity of large-scale WSI--report datasets and the complexity of mapping spatially distributed visual patterns to structured clinical text. To address this, we introduce a clinically curated Pan-Asia WSI--report dataset of approximately 10,500 pairs from five institutions and establish the REG 2025 benchmark through a MICCAI challenge for systematic evaluation of multimodal models. We analyze submitted methods spanning pretrained VLMs, multiple-instance learning frameworks, hierarchical expert models, retrieval-augmented generation, and cross-modal Transformers. Rather than indicating that VLM use alone was sufficient for superior performance, the results suggest that top-performing methods benefited from structured report representations, hierarchical diagnostic decomposition, and effective multimodal grounding. We identify key limitations, including instability in quantitative attribute estimation (e.g., numeric hallucination) and a tendency toward diagnostic overspecification, with some errors resembling known diagnostic pitfalls in routine pathology. These findings establish REG 2025 as a benchmark for evaluating WSI-based structured report generation and vision-language understanding in computational pathology, providing insights for the design of clinically grounded multimodal pathology models.

---


### 168. [The Visual Insensitivity Gap: Diagnosing When Vision-Language Models Fail to Use Visual Evidence](https://arxiv.org/abs/2609.00868)

**<font color=#1a73e8>作者：</font>** Genpei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models are evaluated by aggregate accuracy on multimodal benchmarks, a practice that implicitly assumes the model uses its visual input. We show this assumption fails on 40%--97% of samples across six VLMs and three perceptual benchmarks: blurring the question-relevant visual region leaves the next-token distribution nearly unchanged. We name this phenomenon the Visual Insensitivity Gap and quantify it with a per-sample Visual Sensitivity Index (VSI). The gap is a property of samples, not of models: VSI ranks correlate across models (grand-mean Spearman rho=+0.40, permutation p<10^-3), so the same samples are flagged insensitive by VLMs sharing no architectural detail beyond a contrastively pretrained vision tower. The mechanism is concrete: on the insensitive samples, a linear probe on each model's own vision tower distinguishes perturbed from clean images at 0.72--0.79 accuracy, yet the model's argmax token changes on only 2%--11% of the same samples, an encoder--LLM gap above 0.65 on every model. Mapping VSI's diagnostic utility cell by cell surfaces a strong regime (multi-choice reasoning on capable VLMs: AUROC=0.85--0.87) and a weak regime (well-calibrated factuality, where softmax confidence already leads). VSI is not a universal best abstention signal; it is a sample-intrinsic indicator of vision-ignoring failure, best used as a conditional ensemble component.

---


### 169. [Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning](https://arxiv.org/abs/2609.00879)

**<font color=#1a73e8>作者：</font>** Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable disaster damage assessment requires models that provide both accurate predictions and transparent explanations. However, existing multimodal approaches are limited by scarce annotated data and insufficient evaluation of reasoning quality. This study proposes a two-stage training framework that integrates Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) within a unified data construction pipeline. From a single Human-in-the-Loop (HITL) annotation workflow, two complementary datasets are derived, namely ReasoningSet, which contains validated rationales for SFT, and PreferenceSet, which comprises paired rationales for DPO-based alignment. The framework evaluates both classification performance and explanation quality using automatic metrics, model-based scoring, and human ranking. Experimental results show that SFT improves accuracy from 73.64% to 78.29% and increases Macro-F1 by 29% compared to the baseline, while explanation quality improves by approximately 25%. Subsequent DPO alignment further enhances interpretability on the PreferenceSet. Cross-model validation on InternVL-3-8B and LLaVA-1.5-7B demonstrates the robustness and generalizability of the approach. The proposed framework improves detection of underrepresented mild damage cases, reduces high-risk misclassifications, and strengthens alignment between model reasoning and human judgment. Overall, it provides a reproducible pathway to develop reliable multimodal systems that deliver auditable, actionable disaster insights for emergency management.

---


### 170. [Using LLMs to Elicit Security Requirements for Service-Oriented Cyber Ranges](https://arxiv.org/abs/2609.00886)

**<font color=#1a73e8>作者：</font>** Michail Takaronis, Athanasia Kollarou, Georgios Kavallieratos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber ranges are complex environments comprising many interacting components and stakeholders with different security concerns. The Service-Oriented Cyber Range (SOR) is no exception, particularly when it comes to training scenarios targeting critical infrastructure. Security concerns are translated into security requirements, the elicitation of which is usually difficult and time-consuming. This work examines how large language models can assist in eliciting security requirements for a service-oriented range and help produce a useful baseline for designers and developers. The approach follows a SEBoK-guided process in which security mission objectives and stakeholder needs were first identified and then provided as a prompt context along with architectural guidelines to five LLMs: GPT-5.2, Gemini 3.1 Pro, Grok 4.1, Sonar, and Kimi K2.5. The models generated 84 security requirements in total, which were consolidated into a comprehensive set of 27 requirements and then mapped to the architectural layers of the service-oriented range. The final set was evaluated by five cybersecurity experts against the criteria of necessity, clarity, completeness, feasibility, and testability, with an additional rejection option. The results showed a high acceptance rate, specifically for necessity with 98.5%, clarity with 87.4%, completeness with 85.2%, feasibility with 78.5%, and rejection with 0.7%. Testability was lower at 44.4%, indicating a slight lack of information on how these requirements could be tested. These findings show that LLMs can support early stages of the elicitation of security requirements, although human review is still needed, especially to improve or adjust certain aspects of the requirements.

---


### 171. [CacheBridge: Efficient Cross-Model KV Cache Transfer](https://arxiv.org/abs/2609.00891)

**<font color=#1a73e8>作者：</font>** Xingyu Qu, Siyuan Lu, Zhiyu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sharing context between LLMs in a multi-model system requires the receiving model to prefill the shared prefix because KV caches are model-specific. Recent closed-form cross-model KV transfer, hereafter Full-Head Mapping, avoids this replay by fitting a training-free affine mapper from source to target caches. However, its full-head design maps each target KV head from every source KV head in the selected layers, making transfer quality sensitive to architectural differences and causing mapper storage and application cost to grow with layer support. To this end, we introduce CacheBridge, which co-designs architecture-indexed mapper support, attention-aligned calibration, and bounded mapper construction while retaining a closed-form affine interface for online deployment. CacheBridge restricts each target head to a matched source head, weights reconstruction errors by causal attention sensitivity, and uses a fused GPU kernel to construct weighted sufficient statistics without materializing full observation tensors. Across three transfer directions, CacheBridge recovers the two Ministral 3 transfer directions where Full-Head Mapping loses substantial accuracy while preserving 99.83\% mean target retention on Qwen3. On Qwen3 $14\mathrm{B}\to32\mathrm{B}$, it reduces mapper storage by $8\times$, accelerates application by up to $3.0\times$, matches \fullhead with one tenth of the calibration data, and reduces 500-sequence construction from 92.63 to 8.63 seconds ($10.7\times$).

---


### 172. [CARE: Contrastive Anchor-based Rubric Evolution for Large Language Model Post-Training](https://arxiv.org/abs/2609.00892)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Xinxin Song, Chen Ruinian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning decomposes open-ended instructions into prompt-specific, flexible rubrics, making it better suited than reinforcement learning with verifiable rewards for post-training LLMs on open-ended tasks. However, static rubrics are inevitably hacked as the policy evolves, and existing dynamic approaches introduce new problems: undirected rubric extraction, unreliable hack detection, and unbounded rubric proliferation. We propose $\textbf{CARE}$ ($\textbf{C}$ontrastive $\textbf{A}$nchor-based $\textbf{R}$ubric $\textbf{E}$volution), which grounds every rubric evolution step in a high-quality anchor response generated by a frontier model conditioned on the prompt and its rubrics. At each training step, CARE contrasts the highest-scoring rollout against the anchor, enabling two complementary mechanisms: an Adaptive branch that reactively repairs reward misspecification; and a Chase branch that proactively converts frontier-level quality gaps into sharper rubrics. Together, the two branches $\textbf{maintain discriminative accuracy in the high-reward region}$---the precise region where reward over-optimization mostly originates. Experiments on WildChecklist-9K with Qwen2.5-7B-Base and Qwen2.5-7B-Instruct show that CARE achieves state-of-the-art performance on Arena-Hard-2.0, InfoBench, and FollowBench, and is the $\textbf{only}$ method whose win rate against GPT-4.1 anchor responses shows sustained improvement throughout 300 training steps; additional results on Llama-3.1-8B-Instruct and Qwen3-8B further indicate that CARE generalizes across model families.

---


### 173. [In-Context Neurofeedback: Can LLMs Control Their Internal Representations through Privileged Access?](https://arxiv.org/abs/2609.00904)

**<font color=#1a73e8>作者：</font>** Koshiro Aoki, Ryota Takatsuki, Gouki Minegishi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether large language models (LLMs) can control their own internal representations matters for both machine metacognition and AI safety. A recent study applied neurofeedback to LLMs and claimed that they can control their internal representations. However, the reported control may rely on superficial mechanisms rather than genuine internal access because the control targets in that study are not privileged, meaning that a third party can infer them from the prompt. We redesign the neurofeedback paradigm for LLMs so that the control target satisfies the privileged access requirement, which is closer to neurofeedback experiments in human cognitive neuroscience. Under this stricter setting, the models do not demonstrate reliable control over privileged internal representations, suggesting that previously reported control cannot exclude the possibility that it relies on superficial mechanisms. Our results indicate that rigorous assessments of metacognition in LLMs require evaluation methods that demand privileged access.

---


### 174. [When Metropolis and Hastings Meet Bradley and Terry: Exact MCMC From Preference Voting](https://arxiv.org/abs/2609.00905)

**<font color=#1a73e8>作者：</font>** Ariel Smogorghevski, Nir Rosenfeld, Yaniv Romano  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from distributions conditioned on desired semantic properties is an emerging challenge in modern generative modeling. Metropolis-Hastings (MH) provides a principled route to conditional sampling, but requires access to exact pointwise target-density evaluations, which are not available in generative settings. Meanwhile, pairwise comparisons by humans or model "judge" are highly accessible and have proved valuable across diverse applications. We introduce Pref-MH, a general exact MH sampler for judge-induced conditional distributions using only stochastic binary pairwise comparisons. Our key observation is that the MH unnormalized density ratio matches the preference odds of the Bradley-Terry (BT) choice model. The central challenge is that while MH requires precise ratio computation, BT judges provide only sampled binary feedback. To this end, we develop a valid accept/reject rule whose resulting Markov chain provably converges to the target distribution. We further show that, for a fixed proposal kernel and budget, Pref-MH is optimal in the Peskun-Tierney sense among this class of exact reversible acceptance rules. Experiments on text generation and molecular design with LLM judges, as well as image generation with VLM judges, demonstrate that Pref-MH provides a practical and flexible approach to conditional sampling when comparative feedback is relatively easy to obtain.

---


### 175. [A multicenter benchmark and clinically structured metric for coronary CTA report generation](https://arxiv.org/abs/2609.00909)

**<font color=#1a73e8>作者：</font>** Zhiyu Ye, Yue Sun, Limiao Zou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of automated coronary computed tomography angiography (CCTA) report generation requires standardized multicentre benchmarks and clinically structured metrics. We established a four-centre benchmark comprising 3,021 CCTA series from 818 patient-report pairs to evaluate seven open-source three-dimensional vision-language models. We developed CSM$_{\text{CCTA}}$, a clinically structured metric for CCTA report evaluation, with patient-, vessel-, and segment-level variables defined according to clinical guidelines. Report pairs are compared at the finest shared anatomical level, and the contributions of different clinical components are weighted based on expert assessments. We estimated these weights using 70 expert-scored cases and evaluated clinical alignment in a non-overlapping set of 30 cases. CSM$_{\text{CCTA}}$ showed a strong correlation with radiologist scores (Pearson's $r=0.97$, $p<0.001$), exceeding the next-best metric, FORTE ($r=0.70$), by 0.27, and agreed with expert preferences in 115 of 160 pairwise comparisons (71.9\%). Under controlled perturbations, CSM$_{\text{CCTA}}$ remained stable to clinically equivalent wording and decreased monotonically with progressive information omission. In the multicenter benchmark, the CCTA-trained C2RG model achieved the highest CSM$_{\text{CCTA}}$ scores across all four hospitals, although its performance remained far from optimal. In contrast, CCTA-irrelevant reports accounted for up to 98.7\% of the outputs from generalist models. Together, the benchmark provides a standardized setting for model comparison, while CSM$_{\text{CCTA}}$ enables clinically structured evaluation of finding agreement and anatomical specificity. These results support a more clinically aligned and anatomically resolved approach to evaluating CCTA report generation. Code is available at this https URL.

---


### 176. [RPCBench: A Benchmark for Proactive Premise Critique in LLM-based Recommendation](https://arxiv.org/abs/2609.00918)

**<font color=#1a73e8>作者：</font>** Zhongru Chen, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as interactive recommender assistants. Their evaluation should therefore go beyond plausible item recommendation and test whether they can recognize flawed recommendation requests. Existing recommender benchmarks mainly assess ranking, generation, or preference satisfaction, while existing error-detection benchmarks are usually not grounded in recommendation-specific user and candidate evidence. To address this gap, we introduce RPCBench, a benchmark for evaluating Recommender-Premise Critique: the ability to detect, diagnose, and properly handle faulty premises in natural-language recommendation requests. RPCBench contains evidence-grounded test instances from five recommendation domains and covers ten types of premise failures. Each instance provides a visible recommendation context and a corrupted user query. We further design a fine-grained evaluation framework that measures proactive detection, error localization, post-detection handling strategy, and evidence faithfulness. Through a systematic evaluation of 11 LLMs, we find that proactive detection is the main bottleneck in Recommender-Premise Critique, and models perform worst on underspecified-premise errors. We also observe that target-critical information density matters more than redundant evidence, and that longer reasoning does not monotonically improve critique quality: performance peaks at intermediate reasoning length, while overly long reasoning is accompanied by an overthinking penalty. The code is available at this https URL.

---


### 177. [VIBE-Bench: Evaluating Personalized Large Language Models When Profiles Don't Mean Preferences](https://arxiv.org/abs/2609.00921)

**<font color=#1a73e8>作者：</font>** Yiwen Jiang, Yang Deng, Stephanie Fong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized Large Language Models (PLLMs) aim to tailor responses to individual users, where a central challenge is preference reasoning: inferring query-relevant preferences from user-related history. Existing benchmarks, however, largely assume that such preference can be retrieved from semantically related history. We study an underexplored but practically important regime, profile-preference conceptual misalignment (PRCM), where observable profile cues and query-specific preferences lie in different concept spaces, making semantic retrieval inconsistent for personalization. We introduce VIBE-Bench, a benchmark with two psychology-grounded tasks, 3,504 personas and 12,239 dialogues, including a manually verified gold test set, and requires cross-concept preference reasoning beyond surface semantic overlap. Experiments with several personalization methods show that current PLLMs largely rely on shallow semantic correlations and fail to acquire robust cross-concept mappings. These findings establish PRCM as a distinct failure regime in PLLMs and position VIBE-Bench as a focused testbed for advancing preference reasoning beyond semantic matching.

---


### 178. [Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO](https://arxiv.org/abs/2609.00925)

**<font color=#1a73e8>作者：</font>** Prakhar Gupta, Vaibhav Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models can ignore prompt evidence when it conflicts with memorized knowledge. Post-training can make models follow such evidence more reliably, but it is unclear whether these gains require new machinery or strengthen machinery already present. We compare nine post-training arms spanning GRPO, SFT, and DPO from one starting checkpoint, with key comparisons extended across scales and families. We estimate a grounding direction from that checkpoint before training. Across five tested GRPO variants, grounding gains are small. For the two variants replicated across seeds, equivalence tests bound their effects below the conflict-SFT gain even as the rewarded metric improves. Conflict-SFT improves grounding moderately, while DPO drives grounding near ceiling on its matched distribution. Conflict-SFT and DPO largely use the same causal attention-head set as the starting model. Subtracting the starting-model direction suppresses both gains, while adding it to the starting model recovers 35% of DPO's gain at a dose passing all stated side-effect checks. After a supervised warm start makes the context answer appear in more rollouts, the same GRPO recipe adds essentially no further grounding gain. In our setting, grounding gains largely depend on machinery already present in the starting model.

---


### 179. [DualStake: Dual-Path Confidence Calibration in Deep Research Agents](https://arxiv.org/abs/2609.00935)

**<font color=#1a73e8>作者：</font>** Yinuo Xu, Yuwei Liang, Jianjie Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep Research agents tackle knowledge-intensive tasks through multi-round retrieval and decision-oriented generation. However, these agents suffer from severe overconfidence, making their expressed confidence unreliable for user trust and downstream abstention. To address this, we augment the Deep Research pipeline with step confidence elicitation after each retrieval, building on the commonly used post-answer verbalized confidence. Interestingly, we find that Evidence Confidence (E-Conf), elicited after the final retrieval step, provides a stronger uncertainty signal than Answer Confidence (A-Conf), elicited after answer generation, and that A-Conf is largely shaped by E-Conf. Based on these findings, we propose DualStake, a dual-path calibration method that applies margin-clipped, confidence-dependent stake rewards to jointly align E-Conf and A-Conf with answer correctness while limiting extreme confidence optimization. Experiments on Qwen2.5-7B, Qwen2.5-7B-Instruct, and Qwen3-4B across 8 QA benchmarks demonstrate that DualStake consistently improves calibration without sacrificing answer accuracy. The code is available at this https URL.

---


### 180. [A Dataset for Modeling Iterative Problem-Solving](https://arxiv.org/abs/2609.00940)

**<font color=#1a73e8>作者：</font>** Fagun Patel, Sang T. Truong, Duc Q. Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Solving problems through repeated attempts is a sequential modeling task: at each step, the solver receives feedback and decides how to revise their solutions. Predicting whether performance improves, plateaus, or regresses across attempts is central to understanding any iterative problem-solving process in both human learners and autonomous agents. Beyond outcomes, modeling what errors persist and how strategies shift across attempts provides deeper insight into the mechanics of sequential learning. Studying these dynamics requires observing many solvers as they attempt, receive feedback, and revise. Programming courses with automated grading provide this setting, as students iteratively submit code to test suites and receive feedback on every attempt. We therefore curate CodeInsight, a large-scale dataset of over 3 million submissions from 3,286 undergraduates across 2 introductory C++ courses in 2 academic years, with test-case-level outcomes, timestamps, and source code. On this dataset, we build a benchmark that evaluates models spanning parametric, sequential, and generative traditions under a shared calibration-and-scoring protocol, including a Recurrent State Space Model (RSSM) adapted to track solver characteristics through discrete latent variables and an LLM-based predictor that generates explicit solutions. The adapted RSSM achieves the strongest predictive accuracy on three of the four courses. The LLM predictor is less accurate but produces full submissions at each attempt, enabling direct analysis of failure modes. We find that the model's coding proficiency is inversely related to predictive performance in this setting, with the LLM better understood as a generative solver conditioned on context rather than a faithful predictor of solver behavior. We publicly release our code and the dataset on request to facilitate future research.

---


### 181. [From Terminology to Diagrams: Visual-Instruction Generation for Scientific Diagram Understanding](https://arxiv.org/abs/2609.00948)

**<font color=#1a73e8>作者：</font>** Raul Ortega, José Manuel Gómez-Pérez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated strong performance in visual question answering with natural images. However, they continue to struggle with scientific diagrams, which are designed to convey functional or relational meaning rather than literal scenes. We therefore introduce a framework for generating large-scale diagram-grounded instruction data by leveraging terminology derived from scientific curricula. Our approach systematically extracts domain concepts, synthesizes atomic facts, retrieves relevant diagrams from the web, and generates multimodal supervision in the form of diagram captions and multiple-choice questions. Using this pipeline, we construct SciGram, a dataset of over 194K diagrams and 1.4M visual instructions across life, earth, and physical sciences. Despite relying on noisy web data and synthetic annotations, models fine-tuned on SciGram achieve substantial improvements on diagram-centric benchmarks, including TQA, ScienceQA, and AI2D, outperforming or matching state-of-the-art VLMs while using fewer training instances. Furthermore, augmenting existing models such as LLaVA OneVision with SciGram establishes new state-of-the-art performance on diagram question answering. Our results highlight the effectiveness of terminology-grounded instruction generation as a general strategy for improving vision-language reasoning in scientific domains. To support future research in scientific diagram understanding, we release both the SciGram dataset and models.

---


### 182. [Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling](https://arxiv.org/abs/2609.00949)

**<font color=#1a73e8>作者：</font>** Kangjia Zhao, Jiajun Li, Haozhan Shen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn tool calling is a core evaluation scenario for large language model (LLM) agents. On public tool-calling benchmarks, open-weight models now approach or even surpass closed-source frontier models in aggregate accuracy. However, this metric averages over many different multi-turn situations and obscures whether progress is balanced across them. We propose an action-class-oriented diagnostic framework that decomposes multi-turn failures into two orthogonal modes: action-class miscalibration and action-execution failure. The framework operates over a four-class action space (TOOL_CALL/ASK/REFUSE/CONFIRM) and introduces a self-revealing upper bound Acc <= GAR (Gold Action Recall); the two modes show up as bound violation (Acc > GAR, exposing state-grader masking of miscalibration) and large bound slack (GAR >> Acc, localizing execution failure within TOOL_CALL). We validate it on a panel of tool-calling models across multiple multi-turn benchmarks. Across our panel, the diagnostic reveals action-class miscalibration as a substantial failure mode the state grader cannot see. This gap inflates standing for heavily tool-trained families, which our diagnostic separates from families with context-appropriate action choice. Calibration is reshapable through context-only perturbations, but the reshape is heterogeneous: a single perturbation moves accuracy in opposite directions across families (up to +11.5 vs -21.0 pp on the same scenario), and its effect further depends on the perturbation mechanism. We argue that multi-turn tool-calling evaluations should supplement aggregate accuracy with action-class diagnostics that expose what the model actually does in each scenario.

---


### 183. [PersianAnonymizer: Evaluating LLM-Labeled Training for Efficient NER-based Anonymization in Persian](https://arxiv.org/abs/2609.00958)

**<font color=#1a73e8>作者：</font>** Mohammad Hossein Shalchian, Mostafa Amiri, Amir Mahdi Sadeghzadeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We target practical anonymization of Persian customer chats by training a compact NER model from LLM-labeled supervision and selecting the best labeler for deployment. We compare three instruction-tuned LLMs: DeepSeek-V3-0324, GPT-OSS-120B, and Qwen3-235B-A22B-Instruct-2507, to produce span annotations under a shared JSON protocol, yielding four corpora (OSS_ZeroShot, Qwen_ZeroShot, Qwen_FewShot, DeepSeek_FewShot). A MatinaRoberta-based token-classifier is trained per corpus and evaluated with token-level Precision/Recall/F1 (overall and per-class). We also report Label Coverage Recall (LCR), the proportion of gold non-O tokens predicted as non-O, and quantify cross-labeler behavior via a token-level Venn on test annotations. Finally, we contrast test-set annotation latency of the LLMs on H200 nodes with the trained NER's test-time labeling on a single RTX 3090. Results show that supervision from OSS_ZeroShot yields the strongest macro-F1 and LCR, while the resulting NER labels an entire 40K-message test set in approximately 2 minutes on one consumer GPU. This establishes a practical path to high-quality, low-cost anonymization for Persian industrial data.

---


### 184. [CoBRA: Learning Tool-Use Boundaries via Counterfactual Margins](https://arxiv.org/abs/2609.00967)

**<font color=#1a73e8>作者：</font>** Wenhao Zou, Xianglong Liu, Wendong Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models increasingly act through external tools, deciding when to call a tool has become a central problem alongside deciding how to use it. Unnecessary tool calls introduce latency, cost, retrieval noise, and error propagation, while missed calls hurt knowledge-intensive queries or questions requiring up-to-date evidence. Existing methods typically trigger tools from absolute query or generation signals, such as difficulty, confidence, or final task reward, and therefore lack an explicit estimate of the instance-level marginal benefit of tool use. We propose CoBRA, a counterfactual boundary-learning framework for tool-augmented language models. CoBRA first constructs internal and external experts from the same base model, collects paired trajectories, and estimates the reward margin between answering with and without tools. This margin partitions data into internal-favored, external-favored, and ambiguous cases. CoBRA then uses clear-margin samples for Boundary-Aware Cold-Start SFT, followed by MARS-RL with reference-split rollouts and counterfactual marginal advantages to optimize boundary decisions. Experiments with retrieval as the main tool on Qwen3-4B show that CoBRA improves tool-use efficiency and boundary-sensitive answer accuracy while maintaining strong performance on tool-dependent out-of-distribution questions.

---


### 185. [Disclosure-Gated User Simulation for Companion-Agent Evaluation](https://arxiv.org/abs/2609.00982)

**<font color=#1a73e8>作者：</font>** Yao Liu, Yu He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Using a large language model to play the user is now standard in scalable evaluation. It has a repeatedly diagnosed failure: the simulated user is excessively cooperative, so a system under test can score by the sheer number of questions it asks rather than by making the user willing to speak. We answer with a disclosure gate conditioning information release on the companion agent's behaviour: its state is a ladder of five ordered gates, merged onto three observable depth layers. We specify, ablate, and audit it, and train a user simulator against that specification. Gating behaviour is learned from the training corpus's synthetic branch, while the real branch supplies how people speak and react; after training, the simulator need not be told at runtime which gate each item sits behind. The gate is a load-bearing component of the environment: on the English corpus of a published companion-agent benchmark (CompanionBench), once training no longer states per example which gate each item sits behind, the largest rank displacement across 12 systems under test exceeds the noise band set by re-running that environment under a new seed, while per-system scores show no detectable change. We state two acceptance criteria: a ranking must be order-preserving, and absolute scores must be scale-stable. Of the candidates we examine, only one passes both -- the simulator we release -- and its leaderboard correlates at 0.993 with the benchmark's original simulator. By contrast, prompting a frontier model as the simulator barely moves the ranking while shifting every score upward -- a shift invisible to anyone checking the ranking alone. The environment we specify is the one that benchmark already used. That publication describes the mechanism in about four hundred words, and we supply what it lacked: specification, ablations, human studies, negative controls, and downstream sensitivity analysis.

---


### 186. [Inspicio: Open-Vocabulary, LLM-Based Sense Retrieval for Historical Languages](https://arxiv.org/abs/2609.00998)

**<font color=#1a73e8>作者：</font>** Michele Ciletti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Word Sense Disambiguation has advanced rapidly for English and a handful of well-resourced modern languages, but it continues to assume the existence of a sense inventory and a word-to-sense mapping in the source language (Navigli, 2026). These assumptions break down for most historical and low-resource languages, whose dedicated WordNets are either incomplete or still under construction. We present Inspicio, an open-vocabulary retrieval pipeline that links tokens in context to synsets of the Open English WordNet (McCrae et al., 2020) without requiring any source-language inventory or mapping. For each occurrence, an instruction-tuned LLM produces two English translations of the surrounding sentence, a small set of candidate dictionary-style definitions, and a few candidate English lemmas. These outputs drive a hybrid retrieval step that combines dense definition-synset similarity, sparse lemma matching, and Maximal Marginal Relevance re-ranking. We evaluate the pipeline across a 6x6 grid of LLMs and sentence-embedding models on a new bilingual set of manually annotated Latin and Ancient Greek perception verbs, on a subset of PREMOVE dataset (Farina, 2025), and on a diachronic sample of Italian. The best configuration reaches 96% Recall@50 on the perception-verb test set, with each component contributing measurable gains, and remains competitive in the out-of-domain and cross-lingual settings.

---


### 187. [Right Frame, Wrong Rule: Cultural Cues Expose the Financial Knowledge Gap They Were Meant to Close](https://arxiv.org/abs/2609.00999)

**<font color=#1a73e8>作者：</font>** Rania Elbadry, Ahmed Heakl, Saeed Almheiri 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a question has valid answers under different normative frameworks, a language model must decide which framework to use and whether it can answer correctly within it. We call this setting normative pluralism and study it in Islamic finance using a four-choice taxonomy that separates framework selection from within-framework correctness. This separation reveals the stereotype trap: a cultural cue steers a model toward one framework, but the model selects an incorrect answer within that framework. Across twelve models, two languages, and fifty demographic signals, cultural cues change framework selection and reveal substantial differences in accuracy, especially among non-frontier models. Under the strongest signal, large open-weight models select the Islamic framework 97% of the time. A two-choice evaluation would report near-perfect alignment, although 57--66% of those selections are incorrect. These findings motivate, but do not directly test, the competence-conditioned routing hypothesis: models may favor frameworks where they are more accurate, while cultural cues may expose framework-specific competence gaps.

---


### 188. [SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models](https://arxiv.org/abs/2609.01004)

**<font color=#1a73e8>作者：</font>** Shiyu Li, Zi-Yuan Hu, Shijia Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite their strong multimodal understanding ability, multimodal large language models (MLLMs) incur substantial computational overhead when processing long visual token sequences. To reduce inference costs, recent studies have explored visual token pruning through vision-centric or text-guided strategies. However, these methods often overlook high-norm outlier tokens, i.e., tokens with abnormally large feature norms, leading to suboptimal pruning decisions. In this work, we show that such high-norm outlier tokens are highly redundant in both feature and spatial dimensions, yet are often mistakenly preserved as informative cues by existing methods.
Motivated by this observation, we propose SinkPruner, a training-free visual token pruning framework for efficient MLLM inference. SinkPruner follows a coarse-to-fine design with two key modules: a visual sanitizer that filters high-norm redundancies and alleviates attention sink and attention dispersion, and a text-guided pruner that further retains tokens semantically aligned with the text query.
Extensive experiments on twelve image-language and four video-language benchmarks demonstrate the effectiveness, efficiency, and generalizability of our framework. Notably, SinkPruner preserves 96.5% (91.8%) of the original performance of LLaVA-1.5 (Qwen2.5-VL) under an 89% token reduction. Experiments further indicate that our visual sanitizer exhibits promising transferability in enhancing the performance of existing pruning methods. Our code is available at this https URL.

---


### 189. [PCoMoE: Shifting MoE Inference from Monolithic Expert Selection to Fine-Grained Path Composition](https://arxiv.org/abs/2609.01024)

**<font color=#1a73e8>作者：</font>** Ziyan Gan, Fangxin Liu, Chenyang Guan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures scale Large Language Model (LLM) capacity efficiently by activating a sparse subset of experts per token. However, modern MoE inference remains heavily constrained by the rigid, whole-expert abstraction. Existing frameworks manage, schedule, or prune experts as atomic execution units, which fixes the optimization boundary too early and leaves fine-grained intra-expert computational redundancy underexplored. In this work, we present PCoMoE, a path-compositional execution framework that shifts MoE inference from coarse-grained expert selection to fine-grained path composition. PCoMoE incorporates a path-level formulation of expert computation, a compatibility-aware layer-wise pruning strategy to suppress low-value path combinations, and a hardware-friendly execution engine to exploit reusable sub-expert structures under strictly bounded overheads. Experimental results demonstrate that PCoMoE achieves up to a 1.31x end-to-end inference speedup while enhancing model accuracy by 10%. The code is available at this https URL

---


### 190. [Fi-ImageNet-1k: An OOD Benchmark From the Inside of the ImageNet-1k Validation Set](https://arxiv.org/abs/2609.01027)

**<font color=#1a73e8>作者：</font>** Ruslan Rozumnyi, Matěj Suchánek, Tomáš Vojíř 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection predicts whether a test image belongs to none of the predefined classes. To evaluate this task, benchmarks need images from outside the in-distribution (ID) data; typically, these are defined or collected in an ad hoc fashion. Since no ground truth is perfect, ID-labeled datasets themselves contain a natural source of OOD images. We exploit such annotation errors and present Fi-ImageNet-1k, an OOD dataset built from ImageNet-1k validation images that the recent ReImageNet reannotation effort assigned to no ImageNet-1k class. Each image was examined by expert human annotators supported by evidence from MLLMs, VLMs, and reverse image search, comparing it against all visually similar ID classes. We keep only images that could be assigned a specific class outside the ImageNet-1k label space.
The resulting Fi-ImageNet-1k, with 655 images from 522 classes, is substantially more challenging than any commonly used OOD dataset. No evaluated combination of classifier and OOD detector achieves a false positive rate below 51% at 95% true positive rate (FPR@95). Compared to the recent NINCO, our dataset is 3.8x more challenging in the FPR@95 metric for state-of-the-art supervised OOD detection methods.

---


### 191. [Spawn Freely, Act Sparingly: Progressive Risk Vesting for Recursive LLM-Agent Trees](https://arxiv.org/abs/2609.01035)

**<font color=#1a73e8>作者：</font>** Molly Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive LLM agents can broaden their search by spawning specialists. Some branches later request tools that send data or deploy code. When should a branch receive authority to act? We distinguish sandbox spawning, in which external controls prevent the specified harm, from capability activation, in which a selected branch crosses an irreversible-action boundary. Progressive Risk Vesting (PRV) holds a trajectory-level risk budget in escrow and debits it as branches are activated. We prove an anytime harm bound for adaptively generated trees. Branch outcomes may be dependent, but each local certificate needs to remain valid conditional on the full pre-activation history, including the information used to select the request. When activation gates, branch charges, and compute constraints are held fixed, delayed vesting preserves every policy available under irrevocable spawn charging. Marginal risk estimates can still fail after branch selection. In a stylized branching model, trajectory harm changes as the authority reproduction number $\mathcal{R}_A$ crosses one. As local risk $p$ approaches zero, trajectory harm is proportional to $p$ below criticality, proportional to $\sqrt{p}$ at criticality, and retains a positive floor above it. A finite-type occupancy model yields risk and compute shadow prices. For nested fanout modes with decreasing marginal value per unit risk, these prices produce a threshold rule. Branching calculations and a split-sample experiment illustrate the results. These synthetic studies do not estimate safety in deployed agents. The analysis suggests a design rule: search broadly in the sandbox and grant recursive authority sparingly, with an explicit risk charge.

---


### 192. [Data-Driven Persona-Conditioned Agents for A/B Test Simulation](https://arxiv.org/abs/2609.01038)

**<font color=#1a73e8>作者：</font>** Ziyad Benomar, Weronika Łajewska, Leonardo Perelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A/B testing is the gold standard for evaluating product changes, but each experiment requires real user traffic, engineering effort, and weeks of measurement. We propose a simulation framework that predicts A/B test outcomes using LLM-powered agents conditioned on data-driven personas grounded in real user behavioral signals. Unlike prior work that relies on synthetic or rule-based personas, our agents are constructed from anonymized behavioral data-activity patterns, engagement signals, and inferred demographics-enabling more faithful population modeling. We frame A/B test simulation as a structured question task and systematically study (i) question design formats, (ii) the impact of persona data source and domain alignment, (iii) the trade-off between per-persona behavioral depth and population diversity, and (iv) efficient population subsampling. On a benchmark of 40 A/B tests spanning two metric types, our best configuration achieves 0.75-0.90 directional accuracy depending on the test metric, demonstrating that data-driven personas are a viable path toward fast, low-cost experiment pre-screening.

---


### 193. [AgentFactory: Towards Automated Agentic System Design and Optimization](https://arxiv.org/abs/2609.01045)

**<font color=#1a73e8>作者：</font>** Enci Zhang, Haofeng Wang, Yuesheng Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities as powerful components in agentic systems, enabling sophisticated reasoning and complex task execution. However, current approaches to manually designing and optimizing agentic systems heavily rely on manual effort, limiting their adaptability and scalability. Recent work has explored the automated optimization of workflow designs. However, these approaches often overlook the crucial role of model capabilities and focus on single performance metrics, failing to address real-world deployment constraints. In this paper, we present AgentFactory, a framework that jointly optimizes both foundation models and workflow structures in agentic systems while considering multiple objectives including performance, cost, and efficiency. AgentFactory leverages advanced LLMs as optimizers to navigate the vast search space of possible configurations, employing a three-stage optimization pipeline to automatically discover effective combinations of fine-tuned models and optimized workflows. Through an iterative optimization process, our framework systematically explores and evaluates different agentic system designs, adapting to task-specific requirements while maintaining operational efficiency. We evaluate AgentFactory across eight benchmarks spanning five domains, including general reasoning, coding, mathematics, medicine, and finance. Our experiments demonstrate that AgentFactory consistently outperforms both manually designed methods and existing automated approaches, achieving an average improvement of 9.1% across all benchmarks, with particularly significant gains in domain-specific tasks (19.6% on MedQA and 18.7% on FinEval). These results establish AgentFactory as a promising approach for developing more capable and efficient agentic systems through automated optimization.

---


### 194. [WorldBench: Culturally Grounded Benchmark for Multilingual Agents](https://arxiv.org/abs/2609.01056)

**<font color=#1a73e8>作者：</font>** Leonardo Ranaldi, Sherrie Shen, Jushi Kai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the growing use of LLM-powered agents to solve multi-step tasks in complex environments, existing benchmarks rarely test state preservation, performance across languages, and application to realistic, grounded scenarios. To address these concerns, we present WorldBench: a comprehensive, multilingual benchmark of genuine, persona-grounded everyday workflows, where agents can act in a sandbox via structured actions. WorldBench comprises 1,600 tasks across seven languages and eight cultures, filtered and refined through feedback from human annotators with language- and culture-specific expertise. For evaluation, we extend metrics from previous works and introduce Constrained Task Success (CTS), which combines natural language instructions and testbeds to score task completion, minimal modification, and other complementary metrics through deterministic and LLM-as-a-Judge evaluations. Our experiments show that frontier models reach only 49.2% CTS, with all models demonstrating large gaps between correctness and environment preservation. We thereby show that current agents remain brittle in multilingual, agentic scenarios, especially for long-horizon tasks and under state-preservation constraints

---


### 195. [Dyn-3D: Unveiling and Resolving Ego-Motion Ambiguity in Vision-Language Models](https://arxiv.org/abs/2609.01059)

**<font color=#1a73e8>作者：</font>** Jiayu Ding, Zhuodong Liu, Lei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Vision-Language Models (VLMs) tackle dynamic 3D spatial reasoning, ego-motion perception becomes essential to resolve monocular scale ambiguity. However, current models often overfit to smooth trajectory priors rather than genuinely understanding physical motion. Consequently, their spatial reasoning degrades severely under large displacements, a phenomenon we term Kinematic Collapse. This failure stems from spurious visual-motion correlations in natural videos and a lack of explicit physical supervision. To evaluate this, we introduce Dyn-3D, a benchmark using counterfactual 3D rendering to rigorously decouple visual changes from true kinematic properties. Furthermore, we propose the TempoVista framework, featuring the Kinematic-GSPO algorithm. By embedding metric physical ground truth into policy optimization, TempoVista explicitly grounds visual representations in 3D space. Experiments demonstrate that our approach significantly improves both motion estimation and robust spatial reasoning by utilizing camera dynamics as an effective geometric calibration signal.

---


### 196. [Space Generative AI with Solar Energy Harvesting](https://arxiv.org/abs/2609.01062)

**<font color=#1a73e8>作者：</font>** Jierui Zhang, Jianhao Huang, Zhanwei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Satellites are emerging as promising platforms to extend generative \emph{artificial intelligence} (AI) services to remote areas lacking terrestrial infrastructure. However, deploying space generative AI is fundamentally constrained by the limited, time-varying onboard energy supplied by solar \emph{energy harvesting} (EH). This paper presents a framework for solar-powered space generative AI in which a satellite receives a user prompt, executes a diffusion-based image-generation model, and downlinks the compressed result within a strict time window. We identify the fundamental \emph{computation--communication} (C$^2$) trade-offs governed by the shared harvested-energy budgets. Specifically, increasing the number of generation steps improves intrinsic image quality but depletes energy and time available for downlink transmission, whereas prioritizing communication guarantees reliable delivery but sacrifices semantic quality. To balance these trade-offs and maximize \emph{end-to-end} (E2E) generative performance, we exploit the predictable solar-EH dynamics induced by deterministic orbital motion and develop a joint C$^2$ resource-optimization framework using a tractable two-step approach. First, we characterize the maximum downlink throughput for a fixed generation depth under continuous solar EH. This establishes a separation principle that decouples waiting-time selection from optimal transmit-power control. Next, we formulate a joint C$^2$ utility-maximization problem and derive a closed-form, low-complexity step-selection policy in the dominant constant-power regime. Extensive experiments under realistic orbital dynamics demonstrate that the proposed policy dynamically balances generation quality and transmission reliability. This yields significant E2E performance gains over static computation- and communication-centric baselines across diverse solar-EH states.

---


### 197. [OUTLETS: Output-Length Prediction from Speculative Decoding Backbones](https://arxiv.org/abs/2609.01068)

**<font color=#1a73e8>作者：</font>** Weihuang Wen, Yingying Liu, Yichuan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The heavy-tailed distribution of output lengths in Large Language Model (LLM) serving poses major challenges for resource provisioning and cluster scheduling. Although output-length prediction can mitigate these issues, existing approaches have key drawbacks: external proxy models add substantial latency and often have limited fidelity, whereas internal state-based methods are efficient but rely on shallow probes of current model states. We identify a structural connection between speculative decoding (SD) and length prediction: latent representations produced by the draft decoder in advanced frameworks (e.g., EAGLE-3) encode signals that are predictive of generation length. Building on this insight, we introduce OUTLETS (Output-Length Prediction from Speculative Decoding Backbones), which repurposes the speculative backbone as a trajectory-aware length predictor. When its draft representations are already computed for speculative decoding, OUTLETS adds only a lightweight regression head and achieves lower MAE than the evaluated methods. Under saturated disaggregated serving, OUTLETS predictions enable standard scheduling policies to prioritize shorter requests and distribute requests more evenly across decoding instances, reducing short-request P99 latency by 34.8%.

---


### 198. [Post-hoc Alignment of LLM-judges to Human Judgment Distribution](https://arxiv.org/abs/2609.01073)

**<font color=#1a73e8>作者：</font>** Sebastian Steindl, Nikos Voskarides, Alberto Gasparin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The LLM-as-a-judge (LLMaJ) framework offers a cost-effective and reproducible solution for automatic evaluation. However, current evaluation practices typically compare LLMaJ judgments against aggregated ground-truth labels, overlooking the valuable information contained in Human Label Variation (HLV). Inspired by an increasing line of work that proposes to leverage HLV, we systematically study LLMaJ performance on predicting both a single, aggregated ground truth hard-label and unaggregated soft-labels that represent Human Judgment Distributions (HJD). Our results across five diverse datasets reveal that while LLMs achieve near human-level performance at hard-label prediction on most tasks, they exhibit poor performance when predicting soft-labels. To address this limitation, we propose NAPHA (eNtropy-Aware Post-Hoc Alignment), a simple yet effective lightweight post-hoc alignment method that matches the LLM distribution to the HJD by first assigning an instance to a discrete entropy class and then routing it to specialized, trained alignment models. We find that NAPHA consistently improves soft-labels prediction across base LLM models and datasets, with particularly strong gains on high-entropy instances where capturing diverse human perspectives is most critical. We also show via oracle experiments that improving entropy class prediction can substantially enhance NAPHA's practical effectiveness.

---


### 199. [StateSwap: Probing Support-Elimination Hidden States in Multiple-Choice Questions](https://arxiv.org/abs/2609.01081)

**<font color=#1a73e8>作者：</font>** Chao Gao, Haijiang Liu, Qiyuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often answer the same multiple-choice question inconsistently when it is posed under support-oriented and elimination-oriented framings. We investigate whether these discrepancies arise from different internal representations induced by the two framings. We introduce a dual-framing protocol with minimally varied prompts that use either support- or elimination-oriented framing while keeping the evaluation target fixed. To probe the internal computation, we append an untrained special token, [STATE], and treat its residual-stream activation as an intervention interface. Across both models, the two framings induce separable [STATE] activations concentrated in intermediate layers. Swapping these activations between paired prompts systematically changes predictions and improves cross-framing agreement, providing intervention-based evidence that the activations are behaviorally relevant. Beyond instance-level substitution, mean-difference steering directions derived from the dual-framing contrast exhibit more bounded layer-wise responses than matched contrastive activation addition directions under the evaluated protocol.

---


### 200. [Modelpedia: A Catalog of Model Findings for the Meta-Science of AI](https://arxiv.org/abs/2609.01090)

**<font color=#1a73e8>作者：</font>** Franciszek Bernat, Dawid Płudowski, Michał Jan Włodarczyk 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific knowledge about AI models is produced faster than the community can organize it. Every few months a new foundation model reshapes the field and hundreds of papers, blogs, and technical reports document how each behaves or fails. Yet, these findings remain scattered and effectively unretrievable. To address this gap we present Modelpedia, an automated, LLM-assisted framework that extracts findings about models from published papers, links it to the model, dataset, method, and concept it concerns, and aggregates the result into a searchable public catalog. Applying the prototype to accepted ICLR 2024 and 2025 papers, we extract over a thousand findings and, treating the catalog itself as an object of study, run a meta-analysis of how the community investigates models. Now, we invite the community to explore, contribute to, and build on the open catalog, and to help establish model findings as a shared foundation for the meta-science of AI.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-295](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
