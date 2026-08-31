# 🔐 大模型安全相关研究 | 2026年09月01日

> 本类共 **10** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [ROPE: Routed Origin Policy Enforcement against Indirect Prompt Injection](https://arxiv.org/abs/2608.27496)

**<font color=#1a73e8>作者：</font>** Xinhang Ma, Chaowei Xiao, William Yeoh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection (IPI) plants instructions in the content a tool-using LLM agent reads, steering the agent into harmful tool calls. The strongest defenses are system-level, leveraging techniques such as task-conditional tool screening to prevent execution of malicious tools, and information-flow control to avoid tool execution with untrusted parameters. However, as agents grow more capable, users delegate more to automation. Consequently, tool execution sequences and parameter values are increasingly determined at runtime and cannot be reliably screened from solely user's query without significant utility loss. We present ROPE (Routed Origin Policy Enforcement), which is anchored in a structural notion of trust: a value may reach a state-changing tool only if it traces unforgeably to the user, a source the user explicitly named, or the user's own authoritative records. Enforcement is then a deterministic origin check over an audited set of sensitive tool parameters, and the only reliance on a language model involves solely the trusted user request, out of the attacker's reach. Our approach admits two provable guarantees: 1) at every step of a trajectory, no value whose only origin is attacker-writable content reaches an origin-guarded parameter, and 2) no rewording of an injection changes an admission decision. We evaluate across four agent models on open-ended agent suites, ROPE holds attack success rate to 1.6--2.6\% while retaining 82--100\% of undefended clean utility, significantly exceeding state-of-the-art system-level defenses in utility while attaining comparable or better security. Further, we show that optimizing the injection against ROPE is largely ineffective, while long-horizon attacks that defeat prior system-level defenses achieve zero success rate. Our code and logs are available at this https URL .

---


### 2. [Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study](https://arxiv.org/abs/2608.27504)

**<font color=#1a73e8>作者：</font>** Paria Mehrbod, Boris Knyazev, Guy Wolf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite extensive safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safeguards to elicit harmful content. While prior work attributes this vulnerability to safety training limitations, the internal mechanisms by which LLMs process adversarial prompts remain poorly understood. We present a mechanistic analysis of the jailbreaking behavior in a large-scale, safety-aligned LLM, focusing on LLaMA-2-7B-chat-hf. Leveraging edge attribution patching and subnetwork probing, we systematically identify computational circuits responsible for generating affirmative responses to jailbreak prompts. Ablating these circuits during the first token prediction can reduce attack success rates by up to 80\%, demonstrating its critical role in safety bypass. Our analysis uncovers key attention heads and MLP pathways that mediate adversarial prompt exploitation, revealing how important tokens propagate through these components to override safety constraints. These findings advance the understanding of adversarial vulnerabilities in aligned LLMs and pave the way for targeted, interpretable defense mechanisms based on mechanistic interpretability.

---


### 3. [Quantization-Triggered Backdoors in Language Models: Cross-Quantizer Transferability and the Validation--Deployment Gap](https://arxiv.org/abs/2608.27512)

**<font color=#1a73e8>作者：</font>** Jacopo Dardini, Claudio Stanzione, Giordano Colò 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization is often treated as a semantically neutral optimization for edge deployment of Large Language Models. When a full-precision source checkpoint is evaluated and quantization is applied downstream without equivalent re-evaluation, this workflow creates a structural validation--deployment gap: because quantization is a many-to-one mapping over parameter space, source-precision certification does not guarantee behavioral equivalence in the deployed configuration. We formalize this gap through Quantization Behavioral Equivalence Classes (QBECs) and prove that QBEC membership does not imply behavioral equivalence, providing a theoretical basis for quantization-triggered backdoor attacks. Building on a three-stage adversarial fine-tuning framework, we embed latent malicious payloads into models that satisfy the source-precision checks used in our evaluation, yet activate targeted adversarial behavior upon INT8 or 4-bit compression. We evaluate this threat in two operationally motivated scenarios, tactical machine translation and political content analysis, extending prior work from decoder-only causal LMs to multilingual encoder-decoder sequence-to-sequence models. Results show that backdoored translation models move from zero measured friend--foe corruption at repaired FP16 to up to 85.02% inversion after quantization, and that a paired stance classifier measures an ideological shift of up to $\Delta\mathrm{Bias}=0.33$ upon compression. A cross-quantizer transferability analysis further shows that attack persistence varies across quantization schemes and model architectures, rather than being determined by nominal bit-width alone. These findings demonstrate that source-precision auditing alone does not rule out quantization-triggered behavior and that the final deployed configuration must be included in behavioral certification for trustworthy edge AI.

---


### 4. [Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator](https://arxiv.org/abs/2608.27548)

**<font color=#1a73e8>作者：</font>** Varun Singh, Anuj Doshi, Makesh Narsimhan Sreedhar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.

---


### 5. [LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails](https://arxiv.org/abs/2608.27580)

**<font color=#1a73e8>作者：</font>** Ziyang Chen, Xing Wu, Songlin Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety guardrails serve as the last line of defense against harmful inputs and outputs of large language models (LLMs), yet they are trained and evaluated almost exclusively on short text. We present LongGuard, a framework that evaluates, mechanistically analyzes, and mitigates long-context guardrail failure. We formulate the task as Safety Needle-in-a-Haystack (SafetyNIAH) over a 0.25k-32k length grid; across 15 mainstream guardrails, unsafe recall drops monotonically by more than 50% on average, and a paired Benign-Fill vs. Needle-Repeat design attributes the failure to proportional dilution of the unsafe needle rather than to absolute length. A three-layer attention-logit-behavior analysis on six guardrails locates the mechanism: attention mass on the unsafe needle is diluted, the unsafe-over-safe logit margin is compressed in lockstep, and the detection decision collapses accordingly, with this attention->logit->behavior chain remaining consistent after partialling out length. We further isolate a sparse set of guard-specialized retrieval heads that exhibit partial specificity relative to their base models. Building on the analysis, we propose two training-free mitigations - Chunked Detection (CD) and Attention-Head Sharpening (AHS) - and a deployment protocol, Context-Aware Hyperparameter Routing (CAHR), that selects configurations by context length and audit side. Across five benchmarks spanning synthetic data, long-context attacks, and reasoning-model outputs, CAHR-CD and CAHR-AHS improve the six-guardrail average by 22% and 13%, respectively. Code and data are available online.

---


### 6. [FISGuard: Defending Against Membership Inference via Fixed Input Subspaces](https://arxiv.org/abs/2608.27836)

**<font color=#1a73e8>作者：</font>** Haocheng Jiang, Hua Shen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly adopted in federated learning, protecting user privacy while performing parameter-efficient fine-tuning on distributed private data has become an important challenge. Although clients only share gradients instead of directly uploading raw data, the shared gradients may still leak membership information about training samples. ProjRes (S&P, 2026) further increases this risk: with less information and without accessing model outputs, an attacker can effectively distinguish members from non-members solely based on the projection residual between a candidate representation and the subspace induced by server-observable gradients. Existing defenses against membership inference mostly rely on gradient perturbation or regularization, which can not only degrade model utility but also fail to effectively defend against the membership inference attack introduced by ProjRes, which exploits the geometric structure of gradients.
To address this issue, we propose FISGuard, a lightweight defense. Its key idea is to construct and fix a low-dimensional representation subspace using independent public data, thereby restricting the space through which private representations are exposed via gradients while preserving the primary information required for downstream tasks. This substantially reduces the projection-residual discrepancy between members and non-members.
We evaluate FISGuard against five representative defense methods across three NLP datasets, two LLMs, and two fine-tuning strategies, Adapter and LoRA. The results show that FISGuard reduces the ProjRes attack AUC to near the random-guessing level of 0.5 in most settings, while maintaining downstream task performance close to that of the undefended model and introducing only limited computational overhead, thereby achieving a favorable privacy--utility trade-off.

---


### 7. [EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses](https://arxiv.org/abs/2608.28363)

**<font color=#1a73e8>作者：</font>** Tanmay Sah, Dolly Sah, Harshul Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly modify their own prompts, tools, middleware, resources, and execution harnesses at runtime. Such self-evolution can improve capability, but a successful mutation may leave persistent effects that cannot be safely reversed in states different from the one in which it was created. We introduce EvoUndo, a framework for representing, synthesizing, diagnosing, and independently verifying recoverability of model-generated self-modifications across counterfactual states. Across 600 unseen one-shot self-evolution tasks, we identify 197 capability-improving mutations that fail recoverability verification. Under the original recovery representation, conventional repair strategies recover 0/197 of these natural failures. Deterministic oracle analysis recovers 48/197 under the original recovery language L0, while the extended recovery calculus increases empirical oracle recovery to 191/197. A protocol-locked 2x2 grounding-by-expressivity intervention then separates two bottlenecks: exact state-address grounding increases successful recovery from 0/48 to 38/48 (79.2%) when the original language is sufficient, while extending the recovery language enables recovery on 142/143 (99.3%) failures in the oracle-defined S1 stratum. On the primary gpt-oss-120b backbone, adding exact-address diagnostics to the richer language reduces recovery to 133/143 (93.0%); a Qwen3.8-27B replication preserves the grounding and expressivity effects but not this negative interaction, indicating that the latter is model-dependent. These results indicate that reliable agent self-evolution requires co-designing verification, state grounding, witness semantics, and recovery-language expressivity rather than relying on iterative prompting alone.

---


### 8. [CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents](https://arxiv.org/abs/2608.28389)

**<font color=#1a73e8>作者：</font>** Jaewon Jung, Haizhong Zheng, Hongsun Jang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at this https URL.

---


### 9. [LongPIBench: A Long-Context Benchmark for Prompt Injection](https://arxiv.org/abs/2608.28411)

**<font color=#1a73e8>作者：</font>** Yupei Liu, Yuqi Jia, Neil Zhenqiang Gong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection attacks pose a serious security risk to large language models in real-world applications. However, existing prompt injection benchmarks primarily focus on short-context inputs, leaving the attacks and defenses in long-context settings largely unexplored. This gap leads to a substantial overestimation of the effectiveness of current defenses. In this paper, we bridge the gap by introducing LongPIBench, a long-context benchmark for prompt injection covering 4 realistic application scenarios: paper peer review, resume screening, code review, and email summary. For each scenario, we construct a synthetic dataset and a real-world dataset, with context lengths ranging from thousands to tens of thousands of tokens. The evaluation results on LongPIBench reveal significant vulnerabilities of prompt injection defenses under long-context settings: even simple heuristic prompt injection attacks achieve high success rates and frequently bypass state-of-the-art defenses. We hope LongPIBench can serve as a practical benchmark for systematically evaluating prompt injection defenses in realistic long-context scenarios.

---


### 10. [Logos: An Agent Harness on a Cross-Process Bus](https://arxiv.org/abs/2608.28553)

**<font color=#1a73e8>作者：</font>** Hanzhang Jia, Liheng Zeng, Hao Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
